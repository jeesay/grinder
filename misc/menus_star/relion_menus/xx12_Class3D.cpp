void RelionJob::initialiseClass3DJob()
{
	hidden_name = ".gui_class3d";

    if (is_tomo)
    {
        addTomoInputOptions(true, true, true, false);
    }
    else
    {
        joboptions["fn_img"] = JobOption("Input images STAR file:", LABEL_PARTS_CPIPE, 1, "", "STAR files (*.star)", "A STAR file with all images (and their metadata).");
    }

	joboptions["fn_cont"] = JobOption("Continue from here: ", std::string(""), "STAR Files (*_optimiser.star)", "CURRENT_ODIR", "Select the *_optimiser.star file for the iteration \
from which you want to continue a previous run. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a '_ctX' to the output rootname, \
with X being the iteration from which one continues the previous run.");
	joboptions["fn_ref"] = JobOption("Reference map:", LABEL_MAP_CPIPE, 1, "", "Image Files (*.{spi,vol,mrc})", "A 3D map in MRC/Spider format. \
	Make sure this map has the same dimensions and the same pixel size as your input images, or specify that one can resize the reference if needed.");
	joboptions["fn_mask"] = JobOption("Reference mask (optional):", LABEL_MASK_CPIPE, 1, "", "Image Files (*.{spi,vol,msk,mrc})", "\
If no mask is provided, a soft spherical mask based on the particle diameter will be used.\n\
\n\
Otherwise, provide a Spider/mrc map containing a (soft) mask with the same \
dimensions as the reference(s), and values between 0 and 1, with 1 being 100% protein and 0 being 100% solvent. \
The reconstructed reference map will be multiplied by this mask.\n\
\n\
In some cases, for example for non-empty icosahedral viruses, it is also useful to use a second mask. For all white (value 1) pixels in this second mask \
the corresponding pixels in the reconstructed map are set to the average value of these pixels. \
Thereby, for example, the higher density inside the virion may be set to a constant. \
Note that this second mask should have one-values inside the virion and zero-values in the capsid and the solvent areas. \
To use a second mask, use the additional option --solvent_mask2, which may given in the Additional arguments line (in the Running tab).");

	joboptions["ref_correct_greyscale"] = JobOption("Ref. map is on absolute greyscale?", false, "Probabilities are calculated based on a Gaussian noise model, \
which contains a squared difference term between the reference and the experimental image. This has a consequence that the \
reference needs to be on the same absolute intensity grey-scale as the experimental images. \
RELION and XMIPP reconstruct maps at their absolute intensity grey-scale. \
Other packages may perform internal normalisations of the reference density, which will result in incorrect grey-scales. \
Therefore: if the map was reconstructed in RELION or in XMIPP, set this option to Yes, otherwise set it to No. \
If set to No, RELION will use a (grey-scale invariant) cross-correlation criterion in the first iteration, \
and prior to the second iteration the map will be filtered again using the initial low-pass filter. \
This procedure is relatively quick and typically does not negatively affect the outcome of the subsequent MAP refinement. \
Therefore, if in doubt it is recommended to set this option to No.");
    joboptions["trust_ref_size"] = JobOption("Resize reference if needed?", true, "If true, and if the input reference map (and mask) do not have the same pixel size and/or box size, then they will be re-scaled and re-boxed accordingly. If this option is set to false, then the program will die with an error if the reference does not have the correct pixel and/or box size.");
	joboptions["ini_high"] = JobOption("Initial low-pass filter (A):", 60, 0, 200, 5, "It is recommended to strongly low-pass filter your initial reference map. \
If it has not yet been low-pass filtered, it may be done internally using this option. \
If set to 0, no low-pass filter will be applied to the initial reference(s).");
	joboptions["sym_name"] = JobOption("Symmetry:", std::string("C1"), "If the molecule is asymmetric, \
set Symmetry group to C1. Note their are multiple possibilities for icosahedral symmetry: \n \
* I1: No-Crowther 222 (standard in Heymann, Chagoyen & Belnap, JSB, 151 (2005) 196–207) \n \
* I2: Crowther 222 \n \
* I3: 52-setting (as used in SPIDER?)\n \
* I4: A different 52 setting \n \
The command 'relion_refine --sym D2 --print_symmetry_ops' prints a list of all symmetry operators for symmetry group D2. \
RELION uses XMIPP's libraries for symmetry operations. \
Therefore, look at the XMIPP Wiki for more details:  http://xmipp.cnb.csic.es/twiki/bin/view/Xmipp/WebHome?topic=Symmetry");

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
	float default_T = (is_tomo) ? 1 : 4;
    joboptions["tau_fudge"] = JobOption("Regularisation parameter T:", default_T , 0.1, 10, 0.1, "Bayes law strictly determines the relative weight between \
the contribution of the experimental data and the prior. However, in practice one may need to adjust this weight to put slightly more weight on \
the experimental data to allow optimal results. Values greater than 1 for this regularisation parameter (T in the JMB2011 paper) put more \
weight on the experimental data. Values around 2-4 have been observed to be useful for 3D refinements, values of 1-2 for 2D refinements. \
Too small values yield too-low resolution structures; too high values result in over-estimated resolutions, mostly notable by the apparition of high-frequency noise in the references.");
	joboptions["nr_iter"] = JobOption("Number of iterations:", 25, 1, 50, 1, "Number of iterations to be performed. \
Note that the current implementation of 2D class averaging and 3D classification does NOT comprise a convergence criterium. \
Therefore, the calculations will need to be stopped by the user if further iterations do not yield improvements in resolution or classes. \n\n \
Also note that upon restarting, the iteration number continues to be increased, starting from the final iteration in the previous run. \
The number given here is the TOTAL number of iterations. For example, if 10 iterations have been performed previously and one restarts to perform \
an additional 5 iterations (for example with a finer angular sampling), then the number given here should be 10+5=15.");
	joboptions["do_fast_subsets"] = JobOption("Use fast subsets (for large data sets)?", false, "If set to Yes, the first 5 iterations will be done with random subsets of only K*1500 particles (K being the number of classes); the next 5 with K*4500 particles, the next 5 with 30% of the data set; and the final ones with all data. This was inspired by a cisTEM implementation by Niko Grigorieff et al.");

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
	joboptions["do_blush"] = JobOption("Use Blush regularisation?", false, "If set to Yes, relion_refine will use a neural network to perform regularisation by denoising at every iteration, instead of the standard smoothness regularisation.");

	joboptions["dont_skip_align"] = JobOption("Perform image alignment?", true, "If set to No, then rather than \
performing both alignment and classification, only classification will be performed. This allows the use of very focused masks.\
This requires that the optimal orientations of all particles are already stored in the input STAR file. ");
	joboptions["sampling"] = JobOption("Angular sampling interval:", job_sampling_options, 2, "There are only a few discrete \
angular samplings possible because we use the HealPix library to generate the sampling of the first two Euler angles on the sphere. \
The samplings are approximate numbers and vary slightly over the sphere.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.");
	joboptions["offset_range"] = JobOption("Offset search range (pix):", 5, 0, 30, 1, "Probabilities will be calculated only for translations \
in a circle with this radius (in pixels). The center of this circle changes at every iteration and is placed at the optimal translation \
for each image in the previous iteration.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.");
	joboptions["offset_step"] = JobOption("Offset search step (pix):", 1, 0.1, 5, 0.1, "Translations will be sampled with this step-size (in pixels).\
Translational sampling is also done using the adaptive approach. \
Therefore, if adaptive=1, the translations will first be evaluated on a 2x coarser grid.\n\n \
If auto-sampling is used, this will be the value for the first iteration(s) only, and the sampling rate will be increased automatically after that.");
	joboptions["do_local_ang_searches"] = JobOption("Perform local angular searches?", false, "If set to Yes, then rather than \
performing exhaustive angular searches, local searches within the range given below will be performed. \
A prior Gaussian distribution centered at the optimal orientation in the previous iteration and \
with a stddev of 1/3 of the range given below will be enforced.");
	joboptions["sigma_angles"] = JobOption("Local angular search range:", 5., 0, 15, 0.1, "Local angular searches will be performed \
within +/- the given amount (in degrees) from the optimal orientation in the previous iteration. \
A Gaussian prior (also see previous option) will be applied, so that orientations closer to the optimal orientation \
in the previous iteration will get higher weights than those further away.");
	joboptions["allow_coarser"] = JobOption("Allow coarser sampling?", false, "If set to Yes, the program will use coarser angular and translational samplings if the estimated accuracies of the assignments is still low in the earlier iterations. This may speed up the calculations.");
	joboptions["relax_sym"] = JobOption("Relax symmetry:", std::string(""), "With this option, poses related to the standard local angular search range by the given point group will also be explored. For example, if you have a pseudo-symmetric dimer A-A', refinement or classification in C1 with symmetry relaxation by C2 might be able to improve distinction between A and A'. Note that the reference must be more-or-less aligned to the convention of (pseudo-)symmetry operators. For details, see Ilca et al 2019 and Abrishami et al 2020 cited in the About dialog.");

    if (is_tomo)
        joboptions["sigma_tilt"] = JobOption("Prior width on tilt angle (deg):", -1, -1, 30, 1, "The width of the prior on the tilt angle: angular searches will be +/-3 times this value. Tilt priors will be defined when particles have been picked as filaments, on spheres or on manifolds. Setting this width to a negative value will lead to no prior being used on the tilt angle.");


	joboptions["do_helix"] = JobOption("Do helical reconstruction?", false, "If set to Yes, then perform 3D helical reconstruction.");
	joboptions["helical_tube_inner_diameter"] = JobOption("Tube diameter - inner (A):", std::string("-1"),"Inner and outer diameter (in Angstroms) of the reconstructed helix spanning across Z axis. \
Set the inner diameter to negative value if the helix is not hollow in the center. The outer diameter should be slightly larger than the actual width of helical tubes because it also decides the shape of 2D \
particle mask for each segment. If the psi priors of the extracted segments are not accurate enough due to high noise level or flexibility of the structure, then set the outer diameter to a large value.");
	joboptions["helical_tube_outer_diameter"] = JobOption("Tube diameter - outer (A):", std::string("-1"),"Inner and outer diameter (in Angstroms) of the reconstructed helix spanning across Z axis. \
Set the inner diameter to negative value if the helix is not hollow in the center. The outer diameter should be slightly larger than the actual width of helical tubes because it also decides the shape of 2D \
particle mask for each segment. If the psi priors of the extracted segments are not accurate enough due to high noise level or flexibility of the structure, then set the outer diameter to a large value.");
	joboptions["range_rot"] = JobOption("Angular search range - rot (deg):", std::string("-1"), "Local angular searches will be performed \
within +/- of the given amount (in degrees) from the optimal orientation in the previous iteration. The default negative value means that no local searches will be performed. \
A Gaussian prior will be applied, so that orientations closer to the optimal orientation \
in the previous iteration will get higher weights than those further away.\n\nThese ranges will only be applied to the \
rot, tilt and psi angles in the first few iterations (global searches for orientations) in 3D helical reconstruction. \
Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible structures and more memory and computation time will be used. \
A range of 15 degrees means sigma = 5 degrees.\n\nThese options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.");
	joboptions["range_tilt"] = JobOption("Angular search range - tilt (deg):", std::string("15"), "Local angular searches will be performed \
within +/- the given amount (in degrees) from the optimal orientation in the previous iteration. \
A Gaussian prior (also see previous option) will be applied, so that orientations closer to the optimal orientation \
in the previous iteration will get higher weights than those further away.\n\nThese ranges will only be applied to the \
rot, tilt and psi angles in the first few iterations (global searches for orientations) in 3D helical reconstruction. \
Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible structures and more memory and computation time will be used. \
A range of 15 degrees means sigma = 5 degrees.\n\nThese options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.");
	joboptions["range_psi"] = JobOption("Angular search range - psi (deg):", std::string("10"), "Local angular searches will be performed \
within +/- the given amount (in degrees) from the optimal orientation in the previous iteration. \
A Gaussian prior (also see previous option) will be applied, so that orientations closer to the optimal orientation \
in the previous iteration will get higher weights than those further away.\n\nThese ranges will only be applied to the \
rot, tilt and psi angles in the first few iterations (global searches for orientations) in 3D helical reconstruction. \
Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible structures and more memory and computation time will be used. \
A range of 15 degrees means sigma = 5 degrees.\n\nThese options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.");
	joboptions["do_apply_helical_symmetry"] = JobOption("Apply helical symmetry?", true, "If set to Yes, helical symmetry will be applied in every iteration. Set to No if you have just started a project, helical symmetry is unknown or not yet estimated.");
	joboptions["helical_nr_asu"] = JobOption("Number of unique asymmetrical units:", 1, 1, 100, 1, "Number of unique helical asymmetrical units in each segment box. If the inter-box distance (set in segment picking step) \
is 100 Angstroms and the estimated helical rise is ~20 Angstroms, then set this value to 100 / 20 = 5 (nearest integer). This integer should not be less than 1. The correct value is essential in measuring the \
signal to noise ratio in helical reconstruction.");
	joboptions["helical_twist_initial"] =  JobOption("Initial helical twist (deg):", std::string("0"),"Initial helical symmetry. Set helical twist (in degrees) to positive value if it is a right-handed helix. \
Helical rise is a positive value in Angstroms. If local searches of helical symmetry are planned, initial values of helical twist and rise should be within their respective ranges.");
	joboptions["helical_rise_initial"] = JobOption("Initial helical rise (A):", std::string("0"), "Initial helical symmetry. Set helical twist (in degrees) to positive value if it is a right-handed helix. \
Helical rise is a positive value in Angstroms. If local searches of helical symmetry are planned, initial values of helical twist and rise should be within their respective ranges.");
	joboptions["helical_z_percentage"] = JobOption("Central Z length (%):", 30., 5., 80., 1., "Reconstructed helix suffers from inaccuracies of orientation searches. \
The central part of the box contains more reliable information compared to the top and bottom parts along Z axis, where Fourier artefacts are also present if the \
number of helical asymmetrical units is larger than 1. Therefore, information from the central part of the box is used for searching and imposing \
helical symmetry in real space. Set this value (%) to the central part length along Z axis divided by the box size. Values around 30% are commonly used.");
	joboptions["do_local_search_helical_symmetry"] = JobOption("Do local searches of symmetry?", false, "If set to Yes, then perform local searches of helical twist and rise within given ranges.");
	joboptions["helical_twist_min"] = JobOption("Helical twist search (deg) - Min:", std::string("0"), "Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) \
to positive value if it is a right-handed helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the true helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.");
	joboptions["helical_twist_max"] = JobOption("Helical twist search (deg) - Max:", std::string("0"), "Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) \
to positive value if it is a right-handed helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the true helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.");
	joboptions["helical_twist_inistep"] = JobOption("Helical twist search (deg) - Step:", std::string("0"), "Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) \
to positive value if it is a right-handed helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the true helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.");
	joboptions["helical_rise_min"] = JobOption("Helical rise search (A) - Min:", std::string("0"), "Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. \
Generally it is not necessary for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the true helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.");
	joboptions["helical_rise_max"] = JobOption("Helical rise search (A) - Max:", std::string("0"), "Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. \
Generally it is not necessary for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the true helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.");
	joboptions["helical_rise_inistep"] = JobOption("Helical rise search (A) - Step:", std::string("0"), "Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. \
Generally it is not necessary for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set manually if the default value \
does not guarantee convergence. The program cannot find a reasonable symmetry if the true helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.");
	joboptions["helical_range_distance"] = JobOption("Range factor of local averaging:", -1., 1., 5., 0.1, "Local averaging of orientations and translations will be performed within a range of +/- this value * the box size. Polarities are also set to be the same for segments coming from the same tube during local refinement. \
Values of ~ 2.0 are recommended for flexible structures such as MAVS-CARD filaments, ParM, MamK, etc. This option might not improve the reconstructions of helices formed from curled 2D lattices (TMV and VipA/VipB). Set to negative to disable this option.");
	joboptions["keep_tilt_prior_fixed"] = JobOption("Keep tilt-prior fixed:", true, "If set to yes, the tilt prior will not change during the optimisation. If set to No, at each iteration the tilt prior will move to the optimal tilt value for that segment from the previous iteration.");

	joboptions["do_parallel_discio"] = JobOption("Use parallel disc I/O?", true, "If set to Yes, all MPI followers will read their own images from disc. \
Otherwise, only the leader will read images and send them through the network to the followers. Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.");
	joboptions["nr_pool"] = JobOption("Number of pooled particles:", 3, 1, 16, 1, "Particles are processed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.");
	joboptions["do_pad1"] = JobOption("Skip padding?", false, "If set to Yes, the calculations will not use padding in Fourier space for better interpolation in the references. Otherwise, references are padded 2x before Fourier transforms are calculated. Skipping padding (i.e. use --pad 1) gives nearly as good results as using --pad 2, but some artifacts may appear in the corners from signal that is folded back.");
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
	joboptions["gpu_ids"] = JobOption("Which GPUs to use:", std::string(""), "This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','.  For example: '0,0:1,1:0,0:1,1'");
}

