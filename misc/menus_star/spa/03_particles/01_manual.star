data_manual_lowpass
#
_toolbox.id manual_lowpass
_toolbox.label 'Manual Picking with Low-pass filtering'
_toolbox.icon none
#
_main.id           relion.xxx.yyy
_main.hidden_name '.gui_zzz'
#
_main.label        'todo' 
_main.help         'None'
#
loop_
_tabs.id
_tabs.label
_tabs.icon
io 'I/O' bi-arrow-down-up 
settings 'Settings' bi-tools
running 'Running' bi-send
#
loop_
_fieldsets.tab_id
_fieldsets.id
_fieldsets.icon
_fieldsets.label
_fieldsets.widget
_fieldsets.default
_fieldsets.help
? ? ? ? ? ? ?
#
# Command options
#
loop_
_params.fieldset_id
_params.id
_params.label
_params.widget
_params.params
_params.help
? ? ? ? ?
#
_command.prog_mpi 'which relion_run_xxx_mpi' 
_command.prog     'which relion_run_xxx'
#
loop_
_cli.type
_cli.content
_cli.flag
_cli.bool
? ? ? ?

