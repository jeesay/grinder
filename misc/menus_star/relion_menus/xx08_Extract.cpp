void RelionJob::initialiseExtractJob()
{
	hidden_name = ".gui_extract";

	joboptions["star_mics"]= JobOption("micrograph STAR file: ", LABEL_MICS_CPIPE, 1, "", "Input STAR file (*.{star})", "Filename of the STAR file that contains all micrographs from which to extract particles.");
	// TO DOL set helical option for this
	joboptions["coords_suffix"] = JobOption("Input coordinates: ", LABEL_COORDS_CPIPE, 1, "", "Input coordinates list file (*.star)", "Starfile with a 2-column list of micrograph names and corresponding coordinate filenames (in .star, .box or as 2 or 3-column free text format)");
	joboptions["do_reextract"] = JobOption("OR re-extract refined particles? ", false, "If set to Yes, the input Coordinates above will be ignored. Instead, one uses a _data.star file from a previous 2D or 3D refinement to re-extract the particles in that refinement, possibly re-centered with their refined origin offsets. This is particularly useful when going from binned to unbinned particles.");
	joboptions["fndata_reextract"] = JobOption("Refined particles STAR file: ", LABEL_PARTS_CPIPE, 1, "", "Input STAR file (*.{star})", "Filename of the STAR file with the refined particle coordinates, e.g. from a previous 2D or 3D classification or auto-refine run.");
	joboptions["do_reset_offsets"] = JobOption("Reset the refined offsets to zero? ", false, "If set to Yes, the input origin offsets will be reset to zero. This may be useful after 2D classification of helical segments, where one does not want neighbouring segments to be translated on top of each other for a subsequent 3D refinement or classification.");
	joboptions["do_recenter"] = JobOption("OR: re-center refined coordinates? ", false, "If set to Yes, the input coordinates will be re-centered according to the refined origin offsets in the provided _data.star file. The unit is pixel, not angstrom. The origin is at the center of the box, not at the corner.");
	joboptions["recenter_x"] = JobOption("Re-center on X-coordinate (in pix): ", std::string("0"), "Re-extract particles centered on this X-coordinate (in pixels in the reference)");
	joboptions["recenter_y"] = JobOption("Re-center on Y-coordinate (in pix): ", std::string("0"), "Re-extract particles centered on this Y-coordinate (in pixels in the reference)");
	joboptions["recenter_z"] = JobOption("Re-center on Z-coordinate (in pix): ", std::string("0"), "Re-extract particles centered on this Z-coordinate (in pixels in the reference)");
	joboptions["extract_size"] = JobOption("Particle box size (pix):", 128, 64, 512, 8, "Size of the extracted particles (in pixels). This should be an even number!");
	joboptions["do_invert"] = JobOption("Invert contrast?", true, "If set to Yes, the contrast in the particles will be inverted.");
	joboptions["do_float16"] = JobOption("Write output in float16?", true ,"If set to Yes, this program will write output images in float16 MRC format. This will save a factor of two in disk space compared to the default of writing in float32. Note that RELION and CCPEM will read float16 images, but other programs may not (yet) do so.");

	joboptions["do_norm"] = JobOption("Normalize particles?", true, "If set to Yes, particles will be normalized in the way RELION prefers it.");
	joboptions["bg_diameter"] = JobOption("Diameter background circle (pix): ", -1, -1, 600, 10, "Particles will be normalized to a mean value of zero and a standard-deviation of one for all pixels in the background area.\
The background area is defined as all pixels outside a circle with this given diameter in pixels (before rescaling). When specifying a negative value, a default value of 75% of the Particle box size will be used.");
	joboptions["white_dust"] = JobOption("Stddev for white dust removal: ", -1, -1, 10, 0.1, "Remove very white pixels from the extracted particles. \
Pixels values higher than this many times the image stddev will be replaced with values from a Gaussian distribution. \n \n Use negative value to switch off dust removal.");
	joboptions["black_dust"] = JobOption("Stddev for black dust removal: ", -1, -1, 10, 0.1, "Remove very black pixels from the extracted particles. \
Pixels values higher than this many times the image stddev will be replaced with values from a Gaussian distribution. \n \n Use negative value to switch off dust removal.");
	joboptions["do_rescale"] = JobOption("Rescale particles?", false, "If set to Yes, particles will be re-scaled. Note that the particle diameter below will be in the down-scaled images.");
	joboptions["rescale"] = JobOption("Re-scaled size (pixels): ", 128, 64, 512, 8, "The re-scaled value needs to be an even number");
	joboptions["do_fom_threshold"] = JobOption("Use autopick FOM threshold?", false, "If set to Yes, only particles with rlnAutopickFigureOfMerit values below the threshold below will be extracted.");
	joboptions["minimum_pick_fom"] = JobOption("Minimum autopick FOM: ", 0, -5, 10, 0.1, "The minimum value for the rlnAutopickFigureOfMerit for particles to be extracted.");

	joboptions["do_extract_helix"] = JobOption("Extract helical segments?", false, "Set to Yes if you want to extract helical segments. RELION (.star), EMAN2 (.box) and XIMDISP (.coords) formats of tube or segment coordinates are supported.");
	joboptions["helical_tube_outer_diameter"] = JobOption("Tube diameter (A): ", 200, 100, 1000, 10, "Outer diameter (in Angstroms) of helical tubes. \
This value should be slightly larger than the actual width of helical tubes.");
	joboptions["helical_bimodal_angular_priors"] = JobOption("Use bimodal angular priors?", true, "Normally it should be set to Yes and bimodal angular priors will be applied in the following classification and refinement jobs. \
Set to No if the 3D helix looks the same when rotated upside down.");
	joboptions["do_extract_helical_tubes"] = JobOption("Coordinates are start-end only?", true, "Set to Yes if you want to extract helical segments from manually picked tube coordinates (starting and end points of helical tubes in RELION, EMAN or XIMDISP format). \
Set to No if segment coordinates (RELION auto-picked results or EMAN / XIMDISP segments) are provided.");
	joboptions["do_cut_into_segments"] = JobOption("Cut helical tubes into segments?", true, "Set to Yes if you want to extract multiple helical segments with a fixed inter-box distance. \
If it is set to No, only one box at the center of each helical tube will be extracted.");
	joboptions["helical_nr_asu"] = JobOption("Number of unique asymmetrical units:", 1, 1, 100, 1, "Number of unique helical asymmetrical units in each segment box. This integer should not be less than 1. The inter-box distance (pixels) = helical rise (Angstroms) * number of asymmetrical units / pixel size (Angstroms). \
The optimal inter-box distance might also depend on the box size, the helical rise and the flexibility of the structure. In general, an inter-box distance of ~10% * the box size seems appropriate.");
	joboptions["helical_rise"] = JobOption("Helical rise (A):", 1, 0, 100, 0.01, "Helical rise in Angstroms. (Please click '?' next to the option above for details about how the inter-box distance is calculated.)");

}

