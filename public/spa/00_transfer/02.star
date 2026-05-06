data_
#
#
loop_
_rln_proj_load.id
_rln_proj_load.label
_rln_proj_load.icon
_rln_proj_load.widget
project        "Load..."      bi-building-down     tab
log            "Log"          bi-binoculars-fill   tab
dataviz        "DataViz"      bi-eye               tab
#
#
loop_
_project.id
_project.label 
_project.icon
_project.widget 
_project.default
_project.parent
_project.state
_project.help
project_sel            'Project List'    bi-building-down            fieldset ?      ? ?        ?

#
loop_
_project_sel.id
_project_sel.label
_project_sel.icon
_project_sel.widget
_project_sel.default 
_project_sel.state
_project_sel.help
proj_list             'Project'       ?               select  ?                   required 'Choose one existing RELION Project'
proj_list::proj_none  '-- Choose --'  bi-building-add option  RELION_NONE         ?        ?