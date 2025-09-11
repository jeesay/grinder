void RelionJob::initialiseModelAngeloJob()
{
	hidden_name = ".gui_modelangelo";

	joboptions["fn_map"] = JobOption("B-factor sharpened map:", LABEL_MAP_CPIPE, 1, "", "MRC map files (*.mrc)",  "Provide a (RELION-postprocessed) B-factor sharpened map for model building");
	joboptions["p_seq"] = JobOption("FASTA sequence for proteins:", LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})",  "Provide a FASTA file with sequences for all protein chains to be built in the map. You can leave this empty if you don't know the proteins that are there, and then run a HMMer search to identify the unknown proteins. ModelAngelo will build much better models when provided with a FASTA sequence file!");
	joboptions["d_seq"] = JobOption("FASTA sequence for DNA:", LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})",  "Provide a FASTA file with sequences for all DNA chains to be built in the map.");
	joboptions["r_seq"] = JobOption("FASTA sequence for RNA:", LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})",  "Provide a FASTA file with sequences for all RNA chains to be built in the map.");
	joboptions["fn_modelangelo_exe"] = JobOption("ModelAngelo executable:", std::string("relion_python_modelangelo"), "The modelangelo executable. By default, the relion_python_modelangelo will be used, which was installed inside conda with a typical relion install. Only change this if that version is giving you problems.");
	joboptions["gpu_id"] = JobOption("Which GPUs to use:", std::string("0"), "Provide a number for the GPU to be used (e.g. 0, 1 etc). Use comma-separated values to use multiple GPUs, e.g. 0,1,2");

	joboptions["do_hhmer"] = JobOption("Perform HMMer search?", false ,"If set to Yes, model-angelo will perform a HMM search using HHMer in the output directory of the model-angelo run (without sequence). You can continue an old run with this option switched on, and the model building step will be skipped if the output .cif exists. This way, you can try multiple HHMer runs.");
	joboptions["fn_lib"] = JobOption("Library with sequences for HMMer search:", LABEL_SEQUENCE_CPIPE, 1, "", "FASTA sequence files (*.{fasta,txt})", "FASTA file with library with all sequences for HMMer search. This is often an entire proteome.");
	joboptions["alphabet"] = JobOption("Alphabet for the HMMer search:", job_modelangelo_alphabet_options, 0, "Type of Alphabet for HMM searches.");
	joboptions["F1"] = JobOption("HMMSearch F1: ", 0.02, 1., 10., 0.1, "F1 parameter for HMMSearch, see their documentation at http://eddylab.org/software/hmmer/Userguide.pdf");
	joboptions["F2"] = JobOption("HMMSearch F2: ", 0.001, 1., 10., 0.1, "F2 parameter for HMMSearch, see their documentation at http://eddylab.org/software/hmmer/Userguide.pdf");
	joboptions["F3"] = JobOption("HMMSearch F3: ", 0.00001, 0., 10., 0.1, "F3 parameter for HMMSearch, see their documentation at http://eddylab.org/software/hmmer/Userguide.pdf");
	joboptions["E"] = JobOption("HMMSearch E: ", 10, 0., 100., 10, "E parameter for HMMSearch, see their documentation at http://eddylab.org/software/hmmer/Userguide.pdf");
}


bool RelionJob::getCommandsModelAngeloJob(std::string &outputname, std::vector<std::string> &commands,
		       std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);

	FileName outputmodel = outputname;
	outputmodel = (outputmodel.afterFirstOf("/")).beforeLastOf("/");
	outputmodel = outputname + outputmodel + ".cif";

	// Only run model building for new job or if output.cif is not there yet.
	if (!is_continue || !exists(outputmodel) )
	{
		// Run on a map
		Node node(joboptions["fn_map"].getString(), joboptions["fn_map"].node_type);
		inputNodes.push_back(node);

		std::string command = joboptions["fn_modelangelo_exe"].getString();
		if (joboptions["p_seq"].getString() != "" || joboptions["d_seq"].getString() != "" || joboptions["r_seq"].getString() != "" )
		{
			command += " build ";

			if (joboptions["p_seq"].getString() != "" )
			{
				// Run with a protein sequence file
				Node node2(joboptions["p_seq"].getString(), joboptions["p_seq"].node_type);
				inputNodes.push_back(node2);

				command += " -pf " + joboptions["p_seq"].getString();
			}
			if (joboptions["d_seq"].getString() != "" )
			{
				// Run with a DNA sequence file
				Node node2(joboptions["d_seq"].getString(), joboptions["d_seq"].node_type);
				inputNodes.push_back(node2);

				command += " -df " + joboptions["d_seq"].getString();
			}
			if (joboptions["r_seq"].getString() != "" )
			{
				// Run with a protein sequence file
				Node node2(joboptions["r_seq"].getString(), joboptions["r_seq"].node_type);
				inputNodes.push_back(node2);

				command += " -rf " + joboptions["r_seq"].getString();
			}
		}
		else
		{
			command += " build_no_seq ";
		}

		command += " -v " + joboptions["fn_map"].getString();
		command += " -o " + outputname;
		command += " -d " + joboptions["gpu_id"].getString();

		Node node3(outputmodel, LABEL_ATOMCOORDS_CPIPE);
		outputNodes.push_back(node3);

		// Other arguments for model_angelo
		command += " " + joboptions["other_args"].getString();
		commands.push_back(command);
	}

	// If no sequence was provided, but a library was provided, then also run an HMM search
	if (joboptions["do_hhmer"].getBoolean())
	{
		if (joboptions["fn_lib"].getString() == "")
		{
			error_message = "ERROR: you need to provide a library to perform the HMM search against.";
			return false;
		}

		std::string command2 = joboptions["fn_modelangelo_exe"].getString();

		command2 += " hmm_search ";
		command2 += " -i " + outputname;
		command2 += " -f " + joboptions["fn_lib"].getString();
		command2 += " -o " + outputname;
		command2 += " -a " + joboptions["alphabet"].getString();

		//HMMSearch parameters
		command2 += " --F1 " + joboptions["F1"].getString();
		command2 += " --F2 " + joboptions["F2"].getString();
		command2 += " --F3 " + joboptions["F3"].getString();
		command2 += " --E " + joboptions["E"].getString();

		// Other arguments for model_angelo
		command2 += " " + joboptions["other_args"].getString();
		commands.push_back(command2);
	}

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message, true);
}

