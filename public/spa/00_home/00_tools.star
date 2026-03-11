data_
#
_id       home_main
_label    Home
_icon     bi-house-door
_index    1
_parent   home
#
loop_
_home_main.id
_home_main.label
_home_main.icon
_home_main.widget
_home_main.default
_home_main.help
tool_menu      'Home'   bi-house-door toolmenu  ? ?
#
loop_
_tool_menu.id
_tool_menu.label 
_tool_menu.icon
_tool_menu.widget 
_tool_menu.default
_tool_menu.parent
_tool_menu.help
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
_connect.toolsetid
_connect.help
ws_server_ip  'Server IP Address'   string  '127.0.0.1' ?       ? ? home_dummy 'URL displayed by `grinder-server`'
ws_port       'Server Port'         string  8000        ?       ? ? home_dummy 'Port displayed by `grinder-server`'
do_connect    'Connect'             connect true        bi-send ? ? home_dummy 'Send the connection request'
#
loop_
_project.id
_project.label
_project.widget
_project.default  # None
_project.arg0     # Status
_project.arg1     # Placeholder
_project.arg2     # Node Type
_project.toolsetid
_project.help
current_dir    'Project Directory'  paragraph  '?'     ?       ? ? home_dummy 'URL displayed by `grinder-server`'
relion_project 'RELION Project'     paragraph  '?'     ?       ? ? home_dummy  ?
last_job       'Last Job'           paragraph  '?'     ?       ? ? home_dummy  ?
#
loop_
_software.id
_software.label
_software.widget
_software.default  # None
_software.arg0     # Status
_software.arg1     # Placeholder
_software.arg2     # Node Type
_software.toolsetid
_software.help
softw_list    ?       table    ? ? ? ? home_dummy ?