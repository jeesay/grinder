data_
#
loop_
_misc.id
_misc.label 
_misc.icon
_misc.widget 
selection  'Subset Selection'   bi-list-check            submenu
split_data 'Split Data'         bi-arrows-angle-expand   submenu
joinstar   'Join STAR files'    bi-arrows-angle-contract submenu
extras     'Extras'             bi-bag-plus              submenu
#
loop_
_selection.id
_selection.label        
_selection.widget    
_selection.proc_id 
_selection.proc_label
_selection.filename
_selection.help   
subselect_class       "From job"                 tool              7           "relion.select.job"           01.star       "?"
subselect_mic         "From micrographs.star"    tool              7           "relion.select.micrographs"   02.star       "?"
subselect_ptcls       "From particles.star"      tool              7           "relion.select.particles"     03.star       "?"
#
loop_
_joinstar.id
_joinstar.label        
_joinstar.widget    
_joinstar.proc_id 
_joinstar.proc_label
_joinstar.filename
_joinstar.help   
join_ptcls      "Particle STAR files"         tool      13          "relion.joinstar.particles"       04.star           "?"
join_mics       "Micrograph STAR files"       tool      13          "relion.joinstar.micrographs"     05.star           "?"
join_movs       "Movie STAR files"            tool      13          "relion.joinstar.movies"          06.star           "?"
#
loop_
_extras.id
_extras.label        
_extras.widget    
_extras.proc_id 
_extras.proc_label
_extras.filename
_extras.help   
test            "Test"                                  tool      99      "grinder.debug.test"    10.star         "Test only for debugging"