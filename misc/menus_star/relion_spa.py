import relion_h as rh
import relion_option as rno
import relion_spa_commands as rcom
import os

# Helper to get boolean from joboption
def get_bool(key):
    if key not in joboptions: return False
    val = joboptions[key].value
    return str(val).lower() == "true" or val is True

# Helper to get string
def get_str(key):
    if key not in joboptions: return ""
    return str(joboptions[key].value)

class Node:
    def __init__(self, filename, label):
        self.filename = filename
        self.label = label


def initialiseImportJob():
    hidden_name = ".gui_import"

    joboptions["do_raw"] = rno.JobOption("Import raw movies/micrographs?", True, "")
    joboptions["fn_in_raw"] = rno.JobOption("Raw input files:", "Micrographs/*.tif", "Movie or Image (*.{mrc,mrcs,tif,tiff,eer,mrc.bz2,mrcs.bz2,mrc.zst,mrcs.zst,mrc.xz,mrcs.xz})", ".", "");
    joboptions["is_multiframe"] = rno.JobOption("Are these multi-frame movies?", True, "")

    joboptions["optics_group_name"] = rno.JobOption("Optics group name:", "opticsGroup1", "")
    joboptions["fn_mtf"] = rno.JobOption("MTF of the detector:", "", "STAR Files (*.star)", ".", "")

    joboptions["angpix"] = rno.JobOption("Pixel size (Angstrom):", 1.4, 0.5, 3, 0.1, "")
    joboptions["kV"] = rno.JobOption("Voltage (kV):", 300, 50, 500, 10, "")
    joboptions["Cs"] = rno.JobOption("Spherical aberration (mm):", 2.7, 0, 8, 0.1, "")
    joboptions["Q0"] = rno.JobOption("Amplitude contrast:", 0.1, 0, 0.3, 0.01, "")
    joboptions["beamtilt_x"] = rno.JobOption("Beamtilt in X (mrad):", 0.0, -1.0, 1.0, 0.1, "")
    joboptions["beamtilt_y"] = rno.JobOption("Beamtilt in Y (mrad):", 0.0, -1.0, 1.0, 0.1, "")


    joboptions["do_other"] = rno.JobOption("Import other node types?", False, "")

    joboptions["fn_in_other"] = rno.JobOption("Input file:", "ref.mrc", "Input file (*.*)", ".", "")

    joboptions["node_type"] = rno.JobOption("Node type:", job_nodetype_options, 0, "")
    joboptions["optics_group_particles"] = rno.JobOption("Rename optics group for particles:", "", "")

    return joboptions

def initialiseMotioncorrJob():
    hidden_name = ".gui_motioncorr";

    if (is_tomo):
        joboptions["input_star_mics"] = rno.JobOption("Input tilt series: ", LABEL_TOMOGRAMS_CPIPE, 1, "", "Tilt series STAR file (*.star)", "");

    else:
        joboptions["input_star_mics"] = rno.JobOption("Input movies STAR file:", "LABEL_MOVIES_CPIPE", 1, "", "STAR files (*.star)", "");

    if (not is_tomo):
        joboptions["first_frame_sum"] = rno.JobOption("First frame for corrected sum:", 1, 1, 32, 1, "");
    if (not is_tomo):
        joboptions["last_frame_sum"] = rno.JobOption("Last frame for corrected sum:", -1, 0, 32, 1, "");
    joboptions["eer_grouping"] = rno.JobOption("EER fractionation:", 32, 1, 100, 1, "");
    joboptions["do_float16"] = rno.JobOption("Write output in float16?", True ,"");
    if (is_tomo):
        joboptions["do_even_odd_split"] = rno.JobOption("Save images for denoising?", False ,"");


    # Motioncor2
    default_location = "RELION_MOTIONCOR2_EXECUTABLE"
    default_motioncor2 = DEFAULTMOTIONCOR2LOCATION;
    if (default_location == NULL):
        default_location = default_motioncor2;


    # Common arguments RELION and UCSF implementation
    joboptions["bfactor"] = rno.JobOption("Bfactor:", 150, 0, 1500, 50, "");
    joboptions["patch_x"] = rno.JobOption("Number of patches X:", ("1"), "");
    joboptions["patch_y"] = rno.JobOption("Number of patches Y:", ("1"), "");
    joboptions["group_frames"] = rno.JobOption("Group frames:", 1, 1, 5, 1, "");
    joboptions["bin_factor"] = rno.JobOption("Binning factor:", 1, 1, 2, 1, "");
    joboptions["fn_gain_ref"] = rno.JobOption("Gain-reference image:", "", "*.{mrc,gain}", ".", "");
    joboptions["gain_rot"] = rno.JobOption("Gain rotation:", job_gain_rotation_options, 0, "");
    joboptions["gain_flip"] = rno.JobOption("Gain flip:", job_gain_flip_options, 0, "");

    # UCSF-wrapper
    joboptions["do_own_motioncor"] = rno.JobOption("Use RELION's own implementation?", True ,"");
    joboptions["fn_motioncor2_exe"] = rno.JobOption("MOTIONCOR2 executable:", (default_location), "*.*", ".", "");
    joboptions["fn_defect"] = rno.JobOption("Defect file:", "", "*", ".", "");
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", ("0"), "");
    joboptions["other_motioncor2_args"] = rno.JobOption("Other MOTIONCOR2 arguments", (""), "");

    # Dose-weight
    if (not is_tomo):
        joboptions["do_dose_weighting"] = rno.JobOption("Do dose-weighting?", True ,"");
    if (not is_tomo):
        joboptions["do_save_noDW"] = rno.JobOption("Save non-dose weighted as well?", False, "");
    if (not is_tomo) :
        joboptions["dose_per_frame"] = rno.JobOption("Dose per frame (e/A2):", 1, 0, 5, 0.2, "");
    if (not is_tomo) :
        joboptions["pre_exposure"] = rno.JobOption("Pre-exposure (e/A2):", 0, 0, 5, 0.5, "");

    joboptions["do_save_ps"] = rno.JobOption("Save sum of power spectra?", True, "");
    if (not is_tomo) :
        joboptions["group_for_ps"] = rno.JobOption("Sum power spectra every e/A2:", 4, 0, 10, 0.5, "");
    else:
        joboptions["group_for_ps"] = rno.JobOption("Sum power spectra every n frames:", 4, 0, 10, 0.5, "");




def initialiseCtffindJob():
    hidden_name = ".gui_ctffind";

    default_location = ""

    if (is_tomo):
        joboptions["input_star_mics"] = rno.JobOption("Input tilt series: ", LABEL_TOMOGRAMS_CPIPE, 1, "", "Tilt series STAR file (*.star)", "");

    else:
        joboptions["input_star_mics"] = rno.JobOption("Input micrographs STAR file:", "LABEL_MICS_CPIPE", 1, "", "STAR files (*.star)", "");


    if (not is_tomo) :
        joboptions["use_noDW"] = rno.JobOption("Use micrograph without dose-weighting?", False, "");

    joboptions["do_phaseshift"] = rno.JobOption("Estimate phase shifts?", False, "");
    joboptions["phase_min"] = rno.JobOption("Phase shift (deg) - Min:", 0, "");
    joboptions["phase_max"] = rno.JobOption("Phase shift (deg) - Max:", 180, "");
    joboptions["phase_step"] = rno.JobOption("Phase shift (deg) - Step:", 10, "");

    joboptions["dast"] = rno.JobOption("Amount of astigmatism (A):", 100, 0, 2000, 100,"");

    # CTFFIND options

    # Check for environment variable RELION_CTFFIND_EXECUTABLE
    joboptions["use_given_ps"] = rno.JobOption("Use power spectra from MotionCorr job?", True, "");
    default_location = "RELION_CTFFIND_EXECUTABLE"
    default_ctffind = "DEFAULTCTFFINDLOCATION";
    if (default_location == None):
        default_location = default_ctffind;

    joboptions["fn_ctffind_exe"] = rno.JobOption("CTFFIND-4.1 executable:", (default_location), "*", ".", "");
    joboptions["slow_search"] = rno.JobOption("Use exhaustive search?", False, "");

    joboptions["box"] = rno.JobOption("FFT box size (pix):", 512, 64, 1024, 8, "");
    joboptions["resmin"] = rno.JobOption("Minimum resolution (A):", 30, 10, 200, 10, "");
    joboptions["resmax"] = rno.JobOption("Maximum resolution (A):", 5, 1, 20, 1, "");
    joboptions["dfmin"] = rno.JobOption("Minimum defocus value (A):", 5000, 0, 25000, 1000, "");
    joboptions["dfmax"] = rno.JobOption("Maximum defocus value (A):", 50000, 20000, 100000, 1000, "");
    joboptions["dfstep"] = rno.JobOption("Defocus step size (A):", 500, 200, 2000, 100,"");

    if (is_tomo):
        joboptions["localsearch_nominal_defocus"] = rno.JobOption("Nominal defocus search range (A) ", 10000, 0, 20000, 1000, "");
        joboptions["exp_factor_dose"] = rno.JobOption("Dose-dependent Thon ring fading (e/A^2) ", 100, 0, 200, 10, "");


    joboptions["ctf_win"] = rno.JobOption("Estimate CTF on window size (pix) ", -1, -16, 4096, 16, "");




