'use strict';

import { h } from "./dom.js";

export function log_append(text, isSystem = false) {
    console.info('log_append',text);
    const div = document.querySelector('#Log .tab-content');
    // div.className = isSystem ? 'log-line system-msg' : 'log-line';
    const timestamp = new Date().toLocaleTimeString();
    const row = h('pre.log-row',text);
    div.appendChild(row);
    
    // Auto-scroll
    // terminal.scrollTop = terminal.scrollHeight;
}