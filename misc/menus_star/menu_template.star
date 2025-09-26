#
# Command Options
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
fn_ctffind_exe "CTFFIND-4.1 executable:" string RELION_CTFFIND_EXECUTABLE ? ? ? "Location of the CTFFIND (release 4.1 or later) executable. You can control the default of this field by setting environment variable RELION_CTFFIND_EXECUTABLE, or by editing the first few lines in src/gui_jobwindow.h and recompile the code."
use_noDW       "Use micrograph w/o dose-weighting?" bool false ? ? ? "If set to Yes, the CTF estimation will be done using the micrograph without dose-weighting as in rlnMicrographNameNoDW (_noDW.mrc from MotionCor2). If set to No, the normal rlnMicrographName will be used."
use_given_ps   "Use power spectra from MotionCorr job?" bool true ? ? ? "If set to Yes, the CTF estimation will be done using power spectra calculated during motion correction. You must use this option if you used float16 in motion correction."
#
loop_
_do_phaseshift.id
_do_phaseshift.label
_do_phaseshift.widget
_do_phaseshift.default
_do_phaseshift.arg0
_do_phaseshift.arg1
_do_phaseshift.arg2
_do_phaseshift.help
phase_min   "Phase shift (deg) - Min:"  float    0 ? ? ?  "Minimum, maximum and step size (in degrees) for the search of the phase shift"
phase_max   "Phase shift (deg) - Max:"  float  180 ? ? ?  "Minimum, maximum and step size (in degrees) for the search of the phase shift"
phase_step  "Phase shift (deg) - Step:" float   10 ? ? ?  "Minimum, maximum and step size (in degrees) for the search of the phase shift"
#
loop_
_ctff4_params.id
_ctff4_params.label
_ctff4_params.widget
_ctff4_params.default
_ctff4_params.arg0
_ctff4_params.arg1
_ctff4_params.arg2
_ctff4_params.help
slow_search    "Use exhaustive search?" bool false ? ? ? "If set to Yes, CTFFIND4 will use slower but more exhaustive search. This option is recommended for CTFFIND version 4.1.8 and earlier, but probably not necessary for 4.1.10 and later. It is also worth trying this option when astigmatism and/or phase shifts are difficult to fit."
dast           "Amount of astigmatism (A):" range 100 0 2000 100 "CTFFIND's dAst parameter"
box            "FFT box size (pix):"        range   512    64   1024    8 "CTFFIND's Box parameter"
resmin         "Minimum resolution (A):"    range    30    10    200   10 "CTFFIND's ResMin parameter"
resmax         "Maximum resolution (A):"    range     5     1     20    1 "CTFFIND's ResMax parameter"
dfmin          "Minimum defocus value (A):" range  5000     0  25000 1000 "CTFFIND's dFMin parameter"
dfmax          "Maximum defocus value (A):" range 50000 20000 100000 1000 "CTFFIND's dFMax parameter"
dfstep         "Defocus step size (A):"     range   500   200,  2000, 100 "CTFFIND's FStep parameter"
ctf_win        "Estimate CTF on window size (pix) " range -1 -16 4096 16 
;If a positive value is given, a squared window of this size at the center of the micrograph will be used to estimate the CTF. 
This may be useful to exclude parts of the micrograph that are unsuitable for CTF estimation, e.g. the labels at the edge of photographic film. 

