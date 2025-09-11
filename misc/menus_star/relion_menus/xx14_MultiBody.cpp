void RelionJob::initialiseMultiBodyJob()
{
	type = PROC_MULTIBODY;

	hidden_name = ".gui_multibody";

	joboptions["fn_in"] = JobOption("Consensus refinement optimiser.star: ", std::string(""), "STAR Files (run_it*_optimiser.star)", "Refine3D/.", "Select the *_optimiser.star file for the iteration of the consensus refinement \
from which you want to start multi-body refinement.");

	joboptions["fn_cont"] = JobOption("Continue from here: ", std::string(""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR", "Select the *_optimiser.star file for the iteration \
from which you want to continue this multi-body refinement. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a '_ctX' to the output rootname, \
with X being the iteration from which one continues the previous run.");

	joboptions["fn_bodies"] = JobOption("Body STAR file:", std::string(""), "STAR Files (*.{star})", ".", " Provide the STAR file with all information about the bodies to be used in multi-body refinement. \
An example for a three-body refinement would look like this: \n\
\n\
data_\n\
loop_\n\
_rlnBodyMaskName\n\
_rlnBodyRotateRelativeTo\n\
_rlnBodySigmaAngles\n\
_rlnBodySigmaOffset\n\
large_body_mask.mrc 2 10 2\n\
small_body_mask.mrc 1 10 2\n\
head_body_mask.mrc 2 10 2\n\
\n\
Where each data line represents a different body, and: \n \
 - rlnBodyMaskName contains the name of a soft-edged mask with values in [0,1] that define the body; \n\
 - rlnBodyRotateRelativeTo defines relative to which other body this body rotates (first body is number 1); \n\
 - rlnBodySigmaAngles and _rlnBodySigmaOffset are the standard deviations (widths) of Gaussian priors on the consensus rotations and translations; \n\
\n \
Optionally, there can be a fifth column with _rlnBodyReferenceName. Entries can be 'None' (without the ''s) or the name of a MRC map with an initial reference for that body. In case the entry is None, the reference will be taken from the density in the consensus refinement.\n \n\
Also note that larger bodies should be above smaller bodies in the STAR file. For more information, see the multi-body paper.");

	joboptions["do_subtracted_bodies"] = JobOption("Reconstruct subtracted bodies?", true, "If set to Yes, then the reconstruction of each of the bodies will use the subtracted images. This may give \
useful insights about how well the subtraction worked. If set to No, the original particles are used for reconstruction (while the subtracted ones are still used for alignment). This will result in fuzzy densities for bodies outside the one used for refinement.");
	joboptions["do_blush"] = JobOption("Use Blush regularisation?", false, "If set to Yes, relion_refine will use a neural network to perform regularisation by denoising at every iteration, instead of the standard smoothness regularisation.");

	joboptions["sampling"] = JobOption("Initial angular sampling:", job_sampling_options, 4, "There are only a few discrete \
angular samplings possible because we use the HealPix library to generate the sampling of the first two Euler angles on the sphere. \
The samplings are approximate numbers and vary slightly over the sphere.\n\n \
Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.");
	joboptions["offset_range"] = JobOption("Initial offset range (pix):", 3, 0, 30, 1, "Probabilities will be calculated only for translations \
in a circle with this radius (in pixels). The center of this circle changes at every iteration and is placed at the optimal translation \
for each image in the previous iteration.\n\n \
Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.");
	joboptions["offset_step"] = JobOption("Initial offset step (pix):", 0.75, 0.1, 5, 0.1, "Translations will be sampled with this step-size (in pixels).\
Translational sampling is also done using the adaptive approach. \
Therefore, if adaptive=1, the translations will first be evaluated on a 2x coarser grid.\n\n \
Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.");


	joboptions["do_analyse"] = JobOption("Run flexibility analysis?", true, "If set to Yes, after the multi-body refinement has completed, a PCA analysis will be run on the orientations all all bodies in the data set. This can be set to No initially, and then the job can be continued afterwards to only perform this analysis.");
	joboptions["nr_movies"] = JobOption("Number of eigenvector movies:", 3, 0, 16, 1, "Series of ten output maps will be generated along this many eigenvectors. These maps can be opened as a 'Volume Series' in UCSF Chimera, and then displayed as a movie. They represent the principal motions in the particles.");
	joboptions["do_select"] = JobOption("Select particles based on eigenvalues?", false, "If set to Yes, a particles.star file is written out with all particles that have the below indicated eigenvalue in the selected range.");
	joboptions["select_eigenval"] = JobOption("Select on eigenvalue:", 1, 1, 20, 1, "This is the number of the eigenvalue to be used in the particle subset selection (start counting at 1).");
	joboptions["eigenval_min"] = JobOption("Minimum eigenvalue:", -999., -50, 50, 1, "This is the minimum value for the selected eigenvalue; only particles with the selected eigenvalue larger than this value will be included in the output particles.star file");
	joboptions["eigenval_max"] = JobOption("Maximum eigenvalue:", 999., -50, 50, 1, "This is the maximum value for the selected eigenvalue; only particles with the selected eigenvalue less than this value will be included in the output particles.star file");

	joboptions["do_parallel_discio"] = JobOption("Use parallel disc I/O?", true, "If set to Yes, all MPI followers will read their own images from disc. \
Otherwise, only the leader will read images and send them through the network to the followers. Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.");
	joboptions["nr_pool"] = JobOption("Number of pooled particles:", 3, 1, 16, 1, "Particles are processed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.");
	joboptions["do_pad1"] = JobOption("Skip padding?", false, "If set to Yes, the calculations will not use padding in Fourier space for better interpolation in the references. Otherwise, references are padded 2x before Fourier transforms are calculated. Skipping padding (i.e. use --pad 1) gives nearly as good results as using --pad 2, but some artifacts may appear in the corners from signal that is folded back.");
	joboptions["do_preread_images"] = JobOption("Pre-read all particles into RAM?", false, "If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. \
Because particles are read in float-precision, it will take ( N * box_size * box_size * 8 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. \
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
	joboptions["gpu_ids"] = JobOption("Which GPUs to use:", std::string(""), "This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','.  For example: '0,0:1,1:0,0:1,1'");
}

bool RelionJob::getCommandsMultiBodyJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;

	if (!exists(joboptions["fn_bodies"].getString()))
	{
		error_message = "ERROR: you have to specify an existing body STAR file.";
		return false;
	}

	if (is_continue && joboptions["fn_cont"].getString() == "" && !joboptions["do_analyse"].getBoolean())
	{
		error_message = "ERROR: either specify a optimiser file to continue multibody refinement from; OR run flexibility analysis...";
		return false;
	}

	FileName fn_run = "";
	if (!is_continue || (is_continue && joboptions["fn_cont"].getString() != ""))
	{

		if (joboptions["nr_mpi"].getNumber(error_message) > 1)
			command="`which relion_refine_mpi`";
		else
			command="`which relion_refine`";
		if (error_message != "") return false;

		MetaDataTable MD;
		MD.read(joboptions["fn_bodies"].getString());
		int nr_bodies = MD.numberOfObjects();

		if (is_continue)
		{
			int pos_it = joboptions["fn_cont"].getString().rfind("_it");
			int pos_op = joboptions["fn_cont"].getString().rfind("_optimiser");
			if (pos_it < 0 || pos_op < 0)
				std::cerr << "Warning: invalid optimiser.star filename provided for continuation run: " << joboptions["fn_cont"].getString() << std::endl;
			int it = (int)textToFloat((joboptions["fn_cont"].getString().substr(pos_it+3, 6)).c_str());
			fn_run = "run_ct" + floatToString(it);
			command += " --continue " + joboptions["fn_cont"].getString();
			command += " --o " + outputname + fn_run;
			outputNodes = getOutputNodesRefine(outputname + fn_run, "MultiBody", -1, 1, 3, nr_bodies, is_tomo);

		}
		else
		{
			fn_run = "run";
			command += " --continue " + joboptions["fn_in"].getString();
			command += " --o " + outputname + fn_run;
			outputNodes = getOutputNodesRefine(outputname + "run", "MultiBody", -1, 1, 3, nr_bodies, is_tomo);
			command += " --solvent_correct_fsc --multibody_masks " + joboptions["fn_bodies"].getString();

			Node node(joboptions["fn_in"].getString(), LABEL_REFINE3D_OPT);
			inputNodes.push_back(node);

			// Sampling
			int iover = 1;
			command += " --oversampling " + floatToString((float)iover);
			int sampling = JobOption::getHealPixOrder(joboptions["sampling"].getString());
			if (sampling <= 0)
			{
				error_message = "Wrong choice for sampling";
				return false;
			}
			// The sampling given in the GUI will be the oversampled one!
			command += " --healpix_order " + integerToString(sampling - iover);
			// Always perform local searches!
			command += " --auto_local_healpix_order " + integerToString(sampling - iover);

			// Offset range
			command += " --offset_range " + joboptions["offset_range"].getString();
			// The sampling given in the GUI will be the oversampled one!
			command += " --offset_step " + floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover));
			if (error_message != "") return false;
		}

        if (joboptions["do_blush"].getBoolean())
            command += " --blush ";

		if (joboptions["do_subtracted_bodies"].getBoolean())
			command += " --reconstruct_subtracted_bodies ";

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
		if (joboptions["do_pad1"].getBoolean())
			command += " --pad 1 ";
		else
			command += " --pad 2 ";

		// Running stuff
		command += " --j " + joboptions["nr_threads"].getString();

		// GPU-stuff
		if (joboptions["use_gpu"].getBoolean())
		{
			command += " --gpu \"" + joboptions["gpu_ids"].getString() + "\"";
		}

		// Other arguments
		command += " " + joboptions["other_args"].getString();

		commands.push_back(command);
	} // end if (!is_continue || (is_continue && joboptions["fn_cont"].getString() != ""))

	if (joboptions["do_analyse"].getBoolean())
	{
		command = "`which relion_flex_analyse`";

		// If we had performed relion_refine command, then fn_run would be set now
		// Otherwise, we have to search for _model.star files that do NOT have a _it??? specifier
		if (fn_run == "")
		{
			FileName fn_wildcard = outputname + "run*_model.star";
			std::vector<FileName> fns_model;
			std::vector<FileName> fns_ok;
			fn_wildcard.globFiles(fns_model);
			for (int i = 0; i < fns_model.size(); i++)
			{
				if (!fns_model[i].contains("_it"))
					fns_ok.push_back(fns_model[i]);
			}
			if (fns_ok.size() == 0)
			{
				error_message = "ERROR: cannot find appropriate model.star file in the output directory";
				return false;
			}
			if (fns_ok.size() > 1)
			{
				error_message = "ERROR: there are more than one model.star files (without '_it' specifiers) in the output directory. Move all but one out of the way.";
				return false;
			}
			fn_run = fns_ok[0].beforeFirstOf("_model.star");
		}
		else
			fn_run = outputname + fn_run;

		// General I/O
		command += " --PCA_orient ";
		command += " --model " + fn_run + "_model.star";
		command += " --data " + fn_run + "_data.star";
		command += " --bodies " + joboptions["fn_bodies"].getString();
		command += " --o " + outputname + "analyse";

		// Eigenvector movie maps
		if (joboptions["nr_movies"].getNumber(error_message) > 0)
		{
			command += " --do_maps ";
			command += " --k " + joboptions["nr_movies"].getString();
		}
		if (error_message != "") return false;

		// Selection
		if (joboptions["do_select"].getBoolean())
		{
			float minval = joboptions["eigenval_min"].getNumber(error_message);
			if (error_message != "") return false;

			float maxval = joboptions["eigenval_max"].getNumber(error_message);
			if (error_message != "") return false;

			if ( minval >= maxval)
			{
				error_message = "ERROR: the maximum eigenvalue should be larger than the minimum one!";
				return false;
			}

			command += " --select_eigenvalue " + joboptions["select_eigenval"].getString();
			command += " --select_eigenvalue_min " + joboptions["eigenval_min"].getString();
			command += " --select_eigenvalue_max " + joboptions["eigenval_max"].getString();

			// Add output node: selected particles star file
			FileName fnt = outputname + "analyse_eval"+integerToString(joboptions["select_eigenval"].getNumber(error_message),3)+"_select";
			if (error_message != "") return false;

			int min = ROUND(joboptions["eigenval_min"].getNumber(error_message));
			if (error_message != "") return false;

			int max = ROUND(joboptions["eigenval_max"].getNumber(error_message));
			if (error_message != "") return false;

			if (min > -99998)
				fnt += "_min"+integerToString(min);
			if (max < 99998)
				fnt += "_max"+integerToString(max);
			fnt += ".star";
			Node node2(fnt, LABEL_MULTIBODY_SEL_PARTS);
			outputNodes.push_back(node2);

		}

		// PDF with histograms of the eigenvalues
		Node node3(outputname + "analyse_logfile.pdf", LABEL_MULTIBODY_FLEXLOG);
		outputNodes.push_back(node3);

		commands.push_back(command);
	}

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

