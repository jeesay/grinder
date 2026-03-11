import {StarGate} from "./stargate.js";
import {w_leftpanel, w_tab_tools} from "./widget.js";
import {WSClient} from "./ws_client.js";
//import {*} from "./dom.js";
//import {*} from "./job.js";
//import {*} from "./history.js";
//import {*} from "./browse.js";
//import {*} from "./widget.js";

export const GRINDER = {
  version: '0.1',
  authors: ["Jean-Christophe Taveau"],
  server: new WSClient(),
  filetypes: {
    CURRENT_ODIR: {
      id: 100,
      dialog_title: 'Open file',
      path: ''
    },
    NODE_MOVIES_CPIPE: {
      id: 1,
      dialog_title: 'Open movie STAR file',
      placeholder: '*.star',
      filter: '.star',
      outnode: "MicrographMoviesData.star.relion",
      filterdir: '',
    },
    NODE_MICS_CPIPE: {
      id: 2,
      dialog_title: 'Open Micrographs STAR file',
      placeholder: '*.star',
      filter: '.star',
      outnode: "MicrographsData.star.relion"
    },
    NODE_2DIMGS_CPIPE: {
      id: 3,
      dialog_title: 'Open movie STAR file (*.star)',
      placeholder: '*.star',
      filter: '.star',
      outnode: ''
    },
    NODE_MAP_CPIPE: {
      id: 4,
      dialog_title: 'Open 3D reference',
      placeholder: '*.mrc',
      filter: '.mrc'
    },
    NODE_PARTS_CPIPE: {
      id: 5,
      dialog_title: "Open Particles STAR file",
      placeholder: '*.star',
      filter: '.star'
    },
    NODE_COORDS_CPIPE: {
      id: 6,
      dialog_title: "Open Particle coordinates",
      placeholder: "*.box, *_pick.star",
      filter: '.box,_pick.star'
    },
    NODE_COORDS_HELIX_CPIPE: {
      id: 7,
      dialog_title: "Open Particle coordinates",
      placeholder: "*.box, *_pick.star",
      filter: '.box,_pick.star'
    },
    NODE_PARTS_HELIX_CPIPE: {
      id: 8,
      dialog_title: "Open Particle coordinates",
      placeholder: "*.box, *_pick.star",
      filter: '.box,_pick.star'
    },
    NODE_OPTIMISER_CPIPE: {
      id: 9,
      dialog_title: "Open Particle coordinates",
      placeholder: "*.box, *_pick.star",
      filter: '.box,_pick.star',
      nodetype: "ProcessData.star.relion.optimiser"
    },
    NODE_MASK_CPIPE: {
      id: 10,
      dialog_title: "Open 3D mask",
      placeholder: "*.mrc",
      filter: '.mrc',
      nodetype: "Mask3D.mrc"
    },
    NODE_HALFMAP_CPIPE: {
      id: 11,
      dialog_title: "Open Unfiltered half-map",
      placeholder: "*unfil.mrc",
      filter: '.unfil.mrc',
      nodetype: "DensityMap.mrc.halfmap"
    },
    NODE_RESMAP_CPIPE: {
      id: 12,
      dialog_title: "Open Particle coordinates",
      placeholder: "*.box, *_pick.star",
      filter: '.box,_pick.star',
      nodetype: "Image3D.mrc.localresmap"
    },
    NODE_LOGFILE_CPIPE: {
      id: 13,
      dialog_title: "Open Particle coordinates",
      placeholder: "*.box, *_pick.star",
      filter: '.box,_pick.star',
      filterdir: '',
      nodetype: "LogFile.pdf.relion"
    }
  },
  folders: {
    OUTNODE_MOVIES_CPIPE      : "MicrographMoviesData.star.relion",
    OUTNODE_MICS_CPIPE        : "MicrographsData.star.relion",
    OUTNODE_2DIMGS_CPIPE      : "ImagesData.star.relion",
    OUTNODE_MAP_CPIPE         : "DensityMap.mrc",
    OUTNODE_PARTS_CPIPE       : "ParticlesData.star.relion",
    OUTNODE_COORDS_CPIPE      : "MicrographsCoords.star.relion",
    OUTNODE_COORDS_HELIX_CPIPE: "MicrographsCoords.star.relion.helixstartend",
    OUTNODE_PARTS_HELIX_CPIPE : "ParticlesData.star.relion.helicalsegments",
    OUTNODE_OPTIMISER_CPIPE   : "ProcessData.star.relion.optimiser",
    OUTNODE_MASK_CPIPE        : "Mask3D.mrc",
    OUTNODE_HALFMAP_CPIPE     : "DensityMap.mrc.halfmap",
    OUTNODE_RESMAP_CPIPE      : "Image3D.mrc.localresmap",
    OUTNODE_LOGFILE_CPIPE     : "LogFile.pdf.relion",

    OUTNODE_IMPORT_MOVIES     : "MicrographMoviesData.star.relion",
    OUTNODE_IMPORT_MICS       : "MicrographsData.star.relion",
    OUTNODE_IMPORT_COORDS     : "MicrographsCoords.star.relion",
    OUTNODE_IMPORT_PARTS      : "ParticlesData.star.relion",
    OUTNODE_IMPORT_2DIMG      : "ImagesData.star.relion",
    OUTNODE_IMPORT_MAP        : "DensityMap.mrc",
    OUTNODE_IMPORT_MASK       : "Mask3D.mrc",
    OUTNODE_IMPORT_HALFMAP    : "DensityMap.mrc.halfmap",
    OUTNODE_MOCORR_MICS       : "MicrographsData.star.relion.motioncorr",
    OUTNODE_MOCORR_LOG        : "LogFile.pdf.relion.motioncorr",
    OUTNODE_CTFFIND_MICS      : "MicrographsData.star.relion.ctf",
    OUTNODE_CTFFIND_LOG       : "LogFile.pdf.relion.ctffind",
    OUTNODE_MANPICK_MICS      : "MicrographsData.star.relion",
    OUTNODE_MANPICK_COORDS    : "MicrographsCoords.star.relion.manualpick",
    OUTNODE_AUTOPICK_COORDS   : "MicrographsCoords.star.relion.autopick",
    OUTNODE_AUTOPICK_LOG      : "LogFile.pdf.relion.autopick",
    OUTNODE_AUTOPICK_TOPAZMODEL:"ProcessData.sav.topaz.model", // to be added?
    OUTNODE_AUTOPICK_MICS     : "MicrographsData.star.relion",
    OUTNODE_EXTRACT_PARTS     : "ParticlesData.star.relion",
    OUTNODE_EXTRACT_PARTS_REEX: "ParticlesData.star.relion.reextract",
    OUTNODE_EXTRACT_COORDS_REEX:"MicrographsCoords.star.relion.reextract",
    OUTNODE_CLASS2D_PARTS     : "ParticlesData.star.relion.class2d",
    OUTNODE_CLASS2D_OPT       : "ProcessData.star.relion.optimiser.class2d",
    OUTNODE_SELECT_MICS       : "MicrographsData.star.relion",
    OUTNODE_SELECT_MOVS       : "MicrographMoviesData.star.relion",
    OUTNODE_SELECT_PARTS      : "ParticlesData.star.relion",
    OUTNODE_SELECT_OPT        : "ProcessData.star.relion.optimiser.autoselect",
    OUTNODE_SELECT_CLAVS      : "ImagesData.star.relion.classaverages",
    OUTNODE_INIMOD_MAP        : "DensityMap.mrc.relion.initialmodel",
    OUTNODE_CLASS3D_OPT       : "ProcessData.star.relion.optimiser.class3d",
    OUTNODE_CLASS3D_MAP       : "DensityMap.mrc.relion.class3d",
    OUTNODE_CLASS3D_PARTS     : "ParticlesData.star.relion.class3d",
    OUTNODE_REFINE3D_HALFMAP  : "DensityMap.mrc.relion.halfmap.refine3d",
    OUTNODE_REFINE3D_OPT      : "ProcessData.star.relion.optimiser.refine3d",
    OUTNODE_REFINE3D_MAP      : "DensityMap.mrc.relion.refine3d",
    OUTNODE_REFINE3D_PARTS    : "ParticlesData.star.relion.refine3d",
    OUTNODE_MULTIBODY_HALFMAP : "DensityMap.mrc.relion.halfmap.multibody",
    OUTNODE_MULTIBODY_PARTS   : "ParticlesData.star.relion.multibody",
    OUTNODE_MULTIBODY_OPT     : "ProcessData.star.relion.optimiser.multibody",
    OUTNODE_MULTIBODY_FLEXLOG : "LogFile.pdf.relion.flexanalysis",
    OUTNODE_MULTIBODY_SEL_PARTS:"ParticlesData.star.relion.flexanalysis.eigenselected",
    OUTNODE_MASK3D_MASK       : "Mask3D.mrc.relion",
    OUTNODE_SUBTRACT_SUBTRACTED:"ParticlesData.star.relion.subtracted",
    OUTNODE_SUBTRACT_REVERTED : "ParticlesData.star.relion",
    OUTNODE_LOCRES_OWN        : "Image3D.mrc.relion.localresmap",
    OUTNODE_LOCRES_RESMAP     : "Image3D.mrc.resmap.localresmap",
    OUTNODE_LOCRES_FILTMAP    : "DensityMap.mrc.relion.localresfiltered",
    OUTNODE_LOCRES_LOG        : "LogFile.pdf.relion.localres",
    OUTNODE_CTFREFINE_REFINEPARTS:"ParticlesData.star.relion.ctfrefine",
    OUTNODE_CTFREFINE_LOG     : "LogFile.pdf.relion.ctfrefine",
    OUTNODE_CTFREFINE_ANISOPARTS:"ParticlesData.star.relion.anisomagrefine",
    OUTNODE_POLISH_PARTS      : "ParticlesData.star.relion.polished",
    OUTNODE_POLISH_LOG        : "LogFile.pdf.relion.polish",
    OUTNODE_POLISH_PARAMS     : "ProcessData.txt.relion.polish.params",
    OUTNODE_POST              : "ProcessData.star.relion.postprocess",
    OUTNODE_POST_MAP          : "DensityMap.mrc.relion.postprocess",
    OUTNODE_POST_MASKED       : "DensityMap.mrc.relion.postprocess.masked",
    OUTNODE_POST_LOG          : "LogFile.pdf.relion.postprocess"
/* TODO
    OUTNODE_MANPICK_COORDS_HELIX:     "MicrographsCoords.star.relion.manualpick.helixstartend",
    OUTNODE_EXTRACT_PARTS_HELIX:      "ParticlesData.star.relion.helicalsegments",
    OUTNODE_EXTRACT_COORDS_HELIX:     "MicrographsCoords.star.relion.helixstartend",
    OUTNODE_CLASS2D_PARTS_HELIX:      "ParticlesData.star.relion.class2d.helicalsegments",
    OUTNODE_CLASS3D_PARTS_HELIX:      "ParticlesData.star.relion.class3d.helicalsegments",
    OUTNODE_REFINE3D_PARTS_HELIX:     "ParticlesData.star.relion.refine3d.helicalsegements",
*/
  }
};


