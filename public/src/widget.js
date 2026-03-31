//  GRINDER - Graphical user interface of RelIoN and DataminER
//  Copyright (C) 2023  Jean-Christophe Taveau
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

import {h} from "./dom.js";
import {togglePopup,fetchFileTree, init} from "./browse.js";
import {connect_to_ws_server} from "./main.js"

const get_parent = (desc,parent_id,level=0) => {
  console.info(desc);
  if (desc.parent.id === parent_id || level == 10) {
    return desc.parent;
  }
  return get_parent(desc.parent,parent_id,level++);
}

const get_parent_from_class = (desc,parent_widget,level=0) => {
  console.info(desc);
  if (!desc.hasOwnProperty(parent) || desc.parent.widget === parent_widget || level == 10) {
    return desc.parent;
  }
  return get_parent_from_class(desc.parent,parent_widget,level++);
}

const w_label = (desc) => {
  // TODO
  return h('label',desc.label);
}

const w_option = (desc) => {
  // TODO
  return h(`option#${desc.id}`,{
      props: {
        selected: desc.default,
        value: desc.default
      }
    },
    desc.label);
}

const w_h3 = (desc) => {
  // TODO
  return h('h3',desc.label);
}

const w_button = (desc) => {
  // TODO
  return h('div.row',
    [
      h('label',{attrs: {'for':desc.id}},desc.label),
      h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
      h(`button#${desc.id}`,
        {
          on: ('on_click' in desc) ? {click: desc.on_click} : {}
        },
        desc.label
      )
    ])
}

// Specialized button
const w_connect = (desc) => {

  const new_item = (item,parent) => {
      const w = h('li.file-item',
        {
          dataset: {job: item[0], procid: item[2]}
        },
        item[0]
      );
      parent.appendChild(w)
  }
  desc.on_click = async (ev) => {
    ev.preventDefault(); // Stop the page from refreshing/redirecting
    const data_env = await connect_to_ws_server();
    document.getElementById('project').innerHTML = JSON.stringify(data_env,null,2);
    console.log(data_env);
    const parent = document.querySelector('aside.jobs ul');
    data_env.environment.processes.data.forEach(job => new_item(job,parent));
    jobs.appendChild(h('li.file-item',))
  }
  return w_button(desc);
}

const w_switch = (desc) => {
  // TODO
  return h(`fieldset.switch${(desc.default === "true") ? '' : '.inactive'}`,
    {
      attrs: {disabled: (desc.default === "true") ? true : false},
    },
    [
      h('legend',w_switch_button(desc)),
      ...w_group(desc)
    ]
  );
}

