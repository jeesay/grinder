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
_home_dash.help
connect    'Server Connection'    bi-wifi            fieldset ? ? ?
project    'Project Summary'      bi-clipboard-data  fieldset ? ? ?
software   'Available Softwares'  bi-plugin          fieldset ? ? ?
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
_project.widget
_project.default  # None
_project.arg0     # Status
_project.arg1     # Placeholder
_project.arg2     # Node Type
_project.help
current_dir    'Project Directory'  paragraph  '?'     ?       ? ?  'URL displayed by `grinder-server`'
relion_project 'RELION Project'     paragraph  '?'     ?       ? ?   ?
last_job       'Last Job'           paragraph  '?'     ?       ? ?   ?
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