data_
#
loop_
_class2d_vdam.id
_class2d_vdam.label
_class2d_vdam.icon
_class2d_vdam.widget
_class2d_vdam.value
_class2d_vdam.help
io                   "I/O"                     bi-arrow-down-up     tab              ?        ?
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
indata               "Input Data"                        bi-box-arrow-in-down fieldset   ?          show       ?
outdata              "Output Data"                       bi-box-arrow-down    fieldset   ?          hidden     ?
nodes                "Nodes"                             bi-controller        fieldset   ?          hidden     ?
system               "System"                            bi-incognito         fieldset   ?          hiddden    ?
class2d_vdam_cmd     "Check command"                     bi-chat-right-text   cli        ?          show       ?
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
fn_img               "Input images STAR file:"           file       ?     "ParticleGroupMetadata.star.relion"    1    "STAR files (*.star)" required        
; A STAR file with all images (and their metadata).

Alternatively, you may give a Spider/MRC stack of 2D images, but in that case NO metadata can be included and thus NO CTF correction can be performed, nor will it be possible to perform noise spectra estimation or intensity scale corrections in image groups.
Therefore, running RELION with an input stack will in general provide sub-optimal results and is therefore not recommended!! Use the Preprocessing procedure to get the input STAR file in a semi-automated manner.
Read the RELION wiki for more information.
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
do_em                "Use EM algorithm?"                 bool       false           ?             ?             ?             ?               
; If set to Yes, the slower expectation-maximization algorithm will be used.
This was the default option in releases prior to 4.0-beta.
If set to No, then one needs to use the (faster) VDAM (variable metric gradient descent with adaptive moments) algorithm below.
will be used.
;
do_grad              "Use VDAM algorithm?"               bool       true            ?             ?             ?             ?               
; If set to Yes, the faster VDAM algorithm will be used.
This algorithm was introduced with relion-4.0.
If set to No, then the slower EM algorithm needs to be used.
;
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.display
_settings.help
do_ctf_correction    " Do CTF-correction?"                    bi-chat-right-text   switch     ?          show       ?
general              "General"                                bi-chat-right-text   fieldset   ?          show       ?
do_grad_fs           "VDAM Parameters"                        bi-chat-right-text   fieldset   ?          show       ?
params_01            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
dont_skip_align      "Perform image alignment?"               bi-chat-right-text   switch     ?          show       ?
diskio               "Disk Access"                            bi-database-fill     fieldset   ?          show       ?
use_gpu              "GPU"                                    bi-gpu-card          switch     ?          show       ?
parallel_computing   "Parallel Computing"                     bi-lightning-fill    fieldset   ?          show       ?
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
ctf_intact_first_peak "Ignore CTFs until first peak?"     bool       false           ?             ?             ?             ?               
; If set to Yes, then CTF-amplitude correction will only be performed from the first peak of each CTF onward.
This can be useful if the CTF model is inadequate at the lowest resolution.
Still, in general using higher amplitude contrast on the CTFs (e.g.
10-20%) often yields better results.
Therefore, this option is not generally recommended: try increasing amplitude contrast (in your input STAR file) first!
;
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
nr_classes           "Number of classes:"                range      1               1               50              1               ?               
; The number of classes (K) for a multi-reference refinement.
These classes will be made in an unsupervised manner from a single reference by division of the data into random subsets during the first iteration.
;
tau_fudge            "Regularisation parameter T:"       range      2               0.1             10              0.1             ?               
; Bayes law strictly determines the relative weight between the contribution of the experimental data and the prior.
However, in practice one may need to adjust this weight to put slightly more weight on the experimental data to allow optimal results.
Values greater than 1 for this regularisation parameter (T in the JMB2011 paper) put more weight on the experimental data.
Values around 2-4 have been observed to be useful for 3D refinements, values of 1-2 for 2D refinements.
Too small values yield too-low resolution structures; too high values result in over-estimated resolutions, mostly notable by the apparition of high-frequency noise in the references.
;
#
loop_
_do_grad_fs.id
_do_grad_fs.label
_do_grad_fs.widget
_do_grad_fs.default
_do_grad_fs.arg0
_do_grad_fs.arg1
_do_grad_fs.arg2
_do_grad_fs.constraint
_do_grad_fs.help
nr_iter_grad         "Number of VDAM mini-batches:"      range      200             50              500             10              ?               
; Number of mini-batches to be processed using the VDAM algorithm.
Using 200 has given good results for many data sets.
Using 100 will run faster, at the expense of some quality in the results.
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
particle_diameter    "Mask diameter (A):"                range      200             0               1000            10              ?               
; The experimental images will be masked with a soft circular mask with this diameter.
Make sure this radius is not set too small because that may mask away part of the signal! If set to a value larger than the image size no masking will be performed.

