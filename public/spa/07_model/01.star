data_
#
loop_
_angelo.id
_angelo.label
_angelo.icon
_angelo.widget
_angelo.value
_angelo.help
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
angelo_cmd           "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
fn_map               "B-factor sharpened map:"           file       ?               "DensityMap.mrc" 1               "MRC map files (*.mrc)" required        
; Provide a (RELION-postprocessed) B-factor sharpened map for model building
;
p_seq                "FASTA sequence for proteins:"      file       ?               "Sequence.fasta" 1               "FASTA sequence files (*.{fasta,txt})" ?               
; Provide a FASTA file with sequences for all protein chains to be built in the map.
You can leave this empty if you don't know the proteins that are there, and then run a HMMer search to identify the unknown proteins.
ModelAngelo will build much better models when provided with a FASTA sequence file!
;
d_seq                "FASTA sequence for DNA:"           file       ?               "Sequence.fasta" 1               "FASTA sequence files (*.{fasta,txt})" ?               
; Provide a FASTA file with sequences for all DNA chains to be built in the map.
;
r_seq                "FASTA sequence for RNA:"           file       ?               "Sequence.fasta" 1               "FASTA sequence files (*.{fasta,txt})" ?               
; Provide a FASTA file with sequences for all RNA chains to be built in the map.
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
_angelo_cmd.id
_angelo_cmd.label
_angelo_cmd.widget
_angelo_cmd.default
_angelo_cmd.arg0
_angelo_cmd.arg1
_angelo_cmd.arg2
_angelo_cmd.constraint
_angelo_cmd.help
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
do_hhmer             "Perform HMMer search?"                  bi-chat-right-text   switch     ?          show       ?
alphabet             "Options"                                bi-chat-right-text   fieldset   ?          show       ?
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
fn_modelangelo_exe   "ModelAngelo executable:"           string     relion_python_modelangelo "?"             "?"             "?"             ?               
; The modelangelo executable.
By default, the relion_python_modelangelo will be used, which was installed inside conda with a typical relion install.
Only change this if that version is giving you problems.
;
gpu_id               "Which GPUs to use:"                string     0               "?"             "?"             "?"             ?               
; Provide a number for the GPU to be used (e.g.
0, 1 etc).
Use comma-separated values to use multiple GPUs, e.g.
0,1,2
;
#
loop_
_do_hhmer.id
_do_hhmer.label
_do_hhmer.widget
_do_hhmer.default
_do_hhmer.arg0
_do_hhmer.arg1
_do_hhmer.arg2
_do_hhmer.constraint
_do_hhmer.help
fn_lib               "Library with sequences for HMMer search:" file       ?               "Sequence.fasta" 1               "FASTA sequence files (*.{fasta,txt})" ?               
; FASTA file with library with all sequences for HMMer search.
This is often an entire proteome.
;
alphabet             "Alphabet for the HMMer search:"    select     0               0               "?"             "?"             ?               "Type of Alphabet for HMM searches."
F1                   "HMMSearch F1: "                    range      0.02            1.0             10.0            0.1             ?               
; F1 parameter for HMMSearch, see their documentation at http:#eddylab.org/software/hmmer/Userguide.pdf
;
F2                   "HMMSearch F2: "                    range      0.001           1.0             10.0            0.1             ?               
; F2 parameter for HMMSearch, see their documentation at http:#eddylab.org/software/hmmer/Userguide.pdf
;
F3                   "HMMSearch F3: "                    range      1e-05           0.0             10.0            0.1             ?               
; F3 parameter for HMMSearch, see their documentation at http:#eddylab.org/software/hmmer/Userguide.pdf
;
E                    "HMMSearch E: "                     range      10              0.0             100.0           10              ?               
; E parameter for HMMSearch, see their documentation at http:#eddylab.org/software/hmmer/Userguide.pdf
;
#
loop_
_alphabet.id
_alphabet.label
_alphabet.widget
_alphabet.default
_alphabet.arg0
_alphabet.arg1
_alphabet.arg2
_alphabet.constraint
_alphabet.help
alphabet_opt_00      "amino"                             option     0               "?"             "?"             "?"             ?               "?"
alphabet_opt_01      "DNA"                               option     1               "?"             "?"             "?"             ?               "?"
alphabet_opt_02      "RNA"                               option     2               "?"             "?"             "?"             ?               "?"
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
