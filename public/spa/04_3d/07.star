data_
#
loop_
_dynamight.id
_dynamight.label
_dynamight.icon
_dynamight.widget
_dynamight.value
_dynamight.help
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
dynamight_cmd        "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
fn_star              "Input images STAR file:"           file       ?               "ParticleGroupMetadata.star.relion" 1               "STAR files (*.star) 	 Image stacks (not recommended, read help!) (*.{spi,mrcs})" required        "A STAR file with all images (and their metadata)."
fn_map               "Consensus map:"                    file       ?               "DensityMap.mrc" 1               "Image Files (*.{spi,vol,mrc})" required        
; A 3D map in MRC/Spider format.
Make sure this map has the same dimensions and the same pixel size as your input images.
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
_dynamight_cmd.id
_dynamight_cmd.label
_dynamight_cmd.widget
_dynamight_cmd.default
_dynamight_cmd.arg0
_dynamight_cmd.arg1
_dynamight_cmd.arg2
_dynamight_cmd.constraint
_dynamight_cmd.help
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
nr_gaussians         "Number of Gaussians: "             range      10000           5000            40000           1000            ?               
; Number of Gaussians to describe the consensus map with.
Larger structures that one wishes to describe at higher resolutions will need more Gaussians.
As a rule of thumb, you could try and use 1-2 Gaussians per amino acid or nucleotide in your complex.
But note that running DynaMight with more than 30,000 Gaussians may be problematic on GPUs with a memory of 24 GB.
;
initial_threshold    "Initial map threshold (optional): " string     ?               "?"             "?"             "?"             ?               
; If provided, this threshold will be used to position initial Gaussians in the consensus map.
If left empty, an automatedrh.PROCedure will be used to estimate the appropriate threshold.
;
reg_factor           "Regularization factor: "           range      1               0.2             5               0.1             ?               
; This regularization factor defines the relative weights between the data over the restraints.
Values higher than one will put more weights on the restraints.
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
fn_dynamight_exe     "DynaMight executable:"             string     relion_python_dynamight "?"             "?"             "?"             ?               
; The DynaMight executable.
By default, the relion_python_dynamight will be used, which was installed inside conda with a typical relion install.
Only change this if that version is giving you problems.
;
gpu_id               "Which (single) GPU to use:"        string     0               "?"             "?"             "?"             ?               
; Note that DynaMight can only use one GPU at a time.
Data sets with many particles or large box sizes will require powerful GPUs, like an A100.
;
do_preload           "Preload images in RAM?"            bool       false           "?"             "?"             "?"             ?               
; If set to Yes, dynamight will preload images into memory for learning the forward or inverse deformations and for deformed backprojection.
This will speed up the calculations, but you need to make sure you have enough RAM to do so.
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
