void RelionJob::initialiseInimodelJob()
{
	hidden_name = ".gui_inimodel";

	if (is_tomo)
	{
        addTomoInputOptions(true, true, true, false);
	}
    else
    {
        joboptions["fn_img"] = JobOption("Input images STAR file:", LABEL_PARTS_CPIPE, 1, "", "STAR files (*.star) \t Image stacks (not recommended, read help!) (*.{spi,mrcs})", "A STAR file with all images (and their metadata). \
In Gradient optimisation, it is very important that there are particles from enough different orientations. One only needs a few thousand to 10k particles. When selecting good 2D classes in the Subset Selection jobtype, use the option to select a maximum number of particles from each class to generate more even angular distributions for SGD.\
\n \n Alternatively, you may give a Spider/MRC stack of 2D images, but in that case NO metadata can be included and thus NO CTF correction can be performed, \
nor will it be possible to perform noise spectra estimation or intensity scale corrections in image groups. Therefore, running RELION with an input stack will in general provide sub-optimal results and is therefore not recommended!! Use the Preprocessing procedure to get the input STAR file in a semi-automated manner. Read the RELION wiki for more information.");
    }
	joboptions["fn_cont"] = JobOption("Continue from here: ", std::string(""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR", "Select the *_optimiser.star file for the iteration \
from which you want to continue a previous run. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a '_ctX' to the output rootname, \
with X being the iteration from which one continues the previous run.");

	joboptions["nr_iter"] = JobOption("Number of VDAM mini-batches:", 200, 50, 500, 10, "How many iterations (i.e. mini-batches) to perform with the VDAM algorithm?");
	joboptions["tau_fudge"] = JobOption("Regularisation parameter T:", 4 , 0.1, 10, 0.1, "Bayes law strictly determines the relative weight between \
the contribution of the experimental data and the prior. However, in practice one may need to adjust this weight to put slightly more weight on \
the experimental data to allow optimal results. Values greater than 1 for this regularisation parameter (T in the JMB2011 paper) put more \
weight on the experimental data. Values around 2-4 have been observed to be useful for 3D initial model calculations");

	joboptions["nr_classes"] = JobOption("Number of classes:", 1, 1, 50, 1, "The number of classes (K) for a multi-reference ab initio SGD refinement. \
These classes will be made in an unsupervised manner, starting from a single reference in the initial iterations of the SGD, and the references will become increasingly dissimilar during the inbetween iterations.");
	joboptions["sym_name"] = JobOption("Symmetry:", std::string("C1"), "The initial model is always generated in C1 and then aligned to and symmetrized with the specified point group. If the automatic alignment fails, please manually rotate run_itNNN_class001.mrc (NNN is the number of iterations) so that it conforms the symmetry convention.");
	joboptions["do_run_C1"] = JobOption("Run in C1 and apply symmetry later? ", true, "If set to Yes, the gradient-driven optimisation is run in C1 and the symmetry orientation is searched and applied later. If set to No, the entire optimisation is run in the symmetry point group indicated above.");
	joboptions["particle_diameter"] = JobOption("Mask diameter (A):", 200, 0, 1000, 10, "The experimental images will be masked with a soft \
circular mask with this diameter. Make sure this radius is not set too small because that may mask away part of the signal! \
If set to a value larger than the image size no masking will be performed.\n\n\
The same diameter will also be used for a spherical mask of the reference structures if no user-provided mask is specified.");
	joboptions["do_solvent"] = JobOption("Flatten and enforce non-negative solvent?", true, "If set to Yes, the job will apply a spherical mask and enforce all values in the reference to be non-negative.");

    if (is_tomo)
        joboptions["sigma_tilt"] = JobOption("Prior width on tilt angle (deg):", -1, -1, 30, 1, "The width of the prior on the tilt angle: angular searches will be +/-3 times this value. Tilt priors will be defined when particles have been picked as filaments, on spheres or on manifolds. Setting this width to a negative value will lead to no prior being used on the tilt angle.");

	joboptions["do_ctf_correction"] = JobOption("Do CTF-correction?", true, "If set to Yes, CTFs will be corrected inside the MAP refinement. \
The resulting algorithm intrinsically implements the optimal linear, or Wiener filter. \
Note that CTF parameters for all images need to be given in the input STAR file. \
The command 'relion_refine --print_metadata_labels' will print a list of all possible metadata labels for that STAR file. \
See the RELION Wiki for more details.\n\n Also make sure that the correct pixel size (in Angstrom) is given above!)");
	joboptions["ctf_intact_first_peak"] = JobOption("Ignore CTFs until first peak?", false, "If set to Yes, then CTF-amplitude correction will \
only be performed from the first peak of each CTF onward. This can be useful if the CTF model is inadequate at the lowest resolution. \
Still, in general using higher amplitude contrast on the CTFs (e.g. 10-20%) often yields better results. \
Therefore, this option is not generally recommended: try increasing amplitude contrast (in your input STAR file) first!");

	joboptions["do_parallel_discio"] = JobOption("Use parallel disc I/O?", true, "If set to Yes, all MPI followers will read their own images from disc. \
Otherwise, only the leader will read images and send them through the network to the followers. Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.");
	joboptions["nr_pool"] = JobOption("Number of pooled particles:", 3, 1, 16, 1, "Particles are processed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.");
	joboptions["do_preread_images"] = JobOption("Pre-read all particles into RAM?", false, "If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. \
Because particles are read in float-precision, it will take ( N * box_size * box_size * 4 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. \
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM. \n \n If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.");
	const char *default_scratch = getenv("RELION_SCRATCH_DIR");
	if (default_scratch == NULL)
	{
		default_scratch = DEFAULTSCRATCHDIR;
	}
	joboptions["scratch_dir"] = JobOption("Copy particles to scratch directory:", std::string(default_scratch), "If a directory is provided here, then the job will create a sub-directory in it called relion_volatile. If that relion_volatile directory already exists, it will be wiped. Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory. \
Provided this directory is on a fast local drive (e.g. an SSD drive), processing in all the iterations will be faster. If the job finishes correctly, the relion_volatile directory will be wiped. If the job crashes, you may want to remove it yourself.");
	joboptions["do_combine_thru_disc"] = JobOption("Combine iterations through disc?", false, "If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results. The MPI leader will read in all these files, combine them all, and write out a new file with the combined results. \
All MPI salves will then read in the combined results. This reduces heavy load on the network, but increases load on the disc I/O. \
This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step. It will depend on your system setup which is most efficient.");

	joboptions["use_gpu"] = JobOption("Use GPU acceleration?", false, "If set to Yes, the job will try to use GPU acceleration.");
	joboptions["gpu_ids"] = JobOption("Which GPUs to use:", std::string(""), "This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','. For example: '0,0:1,1:0,0:1,1'");
}

bool RelionJob::getCommandsInimodelJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();

	initialisePipeline(outputname, job_counter);

	if (joboptions["nr_mpi"].getNumber(error_message) > 1)
	{
		error_message = "Gradient refinement is not supported together with MPI.";
		return false;
	}
	if (error_message != "") return false;

	std::string command;
	command="`which relion_refine`";

	FileName fn_sym = joboptions["sym_name"].getString();

	FileName fn_run = "run";
	if (is_continue)
	{
		if (joboptions["fn_cont"].getString() == "")
		{
			error_message = "ERROR: empty field for continuation STAR file...";
			return false;
		}
		int pos_it = joboptions["fn_cont"].getString().rfind("_it");
		int pos_op = joboptions["fn_cont"].getString().rfind("_optimiser");
		if (pos_it < 0 || pos_op < 0)
			std::cerr << "Warning: invalid optimiser.star filename provided for continuation run: " << joboptions["fn_cont"].getString() << std::endl;
		// SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
		//int it = (int)textToFloat((joboptions["fn_cont"].getString().substr(pos_it+3, 6)).c_str());
		//fn_run += "_ct" + floatToString(it);
		command += " --continue " + joboptions["fn_cont"].getString();

	}

	command += " --o " + outputname + fn_run;
	command += " --iter " + joboptions["nr_iter"].getString();

	if (is_tomo) label += ".tomo";

	int total_nr_iter = joboptions["nr_iter"].getNumber(error_message);
	if (error_message != "") return false;
	int nr_classes = joboptions["nr_classes"].getNumber(error_message);
	if (error_message != "") return false;

	if (!is_continue)
	{
		command += " --grad --denovo_3dref ";

		if (is_tomo)
        {
            error_message = getTomoInputCommmand(true, command, HAS_COMPULSORY, HAS_COMPULSORY, HAS_NOT, HAS_NOT);
            if (error_message != "") return false;

            Node node1( outputname + fn_run + "_optimisation_set.star", LABEL_INIMOD_OPTSET);
            outputNodes.push_back(node1);

            float sigma = joboptions["sigma_tilt"].getNumber(error_message);
            if (error_message != "") return false;
            if (sigma > 0.)
            {
                command += " --sigma_tilt " + joboptions["sigma_tilt"].getString();
            }

        }
        else
        {
            if (joboptions["fn_img"].getString() == "")
            {
                error_message = "ERROR: empty field for input STAR file...";
                return false;
            }
            else
            {
                command += " --i " + joboptions["fn_img"].getString();
                Node node(joboptions["fn_img"].getString(), joboptions["fn_img"].node_type);
                inputNodes.push_back(node);
            }
        }

		// CTF stuff
		if (joboptions["do_ctf_correction"].getBoolean())
		{
			command += " --ctf";
			if (joboptions["ctf_intact_first_peak"].getBoolean())
				command += " --ctf_intact_first_peak";
		}

		command += " --K " + joboptions["nr_classes"].getString();
		if (joboptions["do_run_C1"].getBoolean())
		{
			command += " --sym C1 ";
		}
		else
		{
			command += " --sym " + fn_sym;
		}

		if (joboptions["do_solvent"].getBoolean())
			command += " --flatten_solvent ";
		command += " --zero_mask ";
	}

	// Always do compute stuff
	if (!joboptions["do_combine_thru_disc"].getBoolean())
		command += " --dont_combine_weights_via_disc";
	if (!joboptions["do_parallel_discio"].getBoolean())
		command += " --no_parallel_disc_io";
	if (joboptions["do_preread_images"].getBoolean())
		command += " --preread_images " ;
	else if (joboptions["scratch_dir"].getString() != "")
	command += " --scratch_dir " +  joboptions["scratch_dir"].getString();
	command += " --pool " + joboptions["nr_pool"].getString();
	command += " --pad 1 ";

	// Optimisation
	command += " --particle_diameter " + joboptions["particle_diameter"].getString();
	command += " --oversampling 1  --healpix_order 1  --offset_range 6  --offset_step 2 --auto_sampling ";
	command += " --tau2_fudge " + joboptions["tau_fudge"].getString();

	// Running stuff
	command += " --j " + joboptions["nr_threads"].getString();

	// GPU-stuff
	if (joboptions["use_gpu"].getBoolean())
	{
		command += " --gpu \"" + joboptions["gpu_ids"].getString() +"\"";
	}

	// Other arguments
	command += " " + joboptions["other_args"].getString();

	commands.push_back(command);

	// Quickly remove RELION_JOB_EXIT_SUCCESS
	std::string command0 = "rm -f " + outputname + RELION_JOB_EXIT_SUCCESS;
	commands.push_back(command0);


	FileName fn_model;
	fn_model.compose(outputname + fn_run + "_it", total_nr_iter,"",3);
	fn_model+="_model.star";

	// Align with symmetry axes and apply symmetry
	std::string command2 = "`which relion_align_symmetry`";
	command2 += " --i " + fn_model;
	command2 += " --o " + outputname + "initial_model.mrc";

	if ( joboptions["do_run_C1"].getBoolean() && !(fn_sym == "C1" || fn_sym == "c1") )
	{
		command2 += " --sym " + joboptions["sym_name"].getString();
	}
	else
	{
		command2 += " --sym C1 ";
	}
	command2 += " --apply_sym --select_largest_class ";
	commands.push_back(command2);

	// And re-introduce RELION_JOB_EXIT_SUCCESS
	std::string commandF = "touch " + outputname + RELION_JOB_EXIT_SUCCESS;
	commands.push_back(commandF);

	// Output nodes
	Node node2(outputname + "initial_model.mrc", LABEL_INIMOD_MAP);
    outputNodes.push_back(node2);

	// If doing more than 1 class, make them all available (one of them will be the same as initial_model.mrc)
	if (nr_classes > 1)
	{
		for (int iclass = 0; iclass < nr_classes; iclass++)
		{
			FileName fn_tmp;
			fn_tmp.compose(outputname + fn_run + "_it", total_nr_iter, "", 3);
			fn_tmp.compose(fn_tmp + "_class", iclass+1, "mrc", 3);
			Node node3(fn_tmp, LABEL_INIMOD_MAP);
			outputNodes.push_back(node3);
		}
	}

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

