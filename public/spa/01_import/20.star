data_
#
loop_
_pyem_import_ptcls.id
_pyem_import_ptcls.label
_pyem_import_ptcls.icon
_pyem_import_ptcls.widget
_pyem_import_ptcls.value
_pyem_import_ptcls.help
io                   "I/O"                   bi-arrow-down-up     tab        ?        ?
settings             "Settings"              bi-tools             tab        ?        ?
log                  "Log"                   bi-binoculars-fill   tab        ?        ?
#
loop_
_io.id
_io.label
_io.icon
_io.widget
_io.value
_io.display
_io.help
general              "Required"                 bi-chat-right-text      fieldset   ?        show     ?
advanced             "Advanced parameters"      bi-chat-right-text      fieldset   ?        show     ?
nodes                "Nodes"                    bi-controller           fieldset   ?        show     ?
import_cs_cmd        "Check command"            bi-chat-right-text      cli        ?        show     ?
#
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.display
_settings.help
path             "Paths options"           bi-chat-right-text      fieldset   ?        show     ?
advanced         "Advanced parameters"     bi-chat-right-text      fieldset   ?        show     ?
#
loop_
_nodes.id
_nodes.nodetype
_nodes.widget
_nodes.filename
_nodes.filetype
JOB_OUTDIR  outdir node  Import/${NEW_JOB}     Directory.output.relion                           
outfile     output node 'files.star'           ParamsData.star.grinder.test
#
loop_
_general.id
_general.label
_general.widget
_general.default
_general.arg0
_general.arg1
_general.arg2
_general.state
_general.help 
fn_ptcls        "Input particles file:"                  string       Px/Jy/last_iter_particles.cs   ? ?            ?             ?        ?
fn_passthrouh   "Input passthrouh particles file:"       string       Px/Jy/passthrouh_particles.cs  ? ?            ?             ?        ?
fn_out          "Output particles file:"                 string       Px_Jy_particles.star           ? ?            ?             ?        ?
#
loop_
_path.id
_path.label
_path.widget
_path.default
_path.arg0
_path.arg1
_path.arg2
_path.state
_path.help 
stack-path   "Path to single particle stack"        string          ?           ?   ?   ?   ?   "Path to single particle stack"
mic-path     "Path for micrographs or movies"       string          ?           ?   ?   ?   ?   "Replacement path for micrographs or movies"
#
loop_
_advanced.id
_advanced.label
_advanced.widget
_advanced.default
_advanced.arg0
_advanced.arg1
_advanced.arg2
_advanced.state
_advanced.help 
movies       "Write per-movie star files ?"         bool            false       ?   ?   ?   ?   "Write per-movie star files into output directory"   
boxsize      "Box size :"                           string          ?           ?   ?   ?   ?   "Cryosparc refinement box size (if different from particles)"
class        "Select class to keep :"               string          ?           ?   ?   ?   ?   "Keep this class in output, may be passed multiple times"
minhpic      "Minimum posterior probability"        string          ?           ?   ?   ?   ?   "Minimum posterior probability for class assignment"
mic-coor     "Copy micrograph coordinates"          string          ?           ?   ?   ?   ?   "Source for micrograph paths and particle coordinates (file or quoted glob)"
swapxy       "Do swap X and Y ?"                    bool            false       ?   ?   ?   ?   "Swap X and Y axes when converting particle coordinates from normalized to absolute"
invertx      "Invert on X ?"                        bool            false       ?   ?   ?   ?   "Invert particle coordinate X axis"
inverty      "Invert on Y ?"                        bool            false       ?   ?   ?   ?   "Invert particle coordinate Y axis"
flipy        "Invert particle Y"                    bool            false       ?   ?   ?   ?   "Invert particle Y shifts, angles, defocus angle"
flipy-pose   "Invert particle Y only on poses"      bool            false       ?   ?   ?   ?   "Invert particle Y shifts and angles"
flipy-ctf    "Invert particle Y only on ctf"        bool            false       ?   ?   ?   ?   "Invert particle defocus angle"
cached       "Use CryoSPARC cache ?"                bool            false       ?   ?   ?   ?   "Keep paths from the Cryosparc 2+ cache when merging coordinates"
transform    "Rotation to apply (numpy format) :"   string          ?           ?   ?   ?   ?   "Apply rotation matrix or 3x4 rotation plus translation matrix to particles (Numpy format)"
relion2      "Relion2 compatible outputs"           bool            false       ?   ?   ?   ?   "Relion 2 compatible outputs"
strip-uid    "Strip UIDs : "                        string          ?           ?   ?   ?   ?   "Strip all leading UIDs from file names (default) or provide an integer to strip that number of UIDs (starting from the left)"           
10k          "Only read first 10,000 particles"     bool            false       ?   ?   ?   ?   "Only read first 10,000 particles for rapid testing." 
pickle       "Use pickle"                           bool            false       ?   ?   ?   ?   "Use pickle for large .cs files - PERMITS ARBITRARY CODE EXECUTION"
header       "Max header size : "                   string          ?           ?   ?   ?   ?   "Set max header size for large .cs files"
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
_import_cs_cmd.type
_import_cs_cmd.arg
_import_cs_cmd.param_id
prog    "conda run -n pyem csparc2star.py"    ?      
param   ""                    fn_ptcls
param   ""                    fn_passthrouh             
param   ""                    fn_out
param   "--micrograph-path"   mic-path
param   "--stack-path"        stack-path
#