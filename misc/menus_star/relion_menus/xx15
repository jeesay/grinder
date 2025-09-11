void RelionJob::initialiseMaskcreateJob()
{
	hidden_name = ".gui_maskcreate";

	joboptions["fn_in"] = JobOption("Input 3D map:", LABEL_MAP_CPIPE, 1, "", "MRC map files (*.mrc)", "Provide an input MRC map from which to start binarizing the map.");

	joboptions["lowpass_filter"] = JobOption("Lowpass filter map (A)", 15, 10, 100, 5, "Lowpass filter that will be applied to the input map, prior to binarization. To calculate solvent masks, a lowpass filter of 15-20A may work well.");
	joboptions["angpix"] = JobOption("Pixel size (A)", -1, 0.3, 5, 0.1, "Provide the pixel size of the input map in Angstroms to calculate the low-pass filter. This value is also used in the output image header.");

	joboptions["inimask_threshold"] = JobOption("Initial binarisation threshold:", 0.02, 0., 0.5, 0.01, "This threshold is used to make an initial binary mask from the average of the two unfiltered half-reconstructions. \
If you don't know what value to use, display one of the unfiltered half-maps in a 3D surface rendering viewer and find the lowest threshold that gives no noise peaks outside the reconstruction.");
	joboptions["extend_inimask"] = JobOption("Extend binary map this many pixels:", 3, 0, 20, 1, "The initial binary mask is extended this number of pixels in all directions." );
	joboptions["width_mask_edge"] = JobOption("Add a soft-edge of this many pixels:", 3, 0, 20, 1, "The extended binary mask is further extended with a raised-cosine soft edge of the specified width." );

	joboptions["do_helix"] = JobOption("Mask a 3D helix?", false, "Generate a mask for 3D helix which spans across Z axis of the box.");
	joboptions["helical_z_percentage"] = JobOption("Central Z length (%):", 30., 5., 80., 1., "Reconstructed helix suffers from inaccuracies of orientation searches. \
The central part of the box contains more reliable information compared to the top and bottom parts along Z axis. Set this value (%) to the central part length along Z axis divided by the box size. Values around 30% are commonly used but you may want to try different lengths.");
}

bool RelionJob::getCommandsMaskcreateJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;

	command="`which relion_mask_create`";

	// I/O
	if (joboptions["fn_in"].getString() == "")
	{
		error_message = "ERROR: empty field for input STAR file...";
		return false;
	}
	command += " --i " + joboptions["fn_in"].getString();
	Node node(joboptions["fn_in"].getString(), joboptions["fn_in"].node_type);
	inputNodes.push_back(node);

	command += " --o " + outputname + "mask.mrc";
	Node node2(outputname + "mask.mrc", LABEL_MASK3D_MASK);
	outputNodes.push_back(node2);

	if (joboptions["lowpass_filter"].getNumber(error_message) > 0)
	{
		command += " --lowpass " + joboptions["lowpass_filter"].getString();
	}
	if (error_message != "") return false;

	if (joboptions["angpix"].getNumber(error_message) > 0)
	{
		command += " --angpix " + joboptions["angpix"].getString();
	}
	if (error_message != "") return false;

	command += " --ini_threshold " + joboptions["inimask_threshold"].getString();
	command += " --extend_inimask " + joboptions["extend_inimask"].getString();
	command += " --width_soft_edge " + joboptions["width_mask_edge"].getString();

	if (joboptions["do_helix"].getBoolean())
	{
		command += " --helix --z_percentage " + floatToString(joboptions["helical_z_percentage"].getNumber(error_message) / 100.);
		if (error_message != "") return false;
	}

	// Running stuff
	command += " --j " + joboptions["nr_threads"].getString();

	// Other arguments
	command += " " + joboptions["other_args"].getString();

	commands.push_back(command);

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

