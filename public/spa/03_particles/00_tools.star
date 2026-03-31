data_
#
loop_
_ptcls.id
_ptcls.label 
_ptcls.icon
_ptcls.widget 

manual     'Manual Picking'           bi-hand-index-thumb    submenu
auto       'Auto Picking'             bi-check2-square       submenu
auto_topaz 'Topaz'                    bi-robot               submenu
extract    'Particle extraction'      bi-crop                submenu
class2d    '2D classification'        bi-images              submenu
#
loop_
_auto.id
_auto.label        
_auto.widget    
_auto.proc_id 
_auto.labelnew
_auto.help   
_auto.filename
log_filter       "Laplacian of Gaussian filter"             radio_tool              4           ?           "?"             01.star
ref2d           "Picking by 2D References"                  radio_tool              4           ?           "?"             02.star
ref3d           "Picking by 3D References"                  radio_tool              4           ?           "?"             03.star
#
loop_
_auto_topaz.id
_auto_topaz.label        
_auto_topaz.widget    
_auto_topaz.proc_id 
_auto_topaz.labelnew
_auto_topaz.help   
_auto_topaz.filename
topaz_train     "Topaz Training"                 radio_tool              4           ?           "?"             04.star
topaz_pick      "Topaz picking"                  radio_tool              4           ?           "?"             05.star
#
loop_
_extract.id
_extract.label        
_extract.widget    
_extract.proc_id 
_extract.labelnew
_extract.help   
_extract.filename
extract_ptcls       "Extract Particules"                 radio_tool              5           ?           "?"             06.star
reextract_ptcls     "Re-extract Refined Particles"       radio_tool              5           ?           "?"             07.star
#
loop_
_class2d.id
_class2d.label        
_class2d.widget    
_class2d.proc_id 
_class2d.labelnew
_class2d.help   
_class2d.filename
class2d_em          "Expectation Maximisation Algorithm (EM)"    radio_tool   7       ?                '?'   08.star
class2d_vdam        "VDAM Algorithm"                             radio_tool   7       ?                '?'   09.star