const w_switch_button = (desc) => {
  const unique_id = `${desc.id.replaceAll('_','')}-${desc.toolsetid.slice(-5).replace('_','')}_on_off`;
  return [
    h('label',(desc.icon) ? [h(`i.bi.${desc.icon}`),desc.label] : desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h('div.switch_button',
      [
        h(`input#${unique_id}.param.switch-input`, 
          {
            attrs: {
              type:'checkbox',
              name:desc.label
            },
            dataset: {toolset: desc.toolsetid,param: desc.id},
            props: {
              checked: (desc.default === "true") ? true : false
            },
            on: 
              { click: (ev) => {
                console.log("Clicked element:", ev.target);
                ev.target.checked ? false : true; 
                if (ev.target.checked) {
                  ev.target.closest('fieldset').classList.remove('inactive');
                  ev.target.closest('fieldset').disabled = false;
                }
                else { 
                  ev.target.closest('fieldset').classList.add('inactive');
                  ev.target.closest('fieldset').disabled = true;
                } 
              }
            }
          }
        ),
        h('label',
          {
            attrs: {'for':`${unique_id}`},
/*            on: {changed: (ev) => {console.log(ev.target); ev.target.disabled = !ev.target.disabled} } */
          },
          'Toggle'
        )
      ]
    )
  ]
}

///////////////////// FILE ///////////////////////

const w_file = (desc) => {
  console.info('file',desc);
  const prop = (desc.arg0 !== "?") ? desc.arg0 : '';
  const nodetype = desc.arg0;
  const tree_depth = desc.arg1;
  const placeholder = desc.arg2;
  

  let ds = {inputfile: desc.id};
  if ('filetype' in desc) {
    ds.title = GRINDER.filetypes[filetype].dialog_title;
    ds.filter = GRINDER.filetypes[filetype].filter;
  }
  else {
    if ('dialog_title' in desc) {
      ds.title =  desc.dialog_title;
    }
    if ('filter' in desc) {
      ds.filter = desc.filter;
    }
  }
  
  return h('div.row',
    {
      style: (desc.status === 'hidden') ? {display: 'none'} : {display:'flex'}
    },
    [
      h(`label${(desc.arg0 !== '?') ? '.' + desc.arg0 : ''}`,{attrs: {'for':desc.id}},desc.label),
      h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
      h(`input#${desc.id}-${desc.toolsetid.slice(-4)}.param${(prop === 'required') ? '.required' : ''}`, 
        {
          attrs: {
            type:'text',
            value: (desc.default === '?' || desc.default === '') ? '' : desc.default,
            placeholder: placeholder || '',
            name:desc.id
          },
          props: {
              required: (desc.constraint === "required") ? true : false
            },
          dataset: {
            toolset: desc.toolsetid,
            param: desc.id,
            node: nodetype,
            depth: tree_depth,
            option: ('option' in desc) ? desc.option : 0
          },
        }
      ),
      h('input#open_dialog.browse.open-trigger',
        {
          attrs: {
            type:'button',
            value: 'Browse...',
            title: nodetype
          },
          dataset: ds,
          on: {
            click: async (ev) => {
              ev.preventDefault(); // Stop the page from refreshing/redirecting
              const data_tree = await fetchFileTree();
              const popup = document.getElementById('file-popup');
              const isVisible = popup.style.display === 'flex';
              popup.style.display = isVisible ? 'none' : 'flex';
              if (!isVisible) init(JSON.parse(data_tree).children); // Load root on open
            }
          }
        }
      )
    ]
  );
}

const w_string = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h(
      `input#${desc.id.replaceAll('_','')}-${desc.toolsetid.slice(-5).replace('_','')}.param`, 
      {
        attrs: {
          type:'text',
          value: desc.default,
          name:desc.id
        },
        dataset: {
          toolset: desc.toolsetid,
          param: desc.id,
          option: ('option' in desc) ? desc.option : 0
        },
      }
    )
  ]
);

const w_string_ro = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h(
      `input#${desc.id.replaceAll('_','')}-${desc.toolsetid.slice(-5).replace('_','')}.param`, 
      {
        attrs: {
          type:'text',
          value: desc.default,
          name:desc.id,
          readOnly:true
        },
        dataset: {
          toolset: desc.toolsetid,
          param: desc.id,
          option: ('option' in desc) ? desc.option : 0
        },
      }
    )
  ]
);


const w_text = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h(
      `textarea#${desc.id.replaceAll('_','')}-${desc.toolsetid.slice(-5).replace('_','')}.param`, 
      {
        attrs: {
          type:'text',
          value: desc.default,
          name:desc.id
        },
        dataset: {
          toolset: desc.toolsetid,
          param: desc.id,
          option: ('option' in desc) ? desc.option : 0
        },
      }
    )
  ]
);


const w_paragraph = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h(
      `span#${desc.id.replaceAll('_','')}-${desc.toolsetid.slice(-5).replace('_','')}.param`, 
      desc.default
    )
  ]
);


const w_int = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h(
      `input#${desc.id.replaceAll('_','')}-${desc.toolsetid.slice(-5).replace('_','')}.param`, 
      {
        attrs: {
          type:'number',
          value: desc.default,
          lang:'en',
          name:desc.id
        },
        dataset: {
          toolset: desc.toolsetid,
          param: desc.id,
          option: ('option' in desc) ? desc.option : 0
        },
      }
    )
  ]
  );


