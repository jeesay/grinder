data_ctffind4
#
_fieldset.id ctffind
_fieldset.label 'CTF Estimation'
_fieldset.icon bi-bullseye
#
_main.id           relion.ctffind.ctffind4
_main.hidden_name '.gui_ctffind'
_main.use_ctffind4 true
#
_main.parent_id    01_ctffind 
_main.label        'CTF with CTFFIND 4.1' 
_main.help         'If set to Yes, the wrapper will use CTFFIND4 (version 4.1) for CTF estimation. This includes thread-support, calculation of Thon rings from movie frames and phase-shift estimation for phase-plate data.'
#
loop_
_tabs.id
_tabs.label
_tabs.icon
io 'I/O' bi-arrow-down-up 
settings 'Settings' bi-tools
running 'Running' bi-send
#
loop_
_fieldsets.tab_id
_fieldsets.id
_fieldsets.icon
_fieldsets.label
_fieldsets.widget
_fieldsets.default
_fieldsets.help
io       input         ? ? fieldset ? ?
settings general       ? 'General' fieldset ? ?
settings do_phaseshift ? 'Estimate phase shifts?' switch false  'If set to Yes, CTFFIND4 will estimate the phase shift, e.g. as introduced by a Volta phase-plate'
settings params        ? 'CTFFIND 4.1 Parameters' fieldset ? ?
running  process       ? ? fieldset ? ?
running  queue         ? ? switch false ?

#
# CTFFIND options
loop_
_params.parent_id
_params.id
_params.label
_params.widget
_params.params
_params.help
input   input_star_mics 'Input micrographs STAR file:' file 'NODE_MICS_CPIPE, "STAR files (*.star)"' 'A STAR file with all micrographs to run CTFFIND on'
general use_noDW 'Use micrograph without dose-weighting?' bool false 
;If set to Yes, the CTF estimation will be done using 
the micrograph without dose-weighting as in rlnMicrographNameNoDW 
(_noDW.mrc from MotionCor2). If set to No, the normal rlnMicrographName will be used.
;
general dast        'Amount of astigmatism (A):' range '100, 0,  2000,  100' 'CTFFIND\'s dAst parameter, GCTFs -astm parameter'
do_phaseshift phase_min   'Phase shift (deg) - Min:' string '0'  'Minimum, maximum and step size (in degrees) for the search of the phase shift'
do_phaseshift phase_max   'Phase shift (deg) - Max:' string '180' 'Minimum, maximum and step size (in degrees) for the search of the phase shift'
do_phaseshift phase_step  'Phase shift (deg) - Step:' string '10' 'Minimum, maximum and step size (in degrees) for the search of the phase shift'
params fn_ctffind_exe  'CTFFIND-4.1 executable:' string 'default_location '*', '.''  'Location of the CTFFIND (release 4.1 or later) executable. You can control the default of this field by setting environment variable RELION_CTFFIND_EXECUTABLE, or by editing the first few lines in src/gui_jobwindow.h and recompile the code.'
params use_given_ps  'Use power spectra from MotionCorr job?' bool true  'If set to Yes, the CTF estimation will be done using power spectra calculated during motion correction. You must use this option if you used float16 in motion correction.'
params slow_search    'Use exhaustive search?' bool false 'If set to Yes, CTFFIND4 will use slower but more exhaustive search. This option is recommended for CTFFIND version 4.1.8 and earlier, but probably not necessary for 4.1.10 and later. It is also worth trying this option when astigmatism and/or phase shifts are difficult to fit.'
params box     'FFT box size (pix):'                range '512, 64, 1024, 8' 'CTFFIND\'s Box parameter'
params resmin  'Minimum resolution (A):'            range '30, 10, 200, 10' 'CTFFIND\'s ResMin parameter'
params resmax  'Maximum resolution (A):'            range '5, 1, 20, 1' 'CTFFIND\'s ResMax parameter'
params dfmin   'Minimum defocus value (A):'         range '5000, 0, 25000, 1000' 'CTFFIND\'s dFMin parameter'
params dfmax   'Maximum defocus value (A):'         range '50000, 20000, 100000, 1000' 'CTFFIND\'s dFMax parameter'
params dfstep  'Defocus step size (A):'             range '500, 200, 2000, 100' 'CTFFIND\'s FStep parameter'
params ctf_win 'Estimate CTF on window size (pix):' range '-1, -16, 4096, 16' 'If a positive value is given, a squared window of this size at the center of the micrograph will be used to estimate the CTF. This may be useful to exclude parts of the micrograph that are unsuitable for CTF estimation, e.g. the labels at the edge of photographic film. \n \n The original micrograph will be used (i.e. this option will be ignored) if a negative value is given.' 
process nr_mpi "Number of MPI procs:" range '{qsub_nrmpi_val} , 1, {mpi_max}, 1' "Number of MPI nodes to use in parallel. When set to 1, MPI will not be used. The maximum can be set through the environment variable RELION_MPI_MAX."
process nr_threads "Number of threads:" range '{qsub_nrthreads_val}, 1, {getenv("RELION_THREAD_MAX")} 1' "Number of shared-memory (POSIX) threads to use in parallel. When set to 1, no multi-threading will be used. The maximum can be set through the environment variable RELION_THREAD_MAX."
}

_command.prog_mpi 'relion_run_ctffind_mpi' 
_command.prog     'relion_run_ctffind'

loop_
_cli.type
_cli.content
_cli.flag
_cli.bool
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