def initialiseManualpickJob():
    hidden_name = ".gui_manualpick";

    joboptions["fn_in"] = rno.JobOption("Input micrographs:", "LABEL_MICS_CPIPE", 1, "", "Input micrographs (*.{star,mrc})", "");

    joboptions["diameter"] = rno.JobOption("Particle diameter (A):", 100, 0, 500, 50, "" );
    joboptions["micscale"] = rno.JobOption("Scale for micrographs:", 0.2, 0.1, 1, 0.05, "" );
    joboptions["sigma_contrast"] = rno.JobOption("Sigma contrast:", 3, 0, 10, 0.5, "");
    joboptions["white_val"] = rno.JobOption("White value:", 0, 0, 512, 16, "");
    joboptions["black_val"] = rno.JobOption("Black value:", 0, 0, 512, 16, "");

    joboptions["lowpass"] = rno.JobOption("Lowpass filter (A)", 20, 10, 100, 5, "");
    joboptions["highpass"] = rno.JobOption("Highpass filter (A)", -1, 100, 1000, 100, "");
    joboptions["angpix"] = rno.JobOption("Pixel size (A)", -1, 0.3, 5, 0.1, "");
    joboptions["do_topaz_denoise"] = rno.JobOption("OR: use Topaz denoising?", False, "");

    joboptions["do_startend"] = rno.JobOption("Pick start-end coordinates helices?", False, "");

    joboptions["do_fom_threshold"] = rno.JobOption("Use autopick FOM threshold?", False, "");
    joboptions["minimum_pick_fom"] = rno.JobOption("Minimum autopick FOM: ", 0, -5, 10, 0.1, "");

    joboptions["do_color"] = rno.JobOption("Blue<>red color particles?", False, "");
    joboptions["color_label"] = rno.JobOption("MetaDataLabel for color:", ("rlnAutopickFigureOfMerit"), "");
    joboptions["fn_color"] = rno.JobOption("STAR file with color label: ", "", "STAR file (*.star)", ".", "");
    joboptions["blue_value"] = rno.JobOption("Blue value: ", 0., 0., 4., 0.1, "");
    joboptions["red_value"] = rno.JobOption("Red value: ", 2., 0., 4., 0.1, "");




def initialiseAutopickJob():
    hidden_name = ".gui_autopick";

    joboptions["fn_input_autopick"] = rno.JobOption("Input micrographs for autopick:", "LABEL_MICS_CPIPE", 1, "", "Input micrographs (*.{star})", "");
    joboptions["angpix"] = rno.JobOption("Pixel size in micrographs (A)", -1, 0.3, 5, 0.1, "");
    joboptions["continue_manual"] = rno.JobOption("OR: continue manually?", False, "");

    joboptions["do_log"] = rno.JobOption("OR: use Laplacian-of-Gaussian?", False, "");
    joboptions["log_diam_min"] = rno.JobOption("Min. diameter for LoG filter (A)", 200, 50, 500, 10, "");
    joboptions["log_diam_max"] = rno.JobOption("Max. diameter for LoG filter (A)", 250, 50, 500, 10, "");
    joboptions["log_invert"] = rno.JobOption("Are the particles white?", False, "");
    joboptions["log_maxres"] = rno.JobOption("Maximum resolution to consider (A)", 20, 10, 100, 5, "");
    joboptions["log_adjust_thr"] = rno.JobOption("Adjust default threshold (stddev):", 0, -1., 1., 0.05, "");
    joboptions["log_upper_thr"] = rno.JobOption("Upper threshold (stddev):", 999., 0., 10., 0.5, "");

    joboptions["do_topaz"] = rno.JobOption("OR: use Topaz?", False, "");
    joboptions["do_topaz_train"] = rno.JobOption("Perform topaz training?", False, "");
    joboptions["topaz_train_picks"] = rno.JobOption("Input picked coordinates for training:", "LABEL_COORDS_CPIPE", 1, "", "Input micrographs (*.{star})", "");
    joboptions["do_topaz_train_parts"] = rno.JobOption("OR train on a set of particles? ", False, "");
    joboptions["topaz_train_parts"] = rno.JobOption("Particles STAR file for training: ", "LABEL_PARTS_CPIPE", 1, "", "Input STAR file (*.{star})", "");
    joboptions["do_topaz_pick"] = rno.JobOption("Perform topaz picking?", False, "");
    joboptions["topaz_particle_diameter"] = rno.JobOption("Particle diameter (A) ", -1, 0, 2000, 20, "");
    joboptions["topaz_nr_particles"] = rno.JobOption("Nr of particles per micrograph: ", -1, 0, 2000, 20, "");
    joboptions["topaz_model"] = rno.JobOption("Trained topaz model: ", "", "SAV Files (*.sav)", ".", "");
    joboptions["fn_topaz_exe"]= rno.JobOption("Topaz executable:", ("relion_python_topaz"), "");
    joboptions["do_topaz_filaments"] = rno.JobOption("Pick filaments?", False, "");
    joboptions["topaz_filament_threshold"] = rno.JobOption("Threshold:", ("-5"),  "");
    joboptions["topaz_hough_length"] = rno.JobOption("Hough length (A):", ("-1"), "");
    joboptions["topaz_other_args"]= rno.JobOption("Additional topaz arguments:", (""), "");

    joboptions["do_refs"] = rno.JobOption("Use reference-based template-matching?", False, "");
    joboptions["fn_refs_autopick"] = rno.JobOption("2D references:", LABEL_2DIMGS_CPIPE, 1, "", "Input references (*.{star,mrcs})", "");
    joboptions["do_ref3d"]= rno.JobOption("OR: provide a 3D reference?", False, "");
    joboptions["fn_ref3d_autopick"] = rno.JobOption("3D reference:", "LABEL_MAP_CPIPE", 1, "", "Input reference (*.{mrc})", "");
    joboptions["ref3d_symmetry"] = rno.JobOption("Symmetry:", ("C1"), "");
    joboptions["ref3d_sampling"] = rno.JobOption("3D angular sampling:", job_sampling_options, 0, "");

    joboptions["lowpass"] = rno.JobOption("Lowpass filter references (A)", 20, 10, 100, 5, "");
    joboptions["highpass"] = rno.JobOption("Highpass filter (A)", -1, 100, 1000, 100, "");
    joboptions["angpix_ref"] = rno.JobOption("Pixel size in references (A)", -1, 0.3, 5, 0.1, "");
    joboptions["psi_sampling_autopick"] = rno.JobOption("In-plane angular sampling (deg)", 5, 1, 30, 1, "");

    joboptions["do_invert_refs"] = rno.JobOption("References have inverted contrast?", True, "");
    joboptions["do_ctf_autopick"] = rno.JobOption("Are References CTF corrected?", True, "");
    joboptions["do_ignore_first_ctfpeak_autopick"] = rno.JobOption("Ignore CTFs until first peak?", False,"");

    joboptions["threshold_autopick"] = rno.JobOption("Picking threshold:", 0.05, 0, 1., 0.01, "");
    joboptions["mindist_autopick"] = rno.JobOption("Minimum inter-particle distance (A):", 100, 0, 1000, 20, "");
    joboptions["maxstddevnoise_autopick"] = rno.JobOption("Maximum stddev noise:", 1.1, 0.9, 1.5, 0.02, "");
    joboptions["minavgnoise_autopick"] = rno.JobOption("Minimum avg noise:", -999., -2, 0.5, 0.05, "");
    joboptions["do_write_fom_maps"] = rno.JobOption("Write FOM maps?", False, "");
    joboptions["do_read_fom_maps"] = rno.JobOption("Read FOM maps?", False, "");

    joboptions["shrink"] = rno.JobOption("Shrink factor:", 0, 0, 1, 0.1, "");
    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, "");
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), "");

    joboptions["do_pick_helical_segments"] = rno.JobOption("Pick 2D helical segments?", False, "");
    joboptions["do_amyloid"] = rno.JobOption("Pick amyloid segments?", False, "");

    joboptions["helical_tube_outer_diameter"] = rno.JobOption("Tube diameter (A): ", 200, 100, 1000, 10, "");
    joboptions["helical_nr_asu"] = rno.JobOption("Number of unique asymmetrical units:", 1, 1, 100, 1, "");
    joboptions["helical_rise"] = rno.JobOption("Helical rise (A):", -1, 0, 100, 0.01, "");
    joboptions["helical_tube_kappa_max"] = rno.JobOption("Maximum curvature (kappa): ", 0.1, 0.05, 0.5, 0.01, "");
    joboptions["helical_tube_length_min"] = rno.JobOption("Minimum length (A): ", -1, 100, 1000, 10, "");




