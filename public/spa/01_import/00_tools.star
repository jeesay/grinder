data_
# Menu
loop_
_import.id
_import.label
_import.icon
_import.widget
gdr_import  'GRINDER'           bi-cup-hot-fill       submenu
rln_import  'From RELION'       bi-r-circle-fill      submenu
cs_import   'From CryoSparc'    bi-c-circle-fill      submenu
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
import_mov      'Movies'                 tool   0  relion.import.movies           01.star   'Import Movies'
import_mics     'Micrographs'            tool   0  relion.import.mics             02.star   'Import Micrographs'
import_coords   'Coordinates'            tool   0  relion.import.other.box        03.star   'Import Coordinates (*.box,etc.)'
import_parts    'Particles (*.star)'     tool   0  relion.import.other.parts      04.star   'Import Particles as STAR file'  
import_2dimg    '2D/3D References'       tool   0  relion.import.other.refs       05.star   'Import 2D/3D References'  
import_map      'Density Map'            tool   0  relion.import.other.map        06.star   'Import Density Map'       
import_mask     'Mask'                   tool   0  relion.import.other.mask       07.star   'Import Mask'           
import_halfmap  'Half-map(s)'            tool   0  relion.import.other.halfmap    08.star   'Import Half-maps'                                        
# Submenu
loop_
_gdr_import.id
_gdr_import.label        
_gdr_import.widget    
_gdr_import.proc_id 
_gdr_import.proc_label
_gdr_import.filename
_gdr_import.help   
grr_import_all        'Import...'        tool   0       grinder.import.relion      10.star   'Import File(s) for RELION'                           
# Submenu
loop_
_cs_import.id
_cs_import.label        
_cs_import.widget    
_cs_import.proc_id 
_cs_import.proc_label
_cs_import.filename
_cs_import.help   
pyem_import_ptcls      'Particles'        tool   0       pyem.import.relion      20.star   'Import Patticles from Cryosparc with PyEM'                           


