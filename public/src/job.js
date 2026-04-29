//  GRINDER - Graphical user interface of RelIoN and DataminER
//  Copyright (C) 2023-2026  Jean-Christophe Taveau
//
//  This file is part of GRINDER
//
// This program is free software: you can redistribute it and/or modify it
// under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with GRINDER. If not, see <http://www.gnu.org/licenses/>.


'use strict';

import {StarGate} from "./stargate.js";
import { h } from './dom.js';
import {w_alert, w_leftpanel, w_tab_tools} from "./widget.js";
import { read_job } from "./main.js"

/* Obsolete */
const set_job_params = (gui,json) => {
  // Check button in first tab (Tools)
  if (document.querySelector(`#${gui.tool}`)) {
      document.querySelector(`#${gui.tool}`).checked = true;
  }
  // Step #1: Get params and create the other tabs
  json.cli.forEach( cli => {
    const script = cli.script[0];
    const args = Object.keys(script.options).reduce( (accu,key) => `${accu} ${key} ${script.options[key]}\n`, '');

    // Update `Check command`
    document.querySelector('#relion_cli').appendChild(
      h('pre',`${cli.script[0].command}\n${args}`)
    );
    gui.update(args);
  });
  // Set the values in various tabs
  json.cli.forEach( cli => {
    const script = cli.script[0];
    Object.keys(cli.script[0].options).forEach(key => {
      console.log(key);
      let els = document.querySelectorAll(`[data-option~='${key}']`);
      if (els) {
        console.log('Set...',key,cli.script[0].options[key]);
        els.forEach(el => {
          if (el.type === 'checkbox') {
            el.checked = cli.script[0].options[key];
          }
          else {
            el.value = cli.script[0].options[key];
            const len = el.value.length;
              
            // Mostly for Web Browsers
            if (el.setSelectionRange) {
                el.focus();
                el.setSelectionRange(len, len);
            }
          }
        });
      }
    })
  });
}

/* Obsolete ? */
const view_job = async (ev) => {
  // From `job.json`
  const jinfo = ev.target.parentNode.dataset;
  const gui = jobtypes.filter( (j) => j.type === jinfo.jtype)[0];
  console.log(gui);
  // Reset
  document.querySelectorAll('aside ul li').forEach(ww => ww.classList.remove('active'));
  //
  const w = document.querySelector(`aside #${gui.widget}`);
  w.classList.add('active');
  // Create empty menus
  w_navtab(document.querySelector('section'),gui.main_panel());
  // Ask for the various parameters of this job
  GRINDER.server.send(
    JSON.stringify(
      {
        action: {
          tool: 'GET',
          source:'project',
          args:`${jinfo.jpath}/job.json`
        }
      }
    )
  );
  const response = await GRINDER.server.receive();
  // Set the various parameters
  set_job_params(gui,JSON.parse(response));
}

/* Obsolete ? */
const duplicate_job = (ev) => {
  // Lazy copy. Just, get a new alias jobname.
  console.log(ev.target.dataset);
}

/* Utility functions for creating the various job menus */

const fetchFile = async filename => {
  const file = await fetch(filename);
  const text = await file.text();
  
  const obj = new StarGate();
  obj.parseSTAR(text);
  return obj.blocks();
}

const from_startable = (data) => data.rows.map( (row) => {
    const gs = ['program','toolmenu','tabgroup','tab',
      'select_g', 'option_g', 'fieldset', 'grid',
      'switch','details','dropdown','cli', 'toolbar','select'
    ];
    let obj = {};
    for (let h in data.header) {
      obj[data.header[h]] = row[h];
    }
    if (gs.includes(obj.widget)) {
      obj.children = [];
    }
    return obj;
  });

const is_table = (el) => typeof el == 'object' && 'header' in el;

const get_tables = (star) => Object.keys(star).filter(key => is_table(star[key])).map(key => ({key,table:star[key]}));

const flat_tables = (tables) => {
  // Convert each table into object
  let flat_table = tables.map(t => {
    let rows = from_startable(t.table);
    rows.forEach(row => row.parent = t.key );
    return rows // {key: t.key,table: rows}
  }).flat();
  // flat_table = [{id:'tabs',children:[]},...flat_table];
  return flat_table;
}

