data_
#
loop_
_grr_import_all.id
_grr_import_all.label
_grr_import_all.icon
_grr_import_all.widget
_grr_import_all.value
_grr_import_all.help
io                   "I/O"                     bi-arrow-down-up     tab              ?        ?
log                  "Log"                     bi-binoculars-fill   tab              ?        ?
dataviz              "DataViz"                 bi-columns-gap       tab              ?        ?
#
loop_
_io.id
_io.label
_io.icon
_io.widget
_io.default
_io.state
_io.help
indata               "Data Type"      bi-box-arrow-in-down fieldset  ?                                           show    ?
dtype                "Fielset Group"  bi-incognito         select_g  ?                                           ?       ?
dtype::moviedata     ?                ?                    option_g  "MicrographMovieGroupMetadata.star.relion"  hidden  ?
dtype::micdata       ?                ?                    option_g  "MicrographGroupMetadata.star.relion"       hidden  ?
dtype::coordsdata    ?                ?                    option_g  "MicrographCoordsGroup.star.relion"         hidden  ?
dtype::partsdata     ?                ?                    option_g  "ParticleGroupMetadata.star.relion"         hidden  ?
dtype::img2ddata     ?                ?                    option_g  "Image2DGroupMetadata.star.relion"          hidden  ? 
dtype::mapdata       ?                ?                    option_g  "DensityMap.mrc"                            hidden  ?
dtype::maskdata      ?                ?                    option_g  "Mask3D.mrc"                                hidden  ?
dtype::halfmapdata   ?                ?                    option_g  "DensityMap.mrc.halfmap"                    hidden  ?
outdata              "Output Data"    bi-box-arrow-down    fieldset  ?                                           hidden  ?
nodes                "Nodes"          bi-controller        fieldset  ?                                           hidden  ?
system               "System"         bi-incognito         fieldset  ?                                           hiddden ?
import_all_cmd       "Check command"  bi-chat-right-text   cli       ?                                           show    ?
#
loop_
_indata.id
_indata.label
_indata.icon
_indata.widget
_indata.default
_indata.help
nod>dtype          'Choose Data Type'   ?                 select ?                                          ?
nod::dtyp_choose   'Choose a file type' bi-file           option "Choose_File_Type"                         ?
nod::dtyp_movies   'Movies'             bi-film           option "MicrographMovieGroupMetadata.star.relion" ?
nod::dtyp_mics     'Micrographs'        bi-images         option "MicrographGroupMetadata.star.relion"      ?
nod::dtyp_coords   'Coordinates'        bi-dice-5         option "MicrographCoordsGroup.star.relion"        ?
nod::dtyp_parts    'Particles (*.star)' bi-star           option "ParticleGroupMetadata.star.relion"        ?
nod::dtyp_2dimg    '2D/3D References'   bi-transparency   option "Image2DGroupMetadata.star.relion"         ?
nod::dtyp_map      'Density Map'        bi-box            option "DensityMap.mrc"                           ?
nod::dtyp_mask     'Mask'               bi-mask           option "Mask3D.mrc"                               ?
nod::dtyp_halfmap  'Half-map(s)'        bi-building-add   option "DensityMap.mrc.halfmap"                   ?
#
loop_
_moviedata.id
_moviedata.label
_moviedata.icon
_moviedata.widget
_moviedata.default
_moviedata.help
mov_indata      "Movies"       bi-box-arrow-in-down fieldset "MicrographMovieGroupMetadata.star.relion" "Import Movies"
mov_opticsgroup "Optics Group" bi-eyeglasses        fieldset "MicrographMovieGroupMetadata.star.relion" ?
#
loop_
_micdata.id
_micdata.label
_micdata.icon
_micdata.widget
_micdata.default
_micdata.help
mic_indata      "Micrographs"  bi-box-arrow-in-down fieldset  "MicrographGroupMetadata.star.relion" "Import Micrographs"
mic_opticsgroup "Optics Group" bi-eyeglasses        fieldset  "MicrographGroupMetadata.star.relion"  ?
#
loop_
_coordsdata.id
_coordsdata.label
_coordsdata.icon
_coordsdata.widget
_coordsdata.default
_coordsdata.help
box_indata     "Particle Coordinates/Boxes"  bi-box-arrow-in-down fieldset "MicrographCoordsGroup.star.relion" "Import Particle Coordinates"
loop_
_partsdata.id
_partsdata.label
_partsdata.icon
_partsdata.widget
_partsdata.default
_partsdata.help
ptcls_data     "Particle Star File"  bi-box-arrow-in-down fieldset "ParticleGroupMetadata.star.relion" "Import Particle Star File"
#
loop_
_img2ddata.id
_img2ddata.label
_img2ddata.icon
_img2ddata.widget
_img2ddata.help
refs_indata      "2D/3D References"       bi-box-arrow-in-down fieldset "Import Movies"
#
loop_
_mapdata.id
_mapdata.label
_mapdata.icon
_mapdata.widget
_mapdata.help
map_indata      "Density Map"       bi-box-arrow-in-down fieldset "Import Movies"
#
loop_
_maskdata.id
_maskdata.label
_maskdata.icon
_maskdata.widget
_maskdata.help
mask_indata      "Mask"       bi-box-arrow-in-down fieldset "Import Mask"
#
loop_
_halfmapdata.id
_halfmapdata.label
_halfmapdata.icon
_halfmapdata.widget
_halfmapdata.help
halfmap_indata      "Half-maps"       bi-box-arrow-in-down fieldset "Import Movies"
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
dir_in_raw       "Raw input directory:"     string       /path/of/movies/ ?  "."             "?"             required        
; Copy and paste the directory of your raw data. It is best if you set the absolute path rather than the relative one.
In contrary of RELION, the symbolic links will be generated and the output directory will be PROJECT_DIR/Movies/. 
All the imported files will be renamed as <prefix>0001.ext.
;
pattern_in         "Common Pattern"            string movie ? ? ? ? 
; Common pattern to all the input files. All the files corresponding to the regular expression `*pattern*.ext` will be searched.
Be careful when using extra regular expression.
;
img_ext           "Input Image Extension"       select ?          ? ? ? ? ?
img_ext::mrc      "mrc"                         option "mrc"      ? ? ? ? ?
img_ext::mrcs     "mrcs"                        option "mrcs"     ? ? ? ? ?
img_ext::tif      "tif"                         option "tif"      ? ? ? ? ?
img_ext::tiff     "tiff"                        option "tiff"     ? ? ? ? ?
img_ext::eer      "eer"                         option "eer"      ? ? ? ? ?
img_ext::mrc.bz2  "mrc.bz2"                     option "mrc.bz2"  ? ? ? ? ?
img_ext::mrcs.bz2 "mrcs.bz2"                    option "mrcs.bz2" ? ? ? ? ?
img_ext::mrc.zst  "mrc.zst"                     option "mrc.zst"  ? ? ? ? ?
img_ext::mrcs.zst "mrcs.zst"                    option "mrcs.zst" ? ? ? ? ?
img_ext::mrc.xz   "mrc.xz"                      option "mrc.xz"   ? ? ? ? ?
img_ext::mrcs.xz  "mrcs.xz"                     option "mrcs.xz"  ? ? ? ? ?
keep_name         "Keep the original filenames" bool   False      ? ? ? ? 
; By default, the output files are renamed `prefix000001.ext`, `prefix000002.ext`, etc. where `ext` is the image extension.
;
pattern_out       "Output Prefix"    string   mov ? ? ? ? "Common pattern to all the imported output files"
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
loop_
_box_indata.id
_box_indata.label
_box_indata.widget
_box_indata.default
_box_indata.arg0
_box_indata.arg1
_box_indata.arg2
_box_indata.state
_box_indata.help
ptcls_fn_in_raw     "Particles Directory" string "/path/of/particles_box/" ? ? ? ? "Copy and paste the input file path"
