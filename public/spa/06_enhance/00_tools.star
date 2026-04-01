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
_mask_making.proc_label
_mask_making.filename
_mask_making.help   
mask_create        'Mask Creation'         tool       12      "relion.maskcreate"      01.star     "?"
#
loop_
_subpart.id
_subpart.label        
_subpart.widget    
_subpart.proc_id 
_subpart.proc_label
_subpart.filename
_subpart.help 
sub_mask            'Center on Mask'           tool      14      "relion.subtract"              02.star     "If set to Yes, the subtracted particles will be centered on projections of the center-of-mass of the input mask."
sub_coor            'Center on Coords'         tool      14      "relion.subtract.xyz"          03.star     
; If set to Yes, the subtracted particles will be centered on projections of the x,y,z coordinates below. 
The unit is pixel, not angstrom. The origin is at the center of the box, not at the corner.
;
sub_revert          'Revert particles'         tool      14      "relion.subtract.revert"       04.star     "?"
#
loop_
_locres.id
_locres.label        
_locres.widget    
_locres.proc_id 
_locres.proc_label
_locres.filename
_locres.help 
resmap_locres       "ResMap"           tool      16      "relion.localres.resmap"   05.star         "?"
rln_locres          "RELION"           tool      16      "relion.localres"          06.star
; If set to Yes, then relion_postprocess will be used for local-resolution estimation. 
This program basically performs a series of post-processing operations with a small soft, spherical mask that is moved over the entire map, 
while using phase-randomisation to estimate the convolution effects of that mask.

The output relion_locres.mrc map can be used to color the surface of a map in UCSF Chimera according to its local resolution. 
The output relion_locres_filtered.mrc is a composite map that is locally filtered to the estimated resolution. 
This is a developmental feature in need of further testing, but initial results indicate it may be useful.

Note that only this program can use MPI, the ResMap wrapper cannot use MPI.
;