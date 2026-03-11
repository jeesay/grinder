data_
#
_id       enhance_tools
_label    Tools
_icon     bi-tools
_index    6
_parent   enhance
#
loop_
_enhance_tools.id
_enhance_tools.label 
_enhance_tools.icon
_enhance_tools.widget 
_enhance_tools.default
_enhance_tools.parent_id
_enhance_tools.help
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
mask_making     'Making a Mask'         bi-1-circle-fill    fieldset ? enhance_tools ?
locres          'Local Resolution'      bi-trophy           fieldset ? enhance_tools ?
subpart         'Particle Substraction' ?                   fieldset ? enhance_tools ?
#
loop_
_mask_making.id
_mask_making.label        
_mask_making.widget    
_mask_making.proc_id 
_mask_making.labelnew
_mask_making.filename
_mask_making.help   
mask_create        'Mask Creation'         radio_tool       12      "relion.maskcreate"      01.star     "?"
#
loop_
_subpart.id
_subpart.label        
_subpart.widget    
_subpart.proc_id 
_subpart.labelnew
_subpart.filename
_subpart.help 
sub_mask            'Center Substracted Images on Mask'         radio_tool      14      "relion.subtract"       02.star     "?"
sub_coor            'Center on Coordinates'                     radio_tool      14      "relion.subtract"       03.star     "?"
#
loop_
_locres.id
_locres.label        
_locres.widget    
_locres.proc_id 
_locres.labelnew
_locres.filename
_locres.help 
resmap_locres       "ResMap Local Resolution"           radio_tool      16      "relion.localres"       04.star         "?"
rln_locres          "RELION Local Resolution"           radio_tool      16      "relion.localres"       05.star         "?"