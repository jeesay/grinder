data_
#
loop_
_external.id
_external.label
_external.icon
_external.widget
_external.value
_external.help
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
outdata              "Output Data"                            bi-box-arrow-down    fieldset   ?          hidden     ?
nodes                "Nodes"                                  bi-controller        fieldset   ?          hidden     ?
system               "System"                                 bi-incognito         fieldset   ?          hiddden    ?
external_cmd         "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
fn_exe               "External executable:"              file       ?               ""              "."             "?"             required        
; Location of the script that will launch the external program.
This script should write all its output in the directory specified with --o.
Also, it should write in that same directory a file called RELION_JOB_EXIT_SUCCESS upon successful exit, and RELION_JOB_EXIT_FAILURE upon failure.
;
in_mov               "Input movies: "                    file       ?               "MicrographMovieGroupMetadata.star.relion" 1               "movie STAR file (*.star)" required        
; Input movies.
This will be passed with a --in_movies argument to the executable.
;
in_mic               "Input micrographs: "               file       ?               "MicrographGroupMetadata.star.relion" 1               "micrographs STAR file (*.star)" required        
; Input micrographs.
This will be passed with a --in_mics argument to the executable.
;
in_part              "Input particles: "                 file       ?               "ParticleGroupMetadata.star.relion" 1               "particles STAR file (*.star)" required        
; Input particles.
This will be passed with a --in_parts argument to the executable.
;
in_coords            "Input coordinates: "               file       ?               "MicrographCoordsGroup.star.relion" 1               "STAR files (coords_suffix*.star)" required        
; Input coordinates.
This will be passed with a --in_coords argument to the executable.
;
in_3dref             "Input 3D reference: "              file       ?               "DensityMap.mrc" 1               "MRC files (*.mrc)" required        
; Input 3D reference map.
This will be passed with a --in_3dref argument to the executable.
;
in_mask              "Input 3D mask: "                   file       ?               "Mask3D.mrc"    1               "MRC files (*.mrc)" required        
; Input 3D mask.
This will be passed with a --in_mask argument to the executable.
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
_outdata.constraint
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
_nodes.constraint
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
_system.constraint
_system.help
#
loop_
_external_cmd.id
_external_cmd.label
_external_cmd.widget
_external_cmd.default
_external_cmd.arg0
_external_cmd.arg1
_external_cmd.arg2
_external_cmd.constraint
_external_cmd.help
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.display
_settings.help
general              "General"                                bi-chat-right-text   fieldset   ?          show       ?
#
loop_
_general.id
_general.label
_general.widget
_general.default
_general.arg0
_general.arg1
_general.arg2
_general.constraint
_general.help
param1_label         "Param1 - label:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param1_value         "Param1 - value:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param2_label         "Param2 - label:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param2_value         "Param2 - value:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param3_label         "Param3 - label:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param3_value         "Param3 - value:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param4_label         "Param4 - label:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param4_value         "Param4 - value:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param5_label         "Param5 - label:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param5_value         "Param5 - value:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param6_label         "Param6 - label:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param6_value         "Param6 - value:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param7_label         "Param7 - label:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param7_value         "Param7 - value:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param8_label         "Param8 - label:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param8_value         "Param8 - value:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param9_label         "Param9 - label:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param9_value         "Param9 - value:"                   string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param10_label        "Param10 - label:"                  string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
param10_value        "Param10 - value:"                  string     ?               "?"             "?"             "?"             ?               
; Define label and value for optional parameters to the script.
These will be passed as an argument --label value
;
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
