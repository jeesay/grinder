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
connect               'Server Connection'    bi-wifi            fieldset ?                  ? ?        ?
project               'Projects'             bi-newspaper       fieldset ?                  ? hidden   ?
proj_select           'Project Selection'    bi-building        g_select ?                  ? ?        ?
proj_select::projnew  'New Project'          bi-building-add    g_option RELION_NEW_PROJECT ? hidden   ?
software              'Available Softwares'  bi-plugin          fieldset ? ? hidden   ?
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
_project.default 
_project.state
_project.help
proj_list>proj_select 'Project'       ?               select  ?                   required 'Create or choose one existing RELION Project'
proj_list::proj_none  '-- Choose --'  bi-building-add option  RELION_NONE         ?        ?
proj_list::proj_new   'New...'        bi-building-add option  RELION_NEW_PROJECT  ?        ?
#
loop_
_projnew.id
_projnew.label
_projnew.icon
_projnew.widget
_projnew.default  # None
_projnew.state
_projnew.help
pnew   'New Project'    bi-building-add    fieldset RELION_NEW_PROJECT ? ?   'Create a new RELION Project'
#
loop_
_pnew.id
_pnew.label
_pnew.widget
_pnew.default  # None
_pnew.arg0     # Filter
_pnew.arg1     # Placeholder
_pnew.arg2     # Node Type
_pnew.state
_pnew.help
current_dir   'Root Directory'  file     './'          GrinderFolder  ? ?  required 'RELION Project Directory. This is the root directory containing the `default_pipeline.star`.'
proj_name     'New Directory'   string   'my_project'  ?              ? ?  ? ?
proj_apply    'Apply'           button   '?'           ?              ? ?  ? 'Create a RELION Project'
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