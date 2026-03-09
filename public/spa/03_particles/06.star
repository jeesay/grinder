data_
#
loop_
_extract_ptcls.id
_extract_ptcls.label
_extract_ptcls.icon
_extract_ptcls.widget
_extract_ptcls.value
_extract_ptcls.help
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
extract_ptcls_cmd    "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
star_mics            "micrograph STAR file: "            file       ?               "MicrographGroupMetadata.star.relion" 1               "Input STAR file (*.{star})" required        
; Filename of the STAR file that contains all micrographs from which to extract particles.
;
coords_suffix        "Input coordinates: "               file       ?               "MicrographCoordsGroup.star.relion" 1               "Input coordinates list file (*.star)" required        
; Starfile with a 2-column list of micrograph names and corresponding coordinate filenames (in .star, .box or as 2 or 3-column free text format)
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
do_reextract         "OR re-extract refined particles? " bool       false           "?"             "?"             "?"             ?               
; If set to Yes, the input Coordinates above will be ignored.
Instead, one uses a _data.star file from a previous 2D or 3D refinement to re-extract the particles in that refinement, possibly re-centered with their refined origin offsets.
This is particularly useful when going from binned to unbinned particles.
;
#
loop_
_extract_ptcls_cmd.id
_extract_ptcls_cmd.label
_extract_ptcls_cmd.widget
_extract_ptcls_cmd.default
_extract_ptcls_cmd.arg0
_extract_ptcls_cmd.arg1
_extract_ptcls_cmd.arg2
_extract_ptcls_cmd.constraint
_extract_ptcls_cmd.help
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
do_norm              "Normalize particles?"                   bi-chat-right-text   switch     ?          show       ?
do_rescale           "Rescale particles?"                     bi-chat-right-text   switch     ?          show       ?
do_fom_threshold     "Use autopick FOM threshold?"            bi-chat-right-text   switch     ?          show       ?
parallel_computing   "Parallel Computing"                     bi-chat-right-text   fieldset   ?          show       ?
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
do_float16           "Write output in float16?"          bool       true            "?"             "?"             "?"             ?               
; If set to Yes, this program will write output images in float16 MRC format.
This will save a factor of two in disk space compared to the default of writing in float32.
Note that RELION and CCPEM will read float16 images, but other programs may not (yet) do so.
;
extract_size         "Particle box size (pix):"          range      128             64              512             8               ?               
; Size of the extracted particles (in pixels).
This should be an even number!
;
do_invert            "Invert contrast?"                  bool       true            "?"             "?"             "?"             ?               
; If set to Yes, the contrast in the particles will be inverted.
;
#
loop_
_do_norm.id
_do_norm.label
_do_norm.widget
_do_norm.default
_do_norm.arg0
_do_norm.arg1
_do_norm.arg2
_do_norm.constraint
_do_norm.help
bg_diameter          "Diameter background circle (pix): " range      -1              -1              600             10              ?               
; Particles will be normalized to a mean value of zero and a standard-deviation of one for all pixels in the background area.The background area is defined as all pixels outside a circle with this given diameter in pixels (before rescaling).
When specifying a negative value, a default value of 75% of the Particle box size will be used.
;
white_dust           "Stddev for white dust removal: "   range      -1              -1              10              0.1             ?               
; Remove very white pixels from the extracted particles.
Pixels values higher than this many times the image stddev will be replaced with values from a Gaussian distribution.

 
 Use negative value to switch off dust removal.
;
black_dust           "Stddev for black dust removal: "   range      -1              -1              10              0.1             ?               
; Remove very black pixels from the extracted particles.
Pixels values higher than this many times the image stddev will be replaced with values from a Gaussian distribution.

 
 Use negative value to switch off dust removal.
;
#
loop_
_do_rescale.id
_do_rescale.label
_do_rescale.widget
_do_rescale.default
_do_rescale.arg0
_do_rescale.arg1
_do_rescale.arg2
_do_rescale.constraint
_do_rescale.help
rescale              "Re-scaled size (pixels): "         range      128             64              512             8               ?               "The re-scaled value needs to be an even number"
#
loop_
_do_fom_threshold.id
_do_fom_threshold.label
_do_fom_threshold.widget
_do_fom_threshold.default
_do_fom_threshold.arg0
_do_fom_threshold.arg1
_do_fom_threshold.arg2
_do_fom_threshold.constraint
_do_fom_threshold.help
minimum_pick_fom     "Minimum autopick FOM: "            range      0               -5              10              0.1             ?               
; The minimum value for the rlnAutopickFigureOfMerit for particles to be extracted.
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
