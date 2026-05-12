// import { tableFromIPC } from 'apache-arrow';
import {StarGate} from "./stargate.js";
import {w_alert, w_leftpanel, w_tab_tools} from "./widget.js";
import { build_widget_tree } from "./job.js";
import {h} from "./dom.js";
import {WSClient} from "./ws_client.js";


//import {*} from "./dom.js";
//import {*} from "./job.js";
//import {*} from "./history.js";
//import {*} from "./browse.js";
//import {*} from "./widget.js";
import { drawHistogram, drawScatterPlot } from "./dataviz.js"

import * as aq from "https://esm.sh/arquero@7";

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
export  const connect_to_ws_server = async () => {
  const ip_address = document.querySelector('input.param[data-param=ws_server_ip]').value;
  const port = document.querySelector('input.param[data-param=ws_port]').value;
  console.info('WS',`ws://${ip_address}:${port}/welcome`);
  // Open the WebSocket connection and register event handlers.
  // await GRINDER.server.connect(`ws://${ip_address}:${port}/welcome`);
 
  return new Promise((resolve, reject) => {
        // 1. Create the connection
        console.info('New connection to welcome');
        const socket = new WebSocket(`ws://${ip_address}:${port}/welcome`);

        // 2. Handle connection open
        socket.onopen = () => {
            // Do nothing
            socket.send('welcome');
            w_alert(`[Open] Connection established with server ws://${ip_address}:${port}/welcome`,'success');
        };

        // 3. Handle the result
        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            socket.close(); // Close connection after getting the data
            const info = {ip:ip_address,port: port, connected: true,env: data.environment};
            localStorage.setItem('connection',JSON.stringify(info));
            // Update the UI when the server responds
            document.getElementById('connect_fs').classList.toggle('hidden');
            document.getElementById('connected').classList.toggle('hidden');
            // Update icon
            document.getElementById('connect').innerHTML = '<i class="bi bi-wifi"></i>Connected';
            document.getElementById('connect').style.color = 'lightgreen';
            document.getElementById('connect').dataset.ip = info.ip;
            document.getElementById('connect').dataset.port = info.port;
            resolve(data);
        };

        // 4. Handle errors
        socket.onerror = (error) => {
          w_alert(`[Close] Connection failed with server ws://${ip_address}:${port}/welcome`,'error');
          reject(error);
        }
    });
}


/*
 * Run the WebSocket Client and try to connect to the python WebSocket server
*/
export  const load_project = async (project_path) => {
  const connect = JSON.parse(localStorage.getItem('connection'));
  console.log(connect);
  const ip_address = connect.ip;
  const port = connect.port;
  console.info('WS',`ws://${ip_address}:${port}/project`);
  // Open the WebSocket connection and register event handlers.
  // await GRINDER.server.connect(`ws://${ip_address}:${port}/welcome`);
 
  return new Promise((resolve, reject) => {
        // 1. Create the connection
        const socket = new WebSocket(`ws://${ip_address}:${port}/project`);

        // 2. Handle connection open
        socket.onopen = () => {
          // Update the UI when the server responds
          socket.send(project_path);
        };

        // 3. Handle the result
        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            socket.close(); // Close connection after getting the data
            const p = {path: project_path,last_job_id: data.pipeline.rlnPipeLineJobCounter}
            w_alert(`Project <strong>${project_path}</strong> loaded...`,'success');
            localStorage.setItem('current_project',JSON.stringify(p));
            resolve(data);
        };

        // 4. Handle errors
        socket.onerror = (error) => {
          w_alert(`[Close] Connection failed with server ws://${ip_address}:${port}/project`,'error');
          reject(error);
        }
    });
}

