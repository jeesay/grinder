#!/bin/bash

# All the directory names of the different types of jobs defined inside the pipeline
PROC_IMPORT_DIRNAME="Import"       # Import any file as a Node of a given type
PROC_MOTIONCORR_DIRNAME="MotionCorr"   # Import any file as a Node of a given type
PROC_CTFFIND_DIRNAME="CtfFind"       # Estimate CTF parameters from micrographs for either entire micrographs and/or particles
PROC_MANUALPICK_DIRNAME="ManualPick"   # Manually pick particle coordinates from micrographs
PROC_AUTOPICK_DIRNAME="AutoPick"     # Automatically pick particle coordinates from micrographs their CTF and 2D references
PROC_EXTRACT_DIRNAME="Extract"      # Window particles normalize downsize etc from micrographs (also combine CTF into metadata file)
PROC_CLASSSELECT_DIRNAME="Select"      # Read in model.star file and let user interactively select classes through the display (later: auto-selection as well)
PROC_2DCLASS_DIRNAME="Class2D"      # 2D classification (from input particles)
PROC_3DCLASS_DIRNAME="Class3D"      # 3D classification (from input 2D/3D particles an input 3D-reference and possibly a 3D mask)
PROC_3DAUTO_DIRNAME="Refine3D"     # 3D auto-refine (from input particles an input 3Dreference and possibly a 3D mask)
PROC_MASKCREATE_DIRNAME="MaskCreate"   # Process to create masks from input maps
PROC_JOINSTAR_DIRNAME="JoinStar"     # Process to create masks from input maps
PROC_SUBTRACT_DIRNAME="Subtract"     # Process to subtract projections of parts of the reference from experimental images
PROC_POST_DIRNAME="PostProcess"  # Post-processing (from unfiltered half-maps and a possibly a 3D mask)
PROC_RESMAP_DIRNAME="LocalRes"     # Local resolution estimation (from unfiltered half-maps and a 3D mask)
PROC_INIMODEL_DIRNAME="InitialModel" # De-novo generation of 3D initial model (using SGD)
PROC_MULTIBODY_DIRNAME="MultiBody"    # Multi-body refinement
PROC_MOTIONREFINE_DIRNAME="Polish"       # Jasenko's motion fitting program for Bayesian polishing (to replace MovieRefine?)
PROC_CTFREFINE_DIRNAME="CtfRefine"    # Jasenko's program for defocus and beamtilt optimisation
PROC_DYNAMIGHT_DIRNAME="DynaMight"                    # Johannes' DynaMight for modelling continuous heterogeneity
PROC_MODELANGELO_DIRNAME="ModelAngelo"                  # Kiarash's ModelAngelo for automated model building
PROC_TOMO_IMPORT_DIRNAME="Import"                       # Import for tomography GUI
PROC_TOMO_SUBTOMO_DIRNAME="Extract"                      # Creation of pseudo-subtomograms from tilt series images
PROC_TOMO_CTFREFINE_DIRNAME="CtfRefine"                    # CTF refinement (defocus & aberrations) for tomography
PROC_TOMO_EXCLUDE_TILT_IMAGES_DIRNAME="ExcludeTiltImages"  # Exclusion of bad tilt-images from tilt-series
PROC_TOMO_ALIGN_DIRNAME="Polish"                       # Frame alignment and particle polishing for subtomography
PROC_TOMO_RECONSTRUCT_DIRNAME="Reconstruct"                  # Calculation of particle average from the individual tilt series images
PROC_TOMO_DENOISE_DIRNAME="Denoise"                          # Denoise tomograms
PROC_TOMO_PICK_DIRNAME="Picks"                               # Pick particles in tomograms
PROC_EXTERNAL_DIRNAME="External"                     # For running non-relion programs
PROC_TOMO_ALIGN_TILTSERIES_DIRNAME="AlignTiltSeries"         # ilt series alignment for tomogram reconstruction
PROC_TOMO_RECONSTRUCT_TOMOGRAM_DIRNAME="Tomograms" # Reconstruction of tomograms for particle picking
#
# All the directory names of the different types of jobs defined inside the pipeline
PROC_IMPORT_LABELNEW="relion.import"       # Import any file as a Node of a given type
PROC_MOTIONCORR_LABELNEW="relion.motioncorr"   # Import any file as a Node of a given type
PROC_CTFFIND_LABELNEW="relion.ctffind"       # Estimate CTF parameters from micrographs for either entire micrographs and/or particles
PROC_MANUALPICK_LABELNEW="relion.manualpick"   # Manually pick particle coordinates from micrographs
PROC_AUTOPICK_LABELNEW="relion.autopick"     # Automatically pick particle coordinates from micrographs their CTF and 2D references
PROC_EXTRACT_LABELNEW="relion.extract"      # Window particles, normalize,  downsize etc from micrographs (also combine CTF into metadata file)
PROC_CLASSSELECT_LABELNEW="relion.select"      # Read in model.star file and let user interactively select classes through the display (later: auto-selection as well)
PROC_2DCLASS_LABELNEW="relion.class2d"      # 2D classification (from input particles)
PROC_3DCLASS_LABELNEW="relion.class3d"      # 3D classification (from input 2D/3D particles an input 3D-reference and possibly a 3D mask)
PROC_3DAUTO_LABELNEW="relion.refine3d"     # 3D auto-refine (from input particles an input 3Dreference and possibly a 3D mask)
PROC_MASKCREATE_LABELNEW="relion.maskcreate"   # Process to create masks from input maps
PROC_JOINSTAR_LABELNEW="relion.joinstar"     # Process to create masks from input maps
PROC_SUBTRACT_LABELNEW="relion.subtract"     # Process to subtract projections of parts of the reference from experimental images
PROC_POST_LABELNEW="relion.postprocess"  # Post-processing (from unfiltered half-maps and a possibly a 3D mask)
PROC_RESMAP_LABELNEW="relion.localres"     # Local resolution estimation (from unfiltered half-maps and a 3D mask)
PROC_INIMODEL_LABELNEW="relion.initialmodel" # De-novo generation of 3D initial model (using SGD)
PROC_MULTIBODY_LABELNEW="relion.multibody"    # Multi-body refinement
PROC_MOTIONREFINE_LABELNEW="relion.polish"       # Jasenko's motion fitting program for Bayesian polishing (to replace MovieRefine?)
PROC_CTFREFINE_LABELNEW="relion.ctfrefine"    # Jasenko's program for defocus and beamtilt optimisation
PROC_DYNAMIGHT_LABELNEW="dynamight"           # Johannes' DynaMight for modelling continuous heterogeneity
PROC_MODELANGELO_LABELNEW="modelangelo"         # Kiarash's ModelAngelo for automated model building
PROC_TOMO_IMPORT_LABELNEW="relion.importtomo"              # Import for tomography GUI
PROC_TOMO_EXCLUDE_TILT_IMAGES_LABELNEW="relion.excludetilts"    # Exclude bad tilt-images
PROC_TOMO_SUBTOMO_LABELNEW="relion.pseudosubtomo"           # Creation of pseudo-subtomograms from tilt series images
PROC_TOMO_CTFREFINE_LABELNEW="relion.ctfrefinetomo"           # CTF refinement (defocus & aberrations) for tomography
PROC_TOMO_ALIGN_LABELNEW="relion.framealigntomo"          # Frame alignment and particle polishing for subtomography
PROC_TOMO_RECONSTRUCT_LABELNEW="relion.reconstructparticletomo" # Calculation of particle average from the individual tilt series images
PROC_TOMO_DENOISE_LABELNEW="relion.denoisetomo"  # Denoise tomograms
PROC_TOMO_PICK_LABELNEW="relion.picktomo"     # Pick tomograms
PROC_EXTERNAL_LABELNEW="relion.external"     # For running non-relion programs
PROC_TOMO_ALIGN_TILTSERIES_LABELNEW="relion.aligntiltseries" # ilt series alignment for tomogram reconstruction
PROC_TOMO_RECONSTRUCT_TOMOGRAM_LABELNEW="relion.reconstructtomograms" # Reconstruction of tomograms for particle picking
#
# General nodes used for input into relion jobs have a _CPIPE suffix
LABEL_MOVIES_CPIPE="MicrographMovieGroupMetadata.star.relion"
LABEL_MICS_CPIPE="MicrographGroupMetadata.star.relion"
LABEL_2DIMGS_CPIPE="Image2DGroupMetadata.star.relion"
LABEL_MAP_CPIPE="DensityMap.mrc"
LABEL_PARTS_CPIPE="ParticleGroupMetadata.star.relion"
LABEL_COORDS_CPIPE="MicrographCoordsGroup.star.relion"
LABEL_COORDS_HELIX_CPIPE="MicrographCoordsGroup.star.relion.helixstartend"
LABEL_PARTS_HELIX_CPIPE="ParticleGroupMetadata.star.relion.helicalsegments"
LABEL_OPTIMISER_CPIPE="OptimiserData.star.relion"
LABEL_MASK_CPIPE="Mask3D.mrc"
LABEL_HALFMAP_CPIPE="DensityMap.mrc.halfmap"
LABEL_RESMAP_CPIPE="Image3D.mrc.localresmap"
LABEL_LOGFILE_CPIPE="LogFile.pdf.relion"
LABEL_SEQUENCE_CPIPE="Sequence.fasta"
LABEL_SEQUENCEALIGNMENT_CPIPE="SequenceAlignment.hmm"
LABEL_ATOMCOORDS_CPIPE="AtomCoords.cif"
LABEL_TOMO_OPTSET_CPIPE="TomoOptimisationSet.star.relion"
LABEL_TOMOGRAMS_CPIPE="TomogramGroupMetadata.star.relion"
LABEL_TRAJECTORIES_CPIPE="TomoTrajectoryData.star.relion"
LABEL_MANIFOLDS_CPIPE="TomoManifoldData.star.relion"
LABEL_POSTPROCESS_CPIPE="ProcessData.star.relion.postprocess"
#
# More specific output nodes are below
LABEL_IMPORT_MOVIES="MicrographMovieGroupMetadata.star.relion"
LABEL_IMPORT_MICS="MicrographGroupMetadata.star.relion"
LABEL_IMPORT_COORDS="MicrographCoordsGroup.star.relion"
LABEL_IMPORT_PARTS="ParticleGroupMetadata.star.relion"
LABEL_IMPORT_2DIMG="Image2DGroupMetadata.star.relion"
LABEL_IMPORT_MAP="DensityMap.mrc"
LABEL_IMPORT_MASK="Mask3D.mrc"
LABEL_IMPORT_HALFMAP="DensityMap.mrc.halfmap"
LABEL_MOCORR_MICS="MicrographGroupMetadata.star.relion.motioncorr"
LABEL_MOCORR_LOG="LogFile.pdf.relion.motioncorr"
LABEL_CTFFIND_MICS="MicrographGroupMetadata.star.relion.ctf"
LABEL_CTFFIND_LOG="LogFile.pdf.relion.ctffind"
LABEL_CTFFIND_POWER_SPECTRA="Image2DGroupMetadata.star.relion.ctffind.power_spectra"
LABEL_MANPICK_MICS="MicrographGroupMetadata.star.relion"
LABEL_MANPICK_COORDS="MicrographCoordsGroup.star.relion.manualpick"
LABEL_MANPICK_COORDS_HELIX="MicrographCoordsGroup.star.relion.manualpick.helixstartend"
LABEL_AUTOPICK_COORDS="MicrographCoordsGroup.star.relion.autopick"
LABEL_AUTOPICK_LOG="LogFile.pdf.relion.autopick"
LABEL_AUTOPICK_TOPAZMODEL="ParamsData.sav.topaz.model" # to be added?
LABEL_AUTOPICK_MICS="MicrographGroupMetadata.star.relion"
LABEL_EXTRACT_PARTS="ParticleGroupMetadata.star.relion"
LABEL_EXTRACT_PARTS_HELIX="ParticleGroupMetadata.star.relion.helicalsegments"
LABEL_EXTRACT_COORDS_HELIX="MicrographCoordsGroup.star.relion.helixstartend"
LABEL_EXTRACT_PARTS_REEX="ParticleGroupMetadata.star.relion.reextract"
LABEL_EXTRACT_COORDS_REEX="MicrographCoordsGroup.star.relion.reextract"
LABEL_CLASS2D_PARTS="ParticleGroupMetadata.star.relion.class2d"
LABEL_CLASS2D_OPT="OptimiserData.star.relion.class2d"
LABEL_CLASS2D_PARTS_HELIX="ParticleGroupMetadata.star.relion.class2d.helicalsegments"
LABEL_SELECT_MICS="MicrographGroupMetadata.star.relion"
LABEL_SELECT_MOVS="MicrographMovieGroupMetadata.star.relion"
LABEL_SELECT_PARTS="ParticleGroupMetadata.star.relion"
LABEL_SELECT_OPT="OptimiserData.star.relion.select"
LABEL_SELECT_CLAVS="Image2DGroupMetadata.star.relion.classaverages"
LABEL_SELECT_LOG="LogFile.pdf.relion.select"
LABEL_INIMOD_MAP="DensityMap.mrc.relion.initialmodel"
LABEL_INIMOD_OPTSET="TomoOptimisationSet.star.relion.initialmodel"
LABEL_CLASS3D_OPT="OptimiserData.star.relion.class3d"
LABEL_CLASS3D_MAP="DensityMap.mrc.relion.class3d"
LABEL_CLASS3D_PARTS="ParticleGroupMetadata.star.relion.class3d"
LABEL_CLASS3D_PARTS_HELIX="ParticleGroupMetadata.star.relion.class3d.helicalsegments"
LABEL_CLASS3D_OPTSET="TomoOptimisationSet.star.relion.class3d"
LABEL_REFINE3D_HALFMAP="DensityMap.mrc.relion.halfmap.refine3d"
LABEL_REFINE3D_OPT="OptimiserData.star.relion.refine3d"
LABEL_REFINE3D_MAP="DensityMap.mrc.relion.refine3d"
LABEL_REFINE3D_PARTS="ParticleGroupMetadata.star.relion.refine3d"
LABEL_REFINE3D_PARTS_HELIX="ParticleGroupMetadata.star.relion.refine3d.helicalsegements"
LABEL_REFINE3D_OPTSET="TomoOptimisationSet.star.relion.refine3d"
LABEL_MULTIBODY_HALFMAP="DensityMap.mrc.relion.halfmap.multibody"
LABEL_MULTIBODY_PARTS="ParticleGroupMetadata.star.relion.multibody"
LABEL_MULTIBODY_OPT="OptimiserData.star.relion.multibody"
LABEL_MULTIBODY_FLEXLOG="LogFile.pdf.relion.flexanalysis"
LABEL_MULTIBODY_SEL_PARTS="ParticleGroupMetadata.star.relion.flexanalysis.eigenselected"
LABEL_MULTIBODY_OPTSET="TomoOptimisationSet.star.relion.multibody"
LABEL_DYNAMIGHT_HALFMAP="DensityMap.mrc.relion.halfmap.dynamight"
LABEL_MASK3D_MASK="Mask3D.mrc.relion"
LABEL_SUBTRACT_SUBTRACTED="ParticleGroupMetadata.star.relion.subtracted"
LABEL_SUBTRACT_REVERTED="ParticleGroupMetadata.star.relion"
LABEL_LOCRES_OWN="Image3D.mrc.relion.localresmap"
LABEL_LOCRES_RESMAP="Image3D.mrc.resmap.localresmap"
LABEL_LOCRES_FILTMAP="DensityMap.mrc.relion.localresfiltered"
LABEL_LOCRES_LOG="LogFile.pdf.relion.localres"
LABEL_CTFREFINE_REFINEPARTS="ParticleGroupMetadata.star.relion.ctfrefine"
LABEL_CTFREFINE_LOG="LogFile.pdf.relion.ctfrefine"
LABEL_CTFREFINE_ANISOPARTS="ParticleGroupMetadata.star.relion.anisomagrefine"
LABEL_POLISH_PARTS="ParticleGroupMetadata.star.relion.polished"
LABEL_POLISH_LOG="LogFile.pdf.relion.polish"
LABEL_POLISH_PARAMS="ParamsData.txt.relion.polish"
LABEL_POST_POST="ProcessData.star.relion.postprocess"
LABEL_POST_MAP="DensityMap.mrc.relion.postprocess"
LABEL_POST_MASKED="DensityMap.mrc.relion.postprocess.masked"
LABEL_POST_LOG="LogFile.pdf.relion.postprocess"
#
# > spa/01-Import
cat > label.txt <<EOL
#
_id        import_movies
_label     'Raw movies'
_widget    radio
_parent    movies
_help      'Set this to Yes if you plan to import raw multi-frame movies. Don\'t import files outside the project directory.\nPlease make a symbolic link by an absolute path before importing.'
_comment   'import_movies'
_proc_id  0
_labelnew     "${PROC_CTFFIND_LABELNEW}"
_hidden_name  '.gui_zzz'
EOL
cat > io.txt <<EOL
loop_
_indata.id
_indata.label
_indata.widget
_indata.default  # None
_indata.arg0     # Status
_indata.arg1     # Placeholder
_indata.arg2     # Node Type
_indata.help
input_star_mics "Input micrographs STAR file:" file "" required "STAR files (*.star)" LABEL_MICS_CPIPE "A STAR file with all micrographs to run CTFFIND or Gctf on"
#
loop_
_outdata.id
_outdata.label
_outdata.widget
_outdata.default  # None
_outdata.arg0     # filetype
_outdata.arg1     # placeholder
_outdata.arg2     # Directory
_outdata.help
dirname       "Output Dir."       string_ro "${PROC_CTFFIND_DIRNAME}" PROC_IMPORT_DIRNAME ? ? ?
outnode0      "Output Node0"      string_ro "micrographs_ctf.star"    LABEL_CTFFIND_MICS  ? ? ?
outnode1      "Output Node1"      string_ro "logfile.pdf"             LABEL_CTFFIND_LOG   ? ? ?
#
EOL
echo data_ | cat - label.txt tabs.txt io.txt menu_template.star > spa/01_import/01.star
cat > label.txt <<EOL
#
_id        import_micrographs
_label    'Raw micrographs'
_widget   radio
_parent   movies
_help     'Set this to Yes if you plan to import raw single-frame micrographs'
_comment  'import_micrographs'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_ | cat - label.txt tabs.txt io.txt menu_template.star > spa/01_import/02.star
cat > label.txt <<EOL
#
_id        import_micrographs_starfile
_label    'Micrographs STAR File (.star)'
_widget   radio
_parent   movies
_help     ''
_comment  'import_micrographs_starfile'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_ | cat - label.txt tabs.txt io.txt menu_template.star > spa/01_import/03.star
cat > label.txt <<EOL
#
_id       import_particle_coords
_label    'Particles coordinates (.box, *_pick.star)'
_widget    radio
_parent   particles
_help     ''
_comment  'import_particle_coords'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_ | cat - label.txt tabs.txt io.txt menu_template.star > spa/01_import/04.star
cat > label.txt <<EOL
#
_id       particles_starfile
_label    'Particles STAR file (.star)'
_widget    radio
_parent   particles
_help     ''
_comment  'import_particle_starfile'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_ | cat - label.txt tabs.txt io.txt menu_template.star > spa/01_import/05.star
cat > label.txt <<EOL
#
_id       import_ref
_label    'Multiple (2D or 3D) references (.star or .mrcs)'
_widget   radio
_parent   refs
_help     'import_ref'
_comment  'import_movies'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_ | cat - label.txt tabs.txt io.txt menu_template.star > spa/01_import/06.star
cat > label.txt <<EOL
#
_id       import_ref3d
_label    '3D reference (.star)'
_widget    radio
_parent   refs
_help     ''
_comment  'import_ref3d'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_ | cat - label.txt tabs.txt io.txt menu_template.star > spa/01_import/07.star
cat > label.txt <<EOL
#
_id       import_mask3d
_label    '3D mask (.mrc)'
_widget    radio
_parent   masks
_help     ''
_comment  'import_mask3d'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_ | cat - label.txt tabs.txt io.txt menu_template.star > spa/01_import/08.star
cat > label.txt <<EOL
#
_id       import_mask_half
_label    'Unfiltered half-mask (unfil.mrc)'
_widget    radio
_parent   masks
_help     ''
_comment  'import_mask_half'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_ | cat - label.txt tabs.txt io.txt menu_template.star > spa/01_import/09.star
cat > label.txt <<EOL
#
_id       import_other
_label    'MTF, Gain ref., Defect, etc.'
_widget    radio
_parent   others
_help     ''
_comment  'import_other'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_ | cat - label.txt tabs.txt io.txt menu_template.star > spa/01_import/10.star

