data_
#
loop_
_rln_mc.id
_rln_mc.label
_rln_mc.icon
_rln_mc.widget
_rln_mc.value
_rln_mc.help
io                   "I/O"                     bi-arrow-down-up    tab              ?        ?
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
rln_mc_cmd           "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
input_star_mics      "Input movies STAR file:"           file       ?               "MicrographMovieGroupMetadata.star.relion" 1               "STAR files (*.star)" required        "A STAR file with all micrographs to run MOTIONCORR on"
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
do_own_motioncor     "Use RELION's own implementation?"  bool       true            "?"             "?"             "?"             ?               
; If set to Yes, use RELION's own implementation of a MotionCor2-like algorithm by Takanori Nakane.
Otherwise, wrap to the UCSF implementation.
Note that Takanori's program only runs on CPUs but uses multiple threads, while the UCSF-implementation needs a GPU but uses only one CPU thread.
Takanori's implementation is most efficient when the number of frames is divisible by the number of threads (e.g.
12 or 18 threads per MPIrh.PROCess for 36 frames).
On some machines, setting the OMP_PROC_BIND environmental variable to TRUE accelerates the program.
When running on 4k x 4k movies and using 6 to 12 threads, the speeds should be similar.
Note that Takanori's program uses the same model as the UCSF program and gives results that are almost identical.
Whichever program you use, 'Motion Refinement' is highly recommended to get the most of your dataset.
;
#
loop_
_rln_mc_cmd.id
_rln_mc_cmd.label
_rln_mc_cmd.widget
_rln_mc_cmd.default
_rln_mc_cmd.arg0
_rln_mc_cmd.arg1
_rln_mc_cmd.arg2
_rln_mc_cmd.constraint
_rln_mc_cmd.help
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
do_dose_weighting    "Dose Weighting"                         bi-chat-right-text   switch     ?          show       ?
do_save_ps           "Save Power Spectrum"                    bi-chat-right-text   switch     ?          show       ?
params_01            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
gain_rot             "Options"                                bi-chat-right-text   fieldset   ?          show       ?
gain_flip            "Options"                                bi-chat-right-text   fieldset   ?          show       ?
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
first_frame_sum      "First frame for corrected sum:"    range      1               1               32              1               ?               
; First frame to use in corrected average (starts counting at 1).

