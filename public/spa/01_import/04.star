data_
#
loop_
_import_parts.id
_import_parts.label
_import_parts.icon
_import_parts.widget
_import_parts.value
_import_parts.help
io                   "I/O"                     bi-arrow-down-up     tab              ?        ?
log                  "Log"                     bi-binoculars-fill   tab              ?        ?
dataviz              "DataViz"                 bi-eye               tab              ?        ?
#
loop_
_io.id
_io.label
_io.icon
_io.widget
_io.value
_io.display
_io.help
nodtyp               "File Type"              bi-file-earmark      fieldset   ?          show       ?
indata               "Input Data"             bi-box-arrow-in-down fieldset   ?          show       ?
params_01            "Parameters"             bi-chat-right-text   fieldset   ?          show       ?
outdata              "Output Data"            bi-box-arrow-down    fieldset   ?          hidden     ?
nodes                "Nodes"                  bi-controller        fieldset   ?          hidden     ?
system               "System"                 bi-incognito         fieldset   ?          hiddden    ?
import_ptcls_cmd     "Check command"          bi-chat-right-text   cli        ?          show       ?
#
loop_
_indata.id
_indata.label
_indata.widget
_indata.default
_indata.arg0
_indata.arg1
_indata.arg2
_indata.state
_indata.help
fn_in_other          "Input file:"                       file       path/ptcls/*.star         "Input file (*.*)" "."             "?"             required        
; Select any file(s) to import.
Note that for importing coordinate files, one has to give a Linux wildcard, where the *-symbol is before the coordinate-file suffix, e.g.
if the micrographs are called mic1.mrc and the coordinate files mic1.box or mic1_autopick.star, one HAS to give '*.box' or '*_autopick.star', respectively.
 
Also note that micrographs, movies and coordinate files all need to be in the same directory (with the same rootnames, e.g.mic1 in the example above) in order to be imported correctly.
3D masks or references can be imported from anywhere.
 
Note that movie-particle STAR files cannot be imported from a previous version of RELION, as the way movies are handled has changed in RELION-2.0.

For the import of a particle, 2D references or micrograph STAR file or of a 3D reference or mask, only a single file can be imported at a time.
;
#
loop_
_nodtyp.id
_nodtyp.label
_nodtyp.widget
_nodtyp.default
_nodtyp.help
node_type                    "Node type:"                           select     0                                    "Select the type of Node this is."
node_type::node_type_opt_00  "Particle coordinates"                 option     "MicrographCoordsGroup.star.relion"  "Particle coordinates (*.box, *_pick.star)"
node_type::node_type_opt_01  "Particles STAR file"                  option     "ParticleGroupMetadata.star.relion"  "Particles STAR file (.star)"
#
loop_
_params_01.id
_params_01.label
_params_01.widget
_params_01.default
_params_01.arg0
_params_01.arg1
_params_01.arg2
_params_01.state
_params_01.help
optics_group_particles       "Rename optics group for particles:"        string     ?               "?"             "?"             "?"             ?               
; Only for the import of a particles STAR file with a single, or no, optics groups defined: rename the optics group 
for the imported particles to this string.
;
#
loop_
_outdata.id
_outdata.label
_outdata.widget
_outdata.default
_outdata.arg0
_outdata.arg1
_outdata.arg2
_outdata.state
_outdata.help
#
loop_
_nodes.id
_nodes.label
_nodes.widget
_nodes.default
_nodes.arg0
_nodes.arg1
_nodes.arg2
_nodes.state
_nodes.help
#
loop_
_system.id
_system.label
_system.widget
_system.default
_system.arg0
_system.arg1
_system.arg2
_system.state
_system.help
do_raw               "Import raw movies/micrographs?"    bool       false           "?"             "?"             "?"             ?               
; Set this to Yes if you plan to import raw movies or micrographs
;
do_other             "Import other node types?"          bool       true            "?"             "?"             "?"             ?               
; Set this to Yes if you plan to import anything else than movies or micrographs
;
#
loop_
_import_ptcls_cmd.type
_import_ptcls_cmd.arg
_import_ptcls_cmd.param
prog    "grinder import"         ?      
param   --type                   node_type
param   --i                      fn_in_other      
param   --odir                   Import/${RELION_NEW_JOB}/ 
param   --ofile                  outfile
param   --optics_group_name      optics_group_particles
param   --pipeline-control       Import/${RELION_NEW_JOB}/ 
#
loop_
_log.id
_log.label
_log.icon
_log.widget
_log.value
_log.display
_log.help
#
loop_
_dataviz.id
_dataviz.label
_dataviz.icon
_dataviz.widget
_dataviz.value
_dataviz.display
_dataviz.help
#
