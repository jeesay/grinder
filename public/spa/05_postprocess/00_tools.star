data_
#
loop_
_postp.id
_postp.label 
_postp.icon
_postp.widget 
postprocess  'Post-processing'    bi-2-circle-fill submenu
ctfrefine    'CTF Refinement'     bi-3-circle-fill submenu
motionrefine 'Motion Refinement'  bi-4-circle-fill submenu
#
loop_
_postprocess.id
_postprocess.label        
_postprocess.widget    
_postprocess.proc_id 
_postprocess.labelnew
_postprocess.filename
_postprocess.help
pprcss      'Post-Processing'       radio_tool      15      "relion.postprocess"        01.star         "?"
#
loop_
_motionrefine.id
_motionrefine.label        
_motionrefine.widget    
_motionrefine.proc_id 
_motionrefine.labelnew
_motionrefine.filename
_motionrefine.help
ptcls_polish        'Perform Particle Polishing'     radio_tool       20          "relion.polish"         02.star         "?"   
other_polish        'Bayesian Polishing'             radio_tool       20          "relion.polish"         03.star         "?"   
#
loop_
_ctfrefine.id
_ctfrefine.label        
_ctfrefine.widget    
_ctfrefine.proc_id 
_ctfrefine.labelnew
_ctfrefine.filename
_ctfrefine.help
anisomag           'Anisotropic Magnification Estimation CTF Refinement'       radio_tool      21      "relion.ctfrefine"      04.star         "?"
ctfref              'Classic CTF Refinement'                                    radio_tool      21      "relion.ctfrefine"      05.star         "?"


