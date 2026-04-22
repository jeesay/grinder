/**
 * dataviz.js
 * ----------
 * Manage DataViz tab for a job.
 * Each graphs has "chart-card" with :
 *   - header  : title
 *   - body    : graph ECharts
 *
 * prerequisites :
 *   <script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
 *
 * prerequisite importmap :
 *   "apache-arrow": "https://esm.sh/apache-arrow@19.0.0"
 *   "arquero":      "https://esm.sh/arquero@7"
 */

// import { tableFromIPC } from 'apache-arrow';
// import * as aq           from 'arquero';

'use strict';

import { h } from "./dom.js";


// ─── WebSocket /ws/dataviz ────────────────────────────────────────────────────

/**
 * Ask to server to convert .star to .parquet if needed,
 * then, send data in Arrow IPC.
 *
 * @param {string}   jobId      ex: "MotionCorr/job002"
 * @param {string}   sourceFile ex: "corrected_micrograph.star"
 * @param {Function} onData     callback(arqueroTable)
 */
function _fetchData(jobId, sourceFile, onData) {
    const connectEl = document.getElementById('connect');
    const ip   = connectEl.dataset.ip;
    const port = connectEl.dataset.port;

    const socket = new WebSocket(`ws://${ip}:${port}/ws/dataviz`);
    socket.binaryType = 'arraybuffer';

    socket.onopen = () => {
        const request = `get_data:${jobId}:${sourceFile}`;
        console.info(`[dataviz] → ${request}`);
        socket.send(request);
    };

    socket.onmessage = (event) => {
        // Erreur serveur (JSON texte)
        if (typeof event.data === 'string') {
            console.error('[dataviz] Erreur serveur :', JSON.parse(event.data).error);
            return;
        }
        // Binary data Arrow IPC
        try {
            const arrowTable = tableFromIPC(event.data);
            const dt         = aq.fromArrow(arrowTable);
            console.info(`[dataviz] ${dt.numRows()} lignes | colonnes :`, dt.columnNames());
            onData(dt);
        } catch (err) {
            console.error('[dataviz] Erreur Arrow/Arquero :', err);
        }
    };

    socket.onerror = err  => console.error('[dataviz] WS erreur :', err);
    socket.onclose = ()   => console.info('[dataviz] WS fermé');
}


// ─── Pipeline Arquero ─────────────────────────────────────────────────────────

/**
 *
 * @param {aq.Table} dt
 * @param {string}   colName
 * @param {number}   nBins
 * @returns {{ x0: number, x1: number, count: number }[]}
 */
function _buildHistogramBins(dt, colName, nBins = 50) {
    const values = Array.from(dt.array(colName))
        .filter(v => v != null && !isNaN(v))
        .map(Number);

    if (!values.length) return [];

    const min  = Math.min(...values);
    const max  = Math.max(...values);
    const step = (max - min) / nBins || 1;

    const bins = Array.from({ length: nBins }, (_, i) => ({
        x0: min + i * step,
        x1: min + (i + 1) * step,
        count: 0
    }));

    for (const v of values) {
        const idx = Math.min(Math.floor((v - min) / step), nBins - 1);
        bins[idx].count++;
    }

    return bins;
}


/**
 * Initialise l'instance ECharts dans un container.
 *
 * @param {HTMLElement} container
 * @param {{ x0, x1, count }[]} bins
 * @param {string} xLabel
 * @param {string} yLabel
 * @returns {echarts.ECharts}
 */
function _initChart(container, bins, xLabel, yLabel) {
    const chart = echarts.init(container, null, { renderer: 'canvas' });

    chart.setOption({
        backgroundColor: 'transparent',
        grid:   { left: 60, right: 20, top: 20, bottom: 60 },
        tooltip: {
            trigger:   'axis',
            formatter: params => {
                const b = bins[params[0].dataIndex];
                return `${b.x0.toFixed(2)} – ${b.x1.toFixed(2)}<br/>Count : ${b.count}`;
            }
        },
        xAxis: {
            type:         'category',
            data:          bins.map(b => ((b.x0 + b.x1) / 2).toFixed(2)),
            name:          xLabel,
            nameLocation: 'middle',
            nameGap:       40,
            axisLabel:     { rotate: 30, fontSize: 10 }
        },
        yAxis: {
            type:         'value',
            name:          yLabel || 'Count',
            nameLocation: 'middle',
            nameGap:       45
        },
        series: [{
            type:     'bar',
            data:      bins.map(b => b.count),
            barWidth: '99%',
            emphasis: { itemStyle: { opacity: 0.8 } }
        }]
    });

    window.addEventListener('resize', () => chart.resize());
    return chart;
}


