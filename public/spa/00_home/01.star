data_
#
#
loop_
_home_dashboard.id
_home_dashboard.label
_home_dashboard.icon
_home_dashboard.widget
home_dash        "Home"      bi-house-door     tab  
#
loop_
_home_dash.id
_home_dash.label 
_home_dash.icon
_home_dash.widget 
_home_dash.default
_home_dash.parent
_home_dash.state
_home_dash.help
connect         'Server Connection'    bi-wifi            fieldset ? ? ?        ?
project         'Projects'             bi-newspaper       fieldset ? ? hidden   ?
project_new     'Create New Project'   bi-folder-plus     fieldset ? ? hidden   ?
project_summary 'Project Summary'      bi-clipboard-data  fieldset ? ? hidden   ?
software        'Available Softwares'  bi-plugin          fieldset ? ? hidden   ?
#
loop_
_connect.id
_connect.label
_connect.widget
_connect.default  # None
_connect.arg0     # Status
_connect.arg1     # Placeholder
_connect.arg2     # Node Type
_connect.help
ws_server_ip  'Server IP Address'   string  '127.0.0.1' ?       ? ?  'URL displayed by `grinder-server`'
ws_port       'Server Port'         string  8000        ?       ? ?  'Port displayed by `grinder-server`'
do_connect    'Connect'             connect true        bi-send ? ?  'Send the connection request'
#
loop_
_project.id
_project.label
_project.icon
_project.widget
_project.default  # None
_project.state
_project.help
proj_list            'Choose a Project Directory'    ?               select  ?                  required 'Create or choose one existing RELION Project'
proj_list::proj_new  'New...'                        bi-building-add option  RELION_NEW_PROJECT ?        ?
#
loop_
_project_new.id
_project_new.label
_project_new.widget
_project_new.default  # None
_project_new.arg0     # Filter
_project_new.arg1     # Placeholder
_project_new.arg2     # Node Type
_project_new.state
_project_new.help
current_dir   'Project Directory'  file       '?'   GrinderFolderAndCreate  ? ?  required 'RELION Project Directory. This is the root directory containing the `default_pipeline.star`.'
proj_name     'RELION Project'     string     '?'   ?       ? ?  ? ?
proj_apply    'Apply'              button     '?'   ?       ? ?  ? 'Create a RELION Project'
#
loop_
_project_summary.id
_project_summary.label
_project_summary.widget
_project_summary.default  # None
_project_summary.arg0     # Filter
_project_summary.arg1     # Placeholder
_project_summary.arg2     # Node Type
_project_summary.help
current_dir    'Project Directory'  string      ?   ? ?  ? 'RELION Project Directory. This is the root directory containing the `default_pipeline.star`.'
relion_project 'RELION Project'     string      ?   ? ?  ? ?
last_job       'Last Job'           paragraph   ?   ? ?  ? ?
proj_apply     'Apply'              button      ?   ? ?  ? 'Set or Create a RELION Project'
#
loop_
_software.id
_software.label
_software.widget
_software.default  # None
_software.arg0     # Status
_software.arg1     # Placeholder
_software.arg2     # Node Type
_software.help
softw_list    ?       table    ? ? ? ?  ?