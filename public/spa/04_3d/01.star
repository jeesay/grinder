data_
#
_id       refine3d
_label    'Refine3D'
_widget    radio
_parent   refine
_help     ''
_comment  'use_gctf'
_proc_id  0
_labelnew     "relion.refine3d.zzz"                      # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
#
loop_
_tabs.id
_tabs.label
_tabs.icon
_tabs.widget
_tabs.default
_tabs.help
settings 'Settings'               bi-nut                 tab ? 'No help'
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.default
_settings.help
general  'General'                bi-chat-right-text     fieldset ? 'No help'
#
#
# Command Options
#
loop_
_general.id
_general.label
_general.widget
_general.default
_general.arg0
_general.arg1
_general.arg2
_general.help
sampling   "Initial angular sampling:"    select    "7.5 degrees"    ?    ?    ?
;
There are only a few discrete angular samplings possible because we use the HealPix library to generate the sampling of the 
first two Euler angles on the sphere. The samplings are approximate numbers and vary slightly over the sphere.

Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.
;
#
#
loop_
_sampling.id
_sampling.label
_sampling.widget
_sampling.default
_sampling.arg0
_sampling.arg1
_sampling.arg2
_sampling.help
auto_local_sampling_opt_00  "30 degrees"    option    0    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_01  "15 degrees"    option    1    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_02  "7.5 degrees"    option    2    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_03  "3.7 degrees"    option    3    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_04  "1.8 degrees"    option    4    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_05  "0.9 degrees"    option    5    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_06  "0.5 degrees"    option    6    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_07  "0.2 degrees"    option    7    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_08  "0.1 degrees"    option    8    auto_local_sampling    ?    ?   ?
