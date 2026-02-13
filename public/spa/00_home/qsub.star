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
queuename  'Queue name'                 text '' ? ? ? ?
qsub       'Queue submit command'       text '' ? ? ? ?
qsubscript 'Standard submission script' text '' ? ? ?
;Script Files (*.{csh,sh,bash,script})", ".","The template for your standard queue job submission script. Its default location may be changed by setting the environment variable RELION_QSUB_TEMPLATE. 
In the template script a number of variables will be replaced:

XXXcommandXXX = relion command + arguments; 
XXXqueueXXX = The queue name; 
XXXmpinodesXXX = The number of MPI nodes; 
XXXthreadsXXX = The number of threads; 
XXXcoresXXX = XXXmpinodesXXX * XXXthreadsXXX; 
XXXdedicatedXXX = The minimum number of dedicated cores on each node; 
XXXnodesXXX = The number of requested nodes = CEIL(XXXcoresXXX / XXXdedicatedXXX); 
If these options are not enough for your standard jobs, you may define a user-specified number of extra variables: XXXextra1XXX, XXXextra2XXX, etc. 
The number of extra variables is controlled through the environment variable RELION_QSUB_EXTRA_COUNT. 
Their help text is set by the environment variables RELION_QSUB_EXTRA1, RELION_QSUB_EXTRA2, etc 
For example, setenv RELION_QSUB_EXTRA_COUNT 1, together with setenv RELION_QSUB_EXTRA1 "Max number of hours in queue" will result in an additional (text) in the GUI. 
Any variables XXXextra1XXX in the template script will be replaced by the corresponding value.
Likewise, default values for the extra entries can be set through environment variables RELION_QSUB_EXTRA1_DEFAULT, RELION_QSUB_EXTRA2_DEFAULT, etc. 
But note that (unlike all other entries in the GUI) the extra values are not remembered from one run to the other.
;
min_dedicated 'Minimum dedicated cores per node' int 4 ? ? ? ?
#
