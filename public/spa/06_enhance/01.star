data_
#
loop_
_mask_create.id
_mask_create.label
_mask_create.icon
_mask_create.widget
_mask_create.value
_mask_create.help
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
mask_create_cmd      "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
fn_in                "Input 3D map:"                     file       ?               "DensityMap.mrc" 1               "MRC map files (*.mrc)" required        
; Provide an input MRC map from which to start binarizing the map.
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
_mask_create_cmd.id
_mask_create_cmd.label
_mask_create_cmd.widget
_mask_create_cmd.default
_mask_create_cmd.arg0
_mask_create_cmd.arg1
_mask_create_cmd.arg2
_mask_create_cmd.constraint
_mask_create_cmd.help
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
params_01            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
parallel_computing   "Parallel Computing"                     bi-chat-right-text   fieldset   ?          show       ?
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
lowpass_filter       "Lowpass filter map (A)"            range      15              10              100             5               ?               
; Lowpass filter that will be applied to the input map, prior to binarization.
To calculate solvent masks, a lowpass filter of 15-20A may work well.
;
angpix               "Pixel size (A)"                    range      -1              0.3             5               0.1             ?               
; Provide the pixel size of the input map in Angstroms to calculate the low-pass filter.
This value is also used in the output image header.
;
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
inimask_threshold    "Initial binarisation threshold:"   range      0.02            0.0             0.5             0.01            ?               
; This threshold is used to make an initial binary mask from the average of the two unfiltered half-reconstructions.
If you don't know what value to use, display one of the unfiltered half-maps in a 3D surface rendering viewer and find the lowest threshold that gives no noise peaks outside the reconstruction.
;
extend_inimask       "Extend binary map this many pixels:" range      3               0               20              1               ?               
; The initial binary mask is extended this number of pixels in all directions.
;
width_mask_edge      "Add a soft-edge of this many pixels:" range      3               0               20              1               ?               
; The extended binary mask is further extended with a raised-cosine soft edge of the specified width.
;
#
loop_
_parallel_computing.id
_parallel_computing.label
_parallel_computing.widget
_parallel_computing.default
_parallel_computing.arg0
_parallel_computing.arg1
_parallel_computing.arg2
_parallel_computing.constraint
_parallel_computing.help
nr_threads           "Number of threads:"                range      {QSUB_NRTHREADS_VAL} 1               "{RELION_THREAD_MAX}" 1               ?               
; Number of shared-memory (POSIX) threads to use in parallel.
When set to 1, no multi-threading will be used.
The maximum can be set through the environment variable RELION_THREAD_MAX.
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
