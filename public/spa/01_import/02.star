data_
#
loop_
_tabs.id
_tabs.label
_tabs.icon
_tabs.widget
_tabs.default
_tabs.parent
_tabs.help
io       'I/O'                    bi-arrow-down-up       tab ? ? ?
settings 'Settings'               bi-tools               tab ? ? ?
log      'Logs'                   bi-binoculars-fill     tab ? ? ?
result   'DataViz'                bi-eye                 tab ? ? ?
#
loop_
_io.id
_io.label
_io.icon
_io.widget
_io.default
_io.help
indata   'Input'       bi-arrow-bar-down      fieldset ?      'No Help' 
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.default
_settings.help
general  'General'      bi-chat-right-text     fieldset ?      'No Help'
##
loop_
_indata.id
_indata.label
_indata.widget
_indata.default
_indata.arg0
_indata.arg1
_indata.arg2
_indata.help
do_other   "Import other node types?"    bool    false    ?    ?    ?    "Set this to Yes if you plan to import anything else than movies or micrographs"
fn_in_other   "Input file:"    file    ref.mrc    "Input file (*.*)"    .    ?
;
Select any file(s) to import. 
 
 Note that for importing coordinate files, one has to give a Linux wildcard, where the *-symbol is before the coordinate-file suffix, e.g. if the micrographs are called mic1.mrc and the coordinate files mic1.box or mic1_autopick.star, one HAS to give '*.box' or '*_autopick.star', respectively.
 
 Also note that micrographs, movies and coordinate files all need to be in the same directory (with the same rootnames, e.g.mic1 in the example above) in order to be imported correctly. 3D masks or references can be imported from anywhere. 
 
 Note that movie-particle STAR files cannot be imported from a previous version of RELION, as the way movies are handled has changed in RELION-2.0. 
 
 For the import of a particle, 2D references or micrograph STAR file or of a 3D reference or mask, only a single file can be imported at a time. 
 
 Note that due to a bug in a fltk library, you cannot import from directories that contain a substring  of the current directory, e.g. dont important from /home/betagal if your current directory is called /home/betagal_r2. In this case, just change one of the directory names.
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
_general.help
node_type   "Node type:"    select    0    "('Particle coordinates (*.box, *_pick.star)', 'LABEL_IMPORT_COORDS')"    ?    ?    "Select the type of Node this is."
optics_group_particles   "Rename optics group for particles:"    string    ""    ?    ?    ?
;
Only for the import of a particles STAR file with a single, or no, optics groups defined: rename the optics group for the imported particles to this string.
;
#
loop_
_node_type.id
_node_type.label
_node_type.widget
_node_type.default
_node_type.arg0
_node_type.arg1
_node_type.arg2
_node_type.help
node_type_opt_00   "('Particle coordinates (*.box, *_pick.star)', 'LABEL_IMPORT_COORDS')"    option    0    ?    ?    ?    "?"
node_type_opt_01   "('Particles STAR file (.star)', 'LABEL_IMPORT_PARTS')"    option    1    ?    ?    ?    "?"