// ─── Construction de la chart-card ────────────────────────────────────────────

/**
 * Crée et retourne une chart-card DOM complète.
 *
 * @param {object} config   widget _motion parsé depuis le .star
 * {
 *   id:         "totalmotion",
 *   label:      "Total motion per micrographs",
 *   widget:     "histogram",
 *   default:    "30",          ← threshold
 *   arg0:       "corrected_micrograph.star",
 *   arg1:       "data_micrographs",
 *   arg2:       "rnlAccumMotionTotal #5",
 *   constraint: "Total Motion (Å)",
 *   help:       "?"
 * }
 * @returns {HTMLElement}
 */
function _buildCard(config) {
    const threshold = parseFloat(config.default) || 30;

    // ── Squelette HTML ────────────────────────────────────────────────────────
    const card = document.createElement('div');
    card.className  = 'chart-card';
    card.dataset.id = config.id;

    card.innerHTML = `
        <div class="chart-header">
            <span>${config.label}</span>
            <span class="badge" id="badge-${config.id}">${threshold} Å</span>
        </div>
        <div class="chart-body">
            <div class="chart-canvas" id="canvas-${config.id}" style="width:100%;height:320px;"></div>
        </div>`;

    return card;
}

/**
 * Branche les données et les événements sur une chart-card déjà dans le DOM.
 *
 * @param {HTMLElement} card
 * @param {object}      config
 * @param {aq.Table}    dt
 */
function _wireCard(card, config, dt) {
    const colName   = config.arg2;
    const xLabel    = config.constraint !== '?' ? config.constraint : config.label;
    const yLabel    = 'Count';
    const bins      = _buildHistogramBins(dt, colName);
    let   threshold = parseFloat(config.default) || 30;

    const canvasEl  = card.querySelector(`#canvas-${config.id}`);
    const badgeEl   = card.querySelector(`#badge-${config.id}`);


    // Init chart
    const chart = _initChart(canvasEl, bins, xLabel, yLabel);
    _updateChart(chart, bins, threshold, xLabel, yLabel);

    // Init stats
    const updateStats = (t) => {
        const s      = _computeStats(dt, colName, t);
        keepEl.textContent   = s.keep;
        rejectEl.textContent = s.reject;
    };
    updateStats(threshold);

    // Slider interactif
    sliderEl.addEventListener('input', (ev) => {
        threshold          = parseFloat(ev.target.value);
        badgeEl.textContent = `${threshold} Å`;
        _updateChart(chart, bins, threshold, xLabel, yLabel);
        updateStats(threshold);
    });
}


// ─── Point d'entrée ───────────────────────────────────────────────────────────

/**
 * Initialise la DataViz pour un job donné.
 * Crée une grille de chart-cards dans le tab-content DataViz.
 *
 * @param {string}      jobId      ex: "MotionCorr/job001"
 * @param {object[]}    cards      widgets enfants de la card (depuis _motion, _defocus...)
 * @param {HTMLElement} container  div .tab-content de l'onglet DataViz
 */
export function initDataviz(jobId, cards, container) {
    if (!container) {
        console.error('[dataviz] Container introuvable');
        return;
    }

    // Vider et créer la grille
    container.innerHTML = '';
    const grid = document.createElement('div');
    grid.className = 'charts-grid';
    container.appendChild(grid);

    // Pour chaque widget enfant de la card
    for (const config of cards) {
        if (config.widget !== 'histogram') {
            console.warn(`[dataviz] Widget non supporté : ${config.widget}`);
            continue;
        }

        // 1. Construire la card DOM
        const card = _buildCard(config);
        grid.appendChild(card);

        // 2. Afficher un loader
        card.querySelector(`#canvas-${config.id}`).innerHTML =
            `<div class="dataviz-loading"><i class="bi bi-hourglass-split"></i> Chargement...</div>`;

        // 3. Récupérer les données et brancher
        _fetchData(jobId, config.arg0, (dt) => {
            _wireCard(card, config, dt);
        });
    }
}

export function g_graphics(desc) {
    // grid: ncols,nrows????
    console.info("GRAPHIC", desc);
    const canvas = h(
        `canvas#${desc.id}.${desc.widget}`,
        { 
            attrs: {width:200,height:100},
            on: {change: (ev) => console.log('change')}
        }
    )
    return canvas;
}