The original micrograph will be used (i.e. this option will be ignored) if a negative value is given.
;
#
loop_
_dummy.id
_dummy.label
_dummy.widget
_dummy.default
_dummy.arg0
_dummy.arg1
_dummy.arg2
_dummy.help
w00 "Widget's Label (bool)"   bool true ? ? ? 'No help'
w01 "Widget's Label (int)"    int    10 ? ? ? 'No help'
w02 "Widget's Label (string)"   string 'No string' ? ? ? 'No help'
w03 "Widget's Label (range)"  range 10 1 64 1 'No help'
w04 "Widget's Label (file)"   file 'filename.star' ? ? ? 'No help'
#
#
#
loop_
_other.id
_other.label
_other.widget
_other.default
_other.arg0
_other.arg1
_other.arg2
_other.help
other_args 'Additional Arguments' string '' ? ? ? 'Additional arguments that need to be passed'
#
loop_
_disk.id
_disk.label
_disk.widget
_disk.default
_disk.arg0
_disk.arg1
_disk.arg2
_disk.help
do_parallel_discio 'Use parallel disc I/O?' bool true ? ? ?
; If set to Yes, all MPI followers will read images from disc. Otherwise, only the leader will read images and send them through the network to the followers. 
Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.
;
nr_pool 'Number of pooled particles:' range 3 1 16 1 
;Particles are processed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.
;
do_preread_images 'Pre-read all particles into RAM?' bool false ? ? ?
;If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. 
Because particles are read in float-precision, it will take ( N * box_size * box_size * 4 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. 
For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. 
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM. 

If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.
;
scratch_dir 'Copy particles to scratch directory:' file default_scratch ? ? ?
;If a directory is provided here, then the job will create a sub-directory in it called relion_volatile. If that relion_volatile directory already exists, it will be wiped. Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory. 
Provided this directory is on a fast local drive (e.g. an SSD drive), processing in all the iterations will be faster. If the job finishes correctly, the relion_volatile directory will be wiped. If the job crashes, you may want to remove it yourself.
;
do_combine_thru_disc 'Combine iterations through disc?' bool false ? ? ? 
;If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results. The MPI leader will read in all these files, combine them all, and write out a new file with the combined results. 
All MPI salves will then read in the combined results. This reduces heavy load on the network, but increases load on the disc I/O. 
This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step. It will depend on your system setup which is most efficient.
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
gpu_ids 'Which GPUs to use:' string '' ? ? ?
;This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','. For example: '0,0:1,1:0,0:1,1'
;
#
loop_
_do_queue.id
_do_queue.label
_do_queue.widget
_do_queue.default
_do_queue.arg0
_do_queue.arg1
_do_queue.arg2
_do_queue.help
load_queue '' import './spa/00_home/qsub.star' ? ? ? ?
#
loop_
_process.id
_process.label
_process.widget
_process.default
_process.arg0
_process.arg1
_process.arg2
_process.help
nr_mpi "Number of MPI procs:" range '{QSUB_NRMPI_VAL}' 1 '{RELION_MPI_MAX}' 1 "Number of MPI nodes to use in parallel. When set to 1, MPI will not be used. The maximum can be set through the environment variable RELION_MPI_MAX."
nr_threads "Number of threads:" range '{QSUB_NRTHREADS_VAL}' 1 "{RELION_THREAD_MAX}" 1 "Number of shared-memory (POSIX) threads to use in parallel. When set to 1, no multi-threading will be used. The maximum can be set through the environment variable RELION_THREAD_MAX."
#
loop_
_cont.id
_cont.label
_cont.widget
_cont.default
_cont.arg0     # filetype
_cont.arg1     # placeholder
_cont.arg2     # directory
_cont.help
fn_cont "Continue from here: " file  ? ? "STAR Files (*_optimiser.star)" CURRENT_ODIR 
;Select the `*_optimiser.star` file for the iteration \
from which you want to continue a previous run. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a `_ctX` to the output rootname, \
with X being the iteration from which one continues the previous run.
;
#
loop_
_exec.id
_exec.label
_exec.widget
_exec.default  # visibility
_exec.arg0     # ?
_exec.arg1     # icon
_exec.arg2     # parent
_exec.help
do_schedule 'Schedule' button true  ? bi-calendar-plus ? 'No help'
do_run      'Run!'     button true  ? bi-send          ? 'No help'
do_continue 'Continue' button false ? bi-send-plus  ? 'No help'
#
loop_
_command.type
_command.content
_command.flag
_command.bool
prog_mpi '`which relion_run_ctffind_mpi`' nr_mpi 2+
prog     '`which relion_run_ctffind`' nr_mpi 1
io       '--i {input_star_mics} --o {dirname}/job{LAST_JOBID}' ? ?
param    '--Box {box} --ResMin {resmin} --ResMax {resmax}' ? ?
param    '--dFMin {dfmin} --dFMax {dfmax} --FStep {dfstep} --dAst {dast}' ? ?
flag     '--use_noDW' use_noDW  true 
flag     '--do_phaseshift --phase_min {phase_min} --phase_max {phase_max} --phase_step {phase_step}' do_phaseshift true
param    '--ctffind_exe {fn_ctffind_exe} --ctfWin {ctf_win} --is_ctffind4' ? ?
flag     '--fast_search' slow_search false
flag     '--use_given_ps' use_given_ps true
flag     '--only_do_unfinished ' is_continue true
param    '--j {nr_threads}' ? ?
param    '{other_args}'     ? ?
param    '--pipeline_control {dirname}/job{LAST_JOBID}' ? ?
#

