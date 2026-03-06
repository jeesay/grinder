data_
#
loop_
_multibody.id
_multibody.label
_multibody.icon
_multibody.widget
_multibody.value
_multibody.help
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
_io.help
indata               "Input Data"                             bi-box-arrow-in-down fieldset   ?          ?
outdata              "Output Data"                            bi-box-arrow-down    fieldset   ?          ?
nodes                "Nodes"                                  bi-controller        fieldset   ?          ?
system               "System"                                 bi-incognito         fieldset   ?          ?
multibody_cmd        "Check command"                          bi-chat-right-text   cli        ?          ?
#
loop_
_indata.id
_indata.label
_indata.widget
_indata.default
_indata.arg0
_indata.arg1
_indata.arg2
_indata.help
fn_in                "Consensus refinement optimiser.star: " file       ?               "STAR Files (run_it*_optimiser.star)" Refine3D/.      ?               
; Select the *_optimiser.star file for the iteration of the consensus refinement from which you want to start multi-body refinement.
;
fn_bodies            "Body STAR file:"                   file       ?               "STAR Files (*.{star})" .               ?               
;  Provide the STAR file with all information about the bodies to be used in multi-body refinement.
An example for a three-body refinement would look like this: 

data_
loop_
_rlnBodyMaskName
_rlnBodyRotateRelativeTo
_rlnBodySigmaAngles
_rlnBodySigmaOffset
large_body_mask.mrc 2 10 2
small_body_mask.mrc 1 10 2
head_body_mask.mrc 2 10 2

Where each data line represents a different body, and: 
  - rlnBodyMaskName contains the name of a soft-edged mask with values in [0,1] that define the body; 
 - rlnBodyRotateRelativeTo defines relative to which other body this body rotates (first body is number 1) 
 - rlnBodySigmaAngles and _rlnBodySigmaOffset are the standard deviations (widths) of Gaussian priors on the consensus rotations and translations; 

 Optionally, there can be a fifth column with _rlnBodyReferenceName.
Entries can be 'None' (without the ''s) or the name of a MRC map with an initial reference for that body.
In case the entry is None, the reference will be taken from the density in the consensus refinement.
 
Also note that larger bodies should be above smaller bodies in the STAR file.
For more information, see the multi-body paper.
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
_system.help
do_analyse           "Run flexibility analysis?"         bool       false           "?"             ?               ?               
; If set to Yes, after the multi-body refinement has completed, a PCA analysis will be run on the orientations all all bodies in the data set.
This can be set to No initially, and then the job can be continued afterwards to only perform this analysis.
;
#
loop_
_multibody_cmd.id
_multibody_cmd.label
_multibody_cmd.widget
_multibody_cmd.default
_multibody_cmd.arg0
_multibody_cmd.arg1
_multibody_cmd.arg2
_multibody_cmd.help
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.help
general              "General"                                bi-chat-right-text   fieldset   ?          ?
params_01            "Parameters"                             bi-chat-right-text   fieldset   ?          ?
sampling             "Options"                                bi-chat-right-text   fieldset   ?          ?
diskio               "Disk Management"                        bi-chat-right-text   fieldset   ?          ?
params_02            "Parameters"                             bi-chat-right-text   fieldset   ?          ?
use_gpu              "Use GPU acceleration?"                  bi-chat-right-text   switch     ?          ?
parallel_computing   "Parallel Computing"                     bi-chat-right-text   fieldset   ?          ?
#
loop_
_general.id
_general.label
_general.widget
_general.default
_general.arg0
_general.arg1
_general.arg2
_general.help
do_subtracted_bodies "Reconstruct subtracted bodies?"    bool       true            "?"             ?               ?               
; If set to Yes, then the reconstruction of each of the bodies will use the subtracted images.
This may give useful insights about how well the subtraction worked.
If set to No, the original particles are used for reconstruction (while the subtracted ones are still used for alignment).
This will result in fuzzy densities for bodies outside the one used for refinement.
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
_params_01.help
do_blush             "Use Blush regularisation?"         bool       false           "?"             ?               ?               
; If set to Yes, relion_refine will use a neural network to perform regularisation by denoising at every iteration, instead of the standard smoothness regularisation.
;
sampling             "Initial angular sampling:"         select     4               4               ?               ?               
; There are only a few discrete angular samplings possible because we use the HealPix library to generate the sampling of the first two Euler angles on the sphere.
The samplings are approximate numbers and vary slightly over the sphere.

 Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.