const w_float = (desc) => {
  // TODO
  return w_int(desc);
}
/*
<div class="range-container">
  <input type="range" 
         id="myRange" 
         min="0" 
         max="100" 
         value="50" 
         oninput="syncInput(this.value)">

  <input type="number" 
         id="myNumber" 
         value="50" 
         oninput="syncRange(this.value)">
</div>

  const range = document.getElementById('myRange');
  const number = document.getElementById('myNumber');

  function checkBounds(val) {
    const min = parseInt(range.min);
    const max = parseInt(range.max);
    
    // Add red styling if value is outside the 0-100 range
    if (val < min || val > max) {
      number.classList.add('out-of-range');
    } else {
      number.classList.remove('out-of-range');
    }
  }

  function syncInput(val) {
    number.value = val;
    checkBounds(val);
  }

  function syncRange(val) {
    range.value = val;
    checkBounds(val);
  }
*/

function check_bounds(val,widget) {
  console.log(widget);
  let range  = (widget.type === 'range') ? widget : widget.previousElementSibling;
  let number = (widget.type === 'number') ? widget : widget.nextElementSibling
  // Update values
  widget.parentElement.value = val;
  range.value = val;
  number.value = val;
  console.log(range,number);
  const min = parseInt(range.min);;
  const max = parseInt(range.max);

  // Add red styling if value is outside the 0-100 range
  if (val < min || val > max) {
    number.classList.add('out-of-range');
  } else {
    number.classList.remove('out-of-range');
  }
}

const w_range = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    // `div#${desc.id.replace('_','')}-${desc.toolsetid.slice(-5).replace('_','')}_container.range-container`,
    h( 
      `div#${desc.id.replaceAll('_','')}-${desc.toolsetid.slice(-5).replace('_','')}_container.range-container`,
      {
        style: {display:'flex'},
        attrs: {value: desc.default}
      },
      [
        h(`input#${desc.id}_range`, 
          {
            attrs: {
              type:'range',
              min: desc.arg0,
              max: desc.arg1,
              step: desc.arg2,
              value: desc.default,
              name:desc.id + '_range'
            },
            dataset: {
              toolset: desc.toolsetid,
              param: desc.id,
              option: ('option' in desc) ? desc.option : 0
            },
            on: {input: (ev) => check_bounds(ev.target.value,ev.target) }
          }
        ),
        h(
          `input#${desc.id.replaceAll('_','')}-${desc.toolsetid.slice(-5).replace('_','')}.param`, 
          {
            attrs: {
              type:'number',
              value: desc.default,
              step: desc.arg2,
              lang:'en',
              name:desc.id
            },
            dataset: {
              toolset: desc.toolsetid,
              param: desc.id,
              option: ('option' in desc) ? desc.option : 0
            },
            on: {input: (ev) => check_bounds(ev.target.value,ev.target)}
          }
        )
      ])
    ]
  );

const w_bool = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h(
      `input#${desc.id.replaceAll('_','')}-${desc.toolsetid.slice(-5).replace('_','')}.param`, 
      {
        attrs: {
          type:'checkbox',
          name:desc.id
        },
        props: {
          checked: (desc.default === 'true') ? true : false,
        },
        dataset: {
          toolset: desc.toolsetid,
          param: desc.id,
          option: ('option' in desc) ? desc.option : 0
        },
      }
    ),
  ]
  );

/*
  {
    name: 'poly',
    group: 'baseline_methods',
    title: 'Regular Polynomial',
    widget: 'radio',
    value: false,
    help: 'Regular Polynomial Method'
  }
  Output:
  <input type="radio" id="poly" name="baseline_methods" value="poly" checked />
  <label for="poly">Regular Polynomial</label> 
  <i class="bi bi-question-circle" title="Regular Polynomial Method"></i>
*/
const w_radio = (desc) => h('div.row',
  [
    h(
      // Unique ID
      `input#${desc.id}.param`, 
      {
        attrs: {
          type:'radio',
          name:desc.group,
          value:desc.id
        },
        props: {
          checked: (desc.default === true) ? true : false
        },
        dataset: {
          toolset: desc.labelnew,
          param: desc.id,
          option: ('option' in desc) ? desc.option : 0
        },
        on: ('on_click' in desc) ? {click: desc.on_click} : {}
      }
    ),
    h('label',{attrs: {'for': desc.id}},desc.label + ' '),
    h('i.bi.bi-question-circle',{attrs: {title: desc.help}})
  ]
  );

