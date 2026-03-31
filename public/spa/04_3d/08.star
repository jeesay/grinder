data_
#
loop_
_cryodrgn_abinit.id
_cryodrgn_abinit.label
_cryodrgn_abinit.icon
_cryodrgn_abinit.widget
_cryodrgn_abinit.value
_cryodrgn_abinit.help
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
cryodrgn_abinit_cmd  "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
fn_part             "Input particles file :"           file       ?               ?    1               "File (.mrcs, .star, .cs, or .txt)"    required        "particles.star file comming from an Extract or a Select job"
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
outdir              "Path to output directory : "      string       "jobXXX/"                ?    1               ?                             required        "Output directory to save model"
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
_cryodrgn_abinit_cmd.id
_cryodrgn_abinit_cmd.label
_cryodrgn_abinit_cmd.widget
_cryodrgn_abinit_cmd.default
_cryodrgn_abinit_cmd.arg0
_cryodrgn_abinit_cmd.arg1
_cryodrgn_abinit_cmd.arg2
_cryodrgn_abinit_cmd.constraint
_cryodrgn_abinit_cmd.help
cmd   "Generated command"   cli   ?   "cryodrgn abinit"   0   ?   auto   "Command generated from parameters."
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
params_het           "Heterogeneity (Z Space)"                bi-chat-right-text   fieldset   ?          show       ?
params_model         "Model (Hypervolume)"                    bi-chat-right-text   fieldset   ?          show       ?
params_pose          "Pose Search"                            bi-chat-right-text   fieldset   ?          show       ?
params_log           "Logging"                                bi-chat-right-text   fieldset   ?          show       ?
use_gpu              "Use GPU acceleration?"                  bi-chat-right-text   switch     ?          show       ?
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
datadir    "Path to .mrcs files"   string    "jobXXX/Movies"      --datadir    1        ?   optional   "Directory containing .mrcs files when using relative paths."
seed       "Random seed"           range   0      0            100000   1   optional   "Fix random seed for reproducibility."
verbose    "Verbose mode"          bool    false  -v           0        ?   optional   "Increase verbosity."
lazy       "Lazy loading"          bool    false  --lazy       0        ?   optional   "Enable lazy data loading."
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
num_epochs      "Number of epochs"      range   30       1              1000    1           optional   "Total number of training epochs."
batch_size_sgd  "Batch size (SGD)"      range   128      1              1024    1           optional   "Batch size for SGD training."
lr              "Learning rate"         range   0.0001   0.000001       1.0     0.000001    optional   "Learning rate for optimizer."
wd              "Weight decay"          range   0.0      0.0            1.0     0.0001      optional   "Weight decay regularization."
no_shuffle      "Disable shuffle"       bool    false    --no-shuffle   0       ?           optional   "Disable dataset shuffling."
#
loop_
_params_het.id
_params_het.label
_params_het.widget
_params_het.default
_params_het.arg0
_params_het.arg1
_params_het.arg2
_params_het.constraint
_params_het.help
zdim            "Latent dimension (zdim)"   range   8       1                    128    1       required   "Dimension of latent conformational space."
variational     "Variational mode"          bool    false   --variational-het    0      ?       optional   "Enable variational heterogeneity modeling."
std_z_init      "Initial z std"             range   0.1     0.0                  2.0    0.01    optional   "Initial standard deviation of latent vectors."
use_encoder     "Use encoder"               bool    false   --use-conf-encoder   0      ?       optional   "Use CNN encoder to predict conformations."
#
loop_
_params_model.id
_params_model.label
_params_model.widget
_params_model.default
_params_model.arg0
_params_model.arg1
_params_model.arg2
_params_model.constraint
_params_model.help
layers     "Number of layers"     range   3     1       10      1       optional   "Number of hidden layers."
dim        "Hidden dimension"     range   256   16      1024    16      optional   "Size of hidden layers."
pe_dim     "Positional encoding"  range   64    1       256     1       optional   "Number of Fourier features."
#
loop_
_params_pose.id
_params_pose.label
_params_pose.widget
_params_pose.default
_params_pose.arg0
_params_pose.arg1
_params_pose.arg2
_params_pose.constraint
_params_pose.help
l_start     "Start frequency"    range   12   1   64   1   optional   "Initial frequency for pose search."
l_end       "End frequency"      range   32   1   128   1   optional   "Final frequency for pose search."
niter       "Iterations"         range   4    1   20   1   optional   "Number of pose search iterations."
t_extent    "Translation extent" range   20   0   100   1   optional   "Translation search range in pixels."
#
loop_
_params_log.id
_params_log.label
_params_log.widget
_params_log.default
_params_log.arg0
_params_log.arg1
_params_log.arg2
_params_log.constraint
_params_log.help
log_interval   "Logging interval"   range      10000   100   1000000   100   show   "Logging interval in number of images."
checkpoint     "Checkpoint freq"    range      5       1     100       1     show   "Checkpoint frequency (epochs)."
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