/*
  OUTNODE_TOMO_OPTIMISATION : "ProcessData.star.relion.tomo.optimisation_set"
  OUTNODE_TOMO_TOMOGRAMS    : "ProcessData.star.relion.tomo.relion.tomogram_set"
  OUTNODE_TOMO_TRAJECTORIES : "ProcessData.star.relion.tomo.relion.trajectory_set"
  OUTNODE_TOMO_MANIFOLDS    : "ProcessData.star.relion.tomo.manifoldset"
  OUTNODE_TOMO_PARTS        : "Particles.star.relion.tomo"
  OUTNODE_TOMO_MAP          : "DensityMap.mrc.relion.tomo.subvolume"
  OUTNODE_TOMO_HALFMAP      : "DensityMap.mrc.relion.tomo.halfmap"
  OUTNODE_TOMO_POST         : "ProcessData.star.relion.tomo.postprocess"
  OUTNODE_TOMO_POST_LOG     : "LogFile.pdf.relion.tomo.postprocess"
  OUTNODE_TOMO_FRAMEALIGN_LOG      "LogFile.pdf.relion.tomo.framealign"
  OUTNODE_TOMO_CTFREFINE_LOG: "LogFile.pdf.relion.tomo.ctfrefine"
*/


 /**
 * Receive the response of the server and display the result on the HTML page
 * @param  {Websocket} websocket  Server

const receive = (websocket) => {
  websocket.addEventListener("message", (response) => {
    console.log(response);
    const msg = JSON.parse(response.data);

    console.log(`[message] Data received from server: ${msg}`);

    // Dispatch data
    if (event['data'] != null){
      let data = event['data']
      GRINDER.jobs = JSON.parse(msg);
    }
  });
}

 
// https://github.com/jcao219/websocket-async/blob/master/src/websocket-client.js
// 
const receive = function() {
  if (GRINDER.receiveDataQueue.length !== 0) {
    // We have a message ready.
    return Promise.resolve(GRINDER.receiveDataQueue.shift());
  }

  // Wait for the next incoming message and receive it.
  const receivePromise = new Promise((resolve, reject) => {
    GRINDER.receiveCallbacksQueue.push({ resolve, reject });
  });

  return receivePromise;
};
 */
 
 
