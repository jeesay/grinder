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

const w_switch = (desc) => {
  // TODO
  return h(`fieldset.switch${(desc.default === "true") ? '' : '.inactive'}`,
    {
      attrs: {disabled: (desc.default === "true") ? true : false}
    },
    [
      h('legend',w_switch_button(desc)),
      ...w_group(desc)
    ]
  );
}

const w_switch_button = (desc) => {
  return [
    h('label',(desc.icon) ? [h(`i.bi.${desc.icon}`),desc.label] : desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h('div.switch_button',
      [
        h(`input#${desc.id}_on_off.param`, 
          {
            attrs: {
              type:'checkbox',
              name:desc.label
            },
            props: {
              checked: (desc.default === "true") ? true : false
            },
            on: {
              click: (ev) => {
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
          },
        ),
        h('label',
          {
            attrs: {'for':`${desc.id}_on_off`},
/*            on: {changed: (ev) => {console.log(ev.target); ev.target.disabled = !ev.target.disabled} } */
          },
          'Toggle'
        )
      ]
    )
  ]
}

const w_file = (desc) => {
  console.info('file',desc);
  const prop = (desc.arg0 !== "?") ? desc.arg0 : '';
  const placeholder = desc.arg1;
  const nodetype = desc.arg2;

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
      h(`input#${desc.id}.param${(prop === 'required') ? '.required' : ''}`, 
        {
          attrs: {
            type:'text',
            value: (desc.default === '?') ? '' : desc.default,
            placeholder: placeholder || '',
            name:desc.id
          },
          dataset: ('option' in desc) ? {option: desc.option} : {}
        }
      ),
      h('input#open_dialog.browse', 
        {
          attrs: {
            type:'button',
            value: 'Browse...',
            title: nodetype
          },
          dataset: ds,
          on: {
            click: (ev) => {const dialog = new FileChooser(GRINDER.server); dialog.openDialog(ev) }
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
    h(`input#${desc.id}.param`, 
      {
        attrs: {
          type:'text',
          value: desc.default,
          name:desc.id
        },
        dataset: ('option' in desc) ? {option: desc.option} : {}
      }
    )
  ]
);

const w_string_ro = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h(`input#${desc.id}.param`, 
      {
        attrs: {
          type:'text',
          value: desc.default,
          name:desc.id,
          readOnly:true
        },
        dataset: ('option' in desc) ? {option: desc.option} : {}
      }
    )
  ]
);


const w_text = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h(`textarea#${desc.id}.param`, 
      {
        attrs: {
          type:'text',
          value: desc.default,
          name:desc.id
        },
        dataset: ('option' in desc) ? {option: desc.option} : {}
      }
    )
  ]
);


const w_paragraph = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h(`span#${desc.id}`, desc.content)
  ]
);



/*
  {
    name: 'poly_order',
    title: 'Polynomial Order',
    widget: 'int',
    default: 1,
    help: 'The polynomial order for fitting the baseline. Default is 1.'
  }
  Output:
  <label for="poly_order">Polynomial Order</label>
  <input name="poly_order" type="number" value=1></input> 
  <i class="bi bi-question-circle" title="help"></i>

*/
const w_int = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h(`input#${desc.id}.param`, 
      {
        attrs: {
          type:'number',
          value: desc.default,
          lang:'en',
          name:desc.id
        },
        dataset: ('option' in desc) ? {option: desc.option} : {}
      }
    )
  ]
  );


const w_float = (desc) => {
  // TODO
  return w_int(desc);
}

const w_range = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h('div.range_slider',
      {
        style: {display:'flex'}
      },
      [
        h(`input#${desc.id}.param`, 
          {
            attrs: {
              type:'range',
              min: desc.arg0,
              max: desc.arg1,
              step: desc.arg2,
              value: desc.default,
              name:desc.id
            },
            dataset: ('option' in desc) ? {option: desc.option} : {},
            on: {input: (ev) => {ev.target.nextElementSibling.value = ev.target.value} }
          }
        ),
        h('output.not-allowed', {dataset: ('option' in desc) ? {option: desc.option} : {} }, desc.default.toString()),
        h('a',
          {
            props:{href:'#',title:'Type Value'},
            on: {
              click: (ev) => {
                const slider = ev.target.closest(".range_slider");
                slider.style.display = 'none';
                slider.nextElementSibling.style.display = 'flex';
              } 
            }
          },
          [h('i.bi.bi-pencil-square')],
        ),
      ]
    ),
    h('div.range_text',
      {
        style: {display:'none'}
      },
      [
        h(`input#${desc.id}.param_`, 
          {
            attrs: {
              type:'number',
              value: desc.default,
              step: desc.arg2,
              lang:'en',
              name:desc.id
            },
            dataset: ('option' in desc) ? {option: desc.option} : {}
          }
        ),
        h('a',
          {
            props:{href:'#',title:'Modify'},
            on: {
              click: (ev) => {
                const rtext = ev.target.closest(".range_text");
                rtext.style.display = 'none';
                rtext.previousElementSibling.style.display = 'flex';
              } 
            }

    //        on:{'click': (ev) => view(ev)} 
          },
          [h('i.bi.bi-sliders')],
        )
      ])
    ]
  );

