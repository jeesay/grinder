data_
#
loop_
_rec3d.id
_rec3d.label 
_rec3d.icon
_rec3d.widget 
ab_initio     'Ab initio'           bi-box       submenu
class_3d      '3D Classification'   bi-boxes     submenu
refine        'Refinement'          bi-crosshair submenu
#
loop_
_ab_initio.id
_ab_initio.label        
_ab_initio.widget    
_ab_initio.proc_id 
_ab_initio.labelnew
_ab_initio.filename
_ab_initio.help   
inimodel        '3D initial référence'      radio_tool      18       "relion.initialmodel"     01.star        "?" 
cryodrgn_abinit 'CryoDRGN Ab Initio'        radio_tool      99       "cryodrgn.abinit"         08.star        "Ab Initio Reconstruction with Generative AI"
#
loop_
_class_3d.id
_class_3d.label        
_class_3d.widget    
_class_3d.proc_id 
_class_3d.labelnew
_class_3d.filename
_class_3d.help   
3d_align        '3D Classification with image alignment'        radio_tool      9       "relion.class3d.align"    02.star     "?"
3d_skip_align   '3D Classification'                             radio_tool      9       "relion.class3d"          03.star     "?"
#
loop_
_refine.id
_refine.label        
_refine.widget    
_refine.proc_id 
_refine.labelnew  
_refine.filename
_refine.help 
autorefine      '3D Auto-Refine'                                  radio_tool      10          "relion.refine3d"             04.star      "?"
multibody_flex  '3D Multi-body with flexibility analysis'         radio_tool      19          "relion.multibody.flex"       05.star      "?"
multibody       '3D Multi-body'                                   radio_tool      19          "relion.multibody"            06.star      "?"
dynamight       'DynaMight flexibility (Deep Learning model)'     radio_tool      22          "dynamight"                   07.star      "?"