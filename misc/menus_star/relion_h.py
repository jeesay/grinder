"""
/***************************************************************************
 *
 * Author: "Sjors H.W. Scheres"
 * MRC Laboratory of Molecular Biology
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * This complete copyright notice must be included in any revised version of the
 * source code. Additional authorship citations may be added, but existing
 * author citations must be preserved.
 ***************************************************************************/
"""

# General nodes used for input into relion jobs have a _CPIPE suffix

LABEL_MOVIES_CPIPE = "MicrographMovieGroupMetadata.star.relion"
LABEL_MICS_CPIPE = "MicrographGroupMetadata.star.relion"
LABEL_2DIMGS_CPIPE = "Image2DGroupMetadata.star.relion"
LABEL_MAP_CPIPE = "DensityMap.mrc"
LABEL_PARTS_CPIPE = "ParticleGroupMetadata.star.relion"
LABEL_COORDS_CPIPE = "MicrographCoordsGroup.star.relion"
LABEL_COORDS_HELIX_CPIPE = "MicrographCoordsGroup.star.relion.helixstartend"
LABEL_PARTS_HELIX_CPIPE = "ParticleGroupMetadata.star.relion.helicalsegments"
LABEL_OPTIMISER_CPIPE = "OptimiserData.star.relion"
LABEL_MASK_CPIPE = "Mask3D.mrc"
LABEL_HALFMAP_CPIPE = "DensityMap.mrc.halfmap"
LABEL_RESMAP_CPIPE = "Image3D.mrc.localresmap"
LABEL_LOGFILE_CPIPE = "LogFile.pdf.relion"
LABEL_SEQUENCE_CPIPE = "Sequence.fasta"
LABEL_SEQUENCEALIGNMENT_CPIPE = "SequenceAlignment.hmm"
LABEL_ATOMCOORDS_CPIPE = "AtomCoords.cif"
LABEL_TOMO_OPTSET_CPIPE = "TomoOptimisationSet.star.relion"
LABEL_TOMOGRAMS_CPIPE = "TomogramGroupMetadata.star.relion"
LABEL_TRAJECTORIES_CPIPE = "TomoTrajectoryData.star.relion"
LABEL_MANIFOLDS_CPIPE = "TomoManifoldData.star.relion"
LABEL_POSTPROCESS_CPIPE = "ProcessData.star.relion.postprocess"

# More specific output nodes are below

LABEL_IMPORT_MOVIES = "MicrographMovieGroupMetadata.star.relion"
LABEL_IMPORT_MICS = "MicrographGroupMetadata.star.relion"
LABEL_IMPORT_COORDS = "MicrographCoordsGroup.star.relion"
LABEL_IMPORT_PARTS = "ParticleGroupMetadata.star.relion"
LABEL_IMPORT_2DIMG = "Image2DGroupMetadata.star.relion"
LABEL_IMPORT_MAP = "DensityMap.mrc"
LABEL_IMPORT_MASK = "Mask3D.mrc"
LABEL_IMPORT_HALFMAP = "DensityMap.mrc.halfmap"
LABEL_MOCORR_MICS = "MicrographGroupMetadata.star.relion.motioncorr"
LABEL_MOCORR_LOG = "LogFile.pdf.relion.motioncorr"
LABEL_CTFFIND_MICS = "MicrographGroupMetadata.star.relion.ctf"
LABEL_CTFFIND_LOG = "LogFile.pdf.relion.ctffind"
LABEL_CTFFIND_POWER_SPECTRA = "Image2DGroupMetadata.star.relion.ctffind.power_spectra"
LABEL_MANPICK_MICS = "MicrographGroupMetadata.star.relion"
LABEL_MANPICK_COORDS = "MicrographCoordsGroup.star.relion.manualpick"
LABEL_MANPICK_COORDS_HELIX = "MicrographCoordsGroup.star.relion.manualpick.helixstartend"
LABEL_AUTOPICK_COORDS = "MicrographCoordsGroup.star.relion.autopick"
LABEL_AUTOPICK_LOG = "LogFile.pdf.relion.autopick"
LABEL_AUTOPICK_TOPAZMODEL = "ParamsData.sav.topaz.model" # to be added?
LABEL_AUTOPICK_MICS = "MicrographGroupMetadata.star.relion"
LABEL_EXTRACT_PARTS = "ParticleGroupMetadata.star.relion"
LABEL_EXTRACT_PARTS_HELIX = "ParticleGroupMetadata.star.relion.helicalsegments"
LABEL_EXTRACT_COORDS_HELIX = "MicrographCoordsGroup.star.relion.helixstartend"
LABEL_EXTRACT_PARTS_REEX = "ParticleGroupMetadata.star.relion.reextract"
LABEL_EXTRACT_COORDS_REEX = "MicrographCoordsGroup.star.relion.reextract"
LABEL_CLASS2D_PARTS = "ParticleGroupMetadata.star.relion.class2d"
LABEL_CLASS2D_OPT = "OptimiserData.star.relion.class2d"
LABEL_CLASS2D_PARTS_HELIX = "ParticleGroupMetadata.star.relion.class2d.helicalsegments"
LABEL_SELECT_MICS = "MicrographGroupMetadata.star.relion"
LABEL_SELECT_MOVS = "MicrographMovieGroupMetadata.star.relion"
LABEL_SELECT_PARTS = "ParticleGroupMetadata.star.relion"
LABEL_SELECT_OPT = "OptimiserData.star.relion.select"
LABEL_SELECT_CLAVS = "Image2DGroupMetadata.star.relion.classaverages"
LABEL_SELECT_LOG = "LogFile.pdf.relion.select"
LABEL_INIMOD_MAP = "DensityMap.mrc.relion.initialmodel"
LABEL_INIMOD_OPTSET = "TomoOptimisationSet.star.relion.initialmodel"
LABEL_CLASS3D_OPT = "OptimiserData.star.relion.class3d"
LABEL_CLASS3D_MAP = "DensityMap.mrc.relion.class3d"
LABEL_CLASS3D_PARTS = "ParticleGroupMetadata.star.relion.class3d"
LABEL_CLASS3D_PARTS_HELIX = "ParticleGroupMetadata.star.relion.class3d.helicalsegments"
LABEL_CLASS3D_OPTSET = "TomoOptimisationSet.star.relion.class3d"
LABEL_REFINE3D_HALFMAP = "DensityMap.mrc.relion.halfmap.refine3d"
LABEL_REFINE3D_OPT = "OptimiserData.star.relion.refine3d"
LABEL_REFINE3D_MAP = "DensityMap.mrc.relion.refine3d"
LABEL_REFINE3D_PARTS = "ParticleGroupMetadata.star.relion.refine3d"
LABEL_REFINE3D_PARTS_HELIX = "ParticleGroupMetadata.star.relion.refine3d.helicalsegements"
LABEL_REFINE3D_OPTSET = "TomoOptimisationSet.star.relion.refine3d"
LABEL_MULTIBODY_HALFMAP = "DensityMap.mrc.relion.halfmap.multibody"
LABEL_MULTIBODY_PARTS = "ParticleGroupMetadata.star.relion.multibody"
LABEL_MULTIBODY_OPT = "OptimiserData.star.relion.multibody"
LABEL_MULTIBODY_FLEXLOG = "LogFile.pdf.relion.flexanalysis"
LABEL_MULTIBODY_SEL_PARTS = "ParticleGroupMetadata.star.relion.flexanalysis.eigenselected"
LABEL_MULTIBODY_OPTSET = "TomoOptimisationSet.star.relion.multibody"
LABEL_DYNAMIGHT_HALFMAP = "DensityMap.mrc.relion.halfmap.dynamight"
LABEL_MASK3D_MASK = "Mask3D.mrc.relion"
LABEL_SUBTRACT_SUBTRACTED = "ParticleGroupMetadata.star.relion.subtracted"
LABEL_SUBTRACT_REVERTED = "ParticleGroupMetadata.star.relion"
LABEL_LOCRES_OWN = "Image3D.mrc.relion.localresmap"
LABEL_LOCRES_RESMAP = "Image3D.mrc.resmap.localresmap"
LABEL_LOCRES_FILTMAP = "DensityMap.mrc.relion.localresfiltered"
LABEL_LOCRES_LOG = "LogFile.pdf.relion.localres"
LABEL_CTFREFINE_REFINEPARTS = "ParticleGroupMetadata.star.relion.ctfrefine"
LABEL_CTFREFINE_LOG = "LogFile.pdf.relion.ctfrefine"
LABEL_CTFREFINE_ANISOPARTS = "ParticleGroupMetadata.star.relion.anisomagrefine"
LABEL_POLISH_PARTS = "ParticleGroupMetadata.star.relion.polished"
LABEL_POLISH_LOG = "LogFile.pdf.relion.polish"
LABEL_POLISH_PARAMS = "ParamsData.txt.relion.polish"
LABEL_POST_POST = "ProcessData.star.relion.postprocess"
LABEL_POST_MAP = "DensityMap.mrc.relion.postprocess"
LABEL_POST_MASKED = "DensityMap.mrc.relion.postprocess.masked"
LABEL_POST_LOG = "LogFile.pdf.relion.postprocess"

