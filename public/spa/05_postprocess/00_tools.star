data_
#
_id       post_tools
_label    Tools
_icon     bi-tools
_index    5
_parent   postp
#
loop_
_post_tools.id
_post_tools.label 
_post_tools.icon
_post_tools.widget 
_post_tools.default
_post_tools.parent_id
_post_tools.help
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
postprocess  'Post-processing'    bi-2-circle-fill fieldset ? post_tools ?
ctfrefine    'CTF Refinement'     bi-3-circle-fill fieldset ? post_tools ?
motionrefine       'Motion Refinement' bi-4-circle-fill fieldset ? post_tools ?
#
loop_
_postprocess.id
_postprocess.label        
_postprocess.widget    
_postprocess.proc_id 
_postprocess.labelnew
_postprocess.filename
_postprocess.help
pprcss      'Post-Processing'       radio_tool      15      "relion.postprocess"        01.star         "?"
#
loop_
_motionrefine.id
_motionrefine.label        
_motionrefine.widget    
_motionrefine.proc_id 
_motionrefine.labelnew
_motionrefine.filename
_motionrefine.help
ptcls_polish        'Perform Particle Polishing'     radio_tool       20          "relion.polish"         02.star         "?"   
other_polish        'Bayesian Polishing'             radio_tool       20          "relion.polish"         03.star         "?"   


