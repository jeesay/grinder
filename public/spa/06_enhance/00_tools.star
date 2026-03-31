data_
#
loop_
_enhance.id
_enhance.label 
_enhance.icon
_enhance.widget 
mask_making     'Making a Mask'         bi-mask             submenu
locres          'Local Resolution'      bi-trophy           submenu
subpart         'Ptcls Substraction'    bi-dash-circle      submenu
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