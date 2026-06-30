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
_io.display
_io.help
indata               "Input Data"                             bi-box-arrow-in-down fieldset   ?          show       ?
nodes                "Nodes"                                  bi-controller        fieldset   ?          hidden     ?
system               "System"                                 bi-incognito         fieldset   ?          hiddden    ?
import_other_prgm    "Script"                                 bi-chat-right-text   cli        ?          show       ?
import_other_cmd     "Check command"                          bi-chat-right-text   cli        ?          show       ?
#
loop_
_indata.id
_indata.label
_indata.widget
_indata.default
_indata.arg0
_indata.arg1
_indata.arg2
_indata.constraint
_indata.help
fn_in_other          "Input file:"                       file       ref.mrc                        "Input file (*.*)" "."             "?"             required        
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
_nodes.id
_nodes.label
_nodes.widget
_nodes.default
_nodes.arg0
_nodes.arg1
_nodes.arg2
_nodes.constraint
_nodes.help
outnode_00           outnode_00                          outnode    MotionCorr/${RELION_NEW_JOB}/movies.star MicrographMovieGroupMetadata.star.relion ?               ?               ?               ""No Help""
outnode_01           outnode_01                          outnode    MotionCorr/${RELION_NEW_JOB}/micrographs.star MicrographGroupMetadata.star.relion ?               ?               ?               ""No Help""
outnode_02           outnode_02                          outnode    MotionCorr/${RELION_NEW_JOB}/coords_suffix{fn_in_other} MicrographCoordsGroup.star.relion ?               ?               ?               ""No Help""
outnode_03           outnode_03                          outnode    MotionCorr/${RELION_NEW_JOB}/{fn_in_other} ParticleGroupMetadata.star.relion ?               ?               ?               ""No Help""
outnode_04           outnode_04                          outnode    MotionCorr/${RELION_NEW_JOB}/{fn_in_other} Image2DGroupMetadata.star.relion ?               ?               ?               ""No Help""
outnode_05           outnode_05                          outnode    MotionCorr/${RELION_NEW_JOB}/{fn_in_other} DensityMap.mrc  ?               ?               ?               ""No Help""
outnode_06           outnode_06                          outnode    MotionCorr/${RELION_NEW_JOB}/{fn_in_other} Mask3D.mrc      ?               ?               ?               ""No Help""
outnode_07           outnode_07                          outnode    MotionCorr/${RELION_NEW_JOB}/{fn_in_other} MicrographGroupMetadata.star.relion ?               ?               ?               ""No Help""
outnode_08           outnode_08                          outnode    MotionCorr/${RELION_NEW_JOB}/{fn_in_other} DensityMap.mrc.halfmap ?               ?               ?               ""No Help""
outnode_09           outnode_09                          outnode    MotionCorr/${RELION_NEW_JOB}/{fn_in_other} ParticleGroupMetadata.star.relion ?               ?               ?               ""No Help""
#
loop_
_system.id
_system.label
_system.widget
_system.default
_system.arg0
_system.arg1
_system.arg2
_system.constraint
_system.help
do_raw               "Import raw movies/micrographs?"    bool       false                          "?"             "?"             "?"             ?               
; Set this to Yes if you plan to import raw movies or micrographs
;
do_other             "Import other node types?"          bool       true                           "?"             "?"             "?"             ?               
; Set this to Yes if you plan to import anything else than movies or micrographs
;
#
loop_
_import_other_prgm.type
_import_other_prgm.arg
_import_other_prgm.param_id
_import_other_prgm.flag
_import_other_prgm.flagvalue
prog    relion_import                                      ?                    ?                    ?                   
param   --optics_group_name                                optics_group_name                                  ?                    ?    
flag    --do_halfmaps                                      ?                                                  node_type            LABEL_IMPORT_HALFMAP
flag    --do_particles                                     ?                                                  node_type            LABEL_PARTS_CPIPE
flag    --optics_group_name                                optics_group_particles                             node_type            LABEL_PARTS_CPIPE
param   --i                                                fn_in                                              ?                    ?    
param   --odir                                             outputname                                         ?                    ?    
param   --ofile                                            fn_out                                             ?                    ?    
param   --pipeline-control                                 MotionCorr/${RELION_NEW_JOB}/                      ?                    ?    
#
loop_
_import_other_cmd.id
_import_other_cmd.label
_import_other_cmd.widget
_import_other_cmd.default
_import_other_cmd.arg0
_import_other_cmd.arg1
_import_other_cmd.arg2
_import_other_cmd.constraint
_import_other_cmd.help
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.display
_settings.help
params_01            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
node_type            "Options"                                bi-chat-right-text   fieldset   ?          show       ?
#
loop_
_params_01.id
_params_01.label
_params_01.widget
_params_01.default
_params_01.arg0
_params_01.arg1
_params_01.arg2
_params_01.constraint
_params_01.help
node_type            "Node type:"                        select     0                              "LABEL_IMPORT_2DIMG" "?"             "?"             ?               "Select the type of Node this is."
optics_group_particles "Rename optics group for particles:" string     ?                              "?"             "?"             "?"             ?               
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
_node_type.constraint
_node_type.help
node_type_opt_00     "Multiple (2D or 3D) references (.star or .mrcs)" option     LABEL_IMPORT_2DIMG             "?"             "?"             "?"             ?               "?"
node_type_opt_01     "Micrographs STAR file (.star)"     option     LABEL_IMPORT_MICS              "?"             "?"             "?"             ?               "?"
node_type_opt_02     "3D reference (.mrc)"               option     LABEL_IMPORT_MAP               "?"             "?"             "?"             ?               "?"
node_type_opt_03     "3D mask (.mrc)"                    option     LABEL_IMPORT_MASK              "?"             "?"             "?"             ?               "?"
node_type_opt_04     "Unfiltered half-map (unfil.mrc)"   option     LABEL_IMPORT_HALFMAP           "?"             "?"             "?"             ?               "?"
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
