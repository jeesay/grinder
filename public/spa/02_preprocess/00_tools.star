data_
#
loop_
_prep.id
_prep.label 
_prep.icon
_prep.widget 
motion       'Motion Correction'  bi-graph-up          submenu
ctffind      'CTF Estimation'     bi-bullseye          submenu
mic_curation 'Curation'           bi-cart-plus         submenu
mic_denoise  'Denoise'            bi-noise-reduction   submenu
#
loop_
_motion.id
_motion.label
_motion.widget
_motion.proc_id
_motion.proc_label
_motion.filename
_motion.help
rln_mc   "RELION Version"    tool    1    "relion.motioncorr.own"           01.star  "RELION's own implementation"    
ucsf_mc   "UCSF MC2"         tool    1    "relion.motioncorr.motioncor2"    02.star  'MotionCorr executable'         
#
loop_
_ctffind.id
_ctffind.label
_ctffind.widget
_ctffind.proc_id
_ctffind.proc_label
_ctffind.filename
_ctffind.help
ctf         "CTFFIND 4.1"       tool     2      "relion.ctffind"    03.star    "CTF with CTFFIND 4.1"    
#
loop_
_mic_curation.id
_mic_curation.label
_mic_curation.widget
_mic_curation.proc_id
_mic_curation.proc_label
_mic_curation.filename
_mic_curation.help
curation    'Interactive'   tool     2      "grinder.curation"  04.star    "Micrograph Curation" 
#
loop_
_mic_denoise.id
_mic_denoise.label
_mic_denoise.widget
_mic_denoise.proc_id
_mic_denoise.proc_label
_mic_denoise.filename
_mic_denoise.help
tpz_denoise    'Topaz'   tool     2      "topaz.denoise"  05.star    "Topaz Micrograph Denoising" 
 