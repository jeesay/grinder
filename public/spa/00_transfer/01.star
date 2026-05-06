data_
#
#
loop_
_rln_proj_new.id
_rln_proj_new.label
_rln_proj_new.icon
_rln_proj_new.widget
projnew        "New..."      bi-building-down    tab
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