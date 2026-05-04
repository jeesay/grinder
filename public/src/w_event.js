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

import { h} from "./dom.js"
import { update_right_sidebar } from "./job.js";
import { connect_to_ws_server, load_project} from "./main.js"
import { spin,w_alert} from "./widget.js"

function table_cell(ev) {
  if (ev.target.dataset.wtype === '') {
    // TODO 
  }
}

// Private function for click_connect(..)
const _set_project = async (ev) => {
  console.log(ev.target,ev.target.dataset);
  const project_path = ev.target.dataset.path;
  document.getElementById('connect').dataset.projpath = project_path;
  console.log('LOAD',project_path);
  spin();
  const data_proj = await load_project(project_path);
  spin();
  update_right_sidebar(project_path,data_proj);
}

const set_projlist = (paths) => {
  const dropdown = document.querySelector('#project_id .dropdown-list ul');
  paths.forEach( (path) => {
    dropdown.appendChild(
      h('li.dropdown-item',
        [
          h('a',
            {
              attrs: {
                href: "#",
              },
              dataset: {
                path: path
              },
              on : {click: _set_project}
            },
            path)
        ]
      )
    );
  });
}

// In `grinder.home`, button `Connect`
async function click_connect(ev) {
  ev.preventDefault(); // Stop the page from refreshing/redirecting
  const data_env = await connect_to_ws_server();
  // Step #1 - Fill the home dashboard
  // TODO
  console.log(data_env);
   // Step #2 - Fill the project list in the top menubar
  const obj = JSON.parse(localStorage.getItem('connection'));
  obj.proj_list = data_env.project_list;
  set_projlist(data_env.project_list);

}

// In `grinder.home`, button `Apply`
function click_newproject(ev) {
  const info = JSON.parse(localStorage.getItem('connection'));
  if (info?.connected) {
    // Send to server the project creation
  }
  else {
    w_alert('No connection to the server. Please, connect before creating the project');
  }
}

// Factory for various button events in Grinder...
export function button_click(wtype) {
  const funcs = {
    'connect' : click_connect,
    'newproject': click_newproject,
  };

  if (Object.keys(funcs).includes(wtype)) {
    return funcs[wtype];
  }
  // else return nothing
}