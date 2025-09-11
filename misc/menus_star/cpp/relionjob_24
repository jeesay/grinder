void RelionJob::initialiseExternalJob()
{
	hidden_name = ".gui_external";

	// I/O
	joboptions["fn_exe"] = JobOption("External executable:", "", "", ".", "Location of the script that will launch the external program. This script should write all its output in the directory specified with --o. Also, it should write in that same directory a file called RELION_JOB_EXIT_SUCCESS upon successful exit, and RELION_JOB_EXIT_FAILURE upon failure.");

	// Optional input nodes
	joboptions["in_mov"] = JobOption("Input movies: ", LABEL_MOVIES_CPIPE, 1, "", "movie STAR file (*.star)", "Input movies. This will be passed with a --in_movies argument to the executable.");
	joboptions["in_mic"] = JobOption("Input micrographs: ", LABEL_MICS_CPIPE, 1, "", "micrographs STAR file (*.star)", "Input micrographs. This will be passed with a --in_mics argument to the executable.");
	joboptions["in_part"] = JobOption("Input particles: ", LABEL_PARTS_CPIPE, 1, "", "particles STAR file (*.star)", "Input particles. This will be passed with a --in_parts argument to the executable.");
	joboptions["in_coords"] = JobOption("Input coordinates: ", LABEL_COORDS_CPIPE, 1, "", "STAR files (coords_suffix*.star)", "Input coordinates. This will be passed with a --in_coords argument to the executable.");
	joboptions["in_3dref"] = JobOption("Input 3D reference: ", LABEL_MAP_CPIPE, 1, "", "MRC files (*.mrc)", "Input 3D reference map. This will be passed with a --in_3dref argument to the executable.");
	joboptions["in_mask"] = JobOption("Input 3D mask: ", LABEL_MASK_CPIPE, 1, "", "MRC files (*.mrc)", "Input 3D mask. This will be passed with a --in_mask argument to the executable.");

	// Optional parameters
	joboptions["param1_label"] = JobOption("Param1 - label:", std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param1_value"] = JobOption("Param1 - value:" , std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param2_label"] = JobOption("Param2 - label:", std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param2_value"] = JobOption("Param2 - value:" , std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param3_label"] = JobOption("Param3 - label:", std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param3_value"] = JobOption("Param3 - value:" , std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param4_label"] = JobOption("Param4 - label:", std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param4_value"] = JobOption("Param4 - value:" , std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param5_label"] = JobOption("Param5 - label:", std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param5_value"] = JobOption("Param5 - value:" , std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param6_label"] = JobOption("Param6 - label:", std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param6_value"] = JobOption("Param6 - value:" , std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param7_label"] = JobOption("Param7 - label:", std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param7_value"] = JobOption("Param7 - value:" , std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param8_label"] = JobOption("Param8 - label:", std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param8_value"] = JobOption("Param8 - value:" , std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param9_label"] = JobOption("Param9 - label:", std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param9_value"] = JobOption("Param9 - value:" , std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param10_label"] = JobOption("Param10 - label:", std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
	joboptions["param10_value"] = JobOption("Param10 - value:" , std::string(""), "Define label and value for optional parameters to the script. These will be passed as an argument --label value");
}

bool RelionJob::getCommandsExternalJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;

	if (joboptions["fn_exe"].getString() == "")
	{
		error_message = "ERROR: empty field for the external executable script...";
		return false;
	}

	command=joboptions["fn_exe"].getString();
	command += " --o " + outputname;

	// Optional input nodes
	if (joboptions["in_mov"].getString() != "")
	{
		Node node(joboptions["in_mov"].getString(), joboptions["in_mov"].node_type);
		inputNodes.push_back(node);
		command += " --in_movies " + joboptions["in_mov"].getString();
	}
	if (joboptions["in_mic"].getString() != "")
	{
		Node node(joboptions["in_mic"].getString(), joboptions["in_mic"].node_type);
		inputNodes.push_back(node);
		command += " --in_mics " + joboptions["in_mic"].getString();
	}
	if (joboptions["in_part"].getString() != "")
	{
		Node node(joboptions["in_part"].getString(), joboptions["in_part"].node_type);
		inputNodes.push_back(node);
		command += " --in_parts " + joboptions["in_part"].getString();
	}
	if (joboptions["in_coords"].getString() != "")
	{
		Node node(joboptions["in_coords"].getString(), joboptions["in_coords"].node_type);
		inputNodes.push_back(node);
		command += " --in_coords " + joboptions["in_coords"].getString();
	}
	if (joboptions["in_3dref"].getString() != "")
	{
		Node node(joboptions["in_3dref"].getString(), joboptions["in_3dref"].node_type);
		inputNodes.push_back(node);
		command += " --in_3dref " + joboptions["in_3dref"].getString();
	}
	if (joboptions["in_mask"].getString() != "")
	{
		Node node(joboptions["in_mask"].getString(), joboptions["in_mask"].node_type);
		inputNodes.push_back(node);
		command += " --in_mask " + joboptions["in_mask"].getString();
	}

	// Optional arguments
	if (joboptions["param1_label"].getString() != "")
	{
		command += " --" + joboptions["param1_label"].getString() + " " + joboptions["param1_value"].getString();
	}
	if (joboptions["param2_label"].getString() != "")
	{
		command += " --" + joboptions["param2_label"].getString() + " " + joboptions["param2_value"].getString();
	}
	if (joboptions["param3_label"].getString() != "")
	{
		command += " --" + joboptions["param3_label"].getString() + " " + joboptions["param3_value"].getString();
	}
	if (joboptions["param4_label"].getString() != "")
	{
		command += " --" + joboptions["param4_label"].getString() + " " + joboptions["param4_value"].getString();
	}
	if (joboptions["param5_label"].getString() != "")
	{
		command += " --" + joboptions["param5_label"].getString() + " " + joboptions["param5_value"].getString();
	}
	if (joboptions["param6_label"].getString() != "")
	{
		command += " --" + joboptions["param6_label"].getString() + " " + joboptions["param6_value"].getString();
	}
	if (joboptions["param7_label"].getString() != "")
	{
		command += " --" + joboptions["param7_label"].getString() + " " + joboptions["param7_value"].getString();
	}
	if (joboptions["param8_label"].getString() != "")
	{
		command += " --" + joboptions["param8_label"].getString() + " " + joboptions["param8_value"].getString();
	}
	if (joboptions["param9_label"].getString() != "")
	{
		command += " --" + joboptions["param9_label"].getString() + " " + joboptions["param9_value"].getString();
	}
	if (joboptions["param10_label"].getString() != "")
	{
		command += " --" + joboptions["param10_label"].getString() + " " + joboptions["param10_value"].getString();
	}

	// Running stuff
	command += " --j " + joboptions["nr_threads"].getString();

	// Other arguments for extraction
	command += " " + joboptions["other_args"].getString();
	commands.push_back(command);

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

void RelionJob::addTomoInputOptions(bool has_tomograms, bool has_particles,
		bool has_trajectories, bool has_manifolds)
{
	joboptions["in_optimisation"] = JobOption("Input optimisation set: ", LABEL_TOMO_OPTSET_CPIPE, 1, "", "Optimisation set STAR file (*optimisation_set.star)", "Input optimisation set. This will be passed with a --i argument to the executable. If any inidividual components of the optimisation set are specified below, then they will override the components in this optimisation set.");

    // Optional input nodes
	joboptions["use_direct_entries"] = JobOption("OR: use direct entries?", false, "If set to to true, the optimisation set will be ignored and the direct entries below will be used instead.");
    if (has_particles) joboptions["in_particles"] = JobOption("Input particle set: ", LABEL_PARTS_CPIPE, 1, "", "Particle STAR file (*.star)", "Input particle set.");
	if (has_tomograms) joboptions["in_tomograms"] = JobOption("Input tomogram set: ", LABEL_TOMOGRAMS_CPIPE, 1, "", "Tomogram set STAR file (*.star)", "Input tomogram set STAR file. This file gets generated during Tomogram Reconstruction, and updated during Tomogram Frame Alignment or Tomogram CTF Refinement.");
    if (has_trajectories) joboptions["in_trajectories"] = JobOption("Input trajectory set: ", LABEL_TRAJECTORIES_CPIPE, 1, "", "Trajectory set STAR file (*.star)", "Input trajectory set. Leave empty if no particle motion tracks have been estimated during tomogram frame alignment.");
	if (has_manifolds) joboptions["in_manifolds"] = JobOption("Input manifold set: ", LABEL_MANIFOLDS_CPIPE, 1, "", "Manifold set STAR file (*.star)", "Input manifold set. Leave empty if no manifolds have been defined.");
}

std::string RelionJob::getTomoInputCommmand(bool is_for_refine, std::string &command, int has_tomograms, int has_particles,
		int has_trajectories, int has_manifolds)
{
	std::string error_message = "";

	if (!joboptions["use_direct_entries"].getBoolean())
    {
        if (joboptions["in_optimisation"].getString() == "")
        {
            error_message = "ERROR: no optimisation_set is provided, while you are also not using the direct input entries on the GUI.";
            return error_message;
        }
        else
        {
            Node node(joboptions["in_optimisation"].getString(), joboptions["in_optimisation"].node_type);
            inputNodes.push_back(node);
            if (is_for_refine)
                command += " --ios " + joboptions["in_optimisation"].getString();
            else
                command += " --i " + joboptions["in_optimisation"].getString();
        }

    }
    else
	{
        if (joboptions["in_optimisation"].getString() != "")
        {
            error_message = "ERROR: you have indicated to use direct input entries, but the entry for the optimisation set is not empty.";
            return error_message;
        }

        // Check all other necessary files are present
        if (has_tomograms == HAS_COMPULSORY && joboptions["in_tomograms"].getString() == "")
        {
            error_message = "ERROR: no tomogram set is specified (either by the optimisation_set or the direct entry)";
            return error_message;
        }
        if (has_particles == HAS_COMPULSORY && joboptions["in_particles"].getString() == "")
        {
            error_message = "ERROR: no particle set is specified (either by the optimisation_set or the direct entry)";
            return error_message;
        }
        if (has_trajectories == HAS_COMPULSORY && joboptions["in_trajectories"].getString() == "")
        {
            error_message = "ERROR: no trajectory set is specified (either by the optimisation_set or the direct entry)";
            return error_message;
        }
        if (has_manifolds == HAS_COMPULSORY && joboptions["in_manifolds"].getString() == "")
        {
            error_message = "ERROR: no manifold set is specified (either by the optimisation_set or the direct entry)";
            return error_message;
        }

        if (is_for_refine)
        {
            Node node(joboptions["in_particles"].getString(), joboptions["in_particles"].node_type);
            inputNodes.push_back(node);
            command += " --i " + joboptions["in_particles"].getString();

            Node node2(joboptions["in_tomograms"].getString(), joboptions["in_tomograms"].node_type);
            inputNodes.push_back(node2);
            command += " --tomograms " + joboptions["in_tomograms"].getString();

            if (joboptions["in_trajectories"].getString() != "")
            {
                Node node3(joboptions["in_trajectories"].getString(), joboptions["in_trajectories"].node_type);
                inputNodes.push_back(node2);
                command += " --trajectories " + joboptions["in_trajectories"].getString();
            }

        }
        else
        {
            if (has_particles != HAS_NOT && joboptions["in_particles"].getString() != "")
            {
                Node node(joboptions["in_particles"].getString(), joboptions["in_particles"].node_type);
                inputNodes.push_back(node);
                command += " --p " + joboptions["in_particles"].getString();
            }
            if (has_tomograms != HAS_NOT && joboptions["in_tomograms"].getString() != "")
            {
                Node node(joboptions["in_tomograms"].getString(), joboptions["in_tomograms"].node_type);
                inputNodes.push_back(node);
                command += " --t " + joboptions["in_tomograms"].getString();
            }
            if (has_trajectories != HAS_NOT && joboptions["in_trajectories"].getString() != "")
            {
                Node node(joboptions["in_trajectories"].getString(), joboptions["in_trajectories"].node_type);
                inputNodes.push_back(node);
                command += " --mot " + joboptions["in_trajectories"].getString();
            }
            if (has_manifolds != HAS_NOT && joboptions["in_manifolds"].getString() != "")
            {
                Node node(joboptions["in_manifolds"].getString(), joboptions["in_manifolds"].node_type);
                inputNodes.push_back(node);
                command += " --man " + joboptions["in_manifolds"].getString();
            }

        }
    }

	return error_message;
}

