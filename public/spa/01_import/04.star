data_
#
loop_
_grr_import_mov.id
_grr_import_mov.label
_grr_import_mov.icon
_grr_import_mov.widget
_grr_import_mov.value
_grr_import_mov.help
io                   "I/O"                     bi-arrow-down-up     tab              ?        ?
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
indata           "Data Type"      bi-box-arrow-in-down fieldset   ?  show       ?
datatypes        "Group"          ?                    group_x    ?  ?          ?
outdata          "Output Data"    bi-box-arrow-down    fieldset   ?  hidden     ?
nodes            "Nodes"          bi-controller        fieldset   ?  hidden     ?
system           "System"         bi-incognito         fieldset   ?  hiddden    ?
import_mov_cmd   "Check command"  bi-chat-right-text   cli        ?  show       ?
#
loop_
_indata.id
_indata.label
_indata.icon
_indata.widget
_indata.default
_indata.action
_indata.help
node_type                 'Choose Data Type'   ?                 select  ?  ? ?
node_type::dtype_movies   'Movies'             bi-film           option "MicrographMovieGroupMetadata.star.relion" moviedata.show ?
node_type::dtype_mics     'Micrographs'        bi-images         option "MicrographGroupMetadata.star.relion"      micdata.show ?
node_type::dtype_coords   'Coordinates'        bi-dice-5         option "MicrographCoordsGroup.star.relion"        coordsdata.show ?
node_type::dtype_parts    'Particles (*.star)' bi-star           option "ParticleGroupMetadata.star.relion"        partsdata.show ?
node_type::dtype_2dimg    '2D/3D References'   bi-transparency   option "Image2DGroupMetadata.star.relion"         img2ddata.show ?
node_type::dtype_map      'Density Map'        bi-box            option "DensityMap.mrc"                           mapdata.show ?
node_type::dtype_mask     'Mask'               bi-mask           option "Mask3D.mrc"                               maskdata.show ?
node_type::dtype_halfmap  'Half-map(s)'        bi-building-add   option "DensityMap.mrc.halfmap"                   halfmapdata.show ?
#
loop_
_datatypes.id
_datatypes.widget
_datatypes.state
moviedata       group   hidden
micdata         group   hidden
coordsdata      group   hidden
partsdata       group   hidden
img2ddata       group   hidden
mapdata         group   hidden
maskdata        group   hidden
halfmapdata     group   hidden
#
loop_
_moviedata.id
_moviedata.label
_moviedata.widget
_moviedata.help
mov_indata       ? fieldset ?
mov_opticsgroup ? fieldset ?
#
loop_
_mov_indata.id
_mov_indata.label
_mov_indata.widget
_mov_indata.default  # None
_mov_indata.arg0     # Filter
_mov_indata.arg1     # Placeholder
_mov_indata.arg2     # Node Type
_mov_indata.state
_mov_indata.help
fn_in_raw            "Raw input files:"                  file       Micrographs/*.tif "Movie or Image (*.{mrc,mrcs,tif,tiff,eer,mrc.bz2,mrcs.bz2,mrc.zst,mrcs.zst,mrc.xz,mrcs.xz})" "."             "?"             required        
; Provide a Linux wildcard that selects all raw movies or micrographs to be imported.
The path must be a relative path from the project directory.
To import files outside the project directory, first make a symbolic link by an absolute path and then specify the link by a relative path.
See the FAQ page on RELION wiki (https://www3.mrc-lmb.cam.ac.uk/relion/index.php/FAQs#What_is_the_right_way_to_import_files_outside_the_project_directory.3F) for details.Torh.PROCess compressed MRC movies, you need pbzip2, zstd and xz command in your PATH for bzip2, Zstandard and xzip compression, respectively.
;
#
loop_
_mov_opticsgroup.id
_mov_opticsgroup.label
_mov_opticsgroup.widget
_mov_opticsgroup.default
_mov_opticsgroup.arg0
_mov_opticsgroup.arg1
_mov_opticsgroup.arg2
_mov_opticsgroup.state
_mov_opticsgroup.help
optics_group_name    "Optics group name:"                string     opticsGroup1    "?"             "?"             "?"     required               
; Name of this optics group.
Each group of movies/micrographs with different optics characteristics for CTF refinement should have a unique name.
;
fn_mtf               "MTF of the detector:"              file       ?               "STAR Files (*.star)" "."             "?"             ?               
; As of release-3.1, the MTF of the detector is used in the refinement stages of refinement.If you know the MTF of your detector, provide it here.
Curves for some well-known detectors may be downloaded from the RELION Wiki. Also see there for the exact format 
If you do not know the MTF of your detector and do not want to measure it, then by leaving this entry empty, you include the MTF of your detector 
in your overall estimated B-factor upon sharpening the map. Although that is probably slightly less accurate, the overall quality of your map will 
probably not suffer very much.

Note that when combining data from different detectors, the differences between their MTFs can no longer be absorbed in a single B-factor, and 
providing the MTF here is important!
;
angpix               "Pixel size (Angstrom):"            range      1.4             0.5             3               0.1     ?   "Pixel size in Angstroms. "
beamtilt_x           "Beamtilt in X (mrad):"             range      0.0             -1.0            1.0             0.1     ?               
; Known beamtilt in the X-direction (in mrad).Set to zero if unknown.
;
beamtilt_y           "Beamtilt in Y (mrad):"             range      0.0             -1.0            1.0             0.1      ?               
; Known beamtilt in the Y-direction (in mrad). Set to zero if unknown.
;
#