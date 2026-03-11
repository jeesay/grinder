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
