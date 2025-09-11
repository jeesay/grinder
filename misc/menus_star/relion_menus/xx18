void RelionJob::initialisePostprocessJob()
{
	hidden_name = ".gui_post";

	joboptions["fn_in"] = JobOption("One of the 2 unfiltered half-maps:", LABEL_HALFMAP_CPIPE, 1, "", "MRC map files (*half1*.mrc)",  "Provide one of the two unfiltered half-reconstructions that were output upon convergence of a 3D auto-refine run.");
	joboptions["fn_mask"] = JobOption("Solvent mask:", LABEL_MASK_CPIPE, 1, "", "Image Files (*.{spi,vol,msk,mrc})", "Provide a soft mask where the protein is white (1) and the solvent is black (0). Often, the softer the mask the higher resolution estimates you will get. A soft edge of 5-10 pixels is often a good edge width.");
	joboptions["angpix"] = JobOption("Calibrated pixel size (A)", -1, 0.3, 5, 0.1, "Provide the final, calibrated pixel size in Angstroms. This value may be different from the pixel-size used thus far, e.g. when you have recalibrated the pixel size using the fit to a PDB model. The X-axis of the output FSC plot will use this calibrated value.");

	joboptions["do_auto_bfac"] = JobOption("Estimate B-factor automatically?", true, "If set to Yes, then the program will use the automated procedure described by Rosenthal and Henderson (2003, JMB) to estimate an overall B-factor for your map, and sharpen it accordingly. \
Note that your map must extend well beyond the lowest resolution included in the procedure below, which should not be set to resolutions much lower than 10 Angstroms. ");
	joboptions["autob_lowres"] = JobOption("Lowest resolution for auto-B fit (A):", 10, 8, 15, 0.5, "This is the lowest frequency (in Angstroms) that will be included in the linear fit of the Guinier plot as described in Rosenthal and Henderson (2003, JMB). Dont use values much lower or higher than 10 Angstroms. If your map does not extend beyond 10 Angstroms, then instead of the automated procedure use your own B-factor.");
	joboptions["do_adhoc_bfac"] = JobOption("Use your own B-factor?", false, "Instead of using the automated B-factor estimation, provide your own value. Use negative values for sharpening the map. \
This option is useful if your map does not extend beyond the 10A needed for the automated procedure, or when the automated procedure does not give a suitable value (e.g. in more disordered parts of the map).");
	joboptions["adhoc_bfac"] = JobOption("User-provided B-factor:", -1000, -2000, 0, -50, "Use negative values for sharpening. Be careful: if you over-sharpen your map, you may end up interpreting noise for signal!");

	joboptions["fn_mtf"] = JobOption("MTF of the detector (STAR file)", "", "STAR Files (*.star)", ".", "If you know the MTF of your detector, provide it here. Curves for some well-known detectors may be downloaded from the RELION Wiki. Also see there for the exact format \
\n If you do not know the MTF of your detector and do not want to measure it, then by leaving this entry empty, you include the MTF of your detector in your overall estimated B-factor upon sharpening the map.\
Although that is probably slightly less accurate, the overall quality of your map will probably not suffer very much.");
	joboptions["mtf_angpix"] = JobOption("Original detector pixel size:", 1.0, 0.3, 2.0, 0.1, "This is the original pixel size (in Angstroms) in the raw (non-super-resolution!) micrographs.");

	joboptions["do_skip_fsc_weighting"] = JobOption("Skip FSC-weighting?", false, "If set to No (the default), then the output map will be low-pass filtered according to the mask-corrected, gold-standard FSC-curve. \
Sometimes, it is also useful to provide an ad-hoc low-pass filter (option below), as due to local resolution variations some parts of the map may be better and other parts may be worse than the overall resolution as measured by the FSC. \
In such cases, set this option to Yes and provide an ad-hoc filter as described below.");
	joboptions["low_pass"] = JobOption("Ad-hoc low-pass filter (A):",5,1,40,1,"This option allows one to low-pass filter the map at a user-provided frequency (in Angstroms). When using a resolution that is higher than the gold-standard FSC-reported resolution, take care not to interpret noise in the map for signal...");
}

bool RelionJob::getCommandsPostprocessJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;

	command="`which relion_postprocess`";

	// Input mask
	if (joboptions["fn_mask"].getString() == "")
	{
		error_message = "ERROR: empty field for input mask...";
		return false;
	}
	command += " --mask " + joboptions["fn_mask"].getString();
	Node node3(joboptions["fn_mask"].getString(), joboptions["fn_mask"].node_type);
	inputNodes.push_back(node3);

	// Input half map (one of them)
	FileName fn_half1 = joboptions["fn_in"].getString();
	FileName fn_half2;

	if (fn_half1 == "")
	{
		error_message = "ERROR: empty field for input half-map...";
		return false;
	}

	if (fn_half1 != "")
	{
		if (!fn_half1.getTheOtherHalf(fn_half2))
		{
			error_message = "ERROR: cannot find 'half' substring in the input filename...";
			return false;
		}

		Node node(fn_half1, joboptions["fn_in"].node_type);
		inputNodes.push_back(node);
		command += " --i " + fn_half1;
	}

	// The output name contains a directory: use it for output
	command += " --o " + outputname + "postprocess";
	command += "  --angpix " + joboptions["angpix"].getString();
	Node node1(outputname+"postprocess.mrc", LABEL_POST_MAP);
	outputNodes.push_back(node1);
	Node node2(outputname+"postprocess_masked.mrc", LABEL_POST_MASKED);
	outputNodes.push_back(node2);

	Node node2b(outputname+"logfile.pdf", LABEL_POST_LOG);
	outputNodes.push_back(node2b);

	Node node2c(outputname+"postprocess.star", LABEL_POST_POST);
	outputNodes.push_back(node2c);

	// Sharpening
	if (joboptions["fn_mtf"].getString().length() > 0)
	{
		command += " --mtf " + joboptions["fn_mtf"].getString();
		command += " --mtf_angpix " + joboptions["mtf_angpix"].getString();
	}
	if (joboptions["do_auto_bfac"].getBoolean())
	{
		command += " --auto_bfac ";
		command += " --autob_lowres " + joboptions["autob_lowres"].getString();
	}
	if (joboptions["do_adhoc_bfac"].getBoolean())
	{
		command += " --adhoc_bfac " + joboptions["adhoc_bfac"].getString();
	}

	// Filtering
	if (joboptions["do_skip_fsc_weighting"].getBoolean())
	{
		command += " --skip_fsc_weighting ";
		command += " --low_pass "  + joboptions["low_pass"].getString();
	}

	// Other arguments for extraction
	command += " " + joboptions["other_args"].getString();

	commands.push_back(command);
	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

