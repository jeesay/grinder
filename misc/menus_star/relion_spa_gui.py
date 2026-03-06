import relion_h as rh
import relion_option as rno

def initialiseImportJob(is_tomo, job_type=""):
    joboptions = {}
    hidden_name = ".gui_import"

    joboptions["do_raw"] = rno.JobOptionIO("Import raw movies/micrographs?", True, "Set this to Yes if you plan to import raw movies or micrographs")
    joboptions["fn_in_raw"] = rno.JobOptionIO("Raw input files:", "Micrographs/*.tif", "Movie or Image (*.{mrc,mrcs,tif,tiff,eer,mrc.bz2,mrcs.bz2,mrc.zst,mrcs.zst,mrc.xz,mrcs.xz})", ".", """Provide a Linux wildcard that selects all raw movies or micrographs to be imported. The path must be a relative path from the project directory. To import files outside the project directory, first make a symbolic link by an absolute path and then specify the link by a relative path. See the FAQ page on RELION wiki (https://www3.mrc-lmb.cam.ac.uk/relion/index.php/FAQs#What_is_the_right_way_to_import_files_outside_the_project_directory.3F) for details.\
\
Torh.PROCess compressed MRC movies, you need pbzip2, zstd and xz command in your PATH for bzip2, Zstandard and xzip compression, respectively.""")
    joboptions["is_multiframe"] = rno.JobOptionIO("Are these multi-frame movies?", True, "Set to Yes for multi-frame movies, set to No for single-frame micrographs.")

    joboptions["optics_group_name"] = rno.JobOption("Optics group name:", "opticsGroup1", """Name of this optics group. Each group of movies/micrographs with different optics characteristics for CTF refinement should have a unique name.""")
    joboptions["fn_mtf"] = rno.JobOption("MTF of the detector:", "", "STAR Files (*.star)", ".", """As of release-3.1, the MTF of the detector is used in the refinement stages of refinement.  \
If you know the MTF of your detector, provide it here. Curves for some well-known detectors may be downloaded from the RELION Wiki. Also see there for the exact format \
\n If you do not know the MTF of your detector and do not want to measure it, then by leaving this entry empty, you include the MTF of your detector in your overall estimated B-factor upon sharpening the map.\
Although that is probably slightly less accurate, the overall quality of your map will probably not suffer very much. \n \n Note that when combining data from different detectors, the differences between their MTFs can no longer be absorbed in a single B-factor, and providing the MTF here is important!""")

    joboptions["angpix"] = rno.JobOption("Pixel size (Angstrom):", 1.4, 0.5, 3, 0.1, "Pixel size in Angstroms. ")
    joboptions["kV"] = rno.JobOption("Voltage (kV):", 300, 50, 500, 10, "Voltage the microscope was operated on (in kV)")
    joboptions["Cs"] = rno.JobOption("Spherical aberration (mm):", 2.7, 0, 8, 0.1, """Spherical aberration of the microscope used to collect these images (in mm). Typical values are 2.7 (FEI Titan & Talos, most JEOL CRYO-ARM), 2.0 (FEI Polara), 1.4 (some JEOL CRYO-ARM) and 0.01 (microscopes with a Cs corrector).""")
    joboptions["Q0"] = rno.JobOption("Amplitude contrast:", 0.1, 0, 0.3, 0.01, """Fraction of amplitude contrast. Often values around 10% work better than theoretically more accurate lower values...""")
    joboptions["beamtilt_x"] = rno.JobOption("Beamtilt in X (mrad):", 0.0, -1.0, 1.0, 0.1, """Known beamtilt in the X-direction (in mrad). Set to zero if unknown.""")
    joboptions["beamtilt_y"] = rno.JobOption("Beamtilt in Y (mrad):", 0.0, -1.0, 1.0, 0.1, """Known beamtilt in the Y-direction (in mrad). Set to zero if unknown.""")
    

    joboptions["do_other"] = rno.JobOptionIO("Import other node types?", False, "Set this to Yes if you plan to import anything else than movies or micrographs")

    joboptions["fn_in_other"] = rno.JobOptionIO("Input file:", "ref.mrc", "Input file (*.*)", ".", """Select any file(s) to import. \n \n \
Note that for importing coordinate files, one has to give a Linux wildcard, where the *-symbol is before the coordinate-file suffix, e.g. if the micrographs are called mic1.mrc and the coordinate files mic1.box or mic1_autopick.star, one HAS to give '*.box' or '*_autopick.star', respectively.\n \n \
Also note that micrographs, movies and coordinate files all need to be in the same directory (with the same rootnames, e.g.mic1 in the example above) in order to be imported correctly. 3D masks or references can be imported from anywhere. \n \n \
Note that movie-particle STAR files cannot be imported from a previous version of RELION, as the way movies are handled has changed in RELION-2.0. \n \n \
For the import of a particle, 2D references or micrograph STAR file or of a 3D reference or mask, only a single file can be imported at a time. \n \n \
Note that due to a bug in a fltk library, you cannot import from directories that contain a substring  of the current directory, e.g. dont important from /home/betagal if your current directory is called /home/betagal_r2. In this case, just change one of the directory names.""")

    if job_type == "ptcls" :
        joboptions["node_type"] = rno.JobOption("Node type:", rh.job_nodetype_options_particles, 0, "Select the type of Node this is.")
    elif job_type == "other" :
        joboptions["node_type"] = rno.JobOption("Node type:", rh.job_nodetype_options_other, 0, "Select the type of Node this is.")

    joboptions["optics_group_particles"] = rno.JobOption("Rename optics group for particles:", "", """Only for the import of a particles STAR file with a single, or no, optics groups defined: rename the optics group for the imported particles to this string.""")

    return hidden_name,joboptions

def initialiseImportRawJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_import"

    joboptions["do_raw"] = rno.JobOptionIO("Import raw movies/micrographs?", True, "Set this to Yes if you plan to import raw movies or micrographs")
    joboptions["fn_in_raw"] = rno.JobOptionIO("Raw input files:", "Micrographs/*.tif", "Movie or Image (*.{mrc,mrcs,tif,tiff,eer,mrc.bz2,mrcs.bz2,mrc.zst,mrcs.zst,mrc.xz,mrcs.xz})", ".", """Provide a Linux wildcard that selects all raw movies or micrographs to be imported. The path must be a relative path from the project directory. To import files outside the project directory, first make a symbolic link by an absolute path and then specify the link by a relative path. See the FAQ page on RELION wiki (https://www3.mrc-lmb.cam.ac.uk/relion/index.php/FAQs#What_is_the_right_way_to_import_files_outside_the_project_directory.3F) for details.\
\
Torh.PROCess compressed MRC movies, you need pbzip2, zstd and xz command in your PATH for bzip2, Zstandard and xzip compression, respectively.""")
    joboptions["is_multiframe"] = rno.JobOptionIO("Are these multi-frame movies?", True, "Set to Yes for multi-frame movies, set to No for single-frame micrographs.")

    joboptions["optics_group_name"] = rno.JobOption("Optics group name:", "opticsGroup1", """Name of this optics group. Each group of movies/micrographs with different optics characteristics for CTF refinement should have a unique name.""")
    joboptions["fn_mtf"] = rno.JobOption("MTF of the detector:", "", "STAR Files (*.star)", ".", """As of release-3.1, the MTF of the detector is used in the refinement stages of refinement.  \
If you know the MTF of your detector, provide it here. Curves for some well-known detectors may be downloaded from the RELION Wiki. Also see there for the exact format \
\n If you do not know the MTF of your detector and do not want to measure it, then by leaving this entry empty, you include the MTF of your detector in your overall estimated B-factor upon sharpening the map.\
Although that is probably slightly less accurate, the overall quality of your map will probably not suffer very much. \n \n Note that when combining data from different detectors, the differences between their MTFs can no longer be absorbed in a single B-factor, and providing the MTF here is important!""")

    joboptions["angpix"] = rno.JobOption("Pixel size (Angstrom):", 1.4, 0.5, 3, 0.1, "Pixel size in Angstroms. ")
    joboptions["kV"] = rno.JobOption("Voltage (kV):", 300, 50, 500, 10, "Voltage the microscope was operated on (in kV)")
    joboptions["Cs"] = rno.JobOption("Spherical aberration (mm):", 2.7, 0, 8, 0.1, """Spherical aberration of the microscope used to collect these images (in mm). Typical values are 2.7 (FEI Titan & Talos, most JEOL CRYO-ARM), 2.0 (FEI Polara), 1.4 (some JEOL CRYO-ARM) and 0.01 (microscopes with a Cs corrector).""")
    joboptions["Q0"] = rno.JobOption("Amplitude contrast:", 0.1, 0, 0.3, 0.01, """Fraction of amplitude contrast. Often values around 10% work better than theoretically more accurate lower values...""")
    joboptions["beamtilt_x"] = rno.JobOption("Beamtilt in X (mrad):", 0.0, -1.0, 1.0, 0.1, """Known beamtilt in the X-direction (in mrad). Set to zero if unknown.""")
    joboptions["beamtilt_y"] = rno.JobOption("Beamtilt in Y (mrad):", 0.0, -1.0, 1.0, 0.1, """Known beamtilt in the Y-direction (in mrad). Set to zero if unknown.""")


    return hidden_name,joboptions

def initialiseImportParticlesJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_import"

    joboptions["do_other"] = rno.JobOptionIO("Import other node types?", False, "Set this to Yes if you plan to import anything else than movies or micrographs")

    joboptions["fn_in_other"] = rno.JobOptionIO("Input file:", "ref.mrc", "Input file (*.*)", ".", """Select any file(s) to import. \n \n \
Note that for importing coordinate files, one has to give a Linux wildcard, where the *-symbol is before the coordinate-file suffix, e.g. if the micrographs are called mic1.mrc and the coordinate files mic1.box or mic1_autopick.star, one HAS to give '*.box' or '*_autopick.star', respectively.\n \n \
Also note that micrographs, movies and coordinate files all need to be in the same directory (with the same rootnames, e.g.mic1 in the example above) in order to be imported correctly. 3D masks or references can be imported from anywhere. \n \n \
Note that movie-particle STAR files cannot be imported from a previous version of RELION, as the way movies are handled has changed in RELION-2.0. \n \n \
For the import of a particle, 2D references or micrograph STAR file or of a 3D reference or mask, only a single file can be imported at a time. \n \n \
Note that due to a bug in a fltk library, you cannot import from directories that contain a substring  of the current directory, e.g. dont important from /home/betagal if your current directory is called /home/betagal_r2. In this case, just change one of the directory names.""")

    joboptions["node_type"] = rno.JobOption("Node type:", rh.job_nodetype_options_particles, 0, "Select the type of Node this is.")
    joboptions["optics_group_particles"] = rno.JobOption("Rename optics group for particles:", "", """Only for the import of a particles STAR file with a single, or no, optics groups defined: rename the optics group for the imported particles to this string.""")

    return hidden_name,joboptions

def initialiseImportOtherJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_import"

    joboptions["do_other"] = rno.JobOptionIO("Import other node types?", False, "Set this to Yes if you plan to import anything else than movies or micrographs")

    joboptions["fn_in_other"] = rno.JobOptionIO("Input file:", "ref.mrc", "Input file (*.*)", ".", """Select any file(s) to import. \n \n \
Note that for importing coordinate files, one has to give a Linux wildcard, where the *-symbol is before the coordinate-file suffix, e.g. if the micrographs are called mic1.mrc and the coordinate files mic1.box or mic1_autopick.star, one HAS to give '*.box' or '*_autopick.star', respectively.\n \n \
Also note that micrographs, movies and coordinate files all need to be in the same directory (with the same rootnames, e.g.mic1 in the example above) in order to be imported correctly. 3D masks or references can be imported from anywhere. \n \n \
Note that movie-particle STAR files cannot be imported from a previous version of RELION, as the way movies are handled has changed in RELION-2.0. \n \n \
For the import of a particle, 2D references or micrograph STAR file or of a 3D reference or mask, only a single file can be imported at a time. \n \n \
Note that due to a bug in a fltk library, you cannot import from directories that contain a substring  of the current directory, e.g. dont important from /home/betagal if your current directory is called /home/betagal_r2. In this case, just change one of the directory names.""")

    joboptions["node_type"] = rno.JobOption("Node type:", rh.job_nodetype_options_other, 0, "Select the type of Node this is.")
    joboptions["optics_group_particles"] = rno.JobOption("Rename optics group for particles:", "", """Only for the import of a particles STAR file with a single, or no, optics groups defined: rename the optics group for the imported particles to this string.""")

    return hidden_name,joboptions

def initialiseMotioncorrJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_motioncorr"
    is_tomo =  False

    if (is_tomo):
        joboptions["input_star_mics"] = rno.JobOptionIO("Input tilt series: ", rh.LABEL_TOMOGRAMS_CPIPE, 1, "", "Tilt series STAR file (*.star)", "Input global tilt series star file")

    else:
        joboptions["input_star_mics"] = rno.JobOptionIO("Input movies STAR file:", "LABEL_MOVIES_CPIPE", 1, "", "STAR files (*.star)", "A STAR file with all micrographs to run MOTIONCORR on")

    if (not is_tomo):
        joboptions["first_frame_sum"] = rno.JobOption("First frame for corrected sum:", 1, 1, 32, 1, """First frame to use in corrected average (starts counting at 1). """)
    if (not is_tomo):
        joboptions["last_frame_sum"] = rno.JobOption("Last frame for corrected sum:", -1, 0, 32, 1, """Last frame to use in corrected average. Values equal to or smaller than 0 mean 'use all frames'.""")
    joboptions["eer_grouping"] = rno.JobOption("EER fractionation:", 32, 1, 100, 1, """The number of hardware frames to group into one fraction. This option is relevant only for Falcon4 movies in the EER format. Note that all 'frames' in the GUI (e.g. first and last frame for corrected sum, dose per frame) refer to fractions, not raw detector frames. See https://www3.mrc-lmb.cam.ac.uk/relion/index.php/Image_compression#Falcon4_EER for detailed guidance on EERrh.PROCessing.""")
    joboptions["do_float16"] = rno.JobOption("Write output in float16?", True ,"""If set to Yes, RelionCor2 will write output images in float16 MRC format. This will save a factor of two in disk space compared to the default of writing in float32. Note that RELION and CCPEM will read float16 images, but other programs may not (yet) do so. For example, Gctf will not work with float16 images. Also note that this option does not work with UCSF MotionCor2. For CTF estimation, use CTFFIND-4.1 with pre-calculated power spectra (activate the 'Save sum of power spectra' option).""")
    if (is_tomo):
        joboptions["do_even_odd_split"] = rno.JobOption("Save images for denoising?", False ,"""If set to Yes, MotionCor2 will write output images summed from both the even frames of the input movie and the odd frames of the input movie. This generates two versions of the same movie which essential if you wish to carry out denoising later. If you are unsure whether you will need denoising later, it is best to select Yes, but be aware this option increases therh.PROCessing time for MotionCor. At the moment, this is only available in Shawn Zheng's MotionCor2 (>=v1.3.0)  and therefore do_float_16 must equal False too.""")


    # Motioncor2
    default_location = "RELION_MOTIONCOR2_EXECUTABLE"
