data_
#
loop_
_home.id
_home.label 
_home.icon
_home.widget 
_home.default
_home.parent
_home.help
home_main   "Home"   bi-house-door     tab   ?    ?
#
loop_
_home_main.id
_home_main.label 
_home_main.icon
_home_main.widget 
_home_main.default
_home_main.parent
_home_main.help
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