export const build_widget_tree = (datablock,parent) => {
  // Get all tables and build hierarchy
  let tables = get_tables(datablock);
  let flat_table = flat_tables(tables);
  let tab_count = 1;
  flat_table.forEach(wdgt => {
    console.info(wdgt);
    if (wdgt.id !== undefined && wdgt.id.includes('>')) {
      [wdgt.id,wdgt.on_change] = wdgt.id.split('>');
    }
    // Attach the tab to the `parent`
    if (wdgt.widget == 'tab') {
      // wdgt.parent = db.id;
      wdgt.index = tab_count;
      // wdgt.toolsetid = parent.id;
      tab_count++;
      parent.children.push(wdgt);
    }
    else if (wdgt.id !== undefined && (['option','option_g'].includes(wdgt.widget) || wdgt.widget.slice(0,2) === 'g_')) {
      const [parent,child] = wdgt.id.split('::');
      wdgt.id = child;
      wdgt.parent = parent;
      const index = flat_table.map(e => e.id).indexOf(wdgt.parent);
      console.info('OOOPPPPTION',index,flat_table[index]);
      flat_table[index].children.push(wdgt);
    }
    else if ('parent' in wdgt) {
      // Update toolset info
      // wdgt.toolsetid = parent.id;
      // Attach other widgets depending of their parent.
      const index = flat_table.map(e => e.id).indexOf(wdgt.parent);
      console.info(wdgt);
      flat_table[index].children.push(wdgt);
    }
  });
  return parent;
}

/**
 * Generate the HTML widgets for the left sidebar containing all the various cryoEM/SPA tools gui
 * 
 * @param {*} filename 
 */
export const buildSidebar = async filename => {
  // Load and parse `grinder_spa.star`
  const file = await fetch(filename);
  const text = await file.text();
  
  const obj = new StarGate();
  obj.parseSTAR(text);
  const left_panel = obj.datablock('grinder_spa').table('tool_panel');
  console.info('PANEL',left_panel);
  // Create items in left panel
  w_leftpanel(document.querySelector('aside.tools nav ul'),left_panel);
  // Create Tools panel
  let tools = [];
  let tab_count = 1;
  for (let tab of left_panel) {
    console.info('Tab Data',tab);
    // tab.path = 'spa/'+ tab.starfile.split('/')[0] + '/' //HACK
    const _tmp = await fetchFile(tab.path + tab.starfile);
    let db = _tmp.datablocks.default;
    console.log('SUBMENU',db);
    // Get all tables and build hierarchy
    let tables = get_tables(db);
    let flat_table = flat_tables(tables);
    flat_table.forEach(async wdgt => {
      console.log('WIDGET',wdgt);
      if (wdgt.widget === 'submenu') {
        const parent = document.getElementById(tab.id);
        let ul = parent.querySelector('ul');
        if ( ul === null) {
          ul = h('ul.submenu');
          parent.appendChild(ul);
        }
        // Create child
        const w = h('li',[
              h('a',[
                h(`i.nav-icon.bi.${wdgt.icon}`),
                h('span.nav-text',wdgt.label)
              ]),
              h(`ul#${wdgt.id}.sub-submenu`)
            ]);
        ul.appendChild(w);
      }
      else if (wdgt.widget === 'tool') {
        // Load tool
        const source = await fetchFile(tab.path + wdgt.filename);
        const serialized = JSON.stringify(source);
        localStorage.setItem(wdgt.proc_label,serialized);

        const parent = document.getElementById(wdgt.parent);
        // Create child/tab
        const w = h('li',
          [
            h('a',
              {
                dataset: {
                  proclabel: wdgt.proc_label,
                },
                on: {
                  click: (ev) => {
                    if (document.getElementById('connect').dataset.projpath) {
                      const ui = ev.target.parentElement.dataset.proclabel;
                      document.getElementById('job_id').dataset.nodetype = ui;
                      console.info('BUILD TABS',ui);                      
                      console.info('BUILD TABS',localStorage.getItem(ui));
                      const db = JSON.parse(localStorage.getItem(ui));
                      const widgets = build_widget_tree(db.datablocks.default,{children:[]});
                      // Section
                      let section = document.getElementById('main-panel');
                      section.innerHTML = '';
                      w_tab_tools(section,widgets);
                      // Reset display
                      section.style.display = 'block';
                      section.querySelector('input').checked = true; // First child
                      // Update job_toolbar
                      document.querySelector('#job_id span').textContent = 'New Job';
                      update_job_toolbar('new_job');
                    }
                    else {
                      w_alert('No Project found...Please connect to the grinder server and choose a RELION Project');
                    }
                  }
                }
              },
              [
                h('span.nav-text',wdgt.label),
                h('i.nav-icon.bi.bi-question-circle',
                  {
                    attrs:{title: wdgt.help}
                  }
                )
              ]
            )
          ]);
        parent.appendChild(w);
      }
      else if (wdgt.widget == 'menu-item') {
        console.info('MENU-ITEM',wdgt);
        // Load radio_tool (radio button + toolset)
        const source = await fetchFile(tab.path + wdgt.filename);
        const serialized = JSON.stringify(source);
        localStorage.setItem(wdgt.proc_label,serialized);
        const parent = document.querySelector(`#${wdgt.ancestor} a`);
        parent.dataset.proclabel = wdgt.proc_label;
        console.info('PARENT',parent);
        parent.addEventListener('click', (ev) => {
            console.log('CLICK',ev.target);
            const ui = ev.target.parentElement.dataset.proclabel;
            console.info('BUILD TABS',ui);                      
            console.info('BUILD TABS',localStorage.getItem(ui));
            const db = JSON.parse(localStorage.getItem(ui));
            const widgets = build_widget_tree(db.datablocks.default,{children:[]});
            // Section
            let section = document.getElementById('main-panel');
            section.innerHTML = '';
            w_tab_tools(section,widgets);
            // Reset display
            section.style.display = 'block';
            section.querySelector('input').checked = true; // First child
          }
        );
      }
    });
  }
}

