#
_main.id           relion.xxx.yyy
_main.hidden_name  '.gui_zzz'
#
loop_
_tabs.id
_tabs.label
_tabs.icon
io       'I/O'      bi-arrow-down-up
settings 'Settings' bi-tools
display  'Display'  bi-palette
compute  'Compute'  bi-cpu
running  'Running'  bi-send
result   'Results'  bi-eye
#
loop_
_fieldsets.tab_id
_fieldsets.id
_fieldsets.icon
_fieldsets.label
_fieldsets.widget
_fieldsets.default
_fieldsets.help
io       input         bi-arrow-bar-down 'Input' fieldset ? ?
settings general       ? 'General' fieldset ? ?
settings other         ? 'Additional Parameters' fieldset ? ?
compute  disk          ? 'Disk Access' fiedset ?
compute  use_gpu       ? 'Use GPU Acceleration?' switch false 'If set to Yes, the job will try to use GPU acceleration.'
running  process       ? ? fieldset ? ?
running  do_queue      ? 'Submit to queue?' switch false 'If set to Yes, the job will be submit to a queue, otherwise the job will be executed locally. Note that only MPI jobs may be sent to a queue. The default can be set through the environment variable RELION_QUEUE_USE.''
#
# Command Options
loop_
_input.id
_input.label
_input.widget
_input.default
_input.arg0
_input.arg1
_input.arg2
_input.help
todo ? ? ? ? ? ? 'No help'
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
todo ? ? ? ? ? ? 'No help'
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
other_args 'Additional Parameters' string '' ? ? ? 'Additional Parameters'
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
;If set to Yes, all MPI followers will read images from disc. \
Otherwise, only the leader will read images and send them through the network to the followers. 
Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.
;
nr_pool 'Number of pooled particles:' range 3 1 16 1 
;Particles are processed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.
;
do_preread_images 'Pre-read all particles into RAM?' bool false ? ? ?
;If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. \
Because particles are read in float-precision, it will take ( N * box_size * box_size * 4 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. \
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM. \n \n If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.
;
scratch_dir 'Copy particles to scratch directory:' file default_scratch ? ? ?
;If a directory is provided here, then the job will create a sub-directory in it called relion_volatile. If that relion_volatile directory already exists, it will be wiped. Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory. \
Provided this directory is on a fast local drive (e.g. an SSD drive), processing in all the iterations will be faster. If the job finishes correctly, the relion_volatile directory will be wiped. If the job crashes, you may want to remove it yourself.
;
do_combine_thru_disc 'Combine iterations through disc?' bool false ? ? ? 
;If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results. The MPI leader will read in all these files, combine them all, and write out a new file with the combined results. \
All MPI salves will then read in the combined results. This reduces heavy load on the network, but increases load on the disc I/O. \
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
gpu_ids 'Which GPUs to use:' text '' ? ? ?
;This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','. For example: '0,0:1,1:0,0:1,1'
;
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
nr_mpi "Number of MPI procs:" range '{qsub_nrmpi_val}' 1 '{mpi_max}' 1 "Number of MPI nodes to use in parallel. When set to 1, MPI will not be used. The maximum can be set through the environment variable RELION_MPI_MAX."
nr_threads "Number of threads:" range '{qsub_nrthreads_val}' 1 '{getenv("RELION_THREAD_MAX")}' 1 "Number of shared-memory (POSIX) threads to use in parallel. When set to 1, no multi-threading will be used. The maximum can be set through the environment variable RELION_THREAD_MAX."
#
loop_
_queue.id
_queue.label
_queue.widget
_queue.default
_queue.arg0
_queue.arg1
_queue.arg2
_queue.help
queuename  'Queue name' text '' ? ? ? ?
qsub       'Queue submit command' text '' ? ? ? ?
qsubscript 'Standard submission script'text '' ? ? ?
;Script Files (*.{csh,sh,bash,script})", ".","The template for your standard queue job submission script. \
Its default location may be changed by setting the environment variable RELION_QSUB_TEMPLATE. \
In the template script a number of variables will be replaced: \n \
XXXcommandXXX = relion command + arguments; \n \
XXXqueueXXX = The queue name; \n \
XXXmpinodesXXX = The number of MPI nodes; \n \
XXXthreadsXXX = The number of threads; \n \
XXXcoresXXX = XXXmpinodesXXX * XXXthreadsXXX; \n \
XXXdedicatedXXX = The minimum number of dedicated cores on each node; \n \
XXXnodesXXX = The number of requested nodes = CEIL(XXXcoresXXX / XXXdedicatedXXX); \n \
If these options are not enough for your standard jobs, you may define a user-specified number of extra variables: XXXextra1XXX, XXXextra2XXX, etc. \
The number of extra variables is controlled through the environment variable RELION_QSUB_EXTRA_COUNT. \
Their help text is set by the environment variables RELION_QSUB_EXTRA1, RELION_QSUB_EXTRA2, etc \
For example, setenv RELION_QSUB_EXTRA_COUNT 1, together with setenv RELION_QSUB_EXTRA1 \"Max number of hours in queue\" will result in an additional (text) ein the GUI \
Any variables XXXextra1XXX in the template script will be replaced by the corresponding value.\
Likewise, default values for the extra entries can be set through environment variables RELION_QSUB_EXTRA1_DEFAULT, RELION_QSUB_EXTRA2_DEFAULT, etc. \
But note that (unlike all other entries in the GUI) the extra values are not remembered from one run to the other.
;
min_dedicated 'Minimum dedicated cores per node' int 4 ? ? ? ?
#
loop_
_continue.id
_continue.label
_continue.widget
_continue.default
_continue.arg0
_continue.arg1
_continue.arg2
_continue.help
todo ? ? ? ? ? ? ?
#
loop_
_cli.type
_cli.content
_cli.flag
_cli.bool
prog_mpi 'relion_run_ctffind_mpi' ? ?
prog     'relion_run_ctffind' ? ?
io       '--i {input_star_mics} --o {outputname}' ? ?
param    '--Box {box} --ResMin {resmin} --ResMax {resmax}' ? ?
param    '--dFMin {dfmin} --dFMax {dfmax} --FStep {dfstep} --dAst {dast}' ? ?
flag     '--use_noDW' use_noDW  true 
flag     '--do_phaseshift --phase_min {phase_min} --phase_max {phase_max} --phase_step {phase_step}' do_phaseshift true
param    '--ctffind_exe {fn_ctffind_exe} --ctfWin {ctf_win} --is_ctffind4' ? ?
flag     '--fast_search' slow_search false
flag     '--use_given_ps' use_given_ps true
flag     '--only_do_unfinished ' is_continue true
param    '--j {nr_threads}'
param    '{other_args}' ? ?
#