#    default_motioncor2 = DEFAULTMOTIONCOR2LOCATION
#    if (default_location == NULL):
#        default_location = default_motioncor2


    # Common arguments RELION and UCSF implementation
    joboptions["bfactor"] = rno.JobOption("Bfactor:", 150, 0, 1500, 50, "The B-factor that will be applied to the micrographs.")
    joboptions["patch_x"] = rno.JobOption("Number of patches X:", ("1"), """Number of patches (in X and Y direction) to apply motioncor2.""")
    joboptions["patch_y"] = rno.JobOption("Number of patches Y:", ("1"), """Number of patches (in X and Y direction) to apply motioncor2.""")
    joboptions["group_frames"] = rno.JobOption("Group frames:", 1, 1, 5, 1, "Average together this many frames before calculating the beam-induced shifts.")
    joboptions["bin_factor"] = rno.JobOption("Binning factor:", 1, 1, 2, 1, """Bin the micrographs this much by a windowing operation in the Fourier Tranform. Binning at this level is hard to un-do later on, but may be useful to down-scale super-resolution images. Float-values may be used. Do make sure though that the resulting micrograph size is even.""")
    joboptions["fn_gain_ref"] = rno.JobOption("Gain-reference image:", "", "*.{mrc,gain}", ".", """Location of the gain-reference file to be applied to the input micrographs. Leave this empty if the movies are already gain-corrected.""")
    joboptions["gain_rot"] = rno.JobOption("Gain rotation:", rh.job_gain_rotation_options, 0, """Rotate the gain reference by this number times 90 degrees clockwise in relion_display. This is the same as -RotGain in MotionCor2. Note that MotionCor2 uses a different convention for rotation so it says 'counter-clockwise'. Valid values are 0, 1, 2 and 3.""")
    joboptions["gain_flip"] = rno.JobOption("Gain flip:", rh.job_gain_flip_options, 0, """Flip the gain reference after rotation. This is the same as -FlipGain in MotionCor2. 0 means do nothing, 1 means flip Y (upside down) and 2 means flip X (left to right).""")

    # UCSF-wrapper
    joboptions["do_own_motioncor"] = rno.JobOption("Use RELION's own implementation?", True ,"""If set to Yes, use RELION's own implementation of a MotionCor2-like algorithm by Takanori Nakane. Otherwise, wrap to the UCSF implementation. Note that Takanori's program only runs on CPUs but uses multiple threads, while the UCSF-implementation needs a GPU but uses only one CPU thread. Takanori's implementation is most efficient when the number of frames is divisible by the number of threads (e.g. 12 or 18 threads per MPIrh.PROCess for 36 frames). On some machines, setting the OMP_PROC_BIND environmental variable to TRUE accelerates the program.\n\
When running on 4k x 4k movies and using 6 to 12 threads, the speeds should be similar. Note that Takanori's program uses the same model as the UCSF program and gives results that are almost identical.\n\
Whichever program you use, 'Motion Refinement' is highly recommended to get the most of your dataset.""")
    joboptions["fn_motioncor2_exe"] = rno.JobOption("MOTIONCOR2 executable:", (default_location), "*.*", ".", """Location of the MOTIONCOR2 executable. You can control the default of this field by setting environment variable RELION_MOTIONCOR2_EXECUTABLE, or by editing the first few lines in src/gui_jobwindow.h and recompile the code.""")
    joboptions["fn_defect"] = rno.JobOption("Defect file:", "", "*", ".", """Location of a UCSF MotionCor2-style defect text file or a defect map that describe the defect pixels on the detector. Each line of a defect text file should contain four numbers specifying x, y, width and height of a defect region. A defect map is an image (MRC or TIFF), where 0 means good and 1 means bad pixels. The coordinate system is the same as the input movie before application of binning, rotation and/or flipping.\nNote that the format of the defect text is DIFFERENT from the defect text produced by SerialEM! One can convert a SerialEM-style defect file into a defect map using IMOD utilities e.g. `clip defect -D defect.txt -f tif movie.mrc defect_map.tif`. See explanations in the SerialEM manual.\n\nLeave empty if you don't have any defects, or don't want to correct for defects on your detector.""")
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", ("0"), """Provide a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':'. For example, to place one rank on device 0 and one rank on device 1, provide '0:1'.\n\
Note that multiple MotionCor2rh.PROCesses should not share a GPU; otherwise, it can lead to crash or broken outputs (e.g. black images) .""")
    joboptions["other_motioncor2_args"] = rno.JobOption("Other MOTIONCOR2 arguments", (""), "Additional arguments that need to be passed to MOTIONCOR2.")

    # Dose-weight
    if (not is_tomo):
        joboptions["do_dose_weighting"] = rno.JobOption("Do dose-weighting?", True ,"If set to Yes, the averaged micrographs will be dose-weighted.")
        joboptions["do_save_noDW"] = rno.JobOption("Save non-dose weighted as well?", False, """Aligned but non-dose weighted images are sometimes useful in CTF estimation, although there is no difference in most cases. Whichever the choice, CTF refinement job is always done on dose-weighted particles.""")
        joboptions["dose_per_frame"] = rno.JobOption("Dose per frame (e/A2):", 1, 0, 5, 0.2, """Dose per movie frame (in electrons per squared Angstrom).""")
        joboptions["pre_exposure"] = rno.JobOption("Pre-exposure (e/A2):", 0, 0, 5, 0.5, """Pre-exposure dose (in electrons per squared Angstrom).""")

    joboptions["do_save_ps"] = rno.JobOption("Save sum of power spectra?", True, """Sum of non-dose weighted power spectra provides better signal for CTF estimation. The power spectra can be used by CTFFIND4 but not by GCTF. This option is not available for UCSF MotionCor2. You must use this option when writing in float16.""")
    if (not is_tomo) :
        joboptions["group_for_ps"] = rno.JobOption("Sum power spectra every e/A2:", 4, 0, 10, 0.5, """McMullan et al (Ultramicroscopy, 2015) suggest summing power spectra every 4.0 e/A2 gives optimal Thon rings""")
    else:
        joboptions["group_for_ps"] = rno.JobOption("Sum power spectra every n frames:", 4, 0, 10, 0.5, """McMullan et al (Ultramicroscopy, 2015) suggest summing power spectra every 4.0 e/A2 gives optimal Thon rings""")

    return hidden_name,joboptions

def initialiseCtffindJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_ctffind"

    default_location = ""

    if (is_tomo):
        joboptions["input_star_mics"] = rno.JobOptionIO("Input tilt series: ", rh.LABEL_TOMOGRAMS_CPIPE, 1, "", "Tilt series STAR file (*.star)", "Input global tilt series star file.")

    else:
        joboptions["input_star_mics"] = rno.JobOptionIO("Input micrographs STAR file:", "LABEL_MICS_CPIPE", 1, "", "STAR files (*.star)", "A STAR file with all micrographs to run CTFFIND or Gctf on")


    if (not is_tomo) :
        joboptions["use_noDW"] = rno.JobOption("Use micrograph without dose-weighting?", False, """If set to Yes, the CTF estimation will be done using the micrograph without dose-weighting as in rlnMicrographNameNoDW (_noDW.mrc from MotionCor2). If set to No, the normal rlnMicrographName will be used.""")

    joboptions["do_phaseshift"] = rno.JobOption("Estimate phase shifts?", False, """If set to Yes, CTFFIND4 will estimate the phase shift, e.g. as introduced by a Volta phase-plate""")
    joboptions["phase_min"] = rno.JobOption("Phase shift (deg) - Min:", 0, """Minimum, maximum and step size (in degrees) for the search of the phase shift""")
    joboptions["phase_max"] = rno.JobOption("Phase shift (deg) - Max:", 180, """Minimum, maximum and step size (in degrees) for the search of the phase shift""")
    joboptions["phase_step"] = rno.JobOption("Phase shift (deg) - Step:", 10, """Minimum, maximum and step size (in degrees) for the search of the phase shift""")

    joboptions["dast"] = rno.JobOption("Amount of astigmatism (A):", 100, 0, 2000, 100,"CTFFIND's dAst parameter, GCTFs -astm parameter")

    # CTFFIND options

    # Check for environment variable RELION_CTFFIND_EXECUTABLE
    joboptions["use_given_ps"] = rno.JobOption("Use power spectra from MotionCorr job?", True, """If set to Yes, the CTF estimation will be done using power spectra calculated during motion correction. You must use this option if you used float16 in motion correction.""")
    default_location = "RELION_CTFFIND_EXECUTABLE"
    default_ctffind = "DEFAULTCTFFINDLOCATION"
    if (default_location == None):
        default_location = default_ctffind

    joboptions["fn_ctffind_exe"] = rno.JobOption("CTFFIND-4.1 executable:", (default_location), "*", ".", """Location of the CTFFIND (release 4.1 or later) executable. You can control the default of this field by setting environment variable RELION_CTFFIND_EXECUTABLE, or by editing the first few lines in src/gui_jobwindow.h and recompile the code.""")
    joboptions["slow_search"] = rno.JobOption("Use exhaustive search?", False, """If set to Yes, CTFFIND4 will use slower but more exhaustive search. This option is recommended for CTFFIND version 4.1.8 and earlier, but probably not necessary for 4.1.10 and later. It is also worth trying this option when astigmatism and/or phase shifts are difficult to fit.""")

    joboptions["box"] = rno.JobOption("FFT box size (pix):", 512, 64, 1024, 8, "CTFFIND's Box parameter")
    joboptions["resmin"] = rno.JobOption("Minimum resolution (A):", 30, 10, 200, 10, "CTFFIND's ResMin parameter")
    joboptions["resmax"] = rno.JobOption("Maximum resolution (A):", 5, 1, 20, 1, "CTFFIND's ResMax parameter")
    joboptions["dfmin"] = rno.JobOption("Minimum defocus value (A):", 5000, 0, 25000, 1000, "CTFFIND's dFMin parameter")
    joboptions["dfmax"] = rno.JobOption("Maximum defocus value (A):", 50000, 20000, 100000, 1000, "CTFFIND's dFMax parameter")
    joboptions["dfstep"] = rno.JobOption("Defocus step size (A):", 500, 200, 2000, 100,"CTFFIND's FStep parameter")

    if (is_tomo):
        joboptions["localsearch_nominal_defocus"] = rno.JobOption("Nominal defocus search range (A) ", 10000, 0, 20000, 1000, """If a positive value is given, the defocus search range will be set to +/- this value (in A) around the nominal defocus value from the input STAR file. If a zero or negative value are given, then the overall min-max defocus search ranges above will be used instead.""")
        joboptions["exp_factor_dose"] = rno.JobOption("Dose-dependent Thon ring fading (e/A^2) ", 100, 0, 200, 10, """If a positive value is given, then the maximum resolution for CTF estimation is lowerered by exp(dose/this_factor) times the original maximum resolution specified above. Remember that exp(1) ~=2.7, so a value of 100 e/A^2 for this factor will yield 2.7x higher maxres for an accumulated dose of 100 e/A^2; Smaller values will lead to faster decay of the maxres. If zero or a negative value is given, the maximum value specified above will be used for all images.""")


    joboptions["ctf_win"] = rno.JobOption("Estimate CTF on window size (pix) ", -1, -16, 4096, 16, """If a positive value is given, a squared window of this size at the center of the micrograph will be used to estimate the CTF. This may be useful to exclude parts of the micrograph that are unsuitable for CTF estimation, e.g. the labels at the edge of phtographic film. \n \n The original micrograph will be used (i.e. this option will be ignored) if a negative value is given.""")

    return hidden_name,joboptions

def initialiseManualpickJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_manualpick"

    joboptions["fn_in"] = rno.JobOptionIO("Input micrographs:", "LABEL_MICS_CPIPE", 1, "", "Input micrographs (*.{star,mrc})", """Input STAR file (with or without CTF information), OR a unix-type wildcard with all micrographs in MRC format (in this case no CTFs can be used).""")

    joboptions["diameter"] = rno.JobOption("Particle diameter (A):", 100, 0, 500, 50, """The diameter of the circle used around picked particles (in Angstroms). Only used for display.""" )
    joboptions["micscale"] = rno.JobOption("Scale for micrographs:", 0.2, 0.1, 1, 0.05, """The micrographs will be displayed at this relative scale, i.e. a value of 0.5 means that only every second pixel will be displayed.""" )
    joboptions["sigma_contrast"] = rno.JobOption("Sigma contrast:", 3, 0, 10, 0.5, """The micrographs will be displayed with the black value set to the average of all values MINUS this values times the standard deviation of all values in the micrograph, and the white value will be set \
to the average PLUS this value times the standard deviation. Use zero to set the minimum value in the micrograph to black, and the maximum value to white """)
    joboptions["white_val"] = rno.JobOption("White value:", 0, 0, 512, 16, "Use non-zero values to set the value of the whitest pixel in the micrograph.")
    joboptions["black_val"] = rno.JobOption("Black value:", 0, 0, 512, 16, "Use non-zero values to set the value of the blackest pixel in the micrograph.")

    joboptions["lowpass"] = rno.JobOption("Lowpass filter (A)", 20, 10, 100, 5, """Lowpass filter that will be applied to the micrographs. Give a negative value to skip the lowpass filter.""")
    joboptions["highpass"] = rno.JobOption("Highpass filter (A)", -1, 100, 1000, 100, """Highpass filter that will be applied to the micrographs. This may be useful to get rid of background ramps due to uneven ice distributions. Give a negative value to skip the highpass filter. Useful values are often in the range of 200-400 Angstroms.""")
    joboptions["angpix"] = rno.JobOption("Pixel size (A)", -1, 0.3, 5, 0.1, """Pixel size in Angstroms. This will be used to calculate the filters and the particle diameter in pixels. If a CTF-containing STAR file is input, then the value given here will be ignored, and the pixel size will be calculated from the values in the STAR file. A negative value can then be given here.""")
    joboptions["do_topaz_denoise"] = rno.JobOption("OR: use Topaz denoising?", False, "If set to True, Topaz denoising will be performed instead of lowpass filtering.")

    joboptions["do_startend"] = rno.JobOption("Pick start-end coordinates helices?", False, """If set to True, start and end coordinates are picked subsequently and a line will be drawn between each pair""")

    joboptions["do_fom_threshold"] = rno.JobOption("Use autopick FOM threshold?", False, """If set to Yes, only particles with rlnAutopickFigureOfMerit values below the threshold below will be extracted.""")
    joboptions["minimum_pick_fom"] = rno.JobOption("Minimum autopick FOM: ", 0, -5, 10, 0.1, "The minimum value for the rlnAutopickFigureOfMerit for particles to be extracted.")

    joboptions["do_color"] = rno.JobOption("Blue<>red color particles?", False, """If set to True, then the circles for each particles are coloured from red to blue (or the other way around) for a given metadatalabel. If this metadatalabel is not in the picked coordinates STAR file \
