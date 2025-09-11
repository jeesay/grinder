void RelionJob::initialiseLocalresJob()
{
	hidden_name = ".gui_localres";

	joboptions["fn_in"] = JobOption("One of the 2 unfiltered half-maps:", LABEL_HALFMAP_CPIPE, 1, "", "MRC map files (*half1*.mrc)",  "Provide one of the two unfiltered half-reconstructions that were output upon convergence of a 3D auto-refine run.");
	joboptions["angpix"] = JobOption("Calibrated pixel size (A)", 1, 0.3, 5, 0.1, "Provide the final, calibrated pixel size in Angstroms. This value may be different from the pixel-size used thus far, e.g. when you have recalibrated the pixel size using the fit to a PDB model. The X-axis of the output FSC plot will use this calibrated value.");

	// Check for environment variable RELION_RESMAP_TEMPLATE
	char *default_location = getenv("RELION_RESMAP_EXECUTABLE");
	char default_resmap[] = DEFAULTRESMAPLOCATION;
	if (default_location == NULL)
	{
		default_location = default_resmap;
	}

	joboptions["do_resmap_locres"] = JobOption("Use ResMap?", true, "If set to Yes, then ResMap will be used for local resolution estimation.");
	joboptions["fn_resmap"] = JobOption("ResMap executable:", std::string(default_location), "ResMap*", ".", "Location of the ResMap executable. You can control the default of this field by setting environment variable RELION_RESMAP_EXECUTABLE, or by editing the first few lines in src/gui_jobwindow.h and recompile the code. \n \n Note that the ResMap wrapper cannot use MPI.");
	joboptions["fn_mask"] = JobOption("User-provided solvent mask:", LABEL_MASK_CPIPE, 1, "", "Image Files (*.{spi,vol,msk,mrc})", "Provide a mask with values between 0 and 1 around all domains of the complex. ResMap uses this mask for local resolution calculation. RELION does NOT use this mask for calculation, but makes a histogram of local resolution within this mask.");
	joboptions["pval"] = JobOption("P-value:", 0.05, 0., 1., 0.01, "This value is typically left at 0.05. If you change it, report the modified value in your paper!");
	joboptions["minres"] = JobOption("Highest resolution (A): ", 0., 0., 10., 0.1, "ResMaps minRes parameter. By default (0), the program will start at just above 2x the pixel size");
	joboptions["maxres"] = JobOption("Lowest resolution (A): ", 0., 0., 10., 0.1, "ResMaps maxRes parameter. By default (0), the program will stop at 4x the pixel size");
	joboptions["stepres"] = JobOption("Resolution step size (A)", 1., 0.1, 3, 0.1, "ResMaps stepSize parameter." );

	joboptions["do_relion_locres"] = JobOption("Use Relion?", false, "If set to Yes, then relion_postprocess will be used for local-rtesolution estimation. This program basically performs a series of post-processing operations with a small soft, spherical mask that is moved over the entire map, while using phase-randomisation to estimate the convolution effects of that mask. \
\n \n The output relion_locres.mrc map can be used to color the surface of a map in UCSF Chimera according to its local resolution. The output relion_locres_filtered.mrc is a composite map that is locally filtered to the estimated resolution. \
This is a developmental feature in need of further testing, but initial results indicate it may be useful. \n \n Note that only this program can use MPI, the ResMap wrapper cannot use MPI.");

	//joboptions["locres_sampling"] = JobOption("Sampling rate (A):", 25, 5, 50, 5, "The local-resolution map will be calculated every so many Angstroms, by placing soft spherical masks on a cubic grid with this spacing. Very fine samplings (e.g. < 15A?) may take a long time to compute and give spurious estimates!");
	//joboptions["randomize_at"] = JobOption("Frequency for phase-randomisation (A): ", 10., 5, 20., 1, "From this frequency onwards, the phases for the mask-corrected FSC-calculation will be randomized. Make sure this is a lower resolution (i.e. a higher number) than the local resolutions you are after in your map.");
	joboptions["adhoc_bfac"] = JobOption("User-provided B-factor:", -100, -500, 0, -25, "Probably, the overall B-factor as was estimated in the postprocess is a useful value for here. Use negative values for sharpening. Be careful: if you over-sharpen your map, you may end up interpreting noise for signal!");
	joboptions["fn_mtf"] = JobOption("MTF of the detector (STAR file)", "", "STAR Files (*.star)", ".", "The MTF of the detector is used to complement the user-provided B-factor in the sharpening. If you don't have this curve, you can leave this field empty.");
}