const w_leftpanel = (parent,desc) => {
  console.log('leftpanel',desc.label);
  desc.forEach( (child,i) => {
    const el = h(
      `li#${child.id}`,
      [
        h('a',
          [
            h(`i.nav-icon.bi.${child.icon}`),
            h('span.nav-text',child.label)
          ]
        )
      ],
    );
    parent.appendChild(el);
  });
}

const w_tab_tools = (parent,desc) => {
  const g = w_section(desc);
  console.log(g);
  parent.appendChild(g);
}

const w_import = (desc) => {
  console.log('import',desc);
  return h('span',desc.default);
  // TODO
}

const w_navtab = (desc) => {
  // Event function
  const get_logfile = (ev) => {
    // Connect to ws
    console.info(ev.target.dataset.parent, ev.target.dataset.label);
  };

  const get_dataviz = (ev) => {
    // Connect to ws
    console.info(ev.target.dataset.parent, ev.target.dataset.label);
  }

  const nothing = (ev) => {
    console.info('Do nothing');
  }
  
  const funcs = {'I/O': nothing,'Settings': nothing,'Log': get_logfile,'DataViz': get_dataviz};

  console.error(`Has children in ${desc.id}?`,('children' in desc) && (desc.children.length > 0));
  // Remove all the previous children
  // parent.innerHTML = '';
  let i = desc.index + 1; // HACK
  // Step #1 Header
  const el = h(`article#${desc.label}.tab`,
    [
      h(`input#tab-${i}.tab-switch`, 
        {
          attrs: { 
            type:'radio',
            name:'css-tabs'
          },
          dataset: {
            parent: desc.parent,
            label: desc.label
          },
          props: {
            checked: (i==0) ? true : false
          },
          on: ('on_click' in desc) ? {click: desc.on_click} : {click: funcs[desc.label]}
        }
      ),
      h('label.tab-label',{attrs: {'for': `tab-${i}`}},[h(`i.bi.${desc.icon}`),' ',desc.label]),
      h('div.tab-content', 
        (('children' in desc) && (desc.children.length > 0)) ? w_group(desc): []
      )
    ]
  );
  console.info('navtab',desc, desc.index, el);

  return el;
}

const w_toolmenu = w_navtab;

const w_radiotool = (desc) => {
//  // Create radio button linked to the `toolmenu`
//  const el = w_radio(desc);
//  // Create tabs and attach to `section`
//  const tabs= w_tabgroup(desc);
//  return tabs;
}

const w_select = (desc) => {
  console.info('>>>> CREATE SELECT',desc)
  return h('div.row',
  [
    h('label',{attrs: {'for': desc.id}},desc.label + ' '),
    h('i.bi.bi-question-circle',{attrs: {title: desc.help}}),
    h('div.select-dropdown',[
      h(`select#${desc.id}`,
        {
          on: ('on_change' in desc) ? {click: desc.on_change} : {}
        },
        w_group(desc),
       )
    ])
  ]);
}

const w_toolbar = (desc) => {
  console.log('toolbar',desc.label);
  return h('div.toolbar',
    desc.children.map( wdg => {
      if (wdg.arg1 != "?") {
        return h('a.button',{attrs: {title: wdg.label}},[h(`i.bi.${wdg.arg1}`), h('span','')]);
      }
      else {
        return h('a.button',wdg.label);
      }
    }
  ));
}

const w_fieldset = (desc) => {
  console.log('fieldset',desc.label);
  return h(`fieldset#${desc.id}`,
    [
      h('legend',(desc.icon) ? [h(`i.bi.${desc.icon}`),desc.label] : desc.label),...w_group(desc)
    ]
  );
}

const w_tool = (desc) => {
  // // Step #1 - Create the radio button
  // const el = w_radio(desc);
  // el.appendChild(desc.parent);
  // // Step #2 -  Create the toolset
  // const g = w_tabgroup(desc.children);
  // g.appendChild(desc.parent);
}