/* Right sidebar */

function* chunks(arr, n) {
  console.log(arr.length);
  let chunk = [];
  let index = n;
  for (let i = 0; i < arr.length; i++) {
    console.info('index', parseInt(arr[i][0].match(/\d+/)));
    if (parseInt(arr[i][0].match(/\d+/)) <= index) {
      chunk.push(arr[i]);
    }
    else {
      yield chunk;
      index += n;
      chunk = [arr[i]];
    }
  }
  yield chunk;
}

export const update_right_sidebar = (project_path,data_proj) => {

  const new_item = (item, parent, type = 'list') => {
    const projpath = document.getElementById('connect').dataset.projpath;
    const [job, alias, nodetype, status, path, fn] = item;

    const _read = (ev) => {
      const jb = document.getElementById('job_id');
      jb.dataset.projpath = projpath; 
      jb.dataset.path = path;
      jb.dataset.job = job;
      jb.dataset.nodetype = nodetype; // TODO: Here is the label from RELION but not from GRINDER
      document.querySelector('#job_id span').textContent = `${path}/${job}`;
      update_job_toolbar('read_job');
      return read_job({projpath,path,job});
    }
    
    const w = h('li.file-item',
      {
        dataset: { job: fn, proclabel: nodetype },
        on: { click: _read }
      },
      [h('a',
        [
          h('i.nav-icon.bi.bi-gear', { style: { color: (status === 'Succeeded') ? '#0f0' : '#f00' } }),
          h('span.nav-text', (type === 'list') ? fn : job)
        ])
      ]
    );
    parent.appendChild(w)
  }


  const new_menu = (arr, parent, index, N) => {
    const w = h('li.menu-item', {},
      [
        h('a',
          [
            h(`i.nav-icon.bi.bi-${index % 10}-circle`),
            h('span.nav-text', `Jobs ${index * N + 1}-${(index + 1) * N}`)
          ]
        ),
        h('ul.sub-submenu')
      ]);

    parent.appendChild(w);
    arr.forEach(job => {
      const [fn, alias, nodetype, status] = job;
      const [path, jobi, ...dummy] = fn.split('/');
      new_item([jobi, alias, nodetype, status, path, `${path}/${jobi}`], w.children[1])
    });
  }
  
  // Step #1 - Update project
  document.querySelector('#project_id span').textContent = project_path;
  // Step #2 - Fill the Job List
  let parent = document.querySelector('.jobs #joblist');
  // Reset
  parent.innerHTML='';
  const N = 10;
  chunks(data_proj.processes.data, N).forEach((chunk, i) => new_menu(chunk, parent, i, N));
  // Step #3 - Fill the Job Folders
  parent = document.querySelector('.jobs #jobfolder');
  // Reset
  parent.innerHTML='';
  const folders = data_proj.processes.data.reduce((accu, item) => {
    const [fn, alias, nodetype, status] = item;
    const [path, job, ...dummy] = fn.split('/');
    if (path in accu) {
      accu[path].push([job, alias, nodetype, status, path, `${path}/${job}`]);
    }
    else {
      accu[path] = [[job, alias, nodetype, status, path, `${path}/${job}`]];
    }
    return accu;
  }, {});
  Object.entries(folders).forEach(pair => {
    const [folder, jobs] = pair;
    const w = h('li.menu-item', {},
      [
        h('a',
          [
            h(`i.nav-icon.bi.bi-folder2-open`),
            h('span.nav-text', folder)
          ]
        ),
        h('ul.sub-submenu')
      ]);
    parent.appendChild(w);
    jobs.forEach(job => new_item(job, w.children[1],'folder'));
  });
}

