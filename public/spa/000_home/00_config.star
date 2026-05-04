data_
#
# General nodes used for input into relion jobs have a _CPIPE suffix
_LABEL_MOVIES_CPIPE             "MicrographMovieGroupMetadata.star.relion"
_LABEL_MICS_CPIPE               "MicrographGroupMetadata.star.relion"
_LABEL_2DIMGS_CPIPE             "Image2DGroupMetadata.star.relion"
_LABEL_MAP_CPIPE                "DensityMap.mrc"
_LABEL_PARTS_CPIPE              "ParticleGroupMetadata.star.relion"
_LABEL_COORDS_CPIPE             "MicrographCoordsGroup.star.relion"
_LABEL_COORDS_HELIX_CPIPE       "MicrographCoordsGroup.star.relion.helixstartend"
_LABEL_PARTS_HELIX_CPIPE        "ParticleGroupMetadata.star.relion.helicalsegments"
_LABEL_OPTIMISER_CPIPE          "OptimiserData.star.relion"
_LABEL_MASK_CPIPE               "Mask3D.mrc"
_LABEL_HALFMAP_CPIPE             "DensityMap.mrc.halfmap"
_LABEL_RESMAP_CPIPE             "Image3D.mrc.localresmap"
_LABEL_LOGFILE_CPIPE            "LogFile.pdf.relion"
_LABEL_SEQUENCE_CPIPE           "Sequence.fasta"
_LABEL_SEQUENCEALIGNMENT_CPIPE  "SequenceAlignment.hmm"
_LABEL_ATOMCOORDS_CPIPE         "AtomCoords.cif"
_LABEL_TOMO_OPTSET_CPIPE        "TomoOptimisationSet.star.relion"
_LABEL_TOMOGRAMS_CPIPE          "TomogramGroupMetadata.star.relion"
_LABEL_TRAJECTORIES_CPIPE       "TomoTrajectoryData.star.relion"
_LABEL_MANIFOLDS_CPIPE          "TomoManifoldData.star.relion"
_LABEL_POSTPROCESS_CPIPE        "ProcessData.star.relion.postprocess"
#
# More specific output nodes are below
_LABEL_IMPORT_MOVIES            "MicrographMovieGroupMetadata.star.relion"
_LABEL_IMPORT_MICS              "MicrographGroupMetadata.star.relion"
_LABEL_IMPORT_COORDS            "MicrographCoordsGroup.star.relion"
_LABEL_IMPORT_PARTS             "ParticleGroupMetadata.star.relion"
_LABEL_IMPORT_2DIMG             "Image2DGroupMetadata.star.relion"
_LABEL_IMPORT_MAP               "DensityMap.mrc"
_LABEL_IMPORT_MASK              "Mask3D.mrc"
_LABEL_IMPORT_HALFMAP           "DensityMap.mrc.halfmap"
_LABEL_MOCORR_MICS              "MicrographGroupMetadata.star.relion.motioncorr"
_LABEL_MOCORR_LOG               "LogFile.pdf.relion.motioncorr"
_LABEL_CTFFIND_MICS             "MicrographGroupMetadata.star.relion.ctf"
_LABEL_CTFFIND_LOG              "LogFile.pdf.relion.ctffind"
_LABEL_CTFFIND_POWER_SPECTRA    "Image2DGroupMetadata.star.relion.ctffind.power_spectra"
_LABEL_MANPICK_MICS             "MicrographGroupMetadata.star.relion"
_LABEL_MANPICK_COORDS           "MicrographCoordsGroup.star.relion.manualpick"
_LABEL_MANPICK_COORDS_HELIX     "MicrographCoordsGroup.star.relion.manualpick.helixstartend"
_LABEL_AUTOPICK_COORDS          "MicrographCoordsGroup.star.relion.autopick"
_LABEL_AUTOPICK_LOG             "LogFile.pdf.relion.autopick"
_LABEL_AUTOPICK_TOPAZMODEL      "ParamsData.sav.topaz.model" # to be added?
_LABEL_AUTOPICK_MICS            "MicrographGroupMetadata.star.relion"
_LABEL_EXTRACT_PARTS            "ParticleGroupMetadata.star.relion"
_LABEL_EXTRACT_PARTS_HELIX      "ParticleGroupMetadata.star.relion.helicalsegments"
_LABEL_EXTRACT_COORDS_HELIX     "MicrographCoordsGroup.star.relion.helixstartend"
_LABEL_EXTRACT_PARTS_REEX       "ParticleGroupMetadata.star.relion.reextract"
_LABEL_EXTRACT_COORDS_REEX      "MicrographCoordsGroup.star.relion.reextract"
_LABEL_CLASS2D_PARTS            "ParticleGroupMetadata.star.relion.class2d"
_LABEL_CLASS2D_OPT              "OptimiserData.star.relion.class2d"
_LABEL_CLASS2D_PARTS_HELIX      "ParticleGroupMetadata.star.relion.class2d.helicalsegments"
_LABEL_SELECT_MICS              "MicrographGroupMetadata.star.relion"
_LABEL_SELECT_MOVS              "MicrographMovieGroupMetadata.star.relion"
_LABEL_SELECT_PARTS             "ParticleGroupMetadata.star.relion"
_LABEL_SELECT_OPT               "OptimiserData.star.relion.select"
_LABEL_SELECT_CLAVS             "Image2DGroupMetadata.star.relion.classaverages"
_LABEL_SELECT_LOG               "LogFile.pdf.relion.select"
_LABEL_INIMOD_MAP               "DensityMap.mrc.relion.initialmodel"
_LABEL_INIMOD_OPTSET            "TomoOptimisationSet.star.relion.initialmodel"
_LABEL_CLASS3D_OPT              "OptimiserData.star.relion.class3d"
_LABEL_CLASS3D_MAP              "DensityMap.mrc.relion.class3d"
_LABEL_CLASS3D_PARTS            "ParticleGroupMetadata.star.relion.class3d"
_LABEL_CLASS3D_PARTS_HELIX      "ParticleGroupMetadata.star.relion.class3d.helicalsegments"
_LABEL_CLASS3D_OPTSET           "TomoOptimisationSet.star.relion.class3d"
_LABEL_REFINE3D_HALFMAP         "DensityMap.mrc.relion.halfmap.refine3d"
_LABEL_REFINE3D_OPT             "OptimiserData.star.relion.refine3d"
_LABEL_REFINE3D_MAP             "DensityMap.mrc.relion.refine3d"
_LABEL_REFINE3D_PARTS           "ParticleGroupMetadata.star.relion.refine3d"
_LABEL_REFINE3D_PARTS_HELIX     "ParticleGroupMetadata.star.relion.refine3d.helicalsegements"
_LABEL_REFINE3D_OPTSET          "TomoOptimisationSet.star.relion.refine3d"
_LABEL_MULTIBODY_HALFMAP        "DensityMap.mrc.relion.halfmap.multibody"
_LABEL_MULTIBODY_PARTS          "ParticleGroupMetadata.star.relion.multibody"
_LABEL_MULTIBODY_OPT            "OptimiserData.star.relion.multibody"
_LABEL_MULTIBODY_FLEXLOG        "LogFile.pdf.relion.flexanalysis"
_LABEL_MULTIBODY_SEL_PARTS      "ParticleGroupMetadata.star.relion.flexanalysis.eigenselected"
_LABEL_MULTIBODY_OPTSET         "TomoOptimisationSet.star.relion.multibody"
_LABEL_DYNAMIGHT_HALFMAP        "DensityMap.mrc.relion.halfmap.dynamight"
_LABEL_MASK3D_MASK              "Mask3D.mrc.relion"
_LABEL_SUBTRACT_SUBTRACTED      "ParticleGroupMetadata.star.relion.subtracted"
_LABEL_SUBTRACT_REVERTED        "ParticleGroupMetadata.star.relion"
_LABEL_LOCRES_OWN               "Image3D.mrc.relion.localresmap"
_LABEL_LOCRES_RESMAP            "Image3D.mrc.resmap.localresmap"
_LABEL_LOCRES_FILTMAP           "DensityMap.mrc.relion.localresfiltered"
_LABEL_LOCRES_LOG               "LogFile.pdf.relion.localres"
_LABEL_CTFREFINE_REFINEPARTS    "ParticleGroupMetadata.star.relion.ctfrefine"
_LABEL_CTFREFINE_LOG            "LogFile.pdf.relion.ctfrefine"
_LABEL_CTFREFINE_ANISOPARTS     "ParticleGroupMetadata.star.relion.anisomagrefine"
_LABEL_POLISH_PARTS             "ParticleGroupMetadata.star.relion.polished"
_LABEL_POLISH_LOG               "LogFile.pdf.relion.polish"
_LABEL_POLISH_PARAMS            "ParamsData.txt.relion.polish"
_LABEL_POST_POST                "ProcessData.star.relion.postprocess"
_LABEL_POST_MAP                 "DensityMap.mrc.relion.postprocess"
_LABEL_POST_MASKED              "DensityMap.mrc.relion.postprocess.masked"
_LABEL_POST_LOG                 "LogFile.pdf.relion.postprocess"
#
# Tomography-specific jobs
_LABEL_IMPORT_TOMOGRAMS         "TomogramGroupMetadata.star.relion.tomo.import"
_LABEL_IMPORT_TOMO_COORDS       "ParticleGroupMetadata.star.relion.tomo.import"
_LABEL_MOCORR_TOMOGRAMS         "TomogramGroupMetadata.star.relion.tomo.motioncorr"
_LABEL_CTFFIND_TOMOGRAMS        "TomogramGroupMetadata.star.relion.tomo.ctffind"
_LABEL_TILTALIGN_TOMOGRAMS      "TomogramGroupMetadata.star.relion.tomo.aligntiltseries"
_LABEL_TILTALIGN_LOG            "LogFile.pdf.relion.tomo.aligntiltseries"
_LABEL_RECONSTRUCT_TOMOGRAMS    "TomogramGroupMetadata.star.relion.tomo.reconstruct"
_LABEL_DENOISE_TOMOGRAMS        "TomogramGroupMetadata.star.relion.tomo.denoise"
_LABEL_TOMOPICK_PARTS_PARTS     "ParticleGroupMetadata.star.relion.tomo.manualpick.particles"
_LABEL_TOMOPICK_PARTS_SPHERE    "ParticleGroupMetadata.star.relion.tomo.manualpick.spheres"
_LABEL_TOMOPICK_PARTS_FILAMENT  "ParticleGroupMetadata.star.relion.tomo.manualpick.filaments"
_LABEL_TOMOPICK_PARTS_SURFACE   "ParticleGroupMetadata.star.relion.tomo.manualpick.surfaces"
_LABEL_TOMOPICK_OPTSET          "TomoOptimisationSet.star.relion.tomo.manualpick"
_LABEL_EXCLUDE_TOMOGRAMS        "TomogramGroupMetadata.star.relion.tomo.excludeimages"
_LABEL_SUBTOMO_PARTS            "ParticleGroupMetadata.star.relion.tomo.extract"
_LABEL_SUBTOMO_OPTSET           "TomoOptimisationSet.star.relion.tomo.extract"
_LABEL_CTFREFINE_TOMOGRAMS      "TomogramGroupMetadata.star.relion.tomo.ctfrefine"
_LABEL_CTFREFINE_OPTSET         "TomoOptimisationSet.star.relion.tomo.ctfrefine"
_LABEL_CTFREFINE_TOMO_LOG       "LogFile.pdf.relion.tomo.ctfrefine"
_LABEL_FRAMEALIGN_TOMOGRAMS     "TomogramGroupMetadata.star.relion.tomo.polish"
_LABEL_FRAMEALIGN_OPTSET        "TomoOptimisationSet.star.relion.tomo.polish"
_LABEL_FRAMEALIGN_LOG           "LogFile.pdf.relion.tomo.polish"
_LABEL_FRAMEALIGN_PARTS         "ParticleGroupMetadata.star.relion.tomo.polish"
_LABEL_FRAMEALIGN_TRAJS         "TomoTrajectoryData.star.relion.polish"
_LABEL_RECONSPART_OPTSET        "TomoOptimisationSet.star.relion.tomo.reconstruct"
_LABEL_RECONSPART_HALFMAP       "DensityMap.mrc.relion.tomo.halfmap.reconstruct"
_LABEL_RECONSPART_MAP           "DensityMap.mrc.relion.tomo.map.reconstruct"
#
# All the directory names of the different types of jobs defined inside the pipeline
_PROC_IMPORT_DIRNAME           "Import"       # Import any file as a Node of a given type
_PROC_MOTIONCORR_DIRNAME       "MotionCorr"   # Import any file as a Node of a given type
_PROC_CTFFIND_DIRNAME          "CtfFind"       # Estimate CTF parameters from micrographs for either entire micrographs and/or particles
_PROC_MANUALPICK_DIRNAME       "ManualPick"   # Manually pick particle coordinates from micrographs
_PROC_AUTOPICK_DIRNAME         "AutoPick"     # Automatically pick particle coordinates from micrographs their CTF and 2D references
_PROC_EXTRACT_DIRNAME          "Extract"      # Window particles normalize downsize etc from micrographs (also combine CTF into metadata file)
_PROC_CLASSSELECT_DIRNAME      "Select"      # Read in model.star file and let user interactively select classes through the display (later: auto-selection as well)
_PROC_2DCLASS_DIRNAME          "Class2D"      # 2D classification (from input particles)
_PROC_3DCLASS_DIRNAME          "Class3D"      # 3D classification (from input 2D/3D particles an input 3D-reference and possibly a 3D mask)
_PROC_3DAUTO_DIRNAME           "Refine3D"     # 3D auto-refine (from input particles an input 3Dreference and possibly a 3D mask)
_PROC_MASKCREATE_DIRNAME       "MaskCreate"   # Process to create masks from input maps
_PROC_JOINSTAR_DIRNAME         "JoinStar"     # Process to create masks from input maps
_PROC_SUBTRACT_DIRNAME         "Subtract"     # Process to subtract projections of parts of the reference from experimental images
_PROC_POST_DIRNAME        "PostProcess"  # Post-processing (from unfiltered half-maps and a possibly a 3D mask)
_PROC_RESMAP_DIRNAME          "LocalRes"     # Local resolution estimation (from unfiltered half-maps and a 3D mask)
_PROC_INIMODEL_DIRNAME      "InitialModel" # De-novo generation of 3D initial model (using SGD)
_PROC_MULTIBODY_DIRNAME        "MultiBody"    # Multi-body refinement
_PROC_MOTIONREFINE_DIRNAME     "Polish"       # Jasenko's motion fitting program for Bayesian polishing (to replace MovieRefine?)
_PROC_CTFREFINE_DIRNAME        "CtfRefine"    # Jasenko's program for defocus and beamtilt optimisation
_PROC_DYNAMIGHT_DIRNAME        "DynaMight"                    # Johannes' DynaMight for modelling continuous heterogeneity
_PROC_MODELANGELO_DIRNAME      "ModelAngelo"                  # Kiarash's ModelAngelo for automated model building
_PROC_TOMO_IMPORT_DIRNAME      "Import"                       # Import for tomography GUI
_PROC_TOMO_SUBTOMO_DIRNAME     "Extract"                      # Creation of pseudo-subtomograms from tilt series images
_PROC_TOMO_CTFREFINE_DIRNAME   "CtfRefine"                    # CTF refinement (defocus & aberrations) for tomography
_PROC_TOMO_EXCLUDE_TILT_IMAGES_DIRNAME   "ExcludeTiltImages"  # Exclusion of bad tilt-images from tilt-series
_PROC_TOMO_ALIGN_DIRNAME       "Polish"                       # Frame alignment and particle polishing for subtomography
_PROC_TOMO_RECONSTRUCT_DIRNAME "Reconstruct"                  # Calculation of particle average from the individual tilt series images
_PROC_TOMO_DENOISE_DIRNAME "Denoise"                          # Denoise tomograms
_PROC_TOMO_PICK_DIRNAME "Picks"                               # Pick particles in tomograms
_PROC_EXTERNAL_DIRNAME         "External"                     # For running non-relion programs
_PROC_TOMO_ALIGN_TILTSERIES_DIRNAME "AlignTiltSeries"         # ilt series alignment for tomogram reconstruction
_PROC_TOMO_RECONSTRUCT_TOMOGRAM_DIRNAME "Tomograms" # Reconstruction of tomograms for particle picking
#
# All the directory names of the different types of jobs defined inside the pipeline
_PROC_IMPORT_LABELNEW           "relion.import"       # Import any file as a Node of a given type
_PROC_MOTIONCORR_LABELNEW      "relion.motioncorr"   # Import any file as a Node of a given type
_PROC_CTFFIND_LABELNEW         "relion.ctffind"       # Estimate CTF parameters from micrographs for either entire micrographs and/or particles
_PROC_MANUALPICK_LABELNEW       "relion.manualpick"   # Manually pick particle coordinates from micrographs
_PROC_AUTOPICK_LABELNEW       "relion.autopick"     # Automatically pick particle coordinates from micrographs their CTF and 2D references
_PROC_EXTRACT_LABELNEW         "relion.extract"      # Window particles, normalize,  downsize etc from micrographs (also combine CTF into metadata file)
_PROC_CLASSSELECT_LABELNEW      "relion.select"      # Read in model.star file and let user interactively select classes through the display (later: auto-selection as well)
_PROC_2DCLASS_LABELNEW        "relion.class2d"      # 2D classification (from input particles)
_PROC_3DCLASS_LABELNEW       "relion.class3d"      # 3D classification (from input 2D/3D particles an input 3D-reference and possibly a 3D mask)
_PROC_3DAUTO_LABELNEW           "relion.refine3d"     # 3D auto-refine (from input particles an input 3Dreference and possibly a 3D mask)
_PROC_MASKCREATE_LABELNEW       "relion.maskcreate"   # Process to create masks from input maps
_PROC_JOINSTAR_LABELNEW         "relion.joinstar"     # Process to create masks from input maps
_PROC_SUBTRACT_LABELNEW         "relion.subtract"     # Process to subtract projections of parts of the reference from experimental images
_PROC_POST_LABELNEW         "relion.postprocess"  # Post-processing (from unfiltered half-maps and a possibly a 3D mask)
_PROC_RESMAP_LABELNEW           "relion.localres"     # Local resolution estimation (from unfiltered half-maps and a 3D mask)
_PROC_INIMODEL_LABELNEW       "relion.initialmodel" # De-novo generation of 3D initial model (using SGD)
_PROC_MULTIBODY_LABELNEW         "relion.multibody"    # Multi-body refinement
_PROC_MOTIONREFINE_LABELNEW     "relion.polish"       # Jasenko's motion fitting program for Bayesian polishing (to replace MovieRefine?)
_PROC_CTFREFINE_LABELNEW        "relion.ctfrefine"    # Jasenko's program for defocus and beamtilt optimisation
_PROC_DYNAMIGHT_LABELNEW        "dynamight"           # Johannes' DynaMight for modelling continuous heterogeneity
_PROC_MODELANGELO_LABELNEW      "modelangelo"         # Kiarash's ModelAngelo for automated model building
_PROC_TOMO_IMPORT_LABELNEW      "relion.importtomo"              # Import for tomography GUI
_PROC_TOMO_EXCLUDE_TILT_IMAGES_LABELNEW "relion.excludetilts"    # Exclude bad tilt-images
_PROC_TOMO_SUBTOMO_LABELNEW     "relion.pseudosubtomo"           # Creation of pseudo-subtomograms from tilt series images
_PROC_TOMO_CTFREFINE_LABELNEW   "relion.ctfrefinetomo"           # CTF refinement (defocus & aberrations) for tomography
_PROC_TOMO_ALIGN_LABELNEW       "relion.framealigntomo"          # Frame alignment and particle polishing for subtomography
_PROC_TOMO_RECONSTRUCT_LABELNEW "relion.reconstructparticletomo" # Calculation of particle average from the individual tilt series images
_PROC_TOMO_DENOISE_LABELNEW     "relion.denoisetomo"  # Denoise tomograms
_PROC_TOMO_PICK_LABELNEW        "relion.picktomo"     # Pick tomograms
_PROC_EXTERNAL_LABELNEW         "relion.external"     # For running non-relion programs
_PROC_TOMO_ALIGN_TILTSERIES_LABELNEW "relion.aligntiltseries" # ilt series alignment for tomogram reconstruction
_PROC_TOMO_RECONSTRUCT_TOMOGRAM_LABELNEW "relion.reconstructtomograms" # Reconstruction of tomograms for particle picking
#
#
_PROC_IMPORT                      0 # Import any file as a Node of a given type
_PROC_MOTIONCORR                  1 # Import any file as a Node of a given type
_PROC_CTFFIND                     2 # Estimate CTF parameters from micrographs for either entire micrographs and/or particles
_PROC_MANUALPICK                  3 # Manually pick particle coordinates from micrographs
_PROC_AUTOPICK                    4 # Automatically pick particle coordinates from micrographs their CTF and 2D references
_PROC_EXTRACT                     5 # Window particles, normalize, downsize etc from micrographs (also combine CTF into metadata file)
//_PROC_SORT                      6 # Sort particles based on their Z-scores
_PROC_CLASSSELECT                 7 # Read in model.star file and let user interactively select classes through the display (later: auto-selection as well)
_PROC_2DCLASS                     8 # 2D classification (from input particles)
_PROC_3DCLASS                     9 # 3D classification (from input 2D/3D particles an input 3D-reference and possibly a 3D mask)
_PROC_3DAUTO                     10 # 3D auto-refine (from input particles an input 3Dreference and possibly a 3D mask)
//_PROC_POLISH                   11 # Particle-polishing (from movie-particles)
_PROC_MASKCREATE                 12 # Process to create masks from input maps
_PROC_JOINSTAR                   13 # Process to create masks from input maps
_PROC_SUBTRACT                   14 # Process to subtract projections of parts of the reference from experimental images
_PROC_POST                       15 # Post-processing (from unfiltered half-maps and a possibly a 3D mask)
_PROC_RESMAP                     16 # Local resolution estimation (from unfiltered half-maps and a 3D mask)
# _PROC_MOVIEREFINE    17# Movie-particle extraction and refinement combined
_PROC_INIMODEL                   18 # De-novo generation of 3D initial model (using SGD)
_PROC_MULTIBODY                  19 # Multi-body refinement
_PROC_MOTIONREFINE               20 # Jasenko's motion_refine
_PROC_CTFREFINE                  21 # Jasenko's ctf_refine
_PROC_DYNAMIGHT                  22 # wrapper to Johannes' DynaMight
_PROC_MODELANGELO                23 # wrapper to Kiasrash's ModelAngelo
_PROC_TOMO_IMPORT                50 # Import for tomography GUI
_PROC_TOMO_SUBTOMO               51 # Creation of pseudo-subtomograms from tilt series images
_PROC_TOMO_CTFREFINE             52 # CTF refinement (defocus & aberrations for tomography)
_PROC_TOMO_ALIGN                 53 # Frame alignment and particle polishing for subtomography
_PROC_TOMO_RECONSTRUCT           54 # Calculation of particle average from the individual tilt series images
_PROC_TOMO_ALIGN_TILTSERIES      55 # ilt series alignment for tomogram reconstruction
_PROC_TOMO_RECONSTRUCT_TOMOGRAM  56 # Reconstruction of tomograms for particle picking
_PROC_TOMO_EXCLUDE_TILT_IMAGES   57 # Exclude bad tilt-images from tilt-series
_PROC_TOMO_DENOISE_TOMOGRAM      58 # Denoise tomograms
_PROC_TOMO_PICK_TOMOGRAM         59 # Denoise tomograms
_PROC_EXTERNAL                   99 # External scripts
#
# Status a Process may have
_PROC_RUNNING          0 # (hopefully) running
_PROC_SCHEDULED        1 # scheduled for future execution
_PROC_FINISHED_SUCCESS 2 # successfully finished
_PROC_FINISHED_FAILURE 3 # reported an error
_PROC_FINISHED_ABORTED 4 # aborted by the user
#
loop_
_type
_dirname
_labelnew
$PROC_IMPORT                           $PROC_IMPORT_DIRNAME                      $PROC_IMPORT_LABELNEW
$PROC_MOTIONCORR                       $PROC_MOTIONCORR_DIRNAME                  $PROC_MOTIONCORR_LABELNEW
$PROC_CTFFIND                          $PROC_CTFFIND_DIRNAME                     $PROC_CTFFIND_LABELNEW
$PROC_MANUALPICK                       $PROC_MANUALPICK_DIRNAME
$PROC_AUTOPICK                         $PROC_AUTOPICK_DIRNAME
$PROC_EXTRACT                          $PROC_EXTRACT_DIRNAME
$PROC_CLASSSELECT                      $PROC_CLASSSELECT_DIRNAME
$PROC_2DCLASS                          $PROC_2DCLASS_DIRNAME
$PROC_3DCLASS                          $PROC_3DCLASS_DIRNAME
$PROC_3DAUTO                           $PROC_3DAUTO_DIRNAME
$PROC_MASKCREATE                       $PROC_MASKCREATE_DIRNAME
$PROC_JOINSTAR                         $PROC_JOINSTAR_DIRNAME
$PROC_SUBTRACT                         $PROC_SUBTRACT_DIRNAME
$PROC_POST                             $PROC_POST_DIRNAME
$PROC_RESMAP                           $PROC_RESMAP_DIRNAME
$PROC_INIMODEL                         $PROC_INIMODEL_DIRNAME
$PROC_MULTIBODY                        $PROC_MULTIBODY_DIRNAME
$PROC_MOTIONREFINE                     $PROC_MOTIONREFINE_DIRNAME
$PROC_CTFREFINE                        $PROC_CTFREFINE_DIRNAME
$PROC_DYNAMIGHT                        $PROC_DYNAMIGHT_DIRNAME
$PROC_MODELANGELO                      $PROC_MODELANGELO_DIRNAME
$PROC_TOMO_IMPORT                      $PROC_TOMO_IMPORT_DIRNAME
$PROC_TOMO_SUBTOMO                     $PROC_TOMO_SUBTOMO_DIRNAME
$PROC_TOMO_CTFREFINE                   $PROC_TOMO_CTFREFINE_DIRNAME
$PROC_TOMO_ALIGN                       $PROC_TOMO_ALIGN_DIRNAME
$PROC_TOMO_RECONSTRUCT                 $PROC_TOMO_RECONSTRUCT_DIRNAME
$PROC_TOMO_ALIGN_TILTSERIES            $PROC_TOMO_ALIGN_TILTSERIES_DIRNAME
$PROC_TOMO_RECONSTRUCT_TOMOGRAM        $PROC_TOMO_RECONSTRUCT_TOMOGRAM_DIRNAME
$PROC_TOMO_DENOISE_TOMOGRAM            $PROC_TOMO_DENOISE_DIRNAME
$PROC_TOMO_PICK_TOMOGRAM               $PROC_TOMO_PICK_DIRNAME
$PROC_TOMO_EXCLUDE_TILT_IMAGES         $PROC_TOMO_EXCLUDE_TILT_IMAGES_DIRNAME
$PROC_EXTERNAL                         $PROC_EXTERNAL_DIRNAME
#

