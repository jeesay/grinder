data_
# Menu
loop_
_import.id
_import.label
_import.icon
_import.widget
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
import_other      'Import other files'   tool   0       relion.import.other                 03.star   'Import Other File'              