const w_toolset = (desc) => {
  const toolbar = {
    label: desc.label,
    children: [
      {id: 'h3.title',label: desc.label,arg1: '?'},
      {id: 'run',label: 'Run job',arg1: 'bi-send'},
      {id: 'continue',label: 'Continue job',arg1: 'bi-arrow-repeat'},
      {id: 'schedule',label: 'Schedule job',arg1: 'bi-calendar2-week'},
      {id: 'overwrite',label: 'Overwrite job',arg1: 'bi-pencil-square'},
      {id: 'delete',label: 'Remove job',arg1: 'bi-trash'},
      {id: 'h4.title',label: 'Status',arg1: '?'},
      {id: 'h4.title',label: 'Pending',arg1: 'bi-person-standing'},       
    ]
  }
  console.log('toolmenu',desc);
  const args = desc.children;
  console.log('>>>>>>>>>>>>>>>>>< AARRRRGGGGSSSS: ',args);
  // Reset
  // document.querySelectorAll('#args.params').forEach(w => w.remove() );
  const el = h(`div#${desc.id}.toolset`, 
    {
      style: {display: 'none'},
      dataset: {parent: desc.parent},
     },
    w_group(desc)
  );
  console.log('Done!',el);
  el.querySelectorAll('.tab-content').forEach(w => w.prepend(w_toolbar(toolbar)));
  // document.querySelector('section').appendChild(el);
  return el;
}

const w_params_show = (args) => {
  console.log('param',args.id, args.section);
  // Reset all other params tabs
  document.getElementById(args.section).querySelectorAll('div.params').forEach(w => w.style.display='none');
  document.getElementById(args.id).style.display = 'block';
}

const w_section = (desc) => {
  console.log('section',desc.id);
  return h(`section#${desc.id}.tabs`, 
    {
      style: desc.style, 
      dataset: {parent: desc.parent}
    },
    w_group(desc) // ,h(`div#args.params`)]
  );
}

const w_details = (desc) => {
  console.log('details',desc.label);
  return h(`details#${desc.id}`,
    {
      dataset: {
        toolset: desc.toolsetid,
        param: desc.id,
        option: ('option' in desc) ? desc.option : 0
      }
    },
    [h('summary',desc.label),...w_group(desc)]
  );
}

const w_cli = (desc) => {
  console.log('command-line (cli)',desc);

  // Private function
  const gen_cli = (ev) => {
    console.info(ev.target.dataset.toolset);
    const all_args = document.querySelectorAll(`#${ev.target.dataset.toolset} .param`);
    // Create command-line from all the args set up in the GUI
    let cli = '';
    all_args.forEach( (w) => cli += (w.id+ ': ' + ((w.type == 'checkbox') ? w.checked : w.value) + '\n') );
    console.log('CLI ARGS',cli);
    const content = h('table.custom-table',
      [
        h('caption','Program parameters'),
        h('thead',
          [ h('tr',[
            h('th',{attrs: {scope: "col"}},'ID'),
            h('th',{attrs: {scope: "col"}},'Key'),
            h('th',{attrs: {scope: "col"}},'Value')
          ])]
        ),
        h('tbody',
          Array.from(all_args).map(wdgt => h('tr',[
            h('td',{attrs: {scope: "row"}},wdgt.id),
            h('td',{attrs: {scope: "row"}},wdgt.dataset.param),
            h('td',{attrs: {scope: "row"}},(wdgt.type === 'checkbox') ? wdgt.checked.toString() : wdgt.value)
          ])
      ))
      ]
    );

    document.querySelector(`#${ev.target.dataset.toolset}_cmd p.source_code`).appendChild(content); //  = cli + '\n' + desc.children.reduce((accu,child) => accu + ' ' + child.content,'');
  }
  
  // Main
  return h(`details#${desc.id}.cli`,
    {
      dataset: {
        toolset: desc.toolsetid,
        param: desc.id,
        option: ('option' in desc) ? desc.option : 0
      },
      on: {click: gen_cli }
    },
    [
      h('summary',
        {
          dataset: {
            toolset: desc.toolsetid,
            param: desc.id,
            option: ('option' in desc) ? desc.option : 0
          }
        },
        desc.label
      ),
      h('p.source_code','')
    ]
  );
}