# Tomography-specific jobs
LABEL_IMPORT_TOMOGRAMS = "TomogramGroupMetadata.star.relion.tomo.import"
LABEL_IMPORT_TOMO_COORDS = "ParticleGroupMetadata.star.relion.tomo.import"
LABEL_MOCORR_TOMOGRAMS = "TomogramGroupMetadata.star.relion.tomo.motioncorr"
LABEL_CTFFIND_TOMOGRAMS = "TomogramGroupMetadata.star.relion.tomo.ctffind"
LABEL_TILTALIGN_TOMOGRAMS = "TomogramGroupMetadata.star.relion.tomo.aligntiltseries"
LABEL_TILTALIGN_LOG = "LogFile.pdf.relion.tomo.aligntiltseries"
LABEL_RECONSTRUCT_TOMOGRAMS = "TomogramGroupMetadata.star.relion.tomo.reconstruct"
LABEL_DENOISE_TOMOGRAMS = "TomogramGroupMetadata.star.relion.tomo.denoise"
LABEL_TOMOPICK_PARTS_PARTS = "ParticleGroupMetadata.star.relion.tomo.manualpick.particles"
LABEL_TOMOPICK_PARTS_SPHERE = "ParticleGroupMetadata.star.relion.tomo.manualpick.spheres"
LABEL_TOMOPICK_PARTS_FILAMENT = "ParticleGroupMetadata.star.relion.tomo.manualpick.filaments"
LABEL_TOMOPICK_PARTS_SURFACE = "ParticleGroupMetadata.star.relion.tomo.manualpick.surfaces"
LABEL_TOMOPICK_OPTSET = "TomoOptimisationSet.star.relion.tomo.manualpick"
LABEL_EXCLUDE_TOMOGRAMS = "TomogramGroupMetadata.star.relion.tomo.excludeimages"
LABEL_SUBTOMO_PARTS = "ParticleGroupMetadata.star.relion.tomo.extract"
LABEL_SUBTOMO_OPTSET = "TomoOptimisationSet.star.relion.tomo.extract"
LABEL_CTFREFINE_TOMOGRAMS = "TomogramGroupMetadata.star.relion.tomo.ctfrefine"
LABEL_CTFREFINE_OPTSET = "TomoOptimisationSet.star.relion.tomo.ctfrefine"
LABEL_CTFREFINE_TOMO_LOG = "LogFile.pdf.relion.tomo.ctfrefine"
LABEL_FRAMEALIGN_TOMOGRAMS = "TomogramGroupMetadata.star.relion.tomo.polish"
LABEL_FRAMEALIGN_OPTSET = "TomoOptimisationSet.star.relion.tomo.polish"
LABEL_FRAMEALIGN_LOG = "LogFile.pdf.relion.tomo.polish"
LABEL_FRAMEALIGN_PARTS = "ParticleGroupMetadata.star.relion.tomo.polish"
LABEL_FRAMEALIGN_TRAJS = "TomoTrajectoryData.star.relion.polish"
LABEL_RECONSPART_OPTSET = "TomoOptimisationSet.star.relion.tomo.reconstruct"
LABEL_RECONSPART_HALFMAP = "DensityMap.mrc.relion.tomo.halfmap.reconstruct"
LABEL_RECONSPART_MAP = "DensityMap.mrc.relion.tomo.map.reconstruct" # All the directory names of the different types of jobs defined inside the pipeline

