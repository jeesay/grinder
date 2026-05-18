data_
#
loop_
_inimodel.id
_inimodel.label
_inimodel.icon
_inimodel.widget
_inimodel.state
_inimodel.help
cont                 "Continue"            bi-repeat            tab      hidden   ?
io                   "I/O"                 bi-arrow-down-up     tab      ?        ?
settings             "Settings"            bi-tools             tab      ?        ?
log                  "Log"                 bi-binoculars-fill   tab      ?        ?
dataviz              "DataViz"             bi-eye               tab      ?        ?
#
loop_
_io.id
_io.label
_io.icon
_io.widget
_io.value
_io.display
_io.help
indata               "Input Data"          bi-box-arrow-in-down fieldset   ?          show       ?
outdata              "Output Data"         bi-box-arrow-down    fieldset   ?          hidden     ?
nodes                "Nodes"               bi-controller        fieldset   ?          hidden     ?
system               "System"              bi-incognito         fieldset   ?          hiddden    ?
gdr_abinitio_prgm    "Check Command"       bi-chat-right-text   cli        ?          show       ?
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
fn_img               "Input images STAR file:"           file       ?               "ParticleGroupMetadata.star.relion" 1               "STAR files (*.star)" required        
; A STAR file with all images (and their metadata).
In Gradient optimisation, it is very important that there are particles from enough different orientations.
One only needs a few thousand to 10k particles.
When selecting good 2D classes in the Subset Selection jobtype, use the option to select a maximum number of particles from each class to generate more even angular distributions for SGD.
 
 Alternatively, you may give a Spider/MRC stack of 2D images, but in that case NO metadata can be included and thus NO CTF correction can be performed, nor will it be possible to perform noise spectra estimation or intensity scale corrections in image groups.
Therefore, running RELION with an input stack will in general provide sub-optimal results and is therefore not recommended!! Use the Preprocessingrh.PROCedure to get the input STAR file in a semi-automated manner.
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
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.display
_settings.help
do_ctf_correction    "Do CTF-correction?"          bi-chat-right-text   switch     ?          show       ?
general              "General"                     bi-chat-right-text   fieldset   ?          show       ?
params_01            "Parameters"                  bi-chat-right-text   fieldset   ?          show       ?
diskio               "Disk Management"             bi-chat-right-text   fieldset   ?          show       ?
params_03            "Parameters"                  bi-chat-right-text   fieldset   ?          show       ?
use_gpu              "Use GPU acceleration?"       bi-chat-right-text   switch     ?          show       ?
parallel_computing   "Parallel Computing"          bi-chat-right-text   fieldset   ?          show       ?
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
nr_iter              "Number of VDAM mini-batches:"      range      200             50              500             10              ?               
; How many iterations (i.e.
mini-batches) to perform with the VDAM algorithm?
;
tau_fudge            "Regularisation parameter T:"       range      4               0.1             10              0.1             ?               
; Bayes law strictly determines the relative weight between the contribution of the experimental data and the prior.
However, in practice one may need to adjust this weight to put slightly more weight on the experimental data to allow optimal results.
Values greater than 1 for this regularisation parameter (T in the JMB2011 paper) put more weight on the experimental data.
Values around 2-4 have been observed to be useful for 3D initial model calculations
;
nr_classes           "Number of classes:"                range      1               1               50              1               ?               
; The number of classes (K) for a multi-reference ab initio SGD refinement.
These classes will be made in an unsupervised manner, starting from a single reference in the initial iterations of the SGD, and the references will become increasingly dissimilar during the inbetween iterations.
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
do_solvent           "Flatten and enforce non-negative solvent?" bool       true            ?             ?             ?             ?               
; If set to Yes, the job will apply a spherical mask and enforce all values in the reference to be non-negative.
;
sym_name             "Symmetry:"                         string     C1              ?             ?             ?             ?               
; The initial model is always generated in C1 and then aligned to and symmetrized with the specified point group.
If the automatic alignment fails, please manually rotate run_itNNN_class001.mrc (NNN is the number of iterations) so that it conforms the symmetry convention.
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
an SSD drive),rh.PROCessing in all the iterations will be faster.
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
gpu_ids              "Which GPUs to use:"    string     ?       ?       ?      ?             ?               
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
nr_mpi      "Number of MPI procs:"    range      {QSUB_NRMPI_VAL} 1     "{RELION_MPI_MAX}" 1       ?               
; Number of MPI nodes to use in parallel.
When set to 1, MPI will not be used.
The maximum can be set through the environment variable RELION_MPI_MAX.
;
nr_threads  "Number of threads:"      range      {QSUB_NRTHREADS_VAL} 1  "{RELION_THREAD_MAX}" 1   ?               
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
loop_
_gdr_abinitio_prgm.type
_gdr_abinitio_prgm.arg
_gdr_abinitio_prgm.param_id
prog    "grinder abinitio"                   ?
param   --continue                           fn_cont
param   --o                                  "InitialModel/${RELION_NEW_JOB}/initial_model.mrc"
param   -iter                                nr_iter
param   "--grad --denovo_3dref"              ""
param   --sigma_tilt                         sigma_tilt
param   --i                                  fn_img
flag    --ctf                                do_ctf_correction
param   --K                                  nr_classes
flag    "--sym C1"                           do_run_C1==True
flag    "--sym  ${fn_sym}"                   do_run_C1==False
flag    --flatten_solvent                    do_solvent==True
param   --zero_mask                          zero_mask
flag    --dont_combine_weights_via_disc      do_combine_thru_disc==False
flag    --no_parallel_disc_io                do_parallel_discio==False
flag    --preread_images                     do_preread_images==True
flag    --scratch_dir                        "${RELION_SCRATCH_DIR}"
param   --pool                               nr_pool
param   --pad                                1
param   --particle_diameter                  particle_diameter
param   --oversampling                       1                         
param   --healpix_order                      1  
param   --offset_range                       6  
param   --offset_step                        2 
param   --auto_sampling                      ""
param   --tau2_fudge                         tau_fudge
param   --j                                  nr_threads
param   "--gpu ${gpu_ids}"                   use_gpu==True
param   "${other_args}"                      ""
param   --pipeline-control                   "InitialModel/${RELION_NEW_JOB}/"
#