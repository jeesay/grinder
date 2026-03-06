data_
#
_id       import_tools
_label    Tools
_icon     bi-tools
_index    1
_widget   program
_parent   import
#
loop_
_import_tools.id
_import_tools.label
_import_tools.icon
_import_tools.widget
_import_tools.default
_import_tools.help
tool_menu      'Tools'   bi-tools toolmenu  ? ?
#
loop_
_tool_menu.id
_tool_menu.label 
_tool_menu.icon
_tool_menu.widget 
_tool_menu.default
_tool_menu.parent
_tool_menu.help
rln_import  'RELION File Import'       bi-r-circle-fill      fieldset ? import_tools ?
cs_import   'CryoSparc File Import'    bi-c-circle-fill      fieldset ? import_tools ?
# refs        'References'             bi-r-circle      fieldset ? import_tools ?
# masks       'Masks'                  bi-mask          fieldset ? import_tools ?
# others      'Other Files'            bi-file-binary   fieldset ? import_tools ?

#
loop_
_rln_import.id
_rln_import.label        
_rln_import.widget    
_rln_import.proc_id 
_rln_import.labelnew
_rln_import.help   
_rln_import.filename
import_mov        'Import movies'        radio_tool   0       relion.import.raw                'Import Micrographs or Movies'   01.star                          
import_ptcls      'Import particles'     radio_tool   0       relion.import.other              'Import Particles'               02.star                          
import_other      'Import other files'   radio_tool   0       relion.import.other              'Import Other File'              03.star   