(basically only the rlnAutopickFigureOfMerit or rlnClassNumber) would be useful values there, then you may provide an additional STAR file (e.g. after classification/refinement below. Particles with values -999, or that are not in the additional STAR file will be coloured the default color: green""")
    joboptions["color_label"] = rno.JobOption("MetaDataLabel for color:", ("rlnAutopickFigureOfMerit"), """The Metadata label of the value to plot from red<>blue. Useful examples might be: \n \
rlnParticleSelectZScore \n rlnClassNumber \n rlnAutopickFigureOfMerit \n rlnAngleTilt \n rlnLogLikeliContribution \n rlnMaxValueProbDistribution \n rlnNrOfSignificantSamples\n""")
    joboptions["fn_color"] = rno.JobOption("STAR file with color label: ", "", "STAR file (*.star)", ".", """The program will figure out which particles in this STAR file are on the current micrograph and color their circles according to the value in the corresponding column. \
Particles that are not in this STAR file, but present in the picked coordinates file will be colored green. If this field is left empty, then the color label (e.g. rlnAutopickFigureOfMerit) should be present in the coordinates STAR file.""")
    joboptions["blue_value"] = rno.JobOption("Blue value: ", 0., 0., 4., 0.1, """The value of this entry will be blue. There will be a linear scale from blue to red, according to this value and the one given below.""")
    joboptions["red_value"] = rno.JobOption("Red value: ", 2., 0., 4., 0.1, """The value of this entry will be red. There will be a linear scale from blue to red, according to this value and the one given above.""")

    return hidden_name,joboptions

def initialiseAutopickJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_autopick"

    joboptions["fn_input_autopick"] = rno.JobOptionIO("Input micrographs for autopick:", "LABEL_MICS_CPIPE", 1, "", "Input micrographs (*.{star})", """Input STAR file (preferably with CTF information) with all micrographs to pick from.""")
    joboptions["angpix"] = rno.JobOption("Pixel size in micrographs (A)", -1, 0.3, 5, 0.1, """Pixel size in Angstroms. If a CTF-containing STAR file is input, then the value given here will be ignored, and the pixel size will be calculated from the values in the STAR file. A negative value can then be given here.""")
    joboptions["continue_manual"] = rno.JobOption("OR: continue manually?", False, """If set to Yes, an Autopick job can be continued as a manualpick job, so that incorrect picks can be corrected interactively.""")

    joboptions["do_log"] = rno.JobOption("OR: use Laplacian-of-Gaussian?", False, """If set to Yes, a Laplacian-of-Gaussian blob detection will be used (you can then leave the 'References' field empty. The preferred way to autopick is by setting this to no and providing references that were generated by 2D classification from this data set in RELION. The Laplacian-of-Gaussian method may be useful to kickstart a new data set. Please note that some options in the autopick tab are ignored in this method. See help messages of each option for details.""")
    joboptions["log_diam_min"] = rno.JobOption("Min. diameter for LoG filter (A)", 200, 50, 500, 10, """The smallest allowed diameter for the blob-detection algorithm. This should correspond to the smallest size of your particles in Angstroms.""")
    joboptions["log_diam_max"] = rno.JobOption("Max. diameter for LoG filter (A)", 250, 50, 500, 10, """The largest allowed diameter for the blob-detection algorithm. This should correspond to the largest size of your particles in Angstroms.""")
    joboptions["log_invert"] = rno.JobOption("Are the particles white?", False, "Set this option to No if the particles are black, and to Yes if the particles are white.")
    joboptions["log_maxres"] = rno.JobOption("Maximum resolution to consider (A)", 20, 10, 100, 5, """The Laplacian-of-Gaussian filter will be applied to downscaled micrographs with the corresponding size. Give a negative value to skip downscaling.""")
    joboptions["log_adjust_thr"] = rno.JobOption("Adjust default threshold (stddev):", 0, -1., 1., 0.05, """Use this to pick more (negative number -> lower threshold) or less (positive number -> higher threshold) particles compared to the default setting. The threshold is moved this many standard deviations away from the average.""")
    joboptions["log_upper_thr"] = rno.JobOption("Upper threshold (stddev):", 999., 0., 10., 0.5, """Use this to discard picks with LoG thresholds that are this many standard deviations above the average, e.g. to avoid high contrast contamination like ice and ethane droplets. Good values depend on the contrast of micrographs and need to be interactively explored; for low contrast micrographs, values of ~ 1.5 may be reasonable, but the same value will be too low for high-contrast micrographs.""")

    joboptions["do_topaz"] = rno.JobOption("OR: use Topaz?", False, """If set to Yes, topaz will be used for autopicking. Run 2 separate jobs from the Topaz tab: one for training the model and for the actual picking.""")
    joboptions["do_topaz_train"] = rno.JobOption("Perform topaz training?", False, "Set this option to Yes if you want to train a topaz model.")
    joboptions["topaz_train_picks"] = rno.JobOption("Input picked coordinates for training:", "LABEL_COORDS_CPIPE", 1, "", "Input micrographs (*.{star})", """Input STAR file (preferably with CTF information) with all micrographs to pick from.""")
    joboptions["do_topaz_train_parts"] = rno.JobOption("OR train on a set of particles? ", False, """If set to Yes, the input Coordinates above will be ignored. Instead, one uses a _data.star file from a previous 2D or 3D refinement or selection to use those particle positions for training.""")
    joboptions["topaz_train_parts"] = rno.JobOption("Particles STAR file for training: ", "LABEL_PARTS_CPIPE", 1, "", "Input STAR file (*.{star})", """Filename of the STAR file with the particle coordinates to be used for training, e.g. from a previous 2D or 3D classification or selection.""")
    joboptions["do_topaz_pick"] = rno.JobOption("Perform topaz picking?", False, "Set this option to Yes if you want to use a topaz model for autopicking.")
    joboptions["topaz_particle_diameter"] = rno.JobOption("Particle diameter (A) ", -1, 0, 2000, 20, """Diameter of the particle (to be used to infer topaz downscale factor and particle radius)""")
    joboptions["topaz_nr_particles"] = rno.JobOption("Nr of particles per micrograph: ", -1, 0, 2000, 20, "Expected average number of particles per micrograph")
    joboptions["topaz_model"] = rno.JobOption("Trained topaz model: ", "", "SAV Files (*.sav)", ".", """Trained topaz model for topaz-based picking. Use on job for training and a next job for picking. Leave this empty to use the default (general) model.""")
    joboptions["fn_topaz_exe"]= rno.JobOption("Topaz executable:", "relion_python_topaz", """Executable for running topaz. The default relion_python_topaz gets installed automatically through conda in a typical relion install. Only change this if this executable gives you problems.""")
    joboptions["do_topaz_filaments"] = rno.JobOption("Pick filaments?", False, """If set to Yes, this option will activate the -f option in our modified version of topaz that can pick filaments, as described in Lovestam & Scheres, Faraday Discussions 2022""")
    joboptions["topaz_filament_threshold"] = rno.JobOption("Threshold:", ("-5"),  """This sets the filament picking threshold and the length of the Hough transform, as described in Lovestam & Scheres, Faraday Discussions 2022. Useful values in our work on recombinant tau for the threshold range from −4 to −7. We typically do not change the default length of the Hough transform, which is set to be equal to the particle diameter when a negative value is given here. You can provide the additional option -fp to display images of intermediate steps of the algorithm to tune difficult cases.""")
    joboptions["topaz_hough_length"] = rno.JobOption("Hough length (A):", ("-1"), """This sets the filament picking threshold and the length of the Hough transform, as described in Lovestam & Scheres, Faraday Discussions 2022. Useful values in our work on recombinant tau for the threshold range from −4 to −7. We typically do not change the default length of the Hough transform, which is set to be equal to the particle diameter when a negative value is given here. You can provide the additional option -fp to display images of intermediate steps of the algorithm to tune difficult cases.""")
    joboptions["topaz_other_args"]= rno.JobOption("Additional topaz arguments:", (""), "These additional arguments will be passed onto all topaz programs.")

    joboptions["do_refs"] = rno.JobOption("Use reference-based template-matching?", False, """If set to Yes, 2D or 3D references, as defined on the References tab will be used for autopicking.""")
    joboptions["fn_refs_autopick"] = rno.JobOption("2D references:",rh.LABEL_2DIMGS_CPIPE, 1, "", "Input references (*.{star,mrcs})", """Input STAR file or MRC stack with the 2D references to be used for picking. Note that the absolute greyscale needs to be correct, so only use images created by RELION itself, e.g. by 2D class averaging or projecting a RELION reconstruction.""")
    joboptions["do_ref3d"]= rno.JobOption("OR: provide a 3D reference?", False, """Set this option to Yes if you want to provide a 3D map, which will be projected into multiple directions to generate 2D references.""")
    joboptions["fn_ref3d_autopick"] = rno.JobOption("3D reference:", "LABEL_MAP_CPIPE", 1, "", "Input reference (*.{mrc})", """Input MRC file with the 3D reference maps, from which 2D references will be made by projection. Note that the absolute greyscale needs to be correct, so only use maps created by RELION itself from this data set.""")
    joboptions["ref3d_symmetry"] = rno.JobOption("Symmetry:", ("C1"), """Symmetry point group of the 3D reference. Only projections in the asymmetric part of the sphere will be generated.""")
    joboptions["ref3d_sampling"] = rno.JobOption("3D angular sampling:", rh.job_sampling_options, 0, """There are only a few discrete \
angular samplings possible because we use the HealPix library to generate the sampling of the first two Euler angles on the sphere. \
The samplings are approximate numbers and vary slightly over the sphere.\n\n For autopicking, 30 degrees is usually fine enough, but for highly symmetrical objects one may need to go finer to adequately sample the asymmetric part of the sphere.""")

    joboptions["lowpass"] = rno.JobOption("Lowpass filter references (A)", 20, 10, 100, 5, """Lowpass filter that will be applied to the references before template matching. Do NOT use very high-resolution templates to search your micrographs. The signal will be too weak at high resolution anyway, and you may find Einstein from noise.... Give a negative value to skip the lowpass filter.""")
    joboptions["highpass"] = rno.JobOption("Highpass filter (A)", -1, 100, 1000, 100, """Highpass filter that will be applied to the micrographs. This may be useful to get rid of background ramps due to uneven ice distributions. Give a negative value to skip the highpass filter.  Useful values are often in the range of 200-400 Angstroms.""")
    joboptions["angpix_ref"] = rno.JobOption("Pixel size in references (A)", -1, 0.3, 5, 0.1, """Pixel size in Angstroms for the provided reference images. This will be used to calculate the filters and the particle diameter in pixels. If a negative value is given here, the pixel size in the references will be assumed to be the same as the one in the micrographs, i.e. the particles that were used to make the references were not rescaled upon extraction.""")
    joboptions["psi_sampling_autopick"] = rno.JobOption("In-plane angular sampling (deg)", 5, 1, 30, 1, """Angular sampling in degrees for exhaustive searches of the in-plane rotations for all references.""")

    joboptions["do_invert_refs"] = rno.JobOption("References have inverted contrast?", True, """Set to Yes to indicate that the reference have inverted contrast with respect to the particles in the micrographs.""")
    joboptions["do_ctf_autopick"] = rno.JobOption("Are References CTF corrected?", True, """Set to Yes if the references were created with CTF-correction inside RELION. \n \n If set to Yes, the input micrographs can only be given as a STAR file, which should contain the CTF information for each micrograph.""")
    joboptions["do_ignore_first_ctfpeak_autopick"] = rno.JobOption("Ignore CTFs until first peak?", False,"Set this to Yes, only if this option was also used to generate the references.")

    joboptions["threshold_autopick"] = rno.JobOption("Picking threshold:", 0.05, 0, 1., 0.01, """Use lower thresholds to pick more particles (and more junk probably).\
\n\nThis option is ignored in the Laplacian-of-Gaussian picker. Please use 'Adjust default threshold' in the 'Laplacian' tab instead.""")
    joboptions["mindist_autopick"] = rno.JobOption("Minimum inter-particle distance (A):", 100, 0, 1000, 20, """Particles closer together than this distance will be consider to be a single cluster. From each cluster, only one particle will be picked. \
\n\nThis option takes no effect for picking helical segments. The inter-box distance is calculated with the number of asymmetrical units and the helical rise on 'Helix' tab. This option is also ignored in the Laplacian-of-Gaussian picker. The inter-box distance is calculated from particle diameters.""")
    joboptions["maxstddevnoise_autopick"] = rno.JobOption("Maximum stddev noise:", 1.1, 0.9, 1.5, 0.02, """This is useful to prevent picking in carbon areas, or areas with big contamination features. Peaks in areas where the background standard deviation in the normalized micrographs is higher than this value will be ignored. Useful values are probably in the range 1.0 to 1.2. Set to -1 to switch off the feature to eliminate peaks due to high background standard deviations.\
\n\nThis option is ignored in the Laplacian-of-Gaussian picker.""")
    joboptions["minavgnoise_autopick"] = rno.JobOption("Minimum avg noise:", -999., -2, 0.5, 0.05, """This is useful to prevent picking in carbon areas, or areas with big contamination features. Peaks in areas where the background standard deviation in the normalized micrographs is higher than this value will be ignored. Useful values are probably in the range -0.5 to 0. Set to -999 to switch off the feature to eliminate peaks due to low average background densities.\
\n\nThis option is ignored in the Laplacian-of-Gaussian picker.""")
    joboptions["do_write_fom_maps"] = rno.JobOption("Write FOM maps?", False, """If set to Yes, intermediate probability maps will be written out, which (upon reading them back in) will speed up tremendously the optimization of the threshold and inter-particle distance parameters. However, with this option, one cannot run in parallel, as disc I/O is very heavy with this option set.""")
    joboptions["do_read_fom_maps"] = rno.JobOption("Read FOM maps?", False, """If written out previously, read the FOM maps back in and re-run the picking to quickly find the optimal threshold and inter-particle distance parameters""")

    joboptions["shrink"] = rno.JobOption("Shrink factor:", 0, 0, 1, 0.1, """This is useful to speed up the calculations, and to make them less memory-intensive. The micrographs will be downscaled (shrunk) to calculate the cross-correlations, and peak searching will be done in the downscaled FOM maps. When set to 0, the micrographs will de downscaled to the lowpass filter of the references, a value between 0 and 1 will downscale the micrographs by that factor. Note that the results will not be exactly the same when you shrink micrographs!\
\n\nIn the Laplacian-of-Gaussian picker, this option is ignored and the shrink factor always becomes 0.""")
    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, """If set to Yes, the job will try to use GPU acceleration. The Laplacian-of-Gaussian picker does not support GPU.""")
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), """This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':'. For example: 0:1:0:1:0:1""")

    joboptions["do_pick_helical_segments"] = rno.JobOption("Pick 2D helical segments?", False, """Set to Yes if you want to pick 2D helical segments. Note this will run the old algorithms for reference-based helical segment picking, as described by He & Scheres, J Struct Biol, 2017. Often, we now run filament picking from the Topaz tab instead....""")
    joboptions["do_amyloid"] = rno.JobOption("Pick amyloid segments?", False, """Set to Yes if you want to use the algorithm that was developed specifically for picking amyloids.""")

    joboptions["helical_tube_outer_diameter"] = rno.JobOption("Tube diameter (A): ", 200, 100, 1000, 10, """Outer diameter (in Angstroms) of helical tubes. \
This value should be slightly larger than the actual width of the tubes.""")
    joboptions["helical_nr_asu"] = rno.JobOption("Number of unique asymmetrical units:", 1, 1, 100, 1, """Number of unique helical asymmetrical units in each segment box. This integer should not be less than 1. The inter-box distance (pixels) = helical rise (Angstroms) * number of asymmetrical units / pixel size (Angstroms). \
The optimal inter-box distance might also depend on the box size, the helical rise and the flexibility of the structure. In general, an inter-box distance of ~10% * the box size seems appropriate.""")
    joboptions["helical_rise"] = rno.JobOption("Helical rise (A):", -1, 0, 100, 0.01, """Helical rise in Angstroms. (Please click '?' next to the option above for details about how the inter-box distance is calculated.)""")
    joboptions["helical_tube_kappa_max"] = rno.JobOption("Maximum curvature (kappa): ", 0.1, 0.05, 0.5, 0.01, """Maximum curvature allowed for picking helical tubes. \
Kappa = 0.3 means that the curvature of the picked helical tubes should not be larger than 30% the curvature of a circle (diameter = particle mask diameter). \
Kappa ~ 0.05 is recommended for long and straight tubes (e.g. TMV, VipA/VipB and AChR tubes) while 0.20 ~ 0.40 seems suitable for flexible ones (e.g. ParM and MAVS-CARD filaments).""")
    joboptions["helical_tube_length_min"] = rno.JobOption("Minimum length (A): ", -1, 100, 1000, 10, """Minimum length (in Angstroms) of helical tubes for auto-picking. \
Helical tubes with shorter lengths will not be picked. Note that a long helical tube seen by human eye might be treated as short broken pieces due to low FOM values or high picking threshold.""")

    return hidden_name,joboptions

def initialiseExtractJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_extract"

    joboptions["star_mics"]= rno.JobOptionIO("micrograph STAR file: ", "LABEL_MICS_CPIPE", 1, "", "Input STAR file (*.{star})", "Filename of the STAR file that contains all micrographs from which to extract particles.")
    # TO DOL set helical option for this
    joboptions["coords_suffix"] = rno.JobOption("Input coordinates: ", "LABEL_COORDS_CPIPE", 1, "", "Input coordinates list file (*.star)", """Starfile with a 2-column list of micrograph names and corresponding coordinate filenames (in .star, .box or as 2 or 3-column free text format)""")
    joboptions["do_reextract"] = rno.JobOption("OR re-extract refined particles? ", False, """If set to Yes, the input Coordinates above will be ignored. Instead, one uses a _data.star file from a previous 2D or 3D refinement to re-extract the particles in that refinement, possibly re-centered with their refined origin offsets. This is particularly useful when going from binned to unbinned particles.""")
    joboptions["fndata_reextract"] = rno.JobOption("Refined particles STAR file: ", "LABEL_PARTS_CPIPE", 1, "", "Input STAR file (*.{star})", """Filename of the STAR file with the refined particle coordinates, e.g. from a previous 2D or 3D classification or auto-refine run.""")
    joboptions["do_reset_offsets"] = rno.JobOption("Reset the refined offsets to zero? ", False, """If set to Yes, the input origin offsets will be reset to zero. This may be useful after 2D classification of helical segments, where one does not want neighbouring segments to be translated on top of each other for a subsequent 3D refinement or classification.""")
    joboptions["do_recenter"] = rno.JobOption("OR: re-center refined coordinates? ", False, """If set to Yes, the input coordinates will be re-centered according to the refined origin offsets in the provided _data.star file. The unit is pixel, not angstrom. The origin is at the center of the box, not at the corner.""")
    joboptions["recenter_x"] = rno.JobOption("Re-center on X-coordinate (in pix): ", ("0"), """Re-extract particles centered on this X-coordinate (in pixels in the reference)""")
    joboptions["recenter_y"] = rno.JobOption("Re-center on Y-coordinate (in pix): ", ("0"), """Re-extract particles centered on this Y-coordinate (in pixels in the reference)""")
    joboptions["recenter_z"] = rno.JobOption("Re-center on Z-coordinate (in pix): ", ("0"), """Re-extract particles centered on this Z-coordinate (in pixels in the reference)""")
    joboptions["extract_size"] = rno.JobOption("Particle box size (pix):", 128, 64, 512, 8, """Size of the extracted particles (in pixels). This should be an even number!""")
    joboptions["do_invert"] = rno.JobOption("Invert contrast?", True, "If set to Yes, the contrast in the particles will be inverted.")
    joboptions["do_float16"] = rno.JobOption("Write output in float16?", True ,"""If set to Yes, this program will write output images in float16 MRC format. This will save a factor of two in disk space compared to the default of writing in float32. Note that RELION and CCPEM will read float16 images, but other programs may not (yet) do so.""")

    joboptions["do_norm"] = rno.JobOption("Normalize particles?", True, "If set to Yes, particles will be normalized in the way RELION prefers it.")
    joboptions["bg_diameter"] = rno.JobOption("Diameter background circle (pix): ", -1, -1, 600, 10, """Particles will be normalized to a mean value of zero and a standard-deviation of one for all pixels in the background area.\
The background area is defined as all pixels outside a circle with this given diameter in pixels (before rescaling). When specifying a negative value, a default value of 75% of the Particle box size will be used.""")
    joboptions["white_dust"] = rno.JobOption("Stddev for white dust removal: ", -1, -1, 10, 0.1, """Remove very white pixels from the extracted particles. \
Pixels values higher than this many times the image stddev will be replaced with values from a Gaussian distribution. \n \n Use negative value to switch off dust removal.""")
    joboptions["black_dust"] = rno.JobOption("Stddev for black dust removal: ", -1, -1, 10, 0.1, """Remove very black pixels from the extracted particles. \
Pixels values higher than this many times the image stddev will be replaced with values from a Gaussian distribution. \n \n Use negative value to switch off dust removal.""")
    joboptions["do_rescale"] = rno.JobOption("Rescale particles?", False, """If set to Yes, particles will be re-scaled. Note that the particle diameter below will be in the down-scaled images.""")
    joboptions["rescale"] = rno.JobOption("Re-scaled size (pixels): ", 128, 64, 512, 8, "The re-scaled value needs to be an even number")
    joboptions["do_fom_threshold"] = rno.JobOption("Use autopick FOM threshold?", False, """If set to Yes, only particles with rlnAutopickFigureOfMerit values below the threshold below will be extracted.""")
    joboptions["minimum_pick_fom"] = rno.JobOption("Minimum autopick FOM: ", 0, -5, 10, 0.1, "The minimum value for the rlnAutopickFigureOfMerit for particles to be extracted.")

    joboptions["do_extract_helix"] = rno.JobOption("Extract helical segments?", False, """Set to Yes if you want to extract helical segments. RELION (.star), EMAN2 (.box) and XIMDISP (.coords) formats of tube or segment coordinates are supported.""")
    joboptions["helical_tube_outer_diameter"] = rno.JobOption("Tube diameter (A): ", 200, 100, 1000, 10, """Outer diameter (in Angstroms) of helical tubes. \
This value should be slightly larger than the actual width of helical tubes.""")
    joboptions["helical_bimodal_angular_priors"] = rno.JobOption("Use bimodal angular priors?", True, """Normally it should be set to Yes and bimodal angular priors will be applied in the following classification and refinement jobs. \
Set to No if the 3D helix looks the same when rotated upside down.""")
    joboptions["do_extract_helical_tubes"] = rno.JobOption("Coordinates are start-end only?", True, """Set to Yes if you want to extract helical segments from manually picked tube coordinates (starting and end points of helical tubes in RELION, EMAN or XIMDISP format). \
Set to No if segment coordinates (RELION auto-picked results or EMAN / XIMDISP segments) are provided.""")
    joboptions["do_cut_into_segments"] = rno.JobOption("Cut helical tubes into segments?", True, """Set to Yes if you want to extract multiple helical segments with a fixed inter-box distance. \
If it is set to No, only one box at the center of each helical tube will be extracted.""")
    joboptions["helical_nr_asu"] = rno.JobOption("Number of unique asymmetrical units:", 1, 1, 100, 1, """Number of unique helical asymmetrical units in each segment box. This integer should not be less than 1. The inter-box distance (pixels) = helical rise (Angstroms) * number of asymmetrical units / pixel size (Angstroms). \
The optimal inter-box distance might also depend on the box size, the helical rise and the flexibility of the structure. In general, an inter-box distance of ~10% * the box size seems appropriate.""")
    joboptions["helical_rise"] = rno.JobOption("Helical rise (A):", 1, 0, 100, 0.01, """Helical rise in Angstroms. (Please click '?' next to the option above for details about how the inter-box distance is calculated.)""")

    return hidden_name,joboptions

def initialiseSelectJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_select"

    joboptions["fn_model"] = rno.JobOptionIO("Select classes from job:",rh.LABEL_OPTIMISER_CPIPE, 1, "", "STAR files (*_optimiser.star)", """A _optimiser.star (or for backwards compatibility also a _model.star) file from a previous 2D or 3D classification run to select classes from.""")
    joboptions["fn_mic"] = rno.JobOptionIO("OR select from micrographs.star:", "LABEL_MICS_CPIPE", 1, "", "STAR files (*.star)", "A micrographs.star file to select micrographs from.")
    joboptions["fn_data"] = rno.JobOptionIO("OR select from particles.star:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star)", "A particles.star file to select individual particles from.")

    joboptions["do_class_ranker"] = rno.JobOption("Automatically select 2D classes?", False, """If set to True, the class_ranker program will be used to make an automated class selection, based on the parameters below. This option only works when selecting classes from a relion_refine job (input optimiser.star on the I.O tab)""")
    joboptions["rank_threshold"] = rno.JobOption("Minimum threshold for auto-selection: ", 0.5, 0, 1, 0.05, "Only classes with a pre dicted threshold above this value will be selected.")
    joboptions["select_nr_parts"] = rno.JobOption("Select at least this many particles: ", -1, -1, 10000, 500, """Even if they have scores below the minimum threshold, select at least this many particles with the best scores.""")
    joboptions["select_nr_classes"] = rno.JobOption("OR: select at least this many classes: ", -1, -1, 24, 1, """Even if they have scores below the minimum threshold, select at least this many classes with the best scores.""")

    joboptions["do_recenter"] = rno.JobOption("Re-center the class averages?", False, """This option is only used when selecting particles from 2D classes. The selected class averages will all re-centered on their center-of-mass. This is useful when you plane to use these class averages as templates for auto-picking.""")
    joboptions["do_regroup"] = rno.JobOption("Regroup the particles?", False, """If set to Yes, then the program will regroup the selected particles in 'more-or-less' the number of groups indicated below. For re-grouping from individual particle _data.star files, a _model.star file with the same prefix should exist, i.e. the particle star file should be generated by relion_refine""")
    joboptions["nr_groups"] = rno.JobOption("Approximate nr of groups: ", 1, 50, 20, 1, "It is normal that the actual number of groups may deviate a little from this number. ")

    joboptions["do_select_values"] = rno.JobOption("Select based on metadata values?", False, """If set to Yes, the job will be non-interactive and the selected star file will be based only on the value of the corresponding metadata label. Note that this option is only valid for micrographs or particles STAR files.""")
    joboptions["select_label"] = rno.JobOption("Metadata label for subset selection:", "rlnCtfMaxResolution", "This column from the input STAR file will be used for the subset selection.")
    joboptions["select_minval"] = rno.JobOption("Minimum metadata value:",  "-9999.", """Only lines in the input STAR file with the corresponding metadata value larger than or equal to this value will be included in the subset.""")
    joboptions["select_maxval"] = rno.JobOption("Maximum metadata value:",  "9999.", """Only lines in the input STAR file with the corresponding metadata value smaller than or equal to this value will be included in the subset.""")

    joboptions["do_discard"] = rno.JobOption("OR: select on image statistics?", False, """If set to Yes, the job will be non-interactive and all images in the input star file that have average and/or stddev pixel values that are more than the specified sigma-values away from the ensemble mean will be discarded.""")
    joboptions["discard_label"] = rno.JobOption("Metadata label for images:", "rlnImageName", """Specify which column from the input STAR contains the names of the images to be used to calculate the average and stddev values.""")
    joboptions["discard_sigma"] = rno.JobOption("Sigma-value for discarding images:", 4, 1, 10, 0.1, """Images with average and/or stddev values that are more than this many times the ensemble stddev away from the ensemble mean will be discarded.""")

    joboptions["do_split"] = rno.JobOption("OR: split into subsets?", False, """If set to Yes, the job will be non-interactive and the star file will be split into subsets as defined below.""")
    joboptions["do_random"] = rno.JobOption("Randomise order before making subsets?:", False, """If set to Yes, the input STAR file order will be randomised. If set to No, the original order in the input STAR file will be maintained.""")
    joboptions["split_size"] = rno.JobOption("Subset size: ", 100, 100, 10000, 100, """The number of lines in each of the output subsets. When this is -1, items are divided into a number of subsets specified in the next option.""")
    joboptions["nr_split"] = rno.JobOption("OR: number of subsets: ", -1, 1, 50, 1, """Give a positive integer to specify into how many equal-sized subsets the data will be divided. When the subset size is also specified, only this number of subsets, each with the specified size, will be written, possibly missing some items. When this is -1, all items are used, generating as many subsets as necessary.""")

    joboptions["do_remove_duplicates"] = rno.JobOption("OR: remove duplicates?", False, """If set to Yes, duplicated particles that are within a given distance are removed leaving only one. Duplicated particles are sometimes generated when particles drift into the same position during alignment. They inflate and invalidate gold-standard FSC calculation.""")
    joboptions["duplicate_threshold"] = rno.JobOption("Minimum inter-particle distance (A)", 30, 0, 1000, 1, "Particles within this distance are removed leaving only one.")
    joboptions["image_angpix"] = rno.JobOption("Pixel size before extraction (A)", -1, -1, 10, 0.01, """The pixel size of particles (relevant to rlnOriginX/Y) is read from the STAR file. When the pixel size of the original micrograph used for auto-picking and extraction (relevant to rlnCoordinateX/Y) is different, specify it here. In other words, this is the pixel size after binning during motion correction, but before down-sampling during extraction.""")

    joboptions["do_filaments"] = rno.JobOption("OR: select filaments by dendrogram?", False, """If set to Yes, then the FilamentTools program by David Li will be used to perform a hierarchical clustering of the filaments, based on 2D class average assignments of their individual segments.""")
    joboptions["dendrogram_threshold"] = rno.JobOption("Dendrogram threshold: ", 0.85, 0, 1, 0.05, """Lower thresholds will produce more clusters; After the dendrogram has been calculated in the initial running of this job, subsequent continuation jobs can quickly test other threshold values. The output logfile.pdf can be visualised to follow therh.PROCess until a good threshold has been achieved.""")
    joboptions["dendrogram_minclass"] = rno.JobOption("Minimum class size: ", -1000, -1000, 50000, 1000, """If set to a positive value, then particle star files with clusters that have at least this number of particles will be written out. Keep th default negative value for faster testing of the threshold.""")

    return hidden_name,joboptions

def initialiseClass2DJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_class2d"

    joboptions["fn_img"] = rno.JobOptionIO("Input images STAR file:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star) \t Image stacks (not recommended, read help!) (*.{spi,mrcs})", """A STAR file with all images (and their metadata). \n \n Alternatively, you may give a Spider/MRC stack of 2D images, but in that case NO metadata can be included and thus NO CTF correction can be performed, \
nor will it be possible to perform noise spectra estimation or intensity scale corrections in image groups. Therefore, running RELION with an input stack will in general provide sub-optimal results and is therefore not recommended!! Use the Preprocessingrh.PROCedure to get the input STAR file in a semi-automated manner. Read the RELION wiki for more information.""")
    joboptions["fn_cont"] = rno.JobOptionIO("Continue from here: ", (""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR",  """Select the *_optimiser.star file for the iteration \
from which you want to continue a previous run. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a '_ctX' to the output rootname, \
with X being the iteration from which one continues the previous run.""")

    joboptions["do_ctf_correction"] = rno.JobOption("Do CTF-correction?", True, """If set to Yes, CTFs will be corrected inside the MAP refinement. \
The resulting algorithm intrinsically implements the optimal linear, or Wiener filter. \
Note that CTF parameters for all images need to be given in the input STAR file. \
The command 'relion_refine --print_metadata_labels' will print a list of all possible metadata labels for that STAR file. \
See the RELION Wiki for more details.\n\n Also make sure that the correct pixel size (in Angstrom) is given above!)""")
    joboptions["ctf_intact_first_peak"] = rno.JobOption("Ignore CTFs until first peak?", False, """If set to Yes, then CTF-amplitude correction will \
only be performed from the first peak of each CTF onward. This can be useful if the CTF model is inadequate at the lowest resolution. \
Still, in general using higher amplitude contrast on the CTFs (e.g. 10-20%) often yields better results. \
Therefore, this option is not generally recommended: try increasing amplitude contrast (in your input STAR file) first!""")

    joboptions["nr_classes"] = rno.JobOption("Number of classes:", 1, 1, 50, 1, """The number of classes (K) for a multi-reference refinement. \
These classes will be made in an unsupervised manner from a single reference by division of the data into random subsets during the first iteration.""")
    joboptions["tau_fudge"] = rno.JobOption("Regularisation parameter T:", 2 , 0.1, 10, 0.1, """Bayes law strictly determines the relative weight between \
the contribution of the experimental data and the prior. However, in practice one may need to adjust this weight to put slightly more weight on \
the experimental data to allow optimal results. Values greater than 1 for this regularisation parameter (T in the JMB2011 paper) put more \
weight on the experimental data. Values around 2-4 have been observed to be useful for 3D refinements, values of 1-2 for 2D refinements. \
Too small values yield too-low resolution structures; too high values result in over-estimated resolutions, mostly notable by the apparition of high-frequency noise in the references.""")


    joboptions["do_em"] = rno.JobOption("Use EM algorithm?", False, """If set to Yes, the slower expectation-maximization algorithm will be used. This was the default option in releases prior to 4.0-beta. If set to No, then one needs to use the (faster) VDAM (variable metric gradient descent with adaptive moments) algorithm below. will be used.""")
    joboptions["nr_iter_em"] = rno.JobOption("Number of EM iterations:", 25, 1, 50, 1, """Number of EM iterations to be performed. \
Note that the current implementation of 2D class averaging and 3D classification does NOT comprise a convergence criterium. \
Therefore, the calculations will need to be stopped by the user if further iterations do not yield improvements in resolution or classes. \n\n \
Also note that upon restarting, the iteration number continues to be increased, starting from the final iteration in the previous run. \
The number given here is the TOTAL number of iterations. For example, if 10 iterations have been performed previously and one restarts to perform \
an additional 5 iterations (for example with a finer angular sampling), then the number given here should be 10+5=15.""")


    joboptions["do_grad"] = rno.JobOption("Use VDAM algorithm?", True, """If set to Yes, the faster VDAM algorithm will be used. This algorithm was introduced with relion-4.0. If set to No, then the slower EM algorithm needs to be used.""")
    joboptions["nr_iter_grad"] = rno.JobOption("Number of VDAM mini-batches:", 200, 50, 500, 10, """Number of mini-batches to berh.PROCessed using the VDAM algorithm. Using 200 has given good results for many data sets. Using 100 will run faster, at the expense of some quality in the results.""")

    joboptions["particle_diameter"] = rno.JobOption("Mask diameter (A):", 200, 0, 1000, 10, """The experimental images will be masked with a soft \
circular mask with this diameter. Make sure this radius is not set too small because that may mask away part of the signal! \
If set to a value larger than the image size no masking will be performed.\n\n\
The same diameter will also be used for a spherical mask of the reference structures if no user-provided mask is specified.""")
    joboptions["do_zero_mask"] = rno.JobOption("Mask individual particles with zeros?", True, """If set to Yes, then in the individual particles, \
the area outside a circle with the radius of the particle will be set to zeros prior to taking the Fourier transform. \
This will remove noise and therefore increase sensitivity in the alignment and classification. However, it will also introduce correlations \
between the Fourier components that are not modelled. When set to No, then the solvent area is filled with random noise, which prevents introducing correlations.\
High-resolution refinements (e.g. ribosomes or other large complexes in 3D auto-refine) tend to work better when filling the solvent area with random noise (i.e. setting this option to No), refinements of smaller complexes and most classifications go better when using zeros (i.e. setting this option to Yes).""")
    joboptions["highres_limit"] = rno.JobOption("Limit resolution E-step to (A): ", -1, -1, 20, 1, """If set to a positive number, then the expectation step (i.e. the alignment) will be done only including the Fourier components up to this resolution (in Angstroms). \
This is useful to prevent overfitting, as the classification runs in RELION are not to be guaranteed to be 100% overfitting-free (unlike the 3D auto-refine with its gold-standard FSC). In particular for very difficult data sets, e.g. of very small or featureless particles, this has been shown to give much better class averages. \
In such cases, values in the range of 7-12 Angstroms have proven useful.""")
    joboptions["do_center"] = rno.JobOption("Center class averages?", True, """If set to Yes, every iteration the class average images will be centered on their center-of-mass. This will only work for positive signals, so the particles should be white.""")

    joboptions["dont_skip_align"] = rno.JobOption("Perform image alignment?", True, """If set to No, then rather than \
performing both alignment and classification, only classification will be performed. This allows the use of very focused masks.\
This requires that the optimal orientations of all particles are already stored in the input STAR file. """)
    joboptions["psi_sampling"] = rno.JobOption("In-plane angular sampling:", 6., 0.5, 20, 0.5, """The sampling rate for the in-plane rotation angle (psi) in degrees. \
Using fine values will slow down the program. Recommended value for most 2D refinements: 5 degrees.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.""")
    joboptions["offset_range"] = rno.JobOption("Offset search range (pix):", 5, 0, 30, 1, """Probabilities will be calculated only for translations \
in a circle with this radius (in pixels). The center of this circle changes at every iteration and is placed at the optimal translation \
for each image in the previous iteration.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.""")
    joboptions["offset_step"] = rno.JobOption("Offset search step (pix):", 1, 0.1, 5, 0.1, """Translations will be sampled with this step-size (in pixels).\
Translational sampling is also done using the adaptive approach. \
Therefore, if adaptive=1, the translations will first be evaluated on a 2x coarser grid.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.""")
    joboptions["allow_coarser"] = rno.JobOption("Allow coarser sampling?", False, """If set to Yes, the program will use coarser angular and translational samplings if the estimated accuracies of the assignments is still low in the earlier iterations. This may speed up the calculations.""")

    joboptions["do_helix"] = rno.JobOption("Classify 2D helical segments?", False, """Set to Yes if you want to classify 2D helical segments. Note that the helical segments should come with priors of psi angles""")
    joboptions["helical_tube_outer_diameter"] = rno.JobOption("Tube diameter (A): ", 200, 100, 1000, 10, """Outer diameter (in Angstroms) of helical tubes. \
This value should be slightly larger than the actual width of the tubes. You may want to copy the value from previous particle extraction job. \
If negative value is provided, this option is disabled and ordinary circular masks will be applied. Sometimes '--dont_check_norm' option is useful to prevent errors in normalisation of helical segments.""")
    joboptions["do_bimodal_psi"] = rno.JobOption("Do bimodal angular searches?", True, """Do bimodal search for psi angles? \
Set to Yes if you want to classify 2D helical segments with priors of psi angles. The priors should be bimodal due to unknown polarities of the segments. \
Set to No if the 3D helix looks the same when rotated upside down. If it is set to No, ordinary angular searches will be performed.\n\nThis option will be invalid if you choose not to perform image alignment on 'Sampling' tab.""")
    joboptions["range_psi"] = rno.JobOption("Angular search range - psi (deg):", 6, 3, 30, 1, """Local angular searches will be performed \
within +/- the given amount (in degrees) from the psi priors estimated through helical segment picking. \
A range of 15 degrees is the same as sigma = 5 degrees. Note that the ranges of angular searches should be much larger than the sampling.\
\n\nThis option will be invalid if you choose not to perform image alignment on 'Sampling' tab.""")
    joboptions["do_restrict_xoff"] = rno.JobOption("Restrict helical offsets to rise:", True, """Set to Yes if you want to restrict the translational offsets along the helices to the rise of the helix given below. Set to No to allow free (conventional) translational offsets.""")
    joboptions["helical_rise"] = rno.JobOption("Helical rise (A):", 4.75, -1, 100, 1, """The helical rise (in Angstroms). Translational offsets along the helical axis will be limited from -rise/2 to +rise/2, with a flat prior.""")


    joboptions["nr_pool"] = rno.JobOption("Number of pooled particles:", 3, 1, 16, 1, """Particles arerh.PROCessed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.""")
    joboptions["do_parallel_discio"] = rno.JobOption("Use parallel disc I/O?", True, """If set to Yes, all MPI followers will read images from disc. \
Otherwise, only the leader will read images and send them through the network to the followers. Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.""")
    joboptions["do_preread_images"] = rno.JobOption("Pre-read all particles into RAM?", False, """If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. \
Because particles are read in float-precision, it will take ( N * box_size * box_size * 4 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. \
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM. \n \n If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.""")
    default_scratch = "RELION_SCRATCH_DIR"
    # if (default_scratch == NULL):
    #     default_scratch = DEFAULTSCRATCHDIR

    joboptions["scratch_dir"] = rno.JobOption("Copy particles to scratch directory:", (default_scratch), """If a directory is provided here, then the job will create a sub-directory in it called relion_volatile. If that relion_volatile directory already exists, it will be wiped. Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory. \
Provided this directory is on a fast local drive (e.g. an SSD drive),rh.PROCessing in all the iterations will be faster. If the job finishes correctly, the relion_volatile directory will be wiped. If the job crashes, you may want to remove it yourself.""")
    joboptions["do_combine_thru_disc"] = rno.JobOption("Combine iterations through disc?", False, """If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results. The MPI leader will read in all these files, combine them all, and write out a new file with the combined results. \
All MPI salves will then read in the combined results. This reduces heavy load on the network, but increases load on the disc I/O. \
This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step. It will depend on your system setup which is most efficient.""")

    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, "If set to Yes, the job will try to use GPU acceleration.")
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), """This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','. For example: '0,0:1,1:0,0:1,1'""")

    return hidden_name,joboptions

# Constructor for initial model job
def initialiseInimodelJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_inimodel"

    if (is_tomo):
        addTomoInputOptions(True, True, True, False)
    else:
        joboptions["fn_img"] = rno.JobOption("Input images STAR file:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star) \t Image stacks (not recommended, read help!) (*.{spi,mrcs})", """A STAR file with all images (and their metadata). \
In Gradient optimisation, it is very important that there are particles from enough different orientations. One only needs a few thousand to 10k particles. When selecting good 2D classes in the Subset Selection jobtype, use the option to select a maximum number of particles from each class to generate more even angular distributions for SGD.\
\n \n Alternatively, you may give a Spider/MRC stack of 2D images, but in that case NO metadata can be included and thus NO CTF correction can be performed, \
nor will it be possible to perform noise spectra estimation or intensity scale corrections in image groups. Therefore, running RELION with an input stack will in general provide sub-optimal results and is therefore not recommended!! Use the Preprocessingrh.PROCedure to get the input STAR file in a semi-automated manner. Read the RELION wiki for more information.""")

    joboptions["fn_cont"] = rno.JobOption("Continue from here: ", (""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR", """Select the *_optimiser.star file for the iteration \
from which you want to continue a previous run. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a '_ctX' to the output rootname, \
with X being the iteration from which one continues the previous run.""")

    joboptions["nr_iter"] = rno.JobOption("Number of VDAM mini-batches:", 200, 50, 500, 10, """How many iterations (i.e. mini-batches) to perform with the VDAM algorithm?""")
    joboptions["tau_fudge"] = rno.JobOption("Regularisation parameter T:", 4 , 0.1, 10, 0.1, """Bayes law strictly determines the relative weight between \
the contribution of the experimental data and the prior. However, in practice one may need to adjust this weight to put slightly more weight on \
the experimental data to allow optimal results. Values greater than 1 for this regularisation parameter (T in the JMB2011 paper) put more \
weight on the experimental data. Values around 2-4 have been observed to be useful for 3D initial model calculations""")

    joboptions["nr_classes"] = rno.JobOption("Number of classes:", 1, 1, 50, 1, """The number of classes (K) for a multi-reference ab initio SGD refinement. \
These classes will be made in an unsupervised manner, starting from a single reference in the initial iterations of the SGD, and the references will become increasingly dissimilar during the inbetween iterations.""")
    joboptions["sym_name"] = rno.JobOption("Symmetry:", ("C1"), """The initial model is always generated in C1 and then aligned to and symmetrized with the specified point group. If the automatic alignment fails, please manually rotate run_itNNN_class001.mrc (NNN is the number of iterations) so that it conforms the symmetry convention.""")
    joboptions["do_run_C1"] = rno.JobOption("Run in C1 and apply symmetry later? ", True, """If set to Yes, the gradient-driven optimisation is run in C1 and the symmetry orientation is searched and applied later. If set to No, the entire optimisation is run in the symmetry point group indicated above.""")
    joboptions["particle_diameter"] = rno.JobOption("Mask diameter (A):", 200, 0, 1000, 10, """The experimental images will be masked with a soft \
circular mask with this diameter. Make sure this radius is not set too small because that may mask away part of the signal! \
If set to a value larger than the image size no masking will be performed.\n\n\
The same diameter will also be used for a spherical mask of the reference structures if no user-provided mask is specified.""")
    joboptions["do_solvent"] = rno.JobOption("Flatten and enforce non-negative solvent?", True, """If set to Yes, the job will apply a spherical mask and enforce all values in the reference to be non-negative.""")

    if (is_tomo):
        joboptions["sigma_tilt"] = rno.JobOption("Prior width on tilt angle (deg):", -1, -1, 30, 1, """The width of the prior on the tilt angle: angular searches will be +/-3 times this value. Tilt priors will be defined when particles have been picked as filaments, on spheres or on manifolds. Setting this width to a negative value will lead to no prior being used on the tilt angle.""")

    joboptions["do_ctf_correction"] = rno.JobOption("Do CTF-correction?", True, """If set to Yes, CTFs will be corrected inside the MAP refinement. \
The resulting algorithm intrinsically implements the optimal linear, or Wiener filter. \
Note that CTF parameters for all images need to be given in the input STAR file. \
The command 'relion_refine --print_metadata_labels' will print a list of all possible metadata labels for that STAR file. \
See the RELION Wiki for more details.\n\n Also make sure that the correct pixel size (in Angstrom) is given above!)""")
    joboptions["ctf_intact_first_peak"] = rno.JobOption("Ignore CTFs until first peak?", False, """If set to Yes, then CTF-amplitude correction will \
only be performed from the first peak of each CTF onward. This can be useful if the CTF model is inadequate at the lowest resolution. \
Still, in general using higher amplitude contrast on the CTFs (e.g. 10-20%) often yields better results. \
Therefore, this option is not generally recommended: try increasing amplitude contrast (in your input STAR file) first!""")

    joboptions["do_parallel_discio"] = rno.JobOption("Use parallel disc I/O?", True, """If set to Yes, all MPI followers will read their own images from disc. \
Otherwise, only the leader will read images and send them through the network to the followers. Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.""")
    joboptions["nr_pool"] = rno.JobOption("Number of pooled particles:", 3, 1, 16, 1, """Particles arerh.PROCessed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.""")
    joboptions["do_preread_images"] = rno.JobOption("Pre-read all particles into RAM?", False, """If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. \
Because particles are read in float-precision, it will take ( N * box_size * box_size * 4 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. \
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM. \n \n If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.""")
    default_scratch = "RELION_SCRATCH_DIR"
    if (default_scratch == NULL):
        default_scratch = DEFAULTSCRATCHDIR

    joboptions["scratch_dir"] = rno.JobOption("Copy particles to scratch directory:", (default_scratch), """If a directory is provided here, then the job will create a sub-directory in it called relion_volatile. If that relion_volatile directory already exists, it will be wiped. Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory. \
Provided this directory is on a fast local drive (e.g. an SSD drive),rh.PROCessing in all the iterations will be faster. If the job finishes correctly, the relion_volatile directory will be wiped. If the job crashes, you may want to remove it yourself.""")
    joboptions["do_combine_thru_disc"] = rno.JobOption("Combine iterations through disc?", False, """If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results. The MPI leader will read in all these files, combine them all, and write out a new file with the combined results. \
All MPI salves will then read in the combined results. This reduces heavy load on the network, but increases load on the disc I/O. \
This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step. It will depend on your system setup which is most efficient.""")

    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, "If set to Yes, the job will try to use GPU acceleration.")
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), """This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','. For example: '0,0:1,1:0,0:1,1'""")

    return hidden_name,joboptions

def initialiseClass3DJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_class3d"

    if (is_tomo):
        addTomoInputOptions(True, True, True, False)

    else:
        joboptions["fn_img"] = rno.JobOption("Input images STAR file:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star)", "A STAR file with all images (and their metadata).")


    joboptions["fn_cont"] = rno.JobOption("Continue from here: ", (""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR", """Select the *_optimiser.star file for the iteration \
from which you want to continue a previous run. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a '_ctX' to the output rootname, \
with X being the iteration from which one continues the previous run.""")
    joboptions["fn_ref"] = rno.JobOption("Reference map:", "LABEL_MAP_CPIPE", 1, "", "Image Files (*.{spi,vol,mrc})", """A 3D map in MRC/Spider format. \
    Make sure this map has the same dimensions and the same pixel size as your input images, or specify that one can resize the reference if needed.""")
    joboptions["fn_mask"] = rno.JobOption("Reference mask (optional):", "LABEL_MASK_CPIPE", 1, "", "Image Files (*.{spi,vol,msk,mrc})", """\
If no mask is provided, a soft spherical mask based on the particle diameter will be used.\n\
\n\
Otherwise, provide a Spider/mrc map containing a (soft) mask with the same \
dimensions as the reference(s), and values between 0 and 1, with 1 being 100% protein and 0 being 100% solvent. \
The reconstructed reference map will be multiplied by this mask.\n\
\n\
In some cases, for example for non-empty icosahedral viruses, it is also useful to use a second mask. For all white (value 1) pixels in this second mask \
the corresponding pixels in the reconstructed map are set to the average value of these pixels. \
Thereby, for example, the higher density inside the virion may be set to a constant. \
Note that this second mask should have one-values inside the virion and zero-values in the capsid and the solvent areas. \
To use a second mask, use the additional option --solvent_mask2, which may given in the Additional arguments line (in the Running tab).""")

    joboptions["ref_correct_greyscale"] = rno.JobOption("Ref. map is on absolute greyscale?", False, """Probabilities are calculated based on a Gaussian noise model, \
which contains a squared difference term between the reference and the experimental image. This has a consequence that the \
reference needs to be on the same absolute intensity grey-scale as the experimental images. \
RELION and XMIPP reconstruct maps at their absolute intensity grey-scale. \
Other packages may perform internal normalisations of the reference density, which will result in incorrect grey-scales. \
Therefore: if the map was reconstructed in RELION or in XMIPP, set this option to Yes, otherwise set it to No. \
If set to No, RELION will use a (grey-scale invariant) cross-correlation criterion in the first iteration, \
and prior to the second iteration the map will be filtered again using the initial low-pass filter. \
Thisrh.PROCedure is relatively quick and typically does not negatively affect the outcome of the subsequent MAP refinement. \
Therefore, if in doubt it is recommended to set this option to No.""")
    joboptions["trust_ref_size"] = rno.JobOption("Resize reference if needed?", True, """If True, and if the input reference map (and mask) do not have the same pixel size and/or box size, then they will be re-scaled and re-boxed accordingly. If this option is set to False, then the program will die with an error if the reference does not have the correct pixel and/or box size.""")
    joboptions["ini_high"] = rno.JobOption("Initial low-pass filter (A):", 60, 0, 200, 5, """It is recommended to strongly low-pass filter your initial reference map. \
If it has not yet been low-pass filtered, it may be done internally using this option. \
If set to 0, no low-pass filter will be applied to the initial reference(s).""")
    joboptions["sym_name"] = rno.JobOption("Symmetry:", ("C1"), """If the molecule is asymmetric, \
set Symmetry group to C1. Note their are multiple possibilities for icosahedral symmetry: \n \
* I1: No-Crowther 222 (standard in Heymann, Chagoyen & Belnap, JSB, 151 (2005) 196–207) \n \
* I2: Crowther 222 \n \
* I3: 52-setting (as used in SPIDER?)\n \
* I4: A different 52 setting \n \
The command 'relion_refine --sym D2 --print_symmetry_ops' prints a list of all symmetry operators for symmetry group D2. \
RELION uses XMIPP's libraries for symmetry operations. \
Therefore, look at the XMIPP Wiki for more details:  http:#xmipp.cnb.csic.es/twiki/bin/view/Xmipp/WebHome?topic=Symmetry""")

    joboptions["do_ctf_correction"] = rno.JobOption("Do CTF-correction?", True, """If set to Yes, CTFs will be corrected inside the MAP refinement. \
The resulting algorithm intrinsically implements the optimal linear, or Wiener filter. \
Note that CTF parameters for all images need to be given in the input STAR file. \
The command 'relion_refine --print_metadata_labels' will print a list of all possible metadata labels for that STAR file. \
See the RELION Wiki for more details.\n\n Also make sure that the correct pixel size (in Angstrom) is given above!)""")
    joboptions["ctf_intact_first_peak"] = rno.JobOption("Ignore CTFs until first peak?", False, """If set to Yes, then CTF-amplitude correction will \
only be performed from the first peak of each CTF onward. This can be useful if the CTF model is inadequate at the lowest resolution. \
Still, in general using higher amplitude contrast on the CTFs (e.g. 10-20%) often yields better results. \
Therefore, this option is not generally recommended: try increasing amplitude contrast (in your input STAR file) first!""")

    joboptions["nr_classes"] = rno.JobOption("Number of classes:", 1, 1, 50, 1, """The number of classes (K) for a multi-reference refinement. \
These classes will be made in an unsupervised manner from a single reference by division of the data into random subsets during the first iteration.""")
    default_T =  1 if (is_tomo) else 4
    joboptions["tau_fudge"] = rno.JobOption("Regularisation parameter T:", default_T , 0.1, 10, 0.1, """Bayes law strictly determines the relative weight between \
the contribution of the experimental data and the prior. However, in practice one may need to adjust this weight to put slightly more weight on \
the experimental data to allow optimal results. Values greater than 1 for this regularisation parameter (T in the JMB2011 paper) put more \
weight on the experimental data. Values around 2-4 have been observed to be useful for 3D refinements, values of 1-2 for 2D refinements. \
Too small values yield too-low resolution structures; too high values result in over-estimated resolutions, mostly notable by the apparition of high-frequency noise in the references.""")
    joboptions["nr_iter"] = rno.JobOption("Number of iterations:", 25, 1, 50, 1, """Number of iterations to be performed. \
Note that the current implementation of 2D class averaging and 3D classification does NOT comprise a convergence criterium. \
Therefore, the calculations will need to be stopped by the user if further iterations do not yield improvements in resolution or classes. \n\n \
Also note that upon restarting, the iteration number continues to be increased, starting from the final iteration in the previous run. \
The number given here is the TOTAL number of iterations. For example, if 10 iterations have been performed previously and one restarts to perform \
an additional 5 iterations (for example with a finer angular sampling), then the number given here should be 10+5=15.""")
    joboptions["do_fast_subsets"] = rno.JobOption("Use fast subsets (for large data sets)?", False, """If set to Yes, the first 5 iterations will be done with random subsets of only K*1500 particles (K being the number of classes) the next 5 with K*4500 particles, the next 5 with 30% of the data set; and the final ones with all data. This was inspired by a cisTEM implementation by Niko Grigorieff et al.""")

    joboptions["particle_diameter"] = rno.JobOption("Mask diameter (A):", 200, 0, 1000, 10, """The experimental images will be masked with a soft \
circular mask with this diameter. Make sure this radius is not set too small because that may mask away part of the signal! \
If set to a value larger than the image size no masking will be performed.\n\n\
The same diameter will also be used for a spherical mask of the reference structures if no user-provided mask is specified.""")
    joboptions["do_zero_mask"] = rno.JobOption("Mask individual particles with zeros?", True, """If set to Yes, then in the individual particles, \
the area outside a circle with the radius of the particle will be set to zeros prior to taking the Fourier transform. \
This will remove noise and therefore increase sensitivity in the alignment and classification. However, it will also introduce correlations \
between the Fourier components that are not modelled. When set to No, then the solvent area is filled with random noise, which prevents introducing correlations.\
High-resolution refinements (e.g. ribosomes or other large complexes in 3D auto-refine) tend to work better when filling the solvent area with random noise (i.e. setting this option to No), refinements of smaller complexes and most classifications go better when using zeros (i.e. setting this option to Yes).""")
    joboptions["highres_limit"] = rno.JobOption("Limit resolution E-step to (A): ", -1, -1, 20, 1, """If set to a positive number, then the expectation step (i.e. the alignment) will be done only including the Fourier components up to this resolution (in Angstroms). \
This is useful to prevent overfitting, as the classification runs in RELION are not to be guaranteed to be 100% overfitting-free (unlike the 3D auto-refine with its gold-standard FSC). In particular for very difficult data sets, e.g. of very small or featureless particles, this has been shown to give much better class averages. \
In such cases, values in the range of 7-12 Angstroms have proven useful.""")
    joboptions["do_blush"] = rno.JobOption("Use Blush regularisation?", False, """If set to Yes, relion_refine will use a neural network to perform regularisation by denoising at every iteration, instead of the standard smoothness regularisation.""")

    joboptions["dont_skip_align"] = rno.JobOption("Perform image alignment?", True, """If set to No, then rather than \
performing both alignment and classification, only classification will be performed. This allows the use of very focused masks.\
This requires that the optimal orientations of all particles are already stored in the input STAR file. """)
    joboptions["sampling"] = rno.JobOption("Angular sampling interval:", rh.job_sampling_options, 2, """There are only a few discrete \
angular samplings possible because we use the HealPix library to generate the sampling of the first two Euler angles on the sphere. \
The samplings are approximate numbers and vary slightly over the sphere.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.""")
    joboptions["offset_range"] = rno.JobOption("Offset search range (pix):", 5, 0, 30, 1, """Probabilities will be calculated only for translations \
in a circle with this radius (in pixels). The center of this circle changes at every iteration and is placed at the optimal translation \
for each image in the previous iteration.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.""")
    joboptions["offset_step"] = rno.JobOption("Offset search step (pix):", 1, 0.1, 5, 0.1, """Translations will be sampled with this step-size (in pixels).\
Translational sampling is also done using the adaptive approach. \
Therefore, if adaptive=1, the translations will first be evaluated on a 2x coarser grid.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.""")
    joboptions["do_local_ang_searches"] = rno.JobOption("Perform local angular searches?", False, """If set to Yes, then rather than \
performing exhaustive angular searches, local searches within the range given below will be performed. \
A prior Gaussian distribution centered at the optimal orientation in the previous iteration and \
with a stddev of 1/3 of the range given below will be enforced.""")
    joboptions["sigma_angles"] = rno.JobOption("Local angular search range:", 5., 0, 15, 0.1, """Local angular searches will be performed \
within +/- the given amount (in degrees) from the optimal orientation in the previous iteration. \
A Gaussian prior (also see previous option) will be applied, so that orientations closer to the optimal orientation \
in the previous iteration will get higher weights than those further away.""")
    joboptions["allow_coarser"] = rno.JobOption("Allow coarser sampling?", False, """If set to Yes, the program will use coarser angular and translational samplings if the estimated accuracies of the assignments is still low in the earlier iterations. This may speed up the calculations.""")
    joboptions["relax_sym"] = rno.JobOption("Relax symmetry:", (""), """With this option, poses related to the standard local angular search range by the given point group will also be explored. For example, if you have a pseudo-symmetric dimer A-A', refinement or classification in C1 with symmetry relaxation by C2 might be able to improve distinction between A and A'. Note that the reference must be more-or-less aligned to the convention of (pseudo-)symmetry operators. For details, see Ilca et al 2019 and Abrishami et al 2020 cited in the About dialog.""")

    if (is_tomo):
        joboptions["sigma_tilt"] = rno.JobOption("Prior width on tilt angle (deg):", -1, -1, 30, 1, """The width of the prior on the tilt angle: angular searches will be +/-3 times this value. Tilt priors will be defined when particles have been picked as filaments, on spheres or on manifolds. Setting this width to a negative value will lead to no prior being used on the tilt angle.""")


    joboptions["do_helix"] = rno.JobOption("Do helical reconstruction?", False, "If set to Yes, then perform 3D helical reconstruction.")
    joboptions["helical_tube_inner_diameter"] = rno.JobOption("Tube diameter - inner (A):", ("-1"),"""Inner and outer diameter (in Angstroms) of the reconstructed helix spanning across Z axis. \
Set the inner diameter to negative value if the helix is not hollow in the center. The outer diameter should be slightly larger than the actual width of helical tubes because it also decides the shape of 2D \
particle mask for each segment. If the psi priors of the extracted segments are not accurate enough due to high noise level or flexibility of the structure, then set the outer diameter to a large value.""")
    joboptions["helical_tube_outer_diameter"] = rno.JobOption("Tube diameter - outer (A):", ("-1"),"""Inner and outer diameter (in Angstroms) of the reconstructed helix spanning across Z axis. \
Set the inner diameter to negative value if the helix is not hollow in the center. The outer diameter should be slightly larger than the actual width of helical tubes because it also decides the shape of 2D \
particle mask for each segment. If the psi priors of the extracted segments are not accurate enough due to high noise level or flexibility of the structure, then set the outer diameter to a large value.""")
    joboptions["range_rot"] = rno.JobOption("Angular search range - rot (deg):", ("-1"), """Local angular searches will be performed \
within +/- of the given amount (in degrees) from the optimal orientation in the previous iteration. The default negative value means that no local searches will be performed. \
A Gaussian prior will be applied, so that orientations closer to the optimal orientation \
in the previous iteration will get higher weights than those further away.\n\nThese ranges will only be applied to the \
rot, tilt and psi angles in the first few iterations (global searches for orientations) in 3D helical reconstruction. \
Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible structures and more memory and computation time will be used. \
A range of 15 degrees means sigma = 5 degrees.\n\nThese options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.""")
    joboptions["range_tilt"] = rno.JobOption("Angular search range - tilt (deg):", ("15"), """Local angular searches will be performed \
within +/- the given amount (in degrees) from the optimal orientation in the previous iteration. \
A Gaussian prior (also see previous option) will be applied, so that orientations closer to the optimal orientation \
in the previous iteration will get higher weights than those further away.\n\nThese ranges will only be applied to the \
rot, tilt and psi angles in the first few iterations (global searches for orientations) in 3D helical reconstruction. \
Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible structures and more memory and computation time will be used. \
A range of 15 degrees means sigma = 5 degrees.\n\nThese options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.""")
    joboptions["range_psi"] = rno.JobOption("Angular search range - psi (deg):", ("10"), """Local angular searches will be performed \
within +/- the given amount (in degrees) from the optimal orientation in the previous iteration. \
A Gaussian prior (also see previous option) will be applied, so that orientations closer to the optimal orientation \
in the previous iteration will get higher weights than those further away.\n\nThese ranges will only be applied to the \
rot, tilt and psi angles in the first few iterations (global searches for orientations) in 3D helical reconstruction. \
Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible structures and more memory and computation time will be used. \
A range of 15 degrees means sigma = 5 degrees.\n\nThese options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.""")
    joboptions["do_apply_helical_symmetry"] = rno.JobOption("Apply helical symmetry?", True, """If set to Yes, helical symmetry will be applied in every iteration. Set to No if you have just started a project, helical symmetry is unknown or not yet estimated.""")
    joboptions["helical_nr_asu"] = rno.JobOption("Number of unique asymmetrical units:", 1, 1, 100, 1, """Number of unique helical asymmetrical units in each segment box. If the inter-box distance (set in segment picking step) \
is 100 Angstroms and the estimated helical rise is ~20 Angstroms, then set this value to 100 / 20 = 5 (nearest integer). This integer should not be less than 1. The correct value is essential in measuring the \
signal to noise ratio in helical reconstruction.""")
    joboptions["helical_twist_initial"] =  rno.JobOption("Initial helical twist (deg):", ("0"),"""Initial helical symmetry. Set helical twist (in degrees) to positive value if it is a right-handed helix. \
Helical rise is a positive value in Angstroms. If local searches of helical symmetry are planned, initial values of helical twist and rise should be within their respective ranges.""")
    joboptions["helical_rise_initial"] = rno.JobOption("Initial helical rise (A):", ("0"), """Initial helical symmetry. Set helical twist (in degrees) to positive value if it is a right-handed helix. \
Helical rise is a positive value in Angstroms. If local searches of helical symmetry are planned, initial values of helical twist and rise should be within their respective ranges.""")
    joboptions["helical_z_percentage"] = rno.JobOption("Central Z length (%):", 30., 5., 80., 1., """Reconstructed helix suffers from inaccuracies of orientation searches. \
The central part of the box contains more reliable information compared to the top and bottom parts along Z axis, where Fourier artefacts are also present if the \
number of helical asymmetrical units is larger than 1. Therefore, information from the central part of the box is used for searching and imposing \
helical symmetry in real space. Set this value (%) to the central part length along Z axis divided by the box size. Values around 30% are commonly used.""")
    joboptions["do_local_search_helical_symmetry"] = rno.JobOption("Do local searches of symmetry?", False, "If set to Yes, then perform local searches of helical twist and rise within given ranges.")
    joboptions["helical_twist_min"] = rno.JobOption("Helical twist search (deg) - Min:", ("0"), """Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) \
to positive value if it is a right-handed helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_twist_max"] = rno.JobOption("Helical twist search (deg) - Max:", ("0"), """Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) \
to positive value if it is a right-handed helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_twist_inistep"] = rno.JobOption("Helical twist search (deg) - Step:", ("0"), """Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) \
to positive value if it is a right-handed helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_rise_min"] = rno.JobOption("Helical rise search (A) - Min:", ("0"), """Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. \
Generally it is not necessary for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_rise_max"] = rno.JobOption("Helical rise search (A) - Max:", ("0"), """Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. \
Generally it is not necessary for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_rise_inistep"] = rno.JobOption("Helical rise search (A) - Step:", ("0"), """Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. \
Generally it is not necessary for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_range_distance"] = rno.JobOption("Range factor of local averaging:", -1., 1., 5., 0.1, """Local averaging of orientations and translations will be performed within a range of +/- this value * the box size. Polarities are also set to be the same for segments coming from the same tube during local refinement. \
Values of ~ 2.0 are recommended for flexible structures such as MAVS-CARD filaments, ParM, MamK, etc. This option might not improve the reconstructions of helices formed from curled 2D lattices (TMV and VipA/VipB). Set to negative to disable this option.""")
    joboptions["keep_tilt_prior_fixed"] = rno.JobOption("Keep tilt-prior fixed:", True, """If set to yes, the tilt prior will not change during the optimisation. If set to No, at each iteration the tilt prior will move to the optimal tilt value for that segment from the previous iteration.""")

    joboptions["do_parallel_discio"] = rno.JobOption("Use parallel disc I/O?", True, """If set to Yes, all MPI followers will read their own images from disc. \
Otherwise, only the leader will read images and send them through the network to the followers. Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.""")
    joboptions["nr_pool"] = rno.JobOption("Number of pooled particles:", 3, 1, 16, 1, """Particles arerh.PROCessed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.""")
    joboptions["do_pad1"] = rno.JobOption("Skip padding?", False, """If set to Yes, the calculations will not use padding in Fourier space for better interpolation in the references. Otherwise, references are padded 2x before Fourier transforms are calculated. Skipping padding (i.e. use --pad 1) gives nearly as good results as using --pad 2, but some artifacts may appear in the corners from signal that is folded back.""")
    joboptions["do_preread_images"] = rno.JobOption("Pre-read all particles into RAM?", False, """If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. \
Because particles are read in float-precision, it will take ( N * box_size * box_size * 4 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. \
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM. \n \n If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.""")
    default_scratch = "RELION_SCRATCH_DIR"
    if (default_scratch == NULL):
        default_scratch = DEFAULTSCRATCHDIR

    joboptions["scratch_dir"] = rno.JobOption("Copy particles to scratch directory:", (default_scratch), """If a directory is provided here, then the job will create a sub-directory in it called relion_volatile. If that relion_volatile directory already exists, it will be wiped. Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory. \
Provided this directory is on a fast local drive (e.g. an SSD drive),rh.PROCessing in all the iterations will be faster. If the job finishes correctly, the relion_volatile directory will be wiped. If the job crashes, you may want to remove it yourself.""")
    joboptions["do_combine_thru_disc"] = rno.JobOption("Combine iterations through disc?", False, """If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results. The MPI leader will read in all these files, combine them all, and write out a new file with the combined results. \
All MPI salves will then read in the combined results. This reduces heavy load on the network, but increases load on the disc I/O. \
This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step. It will depend on your system setup which is most efficient.""")

    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, "If set to Yes, the job will try to use GPU acceleration.")
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), """This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','.  For example: '0,0:1,1:0,0:1,1'""")

    return hidden_name,joboptions

def initialiseAutorefineJob(is_tomo):
    type = rh.PROC_3DAUTO

    joboptions = {}
    hidden_name = ".gui_auto3d"

    if (is_tomo):
        addTomoInputOptions(True, True, True, False)

    else:
        joboptions["fn_img"] = rno.JobOption("Input images STAR file:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star)", "A STAR file with all images (and their metadata).")


    joboptions["fn_cont"] = rno.JobOption("Continue from here: ", (""), "STAR Files (*_it*_optimiser.star)", "CURRENT_ODIR", """Select the *_optimiser.star file for the iteration \
from which you want to continue a previous run. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a '_ctX' to the output rootname, \
with X being the iteration from which one continues the previous run.""")
    joboptions["fn_ref"] = rno.JobOption("Reference map:", "LABEL_MAP_CPIPE", 1, "", "Image Files (*.{spi,vol,mrc})", """A 3D map in MRC/Spider format. \
    Make sure this map has the same dimensions and the same pixel size as your input images, or specify that one can resize the reference if needed.""")
    joboptions["fn_mask"] = rno.JobOption("Reference mask (optional):", "LABEL_MASK_CPIPE", 1, "", "Image Files (*.{spi,vol,msk,mrc})", """\
If no mask is provided, a soft spherical mask based on the particle diameter will be used.\n\
\n\
Otherwise, provide a Spider/mrc map containing a (soft) mask with the same \
dimensions as the reference(s), and values between 0 and 1, with 1 being 100% protein and 0 being 100% solvent. \
The reconstructed reference map will be multiplied by this mask.\n\
\n\
In some cases, for example for non-empty icosahedral viruses, it is also useful to use a second mask. For all white (value 1) pixels in this second mask \
the corresponding pixels in the reconstructed map are set to the average value of these pixels. \
Thereby, for example, the higher density inside the virion may be set to a constant. \
Note that this second mask should have one-values inside the virion and zero-values in the capsid and the solvent areas. \
To use a second mask, use the additional option --solvent_mask2, which may given in the Additional arguments line (in the Running tab).""")

    joboptions["ref_correct_greyscale"] = rno.JobOption("Ref. map is on absolute greyscale?", False, """Probabilities are calculated based on a Gaussian noise model, \
which contains a squared difference term between the reference and the experimental image. This has a consequence that the \
reference needs to be on the same absolute intensity grey-scale as the experimental images. \
RELION and XMIPP reconstruct maps at their absolute intensity grey-scale. \
Other packages may perform internal normalisations of the reference density, which will result in incorrect grey-scales. \
Therefore: if the map was reconstructed in RELION or in XMIPP, set this option to Yes, otherwise set it to No. \
If set to No, RELION will use a (grey-scale invariant) cross-correlation criterion in the first iteration, \
and prior to the second iteration the map will be filtered again using the initial low-pass filter. \
Thisrh.PROCedure is relatively quick and typically does not negatively affect the outcome of the subsequent MAP refinement. \
Therefore, if in doubt it is recommended to set this option to No.""")
    joboptions["trust_ref_size"] = rno.JobOption("Resize reference if needed?", True, """If True, and if the input reference map (and mask) do not have the same pixel size and/or box size, then they will be re-scaled and re-boxed accordingly. If this option is set to False, then the program will die with an error if the reference does not have the correct pixel and/or box size.""")
    joboptions["ini_high"] = rno.JobOption("Initial low-pass filter (A):", 60, 0, 200, 5, """It is recommended to strongly low-pass filter your initial reference map. \
If it has not yet been low-pass filtered, it may be done internally using this option. \
If set to 0, no low-pass filter will be applied to the initial reference(s).""")
    joboptions["sym_name"] = rno.JobOption("Symmetry:", ("C1"), """If the molecule is asymmetric, \
set Symmetry group to C1. Note their are multiple possibilities for icosahedral symmetry: \n \
* I1: No-Crowther 222 (standard in Heymann, Chagoyen & Belnap, JSB, 151 (2005) 196–207) \n \
* I2: Crowther 222 \n \
* I3: 52-setting (as used in SPIDER?)\n \
* I4: A different 52 setting \n \
The command 'relion_refine --sym D2 --print_symmetry_ops' prints a list of all symmetry operators for symmetry group D2. \
RELION uses XMIPP's libraries for symmetry operations. \
Therefore, look at the XMIPP Wiki for more details:  http:#xmipp.cnb.csic.es/twiki/bin/view/Xmipp/WebHome?topic=Symmetry""")

    joboptions["do_ctf_correction"] = rno.JobOption("Do CTF-correction?", True, """If set to Yes, CTFs will be applied to the projections of the map. This requires that CTF information is present in the input STAR file.""")
    joboptions["ctf_intact_first_peak"] = rno.JobOption("Ignore CTFs until first peak?", False, """If set to Yes, then CTF-amplitude correction will \
only be performed from the first peak of each CTF onward. This can be useful if the CTF model is inadequate at the lowest resolution. \
Still, in general using higher amplitude contrast on the CTFs (e.g. 10-20%) often yields better results. \
Therefore, this option is not generally recommended: try increasing amplitude contrast (in your input STAR file) first!""")

    joboptions["particle_diameter"] = rno.JobOption("Mask diameter (A):", 200, 0, 1000, 10, """The experimental images will be masked with a soft \
circular mask with this diameter. Make sure this radius is not set too small because that may mask away part of the signal! \
If set to a value larger than the image size no masking will be performed.\n\n\
The same diameter will also be used for a spherical mask of the reference structures if no user-provided mask is specified.""")
    joboptions["do_zero_mask"] = rno.JobOption("Mask individual particles with zeros?", True, """If set to Yes, then in the individual particles, \
the area outside a circle with the radius of the particle will be set to zeros prior to taking the Fourier transform. \
This will remove noise and therefore increase sensitivity in the alignment and classification. However, it will also introduce correlations \
between the Fourier components that are not modelled. When set to No, then the solvent area is filled with random noise, which prevents introducing correlations.\
High-resolution refinements (e.g. ribosomes or other large complexes in 3D auto-refine) tend to work better when filling the solvent area with random noise (i.e. setting this option to No), refinements of smaller complexes and most classifications go better when using zeros (i.e. setting this option to Yes).""")
    joboptions["do_solvent_fsc"] = rno.JobOption("Use solvent-flattened FSCs?", False, """If set to Yes, then instead of using unmasked maps to calculate the gold-standard FSCs during refinement, \
masked half-maps are used and a post-processing-like correction of the FSC curves (with phase-randomisation) is performed every iteration. This only works when a reference mask is provided on the I/O tab. \
This may yield higher-resolution maps, especially when the mask contains only a relatively small volume inside the box.""")
    joboptions["do_blush"] = rno.JobOption("Use Blush regularisation?", False, """If set to Yes, relion_refine will use a neural network to perform regularisation by denoising at every iteration, instead of the standard smoothness regularisation.""")

    joboptions["sampling"] = rno.JobOption("Initial angular sampling:", rh.job_sampling_options, 2, """There are only a few discrete \
angular samplings possible because we use the HealPix library to generate the sampling of the first two Euler angles on the sphere. \
The samplings are approximate numbers and vary slightly over the sphere.\n\n \
Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.""")
    joboptions["offset_range"] = rno.JobOption("Initial offset range (pix):", 5, 0, 30, 1, """Probabilities will be calculated only for translations \
in a circle with this radius (in pixels). The center of this circle changes at every iteration and is placed at the optimal translation \
for each image in the previous iteration.\n\n \
Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.""")
    joboptions["offset_step"] = rno.JobOption("Initial offset step (pix):", 1, 0.1, 5, 0.1, """Translations will be sampled with this step-size (in pixels).\
Translational sampling is also done using the adaptive approach. \
Therefore, if adaptive=1, the translations will first be evaluated on a 2x coarser grid.\n\n \
Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.""")
    joboptions["auto_local_sampling"] = rno.JobOption("Local searches from auto-sampling:", rh.job_sampling_options, 4, """In the automatedrh.PROCedure to \
increase the angular samplings, local angular searches of -6/+6 times the sampling rate will be used from this angular sampling rate onwards. For most \
lower-symmetric particles a value of 1.8 degrees will be sufficient. Perhaps icosahedral symmetries may benefit from a smaller value such as 0.9 degrees.""")
    joboptions["relax_sym"] = rno.JobOption("Relax symmetry:", (""), """With this option, poses related to the standard local angular search range by the given point group will also be explored. For example, if you have a pseudo-symmetric dimer A-A', refinement or classification in C1 with symmetry relaxation by C2 might be able to improve distinction between A and A'. Note that the reference must be more-or-less aligned to the convention of (pseudo-)symmetry operators. For details, see Ilca et al 2019 and Abrishami et al 2020 cited in the About dialog.""")
    joboptions["auto_faster"] = rno.JobOption("Use finer angular sampling faster?", False, """If set to Yes, then let auto-refinementrh.PROCeed faster with finer angular samplings. Two additional command-line options will be passed to the refine program: \n \n \
--auto_ignore_angles lets angular sampling go down despite changes still happening in the angles \n \n \
--auto_resol_angles lets angular sampling go down if the current resolution already requires that sampling at the edge of the particle.  \n\n \
This option will make the computation faster, but hasn't been tested for many cases for potential loss in reconstruction quality upon convergence.""")

    if (is_tomo):
        joboptions["sigma_tilt"] = rno.JobOption("Prior width on tilt angle (deg):", -1, -1, 30, 1, """The width of the prior on the tilt angle: angular searches will be +/-3 times this value. Tilt priors will be defined when particles have been picked as filaments, on spheres or on manifolds. Setting this width to a negative value will lead to no prior being used on the tilt angle.""")

    joboptions["do_helix"] = rno.JobOption("Do helical reconstruction?", False, "If set to Yes, then perform 3D helical reconstruction.")
    joboptions["helical_tube_inner_diameter"] = rno.JobOption("Tube diameter - inner (A):", ("-1"),"""Inner and outer diameter (in Angstroms) of the reconstructed helix spanning across Z axis. \
Set the inner diameter to negative value if the helix is not hollow in the center. The outer diameter should be slightly larger than the actual width of helical tubes because it also decides the shape of 2D \
particle mask for each segment. If the psi priors of the extracted segments are not accurate enough due to high noise level or flexibility of the structure, then set the outer diameter to a large value.""")
    joboptions["helical_tube_outer_diameter"] = rno.JobOption("Tube diameter - outer (A):", ("-1"),"""Inner and outer diameter (in Angstroms) of the reconstructed helix spanning across Z axis. \
Set the inner diameter to negative value if the helix is not hollow in the center. The outer diameter should be slightly larger than the actual width of helical tubes because it also decides the shape of 2D \
particle mask for each segment. If the psi priors of the extracted segments are not accurate enough due to high noise level or flexibility of the structure, then set the outer diameter to a large value.""")
    joboptions["range_rot"] = rno.JobOption("Angular search range - rot (deg):", ("-1"), """Local angular searches will be performed \
within +/- of the given amount (in degrees) from the optimal orientation in the previous iteration. The default negative value means that no local searches will be performed. \
A Gaussian prior will be applied, so that orientations closer to the optimal orientation \
in the previous iteration will get higher weights than those further away.\n\nThese ranges will only be applied to the \
rot, tilt and psi angles in the first few iterations (global searches for orientations) in 3D helical reconstruction. \
Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible structures and more memory and computation time will be used. \
A range of 15 degrees means sigma = 5 degrees.\n\nThese options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.""")
    joboptions["range_tilt"] = rno.JobOption("Angular search range - tilt (deg):", ("15"), """Local angular searches will be performed \
within +/- the given amount (in degrees) from the optimal orientation in the previous iteration. \
A Gaussian prior (also see previous option) will be applied, so that orientations closer to the optimal orientation \
in the previous iteration will get higher weights than those further away.\n\nThese ranges will only be applied to the \
rot, tilt and psi angles in the first few iterations (global searches for orientations) in 3D helical reconstruction. \
Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible structures and more memory and computation time will be used. \
A range of 15 degrees means sigma = 5 degrees.\n\nThese options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.""")
    joboptions["range_psi"] = rno.JobOption("Angular search range - psi (deg):", ("10"), """Local angular searches will be performed \
within +/- the given amount (in degrees) from the optimal orientation in the previous iteration. \
A Gaussian prior (also see previous option) will be applied, so that orientations closer to the optimal orientation \
in the previous iteration will get higher weights than those further away.\n\nThese ranges will only be applied to the \
rot, tilt and psi angles in the first few iterations (global searches for orientations) in 3D helical reconstruction. \
Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible structures and more memory and computation time will be used. \
A range of 15 degrees means sigma = 5 degrees.\n\nThese options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.""")
    joboptions["do_apply_helical_symmetry"] = rno.JobOption("Apply helical symmetry?", True, """If set to Yes, helical symmetry will be applied in every iteration. Set to No if you have just started a project, helical symmetry is unknown or not yet estimated.""")
    joboptions["helical_nr_asu"] = rno.JobOption("Number of unique asymmetrical units:", 1, 1, 100, 1, """Number of unique helical asymmetrical units in each segment box. If the inter-box distance (set in segment picking step) \
is 100 Angstroms and the estimated helical rise is ~20 Angstroms, then set this value to 100 / 20 = 5 (nearest integer). This integer should not be less than 1. The correct value is essential in measuring the \
signal to noise ratio in helical reconstruction.""")
    joboptions["helical_twist_initial"] =  rno.JobOption("Initial helical twist (deg):", ("0"),"""Initial helical symmetry. Set helical twist (in degrees) to positive value if it is a right-handed helix. \
Helical rise is a positive value in Angstroms. If local searches of helical symmetry are planned, initial values of helical twist and rise should be within their respective ranges.""")
    joboptions["helical_rise_initial"] = rno.JobOption("Initial helical rise (A):", ("0"), """Initial helical symmetry. Set helical twist (in degrees) to positive value if it is a right-handed helix. \
Helical rise is a positive value in Angstroms. If local searches of helical symmetry are planned, initial values of helical twist and rise should be within their respective ranges.""")
    joboptions["helical_z_percentage"] = rno.JobOption("Central Z length (%):", 30., 5., 80., 1., """Reconstructed helix suffers from inaccuracies of orientation searches. \
The central part of the box contains more reliable information compared to the top and bottom parts along Z axis, where Fourier artefacts are also present if the \
number of helical asymmetrical units is larger than 1. Therefore, information from the central part of the box is used for searching and imposing \
helical symmetry in real space. Set this value (%) to the central part length along Z axis divided by the box size. Values around 30% are commonly used.""")
    joboptions["do_local_search_helical_symmetry"] = rno.JobOption("Do local searches of symmetry?", False, "If set to Yes, then perform local searches of helical twist and rise within given ranges.")
    joboptions["helical_twist_min"] = rno.JobOption("Helical twist search (deg) - Min:", ("0"), """Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) \
to positive value if it is a right-handed helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_twist_max"] = rno.JobOption("Helical twist search (deg) - Max:", ("0"), """Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) \
to positive value if it is a right-handed helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_twist_inistep"] = rno.JobOption("Helical twist search (deg) - Step:", ("0"), """Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) \
to positive value if it is a right-handed helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_rise_min"] = rno.JobOption("Helical rise search (A) - Min:", ("0"), """Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. \
Generally it is not necessary for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_rise_max"] = rno.JobOption("Helical rise search (A) - Max:", ("0"), """Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. \
Generally it is not necessary for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_rise_inistep"] = rno.JobOption("Helical rise search (A) - Step:", ("0"), """Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. \
Generally it is not necessary for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.""")
    joboptions["helical_range_distance"] = rno.JobOption("Range factor of local averaging:", -1., 1., 5., 0.1, """Local averaging of orientations and translations will be performed within a range of +/- this value * the box size. Polarities are also set to be the same for segments coming from the same tube during local refinement. \
Values of ~ 2.0 are recommended for flexible structures such as MAVS-CARD filaments, ParM, MamK, etc. This option might not improve the reconstructions of helices formed from curled 2D lattices (TMV and VipA/VipB). Set to negative to disable this option.""")
    joboptions["keep_tilt_prior_fixed"] = rno.JobOption("Keep tilt-prior fixed:", True, """If set to yes, the tilt prior will not change during the optimisation. If set to No, at each iteration the tilt prior will move to the optimal tilt value for that segment from the previous iteration.""")

    joboptions["do_parallel_discio"] = rno.JobOption("Use parallel disc I/O?", True, """If set to Yes, all MPI followers will read their own images from disc. \
Otherwise, only the leader will read images and send them through the network to the followers. Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.""")
    joboptions["nr_pool"] = rno.JobOption("Number of pooled particles:", 3, 1, 16, 1, """Particles arerh.PROCessed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.""")
    joboptions["do_pad1"] = rno.JobOption("Skip padding?", False, """If set to Yes, the calculations will not use padding in Fourier space for better interpolation in the references. Otherwise, references are padded 2x before Fourier transforms are calculated. Skipping padding (i.e. use --pad 1) gives nearly as good results as using --pad 2, but some artifacts may appear in the corners from signal that is folded back.""")
    joboptions["do_preread_images"] = rno.JobOption("Pre-read all particles into RAM?", False, """If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. \
Because particles are read in float-precision, it will take ( N * box_size * box_size * 8 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. \
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM. \n \n If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.""")
    default_scratch = "RELION_SCRATCH_DIR"
    if (default_scratch == None):
        default_scratch = "DEFAULTSCRATCHDIR"

    joboptions["scratch_dir"] = rno.JobOption("Copy particles to scratch directory:", (default_scratch), """If a directory is provided here, then the job will create a sub-directory in it called relion_volatile. If that relion_volatile directory already exists, it will be wiped. Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory. \
Provided this directory is on a fast local drive (e.g. an SSD drive),rh.PROCessing in all the iterations will be faster. If the job finishes correctly, the relion_volatile directory will be wiped. If the job crashes, you may want to remove it yourself.""")
    joboptions["do_combine_thru_disc"] = rno.JobOption("Combine iterations through disc?", False, """If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results. The MPI leader will read in all these files, combine them all, and write out a new file with the combined results. \
All MPI salves will then read in the combined results. This reduces heavy load on the network, but increases load on the disc I/O. \
This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step. It will depend on your system setup which is most efficient.""")
    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, "If set to Yes, the job will try to use GPU acceleration.")
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), """This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','.  For example: '0,0:1,1:0,0:1,1'""")


    return hidden_name,joboptions

def initialiseMultiBodyJob(is_tomo):
    type =rh.PROC_MULTIBODY

    joboptions = {}
    hidden_name = ".gui_multibody"

    joboptions["fn_in"] = rno.JobOption("Consensus refinement optimiser.star: ", (""), "STAR Files (run_it*_optimiser.star)", "Refine3D/.", """Select the *_optimiser.star file for the iteration of the consensus refinement \
from which you want to start multi-body refinement.""")

    joboptions["fn_cont"] = rno.JobOption("Continue from here: ", (""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR", """Select the *_optimiser.star file for the iteration \
from which you want to continue this multi-body refinement. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a '_ctX' to the output rootname, \
with X being the iteration from which one continues the previous run.""")

    joboptions["fn_bodies"] = rno.JobOption("Body STAR file:", (""), "STAR Files (*.{star})", ".", """ Provide the STAR file with all information about the bodies to be used in multi-body refinement. \
An example for a three-body refinement would look like this: \n\
\n\
data_\n\
loop_\n\
_rlnBodyMaskName\n\
_rlnBodyRotateRelativeTo\n\
_rlnBodySigmaAngles\n\
_rlnBodySigmaOffset\n\
large_body_mask.mrc 2 10 2\n\
small_body_mask.mrc 1 10 2\n\
head_body_mask.mrc 2 10 2\n\
\n\
Where each data line represents a different body, and: \n \
 - rlnBodyMaskName contains the name of a soft-edged mask with values in [0,1] that define the body; \n\
 - rlnBodyRotateRelativeTo defines relative to which other body this body rotates (first body is number 1) \n\
 - rlnBodySigmaAngles and _rlnBodySigmaOffset are the standard deviations (widths) of Gaussian priors on the consensus rotations and translations; \n\
\n \
Optionally, there can be a fifth column with _rlnBodyReferenceName. Entries can be 'None' (without the ''s) or the name of a MRC map with an initial reference for that body. In case the entry is None, the reference will be taken from the density in the consensus refinement.\n \n\
Also note that larger bodies should be above smaller bodies in the STAR file. For more information, see the multi-body paper.""")

    joboptions["do_subtracted_bodies"] = rno.JobOption("Reconstruct subtracted bodies?", True, """If set to Yes, then the reconstruction of each of the bodies will use the subtracted images. This may give \
useful insights about how well the subtraction worked. If set to No, the original particles are used for reconstruction (while the subtracted ones are still used for alignment). This will result in fuzzy densities for bodies outside the one used for refinement.""")
    joboptions["do_blush"] = rno.JobOption("Use Blush regularisation?", False, """If set to Yes, relion_refine will use a neural network to perform regularisation by denoising at every iteration, instead of the standard smoothness regularisation.""")

    joboptions["sampling"] = rno.JobOption("Initial angular sampling:", rh.job_sampling_options, 4, """There are only a few discrete \
angular samplings possible because we use the HealPix library to generate the sampling of the first two Euler angles on the sphere. \
The samplings are approximate numbers and vary slightly over the sphere.\n\n \
Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.""")
    joboptions["offset_range"] = rno.JobOption("Initial offset range (pix):", 3, 0, 30, 1, """Probabilities will be calculated only for translations \
in a circle with this radius (in pixels). The center of this circle changes at every iteration and is placed at the optimal translation \
for each image in the previous iteration.\n\n \
Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.""")
    joboptions["offset_step"] = rno.JobOption("Initial offset step (pix):", 0.75, 0.1, 5, 0.1, """Translations will be sampled with this step-size (in pixels).\
Translational sampling is also done using the adaptive approach. \
Therefore, if adaptive=1, the translations will first be evaluated on a 2x coarser grid.\n\n \
Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.""")


    joboptions["do_analyse"] = rno.JobOption("Run flexibility analysis?", True, """If set to Yes, after the multi-body refinement has completed, a PCA analysis will be run on the orientations all all bodies in the data set. This can be set to No initially, and then the job can be continued afterwards to only perform this analysis.""")
    joboptions["nr_movies"] = rno.JobOption("Number of eigenvector movies:", 3, 0, 16, 1, """Series of ten output maps will be generated along this many eigenvectors. These maps can be opened as a 'Volume Series' in UCSF Chimera, and then displayed as a movie. They represent the principal motions in the particles.""")
    joboptions["do_select"] = rno.JobOption("Select particles based on eigenvalues?", False, """If set to Yes, a particles.star file is written out with all particles that have the below indicated eigenvalue in the selected range.""")
    joboptions["select_eigenval"] = rno.JobOption("Select on eigenvalue:", 1, 1, 20, 1, """This is the number of the eigenvalue to be used in the particle subset selection (start counting at 1).""")
    joboptions["eigenval_min"] = rno.JobOption("Minimum eigenvalue:", -999., -50, 50, 1, """This is the minimum value for the selected eigenvalue; only particles with the selected eigenvalue larger than this value will be included in the output particles.star file""")
    joboptions["eigenval_max"] = rno.JobOption("Maximum eigenvalue:", 999., -50, 50, 1, """This is the maximum value for the selected eigenvalue; only particles with the selected eigenvalue less than this value will be included in the output particles.star file""")

    joboptions["do_parallel_discio"] = rno.JobOption("Use parallel disc I/O?", True, """If set to Yes, all MPI followers will read their own images from disc. \
Otherwise, only the leader will read images and send them through the network to the followers. Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.""")
    joboptions["nr_pool"] = rno.JobOption("Number of pooled particles:", 3, 1, 16, 1, """Particles arerh.PROCessed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.""")
    joboptions["do_pad1"] = rno.JobOption("Skip padding?", False, """If set to Yes, the calculations will not use padding in Fourier space for better interpolation in the references. Otherwise, references are padded 2x before Fourier transforms are calculated. Skipping padding (i.e. use --pad 1) gives nearly as good results as using --pad 2, but some artifacts may appear in the corners from signal that is folded back.""")
    joboptions["do_preread_images"] = rno.JobOption("Pre-read all particles into RAM?", False, """If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. \
Because particles are read in float-precision, it will take ( N * box_size * box_size * 8 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. \
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM. \n \n If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.""")
    default_scratch = "RELION_SCRATCH_DIR"
    if (default_scratch == NULL):
        default_scratch = DEFAULTSCRATCHDIR

    joboptions["scratch_dir"] = rno.JobOption("Copy particles to scratch directory:", (default_scratch), """If a directory is provided here, then the job will create a sub-directory in it called relion_volatile. If that relion_volatile directory already exists, it will be wiped. Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory. \
Provided this directory is on a fast local drive (e.g. an SSD drive),rh.PROCessing in all the iterations will be faster. If the job finishes correctly, the relion_volatile directory will be wiped. If the job crashes, you may want to remove it yourself.""")
    joboptions["do_combine_thru_disc"] = rno.JobOption("Combine iterations through disc?", False, """If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results. The MPI leader will read in all these files, combine them all, and write out a new file with the combined results. \
All MPI salves will then read in the combined results. This reduces heavy load on the network, but increases load on the disc I/O. \
This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step. It will depend on your system setup which is most efficient.""")
    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, "If set to Yes, the job will try to use GPU acceleration.")
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), """This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','.  For example: '0,0:1,1:0,0:1,1'""")




    return hidden_name,joboptions

def initialiseMaskcreateJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_maskcreate"

    joboptions["fn_in"] = rno.JobOption("Input 3D map:", "LABEL_MAP_CPIPE", 1, "", "MRC map files (*.mrc)", "Provide an input MRC map from which to start binarizing the map.")

    joboptions["lowpass_filter"] = rno.JobOption("Lowpass filter map (A)", 15, 10, 100, 5, """Lowpass filter that will be applied to the input map, prior to binarization. To calculate solvent masks, a lowpass filter of 15-20A may work well.""")
    joboptions["angpix"] = rno.JobOption("Pixel size (A)", -1, 0.3, 5, 0.1, """Provide the pixel size of the input map in Angstroms to calculate the low-pass filter. This value is also used in the output image header.""")

    joboptions["inimask_threshold"] = rno.JobOption("Initial binarisation threshold:", 0.02, 0., 0.5, 0.01, """This threshold is used to make an initial binary mask from the average of the two unfiltered half-reconstructions. \
If you don't know what value to use, display one of the unfiltered half-maps in a 3D surface rendering viewer and find the lowest threshold that gives no noise peaks outside the reconstruction.""")
    joboptions["extend_inimask"] = rno.JobOption("Extend binary map this many pixels:", 3, 0, 20, 1, "The initial binary mask is extended this number of pixels in all directions." )
    joboptions["width_mask_edge"] = rno.JobOption("Add a soft-edge of this many pixels:", 3, 0, 20, 1, """The extended binary mask is further extended with a raised-cosine soft edge of the specified width.""" )

    joboptions["do_helix"] = rno.JobOption("Mask a 3D helix?", False, "Generate a mask for 3D helix which spans across Z axis of the box.")
    joboptions["helical_z_percentage"] = rno.JobOption("Central Z length (%):", 30., 5., 80., 1., """Reconstructed helix suffers from inaccuracies of orientation searches. \
The central part of the box contains more reliable information compared to the top and bottom parts along Z axis. Set this value (%) to the central part length along Z axis divided by the box size. Values around 30% are commonly used but you may want to try different lengths.""")




    return hidden_name,joboptions

def initialiseJoinstarJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_joinstar"

    joboptions["do_part"] = rno.JobOption("Combine particle STAR files?", False, "")
    joboptions["fn_part1"] = rno.JobOption("Particle STAR file 1: ", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", "The first of the particle STAR files to be combined.")
    joboptions["fn_part2"] = rno.JobOption("Particle STAR file 2: ", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", "The second of the particle STAR files to be combined.")
    joboptions["fn_part3"] = rno.JobOption("Particle STAR file 3: ", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", """The third of the particle STAR files to be combined. Leave empty if there are only two files to be combined.""")
    joboptions["fn_part4"] = rno.JobOption("Particle STAR file 4: ", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", """The fourth of the particle STAR files to be combined. Leave empty if there are only two or three files to be combined.""")

    joboptions["do_mic"] = rno.JobOption("Combine micrograph STAR files?", False, "")
    joboptions["fn_mic1"] = rno.JobOption("Micrograph STAR file 1: ", "LABEL_MICS_CPIPE", 1, "", "micrograph STAR file (*.star)", "The first of the micrograph STAR files to be combined.")
    joboptions["fn_mic2"] = rno.JobOption("Micrograph STAR file 2: ", "LABEL_MICS_CPIPE", 1, "", "micrograph STAR file (*.star)", "The second of the micrograph STAR files to be combined.")
    joboptions["fn_mic3"] = rno.JobOption("Micrograph STAR file 3: ", "LABEL_MICS_CPIPE", 1, "", "micrograph STAR file (*.star)", """The third of the micrograph STAR files to be combined. Leave empty if there are only two files to be combined.""")
    joboptions["fn_mic4"] = rno.JobOption("Micrograph STAR file 4: ", "LABEL_MICS_CPIPE", 1, "", "micrograph STAR file (*.star)", """The fourth of the micrograph STAR files to be combined. Leave empty if there are only two or three files to be combined.""")

    joboptions["do_mov"] = rno.JobOption("Combine movie STAR files?", False, "")
    joboptions["fn_mov1"] = rno.JobOption("Movie STAR file 1: ", "LABEL_MOVIES_CPIPE", 1, "", "movie STAR file (*.star)", "The first of the micrograph movie STAR files to be combined.")
    joboptions["fn_mov2"] = rno.JobOption("Movie STAR file 2: ", "LABEL_MOVIES_CPIPE", 1, "", "movie STAR file (*.star)", "The second of the micrograph movie STAR files to be combined.")
    joboptions["fn_mov3"] = rno.JobOption("Movie STAR file 3: ", "LABEL_MOVIES_CPIPE", 1, "", "movie STAR file (*.star)", """The third of the micrograph movie STAR files to be combined. Leave empty if there are only two files to be combined.""")
    joboptions["fn_mov4"] = rno.JobOption("Movie STAR file 4: ", "LABEL_MOVIES_CPIPE", 1, "", "movie STAR file (*.star)", """The fourth of the micrograph movie STAR files to be combined. Leave empty if there are only two or three files to be combined.""")


    return hidden_name,joboptions

def initialiseSubtractJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_subtract"

    joboptions["fn_opt"] = rno.JobOption("Input optimiser.star: ",rh.LABEL_OPTIMISER_CPIPE, 1, "", "STAR Files (*_optimiser.star)", """Select the *_optimiser.star file for the iteration of the 3D refinement/classification \
which you want to use for subtraction. It will use the maps from this run for the subtraction, and of no particles input STAR file is given below, it will use all of the particles from this run.""")
    joboptions["fn_mask"] = rno.JobOption("Mask of the signal to keep:", "LABEL_MASK_CPIPE", 1, "", "Image Files (*.{spi,vol,msk,mrc})", """Provide a soft mask where the protein density you wish to subtract from the experimental particles is black (0) and the density you wish to keep is white (1).""")
    joboptions["do_data"] = rno.JobOption("Use different particles?", False, """If set to Yes, subtraction will be performed on the particles in the STAR file below, instead of on all the particles of the 3D refinement/classification from the optimiser.star file.""")
    joboptions["fn_data"] = rno.JobOption("Input particle star file:", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", """The particle STAR files with particles that will be used in the subtraction. Leave this field empty if all particles from the input refinement/classification run are to be used.""")
    joboptions["do_float16"] = rno.JobOption("Write output in float16?", True ,"""If set to Yes, this program will write output images in float16 MRC format. This will save a factor of two in disk space compared to the default of writing in float32. Note that RELION and CCPEM will read float16 images, but other programs may not (yet) do so.""")

    joboptions["do_fliplabel"] = rno.JobOption("OR revert to original particles?", False, """If set to Yes, no signal subtraction is performed. Instead, the labels of rlnImageName and rlnImageOriginalName are flipped in the input STAR file given in the field below. This will make the STAR file point back to the original, non-subtracted images.""")
    joboptions["fn_fliplabel"] = rno.JobOption("revert this particle star file:", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", "The particle STAR files with particles that will be used for label reversion.")

    joboptions["do_center_mask"] = rno.JobOption("Do center subtracted images on mask?", True, """If set to Yes, the subtracted particles will be centered on projections of the center-of-mass of the input mask.""")
    joboptions["do_center_xyz"] = rno.JobOption("Do center on my coordinates?", False, """If set to Yes, the subtracted particles will be centered on projections of the x,y,z coordinates below. The unit is pixel, not angstrom. The origin is at the center of the box, not at the corner.""")
    joboptions["center_x"] = rno.JobOption("Center coordinate (pix) - X:", ("0"), "X-coordinate of the 3D center (in pixels).")
    joboptions["center_y"] = rno.JobOption("Center coordinate (pix) - Y:", ("0"), "Y-coordinate of the 3D center (in pixels).")
    joboptions["center_z"] = rno.JobOption("Center coordinate (pix) - Z:", ("0"), "Z-coordinate of the 3D center (in pixels).")

    joboptions["new_box"] = rno.JobOption("New box size:", -1, 64, 512, 32, "Provide a non-negative value to re-window the subtracted particles in a smaller box size." )




    return hidden_name,joboptions

def initialisePostprocessJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_post"

    joboptions["fn_in"] = rno.JobOption("One of the 2 unfiltered half-maps:",rh.LABEL_HALFMAP_CPIPE, 1, "", "MRC map files (*half1*.mrc)",  """Provide one of the two unfiltered half-reconstructions that were output upon convergence of a 3D auto-refine run.""")
    joboptions["fn_mask"] = rno.JobOption("Solvent mask:", "LABEL_MASK_CPIPE", 1, "", "Image Files (*.{spi,vol,msk,mrc})", """Provide a soft mask where the protein is white (1) and the solvent is black (0). Often, the softer the mask the higher resolution estimates you will get. A soft edge of 5-10 pixels is often a good edge width.""")
    joboptions["angpix"] = rno.JobOption("Calibrated pixel size (A)", -1, 0.3, 5, 0.1, """Provide the final, calibrated pixel size in Angstroms. This value may be different from the pixel-size used thus far, e.g. when you have recalibrated the pixel size using the fit to a PDB model. The X-axis of the output FSC plot will use this calibrated value.""")

    joboptions["do_auto_bfac"] = rno.JobOption("Estimate B-factor automatically?", True, """If set to Yes, then the program will use the automatedrh.PROCedure described by Rosenthal and Henderson (2003, JMB) to estimate an overall B-factor for your map, and sharpen it accordingly. \
Note that your map must extend well beyond the lowest resolution included in therh.PROCedure below, which should not be set to resolutions much lower than 10 Angstroms. """)
    joboptions["autob_lowres"] = rno.JobOption("Lowest resolution for auto-B fit (A):", 10, 8, 15, 0.5, """This is the lowest frequency (in Angstroms) that will be included in the linear fit of the Guinier plot as described in Rosenthal and Henderson (2003, JMB). Dont use values much lower or higher than 10 Angstroms. If your map does not extend beyond 10 Angstroms, then instead of the automatedrh.PROCedure use your own B-factor.""")
    joboptions["do_adhoc_bfac"] = rno.JobOption("Use your own B-factor?", False, """Instead of using the automated B-factor estimation, provide your own value. Use negative values for sharpening the map. \
This option is useful if your map does not extend beyond the 10A needed for the automatedrh.PROCedure, or when the automatedrh.PROCedure does not give a suitable value (e.g. in more disordered parts of the map).""")
    joboptions["adhoc_bfac"] = rno.JobOption("User-provided B-factor:", -1000, -2000, 0, -50, """Use negative values for sharpening. Be careful: if you over-sharpen your map, you may end up interpreting noise for signal!""")

    joboptions["fn_mtf"] = rno.JobOption("MTF of the detector (STAR file)", "", "STAR Files (*.star)", ".", """If you know the MTF of your detector, provide it here. Curves for some well-known detectors may be downloaded from the RELION Wiki. Also see there for the exact format \
\n If you do not know the MTF of your detector and do not want to measure it, then by leaving this entry empty, you include the MTF of your detector in your overall estimated B-factor upon sharpening the map.\
Although that is probably slightly less accurate, the overall quality of your map will probably not suffer very much.""")
    joboptions["mtf_angpix"] = rno.JobOption("Original detector pixel size:", 1.0, 0.3, 2.0, 0.1, """This is the original pixel size (in Angstroms) in the raw (non-super-resolution!) micrographs.""")

    joboptions["do_skip_fsc_weighting"] = rno.JobOption("Skip FSC-weighting?", False, """If set to No (the default), then the output map will be low-pass filtered according to the mask-corrected, gold-standard FSC-curve. \
Sometimes, it is also useful to provide an ad-hoc low-pass filter (option below), as due to local resolution variations some parts of the map may be better and other parts may be worse than the overall resolution as measured by the FSC. \
In such cases, set this option to Yes and provide an ad-hoc filter as described below.""")
    joboptions["low_pass"] = rno.JobOption("Ad-hoc low-pass filter (A):",5,1,40,1,"""This option allows one to low-pass filter the map at a user-provided frequency (in Angstroms). When using a resolution that is higher than the gold-standard FSC-reported resolution, take care not to interpret noise in the map for signal...""")




    return hidden_name,joboptions

def initialiseLocalresJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_localres"

    joboptions["fn_in"] = rno.JobOption("One of the 2 unfiltered half-maps:",rh.LABEL_HALFMAP_CPIPE, 1, "", "MRC map files (*half1*.mrc)",  """Provide one of the two unfiltered half-reconstructions that were output upon convergence of a 3D auto-refine run.""")
    joboptions["angpix"] = rno.JobOption("Calibrated pixel size (A)", 1, 0.3, 5, 0.1, """Provide the final, calibrated pixel size in Angstroms. This value may be different from the pixel-size used thus far, e.g. when you have recalibrated the pixel size using the fit to a PDB model. The X-axis of the output FSC plot will use this calibrated value.""")

    # Check for environment variable RELION_RESMAP_TEMPLATE
    default_location = RELION_RESMAP_EXECUTABLE
    default_resmap = DEFAULTRESMAPLOCATION
    if (default_location == NULL):
        default_location = default_resmap


    joboptions["do_resmap_locres"] = rno.JobOption("Use ResMap?", True, "If set to Yes, then ResMap will be used for local resolution estimation.")
    joboptions["fn_resmap"] = rno.JobOption("ResMap executable:", (default_location), "ResMap*", ".", """Location of the ResMap executable. You can control the default of this field by setting environment variable RELION_RESMAP_EXECUTABLE, or by editing the first few lines in src/gui_jobwindow.h and recompile the code. \n \n Note that the ResMap wrapper cannot use MPI.""")
    joboptions["fn_mask"] = rno.JobOption("User-provided solvent mask:", "LABEL_MASK_CPIPE", 1, "", "Image Files (*.{spi,vol,msk,mrc})", """Provide a mask with values between 0 and 1 around all domains of the complex. ResMap uses this mask for local resolution calculation. RELION does NOT use this mask for calculation, but makes a histogram of local resolution within this mask.""")
    joboptions["pval"] = rno.JobOption("P-value:", 0.05, 0., 1., 0.01, """This value is typically left at 0.05. If you change it, report the modified value in your paper!""")
    joboptions["minres"] = rno.JobOption("Highest resolution (A): ", 0., 0., 10., 0.1, """ResMaps minRes parameter. By default (0), the program will start at just above 2x the pixel size""")
    joboptions["maxres"] = rno.JobOption("Lowest resolution (A): ", 0., 0., 10., 0.1, """ResMaps maxRes parameter. By default (0), the program will stop at 4x the pixel size""")
    joboptions["stepres"] = rno.JobOption("Resolution step size (A)", 1., 0.1, 3, 0.1, "ResMaps stepSize parameter." )

    joboptions["do_relion_locres"] = rno.JobOption("Use Relion?", False, """If set to Yes, then relion_postprocess will be used for local-rtesolution estimation. This program basically performs a series of post-processing operations with a small soft, spherical mask that is moved over the entire map, while using phase-randomisation to estimate the convolution effects of that mask. \
\n \n The output relion_locres.mrc map can be used to color the surface of a map in UCSF Chimera according to its local resolution. The output relion_locres_filtered.mrc is a composite map that is locally filtered to the estimated resolution. \
This is a developmental feature in need of further testing, but initial results indicate it may be useful. \n \n Note that only this program can use MPI, the ResMap wrapper cannot use MPI.""")

    #joboptions["locres_sampling"] = rno.JobOption("Sampling rate (A):", 25, 5, 50, 5, """The local-resolution map will be calculated every so many Angstroms, by placing soft spherical masks on a cubic grid with this spacing. Very fine samplings (e.g. < 15A?) may take a long time to compute and give spurious estimates!""")
    #joboptions["randomize_at"] = rno.JobOption("Frequency for phase-randomisation (A): ", 10., 5, 20., 1, """From this frequency onwards, the phases for the mask-corrected FSC-calculation will be randomized. Make sure this is a lower resolution (i.e. a higher number) than the local resolutions you are after in your map.""")
    joboptions["adhoc_bfac"] = rno.JobOption("User-provided B-factor:", -100, -500, 0, -25, """Probably, the overall B-factor as was estimated in the postprocess is a useful value for here. Use negative values for sharpening. Be careful: if you over-sharpen your map, you may end up interpreting noise for signal!""")
    joboptions["fn_mtf"] = rno.JobOption("MTF of the detector (STAR file)", "", "STAR Files (*.star)", ".", """The MTF of the detector is used to complement the user-provided B-factor in the sharpening. If you don't have this curve, you can leave this field empty.""")





    return hidden_name,joboptions

def initialiseDynaMightJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_dynamight"

    joboptions["fn_star"] = rno.JobOption("Input images STAR file:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star) \t Image stacks (not recommended, read help!) (*.{spi,mrcs})", "A STAR file with all images (and their metadata).")
    joboptions["fn_map"] = rno.JobOption("Consensus map:", "LABEL_MAP_CPIPE", 1, "", "Image Files (*.{spi,vol,mrc})", """A 3D map in MRC/Spider format. Make sure this map has the same dimensions and the same pixel size as your input images.""")
    #joboptions["fn_mask"] = rno.JobOption("Mask (optional):", "LABEL_MASK_CPIPE", "", "Image Files (*.{spi,vol,msk,mrc})", """Provide a mask to limit deformations to a specific region of the consensus structure. Regions outside the mask will be kept fized and will not be visualised.""")
    joboptions["gpu_id"] = rno.JobOption("Which (single) GPU to use:", ("0"), """Note that DynaMight can only use one GPU at a time. Data sets with many particles or large box sizes will require powerful GPUs, like an A100.""")
    joboptions["do_preload"] = rno.JobOption("Preload images in RAM?", False, """If set to Yes, dynamight will preload images into memory for learning the forward or inverse deformations and for deformed backprojection. This will speed up the calculations, but you need to make sure you have enough RAM to do so.""")
    joboptions["fn_dynamight_exe"] = rno.JobOption("DynaMight executable:", ("relion_python_dynamight"), """The DynaMight executable. By default, the relion_python_dynamight will be used, which was installed inside conda with a typical relion install. Only change this if that version is giving you problems.""")

    joboptions["nr_gaussians"] = rno.JobOption("Number of Gaussians: ", 10000, 5000, 40000, 1000, """Number of Gaussians to describe the consensus map with. Larger structures that one wishes to describe at higher resolutions will need more Gaussians. As a rule of thumb, you could try and use 1-2 Gaussians per amino acid or nucleotide in your complex. But note that running DynaMight with more than 30,000 Gaussians may be problematic on GPUs with a memory of 24 GB.""")
    joboptions["initial_threshold"] = rno.JobOption("Initial map threshold (optional): ",("") , """If provided, this threshold will be used to position initial Gaussians in the consensus map. If left empty, an automatedrh.PROCedure will be used to estimate the appropriate threshold.""")
    joboptions["reg_factor"] = rno.JobOption("Regularization factor: ", 1, 0.2, 5, 0.1, """This regularization factor defines the relative weights between the data over the restraints. Values higher than one will put more weights on the restraints.""")

    joboptions["fn_checkpoint"] = rno.JobOption("Checkpoint file:", (""), "Checkpoint files (*.pth)", "CURRENT_ODIR/forward_deformations/checkpoints", """Select the checkpoint file to use for visualization, inverse deformation estimation or deformed backprojection. If left empty, the last available checkpoint file will be used""")

    joboptions["do_visualize"] = rno.JobOption("Do visualization?", False, """If set to Yes, dynamight will be run to visualize the latent space and deformed models. One can also save series of maps to make movies in Chimera, or STAR files of particle subsets within this task.""")
    joboptions["halfset"] = rno.JobOption("Half-set to visualize: ", 1, 0, 2, 1, """Select halfset 1 or 2 to explore the latent space of that halfset. If you select halfset 0, then the validation set is being visualised, which will give you an estimate of the errors in the deformations.""")

    joboptions["do_inverse"] = rno.JobOption("Do inverse-deformation estimation?", False, """If set to Yes, dynamight will be run to estimate inverse-deformations. These are necessary if one want to perform deformed backprojection to calculate an improved consensus model.""")
    joboptions["nr_epochs"] = rno.JobOption("Number of epochs to perform: ", 200, 50, 500, 10, """Number of epochs to perform inverse deformations. You can monitor the convergence of the loss function to assess how many are necessary. Often 200 are enough""")
    joboptions["do_store_deform"] = rno.JobOption("Store deformations in RAM?", False, """If set to Yes, dynamight will store deformations in the GPU memory, which will speed up the calculations, but you need to have enough GPU memory to do this...""")

    joboptions["do_reconstruct"] = rno.JobOption("Do deformed backprojection?", False, """If set to Yes, dynamight will be run to perform a deformed backprojection, using inverse-deformations from a previous task, to get an improved consensus reconstruction.""")
    joboptions["backproject_batchsize"] = rno.JobOption("Backprojection batchsize: ", 10, 1, 500, 10, """Number of images torh.PROCess in parallel. This will speed up the calculation, but will cost GPU memory. Try how high you can go on your GPU, given your box size and size of the neural network.""")





    return hidden_name,joboptions

def initialiseModelAngeloJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_modelangelo"

    joboptions["fn_map"] = rno.JobOption("B-factor sharpened map:", "LABEL_MAP_CPIPE", 1, "", "MRC map files (*.mrc)",  """Provide a (RELION-postprocessed) B-factor sharpened map for model building""")
    joboptions["p_seq"] = rno.JobOption("FASTA sequence for proteins:",rh.LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})",  """Provide a FASTA file with sequences for all protein chains to be built in the map. You can leave this empty if you don't know the proteins that are there, and then run a HMMer search to identify the unknown proteins. ModelAngelo will build much better models when provided with a FASTA sequence file!""")
    joboptions["d_seq"] = rno.JobOption("FASTA sequence for DNA:",rh.LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})",  "Provide a FASTA file with sequences for all DNA chains to be built in the map.")
    joboptions["r_seq"] = rno.JobOption("FASTA sequence for RNA:",rh.LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})",  "Provide a FASTA file with sequences for all RNA chains to be built in the map.")
    joboptions["fn_modelangelo_exe"] = rno.JobOption("ModelAngelo executable:", ("relion_python_modelangelo"), """The modelangelo executable. By default, the relion_python_modelangelo will be used, which was installed inside conda with a typical relion install. Only change this if that version is giving you problems.""")
    joboptions["gpu_id"] = rno.JobOption("Which GPUs to use:", ("0"), """Provide a number for the GPU to be used (e.g. 0, 1 etc). Use comma-separated values to use multiple GPUs, e.g. 0,1,2""")

    joboptions["do_hhmer"] = rno.JobOption("Perform HMMer search?", False ,"""If set to Yes, model-angelo will perform a HMM search using HHMer in the output directory of the model-angelo run (without sequence). You can continue an old run with this option switched on, and the model building step will be skipped if the output .cif exists. This way, you can try multiple HHMer runs.""")
    joboptions["fn_lib"] = rno.JobOption("Library with sequences for HMMer search:",rh.LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})", """FASTA file with library with all sequences for HMMer search. This is often an entire proteome.""")
    joboptions["alphabet"] = rno.JobOption("Alphabet for the HMMer search:", job_modelangelo_alphabet_options, 0, "Type of Alphabet for HMM searches.")
    joboptions["F1"] = rno.JobOption("HMMSearch F1: ", 0.02, 1., 10., 0.1, """F1 parameter for HMMSearch, see their documentation at http:#eddylab.org/software/hmmer/Userguide.pdf""")
    joboptions["F2"] = rno.JobOption("HMMSearch F2: ", 0.001, 1., 10., 0.1, """F2 parameter for HMMSearch, see their documentation at http:#eddylab.org/software/hmmer/Userguide.pdf""")
    joboptions["F3"] = rno.JobOption("HMMSearch F3: ", 0.00001, 0., 10., 0.1, """F3 parameter for HMMSearch, see their documentation at http:#eddylab.org/software/hmmer/Userguide.pdf""")
    joboptions["E"] = rno.JobOption("HMMSearch E: ", 10, 0., 100., 10, """E parameter for HMMSearch, see their documentation at http:#eddylab.org/software/hmmer/Userguide.pdf""")



    return hidden_name,joboptions

def initialiseMotionrefineJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_bayespolish"

    # I/O
    joboptions["fn_mic"] = rno.JobOption("Micrographs (from MotionCorr):", "LABEL_MICS_CPIPE", 1, "", "STAR files (*.star)", """The input STAR file with the micrograph (and their movie metadata) from a MotionCorr job.""")
    joboptions["fn_data"] = rno.JobOption("Particles (from Refine3D or CtfRefine):", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star)", "The input STAR file with the metadata of all particles.")
    joboptions["fn_post"] = rno.JobOption("Postprocess STAR file:", "LABEL_POSTPROCESS_CPIPE", 1, "", "STAR files (postprocess.star)", """The STAR file generated by a PostProcess job. \
The mask used for this postprocessing will be applied to the unfiltered half-maps and should encompass the entire complex. The resulting FSC curve will be used for weighting the different frequencies.""")
    joboptions["do_float16"] = rno.JobOption("Write output in float16?", True ,"""If set to Yes, this program will write output images in float16 MRC format. This will save a factor of two in disk space compared to the default of writing in float32. Note that RELION and CCPEM will read float16 images, but other programs may not (yet) do so.""")

    # Frame range
    joboptions["first_frame"] = rno.JobOption("First movie frame: ", 1., 1., 10., 1, "First movie frame to take into account in motion fit and combination step")
    joboptions["last_frame"] = rno.JobOption("Last movie frame: ", -1., 5., 50., 1, """Last movie frame to take into account in motion fit and combination step. Values equal to or smaller than 0 mean 'use all frames'.""")

    joboptions["extract_size"] = rno.JobOption("Extraction size (pix in unbinned movie):", -1, 64, 1024, 8, """Size of the extracted particles in the unbinned original movie(in pixels). This should be an even number.""")
    joboptions["rescale"] = rno.JobOption("Re-scaled size (pixels): ", -1, 64, 1024, 8, "The re-scaled value needs to be an even number.")

    # Parameter optimisation
    joboptions["do_param_optim"] = rno.JobOption("Train optimal parameters?", False, """If set to Yes, then relion_motion_refine will estimate optimal parameter values for the three sigma values above on a subset of the data (determined by the minimum number of particles to be used below).""")
    joboptions["eval_frac"] = rno.JobOption("Fraction of Fourier pixels for testing: ", 0.5, 0, 1., 0.01, """This fraction of Fourier pixels (at higher resolution) will be used for evaluation of the parameters (test set), whereas the rest (at lower resolution) will be used for parameter estimation itself (work set).""")
    joboptions["optim_min_part"] = rno.JobOption("Use this many particles: ", 10000, 5000, 50000, 1000, """Use at least this many particles for the meta-parameter optimisation. The more particles the more expensive in time and computer memory the calculation becomes, but the better the results may get.""")

    # motion_fit
    joboptions["do_polish"] = rno.JobOption("Perform particle polishing?", True, """If set to Yes, then relion_motion_refine will be run to estimate per-particle motion-tracks using the parameters below, and polished particles will be generated.""")
    joboptions["opt_params"] = rno.JobOption("Optimised parameter file:", "LABEL_POLISH_PARAMS", 1, "", "TXT files (*.txt)", """The output TXT file from a previous Bayesian polishing job in which the optimal parameters were determined.""")
    joboptions["do_own_params"] = rno.JobOption("OR use your own parameters?", False, """If set to Yes, then the field for the optimised parameter file will be ignored and the parameters specified below will be used instead.""")
    joboptions["sigma_vel"] = rno.JobOption("Sigma for velocity (A/dose): ", 0.2, 1., 10., 0.1, """Standard deviation for the velocity regularisation. Smaller values requires the tracks to be shorter.""")
    joboptions["sigma_div"] = rno.JobOption("Sigma for divergence (A): ", 5000, 0, 10000, 10000, """Standard deviation for the divergence of tracks across the micrograph. Smaller values requires the tracks to be spatially more uniform in a micrograph.""")
    joboptions["sigma_acc"] = rno.JobOption("Sigma for acceleration (A/dose): ", 2, -1, 7, 0.1, """Standard deviation for the acceleration regularisation. Smaller values requires the tracks to be straighter.""")

    #combine_frames
    joboptions["minres"] = rno.JobOption("Minimum resolution for B-factor fit (A): ", 20, 8, 40, 1, """The minimum spatial frequency (in Angstrom) used in the B-factor fit.""")
    joboptions["maxres"] = rno.JobOption("Maximum resolution for B-factor fit (A): ", -1, -1, 15, 1, """The maximum spatial frequency (in Angstrom) used in the B-factor fit. If a negative value is given, the maximum is determined from the input FSC curve.""")


    return hidden_name,joboptions

def initialiseCtfrefineJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_ctfrefine"

    # I/O
    joboptions["fn_data"] = rno.JobOption("Particles (from Refine3D):", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star)", "The input STAR file with the metadata of all particles.")
    joboptions["fn_post"] = rno.JobOption("Postprocess STAR file:", "LABEL_POSTPROCESS_CPIPE", 1, "", "STAR files (postprocess.star)", """The STAR file generated by a PostProcess job. \
The mask used for this postprocessing will be applied to the unfiltered half-maps and should encompass the entire complex. The resulting FSC curve will be used for weighting the different frequencies. \n \n Note that for helices it is common practice to use a mask only encompassing the central 30% or so of the box. \
This gives higher resolution estimates, as it disregards ill-defined regions near the box edges. However, for ctf_refine it is better to use a mask encompassing (almost) the entire box, as otherwise there may not be enough signal.""")

    joboptions["minres"] = rno.JobOption("Minimum resolution for fits (A): ", 30, 8, 40, 1, """The minimum spatial frequency (in Angstrom) used in the beamtilt fit.""")

    # Defocus fit
    joboptions["do_ctf"] = rno.JobOption("Perform CTF parameter fitting?", True, """If set to Yes, then relion_ctf_refine will be used to estimate the selected parameters below.""")
    joboptions["do_defocus"] = rno.JobOption("Fit defocus?", rh.job_ctffit_options, 0, """If set to per-particle or per-micrograph, then relion_ctf_refine will estimate defocus values.""")
    joboptions["do_astig"] = rno.JobOption("Fit astigmatism?", rh.job_ctffit_options, 0, """If set to per-particle or per-micrograph, then relion_ctf_refine will estimate astigmatism.""")
    joboptions["do_bfactor"] = rno.JobOption("Fit B-factor?", rh.job_ctffit_options, 0, """If set to per-particle or per-micrograph, then relion_ctf_refine will estimate B-factors that describe the signal falloff.""")
    joboptions["do_phase"] = rno.JobOption("Fit phase-shift?", rh.job_ctffit_options, 0, """If set to per-particle or per-micrograph, then relion_ctf_refine will estimate (VPP?) phase shift values.""")

    # aberrations
    joboptions["do_aniso_mag"] = rno.JobOption("Estimate (anisotropic) magnification?", False, """If set to Yes, then relion_ctf_refine will also estimate the (anisotropic) magnification per optics group. \
This option cannot be done simultaneously with higher-order aberration estimation. It's probably best to estimate the one that is most off first, and the other one second. It might be worth repeating the estimation if both are off.""")

    joboptions["do_tilt"] = rno.JobOption("Estimate beamtilt?", False, """If set to Yes, then relion_ctf_refine will also estimate the beamtilt per optics group. This option is only recommended for data sets that extend beyond 4.5 Angstrom resolution.""")
    joboptions["do_trefoil"] = rno.JobOption("Also estimate trefoil?", False, """If set to Yes, then relion_ctf_refine will also estimate the trefoil (3-fold astigmatism) per optics group. This option is only recommended for data sets that extend beyond 3.5 Angstrom resolution.""")

    joboptions["do_4thorder"] = rno.JobOption("Estimate 4th order aberrations?", False, """If set to Yes, then relion_ctf_refine will also estimate the Cs and the tetrafoil (4-fold astigmatism) per optics group. This option is only recommended for data sets that extend beyond 3 Angstrom resolution.""")


    return hidden_name,joboptions

def initialiseExternalJob(is_tomo):
    joboptions = {}
    hidden_name = ".gui_external"

    # I/O
    joboptions["fn_exe"] = rno.JobOption("External executable:", "", "", ".", """Location of the script that will launch the external program. This script should write all its output in the directory specified with --o. Also, it should write in that same directory a file called RELION_JOB_EXIT_SUCCESS upon successful exit, and RELION_JOB_EXIT_FAILURE upon failure.""")

    # Optional input nodes
    joboptions["in_mov"] = rno.JobOption("Input movies: ", "LABEL_MOVIES_CPIPE", 1, "", "movie STAR file (*.star)", "Input movies. This will be passed with a --in_movies argument to the executable.")
    joboptions["in_mic"] = rno.JobOption("Input micrographs: ", "LABEL_MICS_CPIPE", 1, "", "micrographs STAR file (*.star)", "Input micrographs. This will be passed with a --in_mics argument to the executable.")
    joboptions["in_part"] = rno.JobOption("Input particles: ", "LABEL_PARTS_CPIPE", 1, "", "particles STAR file (*.star)", "Input particles. This will be passed with a --in_parts argument to the executable.")
    joboptions["in_coords"] = rno.JobOption("Input coordinates: ", "LABEL_COORDS_CPIPE", 1, "", "STAR files (coords_suffix*.star)", "Input coordinates. This will be passed with a --in_coords argument to the executable.")
    joboptions["in_3dref"] = rno.JobOption("Input 3D reference: ", "LABEL_MAP_CPIPE", 1, "", "MRC files (*.mrc)", "Input 3D reference map. This will be passed with a --in_3dref argument to the executable.")
    joboptions["in_mask"] = rno.JobOption("Input 3D mask: ", "LABEL_MASK_CPIPE", 1, "", "MRC files (*.mrc)", "Input 3D mask. This will be passed with a --in_mask argument to the executable.")

    # Optional parameters
    joboptions["param1_label"] = rno.JobOption("Param1 - label:", (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param1_value"] = rno.JobOption("Param1 - value:" , (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param2_label"] = rno.JobOption("Param2 - label:", (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param2_value"] = rno.JobOption("Param2 - value:" , (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param3_label"] = rno.JobOption("Param3 - label:", (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param3_value"] = rno.JobOption("Param3 - value:" , (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param4_label"] = rno.JobOption("Param4 - label:", (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param4_value"] = rno.JobOption("Param4 - value:" , (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param5_label"] = rno.JobOption("Param5 - label:", (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param5_value"] = rno.JobOption("Param5 - value:" , (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param6_label"] = rno.JobOption("Param6 - label:", (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param6_value"] = rno.JobOption("Param6 - value:" , (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param7_label"] = rno.JobOption("Param7 - label:", (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param7_value"] = rno.JobOption("Param7 - value:" , (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param8_label"] = rno.JobOption("Param8 - label:", (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param8_value"] = rno.JobOption("Param8 - value:" , (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param9_label"] = rno.JobOption("Param9 - label:", (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param9_value"] = rno.JobOption("Param9 - value:" , (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param10_label"] = rno.JobOption("Param10 - label:", (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")
    joboptions["param10_value"] = rno.JobOption("Param10 - value:" , (""), """Define label and value for optional parameters to the script. These will be passed as an argument --label value""")

def getCommandsImportJob(is_tomo):
    pass

# Initialise
def initialise(_job_type):
    type = _job_type

    has_mpi = False 
    has_thread =  False
    if (type == rh.PROC_IMPORT):
        has_mpi = has_thread = False
        initialiseImportJob()
        result = getCommandsImportJob(outputname, commands, final_command, do_makedir, job_counter, error_message)

    elif (type == rh.PROC_MOTIONCORR):
        has_mpi = has_thread = True
        initialiseMotioncorrJob()

    elif (type == rh.PROC_CTFFIND):
        has_mpi = True
        has_thread = False
        initialiseCtffindJob()

    elif (type == rh.PROC_MANUALPICK):
        has_mpi = has_thread = False
        initialiseManualpickJob()

    elif (type == rh.PROC_AUTOPICK):
        has_mpi = True
        has_thread = False
        initialiseAutopickJob()

    elif (type == rh.PROC_EXTRACT):
        has_mpi = True
        has_thread = False
        initialiseExtractJob()

    elif (type == rh.PROC_CLASSSELECT):
        has_mpi = has_thread = False
        initialiseSelectJob()

    elif (type == rh.PROC_2DCLASS):
        has_mpi = has_thread = True
        initialiseClass2DJob()

    elif (type == rh.PROC_INIMODEL):
        has_mpi = has_thread = True
        initialiseInimodelJob()

    elif (type == rh.PROC_3DCLASS):
        has_mpi = has_thread = True
        initialiseClass3DJob()

    elif (type == rh.PROC_3DAUTO):
        has_mpi = has_thread = True
        initialiseAutorefineJob()

    elif (type == rh.PROC_MULTIBODY):
        has_mpi = has_thread = True
        initialiseMultiBodyJob()

    elif (type == rh.PROC_MASKCREATE):
        has_mpi = False
        has_thread = True
        initialiseMaskcreateJob()

    elif (type == rh.PROC_JOINSTAR):
        has_mpi = has_thread = False
        initialiseJoinstarJob()

    elif (type == rh.PROC_SUBTRACT):
        has_mpi = True
        has_thread = False
        initialiseSubtractJob()

    elif (type == rh.PROC_POST):
        has_mpi = has_thread = False
        initialisePostprocessJob()

    elif (type == rh.PROC_RESMAP):
        has_mpi = True
        has_thread = False
        initialiseLocalresJob()

    elif (type == rh.PROC_MOTIONREFINE):
        has_mpi = has_thread = True
        initialiseMotionrefineJob()

    elif (type == rh.PROC_CTFREFINE):
        has_mpi = has_thread = True
        initialiseCtfrefineJob()

    elif (type == rh.PROC_DYNAMIGHT):
        has_mpi = False
        has_thread = True
        initialiseDynaMightJob()

    elif (type == rh.PROC_MODELANGELO):
        has_mpi = has_thread = False
        initialiseModelAngeloJob()

    elif (type == rh.PROC_TOMO_IMPORT):
        has_mpi = has_thread = False
        initialiseTomoImportJob()

    elif (type == rh.PROC_TOMO_EXCLUDE_TILT_IMAGES):
        has_mpi = has_thread = False
        initialiseTomoExcludeTiltImagesJob()

    elif (type == rh.PROC_TOMO_ALIGN_TILTSERIES):
        has_mpi = True
        has_thread = False
        initialiseTomoAlignTiltSeriesJob()

    elif (type == rh.PROC_TOMO_RECONSTRUCT_TOMOGRAM):
        has_mpi = has_thread = True
        initialiseTomoReconstructTomogramsJob()

    elif (type == rh.PROC_TOMO_DENOISE_TOMOGRAM):
        has_mpi = has_thread = False
        initialiseTomoDenoiseTomogramsJob()

    elif (type == rh.PROC_TOMO_PICK_TOMOGRAM):
        has_mpi = has_thread = False
        initialiseTomoPickTomogramsJob()

    elif (type == rh.PROC_TOMO_EXCLUDE_TILT_IMAGES):
        has_mpi = has_thread = False
        initialiseTomoExcludeTiltImagesJob()

    elif (type == rh.PROC_TOMO_SUBTOMO):
        has_mpi = has_thread = True
        initialiseTomoSubtomoJob()

    elif (type == rh.PROC_TOMO_CTFREFINE):
        has_mpi = has_thread = True
        initialiseTomoCtfRefineJob()

    elif (type == rh.PROC_TOMO_ALIGN):
        has_mpi = has_thread = True
        initialiseTomoAlignJob()

    elif (type == rh.PROC_TOMO_RECONSTRUCT):
        has_mpi = has_thread = True
        initialiseTomoReconPartJob()

    elif (type == rh.PROC_EXTERNAL):
        has_mpi = False
        has_thread = True
        initialiseExternalJob()

    else:
        print("ERROR: unrecognised job-type")

def init_table(name):
    return f'#\nloop_\n{name}.id\n{name}.label\n{name}.widget\n{name}.default\n{name}.arg0\n{name}.arg1\n{name}.arg2\n{name}.help\n'

joboptions = {}


def init_joboptions():
    global joboptions
    joboptions = {}


def get_joboptions():
    # print(joboptions)
    return joboptions

if __name__ == '__main__' :
    is_tomo = False
    tables = {'indata': init_table('_indata'), 'odata': init_table('_odata'), 'general': init_table('_general')}
    # initialise(rh.PROC_CTFFIND)
    # initialise(rh.PROC_3DAUTO)
    initialise(rh.PROC_MOTIONCORR)
    for e in joboptions.keys():
        if joboptions[e].widget == 'node':
            joboptions[e].widget = 'file'
            joboptions[e].arg2 = 'inode'
            tables['indata'] += joboptions[e].to_star(e) + '\n'
        elif joboptions[e].widget == 'select':
            print('select + option')
            tables['general'] += joboptions[e].to_star(e) + '\n'
            # Children
            parent = e
            if parent not in tables:
                tables[parent] = init_table(f'_{parent}')
            for opt in joboptions[e].radio_options:
                # TODO
                tables[parent] += opt.to_star(parent) + '\n'
        else:
            tables['general'] += joboptions[e].to_star(e) + '\n'

    for t in tables:
        print(tables[t])