;
last_frame_sum       "Last frame for corrected sum:"     range      -1              0               32              1               ?               
; Last frame to use in corrected average.
Values equal to or smaller than 0 mean 'use all frames'.
;
dose_per_frame       "Dose per frame (e/A2):"            range      1               0               5               0.2             ?               "Dose per movie frame (in electrons per squared Angstrom)."
pre_exposure         "Pre-exposure (e/A2):"              range      0               0               5               0.5             ?               "Pre-exposure dose (in electrons per squared Angstrom)."
eer_grouping         "EER fractionation:"                range      32              1               100             1               ?               
; The number of hardware frames to group into one fraction.
This option is relevant only for Falcon4 movies in the EER format.
Note that all 'frames' in the GUI (e.g.
first and last frame for corrected sum, dose per frame) refer to fractions, not raw detector frames.
See https://www3.mrc-lmb.cam.ac.uk/relion/index.php/Image_compression#Falcon4_EER for detailed guidance on EERrh.PROCessing.
;
do_float16           "Write output in float16?"          bool       true            "?"             "?"             "?"             ?               
; If set to Yes, RelionCor2 will write output images in float16 MRC format.
This will save a factor of two in disk space compared to the default of writing in float32.
Note that RELION and CCPEM will read float16 images, but other programs may not (yet) do so.
For example, Gctf will not work with float16 images.
Also note that this option does not work with UCSF MotionCor2.
For CTF estimation, use CTFFIND-4.1 with pre-calculated power spectra (activate the 'Save sum of power spectra' option).
;
#
loop_
_do_dose_weighting.id
_do_dose_weighting.label
_do_dose_weighting.widget
_do_dose_weighting.default
_do_dose_weighting.arg0
_do_dose_weighting.arg1
_do_dose_weighting.arg2
_do_dose_weighting.constraint
_do_dose_weighting.help
do_save_noDW         "Save non-dose weighted as well?"   bool       false           "?"             "?"             "?"             ?               
; Aligned but non-dose weighted images are sometimes useful in CTF estimation, although there is no difference in most cases.
Whichever the choice, CTF refinement job is always done on dose-weighted particles.
;
#
loop_
_do_save_ps.id
_do_save_ps.label
_do_save_ps.widget
_do_save_ps.default
_do_save_ps.arg0
_do_save_ps.arg1
_do_save_ps.arg2
_do_save_ps.constraint
_do_save_ps.help
group_for_ps         "Sum power spectra every e/A2:"     range      4               0               10              0.5             ?               
; McMullan et al (Ultramicroscopy, 2015) suggest summing power spectra every 4.0 e/A2 gives optimal Thon rings
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
bfactor              "Bfactor:"                          range      150             0               1500            50              ?               "The B-factor that will be applied to the micrographs."
patch_x              "Number of patches X:"              string     1               "?"             "?"             "?"             ?               
; Number of patches (in X and Y direction) to apply motioncor2.
;
patch_y              "Number of patches Y:"              string     1               "?"             "?"             "?"             ?               
; Number of patches (in X and Y direction) to apply motioncor2.
;
group_frames         "Group frames:"                     range      1               1               5               1               ?               
; Average together this many frames before calculating the beam-induced shifts.
;
bin_factor           "Binning factor:"                   range      1               1               2               1               ?               
; Bin the micrographs this much by a windowing operation in the Fourier Tranform.
Binning at this level is hard to un-do later on, but may be useful to down-scale super-resolution images.
Float-values may be used.
Do make sure though that the resulting micrograph size is even.
;
fn_gain_ref          "Gain-reference image:"             file       ?               "*.{mrc,gain}"  "."             "?"             ?               
; Location of the gain-reference file to be applied to the input micrographs.
Leave this empty if the movies are already gain-corrected.
;
gain_rot             "Gain rotation:"                    select     0               0               "?"             "?"             ?               
; Rotate the gain reference by this number times 90 degrees clockwise in relion_display.
This is the same as -RotGain in MotionCor2.
Note that MotionCor2 uses a different convention for rotation so it says 'counter-clockwise'.
Valid values are 0, 1, 2 and 3.
;
gain_flip            "Gain flip:"                        select     0               0               "?"             "?"             ?               
; Flip the gain reference after rotation.
This is the same as -FlipGain in MotionCor2.
0 means do nothing, 1 means flip Y (upside down) and 2 means flip X (left to right).
;
#
loop_
_gain_rot.id
_gain_rot.label
_gain_rot.widget
_gain_rot.default
_gain_rot.arg0
_gain_rot.arg1
_gain_rot.arg2
_gain_rot.constraint
_gain_rot.help
gain_rot_opt_00      "No rotation"                       option     0               "?"             "?"             "?"             ?               "?"
gain_rot_opt_01      "90 degrees"                        option     1               "?"             "?"             "?"             ?               "?"
gain_rot_opt_02      "180 degrees"                       option     2               "?"             "?"             "?"             ?               "?"
gain_rot_opt_03      "270 degrees"                       option     3               "?"             "?"             "?"             ?               "?"
#
loop_
_gain_flip.id
_gain_flip.label
_gain_flip.widget
_gain_flip.default
_gain_flip.arg0
_gain_flip.arg1
_gain_flip.arg2
_gain_flip.constraint
_gain_flip.help
gain_flip_opt_00     "No flipping"                       option     0               "?"             "?"             "?"             ?               "?"
gain_flip_opt_01     "Flip upside down"                  option     1               "?"             "?"             "?"             ?               "?"
gain_flip_opt_02     "Flip left to right"                option     2               "?"             "?"             "?"             ?               "?"
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
