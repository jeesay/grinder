data_
#
loop_
_test.id
_test.label
_test.icon
_test.widget
_test.value
_test.help
io                   "I/O"                   bi-arrow-down-up     tab        ?        ?
log                  "Log"                   bi-binoculars-fill   tab        ?        ?
#
loop_
_io.id
_io.label
_io.icon
_io.widget
_io.value
_io.display
_io.help
general              "Parameters"             bi-chat-right-text   fieldset   ?        show     ?
nodes                "Nodes"                  bi-controller        fieldset   ?        show     ?
test_cmd             "Check command"          bi-chat-right-text   cli        ?        show     ?
#
loop_
_nodes.id
_nodes.nodetype
_nodes.widget
_nodes.filename
_nodes.filetype
JOB_OUTDIR  outdir node  External/${NEW_JOB}   Directory.output.relion                           
outfile     output node 'files.star'           ParamsData.star.grinder.test
#
loop_
_general.id
_general.label
_general.widget
_general.default
_general.arg0
_general.arg1
_general.arg2
_general.state
_general.help 
time             "Computation Time:"       range      10               2  60 1  no_bounds  "The number of seconds the program is sleeping to mimick computation time"
message          "Message:"                string     "Hello World!"   ?  ?  ?  ?          "Define a message displayed in the log and stored in the results CSV file."
reverse          "Reverse:"                bool       false            ?  ?  ?  ?          "Display the message from right to left"
case             "Modify Case:"            select     ?                ?  ?  ?  ?          "Display the message in a case mode. This param is applied after the `reverse` parameter"
case::none       "No"                      option     unchanged        ?  ?  ?  ?          ?
case::lower      "Lowercase"               option     lower            ?  ?  ?  ?          ?
case::upper      "Uppercase"               option     upper            ?  ?  ?  ?          ?
case::capitalize "Capitalize"              option     cap              ?  ?  ?  ?          ?
repeat           "Repeat:"                 int        10               ?  ?  ?  ?          "Define a number N of iterations creating N files named file<index>.csv containing the message"
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
_test_cmd.type
_test_cmd.arg
_test_cmd.param_id
prog    "grinder test"       ?      
param   --time               time
param   --message            message
param   --repeat             repeat
flag    --rev                reverse     
param   --case               case     
param   --odir               JOB_OUTDIR                
param   --ofile              outfile
#