/*
 * Run the WebSocket Client and try to connect to the python WebSocket server
*/
export  const read_job = async (obj) => {
  const connect = JSON.parse(localStorage.getItem('connection'));
  const ip_address = connect.ip;
  const port = connect.port;
  console.info('WS',`ws://${ip_address}:${port}/job/read`);
  // Open the WebSocket connection and register event handlers.
  // await GRINDER.server.connect(`ws://${ip_address}:${port}/welcome`);
 
  return new Promise((resolve, reject) => {
        // 1. Create the connection
        const socket = new WebSocket(`ws://${ip_address}:${port}/job/read`);

        // 2. Handle connection open
        socket.onopen = () => {
          // Update the UI when the server responds
          const msg = {projpath:obj.projpath,dirname:obj.path,jobname:obj.job};
          console.info(msg, JSON.stringify(msg));
          socket.send(JSON.stringify(msg));
        };

        // 3. Handle the result
        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            socket.close(); // Close connection after getting the data
            console.log(data);
            const nodetype = data.params_head.rlnJobTypeLabel;
            // Step #0 - Update toolbar
            const jb = document.getElementById('job_id');
            jb.dataset.nodetype = nodetype;
            document.querySelector('#tag_id span').textContent = nodetype;
            // Step #1 - Update: get gui from obj.nodetype
            const ui = JSON.parse(localStorage.getItem(nodetype));
            const widgets = build_widget_tree(ui.datablocks.default, {children: []});
            // Section
            let section = document.getElementById('main-panel');
            section.innerHTML = '';
            // Create tabs...
            w_tab_tools(section, widgets);
            // Reset display
            section.style.display = 'block';
            section.querySelector('input').checked = true; // First child
            // Step #2 - Fill Log Tab
            document.querySelector('#Log.tab .tab-content').innerHTML = '';
            document.querySelector('#Log.tab .tab-content').appendChild(h('pre.log-content',data.log));
            // Step #3 - Fill all the widgets with the job values
            const RLN_VAR = data.params.columns.indexOf('rlnJobOptionVariable');
            const RLN_VAL = data.params.columns.indexOf('rlnJobOptionValue');
            [...document.querySelectorAll('.param')].forEach((w) => {
              const key = w.dataset.param;
              const row = data.params.data.filter( r => r[RLN_VAR] === key)[0];
              if (w.type === 'checkbox') {
                w.checked = (row[RLN_VAL] === 'Yes') ? true : false;
              }
              else {
                w.value = row[RLN_VAL];
              }

            });
            resolve(data);
          };
        // 4. Handle errors
        socket.onerror = (error) => {
          w_alert(`[Close] Connection failed with server ws://${ip_address}:${port}/job/read`,'error');
          reject(error);
        }
    });
}

/*
 * Run the WebSocket Client and try to connect to the python WebSocket server
*/
export  const run_job = async () => {
  // Step #1 - Get connection info
  const connect = JSON.parse(localStorage.getItem('connection'));
  const ip_address = connect.ip;
  const port = connect.port;

  // Step #2 - Get all the widgets values
  const supers  = document.querySelectorAll('.super.param');
  const hidden_div_exists = document.querySelector('section .option_g');
  console.log(hidden_div_exists);
  const regulars = (hidden_div_exists) ? document.querySelectorAll(`section .option_g:not(.hidden) .param`) : document.querySelectorAll(`section .param`);
  const all_params = new Set([...supers,...regulars]);
  console.info(all_params);
  const joboptions = [...all_params].map((w) => {
    console.log(w);
    const key = w.dataset.param;
    let value = null;
    if (w.type === 'checkbox') {
      value = (w.checked) ? true : false;
    }
    else {
      value = w.value;
    }
    return {key,value};
  });
  const current_project = JSON.parse(localStorage.getItem('current_project'));
  const current_job = JSON.parse(localStorage.getItem('current_job'));
  const nodes = [...document.querySelectorAll('.node')];

  // Step #3 - Get the CLI
  const tag = current_job.tag;
  const cli = current_job.command;
  const cargo = new StarGate();
  cargo.from_json(JSON.parse(localStorage.getItem(tag)));
  const cmd = cargo.datablock('default').table(cli);
  console.log(cmd);
  // Ready to send...
  const metadata = {current_project,current_job,joboptions,nodes,command: cmd};
  
  // Open the WebSocket connection and register event handlers.
  // await GRINDER.server.connect(`ws://${ip_address}:${port}/welcome`);
 
  return new Promise((resolve, reject) => {
        // 1. Create the connection
        const socket = new WebSocket(`ws://${ip_address}:${port}/job/run`);

        // 2. Handle connection open
        socket.onopen = () => {
          // Update the UI when the server responds
          console.info(metadata);
          socket.send(JSON.stringify(metadata));
        };

        // 3. Handle the result
        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            console.log(data);
            const nodetype = data.params_head.rlnJobTypeLabel;
            // Step #0 - Update toolbar
            const jb = document.getElementById('job_id');
            jb.dataset.nodetype = nodetype;
            document.querySelector('#tag_id span').textContent = nodetype;
            // Step #1 - Update: get gui from obj.nodetype
            const ui = JSON.parse(localStorage.getItem(nodetype));
            const widgets = build_widget_tree(ui.datablocks.default, {children: []});
            // Section
            let section = document.getElementById('main-panel');
            section.innerHTML = '';
            // Create tabs...
            w_tab_tools(section, widgets);
            // Reset display
            section.style.display = 'block';
            section.querySelector('input').checked = true; // First child
            // Step #2 - Fill Log Tab
            document.querySelector('#Log.tab .tab-content').innerHTML = '';
            document.querySelector('#Log.tab .tab-content').appendChild(h('pre',data.log));
            resolve(data);
            socket.close(); // Close connection after getting the data
          };
        // 4. Handle errors
        socket.onerror = (error) => {
          w_alert(`[Close] Connection failed with server ws://${ip_address}:${port}/job/read`,'error');
          reject(error);
        }
    });
}

