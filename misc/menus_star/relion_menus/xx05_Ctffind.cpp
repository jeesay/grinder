void RelionJob::initialiseCtffindJob()
{
	hidden_name = ".gui_ctffind";

	char *default_location;

	if (is_tomo)
	{
		joboptions["input_star_mics"] = JobOption("Input tilt series: ", LABEL_TOMOGRAMS_CPIPE, 1, "", "Tilt series STAR file (*.star)", "Input global tilt series star file.");
	}
	else
	{
		joboptions["input_star_mics"] = JobOption("Input micrographs STAR file:", LABEL_MICS_CPIPE, 1, "", "STAR files (*.star)", "A STAR file with all micrographs to run CTFFIND or Gctf on");
	}

	if (!is_tomo) joboptions["use_noDW"] = JobOption("Use micrograph without dose-weighting?", false, "If set to Yes, the CTF estimation will be done using the micrograph without dose-weighting as in rlnMicrographNameNoDW (_noDW.mrc from MotionCor2). If set to No, the normal rlnMicrographName will be used.");

	joboptions["do_phaseshift"] = JobOption("Estimate phase shifts?", false, "If set to Yes, CTFFIND4 will estimate the phase shift, e.g. as introduced by a Volta phase-plate");
	joboptions["phase_min"] = JobOption("Phase shift (deg) - Min:", std::string("0"), "Minimum, maximum and step size (in degrees) for the search of the phase shift");
	joboptions["phase_max"] = JobOption("Phase shift (deg) - Max:", std::string("180"), "Minimum, maximum and step size (in degrees) for the search of the phase shift");
	joboptions["phase_step"] = JobOption("Phase shift (deg) - Step:", std::string("10"), "Minimum, maximum and step size (in degrees) for the search of the phase shift");

	joboptions["dast"] = JobOption("Amount of astigmatism (A):", 100, 0, 2000, 100,"CTFFIND's dAst parameter, GCTFs -astm parameter");

	// CTFFIND options

	// Check for environment variable RELION_CTFFIND_EXECUTABLE
	joboptions["use_given_ps"] = JobOption("Use power spectra from MotionCorr job?", true, "If set to Yes, the CTF estimation will be done using power spectra calculated during motion correction. You must use this option if you used float16 in motion correction.");
	default_location = getenv ("RELION_CTFFIND_EXECUTABLE");
	char default_ctffind[] = DEFAULTCTFFINDLOCATION;
	if (default_location == NULL)
	{
		default_location = default_ctffind;
	}
	joboptions["fn_ctffind_exe"] = JobOption("CTFFIND-4.1 executable:", std::string(default_location), "*", ".", "Location of the CTFFIND (release 4.1 or later) executable. You can control the default of this field by setting environment variable RELION_CTFFIND_EXECUTABLE, or by editing the first few lines in src/gui_jobwindow.h and recompile the code.");
	joboptions["slow_search"] = JobOption("Use exhaustive search?", false, "If set to Yes, CTFFIND4 will use slower but more exhaustive search. This option is recommended for CTFFIND version 4.1.8 and earlier, but probably not necessary for 4.1.10 and later. It is also worth trying this option when astigmatism and/or phase shifts are difficult to fit.");

	joboptions["box"] = JobOption("FFT box size (pix):", 512, 64, 1024, 8, "CTFFIND's Box parameter");
	joboptions["resmin"] = JobOption("Minimum resolution (A):", 30, 10, 200, 10, "CTFFIND's ResMin parameter");
	joboptions["resmax"] = JobOption("Maximum resolution (A):", 5, 1, 20, 1, "CTFFIND's ResMax parameter");
	joboptions["dfmin"] = JobOption("Minimum defocus value (A):", 5000, 0, 25000, 1000, "CTFFIND's dFMin parameter");
	joboptions["dfmax"] = JobOption("Maximum defocus value (A):", 50000, 20000, 100000, 1000, "CTFFIND's dFMax parameter");
	joboptions["dfstep"] = JobOption("Defocus step size (A):", 500, 200, 2000, 100,"CTFFIND's FStep parameter");

    if (is_tomo)
    {
        joboptions["localsearch_nominal_defocus"] = JobOption("Nominal defocus search range (A) ", 10000, 0, 20000, 1000, "If a positive value is given, the defocus search range will be set to +/- this value (in A) around the nominal defocus value from the input STAR file. If a zero or negative value are given, then the overall min-max defocus search ranges above will be used instead.");
        joboptions["exp_factor_dose"] = JobOption("Dose-dependent Thon ring fading (e/A^2) ", 100, 0, 200, 10, "If a positive value is given, then the maximum resolution for CTF estimation is lowerered by exp(dose/this_factor) times the original maximum resolution specified above. Remember that exp(1) ~=2.7, so a value of 100 e/A^2 for this factor will yield 2.7x higher maxres for an accumulated dose of 100 e/A^2; Smaller values will lead to faster decay of the maxres. If zero or a negative value is given, the maximum value specified above will be used for all images.");
    }

	joboptions["ctf_win"] = JobOption("Estimate CTF on window size (pix) ", -1, -16, 4096, 16, "If a positive value is given, a squared window of this size at the center of the micrograph will be used to estimate the CTF. This may be useful to exclude parts of the micrograph that are unsuitable for CTF estimation, e.g. the labels at the edge of phtographic film. \n \n The original micrograph will be used (i.e. this option will be ignored) if a negative value is given.");

}

