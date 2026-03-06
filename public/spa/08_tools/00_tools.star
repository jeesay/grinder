data_
#
_id       star_tools
_label    Tools
_icon     bi-tools
_index    8
_parent   misc
#
loop_
_star_tools.id
_star_tools.label 
_star_tools.icon
_star_tools.widget 
_star_tools.default
_star_tools.parent_id
_star_tools.help
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
selection  'Subset selection'           bi-list-check            fieldset ? misc_tools ? 
class_sel  'Automatic class selection'  bi-robot                 fieldset ? misc_tools ? 
split_data 'Split data'                 bi-arrows-angle-expand   fieldset ? misc_tools ? 
joinstar   'Join STAR files'            bi-arrows-angle-contract fieldset ? misc_tools ? 
extras     'Extras'                     bi-bag-plus              fieldset ? misc_tools ?
#
loop_
_selection.id
_selection.label        
_selection.widget    
_selection.proc_id 
_selection.labelnew
_selection.help   
_selection.filename
subselect_class       "Select classes from job"                 radio_tool              7           ?           "?"             01.star
subselect_mic         "Select from micrographs.star"            radio_tool              7           ?           "?"             02.star
subselect_ptcls       "Select from particles.star"              radio_tool              7           ?           "?"             03.star