PROC_IMPORT_DIRNAME = "Import"       # Import any file as a Node of a given type
PROC_MOTIONCORR_DIRNAME = "MotionCorr"   # Import any file as a Node of a given type
PROC_CTFFIND_DIRNAME = "CtfFind"         # Estimate CTF parameters from micrographs for either entire micrographs and/or particles
PROC_MANUALPICK_DIRNAME = "ManualPick"   # Manually pick particle coordinates from micrographs
PROC_AUTOPICK_DIRNAME = "AutoPick"     # Automatically pick particle coordinates from micrographs, their CTF and 2D references
PROC_EXTRACT_DIRNAME = "Extract"      # Window particles, normalize, downsize etc from micrographs (also combine CTF into metadata file)
PROC_CLASSSELECT_DIRNAME = "Select"        # Read in model.star file, and let user interactively select classes through the display (later: auto-selection as well)
PROC_2DCLASS_DIRNAME = "Class2D"      # 2D classification (from input particles)
PROC_3DCLASS_DIRNAME = "Class3D"      # 3D classification (from input 2D/3D particles, an input 3D-reference, and possibly a 3D mask)
PROC_3DAUTO_DIRNAME = "Refine3D"     # 3D auto-refine (from input particles, an input 3Dreference, and possibly a 3D mask)
PROC_MASKCREATE_DIRNAME = "MaskCreate"   # Process to create masks from input maps
PROC_JOINSTAR_DIRNAME = "JoinStar"     # Process to create masks from input maps
PROC_SUBTRACT_DIRNAME = "Subtract"     # Process to subtract projections of parts of the reference from experimental images
PROC_POST_DIRNAME = "PostProcess"  # Post-processing (from unfiltered half-maps and a possibly a 3D mask)
PROC_RESMAP_DIRNAME  =  "LocalRes" # Local resolution estimation (from unfiltered half-maps and a 3D mask)
PROC_INIMODEL_DIRNAME  =  "InitialModel" # De-novo generation of 3D initial model (using SGD)
PROC_MULTIBODY_DIRNAME = "MultiBody"    # Multi-body refinement
PROC_MOTIONREFINE_DIRNAME = "Polish"       # Jasenko's motion fitting program for Bayesian polishing (to replace MovieRefine?)
PROC_CTFREFINE_DIRNAME = "CtfRefine"    # Jasenko's program for defocus and beamtilt optimisation
PROC_DYNAMIGHT_DIRNAME = "DynaMight"    # Johannes' DynaMight for modelling continuous heterogeneity
PROC_MODELANGELO_DIRNAME = "ModelAngelo"  # Kiarash's ModelAngelo for automated model building
PROC_TOMO_IMPORT_DIRNAME  = "Import"  # Import for tomography GUI
PROC_TOMO_SUBTOMO_DIRNAME = "Extract"  # Creation of pseudo-subtomograms from tilt series images
PROC_TOMO_CTFREFINE_DIRNAME = "CtfRefine"  # CTF refinement (defocus & aberrations) for tomography
PROC_TOMO_EXCLUDE_TILT_IMAGES_DIRNAME  = "ExcludeTiltImages"  # Exclusion of bad tilt-images from tilt-series
PROC_TOMO_ALIGN_DIRNAME = "Polish"  # Frame alignment and particle polishing for subtomography
PROC_TOMO_RECONSTRUCT_DIRNAME = "Reconstruct" # Calculation of particle average from the individual tilt series images
PROC_TOMO_DENOISE_DIRNAME = "Denoise" # Denoise tomograms
PROC_TOMO_PICK_DIRNAME = "Picks" # Pick particles in tomograms
PROC_EXTERNAL_DIRNAME =  "External"  # For running non-relion programs
PROC_TOMO_ALIGN_TILTSERIES_DIRNAME = "AlignTiltSeries" # Tilt series alignment for tomogram reconstruction
PROC_TOMO_RECONSTRUCT_TOMOGRAM_DIRNAME = "Tomograms" # Reconstruction of tomograms for particle picking

# All the directory names of the different types of jobs defined inside the pipeline
PROC_IMPORT_LABELNEW = "relion.import"       # Import any file as a Node of a given type
PROC_MOTIONCORR_LABELNEW = "relion.motioncorr"   # Import any file as a Node of a given type
PROC_CTFFIND_LABELNEW = "relion.ctffind"         # Estimate CTF parameters from micrographs for either entire micrographs and/or particles
PROC_MANUALPICK_LABELNEW = "relion.manualpick"   # Manually pick particle coordinates from micrographs
PROC_AUTOPICK_LABELNEW = "relion.autopick"     # Automatically pick particle coordinates from micrographs, their CTF and 2D references
PROC_EXTRACT_LABELNEW = "relion.extract"      # Window particles, normalize, downsize etc from micrographs (also combine CTF into metadata file)
PROC_CLASSSELECT_LABELNEW = "relion.select"        # Read in model.star file, and let user interactively select classes through the display (later: auto-selection as well)
PROC_2DCLASS_LABELNEW = "relion.class2d"      # 2D classification (from input particles)
PROC_3DCLASS_LABELNEW = "relion.class3d"      # 3D classification (from input 2D/3D particles, an input 3D-reference, and possibly a 3D mask)
PROC_3DAUTO_LABELNEW = "relion.refine3d"     # 3D auto-refine (from input particles, an input 3Dreference, and possibly a 3D mask)
PROC_MASKCREATE_LABELNEW = "relion.maskcreate"   # Process to create masks from input maps
PROC_JOINSTAR_LABELNEW = "relion.joinstar"     # Process to create masks from input maps
PROC_SUBTRACT_LABELNEW = "relion.subtract"     # Process to subtract projections of parts of the reference from experimental images
PROC_POST_LABELNEW = "relion.postprocess"  # Post-processing (from unfiltered half-maps and a possibly a 3D mask)
PROC_RESMAP_LABELNEW = "relion.localres"  # Local resolution estimation (from unfiltered half-maps and a 3D mask)
PROC_INIMODEL_LABELNEW = "relion.initialmodel" # De-novo generation of 3D initial model (using SGD)
PROC_MULTIBODY_LABELNEW = "relion.multibody"    # Multi-body refinement
PROC_MOTIONREFINE_LABELNEW = "relion.polish"       # Jasenko's motion fitting program for Bayesian polishing (to replace MovieRefine?)
PROC_CTFREFINE_LABELNEW = "relion.ctfrefine"    # Jasenko's program for defocus and beamtilt optimisation
PROC_DYNAMIGHT_LABELNEW = "dynamight"           # Johannes' DynaMight for modelling continuous heterogeneity
PROC_MODELANGELO_LABELNEW = "modelangelo"         # Kiarash's ModelAngelo for automated model building
PROC_TOMO_IMPORT_LABELNEW = "relion.importtomo"              # Import for tomography GUI
PROC_TOMO_EXCLUDE_TILT_IMAGES_LABELNEW = "relion.excludetilts"  # Exclude bad tilt-images
PROC_TOMO_SUBTOMO_LABELNEW = "relion.pseudosubtomo"  # Creation of pseudo-subtomograms from tilt series images
PROC_TOMO_CTFREFINE_LABELNEW  = "relion.ctfrefinetomo"  # CTF refinement (defocus & aberrations) for tomography
PROC_TOMO_ALIGN_LABELNEW  = "relion.framealigntomo"  # Frame alignment and particle polishing for subtomography
PROC_TOMO_RECONSTRUCT_LABELNEW = "relion.reconstructparticletomo" # Calculation of particle average from the individual tilt series images
PROC_TOMO_DENOISE_LABELNEW = "relion.denoisetomo"  # Denoise tomograms
PROC_TOMO_PICK_LABELNEW = "relion.picktomo"     # Pick tomograms
PROC_EXTERNAL_LABELNEW = "relion.external"     # For running non-relion programs
PROC_TOMO_ALIGN_TILTSERIES_LABELNEW = "relion.aligntiltseries" # Tilt series alignment for tomogram reconstruction
PROC_TOMO_RECONSTRUCT_TOMOGRAM_LABELNEW = "relion.reconstructtomograms" # Reconstruction of tomograms for particle picking = PROC_IMPORT = 0 # Import any file as a Node of a given type

