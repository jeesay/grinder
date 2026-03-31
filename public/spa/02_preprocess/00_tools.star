data_
#
loop_
_prep.id
_prep.label 
_prep.icon
_prep.widget 
motion 'Motion Correction'  bi-graph-up  submenu
ctffind 'CTF Estimation'    bi-bullseye  submenu
curation 'Mgraph Curation'  bi-check2-square  submenu
#
loop_
_motion.id
_motion.label
_motion.widget
_motion.proc_id
_motion.labelnew
_motion.help
_motion.filename
rln_mc   "RELION Motion Correction"    radio_tool    1    "relion.motioncorr.own"           'RELIONs own implementation'    01.star
ucsf_mc   "UCSF Motion Correction2"    radio_tool    1    "relion.motioncorr.motioncor2"    'MotionCorr executable'         02.star
#
loop_
_ctffind.id
_ctffind.label
_ctffind.widget
_ctffind.proc_id
_ctffind.labelnew
_ctffind.help
_ctffind.filename
ctf         "CTFFIND 4.1"       radio_tool     2      "relion.ctffind"    "CTF with CTFFIND 4.1"    03.star
