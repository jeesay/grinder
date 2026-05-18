data_
#
loop_
_autorefine.id
_autorefine.label
_autorefine.icon
_autorefine.widget
_autorefine.value
_autorefine.help
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
autorefine_cmd       "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
fn_img               "Input images STAR file:"           file       ?               "ParticleGroupMetadata.star.relion" 1               "STAR files (*.star)" required        "A STAR file with all images (and their metadata)."
fn_ref               "Reference map:"                    file       ?               "DensityMap.mrc" 1               "Image Files (*.{spi,vol,mrc})" required        
; A 3D map in MRC/Spider format.
Make sure this map has the same dimensions and the same pixel size as your input images, or specify that one can resize the reference if needed.
;
fn_mask              "Reference mask (optional):"        file       ?               "Mask3D.mrc"    1               "Image Files (*.{spi,vol,msk,mrc})" required        
; If no mask is provided, a soft spherical mask based on the particle diameter will be used.

Otherwise, provide a Spider/mrc map containing a (soft) mask with the same dimensions as the reference(s), and values between 0 and 1, with 1 being 100% protein and 0 being 100% solvent.
The reconstructed reference map will be multiplied by this mask.

In some cases, for example for non-empty icosahedral viruses, it is also useful to use a second mask.
For all white (value 1) pixels in this second mask the corresponding pixels in the reconstructed map are set to the average value of these pixels.
Thereby, for example, the higher density inside the virion may be set to a constant.
Note that this second mask should have one-values inside the virion and zero-values in the capsid and the solvent areas.
To use a second mask, use the additional option --solvent_mask2, which may given in the Additional arguments line (in the Running tab).
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
_autorefine_cmd.id
_autorefine_cmd.label
_autorefine_cmd.widget
_autorefine_cmd.default
_autorefine_cmd.arg0
_autorefine_cmd.arg1
_autorefine_cmd.arg2
_autorefine_cmd.constraint
_autorefine_cmd.help
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
do_ctf_correction    "Do CTF-correction?"                     bi-chat-right-text   switch     ?          show       ?
params_02            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
params_03            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
params_04            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
sampling             "Options"                                bi-chat-right-text   fieldset   ?          show       ?
params_05            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
auto_local_sampling  "Options"                                bi-chat-right-text   fieldset   ?          show       ?
params_06            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
diskio               "Disk Management"                        bi-chat-right-text   fieldset   ?          show       ?
params_08            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
use_gpu              "Use GPU acceleration?"                  bi-chat-right-text   switch     ?          show       ?
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
ref_correct_greyscale "Ref. map is on absolute greyscale?" bool       false           "?"             "?"             "?"             ?               
; Probabilities are calculated based on a Gaussian noise model, which contains a squared difference term between the reference and the experimental image.
This has a consequence that the reference needs to be on the same absolute intensity grey-scale as the experimental images.
RELION and XMIPP reconstruct maps at their absolute intensity grey-scale.
Other packages may perform internal normalisations of the reference density, which will result in incorrect grey-scales.
Therefore: if the map was reconstructed in RELION or in XMIPP, set this option to Yes, otherwise set it to No.
If set to No, RELION will use a (grey-scale invariant) cross-correlation criterion in the first iteration, and prior to the second iteration the map will be filtered again using the initial low-pass filter.
Thisrh.PROCedure is relatively quick and typically does not negatively affect the outcome of the subsequent MAP refinement.
Therefore, if in doubt it is recommended to set this option to No.
;
trust_ref_size       "Resize reference if needed?"       bool       true            "?"             "?"             "?"             ?               
; If True, and if the input reference map (and mask) do not have the same pixel size and/or box size, then they will be re-scaled and re-boxed accordingly.
If this option is set to False, then the program will die with an error if the reference does not have the correct pixel and/or box size.
;
ini_high             "Initial low-pass filter (A):"      range      60              0               200             5               ?               
; It is recommended to strongly low-pass filter your initial reference map.
If it has not yet been low-pass filtered, it may be done internally using this option.
If set to 0, no low-pass filter will be applied to the initial reference(s).
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
sym_name             "Symmetry:"                         string     C1              "?"             "?"             "?"             ?               
; If the molecule is asymmetric, set Symmetry group to C1.
Note their are multiple possibilities for icosahedral symmetry: 
 * I1: No-Crowther 222 (standard in Heymann, Chagoyen & Belnap, JSB, 151 (2005) 196–207) 
 * I2: Crowther 222 
 * I3: 52-setting (as used in SPIDER?)
 * I4: A different 52 setting 
 The command 'relion_refine --sym D2 --print_symmetry_ops' prints a list of all symmetry operators for symmetry group D2.
