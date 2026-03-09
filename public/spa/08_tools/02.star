data_
#
loop_
_subselect_mic.id
_subselect_mic.label
_subselect_mic.icon
_subselect_mic.widget
_subselect_mic.value
_subselect_mic.help
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
subselect_mic_cmd    "Check command"                          bi-chat-right-text   cli        ?          show       ?
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
fn_mic               "OR select from micrographs.star:"  file       ?               "MicrographGroupMetadata.star.relion" 1               "STAR files (*.star)" required        "A micrographs.star file to select micrographs from."
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
#
loop_
_subselect_mic_cmd.id
_subselect_mic_cmd.label
_subselect_mic_cmd.widget
_subselect_mic_cmd.default
_subselect_mic_cmd.arg0
_subselect_mic_cmd.arg1
_subselect_mic_cmd.arg2
_subselect_mic_cmd.constraint
_subselect_mic_cmd.help
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.display
_settings.help
do_class_ranker      "Automatically select 2D classes?"       bi-chat-right-text   switch     ?          show       ?
general              "General"                                bi-chat-right-text   fieldset   ?          show       ?
do_regroup           "Regroup the particles?"                 bi-chat-right-text   switch     ?          show       ?
do_select_values     "Select based on metadata values?"       bi-chat-right-text   switch     ?          show       ?
do_discard           "OR: select on image statistics?"        bi-chat-right-text   switch     ?          show       ?
do_split             "OR: split into subsets?"                bi-chat-right-text   switch     ?          show       ?
do_remove_duplicates "OR: remove duplicates?"                 bi-chat-right-text   switch     ?          show       ?
do_filaments         "OR: select filaments by dendrogram?"    bi-chat-right-text   switch     ?          show       ?
#
loop_
_do_class_ranker.id
_do_class_ranker.label
_do_class_ranker.widget
_do_class_ranker.default
_do_class_ranker.arg0
_do_class_ranker.arg1
_do_class_ranker.arg2
_do_class_ranker.constraint
_do_class_ranker.help
rank_threshold       "Minimum threshold for auto-selection: " range      0.5             0               1               0.05            ?               
; Only classes with a pre dicted threshold above this value will be selected.
;
select_nr_parts      "Select at least this many particles: " range      -1              -1              10000           500             ?               
; Even if they have scores below the minimum threshold, select at least this many particles with the best scores.
;
select_nr_classes    "OR: select at least this many classes: " range      -1              -1              24              1               ?               
; Even if they have scores below the minimum threshold, select at least this many classes with the best scores.
;
#
loop_
_general.id
_general.label
_general.widget
_general.default
_general.arg0
_general.arg1
_general.arg2
_general.constraint
_general.help
do_recenter          "Re-center the class averages?"     bool       false           "?"             "?"             "?"             ?               
; This option is only used when selecting particles from 2D classes.
The selected class averages will all re-centered on their center-of-mass.
This is useful when you plane to use these class averages as templates for auto-picking.
;
#
loop_
_do_regroup.id
_do_regroup.label
_do_regroup.widget
_do_regroup.default
_do_regroup.arg0
_do_regroup.arg1
_do_regroup.arg2
_do_regroup.constraint
_do_regroup.help
nr_groups            "Approximate nr of groups: "        range      1               50              20              1               ?               
; It is normal that the actual number of groups may deviate a little from this number.

;
#
loop_
_do_select_values.id
_do_select_values.label
_do_select_values.widget
_do_select_values.default
_do_select_values.arg0
_do_select_values.arg1
_do_select_values.arg2
_do_select_values.constraint
_do_select_values.help
select_label         "Metadata label for subset selection:" string     rlnCtfMaxResolution "?"             "?"             "?"             ?               
; This column from the input STAR file will be used for the subset selection.
;
select_minval        "Minimum metadata value:"           string     -9999.          "?"             "?"             "?"             ?               
; Only lines in the input STAR file with the corresponding metadata value larger than or equal to this value will be included in the subset.
;
select_maxval        "Maximum metadata value:"           string     9999.           "?"             "?"             "?"             ?               
; Only lines in the input STAR file with the corresponding metadata value smaller than or equal to this value will be included in the subset.
;
#
loop_
_do_discard.id
_do_discard.label
_do_discard.widget
_do_discard.default
_do_discard.arg0
_do_discard.arg1
_do_discard.arg2
_do_discard.constraint
_do_discard.help
discard_label        "Metadata label for images:"        string     rlnImageName    "?"             "?"             "?"             ?               
; Specify which column from the input STAR contains the names of the images to be used to calculate the average and stddev values.
;
discard_sigma        "Sigma-value for discarding images:" range      4               1               10              0.1             ?               
; Images with average and/or stddev values that are more than this many times the ensemble stddev away from the ensemble mean will be discarded.
;
#
loop_
_do_split.id
_do_split.label
_do_split.widget
_do_split.default
_do_split.arg0
_do_split.arg1
_do_split.arg2
_do_split.constraint
_do_split.help
do_random            "Randomise order before making subsets?:" bool       false           "?"             "?"             "?"             ?               
; If set to Yes, the input STAR file order will be randomised.
If set to No, the original order in the input STAR file will be maintained.
;
split_size           "Subset size: "                     range      100             100             10000           100             ?               
; The number of lines in each of the output subsets.
When this is -1, items are divided into a number of subsets specified in the next option.
;
nr_split             "OR: number of subsets: "           range      -1              1               50              1               ?               
; Give a positive integer to specify into how many equal-sized subsets the data will be divided.
When the subset size is also specified, only this number of subsets, each with the specified size, will be written, possibly missing some items.
When this is -1, all items are used, generating as many subsets as necessary.
;
#
loop_
_do_remove_duplicates.id
_do_remove_duplicates.label
_do_remove_duplicates.widget
_do_remove_duplicates.default
_do_remove_duplicates.arg0
_do_remove_duplicates.arg1
_do_remove_duplicates.arg2
_do_remove_duplicates.constraint
_do_remove_duplicates.help
duplicate_threshold  "Minimum inter-particle distance (A)" range      30              0               1000            1               ?               "Particles within this distance are removed leaving only one."
image_angpix         "Pixel size before extraction (A)"  range      -1              -1              10              0.01            ?               
; The pixel size of particles (relevant to rlnOriginX/Y) is read from the STAR file.
When the pixel size of the original micrograph used for auto-picking and extraction (relevant to rlnCoordinateX/Y) is different, specify it here.
In other words, this is the pixel size after binning during motion correction, but before down-sampling during extraction.
;
#
loop_
_do_filaments.id
_do_filaments.label
_do_filaments.widget
_do_filaments.default
_do_filaments.arg0
_do_filaments.arg1
_do_filaments.arg2
_do_filaments.constraint
_do_filaments.help
dendrogram_threshold "Dendrogram threshold: "            range      0.85            0               1               0.05            ?               
; Lower thresholds will produce more clusters; After the dendrogram has been calculated in the initial running of this job, subsequent continuation jobs can quickly test other threshold values.
The output logfile.pdf can be visualised to follow therh.PROCess until a good threshold has been achieved.
;
dendrogram_minclass  "Minimum class size: "              range      -1000           -1000           50000           1000            ?               
; If set to a positive value, then particle star files with clusters that have at least this number of particles will be written out.
Keep th default negative value for faster testing of the threshold.
;
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