const w_table = (desc) => {
  console.log('table',desc.label);
  let components = [];
  if (desc.children?.[0]) {
    components.push(w_table_head(desc.children[0]));
  }
  if (desc.children?.[1]) {
    components.push(w_table_body(desc.children[1]));
  }
  return h(`table#${desc.id}`,components);
}

const w_table_head = (desc) => {
  console.log('table_head',desc.label);
  return  h(`thead#${desc.id}`,[h('tr',[...w_group(desc)])]);
}

const w_table_body = (desc) => {
  console.log('table_body',desc.label);
  return h(`tbody#${desc.id}`,[...w_group(desc)]);
}

const w_table_row = (desc) => {
  return h(`tr#${desc.id}`,[...w_group(desc)]);
}

const w_table_cell = (desc) => {
  return h(`td#${desc.id}`,desc.value);
}

const w_group = (desc) => {
  console.info('group',desc);
  // Primitive Widgets
  const types = [
    'label','h3','button','bool','cli','connect','import','int','float','file','toolset','string','string_ro','text','range',
    'radio','radio_tool','select','option','section','switch','fieldset','details',
    'tab','table','thead','tbody','trow','tcell','toolbar','toolmenu','paragraph'];
  const creators = [
    w_label,w_h3,w_button,w_bool,w_cli,w_connect,w_import,w_int,w_float,w_file,w_toolset,w_string,w_string_ro,w_text,w_range,
    w_radio,w_radiotool,w_select,w_option,w_section,w_switch,
    w_fieldset,w_details,w_navtab,
    w_table,w_table_head,w_table_body,w_table_row,w_table_cell,w_toolbar,w_toolmenu,w_paragraph
  ];
  if ('children' in desc === false) {
    console.error(desc);
  }

  // Build HTML Elements
  let els = [];
  if (desc.children.length > 0) {
    els =  desc.children.map( child => {
      console.info(child);
      if (types.indexOf(child.widget) !== -1) {
        console.info('group child',child);
        return creators[types.indexOf(child.widget)](child);
      }
    });
  }

  
  // Post-process for `switch` widget
  document.querySelectorAll('.switch').forEach(el => {
    const sbutton = el.querySelector('.switch_button input');
    if (sbutton.checked) {
      el.classList.remove('inactive');
      el.disabled = false;
    }
    else {
      el.classList.add('inactive');
      el.disabled = true;
    } 
  }) ;
  
  return els;
}

////////////////////: UPDATE :////////////////////

const w_navtab_update = (tab_contents) => {
  
  Object.keys(tab_contents).forEach(parent_id => {
    const content = document.querySelector(`article#${parent_id} .tab-content`);
    const desc = tab_contents[parent_id];
    // Update corresponding tab
    content.replaceChildren(...w_group(desc));
  });

}

////////////////////: EVENTS :////////////////////

const submit_command = (tool) => (ev) => {
  const els = document.querySelectorAll('section .param');
  const cli = Array.from(els).reduce( (accu,el) => {
    console.log(el.name,el.type,el.dataset.option,el.value,el.checked);
    if (el.type === 'radio' || el.type === 'checkbox') {
      return (el.checked) ? accu + ` ${el.dataset.option}` : accu;
    }
    else {
      return accu + ` ${el.dataset.option} ${el.value}`;
    }
  },tool);
  document.querySelector('button#submit').disabled = true;
  console.log(cli);
  const event = {
    end:0,
    action: {
      tool: tool,
      title:'sleep',
      args:cli
    } 
  };

  let field = document.querySelectorAll("article#running > div > fieldset")[1];
  let textdiv = document.createElement('div');
  field.appendChild(textdiv);
  console.log("Send");
  console.log(event);
  GRELION.websocket.send(JSON.stringify(event));
}

export {w_leftpanel,w_tab_tools, w_toolmenu};