/*
 * Run the WebSocket Client and try to connect to the python WebSocket server
*/
export const connect_to_ws_server = async () => {
  const ip_address = document.querySelector('input.param[data-param=ws_server_ip]').value;
  const port = document.querySelector('input.param[data-param=ws_port]').value;
  console.info('WS',ip_address,port);
  // Open the WebSocket connection and register event handlers.
  await GRINDER.server.connect(`ws://${ip_address}:${port}/welcome`);
  
  if (GRINDER.server.connected) {
      alert(`[Open] Connection established with server ws://${ip_address}:${port}/welcome`);
      document.getElementById('connect').innerHTML = '<i class="bi bi-wifi"></i>Connected';
      document.getElementById('connect').style.color = 'lightgreen';

      const data = await GRINDER.server.receive();
      document.getElementById('project').innerHTML = data;
  }
  else {
      alert(`[Fail] Unable to connect to the server ws://${ip_address}:${port}/`);
  }

/*
//  GRINDER.websocket.onmessage = (event) => {};

  GRINDER.websocket.onclose = function(event) {
    if (event.wasClean) {
      alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
    } else {
      // e.g. server process killed or network down
      // event.code is usually 1006 in this case
      alert('[close] Connection died');
    }
  };

  GRINDER.websocket.onerror = function(error) {
    alert(`[error]`);
  };

   // Step #1 - Get default_pipeline.json of Project
    let cli = {
      end:0,
      action: {
        tool: 'grinder.py',
        title:'project',
        args:'--get default_pipeline.json'
      }
    };
    GRINDER.websocket.send(JSON.stringify(cli));

  receive(GRINDER.websocket);
*/
};

 const fetchFile = async filename => {
    const file = await fetch(filename);
    const text = await file.text();
    
    const obj = new StarGate();
    obj.parseSTAR(text);
    return obj.blocks();
  }

  const from_startable = (data) => data.rows.map( (row) => {
      let obj = {};
      for (let h in data.header) {
        obj[data.header[h]] = row[h];
      }
      if (['program','toolmenu','tabgroup','radio_tool','tab','fieldset','switch','details', 'cli', 'toolbar','select'].includes(obj.widget)) {
        obj.children = [];
      }
      return obj;
    });

  const is_table = (el) => typeof el == 'object' && 'header' in el;

  const get_tables = (star) => Object.keys(star).filter(key => is_table(star[key])).map(key => ({key,table:star[key]}));

  const flat_tables = (tables) => {
    console.info('++++++++++++++ TABLES',tables);
    // Convert each table into object
    let flat_table = tables.map(t => {
      console.log(t.key);
      let rows = from_startable(t.table);
      console.info(rows);
      rows.forEach(row => row.parent = t.key );
      return rows // {key: t.key,table: rows}
    }).flat();
    // flat_table = [{id:'tabs',children:[]},...flat_table];
    console.info('++++++++++++++ TABLES',flat_table);
    return flat_table;
  }
  
  const build_tree = (datablock,parent) => {
    // Get all tables and build hierarchy
    let tables = get_tables(datablock);
    let flat_table = flat_tables(tables);
    let tab_count = parent.index;
    flat_table.forEach(wdgt => {
      console.log('WIDGET',wdgt);
      // Attach the tab to the `toolset`
      if (wdgt.widget == 'tab') {
        console.log('ADD TAB',wdgt);
        // wdgt.parent = db.id;
        wdgt.index = tab_count;
        wdgt.toolsetid = parent.id;
        tab_count++;
        parent.children.push(wdgt);
      }
      else if ('parent' in wdgt) {
        // Update toolset info
        wdgt.toolsetid = parent.id;
        // Attach other widgets depending of their parent.
        const index = flat_table.map(e => e.id).indexOf(wdgt.parent);
        console.info('FIND PARENT',index,wdgt,flat_table[index]);
        flat_table[index].children.push(wdgt);
      }
    });
    return parent;
  }

  export const fetchRootFile = async filename => {
    // Load and parse `grinder_spa.star`
    const file = await fetch(filename);
    const text = await file.text();
    const all_of_them = [{dummy: '?'}];
    
    const obj = new StarGate();
    obj.parseSTAR(text);
    const left_panel = obj.datablock('grinder_spa').table('tool_panel');
    console.info('PANEL',left_panel);
    // Create items in left panel
    w_leftpanel(document.querySelector('aside ul'),left_panel);
    // Create Tools panel
    let tools = [];
    let tab_count = 1;
    for (let tab of left_panel) {
      console.info('Tab Data',tab);
      // tab.path = 'spa/'+ tab.starfile.split('/')[0] + '/' //HACK
      const _tmp = await fetchFile(tab.path + tab.starfile);
      let db = _tmp.datablocks.default;
      console.log('ROOT',db);
      let root = {
        id : db.id,
        label: db.label,
        widget:db.widget,
        style: {display: 'none'},
        parent:db.parent,
        tab_count: tab_count, // Required by the click
        children: []
      };
      // Get all tables and build hierarchy
      let tables = get_tables(db);
      let flat_table = flat_tables(tables);
      flat_table.forEach(async wdgt => {
        console.log('WIDGET',wdgt);
        // Attach the tab to the `toolset`
        if (wdgt.widget == 'toolmenu') {
          console.log('ADD TOOLMENU',wdgt);
          // wdgt.parent = db.id;
          wdgt.index = tab_count;
          tab_count++;
          root.children.push(wdgt);
        }
        else if (wdgt.widget === 'radio_tool') {
          // Load radio_tool (radio button + toolset)
          const source = await fetchFile(tab.path + wdgt.filename);
          console.info('SOURCE',tab.path + wdgt.filename,source);
          // Create the toolset - parent of all the tool tabs
          let toolset = Object.assign({}, wdgt);
          toolset.widget = 'toolset';
          toolset.index = tab_count;
          toolset.parent = root.id;
          tab_count += 4;
          const tool = build_tree(source.datablocks.default,toolset);
          console.info('THE TOOL',tool);
          root.children.push(tool);
          // Create the radio button
          wdgt.id += '_radio';
          wdgt.widget = 'radio';
          wdgt.on_click = (e) => {
            Array.from(document.querySelectorAll('.toolset')).map(el => el.style.display = 'none');
            document.getElementById(toolset.id).style.display = 'block';
          }
          delete wdgt.children;
          const index = flat_table.map(e => e.id).indexOf(wdgt.parent);
          console.info('FIND PARENT',index,wdgt,flat_table[index]);
          flat_table[index].children.push(wdgt);         
        }
        else if ('parent' in wdgt) {
          // Attach other widgets depending of their parent.
          const index = flat_table.map(e => e.id).indexOf(wdgt.parent);
          console.info('FIND PARENT',index,wdgt,flat_table[index]);
          flat_table[index].children.push(wdgt);
        }
      }); 
      // Prepare all the widgets tree
      console.info('TOOLS',root)

      all_of_them.push(root);
    }
    return all_of_them;
  }
