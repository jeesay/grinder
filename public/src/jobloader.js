/**
 * jobLoader.js
 * ------------
 * Charge un job existant depuis un job.star reçu via WebSocket.
 *
 * Prérequis :
 *   - buildSidebar() a déjà tourné → localStorage contient les .star de définition
 *     ex: localStorage["relion.motioncorr.own"] = JSON.stringify(source)
 *
 * Flux :
 *   job.star (string brut)
 *       → parseJobStar()          extraire procLabel + Map<variable, value>
 *       → localStorage.getItem()  récupérer le .star de définition de l'outil
 *       → injectValuesIntoDB()    injecter les valeurs dans les datablocks
 *       → build_widget_tree()     construire l'arbre de widgets avec les valeurs
 *       → w_tab_tools()           afficher dans #main-panel
 *
 * Usage :
 *   import { loadJobFromStar } from './jobLoader.js';
 *
 *   socket.onmessage = (event) => {
 *       const msg = JSON.parse(event.data);
 *       if (msg.action === 'job_params') {
 *           loadJobFromStar(msg.data);
 *       }
 *   };
 */

import {  w_tab_tools } from './widget.js';
import { build_widget_tree } from './main.js'


// ─── 1. Parser le job.star ────────────────────────────────────────────────────

/**
 * Parse le contenu brut d'un job.star.
 *
 * @param {string} raw  contenu brut du job.star
 * @returns {{ procLabel: string, values: Map<string, string> } | null}
 *
 * Exemple de retour :
 * {
 *   procLabel : "relion.motioncorr.own",
 *   values    : Map {
 *     "bfactor"    => "150",
 *     "gain_flip"  => "No flipping (0)",
 *     "nr_threads" => "60",
 *     ...
 *   }
 * }
 */
export function parseJobStar(raw) {
    if (!raw) return null;

    const lines = raw
        .split('\n')
        .map(l => l.trim())
        .filter(l => l.length > 0 && !l.startsWith('#'));

    // ── Extract _rlnJobTypeLabel ─────────────────────────────────────────────
    let procLabel = null;
    for (const line of lines) {
        if (line.startsWith('_rlnJobTypeLabel')) {
            // ex: "_rlnJobTypeLabel             relion.motioncorr.own"
            const parts = line.split(/\s+/);
            if (parts.length >= 2) {
                procLabel = parts[1].trim();
                break;
            }
        }
    }

    if (!procLabel) {
        console.error('[jobLoader] _rlnJobTypeLabel not found in job.star');
        return null;
    }

    // ── Extraire les paires variable / value ──────────────────────────────────
    const values = new Map();
    let inJobOptions = false;
    let inLoop       = false;

    for (const line of lines) {
        if (line === 'data_joboptions_values') { inJobOptions = true;  continue; }
        if (inJobOptions && line === 'loop_')  { inLoop       = true;  continue; }

        // Ignorer les declarations de colonnes
        if (inLoop && line.startsWith('_rln')) continue;

        // Parser les paires variable / value
        if (inJobOptions && inLoop) {
            const parsed = _parseValueLine(line);
            if (parsed) values.set(parsed.variable, parsed.value);
        }
    }

    console.info(`[jobLoader] procLabel = ${procLabel} | ${values.size} valeurs parsees`);
    return { procLabel, values };
}


/**
 * Parse une ligne "variable  value" du bloc joboptions_values.
 * Gere les valeurs entre guillemets simples/doubles et les valeurs sans guillemets.
 *
 * ex: "   bfactor        150 "          => { variable: "bfactor",    value: "150" }
 * ex: ' fn_gain_ref         "" '        => { variable: "fn_gain_ref", value: "" }
 * ex: ' gain_flip "No flipping (0)" '   => { variable: "gain_flip",   value: "No flipping (0)" }
 *
 * @param   {string} line
 * @returns {{ variable: string, value: string } | null}
 */
function _parseValueLine(line) {
    const trimmed = line.trim();
    if (!trimmed) return null;

    // Capturer : <variable> <"valeur entre guillemets" ou valeur_simple>
    const match = trimmed.match(/^(\S+)\s+(".*?"|'.*?'|\S+)$/);
    if (!match) return null;

    const variable = match[1];
    let   value    = match[2];

    // Retirer les guillemets englobants
    if ((value.startsWith('"') && value.endsWith('"')) ||
        (value.startsWith("'") && value.endsWith("'"))) {
        value = value.slice(1, -1);
    }

    return { variable, value };
}


// ─── 2. Injecter les valeurs dans les datablocks ──────────────────────────────

/**
 * Injecte les valeurs du job dans la structure datablocks recuperee du localStorage.
 * Cherche dans chaque datablock la colonne "id" et met a jour la colonne "default"
 * si l'id correspond a une variable du job.
 *
 * @param {object}             datablocks  datablocks parses (depuis localStorage)
 * @param {Map<string,string>} values      Map variable => value
 * @returns {object}  datablocks mutes avec les valeurs injectees
 */
