data_
#
loop_
_sub_coor.id
_sub_coor.label
_sub_coor.icon
_sub_coor.widget
_sub_coor.value
_sub_coor.help
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
sub_coor_cmd         "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
fn_opt               "Input optimiser.star: "            file       ?               "OptimiserData.star.relion" 1               "STAR Files (*_optimiser.star)" ?               
; Select the *_optimiser.star file for the iteration of the 3D refinement/classification which you want to use for subtraction.
It will use the maps from this run for the subtraction, and of no particles input STAR file is given below, it will use all of the particles from this run.
;
fn_mask              "Mask of the signal to keep:"       file       ?               "Mask3D.mrc"    1               "Image Files (*.{spi,vol,msk,mrc})" required        
; Provide a soft mask where the protein density you wish to subtract from the experimental particles is black (0) and the density you wish to keep is white (1).
;
fn_data              "Input particle star file:"         file       ?               "ParticleGroupMetadata.star.relion" 1               "particle STAR file (*.star)" required        
; The particle STAR files with particles that will be used in the subtraction.
Leave this field empty if all particles from the input refinement/classification run are to be used.
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
do_center_mask       "Do center subtracted images on mask?" bool       false           "?"             "?"             "?"             ?               
; If set to Yes, the subtracted particles will be centered on projections of the center-of-mass of the input mask.
;
do_center_xyz        "Do center on my coordinates?"      bool       true            "?"             "?"             "?"             ?               
; If set to Yes, the subtracted particles will be centered on projections of the x,y,z coordinates below.
The unit is pixel, not angstrom.
The origin is at the center of the box, not at the corner.
;
#
loop_
_sub_coor_cmd.id
_sub_coor_cmd.label
_sub_coor_cmd.widget
_sub_coor_cmd.default
_sub_coor_cmd.arg0
_sub_coor_cmd.arg1
_sub_coor_cmd.arg2
_sub_coor_cmd.constraint
_sub_coor_cmd.help
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
do_fliplabel         "OR revert to original particles?"       bi-chat-right-text   switch     ?          show       ?
do_center_xyz_fs     "Do center on my coordinates?"           bi-chat-right-text   switch     ?          show       ?
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
do_float16           "Write output in float16?"          bool       true            "?"             "?"             "?"             ?               
; If set to Yes, this program will write output images in float16 MRC format.
This will save a factor of two in disk space compared to the default of writing in float32.
Note that RELION and CCPEM will read float16 images, but other programs may not (yet) do so.
;
#
loop_
_do_fliplabel.id
_do_fliplabel.label
_do_fliplabel.widget
_do_fliplabel.default
_do_fliplabel.arg0
_do_fliplabel.arg1
_do_fliplabel.arg2
_do_fliplabel.constraint
_do_fliplabel.help
fn_fliplabel         "revert this particle star file:"   file       ?               "ParticleGroupMetadata.star.relion" 1               "particle STAR file (*.star)" ?               
; The particle STAR files with particles that will be used for label reversion.
;
#
loop_
_do_center_xyz_fs.id
_do_center_xyz_fs.label
_do_center_xyz_fs.widget
_do_center_xyz_fs.default
_do_center_xyz_fs.arg0
_do_center_xyz_fs.arg1
_do_center_xyz_fs.arg2
_do_center_xyz_fs.constraint
_do_center_xyz_fs.help
center_x             "Center coordinate (pix) - X:"      string     0               "?"             "?"             "?"             ?               "X-coordinate of the 3D center (in pixels)."
center_y             "Center coordinate (pix) - Y:"      string     0               "?"             "?"             "?"             ?               "Y-coordinate of the 3D center (in pixels)."
center_z             "Center coordinate (pix) - Z:"      string     0               "?"             "?"             "?"             ?               "Z-coordinate of the 3D center (in pixels)."
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
new_box              "New box size:"                     range      -1              64              512             32              ?               
; Provide a non-negative value to re-window the subtracted particles in a smaller box size.
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
nr_mpi               "Number of MPI procs:"              range      {QSUB_NRMPI_VAL} 1               "{RELION_MPI_MAX}" 1               ?               
; Number of MPI nodes to use in parallel.
When set to 1, MPI will not be used.
The maximum can be set through the environment variable RELION_MPI_MAX.
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
