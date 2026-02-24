data_
#
loop_
_import_mov.id
_import_mov.label
_import_mov.icon
_import_mov.widget
_import_mov.default
_import_mov.parent
_import_mov.help
io       'I/O'                    bi-arrow-down-up       tab ? ? 'No Help'
settings 'Settings'               bi-tools               tab ? ? 'No Help'
#
loop_
_io.id
_io.label
_io.icon
_io.widget
_io.default
_io.help
indata   'Input'       bi-arrow-bar-down      fieldset ?   'No Help'
outdata   'Output'     bi-box-arrow-down      fieldset ?   'No help'
command   'Script'     bi-regex               fieldset ?   'No help'
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.default
_settings.help
general  'General'      bi-chat-right-text     fieldset ?      'No Help'
#
loop_
_indata.id
_indata.label
_indata.widget
_indata.default
_indata.arg0
_indata.arg1
_indata.arg2
_indata.help
do_raw   "Import raw movies/micrographs?"    bool    true    ?    ?    ?    "Set this to Yes if you plan to import raw movies or micrographs"
fn_in_raw   "Raw input files:"    file    Micrographs/*.tif    "Movie or Image (*.{mrc,mrcs,tif,tiff,eer,mrc.bz2,mrcs.bz2,mrc.zst,mrcs.zst,mrc.xz,mrcs.xz})"    .    ?
;
Provide a Linux wildcard that selects all raw movies or micrographs to be imported. The path must be a relative path from the project directory. To import files outside the project directory, first make a symbolic link by an absolute path and then specify the link by a relative path. See the FAQ page on RELION wiki (https://www3.mrc-lmb.cam.ac.uk/relion/index.php/FAQs#What_is_the_right_way_to_import_files_outside_the_project_directory.3F) for details.Torh.PROCess compressed MRC movies, you need pbzip2, zstd and xz command in your PATH for bzip2, Zstandard and xzip compression, respectively.
;
is_multiframe   "Are these multi-frame movies?"    bool    true    ?    ?    ?    "Set to Yes for multi-frame movies, set to No for single-frame micrographs."
#
loop_
_outdata.id
_outdata.label
_outdata.widget
_outdata.default  # None
_outdata.arg0     # Status
_outdata.arg1     # Placeholder
_outdata.arg2     # Node Type
_outdata.help
n_img   "Output directory:"    string_ro    LABEL_PARTS_CPIPE    "STAR files (*.star)"    1    ?    "No Help"
#
loop_
_command.index
_command.type
_command.arg
_command.flag
_command.boolean
_command.assertion
1  prog    'FN_IN={fn_in_raw}{pattern_in}'                    ?                    ?                    ?
2  prog    relion_import                                      None                 None                 None
2  flag    '--do_movies'                                      is_multiframe        True                 ?
2  flag    '--do_micrographs'                                 is_multiframe        False                ?
2  param   '--optics_group_name {optics_group_name}'          ?                    ?                    is_field_not_empty            
2  flag    '--optics_group_mtf'                               ne,{fn_mtf},null     True                 ? 
2  param   '--angpix {angpix}'                                ?                    ?                    ?                             
2  param   '--kV {kV}'                                        ?                    ?                    ?                             
2  param   '--Cs {Cs}'                                        ?                    ?                    ?                             
2  param   '--Q0 {Q0}'                                        ?                    ?                    ?                             
2  param   '--beamtilt_x {beamtilt_x}'                        ?                    ?                    ?                             
2  param   '--beamtilt_y {beamtilt_y}'                        ?                    ?                    ?                             
2  param   ' --i $FN_IN'                                      ?                    ?                    ?                             
2  param   ' --odir Import/{RELION_NEW_JOB}'                  ?                    ?                    ?                             
2  param   ' --ofile  {fn_out}'                               ?                    ?                    ?                             
2  param   ' --pipeline-control Import/{RELION_NEW_JOB}'      ?                    ?                    ?          
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
optics_group_name   "Optics group name:"    string    opticsGroup1    ?    ?    ?
;
Name of this optics group. Each group of movies/micrographs with different optics characteristics for CTF refinement should have a unique name.
;
fn_mtf   "MTF of the detector:"    string    ?    "STAR Files (*.star)"    .    ?
;
As of release-3.1, the MTF of the detector is used in the refinement stages of refinement.  If you know the MTF of your detector, provide it here. Curves for some well-known detectors may be downloaded from the RELION Wiki. Also see there for the exact format 
 If you do not know the MTF of your detector and do not want to measure it, then by leaving this entry empty, you include the MTF of your detector in your overall estimated B-factor upon sharpening the map.Although that is probably slightly less accurate, the overall quality of your map will probably not suffer very much. 
 
 Note that when combining data from different detectors, the differences between their MTFs can no longer be absorbed in a single B-factor, and providing the MTF here is important!
;
angpix   "Pixel size (Angstrom):"    range    1.4    0.5    3    0.1    "Pixel size in Angstroms. "
kV   "Voltage (kV):"    range    300    50    500    10    "Voltage the microscope was operated on (in kV)"
Cs   "Spherical aberration (mm):"    range    2.7    0    8    0.1
;
Spherical aberration of the microscope used to collect these images (in mm). Typical values are 2.7 (FEI Titan & Talos, most JEOL CRYO-ARM), 2.0 (FEI Polara), 1.4 (some JEOL CRYO-ARM) and 0.01 (microscopes with a Cs corrector).
;
Q0   "Amplitude contrast:"    range    0.1    0    0.3    0.01
;
Fraction of amplitude contrast. Often values around 10% work better than theoretically more accurate lower values...
;
beamtilt_x   "Beamtilt in X (mrad):"    range    0.0    -1.0    1.0    0.1    "Known beamtilt in the X-direction (in mrad). Set to zero if unknown."
beamtilt_y   "Beamtilt in Y (mrad):"    range    0.0    -1.0    1.0    0.1    "Known beamtilt in the Y-direction (in mrad). Set to zero if unknown."