RELION uses XMIPP's libraries for symmetry operations.
Therefore, look at the XMIPP Wiki for more details:  http:#xmipp.cnb.csic.es/twiki/bin/view/Xmipp/WebHome?topic=Symmetry
;
#
loop_
_do_ctf_correction.id
_do_ctf_correction.label
_do_ctf_correction.widget
_do_ctf_correction.default
_do_ctf_correction.arg0
_do_ctf_correction.arg1
_do_ctf_correction.arg2
_do_ctf_correction.constraint
_do_ctf_correction.help
ctf_intact_first_peak "Ignore CTFs until first peak?"     bool       false           "?"             "?"             "?"             ?               
; If set to Yes, then CTF-amplitude correction will only be performed from the first peak of each CTF onward.
This can be useful if the CTF model is inadequate at the lowest resolution.
Still, in general using higher amplitude contrast on the CTFs (e.g.
10-20%) often yields better results.
Therefore, this option is not generally recommended: try increasing amplitude contrast (in your input STAR file) first!
;
#
loop_
_params_02.id
_params_02.label
_params_02.widget
_params_02.default
_params_02.arg0
_params_02.arg1
_params_02.arg2
_params_02.constraint
_params_02.help
particle_diameter    "Mask diameter (A):"                range      200             0               1000            10              ?               
; The experimental images will be masked with a soft circular mask with this diameter.
Make sure this radius is not set too small because that may mask away part of the signal! If set to a value larger than the image size no masking will be performed.

The same diameter will also be used for a spherical mask of the reference structures if no user-provided mask is specified.
;
do_zero_mask         "Mask individual particles with zeros?" bool       true            "?"             "?"             "?"             ?               
; If set to Yes, then in the individual particles, the area outside a circle with the radius of the particle will be set to zeros prior to taking the Fourier transform.
This will remove noise and therefore increase sensitivity in the alignment and classification.
However, it will also introduce correlations between the Fourier components that are not modelled.
When set to No, then the solvent area is filled with random noise, which prevents introducing correlations.High-resolution refinements (e.g.
ribosomes or other large complexes in 3D auto-refine) tend to work better when filling the solvent area with random noise (i.e.
setting this option to No), refinements of smaller complexes and most classifications go better when using zeros (i.e.
setting this option to Yes).
;
#
loop_
_params_03.id
_params_03.label
_params_03.widget
_params_03.default
_params_03.arg0
_params_03.arg1
_params_03.arg2
_params_03.constraint
_params_03.help
do_solvent_fsc       "Use solvent-flattened FSCs?"       bool       false           "?"             "?"             "?"             ?               
; If set to Yes, then instead of using unmasked maps to calculate the gold-standard FSCs during refinement, masked half-maps are used and a post-processing-like correction of the FSC curves (with phase-randomisation) is performed every iteration.
This only works when a reference mask is provided on the I/O tab.
This may yield higher-resolution maps, especially when the mask contains only a relatively small volume inside the box.
;
#
loop_
_params_04.id
_params_04.label
_params_04.widget
_params_04.default
_params_04.arg0
_params_04.arg1
_params_04.arg2
_params_04.constraint
_params_04.help
do_blush             "Use Blush regularisation?"         bool       false           "?"             "?"             "?"             ?               
; If set to Yes, relion_refine will use a neural network to perform regularisation by denoising at every iteration, instead of the standard smoothness regularisation.
;
sampling             "Initial angular sampling:"         select     2               2               "?"             "?"             ?               
; There are only a few discrete angular samplings possible because we use the HealPix library to generate the sampling of the first two Euler angles on the sphere.
The samplings are approximate numbers and vary slightly over the sphere.

 Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.