;
offset_range         "Initial offset range (pix):"       range      3               0               30              1               
; Probabilities will be calculated only for translations in a circle with this radius (in pixels).
The center of this circle changes at every iteration and is placed at the optimal translation for each image in the previous iteration.

 Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.
;
offset_step          "Initial offset step (pix):"        range      0.75            0.1             5               0.1             
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
_sampling.help
sampling_opt_00      "30 degrees"                        option     0               "?"             ?               ?               "?"
sampling_opt_01      "15 degrees"                        option     1               "?"             ?               ?               "?"
sampling_opt_02      "7.5 degrees"                       option     2               "?"             ?               ?               "?"
sampling_opt_03      "3.7 degrees"                       option     3               "?"             ?               ?               "?"
sampling_opt_04      "1.8 degrees"                       option     4               "?"             ?               ?               "?"
sampling_opt_05      "0.9 degrees"                       option     5               "?"             ?               ?               "?"
sampling_opt_06      "0.5 degrees"                       option     6               "?"             ?               ?               "?"
sampling_opt_07      "0.2 degrees"                       option     7               "?"             ?               ?               "?"
sampling_opt_08      "0.1 degrees"                       option     8               "?"             ?               ?               "?"
#
loop_
_diskio.id
_diskio.label
_diskio.widget
_diskio.default
_diskio.arg0
_diskio.arg1
_diskio.arg2
_diskio.help
do_parallel_discio   "Use parallel disc I/O?"            bool       true            "?"             ?               ?               
; If set to Yes, all MPI followers will read their own images from disc.
Otherwise, only the leader will read images and send them through the network to the followers.
Parallel file systems like gluster of fhgfs are good at parallel disc I/O.
NFS may break with many followers reading in parallel.
If your datasets contain particles with different box sizes, you have to say Yes.
;
nr_pool              "Number of pooled particles:"       range      3               1               16              1               
; Particles arerh.PROCessed in individual batches by MPI followers.
During each batch, a stack of particle images is only opened and closed once to improve disk access times.
All particle images of a single batch are read into memory together.
The size of these batches is at least one particle per thread used.
The nr_pooled_particles parameter controls how many particles are read together for each thread.
If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together.
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem.
It has a modest cost of increased RAM usage.
;
do_pad1              "Skip padding?"                     bool       false           "?"             ?               ?               
; If set to Yes, the calculations will not use padding in Fourier space for better interpolation in the references.
Otherwise, references are padded 2x before Fourier transforms are calculated.
Skipping padding (i.e.
use --pad 1) gives nearly as good results as using --pad 2, but some artifacts may appear in the corners from signal that is folded back.
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
_params_02.help
do_preread_images    "Pre-read all particles into RAM?"  bool       false           "?"             ?               ?               
; If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access.
However, one should of course be careful with the amount of RAM available.
Because particles are read in float-precision, it will take ( N * box_size * box_size * 8 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM.
For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles.
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM.

 
 If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.
;
scratch_dir          "Copy particles to scratch directory:" string     RELION_SCRATCH_DIR "?"             ?               ?               
; If a directory is provided here, then the job will create a sub-directory in it called relion_volatile.
If that relion_volatile directory already exists, it will be wiped.
Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory.
Provided this directory is on a fast local drive (e.g.
an SSD drive),rh.PROCessing in all the iterations will be faster.
If the job finishes correctly, the relion_volatile directory will be wiped.
If the job crashes, you may want to remove it yourself.
;
do_combine_thru_disc "Combine iterations through disc?"  bool       false           "?"             ?               ?               
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
_use_gpu.help
gpu_ids              "Which GPUs to use:"                string                     "?"             ?               ?               
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
_parallel_computing.help
nr_mpi               "Number of MPI procs:"              range      {QSUB_NRMPI_VAL} 1               {RELION_MPI_MAX} 1               
; Number of MPI nodes to use in parallel.
When set to 1, MPI will not be used.
The maximum can be set through the environment variable RELION_MPI_MAX.
;
nr_threads           "Number of threads:"                range      {QSUB_NRTHREADS_VAL} 1               {RELION_THREAD_MAX} 1               
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
_log.help
#
loop_
_dataviz.id
_dataviz.label
_dataviz.icon
_dataviz.widget
_dataviz.value
_dataviz.help
#
