void RelionJob::initialiseClass2DJob()
{
	hidden_name = ".gui_class2d";

	joboptions["fn_img"] = JobOption("Input images STAR file:", LABEL_PARTS_CPIPE, 1, "", "STAR files (*.star) \t Image stacks (not recommended, read help!) (*.{spi,mrcs})", "A STAR file with all images (and their metadata). \n \n Alternatively, you may give a Spider/MRC stack of 2D images, but in that case NO metadata can be included and thus NO CTF correction can be performed, \
nor will it be possible to perform noise spectra estimation or intensity scale corrections in image groups. Therefore, running RELION with an input stack will in general provide sub-optimal results and is therefore not recommended!! Use the Preprocessing procedure to get the input STAR file in a semi-automated manner. Read the RELION wiki for more information.");
	joboptions["fn_cont"] = JobOption("Continue from here: ", std::string(""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR",  "Select the *_optimiser.star file for the iteration \
from which you want to continue a previous run. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a '_ctX' to the output rootname, \
with X being the iteration from which one continues the previous run.");

	joboptions["do_ctf_correction"] = JobOption("Do CTF-correction?", true, "If set to Yes, CTFs will be corrected inside the MAP refinement. \
The resulting algorithm intrinsically implements the optimal linear, or Wiener filter. \
Note that CTF parameters for all images need to be given in the input STAR file. \
The command 'relion_refine --print_metadata_labels' will print a list of all possible metadata labels for that STAR file. \
See the RELION Wiki for more details.\n\n Also make sure that the correct pixel size (in Angstrom) is given above!)");
	joboptions["ctf_intact_first_peak"] = JobOption("Ignore CTFs until first peak?", false, "If set to Yes, then CTF-amplitude correction will \
only be performed from the first peak of each CTF onward. This can be useful if the CTF model is inadequate at the lowest resolution. \
Still, in general using higher amplitude contrast on the CTFs (e.g. 10-20%) often yields better results. \
Therefore, this option is not generally recommended: try increasing amplitude contrast (in your input STAR file) first!");

	joboptions["nr_classes"] = JobOption("Number of classes:", 1, 1, 50, 1, "The number of classes (K) for a multi-reference refinement. \
These classes will be made in an unsupervised manner from a single reference by division of the data into random subsets during the first iteration.");
	joboptions["tau_fudge"] = JobOption("Regularisation parameter T:", 2 , 0.1, 10, 0.1, "Bayes law strictly determines the relative weight between \
the contribution of the experimental data and the prior. However, in practice one may need to adjust this weight to put slightly more weight on \
the experimental data to allow optimal results. Values greater than 1 for this regularisation parameter (T in the JMB2011 paper) put more \
weight on the experimental data. Values around 2-4 have been observed to be useful for 3D refinements, values of 1-2 for 2D refinements. \
Too small values yield too-low resolution structures; too high values result in over-estimated resolutions, mostly notable by the apparition of high-frequency noise in the references.");


	joboptions["do_em"] = JobOption("Use EM algorithm?", false, "If set to Yes, the slower expectation-maximization algorithm will be used. This was the default option in releases prior to 4.0-beta. If set to No, then one needs to use the (faster) VDAM (variable metric gradient descent with adaptive moments) algorithm below. will be used.");
	joboptions["nr_iter_em"] = JobOption("Number of EM iterations:", 25, 1, 50, 1, "Number of EM iterations to be performed. \
Note that the current implementation of 2D class averaging and 3D classification does NOT comprise a convergence criterium. \
Therefore, the calculations will need to be stopped by the user if further iterations do not yield improvements in resolution or classes. \n\n \
Also note that upon restarting, the iteration number continues to be increased, starting from the final iteration in the previous run. \
The number given here is the TOTAL number of iterations. For example, if 10 iterations have been performed previously and one restarts to perform \
an additional 5 iterations (for example with a finer angular sampling), then the number given here should be 10+5=15.");


	joboptions["do_grad"] = JobOption("Use VDAM algorithm?", true, "If set to Yes, the faster VDAM algorithm will be used. This algorithm was introduced with relion-4.0. If set to No, then the slower EM algorithm needs to be used.");
	joboptions["nr_iter_grad"] = JobOption("Number of VDAM mini-batches:", 200, 50, 500, 10, "Number of mini-batches to be processed using the VDAM algorithm. Using 200 has given good results for many data sets. Using 100 will run faster, at the expense of some quality in the results.");

	joboptions["particle_diameter"] = JobOption("Mask diameter (A):", 200, 0, 1000, 10, "The experimental images will be masked with a soft \
circular mask with this diameter. Make sure this radius is not set too small because that may mask away part of the signal! \
If set to a value larger than the image size no masking will be performed.\n\n\
The same diameter will also be used for a spherical mask of the reference structures if no user-provided mask is specified.");
	joboptions["do_zero_mask"] = JobOption("Mask individual particles with zeros?", true, "If set to Yes, then in the individual particles, \
the area outside a circle with the radius of the particle will be set to zeros prior to taking the Fourier transform. \
This will remove noise and therefore increase sensitivity in the alignment and classification. However, it will also introduce correlations \
between the Fourier components that are not modelled. When set to No, then the solvent area is filled with random noise, which prevents introducing correlations.\
High-resolution refinements (e.g. ribosomes or other large complexes in 3D auto-refine) tend to work better when filling the solvent area with random noise (i.e. setting this option to No), refinements of smaller complexes and most classifications go better when using zeros (i.e. setting this option to Yes).");
	joboptions["highres_limit"] = JobOption("Limit resolution E-step to (A): ", -1, -1, 20, 1, "If set to a positive number, then the expectation step (i.e. the alignment) will be done only including the Fourier components up to this resolution (in Angstroms). \
This is useful to prevent overfitting, as the classification runs in RELION are not to be guaranteed to be 100% overfitting-free (unlike the 3D auto-refine with its gold-standard FSC). In particular for very difficult data sets, e.g. of very small or featureless particles, this has been shown to give much better class averages. \
In such cases, values in the range of 7-12 Angstroms have proven useful.");
	joboptions["do_center"] = JobOption("Center class averages?", true, "If set to Yes, every iteration the class average images will be centered on their center-of-mass. This will only work for positive signals, so the particles should be white.");

	joboptions["dont_skip_align"] = JobOption("Perform image alignment?", true, "If set to No, then rather than \
performing both alignment and classification, only classification will be performed. This allows the use of very focused masks.\
This requires that the optimal orientations of all particles are already stored in the input STAR file. ");
	joboptions["psi_sampling"] = JobOption("In-plane angular sampling:", 6., 0.5, 20, 0.5, "The sampling rate for the in-plane rotation angle (psi) in degrees. \
Using fine values will slow down the program. Recommended value for most 2D refinements: 5 degrees.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.");
	joboptions["offset_range"] = JobOption("Offset search range (pix):", 5, 0, 30, 1, "Probabilities will be calculated only for translations \
in a circle with this radius (in pixels). The center of this circle changes at every iteration and is placed at the optimal translation \
for each image in the previous iteration.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.");
	joboptions["offset_step"] = JobOption("Offset search step (pix):", 1, 0.1, 5, 0.1, "Translations will be sampled with this step-size (in pixels).\
Translational sampling is also done using the adaptive approach. \
Therefore, if adaptive=1, the translations will first be evaluated on a 2x coarser grid.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.");
	joboptions["allow_coarser"] = JobOption("Allow coarser sampling?", false, "If set to Yes, the program will use coarser angular and translational samplings if the estimated accuracies of the assignments is still low in the earlier iterations. This may speed up the calculations.");

	joboptions["do_helix"] = JobOption("Classify 2D helical segments?", false, "Set to Yes if you want to classify 2D helical segments. Note that the helical segments should come with priors of psi angles");
	joboptions["helical_tube_outer_diameter"] = JobOption("Tube diameter (A): ", 200, 100, 1000, 10, "Outer diameter (in Angstroms) of helical tubes. \
This value should be slightly larger than the actual width of the tubes. You may want to copy the value from previous particle extraction job. \
If negative value is provided, this option is disabled and ordinary circular masks will be applied. Sometimes '--dont_check_norm' option is useful to prevent errors in normalisation of helical segments.");
	joboptions["do_bimodal_psi"] = JobOption("Do bimodal angular searches?", true, "Do bimodal search for psi angles? \
Set to Yes if you want to classify 2D helical segments with priors of psi angles. The priors should be bimodal due to unknown polarities of the segments. \
Set to No if the 3D helix looks the same when rotated upside down. If it is set to No, ordinary angular searches will be performed.\n\nThis option will be invalid if you choose not to perform image alignment on 'Sampling' tab.");
	joboptions["range_psi"] = JobOption("Angular search range - psi (deg):", 6, 3, 30, 1, "Local angular searches will be performed \
within +/- the given amount (in degrees) from the psi priors estimated through helical segment picking. \
A range of 15 degrees is the same as sigma = 5 degrees. Note that the ranges of angular searches should be much larger than the sampling.\
\n\nThis option will be invalid if you choose not to perform image alignment on 'Sampling' tab.");
	joboptions["do_restrict_xoff"] = JobOption("Restrict helical offsets to rise:", true, "Set to Yes if you want to restrict the translational offsets along the helices to the rise of the helix given below. Set to No to allow free (conventional) translational offsets.");
	joboptions["helical_rise"] = JobOption("Helical rise (A):", 4.75, -1, 100, 1, "The helical rise (in Angstroms). Translational offsets along the helical axis will be limited from -rise/2 to +rise/2, with a flat prior.");


	joboptions["nr_pool"] = JobOption("Number of pooled particles:", 3, 1, 16, 1, "Particles are processed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.");
	joboptions["do_parallel_discio"] = JobOption("Use parallel disc I/O?", true, "If set to Yes, all MPI followers will read images from disc. \
Otherwise, only the leader will read images and send them through the network to the followers. Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.");
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

bool RelionJob::getCommandsClass2DJob(std::string &outputname, std::vector<std::string> &commands,
		std::string &final_command, bool do_makedir, int job_counter, std::string &error_message)
{
	commands.clear();
	initialisePipeline(outputname, job_counter);
	std::string command;

	if (joboptions["nr_mpi"].getNumber(error_message) > 1)
		command="`which relion_refine_mpi`";
	else
		command="`which relion_refine`";
	if (error_message != "") return false;

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
		{
			error_message = "Warning: invalid optimiser.star filename provided for continuation run!";
			return false;
		}
		// SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
		//int it = (int)textToFloat((joboptions["fn_cont"].getString().substr(pos_it+3, 6)).c_str());
		//fn_run += "_ct" + floatToString(it);
		command += " --continue " + joboptions["fn_cont"].getString();
	}

	command += " --o " + outputname + fn_run;

	int my_classes = (int)joboptions["nr_classes"].getNumber(error_message);
	if (error_message != "") return false;

	// Optimisation
	int my_iter;
	if (joboptions["do_em"].getBoolean())
	{
		if (joboptions["do_grad"].getBoolean())
		{
			error_message = "You cannot specify to use both the EM and the VDAM algorithm!";
			return false;
		}

		command += " --iter " + joboptions["nr_iter_em"].getString();

		my_iter = (int)joboptions["nr_iter_em"].getNumber(error_message);
		if (error_message != "") return false;
	}
	else if (joboptions["do_grad"].getBoolean())
	{
		if (joboptions["nr_mpi"].getNumber(error_message) > 1)
		{
			error_message = "Gradient refinement (running the VDAM algorithm) is not supported together with MPI.";
			return false;
		}

		command += " --grad --class_inactivity_threshold 0.1 --grad_write_iter 10";
		command += " --iter " + joboptions["nr_iter_grad"].getString();

		my_iter = (int)joboptions["nr_iter_grad"].getNumber(error_message);
		if (error_message != "") return false;
	}
	else
	{
		error_message = "You need to specify to use either the EM or the VDAM algorithm";
		return false;
	}

	outputNodes = getOutputNodesRefine(outputname + fn_run, "Class2D", my_iter, my_classes, 2, 1, is_tomo);

	if (!is_continue)
	{
		if (joboptions["fn_img"].getString() == "")
		{
			error_message = "ERROR: empty field for input STAR file...";
			return false;
		}
		command += " --i " + joboptions["fn_img"].getString();
		Node node(joboptions["fn_img"].getString(), joboptions["fn_img"].node_type);
		inputNodes.push_back(node);
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
	// Takanori observed bad 2D classifications with pad1, so use pad2 always. Memory isnt a problem here anyway.
	command += " --pad 2 ";

	// CTF stuff
	if (!is_continue)
	{
		if (joboptions["do_ctf_correction"].getBoolean())
		{
			command += " --ctf ";
			if (joboptions["ctf_intact_first_peak"].getBoolean())
				command += " --ctf_intact_first_peak ";
		}
	}

	command += " --tau2_fudge " + joboptions["tau_fudge"].getString();
	 command += " --particle_diameter " + joboptions["particle_diameter"].getString();
	if (!is_continue)
	{

		command += " --K " + joboptions["nr_classes"].getString();
		// Always flatten the solvent
		command += " --flatten_solvent ";
		if (joboptions["do_zero_mask"].getBoolean())
			command += " --zero_mask ";
		if (joboptions["highres_limit"].getNumber(error_message) > 0)
			command += " --strict_highres_exp " + joboptions["highres_limit"].getString();
		if (error_message != "") return false;

	}

	if (joboptions["do_center"].getBoolean())
	{
		command += " --center_classes ";
	}
	// Sampling
	int iover = 1;
	command += " --oversampling " + floatToString((float)iover);

	if (!joboptions["dont_skip_align"].getBoolean())
	{
		command += " --skip_align ";
	}
	else
	{
		// The sampling given in the GUI will be the oversampled one!
		command += " --psi_step " + floatToString(joboptions["psi_sampling"].getNumber(error_message) * pow(2., iover));
		if (error_message != "") return false;

		// Offset range
		command += " --offset_range " + joboptions["offset_range"].getString();
		// The sampling given in the GUI will be the oversampled one!
		command += " --offset_step " + floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover));
		if (error_message != "") return false;

		if (joboptions["allow_coarser"].getBoolean())
		{
			command += " --allow_coarser_sampling";
		}

	}

	// Helix
	if (joboptions["do_helix"].getBoolean())
	{
		label += ".helical";

		command += " --helical_outer_diameter " + joboptions["helical_tube_outer_diameter"].getString();

		if (joboptions["dont_skip_align"].getBoolean())
		{
			if (joboptions["do_bimodal_psi"].getBoolean())
				command += " --bimodal_psi";

			RFLOAT val = joboptions["range_psi"].getNumber(error_message);
			if (error_message != "") return false;

			val = (val < 0.) ? (0.) : (val);
			val = (val > 90.) ? (90.) : (val);
			command += " --sigma_psi " + floatToString(val / 3.);

			if (joboptions["do_restrict_xoff"].getBoolean())
			{
				command += " --helix --helical_rise_initial " + joboptions["helical_rise"].getString();
			}
		}
	}

	// Always do norm and scale correction
	if (!is_continue)
		command += " --norm --scale ";

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
	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

// Constructor for initial model job