;
offset_range         "Initial offset range (pix):"       range      5               0               30              1               ?               
; Probabilities will be calculated only for translations in a circle with this radius (in pixels).
The center of this circle changes at every iteration and is placed at the optimal translation for each image in the previous iteration.

 Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.
;
offset_step          "Initial offset step (pix):"        range      1               0.1             5               0.1             ?               
; Translations will be sampled with this step-size (in pixels).Translational sampling is also done using the adaptive approach.
Therefore, if adaptive=1, the translations will first be evaluated on a 2x coarser grid.

 Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.
;
#
loop_
_sampling.id
_sampling.label
_sampling.widget
_sampling.default
_sampling.arg0
_sampling.arg1
_sampling.arg2
_sampling.constraint
_sampling.help
sampling_opt_00      "30 degrees"                        option     0               "?"             "?"             "?"             ?               "?"
sampling_opt_01      "15 degrees"                        option     1               "?"             "?"             "?"             ?               "?"
sampling_opt_02      "7.5 degrees"                       option     2               "?"             "?"             "?"             ?               "?"
sampling_opt_03      "3.7 degrees"                       option     3               "?"             "?"             "?"             ?               "?"
sampling_opt_04      "1.8 degrees"                       option     4               "?"             "?"             "?"             ?               "?"
sampling_opt_05      "0.9 degrees"                       option     5               "?"             "?"             "?"             ?               "?"
sampling_opt_06      "0.5 degrees"                       option     6               "?"             "?"             "?"             ?               "?"
sampling_opt_07      "0.2 degrees"                       option     7               "?"             "?"             "?"             ?               "?"
sampling_opt_08      "0.1 degrees"                       option     8               "?"             "?"             "?"             ?               "?"
#
loop_
_params_05.id
_params_05.label
_params_05.widget
_params_05.default
_params_05.arg0
_params_05.arg1
_params_05.arg2
_params_05.constraint
_params_05.help
auto_local_sampling  "Local searches from auto-sampling:" select     4               4               "?"             "?"             ?               
; In the automatedrh.PROCedure to increase the angular samplings, local angular searches of -6/+6 times the sampling rate will be used from this angular sampling rate onwards.
For most lower-symmetric particles a value of 1.8 degrees will be sufficient.
Perhaps icosahedral symmetries may benefit from a smaller value such as 0.9 degrees.
;
relax_sym            "Relax symmetry:"                   string     ?               "?"             "?"             "?"             ?               
; With this option, poses related to the standard local angular search range by the given point group will also be explored.
For example, if you have a pseudo-symmetric dimer A-A', refinement or classification in C1 with symmetry relaxation by C2 might be able to improve distinction between A and A'.
Note that the reference must be more-or-less aligned to the convention of (pseudo-)symmetry operators.
For details, see Ilca et al 2019 and Abrishami et al 2020 cited in the About dialog.
;
#
loop_
_auto_local_sampling.id
_auto_local_sampling.label
_auto_local_sampling.widget
_auto_local_sampling.default
_auto_local_sampling.arg0
_auto_local_sampling.arg1
_auto_local_sampling.arg2
_auto_local_sampling.constraint
_auto_local_sampling.help
auto_local_sampling_opt_00 "30 degrees"                        option     0               "?"             "?"             "?"             ?               "?"
auto_local_sampling_opt_01 "15 degrees"                        option     1               "?"             "?"             "?"             ?               "?"
auto_local_sampling_opt_02 "7.5 degrees"                       option     2               "?"             "?"             "?"             ?               "?"
auto_local_sampling_opt_03 "3.7 degrees"                       option     3               "?"             "?"             "?"             ?               "?"
auto_local_sampling_opt_04 "1.8 degrees"                       option     4               "?"             "?"             "?"             ?               "?"
auto_local_sampling_opt_05 "0.9 degrees"                       option     5               "?"             "?"             "?"             ?               "?"
auto_local_sampling_opt_06 "0.5 degrees"                       option     6               "?"             "?"             "?"             ?               "?"
auto_local_sampling_opt_07 "0.2 degrees"                       option     7               "?"             "?"             "?"             ?               "?"
auto_local_sampling_opt_08 "0.1 degrees"                       option     8               "?"             "?"             "?"             ?               "?"
#
loop_
_params_06.id
_params_06.label
_params_06.widget
_params_06.default
_params_06.arg0
_params_06.arg1
_params_06.arg2
_params_06.constraint
_params_06.help
auto_faster          "Use finer angular sampling faster?" bool       false           "?"             "?"             "?"             ?               
; If set to Yes, then let auto-refinementrh.PROCeed faster with finer angular samplings.
Two additional command-line options will be passed to the refine program: 
 
 --auto_ignore_angles lets angular sampling go down despite changes still happening in the angles 
 
 --auto_resol_angles lets angular sampling go down if the current resolution already requires that sampling at the edge of the particle.
 

 This option will make the computation faster, but hasn't been tested for many cases for potential loss in reconstruction quality upon convergence.
