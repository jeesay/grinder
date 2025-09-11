void RelionJob::initialiseSubtractJob()
{
	hidden_name = ".gui_subtract";

	joboptions["fn_opt"] = JobOption("Input optimiser.star: ", LABEL_OPTIMISER_CPIPE, 1, "", "STAR Files (*_optimiser.star)", "Select the *_optimiser.star file for the iteration of the 3D refinement/classification \
which you want to use for subtraction. It will use the maps from this run for the subtraction, and of no particles input STAR file is given below, it will use all of the particles from this run.");
	joboptions["fn_mask"] = JobOption("Mask of the signal to keep:", LABEL_MASK_CPIPE, 1, "", "Image Files (*.{spi,vol,msk,mrc})", "Provide a soft mask where the protein density you wish to subtract from the experimental particles is black (0) and the density you wish to keep is white (1).");
	joboptions["do_data"] = JobOption("Use different particles?", false, "If set to Yes, subtraction will be performed on the particles in the STAR file below, instead of on all the particles of the 3D refinement/classification from the optimiser.star file.");
	joboptions["fn_data"] = JobOption("Input particle star file:", LABEL_PARTS_CPIPE, 1, "", "particle STAR file (*.star)", "The particle STAR files with particles that will be used in the subtraction. Leave this field empty if all particles from the input refinement/classification run are to be used.");
	joboptions["do_float16"] = JobOption("Write output in float16?", true ,"If set to Yes, this program will write output images in float16 MRC format. This will save a factor of two in disk space compared to the default of writing in float32. Note that RELION and CCPEM will read float16 images, but other programs may not (yet) do so.");

	joboptions["do_fliplabel"] = JobOption("OR revert to original particles?", false, "If set to Yes, no signal subtraction is performed. Instead, the labels of rlnImageName and rlnImageOriginalName are flipped in the input STAR file given in the field below. This will make the STAR file point back to the original, non-subtracted images.");
	joboptions["fn_fliplabel"] = JobOption("revert this particle star file:", LABEL_PARTS_CPIPE, 1, "", "particle STAR file (*.star)", "The particle STAR files with particles that will be used for label reversion.");

	joboptions["do_center_mask"] = JobOption("Do center subtracted images on mask?", true, "If set to Yes, the subtracted particles will be centered on projections of the center-of-mass of the input mask.");
	joboptions["do_center_xyz"] = JobOption("Do center on my coordinates?", false, "If set to Yes, the subtracted particles will be centered on projections of the x,y,z coordinates below. The unit is pixel, not angstrom. The origin is at the center of the box, not at the corner.");
	joboptions["center_x"] = JobOption("Center coordinate (pix) - X:", std::string("0"), "X-coordinate of the 3D center (in pixels).");
	joboptions["center_y"] = JobOption("Center coordinate (pix) - Y:", std::string("0"), "Y-coordinate of the 3D center (in pixels).");
	joboptions["center_z"] = JobOption("Center coordinate (pix) - Z:", std::string("0"), "Z-coordinate of the 3D center (in pixels).");

	joboptions["new_box"] = JobOption("New box size:", -1, 64, 512, 32, "Provide a non-negative value to re-window the subtracted particles in a smaller box size." );
}

bool RelionJob::getCommandsSubtractJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;

	if (joboptions["do_fliplabel"].getBoolean())
	{
		if (joboptions["nr_mpi"].getNumber(error_message) > 1)
		{
			error_message = "You cannot use MPI parallelization to revert particle labels.";
			return false;
		}

		Node node(joboptions["fn_fliplabel"].getString(), joboptions["fn_fliplabel"].node_type);
		inputNodes.push_back(node);

		Node node2(outputname + "original.star", LABEL_SUBTRACT_REVERTED);
		outputNodes.push_back(node2);

		label += ".revert";

		command = "`which relion_particle_subtract`";
		command += " --revert " + joboptions["fn_fliplabel"].getString() + " --o " + outputname;
	}
	else
	{
		if (joboptions["nr_mpi"].getNumber(error_message) > 1)
			command="`which relion_particle_subtract_mpi`";
		else
			command="`which relion_particle_subtract`";
		if (error_message != "") return false;

		// I/O
		if (joboptions["fn_opt"].getString() == "")
		{
			error_message = "ERROR: empty field for input optimiser.star...";
			return false;
		}
		command += " --i " + joboptions["fn_opt"].getString();
		Node node(joboptions["fn_opt"].getString(), LABEL_OPTIMISER_CPIPE);
		inputNodes.push_back(node);

		if (joboptions["fn_mask"].getString() != "")
		{
			command += " --mask " + joboptions["fn_mask"].getString();
			Node node2(joboptions["fn_mask"].getString(), joboptions["fn_mask"].node_type);
			inputNodes.push_back(node2);
		}
		if (joboptions["do_data"].getBoolean())
		{
			if (joboptions["fn_data"].getString() == "")
			{
				error_message = "ERROR: empty field for the input particle STAR file...";
				return false;
			}
			command += " --data " + joboptions["fn_data"].getString();
			Node node3(joboptions["fn_data"].getString(), joboptions["fn_data"].node_type);
			inputNodes.push_back(node3);
		}

		command += " --o " + outputname;
		Node node4(outputname + "particles_subtracted.star", LABEL_SUBTRACT_SUBTRACTED);
		outputNodes.push_back(node4);

		if (joboptions["do_center_mask"].getBoolean())
		{
			command += " --recenter_on_mask";
		}
		else if (joboptions["do_center_xyz"].getBoolean())
		{
			command += " --center_x " + joboptions["center_x"].getString();
			command += " --center_y " + joboptions["center_y"].getString();
			command += " --center_z " + joboptions["center_z"].getString();
		}

		if (joboptions["do_float16"].getBoolean())
		{
			command += " --float16 ";
		}

		if (joboptions["new_box"].getNumber(error_message) > 0)
		{
			command += " --new_box " + joboptions["new_box"].getString();
		}
		if (error_message != "") return false;

	}

	// Other arguments
	command += " " + joboptions["other_args"].getString();

	commands.push_back(command);

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