PROC_IMPORT = 0 #  Import any file as a Node of a given type
PROC_MOTIONCORR = 1 # Import any file as a Node of a given type
PROC_CTFFIND = 2 # Estimate CTF parameters from micrographs for either entire micrographs and/or particles
PROC_MANUALPICK = 3 # Manually pick particle coordinates from micrographs
PROC_AUTOPICK = 4 # Automatically pick particle coordinates from micrographs, their CTF and 2D references
PROC_EXTRACT = 5 # Window particles, normalize, downsize etc from micrographs (also combine CTF into metadata file)
#PROC_SORT = 6 # Sort particles based on their Z-scores
PROC_CLASSSELECT = 7 # Read in model.star file, and let user interactively select classes through the display (later: auto-selection as well)
PROC_2DCLASS = 8 # 2D classification (from input particles)
PROC_3DCLASS = 9 # 3D classification (from input 2D/3D particles, an input 3D-reference, and possibly a 3D mask)
PROC_3DAUTO = 10 # 3D auto-refine (from input particles, an input 3Dreference, and possibly a 3D mask)
#PROC_POLISH = 11 # Particle-polishing (from movie-particles)
PROC_MASKCREATE = 12 # Process to create masks from input maps
PROC_JOINSTAR = 13 # Process to create masks from input maps
PROC_SUBTRACT = 14 # Process to subtract projections of parts of the reference from experimental images
PROC_POST = 15 # Post-processing (from unfiltered half-maps and a possibly a 3D mask)
PROC_RESMAP = 16 # Local resolution estimation (from unfiltered half-maps and a 3D mask)
#PROC_MOVIEREFINE = 17 # Movie-particle extraction and refinement combined
PROC_INIMODEL = 18 # De-novo generation of 3D initial model (using SGD)
PROC_MULTIBODY = 19 # Multi-body refinement
PROC_MOTIONREFINE = 20 # Jasenko's motion_refine
PROC_CTFREFINE = 21 # Jasenko's ctf_refine
PROC_DYNAMIGHT = 22 # wrapper to Johannes' DynaMight
PROC_MODELANGELO = 23 # wrapper to Kiasrash's ModelAngelo
PROC_TOMO_IMPORT = 50 # Import for tomography GUI
PROC_TOMO_SUBTOMO = 51 # Creation of pseudo-subtomograms from tilt series images
PROC_TOMO_CTFREFINE = 52 # CTF refinement (defocus & aberrations for tomography)
PROC_TOMO_ALIGN = 53 # Frame alignment and particle polishing for subtomography
PROC_TOMO_RECONSTRUCT = 54 # Calculation of particle average from the individual tilt series images
PROC_TOMO_ALIGN_TILTSERIES = 55 # Tilt series alignment for tomogram reconstruction
PROC_TOMO_RECONSTRUCT_TOMOGRAM = 56 # Reconstruction of tomograms for particle picking
PROC_TOMO_EXCLUDE_TILT_IMAGES = 57 # Exclude bad tilt-images from tilt-series
PROC_TOMO_DENOISE_TOMOGRAM = 58 # Denoise tomograms
PROC_TOMO_PICK_TOMOGRAM = 59 # Denoise tomograms
PROC_EXTERNAL = 99 # External scripts

JOBOPTION_UNDEFINED = 0
JOBOPTION_ANY = 1
JOBOPTION_FILENAME = 2
JOBOPTION_INPUTNODE = 3
JOBOPTION_RADIO = 4
JOBOPTION_BOOLEAN = 5
JOBOPTION_SLIDER = 6
JOBOPTION_ONLYTEXT = 7