#  > spa/02_preprocess
cat > label.txt <<EOL
#
_id       relioncor2
_label    'Relion Motioncor2-like implementation'
_widget    radio
_parent   motion
_help     'If set to Yes, use RELION's own implementation of a MotionCor2-like algorithm by Takanori Nakane. Note that Takanori's program only runs on CPUs but uses multiple threads. Takanori's implementation is most efficient when the number of frames is divisible by the number of threads (e.g. 12 or 18 threads per MPI process for 36 frames). On some machines, setting the OMP_PROC_BIND environmental variable to TRUE accelerates the program.'
_comment  'relioncor2'
EOL
echo data_  | cat - label.txt tabs.txt io.txt menu_template.star > spa/02_preprocess/01.star
cat > label.txt <<EOL
#
_id       relioncor2
_label    'UCSF MotionCor 2'
_widget    radio
_parent   motion
_help     'Set this to Yes if you plan to use the UCSF implementation. The UCSF-implementation needs a GPU but uses only one CPU thread.'
_comment  'ucsf motioncor2'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_  | cat - label.txt tabs.txt io.txt menu_template.star > spa/02_preprocess/02.star
cat > label.txt <<EOL
#
_id       use_motioncor3
_label    'TODO - Chan Zuckerberg Imaging Institute (CZII) MotionCor 3 (includes CTF estimation)'
_widget    radio
_parent   motion
_help     'Set this to Yes if you plan to use the UCSF implementation. The UCSF-implementation needs a GPU but uses only one CPU thread.'
_comment  'czii motioncor3'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_  | cat - label.txt tabs.txt io.txt menu_template.star > spa/02_preprocess/03.star
cat > label.txt <<EOL
#
_id       use_ctffind4
_label    'CTF with CTFFIND 4.1'
_widget    radio
_parent   ctffind
_help     'If set to Yes, the wrapper will use CTFFIND4 (version 4.1) for CTF estimation. This includes thread-support, calculation of Thon rings from movie frames and phase-shift estimation for phase-plate data.'
_comment  'use_ctffind4'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_  | cat - label.txt tabs.txt io.txt menu_template.star > spa/02_preprocess/04.star
cat > label.txt <<EOL
#
_id       use_gctf
_label    'CTF with gctf'
_widget    radio
_parent   ctffind
_help     ''
_comment  'use_gctf'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_  | cat - label.txt tabs.txt io.txt menu_template.star > spa/02_preprocess/05.star


