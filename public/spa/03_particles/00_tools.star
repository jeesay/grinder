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
extract    'Extraction'               bi-crop                submenu
class2d    '2D classification'        bi-images              submenu
class_sel  'Class Selection'          bi-cookie              submenu
#
loop_
_manual.id
_manual.label        
_manual.widget    
_manual.proc_id 
_manual.proc_label
_manual.help   
_manual.filename
interactive      "Interactive"     tool      4           relion.manualpick          "?"    00.star
#
loop_
_auto.id
_auto.label        
_auto.widget    
_auto.proc_id 
_auto.proc_label
_auto.filename
_auto.help   
log_filter      "LoG"              tool              4           relion.autopick.log           01.star    "Blob Detection with Laplacian of Gaussian filter"
ref2d           "2D References"    tool              4           relion.autopick.ref2d         02.star    "Template Matching from 2D References"
ref3d           "3D References"    tool              4           relion.autopick.ref3d         03.star    "Template Matching from 3D Reference"
#
loop_
_auto_topaz.id
_auto_topaz.label        
_auto_topaz.widget    
_auto_topaz.proc_id 
_auto_topaz.proc_label
_auto_topaz.filename
_auto_topaz.help   
topaz_train     "Topaz Training"      tool     4    relion.autopick.topaz.train    04.star   "?"             
topaz_pick      "Topaz Picking"       tool     4    relion.autopick.topaz.pick     05.star   "?"             
#
loop_
_extract.id
_extract.label        
_extract.widget    
_extract.proc_id 
_extract.proc_label
_extract.filename
_extract.help   
extract_ptcls       "Particles"               tool     5    relion.extract            06.star "?"             
reextract_ptcls     "Re-extract Refined"      tool     5    relion.extract.reextract  07.star "?"             
#
loop_
_class2d.id
_class2d.label        
_class2d.widget    
_class2d.proc_id 
_class2d.proc_label
_class2d.filename
_class2d.help   
class2d_em          "EM Algorithm"    tool   7      relion.class2d.em          08.star 'Expectation Maximisation Algorithm (EM)'   
class2d_vdam        "VDAM Algorithm"  tool   7      relion.class2d.vdam        09.star '?' 
#
loop_
_class_sel.id
_class_sel.label        
_class_sel.widget    
_class_sel.proc_id 
_class_sel.proc_label
_class_sel.filename
_class_sel.help 
class2d_rank        'Class Ranker'    tool   7      relion.select.class2dauto  10.star
; If set to Yes, the class_ranker program will be used to make an automated class selection. 
This option only works when selecting classes from a `relion_refine` job (input optimiser.star on the I/O tab)
;