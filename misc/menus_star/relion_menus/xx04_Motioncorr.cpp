void RelionJob::initialiseMotioncorrJob()
{
	hidden_name = ".gui_motioncorr";

	if (is_tomo)
	{
		joboptions["input_star_mics"] = JobOption("Input tilt series: ", LABEL_TOMOGRAMS_CPIPE, 1, "", "Tilt series STAR file (*.star)", "Input global tilt series star file");
	}
	else
	{
		joboptions["input_star_mics"] = JobOption("Input movies STAR file:", LABEL_MOVIES_CPIPE, 1, "", "STAR files (*.star)", "A STAR file with all micrographs to run MOTIONCORR on");
	}
	if (!is_tomo) joboptions["first_frame_sum"] = JobOption("First frame for corrected sum:", 1, 1, 32, 1, "First frame to use in corrected average (starts counting at 1). ");
	if (!is_tomo) joboptions["last_frame_sum"] = JobOption("Last frame for corrected sum:", -1, 0, 32, 1, "Last frame to use in corrected average. Values equal to or smaller than 0 mean 'use all frames'.");
	joboptions["eer_grouping"] = JobOption("EER fractionation:", 32, 1, 100, 1, "The number of hardware frames to group into one fraction. This option is relevant only for Falcon4 movies in the EER format. Note that all 'frames' in the GUI (e.g. first and last frame for corrected sum, dose per frame) refer to fractions, not raw detector frames. See https://www3.mrc-lmb.cam.ac.uk/relion/index.php/Image_compression#Falcon4_EER for detailed guidance on EER processing.");
	joboptions["do_float16"] = JobOption("Write output in float16?", true ,"If set to Yes, RelionCor2 will write output images in float16 MRC format. This will save a factor of two in disk space compared to the default of writing in float32. Note that RELION and CCPEM will read float16 images, but other programs may not (yet) do so. For example, Gctf will not work with float16 images. Also note that this option does not work with UCSF MotionCor2. For CTF estimation, use CTFFIND-4.1 with pre-calculated power spectra (activate the 'Save sum of power spectra' option).");
	if (is_tomo)
	{
	joboptions["do_even_odd_split"] = JobOption("Save images for denoising?", false ,"If set to Yes, MotionCor2 will write output images summed from both the even frames of the input movie and the odd frames of the input movie. This generates two versions of the same movie which essential if you wish to carry out denoising later. If you are unsure whether you will need denoising later, it is best to select Yes, but be aware this option increases the processing time for MotionCor. At the moment, this is only available in Shawn Zheng's MotionCor2 (>=v1.3.0)  and therefore do_float_16 must equal false too.");
	}

	// Motioncor2
	char *default_location = getenv ("RELION_MOTIONCOR2_EXECUTABLE");
	char default_motioncor2[] = DEFAULTMOTIONCOR2LOCATION;
	if (default_location == NULL)
	{
		default_location = default_motioncor2;
	}

	// Common arguments RELION and UCSF implementation
	joboptions["bfactor"] = JobOption("Bfactor:", 150, 0, 1500, 50, "The B-factor that will be applied to the micrographs.");
	joboptions["patch_x"] = JobOption("Number of patches X:", std::string("1"), "Number of patches (in X and Y direction) to apply motioncor2.");
	joboptions["patch_y"] = JobOption("Number of patches Y:", std::string("1"), "Number of patches (in X and Y direction) to apply motioncor2.");
	joboptions["group_frames"] = JobOption("Group frames:", 1, 1, 5, 1, "Average together this many frames before calculating the beam-induced shifts.");
	joboptions["bin_factor"] = JobOption("Binning factor:", 1, 1, 2, 1, "Bin the micrographs this much by a windowing operation in the Fourier Tranform. Binning at this level is hard to un-do later on, but may be useful to down-scale super-resolution images. Float-values may be used. Do make sure though that the resulting micrograph size is even.");
	joboptions["fn_gain_ref"] = JobOption("Gain-reference image:", "", "*.{mrc,gain}", ".", "Location of the gain-reference file to be applied to the input micrographs. Leave this empty if the movies are already gain-corrected.");
	joboptions["gain_rot"] = JobOption("Gain rotation:", job_gain_rotation_options, 0, "Rotate the gain reference by this number times 90 degrees clockwise in relion_display. This is the same as -RotGain in MotionCor2. Note that MotionCor2 uses a different convention for rotation so it says 'counter-clockwise'. Valid values are 0, 1, 2 and 3.");
	joboptions["gain_flip"] = JobOption("Gain flip:", job_gain_flip_options, 0, "Flip the gain reference after rotation. This is the same as -FlipGain in MotionCor2. 0 means do nothing, 1 means flip Y (upside down) and 2 means flip X (left to right).");

	// UCSF-wrapper
	joboptions["do_own_motioncor"] = JobOption("Use RELION's own implementation?", true ,"If set to Yes, use RELION's own implementation of a MotionCor2-like algorithm by Takanori Nakane. Otherwise, wrap to the UCSF implementation. Note that Takanori's program only runs on CPUs but uses multiple threads, while the UCSF-implementation needs a GPU but uses only one CPU thread. Takanori's implementation is most efficient when the number of frames is divisible by the number of threads (e.g. 12 or 18 threads per MPI process for 36 frames). On some machines, setting the OMP_PROC_BIND environmental variable to TRUE accelerates the program.\n\
When running on 4k x 4k movies and using 6 to 12 threads, the speeds should be similar. Note that Takanori's program uses the same model as the UCSF program and gives results that are almost identical.\n\
Whichever program you use, 'Motion Refinement' is highly recommended to get the most of your dataset.");
	joboptions["fn_motioncor2_exe"] = JobOption("MOTIONCOR2 executable:", std::string(default_location), "*.*", ".", "Location of the MOTIONCOR2 executable. You can control the default of this field by setting environment variable RELION_MOTIONCOR2_EXECUTABLE, or by editing the first few lines in src/gui_jobwindow.h and recompile the code.");
	joboptions["fn_defect"] = JobOption("Defect file:", "", "*", ".", "Location of a UCSF MotionCor2-style defect text file or a defect map that describe the defect pixels on the detector. Each line of a defect text file should contain four numbers specifying x, y, width and height of a defect region. A defect map is an image (MRC or TIFF), where 0 means good and 1 means bad pixels. The coordinate system is the same as the input movie before application of binning, rotation and/or flipping.\nNote that the format of the defect text is DIFFERENT from the defect text produced by SerialEM! One can convert a SerialEM-style defect file into a defect map using IMOD utilities e.g. \"clip defect -D defect.txt -f tif movie.mrc defect_map.tif\". See explanations in the SerialEM manual.\n\nLeave empty if you don't have any defects, or don't want to correct for defects on your detector.");
	joboptions["gpu_ids"] = JobOption("Which GPUs to use:", std::string("0"), "Provide a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':'. For example, to place one rank on device 0 and one rank on device 1, provide '0:1'.\n\
Note that multiple MotionCor2 processes should not share a GPU; otherwise, it can lead to crash or broken outputs (e.g. black images) .");
    joboptions["other_motioncor2_args"] = JobOption("Other MOTIONCOR2 arguments", std::string(""), "Additional arguments that need to be passed to MOTIONCOR2.");

	// Dose-weight
	if (!is_tomo) joboptions["do_dose_weighting"] = JobOption("Do dose-weighting?", true ,"If set to Yes, the averaged micrographs will be dose-weighted.");
	if (!is_tomo) joboptions["do_save_noDW"] = JobOption("Save non-dose weighted as well?", false, "Aligned but non-dose weighted images are sometimes useful in CTF estimation, although there is no difference in most cases. Whichever the choice, CTF refinement job is always done on dose-weighted particles.");
	if (!is_tomo) joboptions["dose_per_frame"] = JobOption("Dose per frame (e/A2):", 1, 0, 5, 0.2, "Dose per movie frame (in electrons per squared Angstrom).");
	if (!is_tomo) joboptions["pre_exposure"] = JobOption("Pre-exposure (e/A2):", 0, 0, 5, 0.5, "Pre-exposure dose (in electrons per squared Angstrom).");

	joboptions["do_save_ps"] = JobOption("Save sum of power spectra?", true, "Sum of non-dose weighted power spectra provides better signal for CTF estimation. The power spectra can be used by CTFFIND4 but not by GCTF. This option is not available for UCSF MotionCor2. You must use this option when writing in float16.");
	if (!is_tomo) joboptions["group_for_ps"] = JobOption("Sum power spectra every e/A2:", 4, 0, 10, 0.5, "McMullan et al (Ultramicroscopy, 2015) suggest summing power spectra every 4.0 e/A2 gives optimal Thon rings");
	else {
		joboptions["group_for_ps"] = JobOption("Sum power spectra every n frames:", 4, 0, 10, 0.5, "McMullan et al (Ultramicroscopy, 2015) suggest summing power spectra every 4.0 e/A2 gives optimal Thon rings");
	}
}