bool RelionJob::getCommandsExtractJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;
	if (joboptions["nr_mpi"].getNumber(error_message) > 1)
		command="`which relion_preprocess_mpi`";
	else
		command="`which relion_preprocess`";
	if (error_message != "") return false;

	// Input
	if (joboptions["star_mics"].getString() == "")
	{
		error_message = "ERROR: empty field for input STAR file...";
		return false;
	}
	command += " --i " + joboptions["star_mics"].getString();
	Node node(joboptions["star_mics"].getString(), joboptions["star_mics"].node_type);
	inputNodes.push_back(node);

	if (joboptions["do_reextract"].getBoolean())
	{
		if (joboptions["fndata_reextract"].getString() == "")
		{
			error_message = "ERROR: empty field for refined particles STAR file...";
			return false;
		}

		if (joboptions["do_reset_offsets"].getBoolean() && joboptions["do_recenter"].getBoolean())
		{
			error_message = "ERROR: you cannot both reset refined offsets and recenter on refined coordinates, choose one...";
			return false;
		}

		label += ".reextract";

		command += " --reextract_data_star " + joboptions["fndata_reextract"].getString();
		Node node2(joboptions["fndata_reextract"].getString(), joboptions["fndata_reextract"].node_type);
		inputNodes.push_back(node2);
		if (joboptions["do_reset_offsets"].getBoolean())
		{
			command += " --reset_offsets";
		}
		else if (joboptions["do_recenter"].getBoolean())
		{
			command += " --recenter";
			command += " --recenter_x " + joboptions["recenter_x"].getString();
			command += " --recenter_y " + joboptions["recenter_y"].getString();
			command += " --recenter_z " + joboptions["recenter_z"].getString();
		}
	}
	else
	{
		FileName mylist = joboptions["coords_suffix"].getString();
		if (mylist == "")
		{
			error_message = "ERROR: empty field for coordinate STAR file...";
			return false;
		}
		// Attempt at backwards compatibility
		if (mylist.contains("coords_suffix"))
		{
			command += " --coord_dir " + mylist.beforeLastOf("/") + "/";
			command += " --coord_suffix " + (mylist.afterLastOf("/")).without("coords_suffix");
		}
		else
		{
			command += " --coord_list " + mylist;
		}
		Node node2(mylist, joboptions["coords_suffix"].node_type);
		inputNodes.push_back(node2);
	}

	// Output
	FileName fn_ostar = outputname + "particles.star";

	command += " --part_star " + fn_ostar;

	if (joboptions["do_reextract"].getBoolean())
	{
		FileName fn_pickstar = outputname + "extractpick.star";
		Node node(fn_pickstar, LABEL_EXTRACT_COORDS_REEX);
		outputNodes.push_back(node);
		command += " --pick_star " + fn_pickstar;
	}

	if (joboptions["do_extract_helix"].getBoolean() && joboptions["do_extract_helical_tubes"].getBoolean())
	{
		FileName fn_pickstar = outputname + "extractpick.star";
		Node node(fn_pickstar, LABEL_EXTRACT_COORDS_HELIX);
		outputNodes.push_back(node);
		command += " --pick_star " + fn_pickstar;
	}


	command += " --part_dir " + outputname;
	command += " --extract";
	command += " --extract_size " + joboptions["extract_size"].getString();

	if (joboptions["do_fom_threshold"].getBoolean())
	{
		command += " --minimum_pick_fom " + joboptions["minimum_pick_fom"].getString();
	}

	if (joboptions["do_float16"].getBoolean())
	{
		command += " --float16 ";
	}

	// Operate stuff
	// Get an integer number for the bg_radius
	RFLOAT bg_radius = (joboptions["bg_diameter"].getNumber(error_message) < 0.) ? 0.75 * joboptions["extract_size"].getNumber(error_message) : joboptions["bg_diameter"].getNumber(error_message);
	if (error_message != "") return false;

	bg_radius /= 2.; // Go from diameter to radius
	if (joboptions["do_rescale"].getBoolean())
	{
		command += " --scale " + joboptions["rescale"].getString();
		bg_radius *= joboptions["rescale"].getNumber(error_message);
		if (error_message != "") return false;

		bg_radius /= joboptions["extract_size"].getNumber(error_message);
		if (error_message != "") return false;
	}
	if (joboptions["do_norm"].getBoolean())
	{
		// Get an integer number for the bg_radius
		bg_radius = (int)bg_radius;
		command += " --norm --bg_radius " + floatToString(bg_radius);
		command += " --white_dust " + joboptions["white_dust"].getString();
		command += " --black_dust " + joboptions["black_dust"].getString();
	}
	if (joboptions["do_invert"].getBoolean())
		command += " --invert_contrast ";

	// Helix
	if (joboptions["do_extract_helix"].getBoolean())
	{
		Node node3(fn_ostar, LABEL_EXTRACT_PARTS_HELIX);
		outputNodes.push_back(node3);

		label += ".helical";

		command += " --helix";
		command += " --helical_outer_diameter " + joboptions["helical_tube_outer_diameter"].getString();
		if (joboptions["helical_bimodal_angular_priors"].getBoolean())
			command += " --helical_bimodal_angular_priors";
		if (joboptions["do_extract_helical_tubes"].getBoolean())
		{
			command += " --helical_tubes";
			if (joboptions["do_cut_into_segments"].getBoolean())
			{
				command += " --helical_cut_into_segments";
				command += " --helical_nr_asu " + joboptions["helical_nr_asu"].getString();
				command += " --helical_rise " + joboptions["helical_rise"].getString();
			}
			else
				command += " --helical_nr_asu 1 --helical_rise 1";
		}
	}
	else
	{
		Node node3(fn_ostar, LABEL_EXTRACT_PARTS);
		outputNodes.push_back(node3);
	}


	if (is_continue)
		command += " --only_do_unfinished ";


	// Other arguments for extraction
	command += " " + joboptions["other_args"].getString();
	commands.push_back(command);


	if (joboptions["do_reextract"].getBoolean())
	{
		Node node(outputname + "reextract.star", LABEL_EXTRACT_COORDS_REEX);
		outputNodes.push_back(node);
	}

	if (joboptions["do_extract_helix"].getBoolean() && joboptions["do_extract_helical_tubes"].getBoolean())
	{
		Node node(outputname + "helix_segments.star", LABEL_EXTRACT_COORDS_HELIX);
		outputNodes.push_back(node);
	}


	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

