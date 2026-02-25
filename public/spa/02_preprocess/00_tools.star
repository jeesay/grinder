data_
#
_id       prep_tools
_label    Tools
_icon     bi-tools
_index    2
_parent   prep
#
loop_
_prep_tools.id
_prep_tools.label 
_prep_tools.icon
_prep_tools.widget 
_prep_tools.default
_prep_tools.parent_id
_prep_tools.help
tool_menu      'Tools'   bi-tools toolmenu  ? ?
#
loop_
_tool_menu.id
_tool_menu.label 
_tool_menu.icon
_tool_menu.widget 
_tool_menu.default
_tool_menu.parent
_tool_menu.help
motion 'Motion Correction'  bi-graph-up  fieldset ? prep_tools ?
ctffind 'CTF Estimation'    bi-bullseye  fieldset ? prep_tools ?
curation 'Micrograpĥ Curation' bi-check2-square  fieldset ? prep_tools ?
#
loop_
_motion.id
_motion.label
_motion.widget
_motion.proc_id
_motion.labelnew
_motion.help
_motion.filename
rln_mc   "RELION Motion Correction"    radio_tool    1    relion.motioncorr.own    'RELIONs own implementation'    01.star
mc2   "UCSF Motion Correction2"    radio_tool    1    relion.motioncorr.motioncor2    'MotionCorr executable'    02.star