The same diameter will also be used for a spherical mask of the reference structures if no user-provided mask is specified.
;
do_zero_mask         "Mask individual particles with zeros?" bool       true            ?             ?             ?             ?               
; If set to Yes, then in the individual particles, the area outside a circle with the radius of the particle will be set to zeros prior to taking the Fourier transform.
This will remove noise and therefore increase sensitivity in the alignment and classification.
However, it will also introduce correlations between the Fourier components that are not modelled.
When set to No, then the solvent area is filled with random noise, which prevents introducing correlations.High-resolution refinements (e.g.
ribosomes or other large complexes in 3D auto-refine) tend to work better when filling the solvent area with random noise (i.e.
setting this option to No), refinements of smaller complexes and most classifications go better when using zeros (i.e.
setting this option to Yes).
;
highres_limit        "Limit resolution E-step to (A): "  range      -1              -1              20              1               ?               
; If set to a positive number, then the expectation step (i.e.
the alignment) will be done only including the Fourier components up to this resolution (in Angstroms).
This is useful to prevent overfitting, as the classification runs in RELION are not to be guaranteed to be 100% overfitting-free 
(unlike the 3D auto-refine with its gold-standard FSC).
In particular for very difficult data sets, e.g. of very small or featureless particles, this has been shown to give much 
better class averages. In such cases, values in the range of 7-12 Angstroms have proven useful.
;
do_center            "Center class averages?"            bool       true            ?             ?             ?             ?               
; If set to Yes, every iteration the class average images will be centered on their center-of-mass.
This will only work for positive signals, so the particles should be white.
;
#
loop_
_dont_skip_align.id
_dont_skip_align.label
_dont_skip_align.widget
_dont_skip_align.default
_dont_skip_align.arg0
_dont_skip_align.arg1
_dont_skip_align.arg2
_dont_skip_align.constraint
_dont_skip_align.help
psi_sampling         "In-plane angular sampling:"        range      6.0             0.5             20              0.5             ?               
; The sampling rate for the in-plane rotation angle (psi) in degrees.
Using fine values will slow down the program.
Recommended value for most 2D refinements: 5 degrees.

 If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.
;
offset_range         "Offset search range (pix):"        range      5               0               30              1               ?               
; Probabilities will be calculated only for translations in a circle with this radius (in pixels).
The center of this circle changes at every iteration and is placed at the optimal translation for each image in the previous iteration.

If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.
;
offset_step          "Offset search step (pix):"         range      1               0.1             5               0.1             ?               
; Translations will be sampled with this step-size (in pixels).Translational sampling is also done using the adaptive approach.
Therefore, if adaptive=1, the translations will first be evaluated on a 2x coarser grid.

If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.
;
allow_coarser        "Allow coarser sampling?"           bool       false           ?             ?             ?             ?               
; If set to Yes, the program will use coarser angular and translational samplings if the estimated accuracies of the assignments is still low in the earlier iterations.
This may speed up the calculations.
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
do_parallel_discio   "Use parallel disc I/O?"            bool       true            ?             ?             ?             ?               
; If set to Yes, all MPI followers will read images from disc.
Otherwise, only the leader will read images and send them through the network to the followers.
Parallel file systems like gluster of fhgfs are good at parallel disc I/O.
NFS may break with many followers reading in parallel.
If your datasets contain particles with different box sizes, you have to say Yes.
;
nr_pool              "Number of pooled particles:"       range      3               1               16              1               ?               
; Particles are processed in individual batches by MPI followers.
During each batch, a stack of particle images is only opened and closed once to improve disk access times.
All particle images of a single batch are read into memory together.
The size of these batches is at least one particle per thread used.
The nr_pooled_particles parameter controls how many particles are read together for each thread.
If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together.
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem.
It has a modest cost of increased RAM usage.
;
do_preread_images    "Pre-read all particles into RAM?"  bool       false           ?             ?             ?             ?               
; If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access.
However, one should of course be careful with the amount of RAM available.
Because particles are read in float-precision, it will take ( N * box_size * box_size * 4 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM.
For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles.
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM.

If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.
;
scratch_dir          "Copy particles to scratch directory:" string     RELION_SCRATCH_DIR ?             ?             ?             ?               
; If a directory is provided here, then the job will create a sub-directory in it called relion_volatile.
If that relion_volatile directory already exists, it will be wiped.
Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory.
Provided this directory is on a fast local drive (e.g.
an SSD drive), processing in all the iterations will be faster.
If the job finishes correctly, the relion_volatile directory will be wiped.
If the job crashes, you may want to remove it yourself.
;
do_combine_thru_disc "Combine iterations through disc?"  bool       false           ?             ?             ?             ?               
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
gpu_ids              "Which GPUs to use:"                string     ?               ?             ?             ?             ?               
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