bool RelionJob::getCommandsMotioncorrJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);

	std::string command;
	if (joboptions["nr_mpi"].getNumber(error_message) > 1)
		command="`which relion_run_motioncorr_mpi`";
	else
		command="`which relion_run_motioncorr`";
	if (error_message != "") return false;

	// I/O
	if (joboptions["input_star_mics"].getString() == "")
	{
		error_message = "ERROR: empty field for input STAR file...";
		return false;
	}
	command += " --i " + joboptions["input_star_mics"].getString();
	Node node(joboptions["input_star_mics"].getString(), joboptions["input_star_mics"].node_type);
	inputNodes.push_back(node);

	command += " --o " + outputname;
	outputName = outputname;
	if (is_tomo)
	{
		Node node2(outputname + "corrected_tilt_series.star", LABEL_MOCORR_TOMOGRAMS);
		outputNodes.push_back(node2);
	}
	else
	{
		Node node2(outputname + "corrected_micrographs.star", LABEL_MOCORR_MICS);
		outputNodes.push_back(node2);
	}
	Node node4(outputname + "logfile.pdf", LABEL_MOCORR_LOG);
	outputNodes.push_back(node4);

	if (!is_tomo) command += " --first_frame_sum " + joboptions["first_frame_sum"].getString();
	if (!is_tomo) command += " --last_frame_sum " + joboptions["last_frame_sum"].getString();

	if (is_tomo && joboptions["do_even_odd_split"].getBoolean())
	{
		command += " --even_odd_split ";
	}
	
	if (joboptions["do_own_motioncor"].getBoolean())
	{
		label += ".own";

		command += " --use_own ";
		command += " --j " + joboptions["nr_threads"].getString();
		if (joboptions["do_float16"].getBoolean())
		{
			if (!joboptions["do_save_ps"].getBoolean())
			{
				error_message = "When writing to float16, you have to write power spectra for CTFFIND-4.1.";
				return false;
			}

			command +=" --float16";
		}
	}
	else
	{
		label += ".motioncor2";

		command += " --use_motioncor2 ";
		command += " --motioncor2_exe " + joboptions["fn_motioncor2_exe"].getString();

		if (joboptions["do_float16"].getBoolean())
		{
			error_message = "ERROR: MotionCor2 cannot write float16 files.";
			return false;
		}

		if ((joboptions["other_motioncor2_args"].getString()).length() > 0)
			command += " --other_motioncor2_args \" " + joboptions["other_motioncor2_args"].getString() + " \"";

		// Which GPUs to use?
		command += " --gpu \"" + joboptions["gpu_ids"].getString() + "\"";
	}

	if ((joboptions["fn_defect"].getString()).length() > 0)
		command += " --defect_file " + joboptions["fn_defect"].getString();

	command += " --bin_factor " + joboptions["bin_factor"].getString();
	command += " --bfactor " + joboptions["bfactor"].getString();
	if (!is_tomo) command += " --dose_per_frame " + joboptions["dose_per_frame"].getString();
	if (!is_tomo) command += " --preexposure " + joboptions["pre_exposure"].getString();
	command += " --patch_x " + joboptions["patch_x"].getString();
	command += " --patch_y " + joboptions["patch_y"].getString();
	command += " --eer_grouping " + joboptions["eer_grouping"].getString();

	if (joboptions["group_frames"].getNumber(error_message) > 1.)
		command += " --group_frames " + joboptions["group_frames"].getString();
	if (error_message != "") return false;

	if ((joboptions["fn_gain_ref"].getString()).length() > 0)
	{

		int gain_rot = -1, gain_flip = -1;
		for (int i = 0; i <= 3; i++)
		{
			if (strcmp((joboptions["gain_rot"].getString()).c_str(), job_gain_rotation_options[i].c_str()) == 0)
			{
				gain_rot = i;
				break;
			}
		}

		for (int i = 0; i <= 2; i++)
		{
			if (strcmp((joboptions["gain_flip"].getString()).c_str(), job_gain_flip_options[i].c_str()) == 0)
			{
				gain_flip = i;
				break;
			}
		}

		if (gain_rot == -1 || gain_flip == -1)
			REPORT_ERROR("Illegal gain_rot and/or gain_flip.");

		command += " --gainref " + joboptions["fn_gain_ref"].getString();
		command += " --gain_rot " + integerToString(gain_rot);
		command += " --gain_flip " + integerToString(gain_flip);
	}

	if (!is_tomo && joboptions["do_dose_weighting"].getBoolean())
	{
		command += " --dose_weighting ";
		if (joboptions["do_save_noDW"].getBoolean())
		{
			command += " --save_noDW ";
		}
	}

	if (joboptions["do_save_ps"].getBoolean())
	{
		if (!joboptions["do_own_motioncor"].getBoolean())
		{
			error_message = "'Save sum of power spectra' is not available with UCSF MotionCor2.";
			return false;
		}

		float dose_for_ps = joboptions["group_for_ps"].getNumber(error_message);
		if (error_message != "") return false;

		float dose_rate = 1.0;
		if (!is_tomo)
		{
		dose_rate = joboptions["dose_per_frame"].getNumber(error_message);
		}
		if (error_message != "") return false;
		if (dose_rate <= 0)
		{
			error_message = "Please specify the dose rate to calculate the grouping for power spectra.";
			return false;
		}
		if (dose_for_ps <= 0)
		{
			error_message = "Invalid dose for the grouping for power spectra.";
			return false;
		}

		int grouping_for_ps = ROUND(dose_for_ps / dose_rate);
		if (grouping_for_ps == 0)
			grouping_for_ps = 1;

		command += " --grouping_for_ps " + integerToString(grouping_for_ps) + " ";
	}

	if (is_continue)
		command += " --only_do_unfinished ";

	// Other arguments
	command += " " + joboptions["other_args"].getString();

	commands.push_back(command);

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

