void RelionJob::initialiseDynaMightJob()
{
	hidden_name = ".gui_dynamight";

	joboptions["fn_star"] = JobOption("Input images STAR file:", LABEL_PARTS_CPIPE, 1, "", "STAR files (*.star) \t Image stacks (not recommended, read help!) (*.{spi,mrcs})", "A STAR file with all images (and their metadata).");
	joboptions["fn_map"] = JobOption("Consensus map:", LABEL_MAP_CPIPE, 1, "", "Image Files (*.{spi,vol,mrc})", "A 3D map in MRC/Spider format. Make sure this map has the same dimensions and the same pixel size as your input images.");
	//joboptions["fn_mask"] = JobOption("Mask (optional):", LABEL_MASK_CPIPE, "", "Image Files (*.{spi,vol,msk,mrc})", "Provide a mask to limit deformations to a specific region of the consensus structure. Regions outside the mask will be kept fized and will not be visualised.");
	joboptions["gpu_id"] = JobOption("Which (single) GPU to use:", std::string("0"), "Note that DynaMight can only use one GPU at a time. Data sets with many particles or large box sizes will require powerful GPUs, like an A100.");
	joboptions["do_preload"] = JobOption("Preload images in RAM?", false, "If set to Yes, dynamight will preload images into memory for learning the forward or inverse deformations and for deformed backprojection. This will speed up the calculations, but you need to make sure you have enough RAM to do so.");
	joboptions["fn_dynamight_exe"] = JobOption("DynaMight executable:", std::string("relion_python_dynamight"), "The DynaMight executable. By default, the relion_python_dynamight will be used, which was installed inside conda with a typical relion install. Only change this if that version is giving you problems.");

	joboptions["nr_gaussians"] = JobOption("Number of Gaussians: ", 10000, 5000, 40000, 1000, "Number of Gaussians to describe the consensus map with. Larger structures that one wishes to describe at higher resolutions will need more Gaussians. As a rule of thumb, you could try and use 1-2 Gaussians per amino acid or nucleotide in your complex. But note that running DynaMight with more than 30,000 Gaussians may be problematic on GPUs with a memory of 24 GB.");
	joboptions["initial_threshold"] = JobOption("Initial map threshold (optional): ",std::string("") , "If provided, this threshold will be used to position initial Gaussians in the consensus map. If left empty, an automated procedure will be used to estimate the appropriate threshold.");
	joboptions["reg_factor"] = JobOption("Regularization factor: ", 1, 0.2, 5, 0.1, "This regularization factor defines the relative weights between the data over the restraints. Values higher than one will put more weights on the restraints.");

	joboptions["fn_checkpoint"] = JobOption("Checkpoint file:", std::string(""), "Checkpoint files (*.pth)", "CURRENT_ODIR/forward_deformations/checkpoints", "Select the checkpoint file to use for visualization, inverse deformation estimation or deformed backprojection. If left empty, the last available checkpoint file will be used");

	joboptions["do_visualize"] = JobOption("Do visualization?", false, "If set to Yes, dynamight will be run to visualize the latent space and deformed models. One can also save series of maps to make movies in Chimera, or STAR files of particle subsets within this task.");
	joboptions["halfset"] = JobOption("Half-set to visualize: ", 1, 0, 2, 1, "Select halfset 1 or 2 to explore the latent space of that halfset. If you select halfset 0, then the validation set is being visualised, which will give you an estimate of the errors in the deformations.");

	joboptions["do_inverse"] = JobOption("Do inverse-deformation estimation?", false, "If set to Yes, dynamight will be run to estimate inverse-deformations. These are necessary if one want to perform deformed backprojection to calculate an improved consensus model.");
	joboptions["nr_epochs"] = JobOption("Number of epochs to perform: ", 200, 50, 500, 10, "Number of epochs to perform inverse deformations. You can monitor the convergence of the loss function to assess how many are necessary. Often 200 are enough");
	joboptions["do_store_deform"] = JobOption("Store deformations in RAM?", false, "If set to Yes, dynamight will store deformations in the GPU memory, which will speed up the calculations, but you need to have enough GPU memory to do this...");

	joboptions["do_reconstruct"] = JobOption("Do deformed backprojection?", false, "If set to Yes, dynamight will be run to perform a deformed backprojection, using inverse-deformations from a previous task, to get an improved consensus reconstruction.");
	joboptions["backproject_batchsize"] = JobOption("Backprojection batchsize: ", 10, 1, 500, 10, "Number of images to process in parallel. This will speed up the calculation, but will cost GPU memory. Try how high you can go on your GPU, given your box size and size of the neural network.");
}