const w_bool = (desc) => h('div.row',
  [
    h('label',{attrs: {'for':desc.id}},desc.label),
    h('i.bi.bi-question-circle',{attrs:{title:desc.help}}),
    h(`input#${desc.id}.param`, 
      {
        attrs: {
          type:'checkbox',
          name:desc.id
        },
        props: {
          checked: (desc.default === 'true') ? true : false,
        },
        dataset: ('option' in desc) ? {option: desc.option} : {}
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
    h(`input#${desc.id}.param`, 
      {
        attrs: {
          type:'radio',
          name:desc.group,
          value:desc.id
        },
        props: {
          checked: (desc.default === true) ? true : false
        },
        dataset: ('option' in desc) ? {option: desc.option} : {},
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
    const el = h(`li#${child.id}`,[h(`i.bi.${child.icon}`),child.label]);
    parent.appendChild(el);
  });
}

const w_tab_tools = (parent,desc) => {
  const g = w_section(desc);
  console.log(g);
  parent.appendChild(g);
}

const w_tab_tools_old = (parent,desc) => {

  const to_obj = (data) => data.rows.map( (row) => {
        let obj = {children: []};
        for (let h in data.header) {
          obj[data.header[h]] = row[h];
        }
        return obj;
      });
      
  desc.children = to_obj(desc.table);
  console.log('TABS',desc);
  const i = +desc.index;
  const el = h(`section#${desc.id}.tabs`, 
    {
      style: {display: 'none'},
      dataset: {parent_id: desc.parent} 
    },
    [
      h(`article#tools.tab`, 
      [
        h(`input#tab-${i}.tab-switch`, 
          {
            attrs: { 
              type:'radio',
              name:'css-tabs',
            },
            props: {
              checked: (i==0) ? true : false
            },
            on: ('on_click' in desc) ? {click: desc.on_click} : {}
          }
        ),
        h('label.tab-label',{attrs: {'for': `tab-${i}`}},[h(`i.bi.${desc.icon}`),' ',desc.label]),
        h('div.tab-content', 
          ('children' in desc) ? w_group(desc): []
        )
      ])
    ]
  );
  parent.appendChild(el);

}

const w_import = (desc) => {
  console.log('import',desc);
  return h('span',desc.default);
  // TODO
}

const w_navtab = (desc) => {
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
          props: {
            checked: (i==0) ? true : false
          },
          on: ('on_click' in desc) ? {click: desc.on_click} : {}
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
const w_navtab_old = (parent,desc) => {
  // Remove all the previous children
  parent.innerHTML = '';
  // Step #1 Header
  desc.forEach( (child,i) => {
    console.log('TABS',child);
    const el = h(`article#${child.label}.tab`,
      [
        h(`input#tab-${i+1}.tab-switch`, 
          {
            attrs: { 
              type:'radio',
              name:'css-tabs'
            },
            props: {
              checked: (i==0) ? true : false
            },
            on: ('on_click' in child) ? {click: child.on_click} : {}
          }
        ),
        h('label.tab-label',{attrs: {'for': `tab-${i+1}`}},[h(`i.bi.${child.icon}`),' ',child.title]),
        h('div.tab-content', 
          ('children' in child) ? w_group(child): []
        )
      ]
    );
    console.info(el);
    parent.appendChild(el);
  });
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
        return h('a.button',[h(`i.bi.${wdg.arg1}`), h('span',wdg.label)]);
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

const w_tabgroup = (desc) => {
  console.log('tabgroup',desc);
  const args = desc.children;
  console.log('>>>>>>>>>>>>>>>>>< AARRRRGGGGSSSS: ',args);
  // Reset
  // document.querySelectorAll('#args.params').forEach(w => w.remove() );
  const el = h(`div#${desc.id}.toolset`, 
    {dataset: {parent: desc.parent}},
    w_group(desc)
  );
  console.log('Done!',el);
  // el.querySelectorAll('.tab-content').forEach(w => w.prepend(h('h3.title',desc.parent_label)));
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
  return h(`details#${desc.id}`,[h('summary',desc.label),...w_group(desc)]);
}

const w_cli = (desc) => {
  console.log('command-line (cli)',desc);

  // Private function
  const gen_cli = (ev) => {
    const all_args = document.querySelector('section #args.params').querySelectorAll('input.param');
    // Create command-line from all the args set up in the GUI
    let cli = '';
    all_args.forEach( (w) => cli += (w.id+ ': ' + ((w.type == 'checkbox') ? w.checked : w.value) + '\n') );
    console.log('CLI ARGS',cli);
    document.getElementById('source_code').innerText = cli + '\n' + desc.children.reduce((accu,child) => accu + ' ' + child.content,'');
  }
  
  // Main
  return h(`details#${desc.id}.cli`,
    {
      on: {click: gen_cli }
    },
    [h('summary',desc.label),h('p#source_code','')]
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
    'label','h3','button','bool','cli','import','int','float','file','tabgroup','string','string_ro','text','range',
    'radio','select','option','section','switch','fieldset','details',
    'tab','table','thead','tbody','trow','tcell','toolbar','paragraph'];
  const creators = [
    w_label,w_h3,w_button,w_bool,w_cli,w_import,w_int,w_float,w_file,w_tabgroup,w_string,w_string_ro,w_text,w_range,
    w_radio,w_select,w_option,w_section,w_switch,
    w_fieldset,w_details,w_navtab,
    w_table,w_table_head,w_table_body,w_table_row,w_table_cell,w_toolbar,w_paragraph
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

export {w_leftpanel,w_tab_tools, w_tabgroup};