def proc_type2dirname(x):
    return {
    PROC_IMPORT:                    PROC_IMPORT_DIRNAME,
	PROC_MOTIONCORR:                PROC_MOTIONCORR_DIRNAME,
	PROC_CTFFIND:                   PROC_CTFFIND_DIRNAME,
	PROC_MANUALPICK:                PROC_MANUALPICK_DIRNAME,
	PROC_AUTOPICK:                  PROC_AUTOPICK_DIRNAME,
	PROC_EXTRACT:                   PROC_EXTRACT_DIRNAME,
	PROC_CLASSSELECT:               PROC_CLASSSELECT_DIRNAME,
	PROC_2DCLASS:                   PROC_2DCLASS_DIRNAME,
	PROC_3DCLASS:                   PROC_3DCLASS_DIRNAME,
	PROC_3DAUTO:                    PROC_3DAUTO_DIRNAME,
	PROC_MASKCREATE:                PROC_MASKCREATE_DIRNAME,
	PROC_JOINSTAR:                  PROC_JOINSTAR_DIRNAME,
	PROC_SUBTRACT:                  PROC_SUBTRACT_DIRNAME,
	PROC_POST:                      PROC_POST_DIRNAME,
	PROC_RESMAP:                    PROC_RESMAP_DIRNAME,
	PROC_INIMODEL:                  PROC_INIMODEL_DIRNAME,
	PROC_MULTIBODY:                 PROC_MULTIBODY_DIRNAME,
	PROC_MOTIONREFINE:              PROC_MOTIONREFINE_DIRNAME,
	PROC_CTFREFINE:                 PROC_CTFREFINE_DIRNAME,
	PROC_DYNAMIGHT:                 PROC_DYNAMIGHT_DIRNAME,
	PROC_MODELANGELO:               PROC_MODELANGELO_DIRNAME,
	PROC_TOMO_IMPORT:               PROC_TOMO_IMPORT_DIRNAME,
	PROC_TOMO_SUBTOMO:              PROC_TOMO_SUBTOMO_DIRNAME,
	PROC_TOMO_CTFREFINE:            PROC_TOMO_CTFREFINE_DIRNAME,
	PROC_TOMO_ALIGN:                PROC_TOMO_ALIGN_DIRNAME,
	PROC_TOMO_RECONSTRUCT:          PROC_TOMO_RECONSTRUCT_DIRNAME,
	PROC_TOMO_ALIGN_TILTSERIES:     PROC_TOMO_ALIGN_TILTSERIES_DIRNAME,
	PROC_TOMO_RECONSTRUCT_TOMOGRAM: PROC_TOMO_RECONSTRUCT_TOMOGRAM_DIRNAME,
	PROC_TOMO_DENOISE_TOMOGRAM:     PROC_TOMO_DENOISE_DIRNAME,
	PROC_TOMO_PICK_TOMOGRAM:        PROC_TOMO_PICK_DIRNAME,
	PROC_TOMO_EXCLUDE_TILT_IMAGES:  PROC_TOMO_EXCLUDE_TILT_IMAGES_DIRNAME,
	PROC_EXTERNAL:                  PROC_EXTERNAL_DIRNAME}[x]

proc_grinder_settings = {
    'PROC_IMPORT_RAW_GRR'          : ("import_mov", "'Import movies'", "radio_tool", PROC_IMPORT,PROC_IMPORT_LABELNEW + ".raw", "'Import Micrographs or Movies'", "01.star"),
	'PROC_IMPORT_PARTICLES_GRR'    : ("import_ptcls", "'Import particles'", "radio_tool", PROC_IMPORT,PROC_IMPORT_LABELNEW + ".other", "'Import Particles'", "02.star"),
	'PROC_IMPORT_OTHER_GRR'        : ("import_other", "'Import other files'", "radio_tool", PROC_IMPORT, PROC_IMPORT_LABELNEW + ".other", "'Import Other File'", "03.star"),
	'PROC_MOTIONCORR_OWN_GRR'      : ("motioncor", "'Motion Correction'", "radio_tool", PROC_MOTIONCORR,PROC_MOTIONCORR_LABELNEW + ".own", "'RELIONs own implementation'", "01.star"), 
	'PROC_MOTIONCORR_MC2_GRR'      : ("motioncor2", "'Motion Correction2'", "radio_tool", PROC_MOTIONCORR, PROC_MOTIONCORR_LABELNEW + ".motioncor2", "'MotionCorr executable'", "02.star"), 
    'PROC_CTFFIND' 				   : ("ctf", "CTF with CTFFIND 4.1", "radio_tool", PROC_CTFFIND,PROC_CTFFIND_LABELNEW, "CTF with CTFFIND 4.1", "03.star"),

	# A FAIRE
	
	'PROC_MANUALPICK':(PROC_MANUALPICK,PROC_MANUALPICK_DIRNAME,PROC_MANUALPICK_LABELNEW),
	'PROC_AUTOPICK':(PROC_AUTOPICK,PROC_AUTOPICK_DIRNAME,PROC_AUTOPICK_LABELNEW),
	'PROC_EXTRACT':(PROC_EXTRACT,PROC_EXTRACT_DIRNAME,PROC_EXTRACT_LABELNEW),
	'PROC_CLASSSELECT':(PROC_CLASSSELECT,PROC_CLASSSELECT_DIRNAME,PROC_CLASSSELECT_LABELNEW),
	'PROC_2DCLASS':(PROC_2DCLASS,PROC_2DCLASS_DIRNAME,PROC_2DCLASS_LABELNEW),
	'PROC_3DCLASS':(PROC_3DCLASS,PROC_3DCLASS_DIRNAME,PROC_3DCLASS_LABELNEW),
	'PROC_3DAUTO':(PROC_3DAUTO,PROC_3DAUTO_DIRNAME,PROC_3DAUTO_LABELNEW),
	'PROC_MASKCREATE':(PROC_MASKCREATE,PROC_MASKCREATE_DIRNAME,PROC_MASKCREATE_LABELNEW),
	'PROC_JOINSTAR':(PROC_JOINSTAR,PROC_JOINSTAR_DIRNAME,PROC_JOINSTAR_LABELNEW),
	'PROC_SUBTRACT':(PROC_SUBTRACT,PROC_SUBTRACT_DIRNAME,PROC_SUBTRACT_LABELNEW),
	'PROC_POST':(PROC_POST,PROC_POST_DIRNAME,PROC_POST_LABELNEW),
	'PROC_RESMAP':(PROC_RESMAP,PROC_RESMAP_DIRNAME,PROC_RESMAP_LABELNEW),
	'PROC_INIMODEL':(PROC_INIMODEL,PROC_INIMODEL_DIRNAME,PROC_INIMODEL_LABELNEW),
	'PROC_MULTIBODY':(PROC_MULTIBODY,PROC_MULTIBODY_DIRNAME,PROC_MULTIBODY_LABELNEW),
	'PROC_MOTIONREFINE':(PROC_MOTIONREFINE,PROC_MOTIONREFINE_DIRNAME,PROC_MOTIONREFINE_LABELNEW),
	'PROC_CTFREFINE':(PROC_CTFREFINE,PROC_CTFREFINE_DIRNAME,PROC_CTFREFINE_LABELNEW),
	'PROC_DYNAMIGHT':(PROC_DYNAMIGHT,PROC_DYNAMIGHT_DIRNAME,PROC_DYNAMIGHT_LABELNEW),
	'PROC_MODELANGELO':(PROC_MODELANGELO,PROC_MODELANGELO_DIRNAME,PROC_MODELANGELO_LABELNEW),
    
	# TOMO
	'PROC_TOMO_IMPORT':(PROC_TOMO_IMPORT,PROC_TOMO_IMPORT_DIRNAME,PROC_TOMO_IMPORT_LABELNEW),
	'PROC_TOMO_SUBTOMO':(PROC_TOMO_SUBTOMO,PROC_TOMO_SUBTOMO_DIRNAME,PROC_TOMO_SUBTOMO_LABELNEW),
	'PROC_TOMO_CTFREFINE':(PROC_TOMO_CTFREFINE,PROC_TOMO_CTFREFINE_DIRNAME,PROC_TOMO_CTFREFINE_LABELNEW),
	'PROC_TOMO_ALIGN':(PROC_TOMO_ALIGN,PROC_TOMO_ALIGN_DIRNAME,PROC_TOMO_ALIGN_LABELNEW),
	'PROC_TOMO_RECONSTRUCT':(PROC_TOMO_RECONSTRUCT,PROC_TOMO_RECONSTRUCT_DIRNAME,PROC_TOMO_RECONSTRUCT_LABELNEW),
	'PROC_TOMO_ALIGN_TILTSERIES':(PROC_TOMO_ALIGN_TILTSERIES,PROC_TOMO_ALIGN_TILTSERIES_DIRNAME,PROC_TOMO_ALIGN_TILTSERIES_LABELNEW),
	'PROC_TOMO_RECONSTRUCT_TOMOGRAM':(PROC_TOMO_RECONSTRUCT_TOMOGRAM,PROC_TOMO_RECONSTRUCT_TOMOGRAM_DIRNAME,PROC_TOMO_RECONSTRUCT_TOMOGRAM_LABELNEW),
	'PROC_TOMO_EXCLUDE_TILT_IMAGES':(PROC_TOMO_EXCLUDE_TILT_IMAGES,PROC_TOMO_EXCLUDE_TILT_IMAGES_DIRNAME,PROC_TOMO_EXCLUDE_TILT_IMAGES_LABELNEW),
	'PROC_TOMO_DENOISE_TOMOGRAM':(PROC_TOMO_DENOISE_TOMOGRAM,PROC_TOMO_DENOISE_DIRNAME,PROC_TOMO_DENOISE_LABELNEW),
	'PROC_TOMO_PICK_TOMOGRAM':(PROC_TOMO_PICK_TOMOGRAM,PROC_TOMO_PICK_DIRNAME,PROC_TOMO_PICK_LABELNEW),
	'PROC_EXTERNAL':(PROC_EXTERNAL,PROC_EXTERNAL_DIRNAME,PROC_EXTERNAL_LABELNEW)
}

