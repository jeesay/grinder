data_
#
_id       model_tools
_label    Tools
_icon     bi-tools
_index    7
_parent   model
#
loop_
_model_tools.id
_model_tools.label 
_model_tools.icon
_model_tools.widget 
_model_tools.default
_model_tools.parent_id
_model_tools.help
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
model    'Model Building' ?          fieldset ? model_tools ?
#
loop_
_model.id
_model.label        
_model.widget    
_model.proc_id 
_model.labelnew
_model.filename
_model.help 
angelo      'ModelAngelo Building'      radio_tool      23      "modelangelo"       01.star         "?"