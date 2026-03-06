data_
#
loop_
_import_other.id
_import_other.label
_import_other.icon
_import_other.widget
_import_other.value
_import_other.help
io                   "I/O"                      bi-arrow-down-up    tab              ?        ?
settings             "Settings"                bi-tools             tab              ?        ?
log                  "Log"                     bi-binoculars-fill   tab              ?        ?
dataviz              "DataViz"                 bi-eye               tab              ?        ?
#
loop_
_io.id
_io.label
_io.icon
_io.widget
_io.value
_io.help
indata               "Input Data"                             bi-box-arrow-in-down fieldset   ?          ?
outdata              "Output Data"                            bi-box-arrow-down    fieldset   ?          ?
nodes                "Nodes"                                  bi-controller        fieldset   ?          ?
system               "System"                                 bi-incognito         fieldset   ?          ?
import_other_cmd     "Check command"                          bi-chat-right-text   cli        ?          ?
#
loop_
_indata.id
_indata.label
_indata.widget
_indata.default
_indata.arg0
_indata.arg1
_indata.arg2
_indata.help
fn_in_other          "Input file:"                       file       ref.mrc         "Input file (*.*)" .               ?               
; Select any file(s) to import.

 
 Note that for importing coordinate files, one has to give a Linux wildcard, where the *-symbol is before the coordinate-file suffix, e.g.
if the micrographs are called mic1.mrc and the coordinate files mic1.box or mic1_autopick.star, one HAS to give '*.box' or '*_autopick.star', respectively.
 
 Also note that micrographs, movies and coordinate files all need to be in the same directory (with the same rootnames, e.g.mic1 in the example above) in order to be imported correctly.
3D masks or references can be imported from anywhere.

 
 Note that movie-particle STAR files cannot be imported from a previous version of RELION, as the way movies are handled has changed in RELION-2.0.

 
 For the import of a particle, 2D references or micrograph STAR file or of a 3D reference or mask, only a single file can be imported at a time.

 
 Note that due to a bug in a fltk library, you cannot import from directories that contain a substring  of the current directory, e.g.
dont important from /home/betagal if your current directory is called /home/betagal_r2.
In this case, just change one of the directory names.
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
_system.help
do_raw               "Import raw movies/micrographs?"    bool       false           "?"             ?               ?               
; Set this to Yes if you plan to import raw movies or micrographs
;
do_other             "Import other node types?"          bool       true            "?"             ?               ?               
; Set this to Yes if you plan to import anything else than movies or micrographs
;
#
loop_
_import_other_cmd.id
_import_other_cmd.label
_import_other_cmd.widget
_import_other_cmd.default
_import_other_cmd.arg0
_import_other_cmd.arg1
_import_other_cmd.arg2
_import_other_cmd.help
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.help
params_01            "Parameters"                             bi-chat-right-text   fieldset   ?          ?
node_type            "Options"                                bi-chat-right-text   fieldset   ?          ?
#
loop_
_params_01.id
_params_01.label
_params_01.widget
_params_01.default
_params_01.arg0
_params_01.arg1
_params_01.arg2
_params_01.help
node_type            "Node type:"                        select     0               "LABEL_IMPORT_2DIMG" ?               ?               "Select the type of Node this is."
optics_group_particles "Rename optics group for particles:" string                     "?"             ?               ?               
; Only for the import of a particles STAR file with a single, or no, optics groups defined: rename the optics group for the imported particles to this string.
;
#
loop_
_node_type.id
_node_type.label
_node_type.widget
_node_type.default
_node_type.arg0
_node_type.arg1
_node_type.arg2
_node_type.help
node_type_opt_00     "Multiple (2D or 3D) references (.star or .mrcs)" option     LABEL_IMPORT_2DIMG "?"             ?               ?               "?"
node_type_opt_01     "Micrographs STAR file (.star)"     option     LABEL_IMPORT_MICS "?"             ?               ?               "?"
node_type_opt_02     "3D reference (.mrc)"               option     LABEL_IMPORT_MAP "?"             ?               ?               "?"
node_type_opt_03     "3D mask (.mrc)"                    option     LABEL_IMPORT_MASK "?"             ?               ?               "?"
node_type_opt_04     "Unfiltered half-map (unfil.mrc)"   option     LABEL_IMPORT_HALFMAP "?"             ?               ?               "?"
#
loop_
_log.id
_log.label
_log.icon
_log.widget
_log.value
_log.help
#
loop_
_dataviz.id
_dataviz.label
_dataviz.icon
_dataviz.widget
_dataviz.value
_dataviz.help
#
