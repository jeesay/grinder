data_00_ctffind4
#
_main.id           relion.ctffind.ctffind4
_main.hidden_name  '.gui_ctffind'
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
_fieldsets.parent_id
_fieldsets.id
_fieldsets.icon
_fieldsets.label
_fieldsets.widget
_fieldsets.default
_fieldsets.help
io input ? ? fieldset ? ?
settings general ? 'General' fieldset ? ?
settings do_phaseshift ? 'Estimate phase shifts?' switch false  'If set to Yes, CTFFIND4 will estimate the phase shift, e.g. as introduced by a Volta phase-plate'
settings params ? 'CTFFIND 4.1 Parameters' fieldset ? ?
running processes ? ? fieldset ? ?
running queue ? ? switch false ?

#
loop
_input.id
_input.label 
_input.widget 
_input.path 
_input.default 
_input.file_type
_input.help
input_star_mics 'Input micrographs STAR file:' file_browser NODE_MICS_CPIPE 'STAR files (*.star)' ? ? 'A STAR file with all micrographs to run CTFFIND on'
#
# CTFFIND options
loop_
_params.parent_id
_params.id
_params.label
_params.widget
_params.params
_params.help
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


loop_
_cli.type
_cli.content
_cli.flag
_cli.bool
prog     '`which relion_run_ctffind_mpi`' '`which relion_run_ctffind`' ?
io       '--i {input_star_mics} --o {outputname}' ? ?
param    '--Box {box} --ResMin {resmin} --ResMax {resmax}' ? ?
param    '--dFMin {dfmin} --dFMax {dfmax} --FStep {dfstep} --dAst {dast}' ? ?
flag     '--use_noDW' use_noDW  true 
flag     '--do_phaseshift --phase_min {phase_min} --phase_max {phase_max} --phase_step {phase_step}' do_phaseshift true
param    '--ctffind_exe {fn_ctffind_exe} --ctfWin {ctf_win} --is_ctffind4' ? ?
flag     '--fast_search' slow_search false
flag     '--use_given_ps' use_given_ps true
flag     '--only_do_unfinished ' is_continue true
param    '{other_args}' ? ?
#

data_gctf
#
_input_star_mics.label       'Input micrographs STAR file:'
_input_star_mics.widget      file_browser
_input_star_mics.path        NODE_MICS_CPIPE, 
_input_star_mics.default       ''
_input_star_mics.file_type   'STAR files (*.star)'
_input_star_mics.help        'A STAR file with all micrographs to run Gctf on'
_input_star_mics.arg         --i
#
_use_noDW.label                'Use micrograph without dose-weighting?'
_use_noDW.widget               checkbox
_use_noDW.default              false 
_use_noDW.help
;If set to Yes, the CTF estimation will be done using 
the micrograph without dose-weighting as in rlnMicrographNameNoDW 
(_noDW.mrc from MotionCor2). If set to No, the normal rlnMicrographName will be used.
_use_noDW.arg
;
#'use_gctf'    'Use Gctf instead?' false 'If set to Yes, Kai Zhang's Gctf program (which runs on NVIDIA GPUs) will be used instead of Niko Grigorieff's CTFFIND4.'

#	default_location = getenv('RELION_GCTF_EXECUTABLE');
#	char default_gctf[] = DEFAULTGCTFLOCATION;
#	if (default_location == NULL)
#	{
#		default_location = default_gctf;
#	}
#'fn_gctf_exe'    'Gctf executable:', std::string(default_location), '*', '.', 'Location of the Gctf executable. You can control the default of this field by setting environment variable RELION_GCTF_EXECUTABLE, or by editing the first few lines in src/gui_jobwindow.h and recompile the code.');
#'do_ignore_ctffind_params'    'Ignore 'Searches' parameters?', true, 'If set to Yes, all parameters EXCEPT for phase shift search and its ranges on the 'Searches' tab will be ignored, and Gctf's default parameters will be used (box.size=1024; min.resol=50; max.resol=4; min.defocus=500; max.defocus=90000; step.defocus=500; astigm=1000) \n \
#\nIf set to No, all parameters on the CTFFIND tab will be passed to Gctf.');
#'do_EPA'    'Perform equi-phase averaging?', false, 'If set to Yes, equi-phase averaging is used in the defocus refinement, otherwise basic rotational averaging will be performed.');
#'other_gctf_args'    'Other Gctf options:', std::string(''), 'Provide additional gctf options here.');
#'gpu_ids'    'Which GPUs to use:', std::string(''), 'This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','. ');
#}
