data_
# Menu
loop_
_import.id
_import.label
_import.icon
_import.widget
grr_import  'GRINDER'      bi-cup-hot-fill       submenu
rln_import  'RELION'       bi-r-circle-fill      submenu
cs_import   'CryoSparc'    bi-c-circle-fill      submenu
# refs        'References'             bi-r-circle      submenu
# masks       'Masks'                  bi-mask          submenu
# others      'Other Files'            bi-file-binary   submenu

# Submenu
loop_
_rln_import.id
_rln_import.label        
_rln_import.widget    
_rln_import.proc_id 
_rln_import.proc_label
_rln_import.filename
_rln_import.help   
import_mov        'Import movies'        tool   0       relion.import.movies                01.star   'Import Micrographs or Movies'                           
import_ptcls      'Import particles'     tool   0       relion.import.other.particles       02.star   'Import Particles'                                        
import_other      'Import other files'   tool   0       relion.import.other                 03.star   'Import Other Files'              
# Submenu
loop_
_grr_import.id
_grr_import.label        
_grr_import.widget    
_grr_import.proc_id 
_grr_import.proc_label
_grr_import.filename
_grr_import.help   
grr_import_mov        'Import movies'        tool   0       grinder.import.movies                04.star   'Import Micrographs or Movies'                           
grr_import_ptcls      'Import particles'     tool   0       grinder.import.other.particles       05.star   'Import Particles'                                        
grr_import_other      'Import other files'   tool   0       grinder.import.other                 06.star   'Import Other Files'              


