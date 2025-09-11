void RelionJob::initialiseManualpickJob()
{
	hidden_name = ".gui_manualpick";

	joboptions["fn_in"] = JobOption("Input micrographs:", LABEL_MICS_CPIPE, 1, "", "Input micrographs (*.{star,mrc})", "Input STAR file (with or without CTF information), OR a unix-type wildcard with all micrographs in MRC format (in this case no CTFs can be used).");

	joboptions["diameter"] = JobOption("Particle diameter (A):", 100, 0, 500, 50, "The diameter of the circle used around picked particles (in Angstroms). Only used for display." );
	joboptions["micscale"] = JobOption("Scale for micrographs:", 0.2, 0.1, 1, 0.05, "The micrographs will be displayed at this relative scale, i.e. a value of 0.5 means that only every second pixel will be displayed." );
	joboptions["sigma_contrast"] = JobOption("Sigma contrast:", 3, 0, 10, 0.5, "The micrographs will be displayed with the black value set to the average of all values MINUS this values times the standard deviation of all values in the micrograph, and the white value will be set \
to the average PLUS this value times the standard deviation. Use zero to set the minimum value in the micrograph to black, and the maximum value to white ");
	joboptions["white_val"] = JobOption("White value:", 0, 0, 512, 16, "Use non-zero values to set the value of the whitest pixel in the micrograph.");
	joboptions["black_val"] = JobOption("Black value:", 0, 0, 512, 16, "Use non-zero values to set the value of the blackest pixel in the micrograph.");

	joboptions["lowpass"] = JobOption("Lowpass filter (A)", 20, 10, 100, 5, "Lowpass filter that will be applied to the micrographs. Give a negative value to skip the lowpass filter.");
	joboptions["highpass"] = JobOption("Highpass filter (A)", -1, 100, 1000, 100, "Highpass filter that will be applied to the micrographs. This may be useful to get rid of background ramps due to uneven ice distributions. Give a negative value to skip the highpass filter. Useful values are often in the range of 200-400 Angstroms.");
	joboptions["angpix"] = JobOption("Pixel size (A)", -1, 0.3, 5, 0.1, "Pixel size in Angstroms. This will be used to calculate the filters and the particle diameter in pixels. If a CTF-containing STAR file is input, then the value given here will be ignored, and the pixel size will be calculated from the values in the STAR file. A negative value can then be given here.");
	joboptions["do_topaz_denoise"] = JobOption("OR: use Topaz denoising?", false, "If set to true, Topaz denoising will be performed instead of lowpass filtering.");

	joboptions["do_startend"] = JobOption("Pick start-end coordinates helices?", false, "If set to true, start and end coordinates are picked subsequently and a line will be drawn between each pair");

	joboptions["do_fom_threshold"] = JobOption("Use autopick FOM threshold?", false, "If set to Yes, only particles with rlnAutopickFigureOfMerit values below the threshold below will be extracted.");
	joboptions["minimum_pick_fom"] = JobOption("Minimum autopick FOM: ", 0, -5, 10, 0.1, "The minimum value for the rlnAutopickFigureOfMerit for particles to be extracted.");

	joboptions["do_color"] = JobOption("Blue<>red color particles?", false, "If set to true, then the circles for each particles are coloured from red to blue (or the other way around) for a given metadatalabel. If this metadatalabel is not in the picked coordinates STAR file \
(basically only the rlnAutopickFigureOfMerit or rlnClassNumber) would be useful values there, then you may provide an additional STAR file (e.g. after classification/refinement below. Particles with values -999, or that are not in the additional STAR file will be coloured the default color: green");
	joboptions["color_label"] = JobOption("MetaDataLabel for color:", std::string("rlnAutopickFigureOfMerit"), "The Metadata label of the value to plot from red<>blue. Useful examples might be: \n \
rlnParticleSelectZScore \n rlnClassNumber \n rlnAutopickFigureOfMerit \n rlnAngleTilt \n rlnLogLikeliContribution \n rlnMaxValueProbDistribution \n rlnNrOfSignificantSamples\n");
	joboptions["fn_color"] = JobOption("STAR file with color label: ", "", "STAR file (*.star)", ".", "The program will figure out which particles in this STAR file are on the current micrograph and color their circles according to the value in the corresponding column. \
Particles that are not in this STAR file, but present in the picked coordinates file will be colored green. If this field is left empty, then the color label (e.g. rlnAutopickFigureOfMerit) should be present in the coordinates STAR file.");
	joboptions["blue_value"] = JobOption("Blue value: ", 0., 0., 4., 0.1, "The value of this entry will be blue. There will be a linear scale from blue to red, according to this value and the one given below.");
	joboptions["red_value"] = JobOption("Red value: ", 2., 0., 4., 0.1, "The value of this entry will be red. There will be a linear scale from blue to red, according to this value and the one given above.");
}

bool RelionJob::getCommandsManualpickJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;

	command="`which relion_manualpick`";

	if (joboptions["fn_in"].getString() == "")
	{
		error_message = "ERROR: empty field for input STAR file...";
		return false;
	}

	command += " --i " + joboptions["fn_in"].getString();
	Node node(joboptions["fn_in"].getString(), joboptions["fn_in"].node_type);
	inputNodes.push_back(node);

	command += " --odir " + outputname;
	command += " --pickname manualpick";

	// Allow saving, and always save default selection file upon launching the program
	FileName fn_outstar = outputname + "micrographs_selected.star";
	Node node3(fn_outstar, LABEL_MANPICK_MICS);
	outputNodes.push_back(node3);
	command += " --allow_save --fast_save --selection " + fn_outstar;

	command += " --scale " + joboptions["micscale"].getString();
	command += " --sigma_contrast " + joboptions["sigma_contrast"].getString();
	command += " --black " + joboptions["black_val"].getString();
	command += " --white " + joboptions["white_val"].getString();

	if (joboptions["do_topaz_denoise"].getBoolean())
	{
		command += " --topaz_denoise";
	}
	else
	{
		if (joboptions["lowpass"].getNumber(error_message) > 0.)
			command += " --lowpass " + joboptions["lowpass"].getString();
		if (error_message != "") return false;

		if (joboptions["highpass"].getNumber(error_message) > 0.)
			command += " --highpass " + joboptions["highpass"].getString();
		if (error_message != "") return false;

		if (joboptions["angpix"].getNumber(error_message) > 0.)
			command += " --angpix " + joboptions["angpix"].getString();
		if (error_message != "") return false;
	}

	if (joboptions["do_fom_threshold"].getBoolean())
	{
		command += " --minimum_pick_fom " + joboptions["minimum_pick_fom"].getString();
	}

	command += " --particle_diameter " + joboptions["diameter"].getString();

	if (joboptions["do_startend"].getBoolean())
	{
		label += ".helical";

		command += " --pick_start_end ";

		// new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
		Node node2(outputname + "manualpick.star", LABEL_MANPICK_COORDS_HELIX);
		outputNodes.push_back(node2);
	}

	else
	{
		// new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
		Node node2(outputname + "manualpick.star", LABEL_MANPICK_COORDS);
		outputNodes.push_back(node2);
	}

	if (joboptions["do_color"].getBoolean())
	{
		command += " --color_label " + joboptions["color_label"].getString();
		command += " --blue " + joboptions["blue_value"].getString();
		command += " --red " + joboptions["red_value"].getString();
		if (joboptions["fn_color"].getString().length() > 0)
			command += " --color_star " + joboptions["fn_color"].getString();
	}

	// Other arguments for extraction
	command += " " + joboptions["other_args"].getString();

	commands.push_back(command);

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