def initialiseExtractJob():
    hidden_name = ".gui_extract";

    joboptions["star_mics"]= rno.JobOption("micrograph STAR file: ", "LABEL_MICS_CPIPE", 1, "", "Input STAR file (*.{star})", "");
    # TO DOL set helical option for this
    joboptions["coords_suffix"] = rno.JobOption("Input coordinates: ", "LABEL_COORDS_CPIPE", 1, "", "Input coordinates list file (*.star)", "");
    joboptions["do_reextract"] = rno.JobOption("OR re-extract refined particles? ", False, "");
    joboptions["fndata_reextract"] = rno.JobOption("Refined particles STAR file: ", "LABEL_PARTS_CPIPE", 1, "", "Input STAR file (*.{star})", "");
    joboptions["do_reset_offsets"] = rno.JobOption("Reset the refined offsets to zero? ", False, "");
    joboptions["do_recenter"] = rno.JobOption("OR: re-center refined coordinates? ", False, "");
    joboptions["recenter_x"] = rno.JobOption("Re-center on X-coordinate (in pix): ", ("0"), "");
    joboptions["recenter_y"] = rno.JobOption("Re-center on Y-coordinate (in pix): ", ("0"), "");
    joboptions["recenter_z"] = rno.JobOption("Re-center on Z-coordinate (in pix): ", ("0"), "");
    joboptions["extract_size"] = rno.JobOption("Particle box size (pix):", 128, 64, 512, 8, "");
    joboptions["do_invert"] = rno.JobOption("Invert contrast?", True, "");
    joboptions["do_float16"] = rno.JobOption("Write output in float16?", True ,"");

    joboptions["do_norm"] = rno.JobOption("Normalize particles?", True, "");
    joboptions["bg_diameter"] = rno.JobOption("Diameter background circle (pix): ", -1, -1, 600, 10, "");
    joboptions["white_dust"] = rno.JobOption("Stddev for white dust removal: ", -1, -1, 10, 0.1, "");
    joboptions["black_dust"] = rno.JobOption("Stddev for black dust removal: ", -1, -1, 10, 0.1, "");
    joboptions["do_rescale"] = rno.JobOption("Rescale particles?", False, "");
    joboptions["rescale"] = rno.JobOption("Re-scaled size (pixels): ", 128, 64, 512, 8, "");
    joboptions["do_fom_threshold"] = rno.JobOption("Use autopick FOM threshold?", False, "");
    joboptions["minimum_pick_fom"] = rno.JobOption("Minimum autopick FOM: ", 0, -5, 10, 0.1, "");

    joboptions["do_extract_helix"] = rno.JobOption("Extract helical segments?", False, "");
    joboptions["helical_tube_outer_diameter"] = rno.JobOption("Tube diameter (A): ", 200, 100, 1000, 10, "");
    joboptions["helical_bimodal_angular_priors"] = rno.JobOption("Use bimodal angular priors?", True, "");
    joboptions["do_extract_helical_tubes"] = rno.JobOption("Coordinates are start-end only?", True, "");
    joboptions["do_cut_into_segments"] = rno.JobOption("Cut helical tubes into segments?", True, "");
    joboptions["helical_nr_asu"] = rno.JobOption("Number of unique asymmetrical units:", 1, 1, 100, 1, "");
    joboptions["helical_rise"] = rno.JobOption("Helical rise (A):", 1, 0, 100, 0.01, "");





def initialiseSelectJob():
    hidden_name = ".gui_select";

    joboptions["fn_model"] = rno.JobOption("Select classes from job:", LABEL_OPTIMISER_CPIPE, 1, "", "STAR files (*_optimiser.star)", "");
    joboptions["fn_mic"] = rno.JobOption("OR select from micrographs.star:", "LABEL_MICS_CPIPE", 1, "", "STAR files (*.star)", "");
    joboptions["fn_data"] = rno.JobOption("OR select from particles.star:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star)", "");

    joboptions["do_class_ranker"] = rno.JobOption("Automatically select 2D classes?", False, "");
    joboptions["rank_threshold"] = rno.JobOption("Minimum threshold for auto-selection: ", 0.5, 0, 1, 0.05, "");
    joboptions["select_nr_parts"] = rno.JobOption("Select at least this many particles: ", -1, -1, 10000, 500, "");
    joboptions["select_nr_classes"] = rno.JobOption("OR: select at least this many classes: ", -1, -1, 24, 1, "");

    joboptions["do_recenter"] = rno.JobOption("Re-center the class averages?", False, "");
    joboptions["do_regroup"] = rno.JobOption("Regroup the particles?", False, "");
    joboptions["nr_groups"] = rno.JobOption("Approximate nr of groups: ", 1, 50, 20, 1, "");

    joboptions["do_select_values"] = rno.JobOption("Select based on metadata values?", False, "");
    joboptions["select_label"] = rno.JobOption("Metadata label for subset selection:", "rlnCtfMaxResolution", "");
    joboptions["select_minval"] = rno.JobOption("Minimum metadata value:",  "-9999.", "");
    joboptions["select_maxval"] = rno.JobOption("Maximum metadata value:",  "9999.", "");

    joboptions["do_discard"] = rno.JobOption("OR: select on image statistics?", False, "");
    joboptions["discard_label"] = rno.JobOption("Metadata label for images:", "rlnImageName", "");
    joboptions["discard_sigma"] = rno.JobOption("Sigma-value for discarding images:", 4, 1, 10, 0.1, "");

    joboptions["do_split"] = rno.JobOption("OR: split into subsets?", False, "");
    joboptions["do_random"] = rno.JobOption("Randomise order before making subsets?:", False, "");
    joboptions["split_size"] = rno.JobOption("Subset size: ", 100, 100, 10000, 100, "");
    joboptions["nr_split"] = rno.JobOption("OR: number of subsets: ", -1, 1, 50, 1, "");

    joboptions["do_remove_duplicates"] = rno.JobOption("OR: remove duplicates?", False, "");
    joboptions["duplicate_threshold"] = rno.JobOption("Minimum inter-particle distance (A)", 30, 0, 1000, 1, "");
    joboptions["image_angpix"] = rno.JobOption("Pixel size before extraction (A)", -1, -1, 10, 0.01, "");

    joboptions["do_filaments"] = rno.JobOption("OR: select filaments by dendrogram?", False, "");
    joboptions["dendrogram_threshold"] = rno.JobOption("Dendrogram threshold: ", 0.85, 0, 1, 0.05, "");
    joboptions["dendrogram_minclass"] = rno.JobOption("Minimum class size: ", -1000, -1000, 50000, 1000, "");



def initialiseClass2DJob():
    hidden_name = ".gui_class2d";

    joboptions["fn_img"] = rno.JobOption("Input images STAR file:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star) \t Image stacks (not recommended, read help!) (*.{spi,mrcs})", "");
    joboptions["fn_cont"] = rno.JobOption("Continue from here: ", (""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR",  "");

    joboptions["do_ctf_correction"] = rno.JobOption("Do CTF-correction?", True, "");
    joboptions["ctf_intact_first_peak"] = rno.JobOption("Ignore CTFs until first peak?", False, "");

    joboptions["nr_classes"] = rno.JobOption("Number of classes:", 1, 1, 50, 1, "");
    joboptions["tau_fudge"] = rno.JobOption("Regularisation parameter T:", 2 , 0.1, 10, 0.1, "");


    joboptions["do_em"] = rno.JobOption("Use EM algorithm?", False, "");
    joboptions["nr_iter_em"] = rno.JobOption("Number of EM iterations:", 25, 1, 50, 1, "");


    joboptions["do_grad"] = rno.JobOption("Use VDAM algorithm?", True, "");
    joboptions["nr_iter_grad"] = rno.JobOption("Number of VDAM mini-batches:", 200, 50, 500, 10, "");

    joboptions["particle_diameter"] = rno.JobOption("Mask diameter (A):", 200, 0, 1000, 10, "");
    joboptions["do_zero_mask"] = rno.JobOption("Mask individual particles with zeros?", True, "");
    joboptions["highres_limit"] = rno.JobOption("Limit resolution E-step to (A): ", -1, -1, 20, 1, "");
    joboptions["do_center"] = rno.JobOption("Center class averages?", True, "");

    joboptions["dont_skip_align"] = rno.JobOption("Perform image alignment?", True, "");
    joboptions["psi_sampling"] = rno.JobOption("In-plane angular sampling:", 6., 0.5, 20, 0.5, "");
    joboptions["offset_range"] = rno.JobOption("Offset search range (pix):", 5, 0, 30, 1, "");
    joboptions["offset_step"] = rno.JobOption("Offset search step (pix):", 1, 0.1, 5, 0.1, "");
    joboptions["allow_coarser"] = rno.JobOption("Allow coarser sampling?", False, "");

    joboptions["do_helix"] = rno.JobOption("Classify 2D helical segments?", False, "");
    joboptions["helical_tube_outer_diameter"] = rno.JobOption("Tube diameter (A): ", 200, 100, 1000, 10, "");
    joboptions["do_bimodal_psi"] = rno.JobOption("Do bimodal angular searches?", True, "");
    joboptions["range_psi"] = rno.JobOption("Angular search range - psi (deg):", 6, 3, 30, 1, "");
    joboptions["do_restrict_xoff"] = rno.JobOption("Restrict helical offsets to rise:", True, "");
    joboptions["helical_rise"] = rno.JobOption("Helical rise (A):", 4.75, -1, 100, 1, "");


    joboptions["nr_pool"] = rno.JobOption("Number of pooled particles:", 3, 1, 16, 1, "");
    joboptions["do_parallel_discio"] = rno.JobOption("Use parallel disc I/O?", True, "");
    joboptions["do_preread_images"] = rno.JobOption("Pre-read all particles into RAM?", False, "");
    default_scratch = RELION_SCRATCH_DIR
    if (default_scratch == NULL):
        default_scratch = DEFAULTSCRATCHDIR;

    joboptions["scratch_dir"] = rno.JobOption("Copy particles to scratch directory:", (default_scratch), "");
    joboptions["do_combine_thru_disc"] = rno.JobOption("Combine iterations through disc?", False, "");

    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, "");
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), "");




