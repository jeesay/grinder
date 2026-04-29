data_
#
loop_
_import_mov.id
_import_mov.label
_import_mov.icon
_import_mov.widget
_import_mov.value
_import_mov.help
io                   "I/O"                     bi-arrow-down-up     tab              ?        ?
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
_io.state
_io.help
indata               "Input Data"              bi-box-arrow-in-down fieldset   ?          show       ?
outdata              "Output Data"             bi-box-arrow-down    fieldset   ?          hidden     ?
nodes                "Nodes"                   bi-controller        fieldset   ?          hidden     ?
system               "System"                  bi-incognito         fieldset   ?          hiddden    ?
import_mov_cmd       "Check command"           bi-chat-right-text   cli        ?          show       ?
#
loop_
_indata.id
_indata.label
_indata.widget
_indata.default
_indata.arg0
_indata.arg1
_indata.arg2
_indata.state
_indata.help
fn_in_raw         "Raw input files:"       file       Movies/*.tif "Movie or Image (*.{mrc,mrcs,tif,tiff,eer,mrc.bz2,mrcs.bz2,mrc.zst,mrcs.zst,mrc.xz,mrcs.xz})" "."             "?"             required        
; Provide a Linux wildcard that selects all raw movies or micrographs to be imported.
The path must be a relative path from the project directory.
To import files outside the project directory, first make a symbolic link by an absolute path and then specify the link by a relative path.
See the FAQ page on RELION wiki (https://www3.mrc-lmb.cam.ac.uk/relion/index.php/FAQs#What_is_the_right_way_to_import_files_outside_the_project_directory.3F) for details.Torh.PROCess compressed MRC movies, you need pbzip2, zstd and xz command in your PATH for bzip2, Zstandard and xzip compression, respectively.
;
#
loop_
_outdata.id
_outdata.label
_outdata.widget
_outdata.default
_outdata.state
_outdata.help
outfile           ?  string_ro   movies.star                              hidden "Only for RELION"
nod               ?  string_ro   MicrographMovieGroupMetadata.star.relion hidden "Only for GRINDER"
#
loop_
_nodes.id
_nodes.label
_nodes.widget
_nodes.default
_nodes.arg0
_nodes.arg1
_nodes.arg2
_nodes.state
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
_system.state
_system.help
do_raw               "Import raw movies/micrographs?"    bool       true            "?"             "?"             "?"             ?               
; Set this to Yes if you plan to import raw movies or micrographs
;
do_other             "Import other node types?"          bool       false           "?"             "?"             "?"             ?               
; Set this to Yes if you plan to import anything else than movies or micrographs
;
is_multiframe        "Are these multi-frame movies?"     bool       true            "?"             "?"             "?"             ?               
; Set to Yes for multi-frame movies, set to No for single-frame micrographs.
;
#
loop_
_import_mov_cmd.type
_import_mov_cmd.arg
_import_mov_cmd.param_id
prog    "grinder import"         ?
param   --type                   nod     
param   --i                      fn_in_raw       
param   --odir                   Import/${RELION_NEW_JOB}/ 
param   --ofile                  outfile
param   --optics_group_mtf       fn_mtf
param   --optics_group_name      optics_group_name
param   --angpix                 angpix
param   --kV                     kV
param   --Cs                     Cs
param   --Q0                     Q0
param   --beamtilt_x             beamtilt_x
param   --beamtilt_y             beamtilt_y
param   --pipeline-control       Import/${RELION_NEW_JOB}/ 
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.display
_settings.help
optics_group         "Optics Group"                           bi-eye               fieldset   ?          show       ?
#
loop_
_optics_group.id
_optics_group.label
_optics_group.widget
_optics_group.default
_optics_group.arg0
_optics_group.arg1
_optics_group.arg2
_optics_group.state
_optics_group.help
optics_group_name    "Optics group name:"                string     opticsGroup1    "?"             "?"             "?"             ?               
; Name of this optics group.
Each group of movies/micrographs with different optics characteristics for CTF refinement should have a unique name.
;
fn_mtf               "MTF of the detector:"              file       ?               "STAR Files (*.star)" "."             "?"             ?               
; As of release-3.1, the MTF of the detector is used in the refinement stages of refinement.
 If you know the MTF of your detector, provide it here.
Curves for some well-known detectors may be downloaded from the RELION Wiki.
Also see there for the exact format 
 If you do not know the MTF of your detector and do not want to measure it, then by leaving this entry empty, you include the MTF of your detector in your overall estimated B-factor upon sharpening the map.Although that is probably slightly less accurate, the overall quality of your map will probably not suffer very much.

 
 Note that when combining data from different detectors, the differences between their MTFs can no longer be absorbed in a single B-factor, and providing the MTF here is important!
;
angpix               "Pixel size (Angstrom):"            range      1.4             0.5             3               0.1             ?               "Pixel size in Angstroms. "
kV                   "Voltage (kV):"                     range      300              50           500                10     ?   "Voltage the microscope was operated on (in kV)"
Cs                   "Spherical aberration (mm):"        range      2.7               0             8               0.1     ?
; Spherical aberration of the microscope used to collect these images (in mm). Typical values are 2.7 (FEI Titan & Talos, most JEOL CRYO-ARM), 
2.0 (FEI Polara), 1.4 (some JEOL CRYO-ARM) and 0.01 (microscopes with a Cs corrector).
;
Q0                   "Amplitude contrast:"               range      0.1               0           0.3              0.01     ?
; Fraction of amplitude contrast. Often values around 10% work better than theoretically more accurate lower values...
;
beamtilt_x           "Beamtilt in X (mrad):"             range      0.0             -1.0            1.0             0.1             ?               
; Known beamtilt in the X-direction (in mrad).
Set to zero if unknown.
;
beamtilt_y           "Beamtilt in Y (mrad):"             range      0.0             -1.0            1.0             0.1             ?               
; Known beamtilt in the Y-direction (in mrad).
Set to zero if unknown.
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
