data_
#
loop_
_ctf.id
_ctf.label
_ctf.icon
_ctf.widget
_ctf.value
_ctf.help
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
ctf_cmd              "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
input_star_mics      "Input micrographs STAR file:"      file       ?               "MicrographGroupMetadata.star.relion" 1               "STAR files (*.star)" required        "A STAR file with all micrographs to run CTFFIND or Gctf on"
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
_ctf_cmd.id
_ctf_cmd.label
_ctf_cmd.widget
_ctf_cmd.default
_ctf_cmd.arg0
_ctf_cmd.arg1
_ctf_cmd.arg2
_ctf_cmd.constraint
_ctf_cmd.help
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.display
_settings.help
do_phaseshift        "Estimate phase shifts"                  bi-chat-right-text   switch     ?          show       ?
general              "General"                                bi-chat-right-text   fieldset   ?          show       ?
params_01            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
parallel_computing   "Parallel Computing"                     bi-chat-right-text   fieldset   ?          show       ?
#
loop_
_do_phaseshift.id
_do_phaseshift.label
_do_phaseshift.widget
_do_phaseshift.default
_do_phaseshift.arg0
_do_phaseshift.arg1
_do_phaseshift.arg2
_do_phaseshift.constraint
_do_phaseshift.help
phase_min            "Phase shift (deg) - Min:"          string     0               "?"             "?"             "?"             ?               
; Minimum, maximum and step size (in degrees) for the search of the phase shift
;
phase_max            "Phase shift (deg) - Max:"          string     180             "?"             "?"             "?"             ?               
; Minimum, maximum and step size (in degrees) for the search of the phase shift
;
phase_step           "Phase shift (deg) - Step:"         string     10              "?"             "?"             "?"             ?               
; Minimum, maximum and step size (in degrees) for the search of the phase shift
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
dast                 "Amount of astigmatism (A):"        range      100             0               2000            100             ?               "CTFFIND's dAst parameter, GCTFs -astm parameter"
fn_ctffind_exe       "CTFFIND-4.1 executable:"           file       RELION_CTFFIND_EXECUTABLE "*"             "."             "?"             ?               
; Location of the CTFFIND (release 4.1 or later) executable.
You can control the default of this field by setting environment variable RELION_CTFFIND_EXECUTABLE, or by editing the first few lines in src/gui_jobwindow.h and recompile the code.
;
use_given_ps         "Use power spectra from MotionCorr job?" bool       true            "?"             "?"             "?"             ?               
; If set to Yes, the CTF estimation will be done using power spectra calculated during motion correction.
You must use this option if you used float16 in motion correction.
;
slow_search          "Use exhaustive search?"            bool       false           "?"             "?"             "?"             ?               
; If set to Yes, CTFFIND4 will use slower but more exhaustive search.
This option is recommended for CTFFIND version 4.1.8 and earlier, but probably not necessary for 4.1.10 and later.
It is also worth trying this option when astigmatism and/or phase shifts are difficult to fit.
;
ctf_win              "Estimate CTF on window size (pix) " range      -1              -16             4096            16              ?               
; If a positive value is given, a squared window of this size at the center of the micrograph will be used to estimate the CTF.
This may be useful to exclude parts of the micrograph that are unsuitable for CTF estimation, e.g.
the labels at the edge of phtographic film.

 
 The original micrograph will be used (i.e.
this option will be ignored) if a negative value is given.
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
box                  "FFT box size (pix):"               range      512             64              1024            8               ?               "CTFFIND's Box parameter"
resmin               "Minimum resolution (A):"           range      30              10              200             10              ?               "CTFFIND's ResMin parameter"
resmax               "Maximum resolution (A):"           range      5               1               20              1               ?               "CTFFIND's ResMax parameter"
dfmin                "Minimum defocus value (A):"        range      5000            0               25000           1000            ?               "CTFFIND's dFMin parameter"
dfmax                "Maximum defocus value (A):"        range      50000           20000           100000          1000            ?               "CTFFIND's dFMax parameter"
dfstep               "Defocus step size (A):"            range      500             200             2000            100             ?               "CTFFIND's FStep parameter"
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
