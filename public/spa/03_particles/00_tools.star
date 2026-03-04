data_
#
_id       particles_tools
_label    Tools
_icon     bi-tools
_index    3
_parent   ptcls
#
loop_
_particles_tools.id
_particles_tools.label 
_particles_tools.icon
_particles_tools.widget 
_particles_tools.default
_particles_tools.parent_id
_particles_tools.help
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
manual     'Manual Picking'           bi-hand-index-thumb    fieldset ? particles_tools ?
auto       'Auto Picking'             bi-check2-square       fieldset ? particles_tools ?
auto_topaz 'Auto Picking by Topaz'    bi-robot               fieldset ? particles_tools ?
extract    'Particle extraction'      bi-crop                fieldset ? particles_tools ?
class2d    '2D classification'        bi-sort-numeric-down   fieldset ? particles_tools ?