function injectValuesIntoDB(datablocks, values) {
    if (!datablocks || !values.size) return datablocks;

    for (const blockKey of Object.keys(datablocks)) {
        const block = datablocks[blockKey];
        if (!block?.table?.rows || !block?.table?.header) continue;

        const header = block.table.header;
        const rows   = block.table.rows;

        const idIdx      = header.indexOf('id');
        const defaultIdx = header.indexOf('default');

        if (idIdx === -1 || defaultIdx === -1) continue;

        for (const row of rows) {
            const fieldId = row[idIdx];
            if (values.has(fieldId)) {
                const newVal = values.get(fieldId);
                row[defaultIdx] = newVal;
                console.info(`[jobLoader] Inject : ${fieldId} = ${newVal}`);
            }
        }
    }

    return datablocks;
}


// ─── 5. Utilitaire : extraire le bloc _dataviz ────────────────────────────────

/**
 * Extrait la liste des configs dataviz depuis le localStorage pour le procLabel actif.
 * Cherche le datablock dont les rows contiennent la colonne "source_file".
 *
 * @returns {object[]}  tableau de configs dataviz, ex:
 * [{
 *   id:                "totalmotion",
 *   label:             "Total motion per micrographs",
 *   widget:            "histogram",
 *   source_file:       "corrected_micrograph.parquet",
 *   data_key:          "data_micrographs",
 *   type:              "histogram",
 *   x_col:             "rnlAccumMotionTotal #5",
 *   x_label:           "Total Motion (Å)",
 *   y_col:             "?",
 *   y_label:           "Count",
 *   threshold_default: "30"
 * }]
 */
export function getDatavizConfig() {
    const section   = document.getElementById('main-panel');
    const procLabel = section?.dataset?.procLabel;

    if (!procLabel) {
        console.error('[jobLoader] Aucun procLabel actif sur #main-panel');
        return [];
    }

    const serialized = localStorage.getItem(procLabel);
    if (!serialized) {
        console.error(`[jobLoader] localStorage vide pour : ${procLabel}`);
        return [];
    }

    let db;
    try {
        db = JSON.parse(serialized);
    } catch (e) {
        console.error('[jobLoader] Erreur parsing localStorage :', e);
        return [];
    }

    // Chercher le datablock "dataviz" — celui dont le header contient "source_file"
    const datablocks = db.datablocks;
    for (const key of Object.keys(datablocks)) {
        const block  = datablocks[key];
        const header = block?.table?.header ?? [];
        if (!header.includes('source_file')) continue;

        // Convertir les rows en objets
        return block.table.rows.map(row => {
            const obj = {};
            header.forEach((col, i) => { obj[col] = row[i]; });
            return obj;
        });
    }

    console.warn('[jobLoader] Bloc dataviz introuvable pour :', procLabel);
    return [];
}


/**
 * Point d'entree principal.
 * Recoit le contenu brut du job.star (depuis WebSocket),
 * reconstruit le formulaire avec les valeurs du job et l'affiche dans #main-panel.
 *
 * @param {string} rawStarContent  contenu brut du job.star recu via WebSocket
 * @returns {boolean}  true si succes, false si erreur
 */
export function loadJobFromStar(rawStarContent, jobId = '') {
    // 1. Parser le job.star
    const parsed = parseJobStar(rawStarContent);
    if (!parsed) return false;

    const { procLabel, values } = parsed;

    // 2. Recuperer le .star de definition depuis localStorage
    const serialized = localStorage.getItem(procLabel);
    if (!serialized) {
        console.error(`[jobLoader] Outil non trouve dans localStorage : "${procLabel}"`);
        console.info('[jobLoader] Cles disponibles :', Object.keys(localStorage));
        return false;
    }

    // 3. Parser le JSON stocke
    let db;
    try {
        db = JSON.parse(serialized);
    } catch (e) {
        console.error('[jobLoader] Erreur parsing localStorage :', e);
        return false;
    }

    // 4. Injecter les valeurs dans les datablocks
    injectValuesIntoDB(db.datablocks, values);

    // 5. Construire l'arbre de widgets avec les valeurs injectees
    const widgets = build_widget_tree(db.datablocks.default, { children: [] });

    // 6. Afficher dans #main-panel (meme logique que le clic sur un outil)
    const section = document.getElementById('main-panel');
    section.innerHTML = '';
    w_tab_tools(section, widgets);
    section.style.display = 'block';
    section.querySelector('input').checked = true;

    // 7. Stocker le contexte actif pour get_dataviz
    section.dataset.procLabel = procLabel;
    section.dataset.jobId     = jobId;

    console.info(`[jobLoader] Job charge : ${procLabel}`);
    return true;
}