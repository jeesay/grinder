data_
#
loop_
_misc.id
_misc.label 
_misc.icon
_misc.widget 
selection  'Subset Selection'           bi-list-check            submenu
class_sel  'Class Ranker'               bi-cookie                submenu
split_data 'Split Data'                 bi-arrows-angle-expand   submenu
joinstar   'Join STAR files'            bi-arrows-angle-contract submenu
extras     'Extras'                     bi-bag-plus              submenu
#
loop_
_selection.id
_selection.label        
_selection.widget    
_selection.proc_id 
_selection.labelnew
_selection.filename
_selection.help   
subselect_class       "Select classes from job"                 radio_tool              7           "relion.select"           01.star       "?"
subselect_mic         "Select from micrographs.star"            radio_tool              7           "relion.select"           02.star       "?"
subselect_ptcls       "Select from particles.star"              radio_tool              7           "relion.select"           03.star       "?"
#
loop_
_joinstar.id
_joinstar.label        
_joinstar.widget    
_joinstar.proc_id 
_joinstar.labelnew
_joinstar.filename
_joinstar.help   
join_ptcls      "Combine particle STAR files"         radio_tool      13          "relion.joinstar"       04.star           "?"
join_mics       "Combine micrograph STAR files"       radio_tool      13          "relion.joinstar"       05.star           "?"
join_movs       "Combine movie STAR files"            radio_tool      13          "relion.joinstar"       06.star           "?"
#
loop_
_extras.id
_extras.label        
_extras.widget    
_extras.proc_id 
_extras.labelnew
_extras.filename
_extras.help   
external        "Provide an External Executable"        radio_tool      99      "relion.external"       07.star         "?"