bool RelionJob::getCommandsCtffindJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;

	outputName = outputname;
	if (is_tomo)
	{
		Node node(outputname + "tilt_series_ctf.star", LABEL_CTFFIND_TOMOGRAMS);
		outputNodes.push_back(node);
	}
	else
	{
		Node node(outputname + "micrographs_ctf.star", LABEL_CTFFIND_MICS);
		outputNodes.push_back(node);
	}

	// PDF with histograms of the eigenvalues
	Node node3(outputname + "logfile.pdf", LABEL_CTFFIND_LOG);
	outputNodes.push_back(node3);

	if (joboptions["nr_mpi"].getNumber(error_message) > 1)
		command="`which relion_run_ctffind_mpi`";
	else
		command="`which relion_run_ctffind`";
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
	command += " --Box " + joboptions["box"].getString();
	command += " --ResMin " + joboptions["resmin"].getString();
	command += " --ResMax " + joboptions["resmax"].getString();
	command += " --dFMin " + joboptions["dfmin"].getString();
	command += " --dFMax " + joboptions["dfmax"].getString();
	command += " --FStep " + joboptions["dfstep"].getString();
	command += " --dAst " + joboptions["dast"].getString();

    if (is_tomo)
    {
        // tomo-specific options
        command += " --localsearch_nominal_defocus " + joboptions["localsearch_nominal_defocus"].getString();
        command += " --exp_factor_dose " +  joboptions["exp_factor_dose"].getString();

        // Tomo-specific output file for display button
        Node node4(outputname + "power_spectra_fits.star", LABEL_CTFFIND_POWER_SPECTRA);
        outputNodes.push_back(node4);

    }
	else
	{
		if (joboptions["use_noDW"].getBoolean())
			command += " --use_noDW ";
	}
	if (joboptions["do_phaseshift"].getBoolean())
	{
		command += " --do_phaseshift ";
		command += " --phase_min " + joboptions["phase_min"].getString();
		command += " --phase_max " + joboptions["phase_max"].getString();
		command += " --phase_step " + joboptions["phase_step"].getString();
	}

    label += ".ctffind4";

    command += " --ctffind_exe " + joboptions["fn_ctffind_exe"].getString();
    command += " --ctfWin " + joboptions["ctf_win"].getString();
    command += " --is_ctffind4 ";
    if (!joboptions["slow_search"].getBoolean())
    {
        command += " --fast_search ";
    }
    if (joboptions["use_given_ps"].getBoolean())
    {
        command += " --use_given_ps ";
    }

	if (is_continue)
		command += " --only_do_unfinished ";

	// Other arguments
	command += " " + joboptions["other_args"].getString();
	commands.push_back(command);

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

