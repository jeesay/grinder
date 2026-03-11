data_
#
loop_
_join_ptcls.id
_join_ptcls.label
_join_ptcls.icon
_join_ptcls.widget
_join_ptcls.value
_join_ptcls.help
io                   "I/O"                      bi-arrow-down-up    tab              ?        ?
settings             "Settings"                bi-tools             tab              ?        ?
log                  "Log"                     bi-binoculars-fill   tab              ?        ?
dataviz              "DataViz"                 bi-eye               tab              ?        ?
#
loop_
_io.id
_io.label
_io.icon
_io.widget
_io.value
_io.display
_io.help
indata               "Input Data"                             bi-box-arrow-in-down fieldset   ?          show       ?
outdata              "Output Data"                            bi-box-arrow-down    fieldset   ?          hidden     ?
nodes                "Nodes"                                  bi-controller        fieldset   ?          hidden     ?
system               "System"                                 bi-incognito         fieldset   ?          hiddden    ?
join_ptcls_cmd       "Check command"                          bi-chat-right-text   cli        ?          show       ?
#
loop_
_indata.id
_indata.label
_indata.widget
_indata.default
_indata.arg0
_indata.arg1
_indata.arg2
_indata.constraint
_indata.help
fn_part1             "Particle STAR file 1: "            file       ?               "ParticleGroupMetadata.star.relion" 1               "particle STAR file (*.star)" ?               "The first of the particle STAR files to be combined."
fn_part2             "Particle STAR file 2: "            file       ?               "ParticleGroupMetadata.star.relion" 1               "particle STAR file (*.star)" ?               "The second of the particle STAR files to be combined."
fn_part3             "Particle STAR file 3: "            file       ?               "ParticleGroupMetadata.star.relion" 1               "particle STAR file (*.star)" ?               
; The third of the particle STAR files to be combined.
Leave empty if there are only two files to be combined.
;
fn_part4             "Particle STAR file 4: "            file       ?               "ParticleGroupMetadata.star.relion" 1               "particle STAR file (*.star)" ?               
; The fourth of the particle STAR files to be combined.
Leave empty if there are only two or three files to be combined.
;
#
loop_
_outdata.id
_outdata.label
_outdata.widget
_outdata.default
_outdata.arg0
_outdata.arg1
_outdata.arg2
_outdata.constraint
_outdata.help
#
loop_
_nodes.id
_nodes.label
_nodes.widget
_nodes.default
_nodes.arg0
_nodes.arg1
_nodes.arg2
_nodes.constraint
_nodes.help
#
loop_
_system.id
_system.label
_system.widget
_system.default
_system.arg0
_system.arg1
_system.arg2
_system.constraint
_system.help
do_part              "Combine particle STAR files?"      bool       true            "?"             "?"             "?"             ?               ""
do_mic               "Combine micrograph STAR files?"    bool       false           "?"             "?"             "?"             ?               ""
do_mov               "Combine movie STAR files?"         bool       false           "?"             "?"             "?"             ?               ""
#
loop_
_join_ptcls_cmd.id
_join_ptcls_cmd.label
_join_ptcls_cmd.widget
_join_ptcls_cmd.default
_join_ptcls_cmd.arg0
_join_ptcls_cmd.arg1
_join_ptcls_cmd.arg2
_join_ptcls_cmd.constraint
_join_ptcls_cmd.help
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.display
_settings.help
#
loop_
_log.id
_log.label
_log.icon
_log.widget
_log.value
_log.display
_log.help
#
loop_
_dataviz.id
_dataviz.label
_dataviz.icon
_dataviz.widget
_dataviz.value
_dataviz.display
_dataviz.help
#