job_sampling_options = [
    ("30 degrees",0),
    ("15 degrees",1),
    ("7.5 degrees",2),
    ("3.7 degrees",3),
    ("1.8 degrees",4),
    ("0.9 degrees",5),
    ("0.5 degrees",6),
    ("0.2 degrees",7),
    ("0.1 degrees",8)
]

# job_nodetype_options = [
#     ("Particle coordinates (*.box, *_pick.star)","LABEL_IMPORT_COORDS"),
#     ("Particles STAR file (.star)","LABEL_IMPORT_PARTS"),
#     ("Multiple (2D or 3D) references (.star or .mrcs)","LABEL_IMPORT_2DIMG"),
#     ("Micrographs STAR file (.star)","LABEL_IMPORT_MICS"),
#     ("3D reference (.mrc)","LABEL_IMPORT_MAP"),
#     ("3D mask (.mrc)","LABEL_IMPORT_MASK"),
#     ("Unfiltered half-map (unfil.mrc)","LABEL_IMPORT_HALFMAP")
# ]

job_nodetype_options_particles = [
    ("Particle coordinates (*.box, *_pick.star)","LABEL_IMPORT_COORDS"),
    ("Particles STAR file (.star)","LABEL_IMPORT_PARTS")
]

job_nodetype_options_other = [
    ("Multiple (2D or 3D) references (.star or .mrcs)","LABEL_IMPORT_2DIMG"),
    ("Micrographs STAR file (.star)","LABEL_IMPORT_MICS"),
    ("3D reference (.mrc)","LABEL_IMPORT_MAP"),
    ("3D mask (.mrc)","LABEL_IMPORT_MASK"),
    ("Unfiltered half-map (unfil.mrc)","LABEL_IMPORT_HALFMAP")
]

job_nodetype_options_tomo = [
    "Set of tomograms STAR file (.star)",
    "Set of tiltseries STAR file (.star)",
    "Particles STAR file (.star)",
    "Multiple (2D or 3D) references (.star or .mrcs)",
    "3D reference (.mrc)",
    "3D mask (.mrc)",
    "Unfiltered half-map (unfil.mrc)"
]

job_gain_rotation_options = [
    ("No rotation",0), 
    ("90 degrees",1), 
    ("180 degrees",2), 
    ("270 degrees",3)
]

job_gain_flip_options = [
    ("No flipping",0), 
    ("Flip upside down",1), 
    ("Flip left to right",2)
]

job_ctffit_options = [
    ("No", 0),
    ("Per-micrograph", 1),
    ("Per-particle", 2)
]

job_tomo_align_shiftonly_options = [
    "Entire micrographs",
    "Only particles"
]

job_tomo_align_def_model = [
    "linear",
    "spline",
    "Fourier"
]

job_tomo_pick_mode = [
    "particles",
    "spheres",
    "surfaces",
    "filaments"
]

job_modelangelo_alphabet_options = [
    ("amino", 0),
    ("DNA", 1),
    ("RNA", 2)
]

