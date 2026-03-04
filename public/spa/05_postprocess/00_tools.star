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
polish       'Bayesian polishing' bi-4-circle-fill fieldset ? post_tools ?