PROC_IMPORT, PROC_IMPORT_LABELNEW},
		{PROC_MOTIONCORR, PROC_MOTIONCORR_LABELNEW},
		{PROC_CTFFIND, PROC_CTFFIND_LABELNEW},
		{PROC_MANUALPICK, PROC_MANUALPICK_LABELNEW},
		{PROC_AUTOPICK, PROC_AUTOPICK_LABELNEW},
		{PROC_EXTRACT, PROC_EXTRACT_LABELNEW},
		{PROC_CLASSSELECT, PROC_CLASSSELECT_LABELNEW},
		{PROC_2DCLASS, PROC_2DCLASS_LABELNEW},
		{PROC_3DCLASS, PROC_3DCLASS_LABELNEW},
		{PROC_3DAUTO, PROC_3DAUTO_LABELNEW},
		{PROC_MASKCREATE,        PROC_MASKCREATE_LABELNEW},
		{PROC_JOINSTAR,        PROC_JOINSTAR_LABELNEW},
		{PROC_SUBTRACT,        PROC_SUBTRACT_LABELNEW},
		{PROC_POST,             PROC_POST_LABELNEW},
		{PROC_RESMAP,           PROC_RESMAP_LABELNEW},
		{PROC_INIMODEL,         PROC_INIMODEL_LABELNEW},
		{PROC_MULTIBODY,        PROC_MULTIBODY_LABELNEW},
		{PROC_MOTIONREFINE,     PROC_MOTIONREFINE_LABELNEW},
		{PROC_CTFREFINE,        PROC_CTFREFINE_LABELNEW},
        {PROC_DYNAMIGHT,        PROC_DYNAMIGHT_LABELNEW},
        {PROC_MODELANGELO,      PROC_MODELANGELO_LABELNEW},
		{PROC_TOMO_IMPORT,      PROC_TOMO_IMPORT_LABELNEW},
		{PROC_TOMO_SUBTOMO,     PROC_TOMO_SUBTOMO_LABELNEW},
		{PROC_TOMO_CTFREFINE,   PROC_TOMO_CTFREFINE_LABELNEW},
		{PROC_TOMO_ALIGN,       PROC_TOMO_ALIGN_LABELNEW},
		{PROC_TOMO_RECONSTRUCT, PROC_TOMO_RECONSTRUCT_LABELNEW},
        {PROC_TOMO_ALIGN_TILTSERIES,     PROC_TOMO_ALIGN_TILTSERIES_LABELNEW},
        {PROC_TOMO_RECONSTRUCT_TOMOGRAM, PROC_TOMO_RECONSTRUCT_TOMOGRAM_LABELNEW},
 	    {PROC_TOMO_DENOISE_TOMOGRAM, PROC_TOMO_DENOISE_LABELNEW},
 	    {PROC_TOMO_PICK_TOMOGRAM, PROC_TOMO_PICK_LABELNEW},
	    {PROC_TOMO_EXCLUDE_TILT_IMAGES, PROC_TOMO_EXCLUDE_TILT_IMAGES_LABELNEW},
        {PROC_EXTERNAL,         PROC_EXTERNAL_LABELNEW}};