# Constructor for initial model job
def initialiseInimodelJob():
    hidden_name = ".gui_inimodel";

    if (is_tomo):
        addTomoInputOptions(True, True, True, False);
    else:
        joboptions["fn_img"] = rno.JobOption("Input images STAR file:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star) \t Image stacks (not recommended, read help!) (*.{spi,mrcs})", "");

    joboptions["fn_cont"] = rno.JobOption("Continue from here: ", (""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR", "");

    joboptions["nr_iter"] = rno.JobOption("Number of VDAM mini-batches:", 200, 50, 500, 10, "");
    joboptions["tau_fudge"] = rno.JobOption("Regularisation parameter T:", 4 , 0.1, 10, 0.1, "");

    joboptions["nr_classes"] = rno.JobOption("Number of classes:", 1, 1, 50, 1, "");
    joboptions["sym_name"] = rno.JobOption("Symmetry:", ("C1"), "");
    joboptions["do_run_C1"] = rno.JobOption("Run in C1 and apply symmetry later? ", True, "");
    joboptions["particle_diameter"] = rno.JobOption("Mask diameter (A):", 200, 0, 1000, 10, "");
    joboptions["do_solvent"] = rno.JobOption("Flatten and enforce non-negative solvent?", True, "");

    if (is_tomo):
        joboptions["sigma_tilt"] = rno.JobOption("Prior width on tilt angle (deg):", -1, -1, 30, 1, "");

    joboptions["do_ctf_correction"] = rno.JobOption("Do CTF-correction?", True, "");
    joboptions["ctf_intact_first_peak"] = rno.JobOption("Ignore CTFs until first peak?", False, "");

    joboptions["do_parallel_discio"] = rno.JobOption("Use parallel disc I/O?", True, "");
    joboptions["nr_pool"] = rno.JobOption("Number of pooled particles:", 3, 1, 16, 1, "");
    joboptions["do_preread_images"] = rno.JobOption("Pre-read all particles into RAM?", False, "");
    default_scratch = RELION_SCRATCH_DIR
    if (default_scratch == NULL):
        default_scratch = DEFAULTSCRATCHDIR;

    joboptions["scratch_dir"] = rno.JobOption("Copy particles to scratch directory:", (default_scratch), "");
    joboptions["do_combine_thru_disc"] = rno.JobOption("Combine iterations through disc?", False, "");

    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, "");
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), "");




def initialiseClass3DJob():
    hidden_name = ".gui_class3d";

    if (is_tomo):
        addTomoInputOptions(True, True, True, False);

    else:
        joboptions["fn_img"] = rno.JobOption("Input images STAR file:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star)", "");


    joboptions["fn_cont"] = rno.JobOption("Continue from here: ", (""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR", "");
    joboptions["fn_ref"] = rno.JobOption("Reference map:", "LABEL_MAP_CPIPE", 1, "", "Image Files (*.{spi,vol,mrc})", "");
    joboptions["fn_mask"] = rno.JobOption("Reference mask (optional):", "LABEL_MASK_CPIPE", 1, "", "Image Files (*.{spi,vol,msk,mrc})", "");

    joboptions["ref_correct_greyscale"] = rno.JobOption("Ref. map is on absolute greyscale?", False, "");
    joboptions["trust_ref_size"] = rno.JobOption("Resize reference if needed?", True, "");
    joboptions["ini_high"] = rno.JobOption("Initial low-pass filter (A):", 60, 0, 200, 5, "");
    joboptions["sym_name"] = rno.JobOption("Symmetry:", ("C1"), "");

    joboptions["do_ctf_correction"] = rno.JobOption("Do CTF-correction?", True, "");
    joboptions["ctf_intact_first_peak"] = rno.JobOption("Ignore CTFs until first peak?", False, "");

    joboptions["nr_classes"] = rno.JobOption("Number of classes:", 1, 1, 50, 1, "");
    default_T =  1 if (is_tomo) else 4;
    joboptions["tau_fudge"] = rno.JobOption("Regularisation parameter T:", default_T , 0.1, 10, 0.1, "");
    joboptions["nr_iter"] = rno.JobOption("Number of iterations:", 25, 1, 50, 1, "");
    joboptions["do_fast_subsets"] = rno.JobOption("Use fast subsets (for large data sets)?", False, "");

    joboptions["particle_diameter"] = rno.JobOption("Mask diameter (A):", 200, 0, 1000, 10, "");
    joboptions["do_zero_mask"] = rno.JobOption("Mask individual particles with zeros?", True, "");
    joboptions["highres_limit"] = rno.JobOption("Limit resolution E-step to (A): ", -1, -1, 20, 1, "");
    joboptions["do_blush"] = rno.JobOption("Use Blush regularisation?", False, "");

    joboptions["dont_skip_align"] = rno.JobOption("Perform image alignment?", True, "");
    joboptions["sampling"] = rno.JobOption("Angular sampling interval:", job_sampling_options, 2, "");
    joboptions["offset_range"] = rno.JobOption("Offset search range (pix):", 5, 0, 30, 1, "");
    joboptions["offset_step"] = rno.JobOption("Offset search step (pix):", 1, 0.1, 5, 0.1, "");
    joboptions["do_local_ang_searches"] = rno.JobOption("Perform local angular searches?", False, "");
    joboptions["sigma_angles"] = rno.JobOption("Local angular search range:", 5., 0, 15, 0.1, "");
    joboptions["allow_coarser"] = rno.JobOption("Allow coarser sampling?", False, "");
    joboptions["relax_sym"] = rno.JobOption("Relax symmetry:", (""), "");

    if (is_tomo):
        joboptions["sigma_tilt"] = rno.JobOption("Prior width on tilt angle (deg):", -1, -1, 30, 1, "");


    joboptions["do_helix"] = rno.JobOption("Do helical reconstruction?", False, "");
    joboptions["helical_tube_inner_diameter"] = rno.JobOption("Tube diameter - inner (A):", ("-1"),"");
    joboptions["helical_tube_outer_diameter"] = rno.JobOption("Tube diameter - outer (A):", ("-1"),"");
    joboptions["range_rot"] = rno.JobOption("Angular search range - rot (deg):", ("-1"), "");
    joboptions["range_tilt"] = rno.JobOption("Angular search range - tilt (deg):", ("15"), "");
    joboptions["range_psi"] = rno.JobOption("Angular search range - psi (deg):", ("10"), "");
    joboptions["do_apply_helical_symmetry"] = rno.JobOption("Apply helical symmetry?", True, "");
    joboptions["helical_nr_asu"] = rno.JobOption("Number of unique asymmetrical units:", 1, 1, 100, 1, "");
    joboptions["helical_twist_initial"] =  rno.JobOption("Initial helical twist (deg):", ("0"),"");
    joboptions["helical_rise_initial"] = rno.JobOption("Initial helical rise (A):", ("0"), "");
    joboptions["helical_z_percentage"] = rno.JobOption("Central Z length (%):", 30., 5., 80., 1., "");
    joboptions["do_local_search_helical_symmetry"] = rno.JobOption("Do local searches of symmetry?", False, "");
    joboptions["helical_twist_min"] = rno.JobOption("Helical twist search (deg) - Min:", ("0"), "");
    joboptions["helical_twist_max"] = rno.JobOption("Helical twist search (deg) - Max:", ("0"), "");
    joboptions["helical_twist_inistep"] = rno.JobOption("Helical twist search (deg) - Step:", ("0"), "");
    joboptions["helical_rise_min"] = rno.JobOption("Helical rise search (A) - Min:", ("0"), "");
    joboptions["helical_rise_max"] = rno.JobOption("Helical rise search (A) - Max:", ("0"), "");
    joboptions["helical_rise_inistep"] = rno.JobOption("Helical rise search (A) - Step:", ("0"), "");
    joboptions["helical_range_distance"] = rno.JobOption("Range factor of local averaging:", -1., 1., 5., 0.1, "");
    joboptions["keep_tilt_prior_fixed"] = rno.JobOption("Keep tilt-prior fixed:", True, "");

    joboptions["do_parallel_discio"] = rno.JobOption("Use parallel disc I/O?", True, "");
    joboptions["nr_pool"] = rno.JobOption("Number of pooled particles:", 3, 1, 16, 1, "");
    joboptions["do_pad1"] = rno.JobOption("Skip padding?", False, "");
    joboptions["do_preread_images"] = rno.JobOption("Pre-read all particles into RAM?", False, "");
    default_scratch = RELION_SCRATCH_DIR
    if (default_scratch == NULL):
        default_scratch = DEFAULTSCRATCHDIR;

    joboptions["scratch_dir"] = rno.JobOption("Copy particles to scratch directory:", (default_scratch), "");
    joboptions["do_combine_thru_disc"] = rno.JobOption("Combine iterations through disc?", False, "");

    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, "");
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), "");




