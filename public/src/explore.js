/**
 * explore.js
 * ----------
 * Gère le panneau de droite "Jobs" :
 *   - Connexion WebSocket sur /ws/explore
 *   - Récupération et affichage de la liste des jobs
 *   - Clic sur un job → récupération du job.star → reconstruction du formulaire
 *
 * Protocole (texte brut, cohérent avec /ws/file-tree) :
 *   Client → "job_list"                     Serveur → JSON arbre des jobs
 *   Client → "job_params:MotionCorr/job001" Serveur → JSON { job_id, data }
 *
 * Usage (dans index.html) :
 *   import { initExplore } from './src/explore.js';
 *   initExplore();
 */

import { loadJobFromStar } from './jobloader.js';

// ─── État du module ───────────────────────────────────────────────────────────

let _socket = null;


// ─── Connexion WebSocket ──────────────────────────────────────────────────────

function _connect() {
    const connectEl = document.getElementById('connect');
    const ip   = connectEl.dataset.ip;
    const port = connectEl.dataset.port;

    _socket = new WebSocket(`ws://${ip}:${port}/ws/explore`);

    _socket.onopen = () => {
        console.info('[explore] WebSocket connecté');
        _socket.send('job_list');    // texte brut, comme /ws/file-tree
    };

    _socket.onmessage = (event) => {
        let data = JSON.parse(event.data);
        console.info('[explore] Message reçu :', data);
        if (typeof data === 'string') {
                data = JSON.parse(data);
            }

        _onMessage(data);
    };

    _socket.onerror = (err) => {
        console.error('[explore] WebSocket erreur :', err);
    };

    _socket.onclose = () => {
        console.info('[explore] WebSocket fermé');
        _socket = null;
    };
}


// ─── Dispatcher des messages entrants ────────────────────────────────────────

function _onMessage(data) {
    // Erreur serveur
    if (data.error) {
        console.error('[explore] Erreur serveur :', data.error);
        return;
    }

    // Réponse job_params → { job_id, data }
    if (data.job_id && data.data) {
        loadJobFromStar(data.data, data.job_id);
        return;
    }

    // Réponse job_list → arbre { name: "root", type: "folder", children: [...] }
    if (data.type === 'folder' && data.name === 'root') {
        _renderJobList(data);
        return;
    }

    // Fallback : si children présent à la racine, c'est quand même un arbre
    if (data.children) {
        _renderJobList(data);
        return;
    }

    console.warn('[explore] Message non reconnu :', data);
}


// ─── Affichage de la liste des jobs ──────────────────────────────────────────

/**
 * Construit la liste des jobs dans #joblist.
 *
 * Structure attendue (retournée par build_relion_tree) :
 * {
 *   name: "root",
 *   children: [
 *     {
 *       name: "MotionCorr",
 *       children: [
 *         { name: "job001", label: "relion.motioncorr.own", parent: "MotionCorr" },
 *         ...
 *       ]
 *     },
 *     ...
 *   ]
 * }
 *
 * @param {object} data  arbre retourné par le serveur
 */
function _renderJobList(data) {
    const joblist = document.getElementById('joblist');
    joblist.innerHTML = '';

    if (!data?.children?.length) {
        joblist.innerHTML = '<li class="nav-empty">Aucun job trouvé</li>';
        return;
    }

    for (const jobType of data.children) {

        // ── Dossier parent (ex: Import, MotionCorr...) ────────────────────────
        const li = document.createElement('li');
        li.className = 'menu-item';

        const header = document.createElement('a');
        header.className = 'nav-row nav-group';
        header.innerHTML = `<i class="nav-icon bi bi-folder2"></i>
                            <span class="nav-text">${jobType.name}</span>`;
        li.appendChild(header);

        // ── Jobs enfants (ex: job001, job008...) ──────────────────────────────
        if (jobType.children?.length) {
            const ul = document.createElement('ul');
            ul.className = 'submenu';

            for (const job of jobType.children) {
                // Le label est sur le premier enfant (fichier .star)
                const label = job.children?.[0]?.label ?? '';

                const jobLi = document.createElement('li');
                jobLi.className = 'menu-item job-item';

                const jobLink = document.createElement('a');
                jobLink.className = 'nav-row';
                jobLink.dataset.jobId    = `${jobType.name}/${job.name}`;
                jobLink.dataset.jobLabel = label;
                jobLink.innerHTML = `<i class="nav-icon bi bi-cpu"></i>
                                     <span class="nav-text">${job.name}</span>
                                     <span class="nav-label">${jobType.name}</span>`;

                jobLink.addEventListener('click', _onJobClick);

                jobLi.appendChild(jobLink);
                ul.appendChild(jobLi);
            }

            li.appendChild(ul);
        }

        joblist.appendChild(li);
    }
}


// ─── Clic sur un job ─────────────────────────────────────────────────────────

function _onJobClick(ev) {
    const el    = ev.currentTarget;
    const jobId = el.dataset.jobId;
    if (!jobId) return;

    // Highlight
    document.querySelectorAll('#joblist .job-item a')
        .forEach(a => a.classList.remove('active'));
    el.classList.add('active');

    // Mettre à jour la navbar
    const jobEl = document.querySelector('#job_id span');
    if (jobEl) jobEl.textContent = jobId;

    // Envoyer la requête au serveur (texte brut)
    const request = `job_params:${jobId}`;

    if (!_socket || _socket.readyState !== WebSocket.OPEN) {
        console.warn('[explore] WebSocket non connecté, reconnexion...');
        _connect();
        _socket.addEventListener('open', () => {
            _socket.send(request);
        }, { once: true });
        return;
    }

    console.info(`[explore] → ${request}`);
    _socket.send(request);
}


// ─── Point d'entrée ───────────────────────────────────────────────────────────

/**
 * Initialise le panneau explore.
 * À appeler une fois que ip/port sont définis dans dataset de #connect.
 */
export function initExplore() {
    _connect();
}