# GRINDER Labels
PROC_IMPORT_RAW_GRR          = PROC_IMPORT_LABELNEW + ".raw"
PROC_IMPORT_OTHER_GRR        = PROC_IMPORT_LABELNEW + ".other"
PROC_PROC_MOTIONCORR_OWN_GRR = PROC_MOTIONCORR_LABELNEW + ".own"
PROC_PROC_MOTIONCORR_MC2_GRR = PROC_MOTIONCORR_LABELNEW + ".motioncor2"
PROC_CTFFIND_GRR             = PROC_CTFFIND_LABELNEW
PROC_MANUALPICK_GRR          = PROC_MANUALPICK_LABELNEW
PROC_AUTOPICK_LOG_GRR        = PROC_AUTOPICK_LABELNEW + ".log"
PROC_AUTOPICK_TOPAZ_GRR      = PROC_AUTOPICK_LABELNEW + '.topaz'
PROC_AUTOPICK_TOPAZTRAIN_GRR = PROC_AUTOPICK_LABELNEW + '.train'
PROC_AUTOPICK_TOPAZPICK_GRR  = PROC_AUTOPICK_LABELNEW + '.topaz.pick'
PROC_AUTOPICK_REF3D_GRR      = PROC_AUTOPICK_LABELNEW + '.ref3d'
PROC_AUTOPICK_REF2D_GRR      = PROC_AUTOPICK_LABELNEW + '.ref2d'
PROC_EXTRACT_GRR             = PROC_EXTRACT_LABELNEW
PROC_EXTRACT_RE_GRR          = PROC_EXTRACT_LABELNEW + ".reextract"
PROC_CLASSSELECT_GRR         = PROC_CLASSSELECT_LABELNEW
PROC_CLASSSELECT_DUPL_GRR    = PROC_CLASSSELECT_LABELNEW + ".removeduplicates"
PROC_CLASSSELECT_DSCRD_GRR   = PROC_CLASSSELECT_LABELNEW + ".discard"
PROC_CLASSSELECT_ONVAL_GRR   = PROC_CLASSSELECT_LABELNEW + ".onvalue"
PROC_CLASSSELECT_SPLIT_GRR   = PROC_CLASSSELECT_LABELNEW + ".split"
PROC_CLASSSELECT_RANK_GRR    = PROC_CLASSSELECT_LABELNEW + ".class2dauto"
PROC_CLASSSELECT_MAN_GRR     = PROC_CLASSSELECT_LABELNEW + ".interactive"
PROC_2DCLASS_GRR             = PROC_2DCLASS_LABELNEW
PROC_3DCLASS_GRR             = PROC_3DCLASS_LABELNEW
PROC_3DAUTO_GRR              = PROC_3DAUTO_LABELNEW
PROC_MASKCREATE_GRR          = PROC_MASKCREATE_LABELNEW
PROC_JOINSTAR_GRR            = PROC_JOINSTAR_LABELNEW
PROC_SUBTRACT_GRR            = PROC_SUBTRACT_LABELNEW
PROC_POST_GRR                = PROC_POST_LABELNEW
PROC_RESMAP_GRR              = PROC_RESMAP_LABELNEW
PROC_INIMODEL_GRR            = PROC_INIMODEL_LABELNEW
PROC_MULTIBODY_GRR           = PROC_MULTIBODY_LABELNEW
PROC_MOTIONREFINE_GRR        = PROC_MOTIONREFINE_LABELNEW
PROC_CTFREFINE_GRR           = PROC_CTFREFINE_LABELNEW
PROC_DYNAMIGHT_GRR           = PROC_DYNAMIGHT_LABELNEW
PROC_MODELANGELO_GRR         = PROC_MODELANGELO_LABELNEW
# Helical
PROC_EXTRACT_HLX_GRR         = PROC_EXTRACT_LABELNEW + ".helical"
PROC_2DCLASS_HLX_GRR         = PROC_2DCLASS_LABELNEW + ".helical"
PROC_3DCLASS_HLX_GRR         = PROC_3DCLASS_LABELNEW + ".helical"
# Tomo
PROC_INIMODEL_TOMO_GRR       = PROC_INIMODEL_LABELNEW + ".tomo"
PROC_3DAUTO_TOMO_GRR         = PROC_3DAUTO_LABELNEW + ".tomo"


