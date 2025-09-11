void RelionJob::initialiseJoinstarJob()
{
	hidden_name = ".gui_joinstar";

	joboptions["do_part"] = JobOption("Combine particle STAR files?", false, "");
	joboptions["fn_part1"] = JobOption("Particle STAR file 1: ", LABEL_PARTS_CPIPE, 1, "", "particle STAR file (*.star)", "The first of the particle STAR files to be combined.");
	joboptions["fn_part2"] = JobOption("Particle STAR file 2: ", LABEL_PARTS_CPIPE, 1, "", "particle STAR file (*.star)", "The second of the particle STAR files to be combined.");
	joboptions["fn_part3"] = JobOption("Particle STAR file 3: ", LABEL_PARTS_CPIPE, 1, "", "particle STAR file (*.star)", "The third of the particle STAR files to be combined. Leave empty if there are only two files to be combined.");
	joboptions["fn_part4"] = JobOption("Particle STAR file 4: ", LABEL_PARTS_CPIPE, 1, "", "particle STAR file (*.star)", "The fourth of the particle STAR files to be combined. Leave empty if there are only two or three files to be combined.");

	joboptions["do_mic"] = JobOption("Combine micrograph STAR files?", false, "");
	joboptions["fn_mic1"] = JobOption("Micrograph STAR file 1: ", LABEL_MICS_CPIPE, 1, "", "micrograph STAR file (*.star)", "The first of the micrograph STAR files to be combined.");
	joboptions["fn_mic2"] = JobOption("Micrograph STAR file 2: ", LABEL_MICS_CPIPE, 1, "", "micrograph STAR file (*.star)", "The second of the micrograph STAR files to be combined.");
	joboptions["fn_mic3"] = JobOption("Micrograph STAR file 3: ", LABEL_MICS_CPIPE, 1, "", "micrograph STAR file (*.star)", "The third of the micrograph STAR files to be combined. Leave empty if there are only two files to be combined.");
	joboptions["fn_mic4"] = JobOption("Micrograph STAR file 4: ", LABEL_MICS_CPIPE, 1, "", "micrograph STAR file (*.star)", "The fourth of the micrograph STAR files to be combined. Leave empty if there are only two or three files to be combined.");

	joboptions["do_mov"] = JobOption("Combine movie STAR files?", false, "");
	joboptions["fn_mov1"] = JobOption("Movie STAR file 1: ", LABEL_MOVIES_CPIPE, 1, "", "movie STAR file (*.star)", "The first of the micrograph movie STAR files to be combined.");
	joboptions["fn_mov2"] = JobOption("Movie STAR file 2: ", LABEL_MOVIES_CPIPE, 1, "", "movie STAR file (*.star)", "The second of the micrograph movie STAR files to be combined.");
	joboptions["fn_mov3"] = JobOption("Movie STAR file 3: ", LABEL_MOVIES_CPIPE, 1, "", "movie STAR file (*.star)", "The third of the micrograph movie STAR files to be combined. Leave empty if there are only two files to be combined.");
	joboptions["fn_mov4"] = JobOption("Movie STAR file 4: ", LABEL_MOVIES_CPIPE, 1, "", "movie STAR file (*.star)", "The fourth of the micrograph movie STAR files to be combined. Leave empty if there are only two or three files to be combined.");
}

