data_
#
loop_
_postp.id
_postp.label 
_postp.icon
_postp.widget 
postprocess  'Post-processing'    bi-1-circle-fill submenu
ctfrefine    'CTF Refinement'     bi-2-circle-fill submenu
motionrefine 'Motion Refinement'  bi-3-circle-fill submenu
#
loop_
_postprocess.id
_postprocess.label        
_postprocess.widget    
_postprocess.proc_id 
_postprocess.proc_label
_postprocess.filename
_postprocess.help
pprcss      'Post-Processing'       tool      15      "relion.postprocess"        01.star         "?"
#
loop_
_motionrefine.id
_motionrefine.label        
_motionrefine.widget    
_motionrefine.proc_id 
_motionrefine.proc_label
_motionrefine.filename
_motionrefine.help
ptcls_polish        'Polishing Train'  tool       20          "relion.polish.train"   02.star         "?"   
other_polish        'Polishing'        tool       20          "relion.polish"         03.star         "?"   
#
loop_
_ctfrefine.id
_ctfrefine.label        
_ctfrefine.widget    
_ctfrefine.proc_id 
_ctfrefine.proc_label
_ctfrefine.filename
_ctfrefine.help
anisomag           'Aniso. Mag.'      tool      21      "relion.ctfrefine.anisomag"   04.star         "Anisotropic Magnification Estimation CTF Refinement"
ctfref             'CTF Refine'       tool      21      "relion.ctfrefine"            05.star         "Classical CTF Refinement"