bool RelionJob::getCommandsLocalresJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;

	if (joboptions["do_resmap_locres"].getBoolean() == joboptions["do_relion_locres"].getBoolean())
	{
		error_message = "ERROR: choose either ResMap or Relion for local resolution estimation";
		return false;
	}

	if (joboptions["fn_in"].getString() == "")
	{
		error_message = "ERROR: empty field for input half-map...";
		return false;
	}
	// Get the two half-reconstruction names from the single one
	FileName fn_half1 = joboptions["fn_in"].getString();
	FileName fn_half2;
	if (!fn_half1.getTheOtherHalf(fn_half2))
	{
		error_message = "ERROR: cannot find 'half' substring in the input filename...";
		return false;
	}

	Node node(joboptions["fn_in"].getString(), joboptions["fn_in"].node_type);
	inputNodes.push_back(node);

	if (joboptions["do_resmap_locres"].getBoolean())
	{

		label += ".resmap";

		// ResMap wrapper
		if (joboptions["fn_resmap"].getString().length() == 0)
		{
			error_message = "ERROR: please provide an executable for the ResMap program.";
			return false;
		}

		if (joboptions["fn_mask"].getString() == "")
		{
			error_message = "ERROR: Please provide an input mask for ResMap local-resolution estimation.";
			return false;
		}

		if (joboptions["do_queue"].getBoolean())
		{
			error_message = "ERROR: You cannot submit a ResMap job to the queue, as it needs user interaction.";
			return false;
		}

		if (joboptions["nr_mpi"].getNumber(error_message) > 1)
		{
			error_message = "You cannot use more than 1 MPI processor for the ResMap wrapper...";
			return false;
		}
		if (error_message != "") return false;

		// Make symbolic links to the half-maps in the output directory
		commands.push_back("ln -s ../../" + fn_half1 + " " + outputname + "half1.mrc");
		commands.push_back("ln -s ../../" + fn_half2 + " " + outputname + "half2.mrc");

		Node node2(joboptions["fn_mask"].getString(), joboptions["fn_mask"].node_type);
		inputNodes.push_back(node2);

		Node node3(outputname + "half1_resmap.mrc", LABEL_LOCRES_RESMAP);
		outputNodes.push_back(node3);

		command = joboptions["fn_resmap"].getString();
		command += " --maskVol=" + joboptions["fn_mask"].getString();
		command += " --noguiSplit " + outputname + "half1.mrc " +  outputname + "half2.mrc";
		command += " --vxSize=" + joboptions["angpix"].getString();
		command += " --pVal=" + joboptions["pval"].getString();
		command += " --minRes=" + joboptions["minres"].getString();
		command += " --maxRes=" + joboptions["maxres"].getString();
		command += " --stepRes=" + joboptions["stepres"].getString();

	}
	else if (joboptions["do_relion_locres"].getBoolean())
	{
		// Relion postprocessing
		label += ".own";

		if (joboptions["nr_mpi"].getNumber(error_message) > 1)
			command="`which relion_postprocess_mpi`";
		else
			command="`which relion_postprocess`";
		if (error_message != "") return false;

		command += " --locres --i " + joboptions["fn_in"].getString();
		command += " --o " + outputname + "relion";
		command += " --angpix " + joboptions["angpix"].getString();
		//command += " --locres_sampling " + joboptions["locres_sampling"].getString();
		//command += " --locres_randomize_at " + joboptions["randomize_at"].getString();
		command += " --adhoc_bfac " + joboptions["adhoc_bfac"].getString();
		if (joboptions["fn_mtf"].getString() != "")
			command += " --mtf " + joboptions["fn_mtf"].getString();

		if (joboptions["fn_mask"].getString() != "")
		{
			command += " --mask " + joboptions["fn_mask"].getString();
			Node node0(outputname+"histogram.pdf", LABEL_LOCRES_LOG);
			outputNodes.push_back(node0);
		}

		Node node1(outputname+"relion_locres_filtered.mrc", LABEL_LOCRES_FILTMAP);
		outputNodes.push_back(node1);
		Node node2(outputname+"relion_locres.mrc", LABEL_LOCRES_RESMAP);
		outputNodes.push_back(node2);
	}

	// Other arguments for extraction
	command += " " + joboptions["other_args"].getString();
	commands.push_back(command);

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