bool RelionJob::getCommandsJoinstarJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;
	command="`which relion_star_handler`";

	int ii = 0;
	if (joboptions["do_part"].getBoolean())
	{
		ii++;
		label += ".particles";
	}
	if (joboptions["do_mic"].getBoolean())
	{
		ii++;
		label += ".micrographs";
	}
	if (joboptions["do_mov"].getBoolean())
	{
		ii++;
		label += ".movies";
	}

	if (ii == 0)
	{
		error_message = "You've selected no type of files for joining. Select a single type!";
		return false;
	}

	if (ii > 1)
	{
		error_message = "You've selected more than one type of files for joining. Only select a single type!";
		return false;
	}

	// I/O
	if (joboptions["do_part"].getBoolean())
	{
		if (joboptions["fn_part1"].getString() == "" || joboptions["fn_part2"].getString() == "")
		{
			error_message = "ERROR: empty field for first or second input STAR file...";
			return false;
		}
		command += " --combine --i \" " + joboptions["fn_part1"].getString();
		Node node(joboptions["fn_part1"].getString(), joboptions["fn_part1"].node_type);
		inputNodes.push_back(node);
		command += " " + joboptions["fn_part2"].getString();
		Node node2(joboptions["fn_part2"].getString(), joboptions["fn_part2"].node_type);
		inputNodes.push_back(node2);
		if (joboptions["fn_part3"].getString() != "")
		{
			command += " " + joboptions["fn_part3"].getString();
			Node node3(joboptions["fn_part3"].getString(), joboptions["fn_part3"].node_type);
			inputNodes.push_back(node3);
		}
		if (joboptions["fn_part4"].getString() != "")
		{
			command += " " + joboptions["fn_part4"].getString();
			Node node4(joboptions["fn_part4"].getString(), joboptions["fn_part4"].node_type);
			inputNodes.push_back(node4);
		}
		command += " \" ";

		// Check for duplicates
		command += " --check_duplicates rlnImageName ";
		command += " --o " + outputname + "join_particles.star";
		Node node5(outputname + "join_particles.star", joboptions["fn_part1"].node_type);
		outputNodes.push_back(node5);

	}
	else if (joboptions["do_mic"].getBoolean())
	{
		if (joboptions["fn_mic1"].getString() == "" || joboptions["fn_mic2"].getString() == "")
		{
			error_message = "ERROR: empty field for first or second input STAR file...";
			return false;
		}
		command += " --combine --i \" " + joboptions["fn_mic1"].getString();
		Node node(joboptions["fn_mic1"].getString(), joboptions["fn_mic1"].node_type);
		inputNodes.push_back(node);
		command += " " + joboptions["fn_mic2"].getString();
		Node node2(joboptions["fn_mic2"].getString(), joboptions["fn_mic2"].node_type);
		inputNodes.push_back(node2);
		if (joboptions["fn_mic3"].getString() != "")
		{
			command += " " + joboptions["fn_mic3"].getString();
			Node node3(joboptions["fn_mic3"].getString(), joboptions["fn_mic3"].node_type);
			inputNodes.push_back(node3);
		}
		if (joboptions["fn_mic4"].getString() != "")
		{
			command += " " + joboptions["fn_mic4"].getString();
			Node node4(joboptions["fn_mic4"].getString(), joboptions["fn_mic4"].node_type);
			inputNodes.push_back(node4);
		}
		command += " \" ";

		// Check for duplicates
		command += " --check_duplicates rlnMicrographName ";
		command += " --o " + outputname + "join_mics.star";
		Node node5(outputname + "join_mics.star", joboptions["fn_mic1"].node_type);
		outputNodes.push_back(node5);

	}
	else if (joboptions["do_mov"].getBoolean())
	{
		if (joboptions["fn_mov1"].getString() == "" || joboptions["fn_mov2"].getString() == "")
		{
			error_message = "ERROR: empty field for first or second input STAR file...";
			return false;
		}
		command += " --combine --i \" " + joboptions["fn_mov1"].getString();
		Node node(joboptions["fn_mov1"].getString(), joboptions["fn_mov1"].node_type);
		inputNodes.push_back(node);
		command += " " + joboptions["fn_mov2"].getString();
		Node node2(joboptions["fn_mov2"].getString(), joboptions["fn_mov2"].node_type);
		inputNodes.push_back(node2);
		if (joboptions["fn_mov3"].getString() != "")
		{
			command += " " + joboptions["fn_mov3"].getString();
			Node node3(joboptions["fn_mov3"].getString(), joboptions["fn_mov3"].node_type);
			inputNodes.push_back(node3);
		}
		if (joboptions["fn_mov4"].getString() != "")
		{
			command += " " + joboptions["fn_mov4"].getString();
			Node node4(joboptions["fn_mov4"].getString(), joboptions["fn_mov4"].node_type);
			inputNodes.push_back(node4);
		}
		command += " \" ";

		// Check for duplicates
		command += " --check_duplicates rlnMicrographMovieName ";
		command += " --o " + outputname + "join_movies.star";
		Node node5(outputname + "join_movies.star", joboptions["fn_mov1"].node_type);
		outputNodes.push_back(node5);
	}

	// Other arguments
	command += " " + joboptions["other_args"].getString();

	commands.push_back(command);

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

