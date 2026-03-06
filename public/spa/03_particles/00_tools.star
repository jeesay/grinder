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
#
loop_
_class2d.id
_class2d.label        
_class2d.widget    
_class2d.proc_id 
_class2d.labelnew
_class2d.help   
_class2d.filename
class2d_em          "Expectation Maximisation Algorithm (EM)"    radio_tool   7       ?                '?'   99.star
class2d_vdam        "VDAM Algorithm"                             radio_tool   7       ?                '?'   98.star
#
loop_
_auto.id
_auto.label        
_auto.widget    
_auto.proc_id 
_auto.labelnew
_auto.help   
_auto.filename
log_filter       "Laplacian of Gaussian filter"             radio_tool              4           ?           "?"             97.star
ref2d           "Picking by 2D References"                  radio_tool              4           ?           "?"             96.star
ref3d           "Picking by 3D References"                  radio_tool              4           ?           "?"             95.star
#
loop_
_auto_topaz.id
_auto_topaz.label        
_auto_topaz.widget    
_auto_topaz.proc_id 
_auto_topaz.labelnew
_auto_topaz.help   
_auto_topaz.filename
topaz_train     "Topaz Training"                 radio_tool              4           ?           "?"             94.star
topaz_pick      "Topaz picking"                  radio_tool              4           ?           "?"             93.star
#
loop_
_extract.id
_extract.label        
_extract.widget    
_extract.proc_id 
_extract.labelnew
_extract.help   
_extract.filename
extract_ptcls       "Extract Particules"                 radio_tool              5           ?           "?"             92.star
reextract_ptcls     "Re-extract Refined Particles"       radio_tool              5           ?           "?"             91.star