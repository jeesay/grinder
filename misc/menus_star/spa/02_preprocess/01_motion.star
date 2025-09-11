data_motion_own
#
_toolbox.id motion
_toolbox.label 'Motion Correction'
_toolbox.icon bi-graph-up
#
_main.id           relion.motioncor.own
_main.hidden_name '.gui_motioncorr"'
_main.use_ctffind4 true
#
_main.parent_id    01_ctffind 
_main.label        'CTF with CTFFIND 4.1' 
_main.help         'If set to Yes, the wrapper will use CTFFIND4 (version 4.1) for CTF estimation. This includes thread-support, calculation of Thon rings from movie frames and phase-shift estimation for phase-plate data.'
#
_tools.parent_id
_tools.label
_tools.help
_tools.starfile
_tools.block
motion 'Relion Motioncor2-like implementation' ? ? ?
motion 'UCSF MotionCor 2' ? ? ?
motion 'TODO -  MotionCor 3 (includes CTF estimation)' 'Chan Zuckerberg Imaging Institute (CZII) version' ? ?

ctffind 'CTF with CTFFIND 4.1' 'If set to Yes, the wrapper will use CTFFIND4 (version 4.1) for CTF estimation. This includes thread-support, calculation of Thon rings from movie frames and phase-shift estimation for phase-plate data.' relion_ctffind.star ctffind4
ctffind 'CTF with GCTF' ? relion_ctffind.star gctf