def initialiseAutorefineJob():
    type = rh.PROC_3DAUTO;

    hidden_name = ".gui_auto3d";

    if (is_tomo):
        addTomoInputOptions(True, True, True, False);

    else:
        joboptions["fn_img"] = rno.JobOption("Input images STAR file:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star)", "");


    joboptions["fn_cont"] = rno.JobOption("Continue from here: ", (""), "STAR Files (*_it*_optimiser.star)", "CURRENT_ODIR", "");
    joboptions["fn_ref"] = rno.JobOption("Reference map:", "LABEL_MAP_CPIPE", 1, "", "Image Files (*.{spi,vol,mrc})", "");
    joboptions["fn_mask"] = rno.JobOption("Reference mask (optional):", "LABEL_MASK_CPIPE", 1, "", "Image Files (*.{spi,vol,msk,mrc})", "");

    joboptions["ref_correct_greyscale"] = rno.JobOption("Ref. map is on absolute greyscale?", False, "");
    joboptions["trust_ref_size"] = rno.JobOption("Resize reference if needed?", True, "");
    joboptions["ini_high"] = rno.JobOption("Initial low-pass filter (A):", 60, 0, 200, 5, "");
    joboptions["sym_name"] = rno.JobOption("Symmetry:", ("C1"), "");

    joboptions["do_ctf_correction"] = rno.JobOption("Do CTF-correction?", True, "");
    joboptions["ctf_intact_first_peak"] = rno.JobOption("Ignore CTFs until first peak?", False, "");

    joboptions["particle_diameter"] = rno.JobOption("Mask diameter (A):", 200, 0, 1000, 10, "");
    joboptions["do_zero_mask"] = rno.JobOption("Mask individual particles with zeros?", True, "");
    joboptions["do_solvent_fsc"] = rno.JobOption("Use solvent-flattened FSCs?", False, "");
    joboptions["do_blush"] = rno.JobOption("Use Blush regularisation?", False, "");

    joboptions["sampling"] = rno.JobOption("Initial angular sampling:", rh.job_sampling_options, 2, "");
    joboptions["offset_range"] = rno.JobOption("Initial offset range (pix):", 5, 0, 30, 1, "");
    joboptions["offset_step"] = rno.JobOption("Initial offset step (pix):", 1, 0.1, 5, 0.1, "");
    joboptions["auto_local_sampling"] = rno.JobOption("Local searches from auto-sampling:", rh.job_sampling_options, 4, "");
    joboptions["relax_sym"] = rno.JobOption("Relax symmetry:", (""), "");
    joboptions["auto_faster"] = rno.JobOption("Use finer angular sampling faster?", False, "");

    if (is_tomo):
        joboptions["sigma_tilt"] = rno.JobOption("Prior width on tilt angle (deg):", -1, -1, 30, 1, "");

    joboptions["do_helix"] = rno.JobOption("Do helical reconstruction?", False, "");
    joboptions["helical_tube_inner_diameter"] = rno.JobOption("Tube diameter - inner (A):", ("-1"),"");
    joboptions["helical_tube_outer_diameter"] = rno.JobOption("Tube diameter - outer (A):", ("-1"),"");
    joboptions["range_rot"] = rno.JobOption("Angular search range - rot (deg):", ("-1"), "");
    joboptions["range_tilt"] = rno.JobOption("Angular search range - tilt (deg):", ("15"), "");
    joboptions["range_psi"] = rno.JobOption("Angular search range - psi (deg):", ("10"), "");
    joboptions["do_apply_helical_symmetry"] = rno.JobOption("Apply helical symmetry?", True, "");
    joboptions["helical_nr_asu"] = rno.JobOption("Number of unique asymmetrical units:", 1, 1, 100, 1, "");
    joboptions["helical_twist_initial"] =  rno.JobOption("Initial helical twist (deg):", ("0"),"");
    joboptions["helical_rise_initial"] = rno.JobOption("Initial helical rise (A):", ("0"), "");
    joboptions["helical_z_percentage"] = rno.JobOption("Central Z length (%):", 30., 5., 80., 1., "");
    joboptions["do_local_search_helical_symmetry"] = rno.JobOption("Do local searches of symmetry?", False, "");
    joboptions["helical_twist_min"] = rno.JobOption("Helical twist search (deg) - Min:", ("0"), "");
    joboptions["helical_twist_max"] = rno.JobOption("Helical twist search (deg) - Max:", ("0"), "");
    joboptions["helical_twist_inistep"] = rno.JobOption("Helical twist search (deg) - Step:", ("0"), "");
    joboptions["helical_rise_min"] = rno.JobOption("Helical rise search (A) - Min:", ("0"), "");
    joboptions["helical_rise_max"] = rno.JobOption("Helical rise search (A) - Max:", ("0"), "");
    joboptions["helical_rise_inistep"] = rno.JobOption("Helical rise search (A) - Step:", ("0"), "");
    joboptions["helical_range_distance"] = rno.JobOption("Range factor of local averaging:", -1., 1., 5., 0.1, "");
    joboptions["keep_tilt_prior_fixed"] = rno.JobOption("Keep tilt-prior fixed:", True, "");

    joboptions["do_parallel_discio"] = rno.JobOption("Use parallel disc I/O?", True, "");
    joboptions["nr_pool"] = rno.JobOption("Number of pooled particles:", 3, 1, 16, 1, "");
    joboptions["do_pad1"] = rno.JobOption("Skip padding?", False, "");
    joboptions["do_preread_images"] = rno.JobOption("Pre-read all particles into RAM?", False, "");
    default_scratch = "RELION_SCRATCH_DIR"
    if (default_scratch == None):
        default_scratch = "DEFAULTSCRATCHDIR";

    joboptions["scratch_dir"] = rno.JobOption("Copy particles to scratch directory:", (default_scratch), "");
    joboptions["do_combine_thru_disc"] = rno.JobOption("Combine iterations through disc?", False, "");
    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, "");
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), "");