/*
 * Run the WebSocket Client and try to connect to the python WebSocket server
*/
export  const read_data = async (obj) => {
  const connect = JSON.parse(localStorage.getItem('connection'));
  const ip_address = connect.ip;
  const port = connect.port;
  console.info('WS',`ws://${ip_address}:${port}/job/data`);
  // Open the WebSocket connection and register event handlers.
  // await GRINDER.server.connect(`ws://${ip_address}:${port}/welcome`);
 
  return new Promise((resolve, reject) => {
        // 1. Create the connection
        const socket = new WebSocket(`ws://${ip_address}:${port}/job/data`);

        // 2. Handle connection open
        socket.onopen = () => {
          // Update the UI when the server responds
          const msg = {projpath:obj.projpath,dirname:obj.path,jobname:obj.job};
          console.info(msg, JSON.stringify(msg));
          const form = localStorage.getItem(obj.nodetype);
          // console.log("TESSSSSSSTTTTTTTTTTT", form);
          const s = {"request" : JSON.stringify(msg), "data": form}
          socket.send(JSON.stringify(s));
        };

        // 3. Handle the result
        socket.onmessage = (event) => {
            const msg = JSON.parse(event.data);
            console.log(msg);
            // // Update: form from obj.nodetype
            // const form = localStorage.getItem(obj.nodetype);
            // console.log(form);

            if (msg.type == "dataviz_package"){
              Object.entries(msg.widget).forEach(([id, config]) => {
                // config.data contain { rlnIndex: [...], rlnAccumMotionTotal: [...] }
                const data = config.data;
                
                const targetId = id.split('::')[1];
                console.log(targetId);
                // const container = document.querySelector(`div#${targetId}.canvas`);
                const container = document.getElementById(targetId)
                console.log(`Recherche de ${targetId}:`, container); // <--- CHECK 

              if (container) {
                  // We empty the div just in case
                  container.innerHTML = "";
                  
                  // The correct function is called according to the type
                  if (config.widget === 'g_hist') {
                      drawHistogram(container, data, config);
                      console.log(`Tentative de dessin réussie pour ${id}`);
                  } 
                  else if (config.widget === 'g_plot') {
                      drawScatterPlot(container, data, config);
                      console.log(`Tentative de dessin réussie pour ${id}`);
                  }
              }

                // if (!container) return;
                // let fig = null;
                // if (config.widget === 'g_hist') {
                //     drawHistogram(container, data, config);
                // } else if (config.widget === 'g_plot') {
                //     drawScatterPlot(container, data, config);
                // }
                // if (fig) { 
                //   container.appendChild(fig);
                // };
              });
            }
          
            // socket.close(); // Close connection after getting the data
            // resolve(msg);
        };

        // Handle errors
        socket.onerror = (error) => {
          w_alert(`[Close] Connection failed with server ws://${ip_address}:${port}/job/data`,'error');
          reject(error);
        }
    });
}