bool RelionJob::getCommandsClass3DJob(std::string &outputname, std::vector<std::string> &commands,
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
			std::cerr << "Warning: invalid optimiser.star filename provided for continuation run: " << joboptions["fn_cont"].getString() << std::endl;
		// SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
		//int it = (int)textToFloat((joboptions["fn_cont"].getString().substr(pos_it+3, 6)).c_str());
		//fn_run += "_ct" + floatToString(it);;
		command += " --continue " + joboptions["fn_cont"].getString();

	}

	command += " --o " + outputname + fn_run;

	int my_iter = (int)joboptions["nr_iter"].getNumber(error_message);
	if (error_message != "") return false;

	int my_classes = (int)joboptions["nr_classes"].getNumber(error_message);
	if (error_message != "") return false;

	outputNodes = getOutputNodesRefine(outputname + fn_run, "Class3D", my_iter, my_classes, 3, 1, is_tomo);

	if (!is_continue)
	{
        if (is_tomo)
        {
            error_message = getTomoInputCommmand(true, command, HAS_COMPULSORY, HAS_COMPULSORY, HAS_NOT, HAS_NOT);
            if (error_message != "") return false;

            Node node1( outputname + fn_run + "_optimisation_set.star", LABEL_CLASS3D_OPTSET);
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

        if (joboptions["fn_ref"].getString() == "")
        {
            error_message = "ERROR: empty field for reference.";
            return false;
        }
        else
		{
			command += " --ref " + joboptions["fn_ref"].getString();
			if (joboptions["fn_ref"].getString() != "None")
            {
                Node node(joboptions["fn_ref"].getString(), joboptions["fn_ref"].node_type);
                inputNodes.push_back(node);
            }
			if (!joboptions["ref_correct_greyscale"].getBoolean())
				command += " --firstiter_cc";

            if (joboptions["trust_ref_size"].getBoolean())
                command += " --trust_ref_size";
		}

		if (joboptions["ini_high"].getNumber(error_message) > 0.)
			command += " --ini_high " + joboptions["ini_high"].getString();
		if (error_message != "") return false;

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
	if (joboptions["do_pad1"].getBoolean())
		command += " --pad 1 ";
	else
		command += " --pad 2 ";

	// CTF stuff
	if (!is_continue)
	{
		if (joboptions["do_ctf_correction"].getBoolean())
		{
			command += " --ctf";
			if (joboptions["ctf_intact_first_peak"].getBoolean())
				command += " --ctf_intact_first_peak";
		}
	}

	// Optimisation
	command += " --iter " + joboptions["nr_iter"].getString();
	command += " --tau2_fudge " + joboptions["tau_fudge"].getString();
	command += " --particle_diameter " + joboptions["particle_diameter"].getString();
	if (!is_continue)
	{
		if (joboptions["do_fast_subsets"].getBoolean())
			command += " --fast_subsets ";

		command += " --K " + joboptions["nr_classes"].getString();
		// Always flatten the solvent
		command += " --flatten_solvent";
		if (joboptions["do_zero_mask"].getBoolean())
			command += " --zero_mask";
		if (joboptions["highres_limit"].getNumber(error_message) > 0)
			command += " --strict_highres_exp " + joboptions["highres_limit"].getString();
		if (error_message != "") return false;
	}

	if (joboptions["do_blush"].getBoolean())
		command += " --blush ";

	if (joboptions["fn_mask"].getString().length() > 0)
	{
		command += " --solvent_mask " + joboptions["fn_mask"].getString();
		Node node(joboptions["fn_mask"].getString(), joboptions["fn_mask"].node_type);
		inputNodes.push_back(node);
	}

	// Sampling
	if (!joboptions["dont_skip_align"].getBoolean())
	{
		command += " --skip_align ";
	}
	else
	{
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

		// Manually input local angular searches
		if (joboptions["do_local_ang_searches"].getBoolean())
		{
			command += " --sigma_ang " + floatToString(joboptions["sigma_angles"].getNumber(error_message) / 3.);
			if (joboptions["relax_sym"].getString().length() > 0)
				command += " --relax_sym " + joboptions["relax_sym"].getString();

			if (error_message != "") return false;
		}

		// Offset range
		command += " --offset_range " + joboptions["offset_range"].getString();
		// The sampling given in the GUI will be the oversampled one!
		command += " --offset_step " +  floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover));
		if (error_message != "") return false;

		if (joboptions["allow_coarser"].getBoolean())
		{
			command += " --allow_coarser_sampling";
		}
	}

	// Provide symmetry, and always do norm and scale correction
	if (!is_continue)
	{
		command += " --sym " + joboptions["sym_name"].getString();
		command += " --norm --scale ";
	}

	if ( (!is_continue) && (joboptions["do_helix"].getBoolean()) )
	{
		label += ".helical";

		command += " --helix";

		float inner_diam = joboptions["helical_tube_inner_diameter"].getNumber(error_message);
		if (error_message != "") return false;
		if (inner_diam > 0.)
			command += " --helical_inner_diameter " + joboptions["helical_tube_inner_diameter"].getString();

		command += " --helical_outer_diameter " + joboptions["helical_tube_outer_diameter"].getString();
		if (joboptions["do_apply_helical_symmetry"].getBoolean())
		{
			command += " --helical_nr_asu " + joboptions["helical_nr_asu"].getString();
			command += " --helical_twist_initial " + joboptions["helical_twist_initial"].getString();
			command += " --helical_rise_initial " + joboptions["helical_rise_initial"].getString();

			float myz = joboptions["helical_z_percentage"].getNumber(error_message) / 100.;
			if (error_message != "") return false;
			command += " --helical_z_percentage " + floatToString(myz);

			if (joboptions["do_local_search_helical_symmetry"].getBoolean())
			{
				command += " --helical_symmetry_search";
				command += " --helical_twist_min " + joboptions["helical_twist_min"].getString();
				command += " --helical_twist_max " + joboptions["helical_twist_max"].getString();

				float twist_inistep = joboptions["helical_twist_inistep"].getNumber(error_message);
				if (error_message != "") return false;
				if (twist_inistep > 0.)
					command += " --helical_twist_inistep " + joboptions["helical_twist_inistep"].getString();

				command += " --helical_rise_min " + joboptions["helical_rise_min"].getString();
				command += " --helical_rise_max " + joboptions["helical_rise_max"].getString();

				float rise_inistep = joboptions["helical_rise_inistep"].getNumber(error_message);
				if (error_message != "") return false;
				if (rise_inistep > 0.)
					command += " --helical_rise_inistep " + joboptions["helical_rise_inistep"].getString();
			}
		}
		else
			command += " --ignore_helical_symmetry";
		if (joboptions["keep_tilt_prior_fixed"].getBoolean())
			command += " --helical_keep_tilt_prior_fixed";
		if ( (joboptions["dont_skip_align"].getBoolean()) && (!joboptions["do_local_ang_searches"].getBoolean()) )
		{
			float val = joboptions["range_tilt"].getNumber(error_message);
			if (error_message != "") return false;
			val = (val < 0.) ? (0.) : (val);
			val = (val > 90.) ? (90.) : (val);
			command += " --sigma_tilt " + floatToString(val / 3.);

			val = joboptions["range_psi"].getNumber(error_message);
			if (error_message != "") return false;
			val = (val < 0.) ? (0.) : (val);
			val = (val > 90.) ? (90.) : (val);
			command += " --sigma_psi " + floatToString(val / 3.);

			val = joboptions["range_rot"].getNumber(error_message);
			if (error_message != "") return false;
			val = (val < 0.) ? (0.) : (val);
			val = (val > 90.) ? (90.) : (val);
			command += " --sigma_rot " + floatToString(val / 3.);

			val = joboptions["helical_range_distance"].getNumber(error_message);
			if (error_message != "") return false;
			if (val > 0.)
				command += " --helical_sigma_distance " + floatToString(val / 3.);
		}
	}

	// Running stuff
	command += " --j " + joboptions["nr_threads"].getString();

	// GPU-stuff
	if (joboptions["use_gpu"].getBoolean())
	{
		if (!joboptions["dont_skip_align"].getBoolean())
		{
			error_message = "ERROR: you cannot use GPUs when skipping image alignments.";
			return false;
		}
		command += " --gpu \"" + joboptions["gpu_ids"].getString() + "\"";
	}

	// Other arguments
	command += " " + joboptions["other_args"].getString();

	commands.push_back(command);

	return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message);
}