;
#
loop_
_diskio.id
_diskio.label
_diskio.widget
_diskio.default
_diskio.arg0
_diskio.arg1
_diskio.arg2
_diskio.constraint
_diskio.help
do_parallel_discio   "Use parallel disc I/O?"            bool       true            "?"             "?"             "?"             ?               
; If set to Yes, all MPI followers will read their own images from disc.
Otherwise, only the leader will read images and send them through the network to the followers.
Parallel file systems like gluster of fhgfs are good at parallel disc I/O.
NFS may break with many followers reading in parallel.
If your datasets contain particles with different box sizes, you have to say Yes.
;
nr_pool              "Number of pooled particles:"       range      3               1               16              1               ?               
; Particles arerh.PROCessed in individual batches by MPI followers.
During each batch, a stack of particle images is only opened and closed once to improve disk access times.
All particle images of a single batch are read into memory together.
The size of these batches is at least one particle per thread used.
The nr_pooled_particles parameter controls how many particles are read together for each thread.
If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together.
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem.
It has a modest cost of increased RAM usage.
;
do_pad1              "Skip padding?"                     bool       false           "?"             "?"             "?"             ?               
; If set to Yes, the calculations will not use padding in Fourier space for better interpolation in the references.
Otherwise, references are padded 2x before Fourier transforms are calculated.
Skipping padding (i.e.
use --pad 1) gives nearly as good results as using --pad 2, but some artifacts may appear in the corners from signal that is folded back.
;
#
loop_
_params_08.id
_params_08.label
_params_08.widget
_params_08.default
_params_08.arg0
_params_08.arg1
_params_08.arg2
_params_08.constraint
_params_08.help
do_preread_images    "Pre-read all particles into RAM?"  bool       false           "?"             "?"             "?"             ?               
; If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access.
However, one should of course be careful with the amount of RAM available.
Because particles are read in float-precision, it will take ( N * box_size * box_size * 8 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM.
For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles.
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM.

 
 If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.
;
scratch_dir          "Copy particles to scratch directory:" string     RELION_SCRATCH_DIR "?"             "?"             "?"             ?               
; If a directory is provided here, then the job will create a sub-directory in it called relion_volatile.
If that relion_volatile directory already exists, it will be wiped.
Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory.
Provided this directory is on a fast local drive (e.g.
an SSD drive),rh.PROCessing in all the iterations will be faster.
If the job finishes correctly, the relion_volatile directory will be wiped.
If the job crashes, you may want to remove it yourself.
;
do_combine_thru_disc "Combine iterations through disc?"  bool       false           "?"             "?"             "?"             ?               
; If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results.
The MPI leader will read in all these files, combine them all, and write out a new file with the combined results.
All MPI salves will then read in the combined results.
This reduces heavy load on the network, but increases load on the disc I/O.
This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step.
It will depend on your system setup which is most efficient.
;
#
loop_
_use_gpu.id
_use_gpu.label
_use_gpu.widget
_use_gpu.default
_use_gpu.arg0
_use_gpu.arg1
_use_gpu.arg2
_use_gpu.constraint
_use_gpu.help
gpu_ids              "Which GPUs to use:"                string     ?               "?"             "?"             "?"             ?               
; This argument is not necessary.
If left empty, the job itself will try to allocate available GPU resources.
You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use.
MPI-processes are separated by ':', threads by ','.
 For example: '0,0:1,1:0,0:1,1'
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
