data_
#
loop_
_resmap_locres.id
_resmap_locres.label
_resmap_locres.icon
_resmap_locres.widget
_resmap_locres.value
_resmap_locres.help
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
resmap_locres_cmd    "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
fn_in                "One of the 2 unfiltered half-maps:" file       ?               "DensityMap.mrc.halfmap" 1               "MRC map files (*half1*.mrc)" required        
; Provide one of the two unfiltered half-reconstructions that were output upon convergence of a 3D auto-refine run.
;
fn_mask              "User-provided solvent mask:"       file       ?               "Mask3D.mrc"    1               "Image Files (*.{spi,vol,msk,mrc})" required        
; Provide a mask with values between 0 and 1 around all domains of the complex.
ResMap uses this mask for local resolution calculation.
RELION does NOT use this mask for calculation, but makes a histogram of local resolution within this mask.
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
do_resmap_locres     "Use ResMap?"                       bool       true            "?"             "?"             "?"             ?               
; If set to Yes, then ResMap will be used for local resolution estimation.
;
do_relion_locres     "Use Relion?"                       bool       false           "?"             "?"             "?"             ?               
; If set to Yes, then relion_postprocess will be used for local-rtesolution estimation.
This program basically performs a series of post-processing operations with a small soft, spherical mask that is moved over the entire map, while using phase-randomisation to estimate the convolution effects of that mask.

 
 The output relion_locres.mrc map can be used to color the surface of a map in UCSF Chimera according to its local resolution.
The output relion_locres_filtered.mrc is a composite map that is locally filtered to the estimated resolution.
This is a developmental feature in need of further testing, but initial results indicate it may be useful.

 
 Note that only this program can use MPI, the ResMap wrapper cannot use MPI.
;
#
loop_
_resmap_locres_cmd.id
_resmap_locres_cmd.label
_resmap_locres_cmd.widget
_resmap_locres_cmd.default
_resmap_locres_cmd.arg0
_resmap_locres_cmd.arg1
_resmap_locres_cmd.arg2
_resmap_locres_cmd.constraint
_resmap_locres_cmd.help
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
do_resmap_locres_fs  "ResMap Parameters"                      bi-chat-right-text   fieldset   ?          show       ?
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
angpix               "Calibrated pixel size (A)"         range      1               0.3             5               0.1             ?               
; Provide the final, calibrated pixel size in Angstroms.
This value may be different from the pixel-size used thus far, e.g.
when you have recalibrated the pixel size using the fit to a PDB model.
The X-axis of the output FSC plot will use this calibrated value.
;
#
loop_
_do_resmap_locres_fs.id
_do_resmap_locres_fs.label
_do_resmap_locres_fs.widget
_do_resmap_locres_fs.default
_do_resmap_locres_fs.arg0
_do_resmap_locres_fs.arg1
_do_resmap_locres_fs.arg2
_do_resmap_locres_fs.constraint
_do_resmap_locres_fs.help
fn_resmap            "ResMap executable:"                file       RELION_RESMAP_EXECUTABLE "ResMap*"       "."             "?"             ?               
; Location of the ResMap executable.
You can control the default of this field by setting environment variable RELION_RESMAP_EXECUTABLE, or by editing the first few lines in src/gui_jobwindow.h and recompile the code.

 
 Note that the ResMap wrapper cannot use MPI.
;
pval                 "P-value:"                          range      0.05            0.0             1.0             0.01            ?               
; This value is typically left at 0.05.
If you change it, report the modified value in your paper!
;
minres               "Highest resolution (A): "          range      0.0             0.0             10.0            0.1             ?               
; ResMaps minRes parameter.
By default (0), the program will start at just above 2x the pixel size
;
maxres               "Lowest resolution (A): "           range      0.0             0.0             10.0            0.1             ?               
; ResMaps maxRes parameter.
By default (0), the program will stop at 4x the pixel size
;
stepres              "Resolution step size (A)"          range      1.0             0.1             3               0.1             ?               "ResMaps stepSize parameter."
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