error_message = {
    # "IMPORT_BOTH": "ERROR: you cannot import BOTH raw movies/micrographs AND other node types at the same time...",
    "OPTICS_NAME_INVALID": "ERROR: an optics group name may contain only numbers, alphabets and hyphen(-).",
    "MODELSTAR_NOT_FOUND": "ERROR: cannot find appropriate model.star file in the output directory",
	"key": "ERROR: cannot find 'half' substring in the halfmap filename...",
	"key": "ERROR: cannot find 'half' substring in the input filename...",
	"key": "ERROR: Choose either parameter training or polishing, not both.",
	"key": "ERROR: choose either ResMap or Relion for local resolution estimation",
	"key": "ERROR: cryoCARE cannot currently use MPI or multiple GPUs in parallel. Only select one GPU.",
	"key": "ERROR: cryoCARE predict is enabled but path to the denoising model (--care_denoising_model) generated in cryoCARE:train has not been specified.",
	"key": "ERROR: cryoCARE training is enabled but the tomograms to train (--tomograms_for_training) on have not been specified.",
	"FILE_IN_PROJECTDIR": "ERROR: don't import files outside the project directory.\nPlease make a symbolic link by an absolute path before importing.",
    "FILE_IN_PATH": "ERROR: please import files by a relative path.\nIf you want to import files outside the project directory, make a symbolic link by an absolute path and\nimport the symbolic link by a relative path.",
	"key": "ERROR: Duplicate removal is only possible for particle STAR files...",
	"key": "ERROR: Duplicate removal needs a particle STAR file...",
	"key": "ERROR: either specify a optimiser file to continue multibody refinement from; OR run flexibility analysis...",
	"GPUID_REQUIRED": "ERROR: You must state desired GPU ID.",
    "GPU_NOT_SUPPORTED": "ERROR: This program/tool does not support GPU.",
    # "GPU_NOT_SUPPORTED": "ERROR: The Laplacian-of-Gaussian picker does not support GPU.",
	# "GPU_NOT_SUPPORTED": "ERROR: you cannot use GPUs when skipping image alignments.",
	"FIELD_REQUIRED": "ERROR: empty field...",
	"FIELD_REQUIRED_3DREF": "ERROR: empty field for 3D reference...",
	"FIELD_REQUIRED_CONT": "ERROR: empty field for continuation STAR file...",
	"FIELD_REQUIRED_COORD": "ERROR: empty field for coordinate STAR file...",
	"FIELD_REQUIRED_STAR": "ERROR: empty field for first or second input STAR file...", #  "ERROR: empty field for input STAR file...",
	"FIELD_REQUIRED_HALFMAP": "ERROR: empty field for input half-map...",
	"FIELD_REQUIRED_MASK": "ERROR: empty field for input mask...",
	"FIELD_REQUIRED_MIC": "ERROR: empty field for input micrograph STAR file...",
	# "FIELD_REQUIRED_OPTIM": "ERROR: Please specify an optimised parameter file OR choose 'use own paramaeters' and set three sigma values.",
	"FIELD_REQUIRED_OPTIM": "ERROR: empty field for input optimiser.star...",
	"FIELD_REQUIRED_POST": "ERROR: empty field for input PostProcess STAR file...",
	"FIELD_REQUIRED_REF": "ERROR: empty field for input reference...", # "ERROR: empty field for reference.",
	"FIELD_REQUIRED_REFS": "ERROR: empty field for references...",
	"FIELD_REQUIRED_REFINED": "ERROR: empty field for refined particles STAR file...",
	"FIELD_REQUIRED_EXT": "ERROR: empty field for the external executable script...",
	"FIELD_REQUIRED_PTCLS": "ERROR: empty field for the input particle STAR file...",
	"FIELD_REQUIRED_EXEC": "ERROR: please provide an executable for the ResMap program.",
	"FIELD_REQUIRED_RESMAP_HALFMAP": "ERROR: Please provide an input mask for ResMap local-resolution estimation.",
	"FIELD_REQUIRED_OPTICS": "ERROR: please specify an optics group name.",
	"key": "ERROR: Please specify both the extraction box size and the downsampled size, or leave both the default (-1)",
	"key": "ERROR: Filament selection by dendrogram analysis is only possible for optimiser STAR files...",
	"key": "ERROR: Filament selection by dendrogram analysis needs an optimiser STAR file...",
	"key": "ERROR: For Topaz training, specify which GPUs to use on the autopicking tab; for Topaz picking GPU usage is optional",
	"key": "ERROR: MotionCor2 cannot write float16 files.",
	"key": "ERROR: no manifold set is specified (either by the optimisation_set or the direct entry)",
	"key": "ERROR: no optimisation_set is provided, while you are also not using the direct input entries on the GUI.",
	"key": "ERROR: no particle set is specified (either by the optimisation_set or the direct entry)",
	"key": "ERROR: no reference half map file is specified",
	"key": "ERROR: nothing to do... ",
	"key": "ERROR: nothing to do, choose either parameter training or polishing.",
	"key": "ERROR: no tomogram set is specified (either by the optimisation_set or the direct entry)",
	"key": "ERROR: no trajectory set is specified (either by the optimisation_set or the direct entry)",
	"key": "ERROR: On the I/O tab specify (only) one of three methods: template-matching, LoG or topaz ...",
	"key": "ERROR: On the Topaz tab specify (only) one of two methods: training or picking...",
	"key": "ERROR: Per-particle motion and shift only corrections cannot be applied simultaneously.",
	"key": "ERROR: per-tomogram scale estimation and per-frame scale estimation are mutually exclusive",
	"key": "ERROR: regrouping and recentering have not been implemented in class_ranker.",
	"key": "ERROR: sorry 'surfaces/filaments' picking is yet to be implemented. Please bear with us...",
	"key": "ERROR: The downsampled box size cannot be larger than the extraction size.",
	"key": "ERROR: The downsampled box size must be an even number.",
	"key": "ERROR: The extraction box size must be an even number",
	"key": "ERROR: the fraction of Fourier pixels used for evaluation should be between 0.1 and 0.9.",
	"key": "ERROR: the maximum eigenvalue should be larger than the minimum one!",
	"key": "ERROR: there are more than one model.star files (without '_it' specifiers) in the output directory. Move all but one out of the way.",
	"key": "ERROR: Value-selection or subset splitting is only possible for micrograph or particle STAR files...",
	"key": "ERROR: When splitting the input STAR file into subsets, set nr_split and/or split_size to a positive value",
	"key": "ERROR: When using automatically selecting 2D classes, one needs to provide an optimiser.star file",
	"key": "ERROR: you cannot both reset refined offsets and recenter on refined coordinates, choose one...",
	"key": "ERROR: you cannot generate tomograms for denoising with the Fourier-inversion from odd/even frames method! Disable at least one of them.",
	"key": "ERROR: You cannot submit a ResMap job to the queue, as it needs user interaction.",
	"key": "ERROR: you did not select any CTF parameter to fit. Either switch off CTF parameter fitting, or select one to fit.",
	"key": "ERROR: you have indicated to use direct input entries, but the entry for the optimisation set is not empty.",
	"key": "ERROR: you haven't selected to fit anything...",
	"key": "ERROR: you have to specify an existing body STAR file.",
	"key": "ERROR: you need to provide a library to perform the HMM search against.",
	"key": "ERROR: you need to provide an input STAR file",
	"key": "ERROR: you should (only) enable ONE of the methods: cryoCARE:train (--do_cryocare_train), cryoCARE:predict (--do_cryocare_predict)",
	"key": "ERROR: you should (only) select ONE of the alignment methods: IMOD:fiducials or IMOD:patchtracking or AreTomo.",
	"key": "You're submitting a local job with ${NR_MPI} parallel MPI processes. That's more than allowed by the RELION_ERROR_LOCAL_MPI environment variable.",
}

"""
REPORT_ERROR("ERROR: Cannot write to file: " + fn_star),
REPORT_ERROR(" ERROR: Job does not contain label: " + label),
REPORT_ERROR(" ERROR: no '==' entry on JobOptionLine: " + setOptionLine),
REPORT_ERROR("ERROR reading file: " + myfilename + "run.job"),
REPORT_ERROR("ERROR: this jobOption does not return a boolean: " + label),
REPORT_ERROR("ERROR: unrecognised job-type"),
REPORT_ERROR("ERROR: unrecognised job-type: type = " + integerToString(type)),
REPORT_ERROR("getOutputNodesRefine ERROR: invalid dim value"),
REPORT_ERROR("Illegal gain_rot and/or gain_flip.")
"""