export const read_log = async (obj) => {
    const connect = JSON.parse(localStorage.getItem('connection'));
    const ip_address = connect.ip;
    const port = connect.port;
    
    console.info('WS',`ws://${ip_address}:${port}/log/test`);

    return new Promise((resolve, reject) => {
        const socketUrl = `ws://${ip_address}:${port}/log/test`;
        const socket = new WebSocket(socketUrl);

        socket.onopen = () => {
            const msg = { 
                projpath: obj.projpath, 
                dirname: obj.path, 
                jobname: obj.job,
                command: "start_monitoring" 
            };
            socket.send(JSON.stringify(msg));
        };

        socket.onmessage = (event) => {
            const msg = JSON.parse(event.data);

            if (msg.type === "log_update") {
                appendLine(msg.content); 
            }
            resolve(msg);
        };

        socket.onerror = (error) => {
          console.log(error);
            w_alert(`Log error ${socketUrl} ${error}`, 'error');
            reject(error);
        };

        socket.onclose = (event) => {
          w_alert(`Log closed ${socketUrl} ${event.code} ${event.reason}`, 'info');
            console.log("Stream closed");
        };
        
        // We can link socket to window object to close it later
        window.currentLogSocket = socket;
    });
}

function appendLine(text, isSystem = false) {
    const div = document.createElement('div');
    div.className = isSystem ? 'log-line system-msg' : 'log-line';
    const timestamp = new Date().toLocaleTimeString();
    div.textContent = `[${timestamp}] ${text}`;
    terminal.appendChild(div);
    
    // Auto-scroll vers le bas
    terminal.scrollTop = terminal.scrollHeight;
}

export  const compute_data = async (obj) => {
  const connect = JSON.parse(localStorage.getItem('connection'));
  const ip_address = connect.ip;
  const port = connect.port;
  console.info('WS',`ws://${ip_address}:${port}/job/compute`);
  // Open the WebSocket connection and register event handlers.
  // await GRINDER.server.connect(`ws://${ip_address}:${port}/welcome`);
 
  return new Promise((resolve, reject) => {
        // 1. Create the connection
        const socket = new WebSocket(`ws://${ip_address}:${port}/job/compute`);

        // 2. Handle connection open
        socket.onopen = () => {
          // Update the UI when the server responds
          const msg = {projpath:obj.projpath,dirname:obj.path,jobname:obj.job};
          console.info(msg, JSON.stringify(msg));
          const form = localStorage.getItem(obj.nodetype);
          // console.log("TESSSSSSSTTTTTTTTTTT", form);
          const s = {"request" : JSON.stringify(msg), "data": form}
          socket.send(JSON.stringify(s));
        };

        // 3. Handle the result
        socket.onmessage = (event) => {
            const msg = JSON.parse(event.data);
            console.log(msg);

        };

        // Handle errors
        socket.onerror = (error) => reject(error);
    });
}

async function fetchParticleStream() {
    const response = await fetch('http://localhost:8000/stream-particles');
    
    // tableFromIPC handles the stream directly from the response body
    const table = await tableFromIPC(response.body);

    // Now you can access the columns with zero-copy speed
    const xCoords = table.getChild('rlnCoordinateX');
    
    console.log(`Loaded ${table.numRows} particles!`);
    
    for (let i = 0; i < table.numRows; i++) {
        // Access coordinates for your visualization
        const x = xCoords.get(i);
    }
}
//   if (GRINDER.server.connected) {
//     // Update the UI when the server responds
//       alert(`[Open] Connection established with server ws://${ip_address}:${port}/welcome`);
//       document.getElementById('connect').innerHTML = '<i class="bi bi-wifi"></i>Connected';
//       document.getElementById('connect').style.color = 'lightgreen';
//       document.getElementById('connect').dataset.ip = ip_address;
//       document.getElementById('connect').dataset.port = port;
      

//       const data = await GRINDER.server.receive();
//       document.getElementById('project').innerHTML = data;
//   }
//   else {
//       alert(`[Fail] Unable to connect to the server ws://${ip_address}:${port}/`);
//   }
// }

/*
 * Run the WebSocket Client and try to connect to the python WebSocket server
*/
// export const get_file_tree = async () => {
 
//   const socket = new WebSocket("ws://localhost:20000/ws/file-tree");

//   function requestTree(path, depth) {
//       const payload = {
//           path: path,
//           depth: depth
//       };
//       socket.send(JSON.stringify(payload));
//   }

//   // Example: Trigger with depth 2 on button click
//   refreshBtn.addEventListener("click", () => {
//       requestTree(".", 2); 
//   });
// };

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

/* Move in `job.js`
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

  const build_widget_tree = (datablock,parent) => {
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
                      document.getElementById('job_id').textContent = 'New Job';
                      update_job_toolbar('new_job');
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

  */
