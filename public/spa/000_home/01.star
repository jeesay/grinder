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
connect_fs            'Server Connection'    bi-wifi            fieldset ?      ? ?        ?
connected             'Server Parameters'    bi-wifi            fieldset ?      ? hidden   ?
project               'Projects'             bi-newspaper       fieldset ?      ? hidden   ?
projnew               'New Project'          bi-building-add    switch   False  ? hidden   ?
software              'Available Softwares'  bi-plugin          fieldset ?      ? hidden   ?
#
loop_
_connect_fs.id
_connect_fs.label
_connect_fs.widget
_connect_fs.default  # None
_connect_fs.arg0     # Status
_connect_fs.arg1     # Placeholder
_connect_fs.arg2     # Node Type
_connect_fs.help
ws_server_ip  'Server IP Address'   string          '127.0.0.1' ?       ? ?  'URL displayed by `grinder-server`'
ws_port       'Server Port'         string          8000        ?       ? ?  'Port displayed by `grinder-server`'
do_connect    'Connect'             button[connect] true        bi-send ? ?  'Send the connection request'
#
loop_
_project.id
_project.label
_project.icon
_project.widget
_project.default 
_project.state
_project.help
proj_list             'Project'       ?               select  ?                   required 'Create or choose one existing RELION Project'
proj_list::proj_none  '-- Choose --'  bi-building-add option  RELION_NONE         ?        ?
#
loop_
_projnew.id
_projnew.label
_projnew.widget
_projnew.default  # None
_projnew.arg0     # Filter
_projnew.arg1     # Placeholder
_projnew.arg2     # Node Type
_projnew.state
_projnew.help
current_dir   'Root Directory'  file                 './'              GrinderFolder  ? ?  required 'RELION Project Directory. This is the root directory containing the `default_pipeline.star`.'
proj_dir      'New Directory'   string               'my_project_dir'  ?              ? ?  ? ?
proj_name     'Project Name'    string               'my_project'      ?              ? ?  ? ?
proj_apply    'Apply'           button[newproject]   '?'               ?              ? ?  ? 'Create a RELION Project'
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