def initialiseMultiBodyJob():
    type =rh.PROC_MULTIBODY;

    hidden_name = ".gui_multibody";

    joboptions["fn_in"] = rno.JobOption("Consensus refinement optimiser.star: ", (""), "STAR Files (run_it*_optimiser.star)", "Refine3D/.", "");

    joboptions["fn_cont"] = rno.JobOption("Continue from here: ", (""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR", "");

    joboptions["fn_bodies"] = rno.JobOption("Body STAR file:", (""), "STAR Files (*.{star})", ".", "");

    joboptions["do_subtracted_bodies"] = rno.JobOption("Reconstruct subtracted bodies?", True, "");
    joboptions["do_blush"] = rno.JobOption("Use Blush regularisation?", False, "");

    joboptions["sampling"] = rno.JobOption("Initial angular sampling:", rh.job_sampling_options, 4, "");
    joboptions["offset_range"] = rno.JobOption("Initial offset range (pix):", 3, 0, 30, 1, "");
    joboptions["offset_step"] = rno.JobOption("Initial offset step (pix):", 0.75, 0.1, 5, 0.1, "");


    joboptions["do_analyse"] = rno.JobOption("Run flexibility analysis?", True, "");
    joboptions["nr_movies"] = rno.JobOption("Number of eigenvector movies:", 3, 0, 16, 1, "");
    joboptions["do_select"] = rno.JobOption("Select particles based on eigenvalues?", False, "");
    joboptions["select_eigenval"] = rno.JobOption("Select on eigenvalue:", 1, 1, 20, 1, "");
    joboptions["eigenval_min"] = rno.JobOption("Minimum eigenvalue:", -999., -50, 50, 1, "");
    joboptions["eigenval_max"] = rno.JobOption("Maximum eigenvalue:", 999., -50, 50, 1, "");

    joboptions["do_parallel_discio"] = rno.JobOption("Use parallel disc I/O?", True, "");
    joboptions["nr_pool"] = rno.JobOption("Number of pooled particles:", 3, 1, 16, 1, "");
    joboptions["do_pad1"] = rno.JobOption("Skip padding?", False, "");
    joboptions["do_preread_images"] = rno.JobOption("Pre-read all particles into RAM?", False, "");
    default_scratch = RELION_SCRATCH_DIR
    if (default_scratch == NULL):
        default_scratch = DEFAULTSCRATCHDIR;

    joboptions["scratch_dir"] = rno.JobOption("Copy particles to scratch directory:", (default_scratch), "");
    joboptions["do_combine_thru_disc"] = rno.JobOption("Combine iterations through disc?", False, "");
    joboptions["use_gpu"] = rno.JobOption("Use GPU acceleration?", False, "");
    joboptions["gpu_ids"] = rno.JobOption("Which GPUs to use:", (""), "");




def initialiseMaskcreateJob():
    hidden_name = ".gui_maskcreate";

    joboptions["fn_in"] = rno.JobOption("Input 3D map:", "LABEL_MAP_CPIPE", 1, "", "MRC map files (*.mrc)", "");

    joboptions["lowpass_filter"] = rno.JobOption("Lowpass filter map (A)", 15, 10, 100, 5, "");
    joboptions["angpix"] = rno.JobOption("Pixel size (A)", -1, 0.3, 5, 0.1, "");

    joboptions["inimask_threshold"] = rno.JobOption("Initial binarisation threshold:", 0.02, 0., 0.5, 0.01, "");
    joboptions["extend_inimask"] = rno.JobOption("Extend binary map this many pixels:", 3, 0, 20, 1, "" );
    joboptions["width_mask_edge"] = rno.JobOption("Add a soft-edge of this many pixels:", 3, 0, 20, 1, "" );

    joboptions["do_helix"] = rno.JobOption("Mask a 3D helix?", False, "");
    joboptions["helical_z_percentage"] = rno.JobOption("Central Z length (%):", 30., 5., 80., 1., "");




def initialiseJoinstarJob():
    hidden_name = ".gui_joinstar";

    joboptions["do_part"] = rno.JobOption("Combine particle STAR files?", False, "");
    joboptions["fn_part1"] = rno.JobOption("Particle STAR file 1: ", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", "");
    joboptions["fn_part2"] = rno.JobOption("Particle STAR file 2: ", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", "");
    joboptions["fn_part3"] = rno.JobOption("Particle STAR file 3: ", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", "");
    joboptions["fn_part4"] = rno.JobOption("Particle STAR file 4: ", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", "");

    joboptions["do_mic"] = rno.JobOption("Combine micrograph STAR files?", False, "");
    joboptions["fn_mic1"] = rno.JobOption("Micrograph STAR file 1: ", "LABEL_MICS_CPIPE", 1, "", "micrograph STAR file (*.star)", "");
    joboptions["fn_mic2"] = rno.JobOption("Micrograph STAR file 2: ", "LABEL_MICS_CPIPE", 1, "", "micrograph STAR file (*.star)", "");
    joboptions["fn_mic3"] = rno.JobOption("Micrograph STAR file 3: ", "LABEL_MICS_CPIPE", 1, "", "micrograph STAR file (*.star)", "");
    joboptions["fn_mic4"] = rno.JobOption("Micrograph STAR file 4: ", "LABEL_MICS_CPIPE", 1, "", "micrograph STAR file (*.star)", "");

    joboptions["do_mov"] = rno.JobOption("Combine movie STAR files?", False, "");
    joboptions["fn_mov1"] = rno.JobOption("Movie STAR file 1: ", "LABEL_MOVIES_CPIPE", 1, "", "movie STAR file (*.star)", "");
    joboptions["fn_mov2"] = rno.JobOption("Movie STAR file 2: ", "LABEL_MOVIES_CPIPE", 1, "", "movie STAR file (*.star)", "");
    joboptions["fn_mov3"] = rno.JobOption("Movie STAR file 3: ", "LABEL_MOVIES_CPIPE", 1, "", "movie STAR file (*.star)", "");
    joboptions["fn_mov4"] = rno.JobOption("Movie STAR file 4: ", "LABEL_MOVIES_CPIPE", 1, "", "movie STAR file (*.star)", "");




def initialiseSubtractJob():
    hidden_name = ".gui_subtract";

    joboptions["fn_opt"] = rno.JobOption("Input optimiser.star: ", LABEL_OPTIMISER_CPIPE, 1, "", "STAR Files (*_optimiser.star)", "");
    joboptions["fn_mask"] = rno.JobOption("Mask of the signal to keep:", "LABEL_MASK_CPIPE", 1, "", "Image Files (*.{spi,vol,msk,mrc})", "");
    joboptions["do_data"] = rno.JobOption("Use different particles?", False, "");
    joboptions["fn_data"] = rno.JobOption("Input particle star file:", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", "");
    joboptions["do_float16"] = rno.JobOption("Write output in float16?", True ,"");

    joboptions["do_fliplabel"] = rno.JobOption("OR revert to original particles?", False, "");
    joboptions["fn_fliplabel"] = rno.JobOption("revert this particle star file:", "LABEL_PARTS_CPIPE", 1, "", "particle STAR file (*.star)", "");

    joboptions["do_center_mask"] = rno.JobOption("Do center subtracted images on mask?", True, "");
    joboptions["do_center_xyz"] = rno.JobOption("Do center on my coordinates?", False, "");
    joboptions["center_x"] = rno.JobOption("Center coordinate (pix) - X:", ("0"), "");
    joboptions["center_y"] = rno.JobOption("Center coordinate (pix) - Y:", ("0"), "");
    joboptions["center_z"] = rno.JobOption("Center coordinate (pix) - Z:", ("0"), "");

    joboptions["new_box"] = rno.JobOption("New box size:", -1, 64, 512, 32, "" );




def initialisePostprocessJob():
    hidden_name = ".gui_post";

    joboptions["fn_in"] = rno.JobOption("One of the 2 unfiltered half-maps:", LABEL_HALFMAP_CPIPE, 1, "", "MRC map files (*half1*.mrc)",  "");
    joboptions["fn_mask"] = rno.JobOption("Solvent mask:", "LABEL_MASK_CPIPE", 1, "", "Image Files (*.{spi,vol,msk,mrc})", "");
    joboptions["angpix"] = rno.JobOption("Calibrated pixel size (A)", -1, 0.3, 5, 0.1, "");

    joboptions["do_auto_bfac"] = rno.JobOption("Estimate B-factor automatically?", True, "");
    joboptions["autob_lowres"] = rno.JobOption("Lowest resolution for auto-B fit (A):", 10, 8, 15, 0.5, "");
    joboptions["do_adhoc_bfac"] = rno.JobOption("Use your own B-factor?", False, "");
    joboptions["adhoc_bfac"] = rno.JobOption("User-provided B-factor:", -1000, -2000, 0, -50, "");

    joboptions["fn_mtf"] = rno.JobOption("MTF of the detector (STAR file)", "", "STAR Files (*.star)", ".", "");
    joboptions["mtf_angpix"] = rno.JobOption("Original detector pixel size:", 1.0, 0.3, 2.0, 0.1, "");

    joboptions["do_skip_fsc_weighting"] = rno.JobOption("Skip FSC-weighting?", False, "");
    joboptions["low_pass"] = rno.JobOption("Ad-hoc low-pass filter (A):",5,1,40,1,"");




def initialiseLocalresJob():
    hidden_name = ".gui_localres";

    joboptions["fn_in"] = rno.JobOption("One of the 2 unfiltered half-maps:", LABEL_HALFMAP_CPIPE, 1, "", "MRC map files (*half1*.mrc)",  "");
    joboptions["angpix"] = rno.JobOption("Calibrated pixel size (A)", 1, 0.3, 5, 0.1, "");

    # Check for environment variable RELION_RESMAP_TEMPLATE
    default_location = RELION_RESMAP_EXECUTABLE
    default_resmap = DEFAULTRESMAPLOCATION
    if (default_location == NULL):
        default_location = default_resmap;


    joboptions["do_resmap_locres"] = rno.JobOption("Use ResMap?", True, "");
    joboptions["fn_resmap"] = rno.JobOption("ResMap executable:", (default_location), "ResMap*", ".", "");
    joboptions["fn_mask"] = rno.JobOption("User-provided solvent mask:", "LABEL_MASK_CPIPE", 1, "", "Image Files (*.{spi,vol,msk,mrc})", "");
    joboptions["pval"] = rno.JobOption("P-value:", 0.05, 0., 1., 0.01, "");
    joboptions["minres"] = rno.JobOption("Highest resolution (A): ", 0., 0., 10., 0.1, "");
    joboptions["maxres"] = rno.JobOption("Lowest resolution (A): ", 0., 0., 10., 0.1, "");
    joboptions["stepres"] = rno.JobOption("Resolution step size (A)", 1., 0.1, 3, 0.1, "" );

    joboptions["do_relion_locres"] = rno.JobOption("Use Relion?", False, "");

    #joboptions["""locres_sampling"""] = rno.JobOption("""Sampling rate (A):""", 25, 5, 50, 5, """The local-resolution map will be calculated every so many Angstroms, by placing soft spherical masks on a cubic grid with this spacing. Very fine samplings (e.g. < 15A?) may take a long time to compute and give spurious estimates!""");
    #joboptions["""randomize_at"""] = rno.JobOption("""Frequency for phase-randomisation (A): """, 10., 5, 20., 1, """From this frequency onwards, the phases for the mask-corrected FSC-calculation will be randomized. Make sure this is a lower resolution (i.e. a higher number) than the local resolutions you are after in your map.""");
    joboptions["adhoc_bfac"] = rno.JobOption("User-provided B-factor:", -100, -500, 0, -25, "");
    joboptions["fn_mtf"] = rno.JobOption("MTF of the detector (STAR file)", "", "STAR Files (*.star)", ".", "");





def initialiseDynaMightJob():
    hidden_name = ".gui_dynamight";

    joboptions["fn_star"] = rno.JobOption("Input images STAR file:", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star) \t Image stacks (not recommended, read help!) (*.{spi,mrcs})", "");
    joboptions["fn_map"] = rno.JobOption("Consensus map:", "LABEL_MAP_CPIPE", 1, "", "Image Files (*.{spi,vol,mrc})", "");
    #joboptions["""fn_mask"""] = rno.JobOption("""Mask (optional):""", "LABEL_MASK_CPIPE", """""", """Image Files (*.{spi,vol,msk,mrc})""", """Provide a mask to limit deformations to a specific region of the consensus structure. Regions outside the mask will be kept fized and will not be visualised.""");
    joboptions["gpu_id"] = rno.JobOption("Which (single) GPU to use:", ("0"), "");
    joboptions["do_preload"] = rno.JobOption("Preload images in RAM?", False, "");
    joboptions["fn_dynamight_exe"] = rno.JobOption("DynaMight executable:", ("relion_python_dynamight"), "");

    joboptions["nr_gaussians"] = rno.JobOption("Number of Gaussians: ", 10000, 5000, 40000, 1000, "");
    joboptions["initial_threshold"] = rno.JobOption("Initial map threshold (optional): ",("") , "");
    joboptions["reg_factor"] = rno.JobOption("Regularization factor: ", 1, 0.2, 5, 0.1, "");

    joboptions["fn_checkpoint"] = rno.JobOption("Checkpoint file:", (""), "Checkpoint files (*.pth)", "CURRENT_ODIR/forward_deformations/checkpoints", "");

    joboptions["do_visualize"] = rno.JobOption("Do visualization?", False, "");
    joboptions["halfset"] = rno.JobOption("Half-set to visualize: ", 1, 0, 2, 1, "");

    joboptions["do_inverse"] = rno.JobOption("Do inverse-deformation estimation?", False, "");
    joboptions["nr_epochs"] = rno.JobOption("Number of epochs to perform: ", 200, 50, 500, 10, "");
    joboptions["do_store_deform"] = rno.JobOption("Store deformations in RAM?", False, "");

    joboptions["do_reconstruct"] = rno.JobOption("Do deformed backprojection?", False, "");
    joboptions["backproject_batchsize"] = rno.JobOption("Backprojection batchsize: ", 10, 1, 500, 10, "");





def initialiseModelAngeloJob():
    hidden_name = ".gui_modelangelo";

    joboptions["fn_map"] = rno.JobOption("B-factor sharpened map:", "LABEL_MAP_CPIPE", 1, "", "MRC map files (*.mrc)",  "");
    joboptions["p_seq"] = rno.JobOption("FASTA sequence for proteins:", LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})",  "");
    joboptions["d_seq"] = rno.JobOption("FASTA sequence for DNA:", LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})",  "");
    joboptions["r_seq"] = rno.JobOption("FASTA sequence for RNA:", LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})",  "");
    joboptions["fn_modelangelo_exe"] = rno.JobOption("ModelAngelo executable:", ("relion_python_modelangelo"), "");
    joboptions["gpu_id"] = rno.JobOption("Which GPUs to use:", ("0"), "");

    joboptions["do_hhmer"] = rno.JobOption("Perform HMMer search?", False ,"");
    joboptions["fn_lib"] = rno.JobOption("Library with sequences for HMMer search:", LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})", "");
    joboptions["alphabet"] = rno.JobOption("Alphabet for the HMMer search:", job_modelangelo_alphabet_options, 0, "");
    joboptions["F1"] = rno.JobOption("HMMSearch F1: ", 0.02, 1., 10., 0.1, "");
    joboptions["F2"] = rno.JobOption("HMMSearch F2: ", 0.001, 1., 10., 0.1, "");
    joboptions["F3"] = rno.JobOption("HMMSearch F3: ", 0.00001, 0., 10., 0.1, "");
    joboptions["E"] = rno.JobOption("HMMSearch E: ", 10, 0., 100., 10, "");



def initialiseMotionrefineJob():
    hidden_name = ".gui_bayespolish";

    # I/O
    joboptions["fn_mic"] = rno.JobOption("Micrographs (from MotionCorr):", "LABEL_MICS_CPIPE", 1, "", "STAR files (*.star)", "");
    joboptions["fn_data"] = rno.JobOption("Particles (from Refine3D or CtfRefine):", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star)", "");
    joboptions["fn_post"] = rno.JobOption("Postprocess STAR file:", "LABEL_POSTPROCESS_CPIPE", 1, "", "STAR files (postprocess.star)", "");
    joboptions["do_float16"] = rno.JobOption("Write output in float16?", True ,"");

    # Frame range
    joboptions["first_frame"] = rno.JobOption("First movie frame: ", 1., 1., 10., 1, "");
    joboptions["last_frame"] = rno.JobOption("Last movie frame: ", -1., 5., 50., 1, "");

    joboptions["extract_size"] = rno.JobOption("Extraction size (pix in unbinned movie):", -1, 64, 1024, 8, "");
    joboptions["rescale"] = rno.JobOption("Re-scaled size (pixels): ", -1, 64, 1024, 8, "");

    # Parameter optimisation
    joboptions["do_param_optim"] = rno.JobOption("Train optimal parameters?", False, "");
    joboptions["eval_frac"] = rno.JobOption("Fraction of Fourier pixels for testing: ", 0.5, 0, 1., 0.01, "");
    joboptions["optim_min_part"] = rno.JobOption("Use this many particles: ", 10000, 5000, 50000, 1000, "");

    # motion_fit
    joboptions["do_polish"] = rno.JobOption("Perform particle polishing?", True, "");
    joboptions["opt_params"] = rno.JobOption("Optimised parameter file:", "LABEL_POLISH_PARAMS", 1, "", "TXT files (*.txt)", "");
    joboptions["do_own_params"] = rno.JobOption("OR use your own parameters?", False, "");
    joboptions["sigma_vel"] = rno.JobOption("Sigma for velocity (A/dose): ", 0.2, 1., 10., 0.1, "");
    joboptions["sigma_div"] = rno.JobOption("Sigma for divergence (A): ", 5000, 0, 10000, 10000, "");
    joboptions["sigma_acc"] = rno.JobOption("Sigma for acceleration (A/dose): ", 2, -1, 7, 0.1, "");

    #combine_frames
    joboptions["minres"] = rno.JobOption("Minimum resolution for B-factor fit (A): ", 20, 8, 40, 1, "");
    joboptions["maxres"] = rno.JobOption("Maximum resolution for B-factor fit (A): ", -1, -1, 15, 1, "");


def initialiseCtfrefineJob():
    hidden_name = ".gui_ctfrefine";

    # I/O
    joboptions["fn_data"] = rno.JobOption("Particles (from Refine3D):", "LABEL_PARTS_CPIPE", 1, "", "STAR files (*.star)", "");
    joboptions["fn_post"] = rno.JobOption("Postprocess STAR file:", "LABEL_POSTPROCESS_CPIPE", 1, "", "STAR files (postprocess.star)", "");

    joboptions["minres"] = rno.JobOption("Minimum resolution for fits (A): ", 30, 8, 40, 1, "");

    # Defocus fit
    joboptions["do_ctf"] = rno.JobOption("Perform CTF parameter fitting?", True, "");
    joboptions["do_defocus"] = rno.JobOption("Fit defocus?", job_ctffit_options, 0, "");
    joboptions["do_astig"] = rno.JobOption("Fit astigmatism?", job_ctffit_options, 0, "");
    joboptions["do_bfactor"] = rno.JobOption("Fit B-factor?", job_ctffit_options, 0, "");
    joboptions["do_phase"] = rno.JobOption("Fit phase-shift?", job_ctffit_options, 0, "");

    # aberrations
    joboptions["do_aniso_mag"] = rno.JobOption("Estimate (anisotropic) magnification?", False, "");

    joboptions["do_tilt"] = rno.JobOption("Estimate beamtilt?", False, "");
    joboptions["do_trefoil"] = rno.JobOption("Also estimate trefoil?", False, "");

    joboptions["do_4thorder"] = rno.JobOption("Estimate 4th order aberrations?", False, "");


def initialiseExternalJob():
    hidden_name = ".gui_external";

    # I/O
    joboptions["fn_exe"] = rno.JobOption("External executable:", "", "", ".", "");

    # Optional input nodes
    joboptions["in_mov"] = rno.JobOption("Input movies: ", "LABEL_MOVIES_CPIPE", 1, "", "movie STAR file (*.star)", "");
    joboptions["in_mic"] = rno.JobOption("Input micrographs: ", "LABEL_MICS_CPIPE", 1, "", "micrographs STAR file (*.star)", "");
    joboptions["in_part"] = rno.JobOption("Input particles: ", "LABEL_PARTS_CPIPE", 1, "", "particles STAR file (*.star)", "");
    joboptions["in_coords"] = rno.JobOption("Input coordinates: ", "LABEL_COORDS_CPIPE", 1, "", "STAR files (coords_suffix*.star)", "");
    joboptions["in_3dref"] = rno.JobOption("Input 3D reference: ", "LABEL_MAP_CPIPE", 1, "", "MRC files (*.mrc)", "");
    joboptions["in_mask"] = rno.JobOption("Input 3D mask: ", "LABEL_MASK_CPIPE", 1, "", "MRC files (*.mrc)", "");

    # Optional parameters
    joboptions["param1_label"] = rno.JobOption("Param1 - label:", (""), "");
    joboptions["param1_value"] = rno.JobOption("Param1 - value:" , (""), "");
    joboptions["param2_label"] = rno.JobOption("Param2 - label:", (""), "");
    joboptions["param2_value"] = rno.JobOption("Param2 - value:" , (""), "");
    joboptions["param3_label"] = rno.JobOption("Param3 - label:", (""), "");
    joboptions["param3_value"] = rno.JobOption("Param3 - value:" , (""), "");
    joboptions["param4_label"] = rno.JobOption("Param4 - label:", (""), "");
    joboptions["param4_value"] = rno.JobOption("Param4 - value:" , (""), "");
    joboptions["param5_label"] = rno.JobOption("Param5 - label:", (""), "");
    joboptions["param5_value"] = rno.JobOption("Param5 - value:" , (""), "");
    joboptions["param6_label"] = rno.JobOption("Param6 - label:", (""), "");
    joboptions["param6_value"] = rno.JobOption("Param6 - value:" , (""), "");
    joboptions["param7_label"] = rno.JobOption("Param7 - label:", (""), "");
    joboptions["param7_value"] = rno.JobOption("Param7 - value:" , (""), "");
    joboptions["param8_label"] = rno.JobOption("Param8 - label:", (""), "");
    joboptions["param8_value"] = rno.JobOption("Param8 - value:" , (""), "");
    joboptions["param9_label"] = rno.JobOption("Param9 - label:", (""), "");
    joboptions["param9_value"] = rno.JobOption("Param9 - value:" , (""), "");
    joboptions["param10_label"] = rno.JobOption("Param10 - label:", (""), "");
    joboptions["param10_value"] = rno.JobOption("Param10 - value:" , (""), "");


# Initialise
def initialise(_job_type):
    type = _job_type

    has_mpi = False 
    has_thread =  False
    if (type == rh.PROC_IMPORT):
        has_mpi = has_thread = False
        initialiseImportJob()
#        dirname = rh.proc_type2dirname(rh.PROC_IMPORT)
#        getCommandsImportJobRaw(f'{dirname}/job{counter}/')
#        getCommandsImportJobOther(f'{dirname}/job{counter}/')

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

def header():
    general = f"""
data_
#
_id       refine3d
_label    'Refine3D'
_widget    radio
_parent   refine
_help     ''
_comment  'use_gctf'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
#
"""

def tabs():
    return """
loop_
_groups.id
_groups.label
_groups.icon
_groups.widget
_groups.default
_groups.parent
_groups.help
io       'I/O'                    bi-arrow-down-up       tab ? ? ?
settings 'Settings'               bi-tools               tab ? ? ?
display  'Display'                bi-palette             tab ? ? ?
compute  'Compute'                bi-cpu                 tab ? ? ?
running  'Running'                bi-send                tab ? ? ?
result   'DataViz'                bi-eye                 tab ? ? ?
indata   'Input'                  bi-arrow-bar-down      fieldset ?      io       ?
cont     'Continue Job'           bi-send-plus           fieldset hidden io       ?
outdata  'Output and System'      bi-terminal            fieldset ?      io       ?
general  'General'                bi-chat-right-text     fieldset ?      settings ?
other    'Other Parameters'       bi-chat-right-dots     fieldset ?      settings ?
disk     'Disk Access'            bi-database            fieldset ?      compute  ?    
gpu      'Use GPU Acceleration?'  bi-gpu-card            switch   false  compute  'If set to Yes, the job will try to use GPU acceleration.'
process  'Processes'              bi-gear-fill           fieldset ?      compute  ?
do_queue 'Submit to queue?'       bi-box-arrow-in-right  switch   false  running  'If set to Yes, the job will be submitted to a queue, otherwise the job will be executed locally. Note that only MPI jobs may be sent to a queue. The default can be set through the environment variable RELION_QUEUE_USE.'
command  'Check Command'          bi-terminal-plus       cli      ?      running  'RELION Command as it appears in `note.txt`'
exec     'Execute Command'        bi-send-plus           toolbar  ?      running  'No help'
"""

def additional_args():
    return """
#
loop_
_other.id
_other.label
_other.widget
_other.default
_other.arg0
_other.arg1
_other.arg2
_other.help
other_args 'Additional Arguments' string '' ? ? ? 'Additional arguments that need to be passed'
#
"""

def disk_access():
    return """
loop_
_disk.id
_disk.label
_disk.widget
_disk.default
_disk.arg0
_disk.arg1
_disk.arg2
_disk.help
do_parallel_discio 'Use parallel disc I/O?' bool true ? ? ?
; If set to Yes, all MPI followers will read images from disc. Otherwise, only the leader will read images and send them through the network to the followers. 
Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.
;
nr_pool 'Number of pooled particles:' range 3 1 16 1 
;Particles are processed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.
;
do_preread_images 'Pre-read all particles into RAM?' bool false ? ? ?
;If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. 
Because particles are read in float-precision, it will take ( N * box_size * box_size * 4 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. 
For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. 
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM. 

If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.
;
scratch_dir 'Copy particles to scratch directory:' file default_scratch ? ? ?
;If a directory is provided here, then the job will create a sub-directory in it called relion_volatile. If that relion_volatile directory already exists, it will be wiped. Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory. 
Provided this directory is on a fast local drive (e.g. an SSD drive), processing in all the iterations will be faster. If the job finishes correctly, the relion_volatile directory will be wiped. If the job crashes, you may want to remove it yourself.
;
do_combine_thru_disc 'Combine iterations through disc?' bool false ? ? ? 
;If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results. The MPI leader will read in all these files, combine them all, and write out a new file with the combined results. 
All MPI salves will then read in the combined results. This reduces heavy load on the network, but increases load on the disc I/O. 
This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step. It will depend on your system setup which is most efficient.
;
#
"""

def compute_gpu():
    return """
loop_
_use_gpu.id
_use_gpu.label
_use_gpu.widget
_use_gpu.default
_use_gpu.arg0
_use_gpu.arg1
_use_gpu.arg2
_use_gpu.help
gpu_ids 'Which GPUs to use:' string '' ? ? ?
;This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','. For example: '0,0:1,1:0,0:1,1'
;
#
"""

def compute_queue():
    return """
loop_
_do_queue.id
_do_queue.label
_do_queue.widget
_do_queue.default
_do_queue.arg0
_do_queue.arg1
_do_queue.arg2
_do_queue.help
load_queue '' import './spa/00_home/qsub.star' ? ? ? ?
#
"""

def compute_mpi():
    return """
loop_
_process.id
_process.label
_process.widget
_process.default
_process.arg0
_process.arg1
_process.arg2
_process.help
nr_mpi "Number of MPI procs:" range '{QSUB_NRMPI_VAL}' 1 '{RELION_MPI_MAX}' 1 "Number of MPI nodes to use in parallel. When set to 1, MPI will not be used. The maximum can be set through the environment variable RELION_MPI_MAX."
nr_threads "Number of threads:" range '{QSUB_NRTHREADS_VAL}' 1 "{RELION_THREAD_MAX}" 1 "Number of shared-memory (POSIX) threads to use in parallel. When set to 1, no multi-threading will be used. The maximum can be set through the environment variable RELION_THREAD_MAX."
#
"""

def cont_process():
    return """
loop_
_cont.id
_cont.label
_cont.widget
_cont.default
_cont.arg0     # filetype
_cont.arg1     # placeholder
_cont.arg2     # directory
_cont.help
fn_cont "Continue from here: " file  ? ? "STAR Files (*_optimiser.star)" CURRENT_ODIR 
;Select the `*_optimiser.star` file for the iteration \
from which you want to continue a previous run. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a `_ctX` to the output rootname, \
with X being the iteration from which one continues the previous run.
;
#
"""

def run_buttons():
    return """
loop_
_exec.id
_exec.label
_exec.widget
_exec.default  # visibility
_exec.arg0     # ?
_exec.arg1     # icon
_exec.arg2     # parent
_exec.help
do_schedule 'Schedule' button true  ? bi-calendar-plus ? 'No help'
do_run      'Run!'     button true  ? bi-send          ? 'No help'
do_continue 'Continue' button false ? bi-send-plus  ? 'No help'
#
"""

########################## M A I N ##########################
#
joboptions = {}
is_tomo = False
tables = {'indata': init_table('_indata'), 'odata': init_table('_odata'), 'general': init_table('_general')}
if __name__ == "__main__":
    header()
    # initialise(rh.PROC_CTFFIND)
    initialise(rh.PROC_3DAUTO)
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