/* Toolbar management functions */

/* Creating the job toolbar */
const job_toolbar = (desc) => {
  const tools = ['job_run' , 'job_stop', 'job_cont', 'job_schd', 'job_dupl' , 'job_mod', 'job_rm'];
  const status = ['job_lock', 'job_running', 'job_pending'];
  const tools_elements = tools.map( (t) => h(
    `li#${t}.job_action`,
      [
        h('a',{attrs: {href:'#'}},
          [
            h('i.nav-icon.bi.bi-send',{attrs: {title: 'Run Job'}})
          ]
        )
      ]
    )
  );

  const status_elements = status.map( (t) => h(
    `li#${t}.job_status`,
      [
        h('a',{attrs: {href:'#'}},
          [
            h('i.nav-icon.bi.bi-send',{attrs: {title: 'Run Job'}})
          ]
        )
      ]
    )
  );

  return h('div.actions',
    [
      h('ul',[...tools_elements, ...status_elements])
    ]
  );
};

/* Update toolbar icons depending of a scenario `unconnected`, `new_job`, `read_job`, etc.  */
export const update_job_toolbar = (scenario) => {
  const scenarii = {
    unconnected: {
      'job_run': 'hidden' , 'job_stop': 'hidden', 'job_cont': 'hidden', 'job_schd': 'hidden', 'job_dupl': 'hidden' , 
      'job_mod': 'hidden', 'job_rm': 'hidden', 
      'job_lock': 'hidden', 'job_running': 'hidden', 'job_pending': 'hidden', 'job_none': 'hidden'},
    new_job: {
      'job_run': '' , 'job_stop': 'hidden', 'job_cont': 'hidden', 'job_schd': '', 'job_dupl': 'hidden' , 'job_mod': 'hidden', 'job_rm': 'hidden', 
      'job_lock': 'hidden', 'job_running': 'hidden', 'job_pending': '', 'job_none': 'hidden'},
    read_job: {
      'job_run': 'hidden' , 'job_stop': 'hidden', 'job_cont': '', 'job_schd': 'hidden', 'job_dupl': '' , 'job_mod': '', 'job_rm': '', 
      'job_lock': '', 'job_running': 'hidden', 'job_pending': 'hidden', 'job_none': 'hidden'},
   running_job: {
      'job_run': 'hidden' , 'job_stop': '', 'job_cont': 'hidden', 'job_schd': 'hidden', 'job_dupl': 'hidden' , 'job_mod': 'hidden', 'job_rm': 'hidden', 
      'job_lock': '', 'job_running': '', 'job_pending': 'hidden', 'job_none': 'hidden'},
  };

  document.querySelectorAll('.actions li').forEach( (el) => {
    const klass = scenarii[scenario][el.id];
    if (klass !== '') {
      el.classList.add(klass);
    } 
    else {
      el.classList.remove('hidden');
    }
  });
}

