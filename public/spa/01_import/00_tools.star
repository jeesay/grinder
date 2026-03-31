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
_rln_import.labelnew
_rln_import.help   
_rln_import.filename
import_mov        'Import movies'        radio_tool   0       relion.import.movies                'Import Micrographs or Movies'   01.star                          
import_ptcls      'Import particles'     radio_tool   0       relion.import.other.particles       'Import Particles'               02.star                          
import_other      'Import other files'   radio_tool   0       relion.import.other                 'Import Other File'              03.star   