bool RelionJob::getCommandsDynaMightJob(std::string &outputname, std::vector<std::string> &commands,
                                       std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;

	command = joboptions["fn_dynamight_exe"].getString();

	if (!is_continue)
	{
		// New jobs need to add the input nodes

		Node node(joboptions["fn_star"].getString(), joboptions["fn_star"].node_type);
		inputNodes.push_back(node);
		Node node2(joboptions["fn_map"].getString(), joboptions["fn_map"].node_type);
		inputNodes.push_back(node2);
		/*
		if (joboptions["fn_mask"].getString() != "")
		{
			Node node3(joboptions["fn_mask"].getString(), joboptions["fn_mask"].node_type);
			inputNodes.push_back(node3);
		}
		*/
	}
	else
	{
		int c = 0;
		if (joboptions["do_visualize"].getBoolean()) c++;
		if (joboptions["do_inverse"].getBoolean()) c++;
		if (joboptions["do_reconstruct"].getBoolean()) c++;
		if (c == 0)
		{
			error_message = "You need to select at least one task on one of the tabs...";
			return false;
		}
		if (c > 1)
		{
			error_message = "You can not perform more than one task simultaneously...";
			return false;
		}
	}

	if (!is_continue || !(joboptions["do_visualize"].getBoolean() || joboptions["do_inverse"].getBoolean() || joboptions["do_reconstruct"].getBoolean()) )
	{
		command += " optimize-deformations ";
		command += " --refinement-star-file " + joboptions["fn_star"].getString();
		command += " --output-directory " + outputname;
		command += " --initial-model " + joboptions["fn_map"].getString();
		command += " --n-gaussians " + joboptions["nr_gaussians"].getString();
		if (joboptions["initial_threshold"].getString() != "")
		command += " --initial-threshold " + joboptions["initial_threshold"].getString();
		command += " --regularization-factor "  + joboptions["reg_factor"].getString();
		command += " --n-threads " + joboptions["nr_threads"].getString();

		if (joboptions["do_preload"].getBoolean())
			command += " --preload-images ";

		//if (joboptions["fn_mask"].getString() != "")
		//    command += " --mask-file " + joboptions["fn_mask"].getString();

	}
	else if (joboptions["do_visualize"].getBoolean())
	{

		command += " explore-latent-space " + outputname;
		command += " --half-set " + joboptions["halfset"].getString();

		if (joboptions["fn_checkpoint"].getString() != "")
			command += " --checkpoint-file " + joboptions["fn_checkpoint"].getString();

		//if (joboptions["fn_mask"].getString() != "")
		//    command += " --mask-file " + joboptions["fn_mask"].getString();
	}
	else if (joboptions["do_inverse"].getBoolean())
	{
		command += " optimize-inverse-deformations " + outputname;
		command += " --n-epochs " + joboptions["nr_epochs"].getString();

		if (joboptions["fn_checkpoint"].getString() != "")
			command += " --checkpoint-file " + joboptions["fn_checkpoint"].getString();

		if (joboptions["do_store_deform"].getBoolean())
			command += " --save-deformations ";

		if (joboptions["do_preload"].getBoolean())
			command += " --preload-images";
	}
	else if (joboptions["do_reconstruct"].getBoolean())
	{
		command += " deformable-backprojection " + outputname;
		command += " --batch-size " + joboptions["backproject_batchsize"].getString();

		if (joboptions["fn_checkpoint"].getString() != "")
			command += " --checkpoint-file " + joboptions["fn_checkpoint"].getString();

		if (joboptions["do_preload"].getBoolean())
			command += " --preload-images";

		//if (joboptions["fn_mask"].getString() != "")
		//    command += " --mask-file " + joboptions["fn_mask"].getString();

		Node onode(outputname + "backprojection/map_half1.mrc", LABEL_DYNAMIGHT_HALFMAP);
		outputNodes.push_back(onode);
		Node onode2(outputname + "backprojection/map_half2.mrc", LABEL_DYNAMIGHT_HALFMAP);
		outputNodes.push_back(onode2);

	}

	if (joboptions["gpu_id"].getString() != "")
		command += " --gpu-id " + joboptions["gpu_id"].getString();

	// Other arguments for model_angelo
	command += " " + joboptions["other_args"].getString();
	commands.push_back(command);

	// Besides

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message, true);
}