# > spa/03_particles
cat > label.txt <<EOL
#
_id       use_manual
_label    'Manual'
_widget    radio
_parent   manual
_help     ''
_comment  'manual'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_   | cat - label.txt tabs.txt io.txt menu_template.star > spa/03_particles/01.star
cat > label.txt <<EOL
#
_id       auto_LoG
_label    'Blob Detection (LoG)'
_widget   radio
_parent   auto
_help     ''
_comment  'auto_LoG'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_   | cat - label.txt tabs.txt io.txt menu_template.star > spa/03_particles/02.star
cat > label.txt <<EOL
#
_id       auto_template
_label    'Template Matching'
_widget    radio
_parent   auto
_help     ''
_comment  'auto_template'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_   | cat - label.txt tabs.txt io.txt menu_template.star > spa/03_particles/03.star
cat > label.txt <<EOL
#
_id       auto_topaz_train_coords
_label    'CTF with gctf'
_widget    radio
_parent   auto_topaz
_help     ''
_comment  'auto_topaz_train_coords'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_   | cat - label.txt tabs.txt io.txt menu_template.star > spa/03_particles/04.star
cat > label.txt <<EOL
#
_id       auto_topaz_train_ptcls
_label    'CTF with gctf'
_widget    radio
_parent   auto_topaz
_help     ''
_comment  'auto_topaz_train_ptcls'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_   | cat - label.txt tabs.txt io.txt menu_template.star > spa/03_particles/05.star
cat > label.txt <<EOL
#
_id       auto_topaz_pick
_label    'CTF with gctf'
_widget    radio
_parent   auto_topaz
_help     ''
_comment  'auto_topaz_pick'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_   | cat - label.txt tabs.txt io.txt menu_template.star > spa/03_particles/06.star
cat > label.txt <<EOL
#
_id       do_extract
_label    'Extract Particles'
_widget    radio
_parent   extract
_help     ''
_comment  'extract'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_   | cat - label.txt tabs.txt io.txt menu_template.star > spa/03_particles/07.star
cat > label.txt <<EOL
#
_id       do_re_extract
_label    'Re-extract Refined Particles'
_widget    radio
_parent   extract
_help     ''
_comment  're_extract'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_   | cat - label.txt tabs.txt io.txt menu_template.star > spa/03_particles/08.star
cat > label.txt <<EOL
#
_id       class2d_em
_label    'CTF with gctf'
_widget    radio
_parent   class2d
_help     ''
_comment  'class2d_em'
_proc_id  8
_labelnew     "relion.class2d"                            # PROC_2DCLASS_LABELNEW
_dirname      "Class2D"                                   # PROC_2DCLASS_DIRNAME
_hidden_name  '.gui_zzz'
#
loop_
_innode.id
_innode.label
LABEL_PARTS_CPIPE       "ParticleGroupMetadata.star.relion"
# 
loop_
_outnode.id
_outnode.label
LABEL_CLASS2D_PARTS      "ParticleGroupMetadata.star.relion.class2d"
LABEL_CLASS2D_OPT        "OptimiserData.star.relion.class2d"
EOL
echo data_   | cat - label.txt tabs.txt io.txt menu_template.star > spa/03_particles/09.star
cat > label.txt <<EOL
#
_id       class2d_vdam
_label    'CTF with gctf'
_widget    radio
_parent   class2d
_help     ''
_comment  'class2d_vdam'
_proc_id  8
_labelnew     "relion.class2d"                           # PROC_2DCLASS_LABELNEW
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
EOL
echo data_   | cat - label.txt tabs.txt io.txt menu_template.star > spa/03_particles/10.star
#******************************************************************************************
#
#******************************************************************************************
# > spa/04_3d
echo data_test | cat - menu_template.star > spa/04_3d/01_abinitio.star
echo data_test | cat - menu_template.star > spa/04_3d/02_class3d.star
echo data_test | cat - menu_template.star > spa/04_3d/03_class3d_noalign.star
echo data_test | cat - menu_template.star > spa/04_3d/04_refine.star
echo data_test | cat - menu_template.star > spa/04_3d/05_autorefine.star
echo data_test | cat - menu_template.star > spa/04_3d/06_multibody.star
# > spa/05_postprocess
echo data_test | cat - menu_template.star > spa/05_postprocess/01_mask.star
echo data_test | cat - menu_template.star > spa/05_postprocess/02_postprocess.star
echo data_test | cat - menu_template.star > spa/05_postprocess/03_sharpen_auto.star
echo data_test | cat - menu_template.star > spa/05_postprocess/04_sharpen_user.star
echo data_test | cat - menu_template.star > spa/05_postprocess/05_ctfrefine.star
echo data_test | cat - menu_template.star > spa/05_postprocess/06_aberrations.star
echo data_test | cat - menu_template.star > spa/05_postprocess/07_anisomag.star
echo data_test | cat - menu_template.star > spa/05_postprocess/08_defocus.star
echo data_test | cat - menu_template.star > spa/05_postprocess/09_advctfrefine.star
echo data_test | cat - menu_template.star > spa/05_postprocess/10_polish.star
echo data_test | cat - menu_template.star > spa/05_postprocess/11_polish_train.star
echo data_test | cat - menu_template.star > spa/05_postprocess/12_polish_perform.star
echo data_test | cat - menu_template.star > spa/05_postprocess/13_polish_perform_manual.star
# > spa/06_metrics
echo data_test | cat - menu_template.star > spa/06_metrics/locres.star
echo data_test | cat - menu_template.star > spa/06_metrics/locres_relion.star
# > spa/07_tools
echo data_test | cat - menu_template.star > spa/07_tools/01_subset_selection.star
echo data_test | cat - menu_template.star > spa/07_tools/01_subset_selection_stats.star
# Automatic class selection
#echo data_test | cat - menu_template.star > spa/07_tools/01_select_particles_from_classes.star
#echo data_test | cat - menu_template.star > spa/07_tools/01_select_classes.star
echo data_test | cat - menu_template.star > spa/07_tools/01_split_in_elements.star
echo data_test | cat - menu_template.star > spa/07_tools/01_split_in_subsets.star
echo data_test | cat - menu_template.star > spa/07_tools/01_join_star.star
echo data_test | cat - menu_template.star > spa/07_tools/01_combine_particle.star
echo data_test | cat - menu_template.star > spa/07_tools/01_combine_micrograph.star
echo data_test | cat - menu_template.star > spa/07_tools/01_combine_movie.star
echo data_test | cat - menu_template.star > spa/07_tools/01_ptcls_subtract.star
echo data_test | cat - menu_template.star > spa/07_tools/01_crop_pad.star
echo data_test | cat - menu_template.star > spa/07_tools/01_resize_map.star
echo data_test | cat - menu_template.star > spa/07_tools/01_external.star



