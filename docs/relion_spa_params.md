
---
### relion

```bash
 [--refresh 2]  : refresh rate in seconds
 [--idle 3600]  : quit GUI after this many second
 [--readonly]   : limited version of GUI that does not touch any files
 [--tomo]   : show tomography-specific GUI
 [--ccpem]  : use the ccpem pipeliner
 [--do_projdir] : Don't confirm the creation of a new project directory, just make it if it doesn't exist
 [--version]: show the version of this program
```

---
### relion_align_symmetry

####  Options 
```bash 
--i : Input map to be aligned (OR: input model.star, from which input map will be selected)
--sym : Target point group symmetry
--select_largest_class (false) : Select largest class from model.star; by default map with best symmetry will be selected
--select_highest_resol (false) : Select class with highest resolution from model.star; by default map with best symmetry will be selected
--o (aligned.mrc) : Name for output aligned map)
--box_size (64) : Working box size in pixels. Very small box (such that Nyquist is aroud 20 A) is usually sufficient.
--keep_centre (false) : Do not re-centre the input
--angpix (-1) : Pixel size (in Angstroms)
--only_rot (false) : Keep TILT and PSI fixed and search only ROT (rotation along the Z axis)
--nr_uniform (400) : Randomly search this many orientations
--maxres (-1) : Maximum resolution (in Angstrom) to consider in Fourier space (default Nyquist)
--local_search_range (2) : Local search range (1 + 2 * this number)
--local_search_step (2) : Local search step (in degrees)
--pad (2) : Padding factor
--apply_sym (false) : Also apply the symmetry to the map
--NN (false) : Use nearest-neighbour instead of linear interpolation
--version : Print RELION version and exit
```
---
### relion_align_tiltseries

---
### relion_autopick

####  General options 
```bash 
--i : Micrograph STAR file OR filenames from which to autopick particles, e.g. "Micrographs/*.mrc"
--pickname (autopick) : Rootname for coordinate STAR files
--odir (AutoPick/) : Output directory for coordinate files (default is to store next to micrographs)
--angpix (1) : Pixel size of the micrographs in Angstroms
--particle_diameter (-1) : Diameter of the circular mask that will be applied to the experimental images (in Angstroms, default=automatic)
--shrink_particle_mask (2) : Shrink the particle mask by this many pixels (to detect Einstein-from-noise classes)
--outlier_removal_zscore (8.) : Remove pixels that are this many sigma away from the mean
--write_fom_maps (false) : Write calculated probability-ratio maps to disc (for re-reading in subsequent runs)
--no_fom_limit (false) : Ignore default maximum limit of 30 fom maps being written
--read_fom_maps (false) : Skip probability calculations, re-read precalculated maps from disc
--skip_optimise_scale (false) : Skip the optimisation of the micrograph scale for better prime factors in the FFTs. This runs slower, but at exactly the requested resolution.
--only_do_unfinished (false) : Only autopick those micrographs for which the coordinate file does not yet exist
--gpu (false) : Use GPU acceleration when availiable
```
####  References options 
```bash 
--ref () : STAR file with the reference names, or an MRC stack with all references, or "gauss" for blob-picking
--angpix_ref (-1) : Pixel size of the references in Angstroms (default is same as micrographs)
--invert (false) : Density in micrograph is inverted w.r.t. density in template
--ang (10) : Angular sampling (in degrees); use 360 for no rotations
--lowpass (-1) : Lowpass filter in Angstroms for the references (prevent Einstein-from-noise!)
--highpass (-1) : Highpass filter in Angstroms for the micrographs
--ctf (false) : Perform CTF correction on the references?
--ctf_intact_first_peak (false) : Ignore CTFs until their first peak?
--gauss_max (0.1) : Value of the peak in the Gaussian blob reference
--healpix_order (1) : Healpix order for projecting a 3D reference (hp0=60deg; hp1=30deg; hp2=15deg)
--sym (C1) : Symmetry point group for a 3D reference
```
####  Laplacian-of-Gaussian options 
```bash 
--LoG (false) : Use Laplacian-of-Gaussian filter-based picking, instead of template matching
--LoG_diam_min (-1) : Smallest particle diameter (in Angstroms) for blob-detection by Laplacian-of-Gaussian filter
--LoG_diam_max (-1) : Largest particle diameter (in Angstroms) for blob-detection by Laplacian-of-Gaussian filter
--LoG_neighbour (100) : Avoid neighbouring particles within (the detected diameter + the minimum diameter) times this percent
--Log_invert (false) : Use this option if the particles are white instead of black
--LoG_adjust_threshold (0.) : Use this option to adjust the picking threshold: positive for less particles, negative for more
--LoG_upper_threshold (99999) : Use this option to set the upper limit of the picking threshold
--LoG_use_ctf (false) : Use CTF until the first peak in Laplacian-of-Gaussian picker
```
####  Topaz wrapper options 
```bash 
--topaz_train (false) : Use wrapper to the topaz train command
--topaz_extract (false) : Use wrapper to the topaz extract command (i.e. predict particle positions)
--topaz_nr_particles (200) : Expected number of particles per micrograph for topaz
--topaz_threshold (-6) : Minimum threshold for topaz picking
--topaz_train_picks () : Name of picking coordinates for topaz training
--topaz_train_parts () : OR: name of particle star file for topaz training
--topaz_test_ratio (0.2) : Ratio of picks in the test set for cross-validation in topaz training
--topaz_downscale (-1) : Downscale factor for topaz
--topaz_model () : Saved model model from topaz train for topaz extract. Leave this empty to use the default (general) model.
--topaz_radius (-1) : Particle radius (in pix) for topaz extract (default is from particle diameter)
--topaz_args () : Additional arguments to be passed to topaz
--topaz_workers (1) : Number of topaz workers for parallelized training
--topaz_plot (false) : Plot intermediate information for helical picking in topaz (developmental)
--fn_topaz_exe (relion_python_topaz) : Topaz executable (default is using relion_python_topaz from conda install)
```
####  Helix options 
```bash 
--helix (false) : Are the references 2D helical segments? If so, in-plane rotation angles (psi) are estimated for the references.
--helical_tube_kappa_max (0.25) : Factor of maximum curvature relative to that of a circle
--helical_tube_outer_diameter (-1) : Tube diameter in Angstroms
--helical_tube_length_min (-1) : Minimum tube length in Angstroms
--amyloid (false) : Activate specific algorithm for amyloid picking?
--max_diam_local_avg (-1) : Maximum diameter to calculate local average density in Angstroms
```
####  Peak-search options 
```bash 
--threshold (0.25) : Fraction of expected probability ratio in order to consider peaks?
--min_distance (-1) : Minimum distance (in A) between any two particles (default is half the box size)
--max_stddev_noise (-1) : Maximum standard deviation in the noise area to use for picking peaks (default is no maximum)
--min_avg_noise (-999.) : Minimum average in the noise area to use for picking peaks (default is no minimum)
--skip_side (0) : Keep this many extra pixels (apart from particle_size/2) away from the edge of the micrograph 
```
####  Expert options 
```bash 
--verb (1) : Verbosity
--pad (2) : Padding factor for Fourier transforms
--random_seed (1) : Number for the random seed generator
--shrink (1.0) : Reduce micrograph to this fraction size, during correlation calc (saves memory and time)
--Log_max_search (5.) : Maximum diameter in LoG-picking multi-scale approach is this many times the min/max diameter
--extra_pad (0) : Number of pixels for additional padding of the original micrograph
--version : Print RELION version and exit
```
---
### relion_autopick_mpi

####  General options 
```bash 
--i : Micrograph STAR file OR filenames from which to autopick particles, e.g. "Micrographs/*.mrc"
--pickname (autopick) : Rootname for coordinate STAR files
--odir (AutoPick/) : Output directory for coordinate files (default is to store next to micrographs)
--angpix (1) : Pixel size of the micrographs in Angstroms
--particle_diameter (-1) : Diameter of the circular mask that will be applied to the experimental images (in Angstroms, default=automatic)
--shrink_particle_mask (2) : Shrink the particle mask by this many pixels (to detect Einstein-from-noise classes)
--outlier_removal_zscore (8.) : Remove pixels that are this many sigma away from the mean
--write_fom_maps (false) : Write calculated probability-ratio maps to disc (for re-reading in subsequent runs)
--no_fom_limit (false) : Ignore default maximum limit of 30 fom maps being written
--read_fom_maps (false) : Skip probability calculations, re-read precalculated maps from disc
--skip_optimise_scale (false) : Skip the optimisation of the micrograph scale for better prime factors in the FFTs. This runs slower, but at exactly the requested resolution.
--only_do_unfinished (false) : Only autopick those micrographs for which the coordinate file does not yet exist
--gpu (false) : Use GPU acceleration when availiable
```
####  References options 
```bash 
--ref () : STAR file with the reference names, or an MRC stack with all references, or "gauss" for blob-picking
--angpix_ref (-1) : Pixel size of the references in Angstroms (default is same as micrographs)
--invert (false) : Density in micrograph is inverted w.r.t. density in template
--ang (10) : Angular sampling (in degrees); use 360 for no rotations
--lowpass (-1) : Lowpass filter in Angstroms for the references (prevent Einstein-from-noise!)
--highpass (-1) : Highpass filter in Angstroms for the micrographs
--ctf (false) : Perform CTF correction on the references?
--ctf_intact_first_peak (false) : Ignore CTFs until their first peak?
--gauss_max (0.1) : Value of the peak in the Gaussian blob reference
--healpix_order (1) : Healpix order for projecting a 3D reference (hp0=60deg; hp1=30deg; hp2=15deg)
--sym (C1) : Symmetry point group for a 3D reference
```
####  Laplacian-of-Gaussian options 
```bash 
--LoG (false) : Use Laplacian-of-Gaussian filter-based picking, instead of template matching
--LoG_diam_min (-1) : Smallest particle diameter (in Angstroms) for blob-detection by Laplacian-of-Gaussian filter
--LoG_diam_max (-1) : Largest particle diameter (in Angstroms) for blob-detection by Laplacian-of-Gaussian filter
--LoG_neighbour (100) : Avoid neighbouring particles within (the detected diameter + the minimum diameter) times this percent
--Log_invert (false) : Use this option if the particles are white instead of black
--LoG_adjust_threshold (0.) : Use this option to adjust the picking threshold: positive for less particles, negative for more
--LoG_upper_threshold (99999) : Use this option to set the upper limit of the picking threshold
--LoG_use_ctf (false) : Use CTF until the first peak in Laplacian-of-Gaussian picker
```
####  Topaz wrapper options 
```bash 
--topaz_train (false) : Use wrapper to the topaz train command
--topaz_extract (false) : Use wrapper to the topaz extract command (i.e. predict particle positions)
--topaz_nr_particles (200) : Expected number of particles per micrograph for topaz
--topaz_threshold (-6) : Minimum threshold for topaz picking
--topaz_train_picks () : Name of picking coordinates for topaz training
--topaz_train_parts () : OR: name of particle star file for topaz training
--topaz_test_ratio (0.2) : Ratio of picks in the test set for cross-validation in topaz training
--topaz_downscale (-1) : Downscale factor for topaz
--topaz_model () : Saved model model from topaz train for topaz extract. Leave this empty to use the default (general) model.
--topaz_radius (-1) : Particle radius (in pix) for topaz extract (default is from particle diameter)
--topaz_args () : Additional arguments to be passed to topaz
--topaz_workers (1) : Number of topaz workers for parallelized training
--topaz_plot (false) : Plot intermediate information for helical picking in topaz (developmental)
--fn_topaz_exe (relion_python_topaz) : Topaz executable (default is using relion_python_topaz from conda install)
```
####  Helix options 
```bash 
--helix (false) : Are the references 2D helical segments? If so, in-plane rotation angles (psi) are estimated for the references.
--helical_tube_kappa_max (0.25) : Factor of maximum curvature relative to that of a circle
--helical_tube_outer_diameter (-1) : Tube diameter in Angstroms
--helical_tube_length_min (-1) : Minimum tube length in Angstroms
--amyloid (false) : Activate specific algorithm for amyloid picking?
--max_diam_local_avg (-1) : Maximum diameter to calculate local average density in Angstroms
```
####  Peak-search options 
```bash 
--threshold (0.25) : Fraction of expected probability ratio in order to consider peaks?
--min_distance (-1) : Minimum distance (in A) between any two particles (default is half the box size)
--max_stddev_noise (-1) : Maximum standard deviation in the noise area to use for picking peaks (default is no maximum)
--min_avg_noise (-999.) : Minimum average in the noise area to use for picking peaks (default is no minimum)
--skip_side (0) : Keep this many extra pixels (apart from particle_size/2) away from the edge of the micrograph 
```
####  Expert options 
```bash 
--verb (1) : Verbosity
--pad (2) : Padding factor for Fourier transforms
--random_seed (1) : Number for the random seed generator
--shrink (1.0) : Reduce micrograph to this fraction size, during correlation calc (saves memory and time)
--Log_max_search (5.) : Maximum diameter in LoG-picking multi-scale approach is this many times the min/max diameter
--extra_pad (0) : Number of pixels for additional padding of the original micrograph
--version : Print RELION version and exit
```
---
### relion_backproject_2d

####  General options 
```bash 
--o : Output directory
--i () : Input file (e.g. run_it023_data.star)
--reextract (false) : Extract particles from the micrographs
--dual_contrast (false) : Perform a dual-contrast reconstruction
--SNR (0.1) : Assumed signal-to-noise ratio
--m (20) : Margin around the particle [Px]
--j (6) : Number of OMP threads
```
####  Display options 
```bash 
--theme (molten) : Select display theme
--list_themes (false) : List available themes and quit
--version : Print RELION version and exit
```
---
### relion_batchrun

####  General options 
```bash 
--i : Input text file with the jobs to execute
--verb (1) : Verbosity
--continue (false) : Only execute those commands that were not done yet
--version : Print RELION version and exit
```
---
### relion_class_ranker

####  General options 
```bash 
--opt () : Input optimiser.star file
--o (./) : Directory name for output files
--ext (ranked) : Extension for root filenames of output optimiser.star and model.star
--auto_select (false) : Perform auto-selection of particles based on below thresholds for the score
--min_score (0.5) : Minimum selected score to be included in class selection
--max_score (999.) : Maximum selected score to be included in class selection
--select_min_nr_particles (-1) : select at least this many particles, regardless of their class score
--select_min_nr_classes (-1) : OR: Select at least this many classes, regardless of their score
--relative_thresholds (false) : If true, interpret the above min and max_scores as fractions of the maximum score of all predicted classes in the input
--fn_sel_parts (particles.star) : Filename for output star file with selected particles
--fn_sel_classavgs (class_averages.star) : Filename for output star file with selected class averages
--fn_root (rank) : rootname for output model.star and optimiser.star files
```
####  Network training options (only used in development!) 
```bash 
--train (false) : Only write output files for training purposes (don't rank classes)
--select (backup_selection.star) : Input class_averages.star from the Selection job or backup_selection.star
--fn_score (job_score.txt) : Input job score file
--cf_file () : Input class feature star file
--only_class_nr (-1) : Class number of the class of interest
--skip_angular_errors (false) : Skip angular error calculation
--do_granularity_features (false) : Calculate granularity features
--save_masks (false) : Save the automatically generated 2D solvent masks for all references
--save_mask_c (false) : Write out images of protein mask circumferences.
--mask_folder_name (protein_solvent_masks) : Folder name for saving all masks.
```
####  Extract subimage for deep convolutional neural network analysis 
```bash 
--extract_subimages (false) : Extract subimages for each class
--nr_subimages (25) : Number of subimage to extract (randonly)
--subimage_boxsize (24) : Boxsize (in pixels) for subimages
--only_do_subimages (false) : Dont do anything else than extracting subimages
```
####  Expert options 
```bash 
--radius_ratio (0.95) : Ratio of inner radius of the interested ring area in proportion to the current circular mask radius
--radius (-1) : Inner radius of the interested ring area to the current circular mask radius
--lowpass (25) : Image lowpass filter threshold for generating binary masks.
--binary_threshold (0.) : Threshold for generating binary masks.
--debug (0) : Debug level
--verb (1) : Verbosity level
--fn_features (features.star) : Filename for output features star file
--write_normalized_features (false) : Also write out normalized feature vectors
--version : Print RELION version and exit
```
---
### relion_convert_star

---
### relion_convert_to_tiff

####  General Options 
```bash 
--i : Input movie to be compressed (an MRC/MRCS file or a list of movies as .star or .lst)
--o (./) : Directory for output TIFF files
--only_do_unfinished (false) : Only process non-converted movies.
--j (1) : Number of threads (useful only for--estimate_gain)
--gain () : Estimated gain map and its reliablity map (read)
--thresh (50) : Number of success needed to consider a pixel reliable
--estimate_gain (false) : Estimate gain
```
####  EER rendering options 
```bash 
--eer_grouping (40) : EER grouping
--eer_upsampling (1) : EER upsampling (1 = physical or 2 = 2x super-resolution)
--short (false) : use unsigned short instead of signed byte for EER rendering
```
####  TIFF writing options 
```bash 
--compression (auto) : compression type (none, auto, deflate (= zip), lzw)
--deflate_level (6) : deflate level. 1 (fast) to 9 (slowest but best compression)
--ignore_error (false) : Don't die on un-expected defect pixels (can be dangerous)
--line_by_line (false) : Use one strip per row
--version : Print RELION version and exit
```
---
### relion_ctf_mask_test

####  General options 
```bash 
--i : Input particle *.star file
--s : Image size
--r : Particle radius
--t : Frequency step
--tw : Filter step width
--o : Output path
--j (1) : Number of threads
--mg (0) : Micrograph index
--version : Print RELION version and exit
```
---
### relion_ctf_refine

####  General options 
```bash 
--i : Input STAR file containing the particles
--f : Input STAR file with the FSC of the reference (usually from PostProcess)
--o : Output directory, e.g. CtfRefine/job041/
--m1 () : Reference map, half 1
--m2 () : Reference map, half 2
--a1 () : Amplitude reference map, half 1
--a2 () : Amplitude reference map, half 2
--angpix_ref (-1) : Pixel size of the reference map
--mask () : Reference mask
--pad (2) : Padding factor
--only_do_unfinished (false) : Skip those steps for which output files already exist.
--ctf_pad (false) : Use larger box to calculate CTF and then downscale to mimic boxing operation in real space
--diag (false) : Write out diagnostic data (slower)
```
####  Defocus fit options 
```bash 
--fit_defocus (false) : Perform refinement of per-particle defocus values?
--fit_mode (fpmfm) : String of 5 characters describing whether to fit the phase shift (1), 
  defocus (2), astigmatism (3), spherical aberration (4) and B-factors (5) 
  per particle ('p'), per micrograph ('m') or to keep them fixed ('f')
  during the per-micrograph CTF refinement.
--max_defocus_iters (100) : Maximum number of iterations for CTF refinement.
--bf0 (false) : Perform brute-force per-particle defocus search (as in RELION 3.0) prior 
  to the per-micrograph CTF refinement.
--bf1 (false) : Perform brute-force defocus search after CTF refinement.
--bf_only (false) : Skip CTF refinement and only perform a brute-force defocus search.
--bf_range (2000.) : Defocus scan range (in A) for brute-force search.
--legacy_astig (false) : Estimate independent per-particle astigmatism (from RELION 3.0)
--kmin_defocus (30.0) : Inner freq. threshold for defocus estimation [Angst]
```
####  B-factor options 
```bash 
--fit_bfacs (false) : Estimate CTF B-factors
--bfac_per_mg (false) : Estimate B-factors per micrograph, instead of per particle
--bfac_min_B (-30) : Minimal allowed B-factor
--bfac_max_B (300) : Maximal allowed B-factor
--bfac_min_scale (0.2) : Minimal allowed scale-factor (essential for outlier rejection)
--kmin_bfac (30.0) : Inner freq. threshold for B-factor estimation [Angst]
```
####  Beam-tilt options 
```bash 
--fit_beamtilt (false) : Perform refinement of beamtilt
--kmin_tilt (20.0) : Inner freq. threshold for beamtilt estimation [Å]
--odd_aberr_max_n (0) : Maximum degree of Zernike polynomials used to fit odd (i.e. antisymmetrical) aberrations
--xr0_t (-1) : Exclusion ring start [Å] - use to exclude dominant frequency (e.g. for helices)
--xr1_t (-1) : Exclusion ring end [Å]
```
####  Symmetric aberrations options 
```bash 
--fit_aberr (false) : Estimate symmetric aberrations
--kmin_aberr (20.0) : Inner freq. threshold for symmetrical aberration estimation [Å]
--even_aberr_max_n (4) : Maximum degree of Zernike polynomials used to fit even (i.e. symmetrical) aberrations
--xr0_a (-1) : Exclusion ring start [Å]
--xr1_a (-1) : Exclusion ring end [Å]
```
####  Anisotropic magnification options 
```bash 
--fit_aniso (false) : Estimate anisotropic magnification
--kmin_mag (20.0) : Inner freq. threshold for anisotropic magnification estimation [Angst]
--keep_astig (false) : Do not translate astigmatism into new coordinates
--part_astig (false) : Allow astigmatism to vary among the particles of a micrograph
```
####  Computational options 
```bash 
--j (1) : Number of (OMP) threads
--min_MG (0) : First micrograph index
--max_MG (-1) : Last micrograph index (default is to process all)
--debug (false) : Write debugging data
--verb (1) : Verbosity
--version : Print RELION version and exit
```
---
### relion_ctf_toolbox

####  Pre-multiply options 
```bash 
--i () : Input STAR file with CTF information
--o () : Output rootname (for multiple images: insert this string before each image's extension)
--apply_orient (false) : Also apply the in-plane rotation and translation to the CTF-premultiplied images
```
####  OR: simulate options 
```bash 
--simulate () : Output name for simulated CTF image
--angpix (1.) : Pixel size (A)
--box (256) : Box size (pix)
--kV (300) : Voltage (kV)
--Q0 (0.1) : Amplitude contrast
--Cs (2.7) : Spherical aberration (mm)
--defU (20000) : Defocus in U-direction (A)
--defV (-1.) : Defocus in V-direction (A, default = defU)
--defAng (0.) : Defocus angle (deg)
--phase_shift (0.) : Phase shift (deg)
```
####  Shared options 
```bash 
--ctf_intact_first_peak (false) : Leave CTFs intact until first peak
--ctf_intact_after_first_peak (false) : Leave CTFs intact after first peak
--ctf_pad (false) : Pre-multiply with a 2x finer-sampled CTF that is then downscaled
--version : Print RELION version and exit
```
---
### relion_delete_blobs_2d


####  General options 
```bash 
--i : Micrograph lists filename
--md : Micrographs directory
--bd : Initial blobs directory
--o : Output filename pattern
--ptc () : Optional particles file for phase flipping
--ring_min (0) : Inner radius of ring to isolate (relative to blob surface)
--ring_max (0) : Outer radius of ring to isolate
--ring_edge_sigma (32) : Smoothness sigma of isolation ring
--c2f (false) : Apply a coarse-to-fine progression instead of initialising with a global pre-fit
--rnd (0) : Roundedness prior
--smt (-1) : Outline average smoothness (negative means full average)
--sig (0) : Weight of initial position
--bin0 (8) : Initial (maximal) binning factor
--bin1 (4) : Final (minimal) binning factor
--nomask (false) : Do not mask out neighbouring blobs
--diag (false) : Write out diagnostic information
--n (12) : Number of frequencies
--th (0.25) : Blob thickness [fraction of radius]
--hp (300) : High-pass sigma [Å, real space]
--max_iters (1000) : Maximum number of iterations
--cth (0.02) : Convergence threshold
--j (6) : Number of OMP threads
```
####  Display options 
```bash 
--theme (molten) : Select display theme
--list_themes (false) : List available themes and quit
--version : Print RELION version and exit
```
---
### relion_demodulate

####  General options 
```bash 
--i : Input STAR file with a list of particles
--out : Output path
--j (6) : Number of OMP threads
--r31 (false) : Write output in Relion-3.1 format
--version : Print RELION version and exit
```
---
### relion_display

####  General options 
```bash 
--i () : Input STAR file, image or stack
--gui (false) : Use this to provide all other parameters through a GUI
--display (rlnImageName) : Metadata label to display
--text_label (EMDL_UNDEFINED) : Metadata label to display text
--table () : Name of the table to read from in the input STAR file
--scale (1) : Relative scale
--black (0) : Pixel value for black (default is auto-contrast)
--white (0) : Pixel value for white (default is auto-contrast)
--sigma_contrast (0) : Set white and black pixel values this many times the image stddev from the mean
--read_whole_stack (false) : Read entire stacks at once (to speed up when many images of each stack are displayed)
--show_fourier_amplitudes (false) : Show amplitudes of 2D Fourier transform?
--show_fourier_phase_angles (false) : Show phase angles of 2D Fourier transforms?
--colour_fire (false) : Show images in black-grey-white-red colour scheme (highlight high signal)?
--colour_ice (false) : Show images in blue-black-grey-white colour scheme (highlight low signal)?
--colour_fire-n-ice (false) : Show images in blue-grey-red colour scheme (highlight high&low signal)?
--colour_rainbow (false) : Show images in cyan-blue-black-red-yellow colour scheme?
--colour_difference (false) : Show images in cyan-blue-black-red-yellow colour scheme (for difference images)?
--colour_bar (false) : Show colourbar image?
--ignore_optics (false) : Ignore information about optics groups in input STAR file?
```
####  Multiviewer options 
```bash 
--col (5) : Number of columns
--apply_orient (false) : Apply the orientation as stored in the input STAR file angles and offsets
--angpix (-1) : Pixel size (in A) to calculate lowpass filter and/or translational offsets 
--ori_scale (1) : Relative scale for viewing individual images in multiviewer
--sort (EMDL_UNDEFINED) : Metadata label to sort images on
--random_sort (false) : Use random order in the sorting
--reverse (false) : Use reverse order (from high to low) in the sorting
--class (false) : Use this to analyse classes in input optimiser.star or model.star file
--regroup (-1) : Number of groups to regroup saved particles from selected classes in (default is no regrouping)
--allow_save (false) : Allow saving of selected particles or class averages
--fn_imgs () : Name of the STAR file in which to save selected images.
--fn_parts () : Name of the STAR file in which to save particles from selected classes.
--max_nr_parts_per_class (-1) : Select maximum this number of particles from each selected classes.
--recenter (false) : Recenter the selected images to the center-of-mass of all positive pixel values. 
--max_nr_images (-1) : Only show this many images (default is show all)
```
####  Picking options 
```bash 
--pick (false) : Pick coordinates in input image
--pick_start_end (false) : Pick start-end coordinates in input image
--coords () : STAR file with picked particle coordinates
--coord_scale (1.0) : Scale particle coordinates before display
--particle_radius (100) : Particle radius in pixels
--topaz_denoise (false) : Use Topaz denoising before picking (on GPU 0)
--bash_exe (/bin/bash) : Name of bash shell executable
--lowpass (0) : Lowpass filter (in A) to filter micrograph before displaying
--highpass (0) : Highpass filter (in A) to filter micrograph before displaying
--minimum_pick_fom (-9999.) : Minimum value for rlnAutopickFigureOfMerit to display picks
--color_star () : STAR file with a column for red-blue coloring (a subset of) the particles
--color_label () : MetaDataLabel to color particles on (e.g. rlnParticleSelectZScore)
--blue (1.) : Value of the blue color
--red (0.) : Value of the red color
--verb (1) : Verbosity
--version : Print RELION version and exit
```
---
### relion_estimate_gain

####  Options 
```bash 
--i : Input movie STAR file
--o : Output file name
--j (1) : Number of threads
--max_frames (-1) : Target number of frames to average (rounded to movies; -1 means use all)
--random (false) : Randomise the order of input movies before taking subset
--dont_invert (false) : Don't take the inverse but simply writes the sum
--eer_upsampling (2) : EER upsampling (1 = physical or 2 = 2x super-resolution)
--version : Print RELION version and exit
```
---
### relion_external_reconstruct

---
### relion_filament_selection
```
usage: relion_filament_selection [-h] -i INPUT -o OUTPUT [-t THRESHOLD]
   [-c CLASSMIN]
   [--pipeline_control PIPELINE_CONTROL]

options:
  -h,--helpshow this help message and exit
  -i INPUT,--input INPUT
  Input optimiser.star from 2D classification
  -o OUTPUT,--output OUTPUT
  Output directory
  -t THRESHOLD,--threshold THRESHOLD
  Dendrogram threshold
  -c CLASSMIN,--classmin CLASSMIN
  Minimum number of particles per class; write out star
  files if positive
--pipeline_control PIPELINE_CONTROL
  Needed to work together with relion GUI
```
---
### relion_find_tiltpairs

####  General Options 
```bash 
--u : STAR file with the untilted xy-coordinates
--t : STAR file with the untilted xy-coordinates
--size : Largest dimension of the micrograph (in pixels), e.g. 4096
--acc : Allowed accuracy (in pixels), e.g. half the particle diameter
--dim (200) : Dimension of boxed particles (for EMAN .box files in pixels)
--tilt (99999.) : Fix tilt angle (in degrees)
--rot (99999.) : Fix direction of the tilt axis (in degrees), 0 = along y, 90 = along x
--dont_opt (false) : Skip optimization of the transformation matrix
```
####  Specified tilt axis and translational search ranges 
```bash 
--tilt0 (0.) : Minimum tilt angle (in degrees)
--tiltF (99999.) : Maximum tilt angle (in degrees)
--tiltStep (1.) : Tilt angle step size (in degrees)
--rot0 (0.) : Minimum rot angle (in degrees)
--rotF (99999.) : Maximum rot angle (in degrees)
--rotStep (1.) : Rot angle step size (in degrees)
--x0 (-99999) : Minimum X offset (pixels)
--xF (99999) : Maximum X offset (pixels)
--xStep (-1) : X offset step size (pixels)
--y0 (-99999) : Minimum Y offset (pixels)
--yF (99999) : Maximum Y offset (pixels)
--yStep (-1) : Y offset step size (pixels)
--version : Print RELION version and exit
```
---
### relion_flex_analyse

####  General options 
```bash 
--data () : The _data.star file with the orientations to be analysed
--model () :  The corresponding _model.star file with the refined model
--bodies () : The corresponding star file with the definition of the bodies
--o (analyse) : Output rootname
```
####  3D model options 
```bash 
--3dmodels (false) : Generate a 3D model for each experimental particles
--size_3dmodels (-1) : Output size of the 3D models (default is same as input particles)
```
####  PCA options 
```bash 
--PCA_orient (false) : Perform a principal components analysis on the multibody orientations
--do_maps (false) : Generate maps along the principal components
--k (-1) : Number of principal components to generate maps for
--v (0.75) : Or use as many principal components to explain this fraction of variance (&lt;0,1])
--maps_per_movie (10) : Number of maps to use for the movie of each principal component
--bins (100) : Number of bins in histograms of the eigenvalues for each principal component
--select_eigenvalue (-1) : Output a selection particle.star file based on eigenvalues along this eigenvector
--select_eigenvalue_min (-99999.) : Minimum for eigenvalue to include particles in selection output star file
--select_eigenvalue_max (99999.) : Maximum for eigenvalue to include particles in selection output star file
--write_pca_projections (false) : Write out a text file with all PCA projections for all particles
--verb (1) : Verbosity
--version : Print RELION version and exit
```
---
### relion_flex_analyse_mpi

####  General options 
```bash 
--data () : The _data.star file with the orientations to be analysed
--model () :  The corresponding _model.star file with the refined model
--bodies () : The corresponding star file with the definition of the bodies
--o (analyse) : Output rootname
```
####  3D model options 
```bash 
--3dmodels (false) : Generate a 3D model for each experimental particles
--size_3dmodels (-1) : Output size of the 3D models (default is same as input particles)
```
####  PCA options 
```bash 
--PCA_orient (false) : Perform a principal components analysis on the multibody orientations
--do_maps (false) : Generate maps along the principal components
--k (-1) : Number of principal components to generate maps for
--v (0.75) : Or use as many principal components to explain this fraction of variance (&lt;0,1])
--maps_per_movie (10) : Number of maps to use for the movie of each principal component
--bins (100) : Number of bins in histograms of the eigenvalues for each principal component
--select_eigenvalue (-1) : Output a selection particle.star file based on eigenvalues along this eigenvector
--select_eigenvalue_min (-99999.) : Minimum for eigenvalue to include particles in selection output star file
--select_eigenvalue_max (99999.) : Maximum for eigenvalue to include particles in selection output star file
--write_pca_projections (false) : Write out a text file with all PCA projections for all particles
--verb (1) : Verbosity
--version : Print RELION version and exit
```
---
### relion_helix_inimodel2d

####  General options 
```bash 
--o () : Output rootname
--i () :  STAR file with the input images and orientation parameters
```
####  Parameters 
```bash 
--crossover_distance () : Distance in Angstroms between 2 cross-overs
--iter (10) : Maximum number of iterations to perform
--K (1) : Number of classes
--angpix (-1) : Pixel size in Angstroms (default take from STAR file)
--maxres (-1) : Limit calculations to approximately this resolution in Angstroms
--search_shift (0) : How many Angstroms to search translations perpendicular to helical axis?
--search_angle (0) : How many degrees to search in-plane rotations?
--step_angle (1) : The step size (in degrees) of the rotational searches
--iniref () : An initial model to starting optimisation path
--sym (1) : Order of symmetry in the 2D xy-slice?
--smear (0) : Smear out each image along X to ensure continuity
--random_seed (-1) : Random seed (default is with clock)
--search_size (5) : Search this many pixels up/down of the target downscaled size to fit best crossover distance
--mask_diameter (-1) : The diameter (A) of a mask to be aplpied to the 2D reconstruction
--j (1) : Number of (openMP) threads
--only_make_3d (false) : Take the iniref image, and create a 3D model from that without any alignment of the input images
--version : Print RELION version and exit
```

---
### relion_image_handler

####  General options 
```bash 
--i : Input STAR file, image (.mrc) or movie/stack (.mrcs)
--o () : Output name (for STAR-input: insert this string before each image's extension)
--float16 (false) : Write in half-precision 16 bit floating point numbers (MRC mode 12), instead of 32 bit (MRC mode 0).
####  image-by-constant operations 
```bash 
--multiply_constant (1) : Multiply the image(s) pixel values by this constant
--divide_constant (1) : Divide the image(s) pixel values by this constant
--add_constant (0.) : Add this constant to the image(s) pixel values
--subtract_constant (0.) : Subtract this constant from the image(s) pixel values
--threshold_above (999.) : Set all values higher than this value to this value
--threshold_below (-999.) : Set all values lower than this value to this value
```
####  image-by-image operations 
```bash 
--multiply () : Multiply input image(s) by the pixel values in this image
--divide () : Divide input image(s) by the pixel values in this image
--add () : Add the pixel values in this image to the input image(s) 
--subtract () : Subtract the pixel values in this image to the input image(s) 
--fsc () : Calculate FSC curve of the input image with this image
--power (false) : Calculate power spectrum (|F|^2) of the input image
--guinier (false) : Calculate Guinier plot and determine B-factor of the input image
--guinier_minres (10.) : Lowest resolution (in A) to include in fitting of the B-factor
--guinier_maxres (0.01) : Highest resolution (in A) to include in fitting of the B-factor
--adjust_power () : Adjust the power spectrum of the input image to be the same as this image 
--fourier_filter () : Multiply the Fourier transform of the input image(s) with this one image
```
####  additional subtract options 
```bash 
--optimise_scale_subtract (false) : Optimise scale between maps before subtraction?
--optimise_bfactor_subtract (0.) : Search range for relative B-factor for subtraction (in A^2)
--mask_optimise_subtract () : Use only voxels in this mask to optimise scale for subtraction
```
####  per-image operations 
```bash 
--stats (false) : Calculate per-image statistics?
--com (false) : Calculate center of mass?
--bfactor (0.) : Apply a B-factor (in A^2)
--lowpass (-1.) : Low-pass filter frequency (in A)
--highpass (-1.) : High-pass filter frequency (in A)
--directional () : Directionality of low-pass filter frequency ('X', 'Y' or 'Z', default non-directional)
--LoG (-1.) : Diameter for optimal response of Laplacian of Gaussian filter (in A)
--angpix (-1) : Pixel size (in A)
--rescale_angpix (-1.) : Scale input image(s) to this new pixel size (in A)
--force_header_angpix (-1.) : Change the pixel size in the header (in A). Without--rescale_angpix, the image is not scaled.
--new_box (-1) : Resize the image(s) to this new box size (in pixel) 
--filter_edge_width (2) : Width of the raised cosine on the low/high-pass filter edge (in resolution shells)
--flipX (false) : Flip (mirror) a 2D image or 3D map in the X-direction?
--flipY (false) : Flip (mirror) a 2D image or 3D map in the Y-direction?
--flipZ (false) : Flip (mirror) a 3D map in the Z-direction?
--invert_hand (false) : Invert hand by flipping X? Similar to flipX, but preserves the symmetry origin. Edge pixels are wrapped around.
--shift_com (false) : Shift image(s) to their center-of-mass (only on positive pixel values)
--shift_x (0.) : Shift images this many pixels in the X-direction
--shift_y (0.) : Shift images this many pixels in the Y-direction
--shift_z (0.) : Shift images this many pixels in the Z-direction
--avg_ampl (false) : Calculate average amplitude spectrum for all images?
--avg_ampl2 (false) : Calculate average amplitude spectrum for all images?
--avg_ampl2_ali (false) : Calculate average amplitude spectrum for all aligned images?
--average (false) : Calculate average of all images (without alignment)
--correct_avg_ampl () : Correct all images with this average amplitude spectrum
--minr_ampl_corr (0) : Minimum radius (in Fourier pixels) to apply average amplitudes
--remove_nan (false) : Replace non-numerical values (NaN, inf, etc) in the image(s)
--replace_nan (0) : Replace non-numerical values (NaN, inf, etc) with this value
--phase_randomise (-1) : Randomise phases beyond this resolution (in Angstroms)
```
####  3D operations 
```bash 
--sym () : Symmetrise 3D map with this point group (e.g. D6)
```
####  2D-micrograph (or movie) operations 
```bash 
--flipXY (false) : Flip the image(s) in the XY direction?
--flipmXY (false) : Flip the image(s) in the -XY direction?
--add_edge (false) : Add a barcode-like edge to the micrograph/movie frames?
--edge_x0 (0) : Pixel column to be used for the left edge
--edge_y0 (0) : Pixel row to be used for the top edge
--edge_xF (4095) : Pixel column to be used for the right edge
--edge_yF (4095) : Pixel row to be used for the bottom edge
```
####  Movie-frame averaging options 
```bash 
--avg_bin (-1) : Width (in frames) for binning average, i.e. of every so-many frames
--avg_first (-1) : First frame to include in averaging
--avg_last (-1) : Last frame to include in averaging
--average_all_movie_frames (false) : Average all movie frames of all movies in the input STAR file.
```
####  PNG options 
```bash 
--black (0) : Pixel value for black (default is auto-contrast)
--white (0) : Pixel value for white (default is auto-contrast)
--sigma_contrast (0) : Set white and black pixel values this many times the image stddev from the mean
--colour_fire (false) : Show images in black-grey-white-red colour scheme (highlight high signal)?
--colour_ice (false) : Show images in blue-black-grey-white colour scheme (highlight low signal)?
--colour_fire-n-ice (false) : Show images in blue-grey-red colour scheme (highlight high&low signal)?
--colour_rainbow (false) : Show images in cyan-blue-black-red-yellow colour scheme?
--colour_difference (false) : Show images in cyan-blue-black-red-yellow colour scheme (for difference images)?
--version : Print RELION version and exit
```
---
### relion_import

####  General options 
```bash 
--i : Input (wildcard) filename
--odir : Output directory (e.g. "Import/job001/"
--ofile : Output file name (e.g. "movies.star"
--do_movies (false) : Import movies
--do_micrographs (false) : Import micrographs
--do_coordinates (false) : Import coordinates
--do_halfmaps (false) : Import unfiltered half maps
--do_particles (false) : Import particle STAR files
--particles_optics_group_name () : Rename optics group for all imported particles (e.g. "opticsGroupLMBjan2019"
--do_other (false) : Import anything else
```
####  Specific options for movies or micrographs 
```bash 
--optics_group_name (opticsGroup1) : Name for this optics group
--optics_group_mtf () : Name for this optics group's MTF
--angpix (1.0) : Pixel size (Angstrom)
--kV (300) : Voltage (kV)
--Cs (2.7) : Spherical aberration (mm)
--Q0 (0.1) : Amplitude contrast
--beamtilt_x (0.0) : Beam tilt (X; mrad)
--beamtilt_y (0.0) : Beam tilt (Y; mrad)
--continue (false) : Continue and old run, add more files to the same import directory
--version : Print RELION version and exit
```
---
### relion_it.py

---
### relion_localsym

####  Show usage 
```bash 
--function_help (false) : Show usage for the selected function (JUN 30, 2017)
```
####  Options 
```bash 
--apply (false) : Apply local symmetry to a 3D cryo-EM density map
--duplicate (false) : Duplicate subunits/masks according to local symmetry operators
--search (false) : Local searches of local symmetry operators
--transform (false) : Transform a map according to three Euler angles and XYZ translations
--txt2rln (false) : Convert operators from DM to RELION STAR format
--debug (false) : (DEBUG ONLY)
```
####  Parameters (alphabetically ordered) 
```bash 
--angpix (1.) : Pixel size (in Angstroms) of input image
--ang_range (0.) : Angular search range of operators (in degrees), overwrite rot-tilt-psi ranges if set to positive
--ang_rot_range (0.) : Angular (rot) search range of operators (in degrees)
--ang_tilt_range (0.) : Angular (tilt) search range of operators (in degrees)
--ang_psi_range (0.) : Angular (psi) search range of operators (in degrees)
--ang_step (1.) : Angular search step of operators (in degrees)
--bin (-1.) : Binning factor (&lt;= 1 means no binning)
--ini_threshold (0.01) : Initial threshold for binarization
--i_map () : Input 3D unsymmetrised map
--i_mask_info (maskinfo.txt) : Input file with mask filenames and rotational / translational operators (for local searches)
--i_op_mask_info (None) : Input file with mask filenames for all operators (for global searches)
--n (2) : Create this number of masks according to the input density map
--offset_range (0.) : Translational search range of operators (in Angstroms), overwrite x-y-z ranges if set to positive
--offset_x_range (0.) : Translational (x) search range of operators (in Angstroms)
--offset_y_range (0.) : Translational (y) search range of operators (in Angstroms)
--offset_z_range (0.) : Translational (z) search range of operators (in Angstroms)
--offset_step (1.) : Translational search step of operators (in Angstroms)
--o_map () : Output 3D symmetrised map
--o_mask_info (maskinfo_refined.txt) : Output file with mask filenames and rotational / translational operators
--psi (0.) : Third Euler angle (psi, in degrees)
--rot (0.) : First Euler angle (rot, in degrees)
--sphere_percentage (-1.) : Diameter of spherical mask divided by the box size (&lt; 0.99)
--tilt (0.) : Second Euler angle (tilt, in degrees)
--xoff (0.) : X-offset (in Angstroms)
--yoff (0.) : Y-offset (in Angstroms)
--zoff (0.) : Z-offset (in Angstroms)
--verb (false) : Verbose output?
```
####  Parameters (expert options - alphabetically ordered) 
```bash 
--i_mask (mask.mrc) : (DEBUG) Input mask
--i_mask_info_parsed_ext (parsed) : Extension of parsed input file with mask filenames and rotational / translational operators
--use_healpix (false) : Use Healpix for angular samplings?
--width (5.) : Width of cosine soft edge (in pixels)
--version : Print RELION version and exit
```
---
### relion_localsym_mpi

####  Show usage 
```bash 
--function_help (false) : Show usage for the selected function (JUN 30, 2017)
```
####  Options 
```bash 
--apply (false) : Apply local symmetry to a 3D cryo-EM density map
--duplicate (false) : Duplicate subunits/masks according to local symmetry operators
--search (false) : Local searches of local symmetry operators
--transform (false) : Transform a map according to three Euler angles and XYZ translations
--txt2rln (false) : Convert operators from DM to RELION STAR format
--debug (false) : (DEBUG ONLY)
```

####  Parameters (alphabetically ordered) 
```bash 
--angpix (1.) : Pixel size (in Angstroms) of input image
--ang_range (0.) : Angular search range of operators (in degrees), overwrite rot-tilt-psi ranges if set to positive
--ang_rot_range (0.) : Angular (rot) search range of operators (in degrees)
--ang_tilt_range (0.) : Angular (tilt) search range of operators (in degrees)
--ang_psi_range (0.) : Angular (psi) search range of operators (in degrees)
--ang_step (1.) : Angular search step of operators (in degrees)
--bin (-1.) : Binning factor (&lt;= 1 means no binning)
--ini_threshold (0.01) : Initial threshold for binarization
--i_map () : Input 3D unsymmetrised map
--i_mask_info (maskinfo.txt) : Input file with mask filenames and rotational / translational operators (for local searches)
--i_op_mask_info (None) : Input file with mask filenames for all operators (for global searches)
--n (2) : Create this number of masks according to the input density map
--offset_range (0.) : Translational search range of operators (in Angstroms), overwrite x-y-z ranges if set to positive
--offset_x_range (0.) : Translational (x) search range of operators (in Angstroms)
--offset_y_range (0.) : Translational (y) search range of operators (in Angstroms)
--offset_z_range (0.) : Translational (z) search range of operators (in Angstroms)
--offset_step (1.) : Translational search step of operators (in Angstroms)
--o_map () : Output 3D symmetrised map
--o_mask_info (maskinfo_refined.txt) : Output file with mask filenames and rotational / translational operators
--psi (0.) : Third Euler angle (psi, in degrees)
--rot (0.) : First Euler angle (rot, in degrees)
--sphere_percentage (-1.) : Diameter of spherical mask divided by the box size (&lt; 0.99)
--tilt (0.) : Second Euler angle (tilt, in degrees)
--xoff (0.) : X-offset (in Angstroms)
--yoff (0.) : Y-offset (in Angstroms)
--zoff (0.) : Z-offset (in Angstroms)
--verb (false) : Verbose output?
```
####  Parameters (expert options - alphabetically ordered) 
```bash 
--i_mask (mask.mrc) : (DEBUG) Input mask
--i_mask_info_parsed_ext (parsed) : Extension of parsed input file with mask filenames and rotational / translational operators
--use_healpix (false) : Use Healpix for angular samplings?
--width (5.) : Width of cosine soft edge (in pixels)
--version : Print RELION version and exit
```
---
### relion_manualpick

####  General options 
```bash 
--i : Micrograph STAR file OR filenames from which to pick particles, e.g. "Micrographs/*.mrc"
--particle_diameter : Diameter of the circles that will be drawn around each picked particle (in Angstroms)
--odir (ManualPick/) : Output directory for coordinate files (default is to store next to micrographs)
--selection (micrographs_selected.star) : STAR file with selected micrographs
--pickname (manualpick) : Rootname for the picked coordinate files
--angpix (-1.) : Pixel size in Angstroms
--coord_scale (1.0) : Scale coordinates before display
--pick_start_end (false) : Pick start-end coordinates of helices
--allow_save (false) : Allow saving of the selected micrographs
--fast_save (false) : Save a default selection of all micrographs immediately
--open_simultaneous (10) : Open this many of the next micrographs simultaneously when pressing CTRL and a Pick button
```
####  Displaying options 
```bash 
--scale (1) : Relative scale for the micrograph display
--black (0) : Pixel value for black (default is auto-contrast)
--white (0) : Pixel value for white (default is auto-contrast)
--sigma_contrast (0) : Set white and black pixel values this many times the image stddev from the mean (default is auto-contrast)
--lowpass (0) : Lowpass filter in Angstroms for the micrograph (0 for no filtering)
--highpass (0) : Highpass filter in Angstroms for the micrograph (0 for no filtering)
--topaz_denoise (false) : Or instead of filtering, use Topaz denoising before picking (on GPU 0)
--ctf_scale (1) : Relative scale for the CTF-image display
--ctf_sigma_contrast (3) : Sigma-contrast for the CTF-image display
--minimum_pick_fom (-9999.) : Minimum value for rlnAutopickFigureOfMerit to display picks
--color_star () : STAR file with a column for red-blue coloring (a subset of) the particles
--color_label () : MetaDataLabel to color particles on (e.g. rlnParticleSelectZScore)
--blue (1.) : Value of the blue color
--red (0.) : Value of the red color
--version : Print RELION version and exit
```
---
### relion_mask_create

####  Mask creation options 
```bash 
--i () : Input map to use for thresholding to generate initial binary mask
--o (mask.mrc) : Output mask
--and () : Pixels in the initial mask will be one if the input AND this map are above the--ini_threshold value
--or () : Pixels in the initial mask will be one if the input OR this map are above the--ini_threshold value
--and_not () : Pixels in the initial mask will be one if the input is above the--ini_threshold AND this map is below it
--or_not () : Pixels in the initial mask will be one if the input is above the--ini_threshold OR this map is below it
--ini_threshold (0.01) : Initial threshold for binarization
--extend_inimask (0) : Extend initial binary mask this number of pixels
--width_soft_edge (0) : Width (in pixels) of the additional soft edge on the binary mask
--invert (false) : Invert the final mask
--helix (false) : Generate a mask for 3D helix
--lowpass (-1) : Lowpass filter (in Angstroms) for the input map, prior to binarization (default is none)
--angpix (-1) : Pixel size (in Angstroms) for the lowpass filter
--z_percentage (0.3) : This box length along the center of Z axis contains good information of the helix
--j (1) : Number of threads
```
####  De novo mask creation 
```bash 
--denovo (false) : Create a mask de novo
--box_size (-1) : The box size of the mask in pixels
--inner_radius (0) : Inner radius of the masked region in pixels
--outer_radius (99999) : Outer radius of the mask region in pixels
--center_x (0) : X coordinate of the center of the mask in pixels
--center_y (0) : Y coordinate of the center of the mask in pixels
--center_z (0) : Z coordinate of the center of the mask in pixels
--version : Print RELION version and exit
```
---
### relion_merge_particles

```bash
No help
```

---
### relion_motion_refine | relion_motion_refine_mpi

####  General options 
```bash 
--i : Input STAR file
--o : Output directory, e.g. MotionFit/job041/
--f : Input STAR file with the FSC of the reference (usually from PostProcess)
--m1 () : Reference map, half 1
--m2 () : Reference map, half 2
--a1 () : Amplitude reference map, half 1
--a2 () : Amplitude reference map, half 2
--angpix_ref (-1) : Pixel size of the reference map
--mask () : Reference mask
--pad (2) : Padding factor
--first_frame (1) : First move frame to process
--last_frame (-1) : Last movie frame to process (default is all)
--only_do_unfinished (false) : Skip those steps for which output files already exist.
--verb (1) : Verbosity
```
####  Motion fit options (basic) 
```bash 
--fdose (-1) : Electron dose per frame (in e^-/A^2)
--s_vel (0.5) : Velocity sigma [Angst/dose]
--s_div (5000.0) : Divergence sigma [Angst]
--s_acc (2.0) : Acceleration sigma [Angst/dose]
--params_file () : File containing s_vel, s_div and s_acc (overrides command line parameters)
--only_group (-1) : Only align micrographs containing particles from this optics group (negative means off)
--diag (false) : Write out diagnostic data
```
####  Motion fit options (advanced) 
```bash 
--cc_pad (1.0) : Cross-correlation Fourier-padding
--dmg_a ( 3.40) : Damage model, parameter a
--dmg_b (-1.06) :   b
--dmg_c (-0.54) :   c
--max_iters (10000) : Maximum number of iterations
--eps (1e-5) : Terminate optimization after gradient length falls below this value
--no_whiten (false) : Do not whiten the noise spectrum
--unreg_glob (false) : Do not regularize global component of motion
--glob_off (false) : Compute initial per-particle offsets
--glob_off_max (10) : Maximum per-particle offset range [Pixels]
--absolute_params (false) : Do not scale input motion parameters by dose
--debug_opt (false) : Write optimization debugging info
--gi (false) : Initialize with global trajectories instead of loading them from metadata file
--sq_exp_ker (false) : Use a square-exponential kernel instead of an exponential one
--max_ed (-1) : Maximum number of eigendeformations
--out_cut (false) : Do not consider frequencies beyond the 0.143-FSC threshold for alignment
```
####  Parameter estimation 
```bash 
--params2 (false) : Estimate 2 parameters instead of motion
--params3 (false) : Estimate 3 parameters instead of motion
--align_frac (0.5) : Fraction of pixels to be used for alignment
--eval_frac (0.5) : Fraction of pixels to be used for evaluation
--min_p (1000) : Minimum number of particles on which to estimate the parameters
--par_group (-1) : Estimate parameters for this optics group only (negative means all)
--s_vel_0 (0.6) : Initial s_vel
--s_div_0 (10000) : Initial s_div
--s_acc_0 (3) : Initial s_acc
--in_step (3000) : Initial step size in s_div
--conv (30) : Abort when simplex diameter falls below this
--par_iters (100) : Max. number of iterations
--mot_range (50) : Limit allowed motion range [Px]
--seed (23) : Random seed for micrograph selection
```
####  Combine frames options 
```bash 
--combine_frames (false) : Combine movie frames into polished particles.
--float16 (false) : Write in half-precision 16 bit floating point numbers (MRC mode 12), instead of 32 bit (MRC mode 0).
--scale (-1) : Re-scale the particles to this size (by default read from particles star file)
--window (-1) : Re-window the particles to this size (in movie-pixels; by default read from particles star file)
--crop (-1) : Crop the scaled particles to this size after CTF pre-multiplication
--ctf_multiply (false) : Premultiply by CTF.
--bfac_minfreq (20) : Min. frequency used in B-factor fit [Angst]
--bfac_maxfreq (-1) : Max. frequency used in B-factor fit [Angst]
--bfactors () : A .star file with external B/k-factors
--diag_bfactor (false) : Write out B/k-factor diagnostic data
--suffix () : Add this suffix to shiny MRCS and STAR files
--recenter (false) : Re-center particle according to rlnOriginX/Y in--reextract_data_star STAR file
--recenter_x (0.) : X-coordinate (in pixel inside the reference) to recenter re-extracted data on
--recenter_y (0.) : Y-coordinate (in pixel inside the reference) to recenter re-extracted data on
--recenter_z (0.) : Z-coordinate (in pixel inside the reference) to recenter re-extracted data on
```
####  Computational options 
```bash 
--j (1) : Number of (OMP) threads
--B_parts (-1) : Number of particles used for B-factor estimation (negative means all)
--min_MG (0) : First micrograph index
--max_MG (-1) : Last micrograph index (default is to process all)
--sbs (false) : Load movies slice-by-slice to save memory (slower)
```
####  Expert options 
```bash 
--corr_mic : List of uncorrected micrographs (e.g. corrected_micrographs.star)
--find_shortest (false) : Load only as many frames as are present in all movies.
--debug (false) : Write debugging data
--mps (-1) : Pixel size of input movies (Angst/pix)
--cps (-1) : Pixel size of particle coordinates in star-file (Angst/pix)
--hot (-1) : Clip hot pixels to this max. value (-1 = off, TIFF only)
--debug_mov (false) : Write debugging data for movie loading
--mov_toReplace () : Replace this string in micrograph names...
--mov_replaceBy () : ..by this one
--eer_upsampling (-1) : EER upsampling (1 = physical or 2 = 2x super-resolution)
--eer_grouping (-1) : EER grouping
--version : Print RELION version and exit
```
---
### relion_movie_reconstruct

####  General options 
```bash 
--i () : Input STAR file with the projection images and their orientations
--o (relion.mrc) : Name for output reconstruction
--sym (c1) : Symmetry group
--maxres (-1) : Maximum resolution (in Angstrom) to consider in Fourier space (default Nyquist)
--pad (2) : Padding factor
--corr_mic () : Motion correction STAR file
--traj_path () : Trajectory path prefix
--movie_angpix (-1) : Pixel size in the movie
--coord_angpix (-1) : Pixel size of particle coordinates
--frame (1) : Movie frame to reconstruct (1-indexed)
--eer_grouping (-1) : Override EER grouping (--frame is in this new grouping)
--window (-1) : Box size to extract from raw movies
--scale (-1) : Box size after down-sampling
--j (2) : Number of threads (1 or 2)
```
####  CTF options 
```bash 
--ctf (false) : Apply CTF correction
--ctf_intact_first_peak (false) : Leave CTFs intact until first peak
--ctf_phase_flipped (false) : Images have been phase flipped
--only_flip_phases (false) : Do not correct CTF-amplitudes, only flip phases
####  Ewald-sphere correction options 
```bash 
--ewald (false) : Correct for Ewald-sphere curvature (developmental)
--mask_diameter (-1.) : Diameter (in A) of mask for Ewald-sphere curvature correction
--width_mask_edge (3) : Width (in pixels) of the soft edge on the mask
--reverse_curvature (false) : Try curvature the other way around
--sectors (2) : Number of sectors for Ewald sphere correction
--skip_mask (false) : Do not apply real space mask during Ewald sphere correction
--skip_weighting (false) : Do not apply weighting during Ewald sphere correction
```
####  Helical options 
```bash 
--nr_helical_asu (1) : Number of helical asymmetrical units
--helical_rise (0.) : Helical rise (in Angstroms)
--helical_twist (0.) : Helical twist (in degrees, + for right-handedness)
```
####  Expert options 
```bash 
--NN (false) : Use nearest-neighbour instead of linear interpolation before gridding correction
--blob_r (1.9) : Radius of blob for gridding interpolation
--blob_m (0) : Order of blob for gridding interpolation
--blob_a (15) : Alpha-value of blob for gridding interpolation
--iter (10) : Number of gridding-correction iterations
--skip_gridding (false) : Skip gridding part of the reconstruction
--no_barcode (false) : Don't apply barcode-like extension when extracting outside a micrograph
--verb (1) : Verbosity
--version : Print RELION version and exit
```
---
### relion_mrc2vtk

---
### relion_particle_reposition

####  Options 
```bash 
--i : Input STAR file with rlnMicrographName's 
--opt : Optimiser STAR file with the 2D classes or 3D maps to be repositioned
--o () : Output rootname, to be added to input micrograph names
--odir () : Output directory (default is same as input micrographs directory
--data () : Data STAR file with selected particles (default is to use all particles)
--background (0.1) : The fraction of micrograph background noise in the output micrograph
--invert (false) : Invert the contrast in the references?
--ctf (false) : Apply CTF for each particle to the references?
--norm_radius (-1) : Radius of the circle used for background normalisation (in pixels)
--subtract (false) : Subtract repositioned micrographs from the input ones?
--version : Print RELION version and exit
```
---
### relion_particle_select

####  General options 
```bash 
--i : Input STAR file containing the source particles
--i_ref : Input STAR file containing reference particles
--angles (false) : Copy particle viewing angles from reference
--offsets (false) : Copy particle offsets from reference
--o (selected.star) : Output path
--version : Print RELION version and exit
```
---
### relion_particle_subtract

####  General options 
```bash 
--i () : Name of optimiser.star file from refinement/classification to use for subtraction
--o (Subtract/) : Output directory name
--mask () : Name of the 3D mask with all density that should be kept, i.e. not subtracted
--data () : Name of particle STAR file, in case not all particles from optimiser are to be used
--ignore_class (false) : Ignore the rlnClassNumber column in the particle STAR file.
--revert () : Name of particle STAR file to revert. When this is provided, all other options are ignored.
--ssnr (false) : Don't subtract, only calculate average spectral SNR in the images
--float16 (false) : Write in half-precision 16 bit floating point numbers (MRC mode 12), instead of 32 bit (MRC mode 0).
```
####  Centering options 
```bash 
--recenter_on_mask (false) : Use this flag to center the subtracted particles on projections of the centre-of-mass of the input mask
--center_x (9999) : X-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
--center_y (9999) : Y-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
--center_z (9999) : Z-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
--new_box (-1) : Output size of the subtracted particles
--version : Print RELION version and exit
```
---
### relion_particle_subtract_mpi

####  General options 
```bash 
--i () : Name of optimiser.star file from refinement/classification to use for subtraction
--o (Subtract/) : Output directory name
--mask () : Name of the 3D mask with all density that should be kept, i.e. not subtracted
--data () : Name of particle STAR file, in case not all particles from optimiser are to be used
--ignore_class (false) : Ignore the rlnClassNumber column in the particle STAR file.
--revert () : Name of particle STAR file to revert. When this is provided, all other options are ignored.
--ssnr (false) : Don't subtract, only calculate average spectral SNR in the images
--float16 (false) : Write in half-precision 16 bit floating point numbers (MRC mode 12), instead of 32 bit (MRC mode 0).
```
####  Centering options 
```bash 
--recenter_on_mask (false) : Use this flag to center the subtracted particles on projections of the centre-of-mass of the input mask
--center_x (9999) : X-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
--center_y (9999) : Y-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
--center_z (9999) : Z-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
--new_box (-1) : Output size of the subtracted particles
--version : Print RELION version and exit
```
---
### relion_particle_symmetry_expand

####  Options 
```bash 
--i : Input particle STAR file
--o (expanded.star) : Output expanded particle STAR file
--sym (C1) : Symmetry point group
```
####  Helix 
```bash 
--helix (false) : Do helical symmetry expansion
--twist (0.) : Helical twist (deg)
--rise (0.) : Helical rise (A)
--angpix (1.) : Pixel size (A)
--asu (1) : Number of asymmetrical units to expand
--frac_sampling (1) : Number of samplings in between a single asymmetrical unit
--frac_range (0.5) : Range of the rise [-0.5, 0.5&gt; to be sampled
--ignore_optics (false) : Provide this option for relion-3.0 functionality, without optics groups
--version : Print RELION version and exit
```
---
### relion_pipeliner

####  Check job completion options 
```bash 
--check_job_completion (false) : Use this flag to only check whether running jobs have completed
```
####  Add scheduled jobs options 
```bash 
--addJobFromStar () : Add a job with the type and options as in this job.star to the pipeline
--addJob () : Add a job of this type to the pipeline
--addJobOptions () : Options for this job (either through--addJobFromStar or--addJob)
--setJobAlias () : Set an alias to this job
```
####  Run scheduled jobs options 
```bash 
--RunJobs () : Run these jobs
--schedule () : Name of the scheduler for running the scheduled jobs
--repeat (1) : Run the scheduled jobs this many times
--min_wait (0) : Wait at least this many minutes between each repeat
--min_wait_before (0) : Wait this many minutes before starting the running the first job
--sec_wait_after (10) : Wait this many seconds after a process finishes (workaround for slow IO)
```
####  Edit jobs 
```bash 
--editJob () : Star file of a job to be edited
--editJobOut () : Output star file of the edited job (default is to overwrite input)
--editOption () : The name of the joboption to be edited. This needs to be present in the input star file.
--editValue () : The value of the joboption to be set.
```
####  Expert options 
```bash 
--pipeline (default) : Name of the pipeline
--gentle_clean (-1) : Gentle clean this job
--harsh_clean (-1) : Harsh clean this job
--version : Print RELION version and exit
```
---
### relion_plot_delocalisation

####  General options 
```bash 
--i : Input particle *.star file
--rad : Particle radius [Å]
--o : Output path
--og (1) : Optics group
--max_freq (-1) : Max. image frequency [Å] (default is Nyquist)
--min_freq (0) : Min. image frequency [Å]
--name () : Name of dataset (for the plot)
--all_part (false) : Consider all particles, instead of only the first one in each micrograph
--s (256) : Square size for estimation
--j (1) : Number of threads
--version : Print RELION version and exit
```
---
### relion_postprocess

####  General options 
```bash 
--i () : Input name of half1, e.g. run_half1_class001_unfil.mrc
--i2 () : Input name of half2, (default replaces half1 from--i with half2)
--ios () : Input tomo optimiser set file. It is used to set--i if not provided. Updated output optimiser set is created.
--o (postprocess) : Output rootname
--angpix (-1) : Pixel size in Angstroms
--half_maps (false) : Write post-processed half maps for validation
--mtf_angpix (-1.) : Pixel size in the original micrographs/movies (in Angstroms)
--molweight (-1) : Molecular weight (in kDa) of ordered protein mass
```
####  Masking options 
```bash 
--auto_mask (false) : Perform automated masking, based on a density threshold
--inimask_threshold (0.02) : Density at which to threshold the map for the initial seed mask
--extend_inimask (3.) : Number of pixels to extend the initial seed mask
--width_mask_edge (6.) : Width for the raised cosine soft mask edge (in pixels)
--mask () : Filename of a user-provided mask (1=protein, 0=solvent, all values in range [0,1])
--force_mask (false) : Use the mask even when the masked resolution is worse than the unmasked resolution
```
####  Sharpening options 
```bash 
--mtf () : User-provided STAR-file with the MTF-curve of the detector
--auto_bfac (false) : Perform automated B-factor determination (Rosenthal and Henderson, 2003)
--autob_lowres (10.) : Lowest resolution (in A) to include in fitting of the B-factor
--autob_highres (0.) : Highest resolution (in A) to include in fitting of the B-factor
--adhoc_bfac (0.) : User-provided B-factor (in A^2) for map sharpening, e.g. -400
```
####  Filtering options 
```bash 
--skip_fsc_weighting (false) : Do not use FSC-weighting (Rosenthal and Henderson, 2003) in the sharpening process
--low_pass (0) : Resolution (in Angstroms) at which to low-pass filter the final map (0: disable, negative: resolution at FSC=0.143)
```
####  Local-resolution options 
```bash 
--locres (false) : Perform local resolution estimation
--locres_sampling (25.) : Sampling rate (in Angstroms) with which to sample the local-resolution map
--locres_maskrad (-1) : Radius (in A) of spherical mask for local-resolution map (default = 0.5*sampling)
--locres_edgwidth (-1) : Width of soft edge (in A) on masks for local-resolution map (default = sampling)
--locres_randomize_at (25.) : Randomize phases from this resolution (in A)
--locres_minres (50.) : Lowest local resolution allowed (in A)
```
####  Expert options 
```bash 
--ampl_corr (false) : Perform amplitude correlation and DPR, also re-normalize amplitudes for non-uniform angular distributions
--randomize_at_fsc (0.8) : Randomize phases from the resolution where FSC drops below this value
--randomize_at_A (-1) : Randomize phases from this resolution (in A) onwards (if positive)
--filter_edge_width (2) : Width of the raised cosine on the low-pass filter edge (in resolution shells)
--interpolate (false) : Interpolate the FSC to obtain an additional, more precise resolution estimate
--verb (1) : Verbosity
--random_seed (0) : Seed for random number generator (negative value for truly random)
--version : Print RELION version and exit
```
---
### relion_postprocess_mpi

####  General options 
```bash 
--i () : Input name of half1, e.g. run_half1_class001_unfil.mrc
--i2 () : Input name of half2, (default replaces half1 from--i with half2)
--ios () : Input tomo optimiser set file. It is used to set--i if not provided. Updated output optimiser set is created.
--o (postprocess) : Output rootname
--angpix (-1) : Pixel size in Angstroms
--half_maps (false) : Write post-processed half maps for validation
--mtf_angpix (-1.) : Pixel size in the original micrographs/movies (in Angstroms)
--molweight (-1) : Molecular weight (in kDa) of ordered protein mass
```
####  Masking options 
```bash 
--auto_mask (false) : Perform automated masking, based on a density threshold
--inimask_threshold (0.02) : Density at which to threshold the map for the initial seed mask
--extend_inimask (3.) : Number of pixels to extend the initial seed mask
--width_mask_edge (6.) : Width for the raised cosine soft mask edge (in pixels)
--mask () : Filename of a user-provided mask (1=protein, 0=solvent, all values in range [0,1])
--force_mask (false) : Use the mask even when the masked resolution is worse than the unmasked resolution
```
####  Sharpening options 
```bash 
--mtf () : User-provided STAR-file with the MTF-curve of the detector
--auto_bfac (false) : Perform automated B-factor determination (Rosenthal and Henderson, 2003)
--autob_lowres (10.) : Lowest resolution (in A) to include in fitting of the B-factor
--autob_highres (0.) : Highest resolution (in A) to include in fitting of the B-factor
--adhoc_bfac (0.) : User-provided B-factor (in A^2) for map sharpening, e.g. -400
```
####  Filtering options 
```bash 
--skip_fsc_weighting (false) : Do not use FSC-weighting (Rosenthal and Henderson, 2003) in the sharpening process
--low_pass (0) : Resolution (in Angstroms) at which to low-pass filter the final map (0: disable, negative: resolution at FSC=0.143)
```
####  Local-resolution options 
```bash 
--locres (false) : Perform local resolution estimation
--locres_sampling (25.) : Sampling rate (in Angstroms) with which to sample the local-resolution map
--locres_maskrad (-1) : Radius (in A) of spherical mask for local-resolution map (default = 0.5*sampling)
--locres_edgwidth (-1) : Width of soft edge (in A) on masks for local-resolution map (default = sampling)
--locres_randomize_at (25.) : Randomize phases from this resolution (in A)
--locres_minres (50.) : Lowest local resolution allowed (in A)
```
####  Expert options 
```bash 
--ampl_corr (false) : Perform amplitude correlation and DPR, also re-normalize amplitudes for non-uniform angular distributions
--randomize_at_fsc (0.8) : Randomize phases from the resolution where FSC drops below this value
--randomize_at_A (-1) : Randomize phases from this resolution (in A) onwards (if positive)
--filter_edge_width (2) : Width of the raised cosine on the low-pass filter edge (in resolution shells)
--interpolate (false) : Interpolate the FSC to obtain an additional, more precise resolution estimate
--verb (1) : Verbosity
--random_seed (0) : Seed for random number generator (negative value for truly random)
--version : Print RELION version and exit
```


---
### relion_preprocess | relion_preprocess_mpi

####  General options 
```bash 
--i () : The STAR file with all (selected) micrographs to extract particles from
--coord_suffix () : The suffix for the coordinate files, e.g. "_picked.star" or ".box"
--coord_dir (ASINPUT) : The directory where the coordinate files are (default is same as micrographs)
--coord_list () : Alternative to coord_suffix&dir: provide a 2-column STAR file with micrographs and coordinate files
--part_dir (Particles/) : Output directory for particle stacks
--part_star () : Output STAR file with all particles metadata
--pick_star () : Output STAR file with 2 columns for micrographs and coordinate files
--reextract_data_star () : A _data.star file from a refinement to re-extract, e.g. with different binning or re-centered (instead of--coord_suffix)
--float16 (false) : Write in half-precision 16 bit floating point numbers (MRC mode 12), instead of 32 bit (MRC mode 0).
--keep_ctfs_micrographs (false) : By default, CTFs from fn_data will be kept. Use this flag to keep CTFs from input micrographs STAR file
--reset_offsets (false) : reset the origin offsets from the input _data.star file to zero?
--recenter (false) : Re-center particle according to rlnOriginX/Y in--reextract_data_star STAR file
--recenter_x (0.) : X-coordinate (in pixel inside the reference) to recenter re-extracted data on
--recenter_y (0.) : Y-coordinate (in pixel inside the reference) to recenter re-extracted data on
--recenter_z (0.) : Z-coordinate (in pixel inside the reference) to recenter re-extracted data on
--ref_angpix (-1) : Pixel size of the reference used for recentering. -1 uses the pixel size of particles.
```
####  Particle extraction 
```bash 
--extract (false) : Extract all particles from the micrographs
--selection_type (0) : Only extract particles with this selection type in the coordinate files (default = extract all)
--extract_size (-1) : Size of the box to extract the particles in (in pixels)
--premultiply_ctf (false) : Premultiply the micrograph/frame with its CTF prior to particle extraction
--premultiply_extract_size (-1) : Size of the box to extract the particles in (in pixels) before CTF premultiplication
--ctf_intact_first_peak (false) : When premultiplying with the CTF, leave frequencies intact until the first peak
--phase_flip (false) : Flip CTF-phases in the micrograph/frame prior to particle extraction
--extract_bias_x (0) : Bias in X-direction of picked particles (this value in pixels will be added to the coords)
--extract_bias_y (0) : Bias in Y-direction of picked particles (this value in pixels will be added to the coords)
--only_do_unfinished (false) : Extract only particles if the STAR file for that micrograph does not yet exist.
--minimum_pick_fom (-999.) : Minimum value for rlnAutopickFigureOfMerit for particle extraction
```
####  Particle operations 
```bash 
--project3d (false) : Project sub-tomograms along Z to generate 2D particles
--scale (-1) : Re-scale the particles to this size (in pixels)
--window (-1) : Re-window the particles to this size (in pixels)
--norm (false) : Normalise the background to average zero and stddev one
--no_ramp (false) : Just subtract the background mean in the normalisation, instead of subtracting a fitted ramping background. 
--bg_radius (-1) : Radius of the circular mask that will be used to define the background area (in pixels)
--white_dust (-1) : Sigma-values above which white dust will be removed (negative value means no dust removal)
--black_dust (-1) : Sigma-values above which black dust will be removed (negative value means no dust removal)
--invert_contrast (false) : Invert the contrast in the input images
--operate_on () : Use this option to operate on an input image stack 
--operate_out (preprocessed.mrcs) : Output name when operating on an input image stack
####  Helix extraction 
```bash 
--helix (false) : Extract helical segments
--helical_outer_diameter (-1.) : Outer diameter of helical tubes in Angstroms (for masks of helical segments)
--helical_tubes (false) : Extract helical segments from tube coordinates
--helical_nr_asu (1) : Number of helical asymmetrical units
--helical_rise (0.) : Helical rise (in Angstroms)
--helical_bimodal_angular_priors (false) : Add bimodal angular priors for helical segments
--helical_cut_into_segments (false) : Cut helical tubes into segments
####  MPI options 
```bash 
--max_mpi_nodes (8) : Limit the number of effective MPI nodes to protect from too heavy disk I/O (thus ignoring larger values from mpirun)
--version : Print RELION version and exit
```
---
### relion_project

####  Options 
```bash 
--i : Input map to be projected
--o (proj) : Rootname for output projections
--float16 (false) : Write in half-precision 16 bit floating point numbers (MRC mode 12), instead of 32 bit (MRC mode 0).
--ctf (false) : Apply CTF to reference projections
--ctf_phase_flip (false) : Flip phases of the CTF in the output projections
--ctf_intact_first_peak (false) : Ignore CTFs until their first peak?
--angpix (-1) : Pixel size (in Angstroms)
--mask () : Mask that will be applied to the input map prior to making projections
--ang (None) : Particle STAR file with orientations and CTF for multiple projections (if None, assume single projection)
--nr_uniform (-1) :  OR get this many random samples from a uniform angular distribution
--sigma_offset (0) : Apply Gaussian errors (A) with this stddev to the XY-offsets
--rot (0) : First Euler angle (for a single projection)
--tilt (0) : Second Euler angle (for a single projection)
--psi (0) : Third Euler angle (for a single projection)
--xoff (0) : Origin X-offsets (in pixels) (for a single projection)
--yoff (0) : Origin Y-offsets (in pixels) (for a single projection)
--zoff (0) : Origin Z-offsets (in pixels) (for a single 3D rotation)
--add_noise (false) : Add noise to the output projections (only with--ang)
--white_noise (0) : Standard deviation of added white Gaussian noise
--model_noise () : Model STAR file with power spectra for coloured Gaussian noise
--subtract_exp (false) : Subtract projections from experimental images (in--ang)
--ignore_particle_name (false) : Ignore the rlnParticleName column (in--ang)
--3d_rot (false) : Perform 3D rotations instead of projection into 2D images
--simulate (false) : Simulate data with known ground-truth by subtracting signal and adding projection in random orientation.
--adjust_simulation_SNR (1.) : Relative SNR compared to input images for realistic simulation of data
--ang_simulate () : STAR file with orientations for projections of realistic simulations (random from--ang STAR file by default)
--maxres (-1) : Maximum resolution (in Angstrom) to consider in Fourier space (default Nyquist)
--pad (2) : Padding factor
--ctf2 (false) : Apply CTF*CTF to reference projections
--NN (false) : Use nearest-neighbour instead of linear interpolation
--version : Print RELION version and exit
```
---
### relion_python_blush

```bash
usage: Main command line for running Blush in RELION. [-h] [-m MODEL_NAME]
[-s STRIDES]
[-b BATCH_SIZE]
[-g [GPU]]
[--device_timeout DEVICE_TIMEOUT]
[--debug]
[--skip-spectral-trailing]
[star_file]

positional arguments:
  star_file

options:
  -h,--helpshow this help message and exit
  -m MODEL_NAME,--model_name MODEL_NAME
  Model name to use
  -s STRIDES,--strides STRIDES
  Strides for running the denoiser
  -b BATCH_SIZE,--batch_size BATCH_SIZE
  Batch size for running denoiser
  -g [GPU],--gpu [GPU]
  GPU id to use. If not specified, all available GPUs
  will be used.
--device_timeout DEVICE_TIMEOUT
  Time to wait for GPUs to free up.
--debug   Debug mode (slower)
--skip-spectral-trailing
  Use no spectral trailing (unsafe).

```

---
### relion_python_classranker

```
usage: -c [-h] [-m MODEL_NAME] [project_dir]

positional arguments:
  project_dir

options:
  -h,--help show this help message and exit
  -m MODEL_NAME,--model_name MODEL_NAME
```

---
### relion_python_dynamight

```bash
 Usage: -c [OPTIONS] COMMAND [ARGS]...  

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│--help  Show this message and exit.  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ compute-masks-for-rigid-transforms   │
│ compute-rigid-transforms   │
│ deformable-backprojection  │
│ deformable-backprojection-correction │
│ deformable-backprojection-single│
│ deformable-backprojection-single-deformation │
│ explore-latent-space   │
│ optimize-deformations  │
│ optimize-deformations-rigid│
│ optimize-deformations-single   │
│ optimize-inverse-deformations  │
│ optimize-inverse-deformations-single │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

---
### relion_python_fetch_weights
Attempting to download weights for class ranker...
Model (v1.0) loaded successfully from checkpoint /usr/local/torch_models/hub/checkpoints/relion_class_ranker/v1.0.ckpt
No project directory was specified... exiting!
Attempting to download weights for Blush...
Blush model (v1.0) loaded successfully from checkpoint /usr/local/torch_models/hub/checkpoints/relion_blush/v1.0.ckpt
No job target was specified for Blush regularization... exiting!
Attempting to download weights for ModelAngelo...


---
   Has RELION been provided a Python interpreter with the correct environment?
   The interpreter can be passed to RELION either during Cmake configuration by
 using the Cmake flag -DPYTHON_EXE_PATH=&lt;path/to/python/interpreter>.
   NOTE: For some modules TORCH_HOME needs to be set to find pretrained models

  Using python executable: /usr/local/conda/envs/relion-5.0/bin/python

One or more download tasks failed. See above error messages.

---
### relion_python_modelangelo

   Has RELION been provided a Python interpreter with the correct environment?
   The interpreter can be passed to RELION either during Cmake configuration by
 using the Cmake flag -DPYTHON_EXE_PATH=&lt;path/to/python/interpreter>.
   NOTE: For some modules TORCH_HOME needs to be set to find pretrained models



  Using python executable: /usr/local/conda/envs/relion-5.0/bin/python



---
### relion_python_topaz

```bash
usage: -c [-h] [--version] &lt;command> ...

options:
  -h,--help  show this help message and exit
--version   show program's version number and exit

commands:
  Particle picking:
traintrain region classifier from images with labeled
 coordinates
segment  segment images using a trained region classifier
extract  extract particles from segmented images or segment and
 extract in one step with a trained classifier
precision_recall_curve calculate the precision-recall curve for a set of
 predicted particle coordinates with scores and a set of
 target coordinates
  
  Image processing:
downsampledownsample micrographs with truncated DFT
normalizenormalize a set of images using the 2-component Gaussian
 mixture model
preprocessdownsample and normalize images in one step
denoise  denoise micrographs with various denoising algorithms
denoise3ddenoise 3D volumes with various denoising algorithms
  
  File utilities:
convert  convert particle coordinate files between various
 formats automatically. also allows filtering particles
 by score threshold and UP- and DOWN-scaling coordinates.
splitsplit particle file containing coordinates for multiple
 micrographs into one file per micrograph
particle_stack extract mrc particle stack given coordinates table
train_test_split   split micrographs with labeled particles into
 train/test sets
  
  GUI:
gui  opens the topaz GUI in a web browser
  
  [Deprecated]:
scale_coordinates  scale particle coordinates for resized images
boxes_to_coordinates   convert .box format coordinates to tab delimited
 coordinates table
star_to_coordinatesconvert .star file coordinates to tab delimited
 coordinates table
coordinates_to_starconvert coordinates table to .star file format
coordinates_to_boxes   convert coordinates table to .box format files per image
coordinates_to_eman2_json  convert coordinates table to EMAN2 json format files per
 image
star_particles_threshold   filter the particles in a .star file by score threshold

  &lt;command>
```

---
### relion_reconstruct | relion_reconstruct_mpi

####  General options 
```bash 
--i () : Input STAR file with the projection images and their orientations
--o (relion.mrc) : Name for output reconstruction
--sym (c1) : Symmetry group
--maxres (-1) : Maximum resolution (in Angstrom) to consider in Fourier space (default Nyquist)
--pad (2) : Padding factor
--img () : Optional: image path prefix
--subset (-1) : Subset of images to consider (1: only reconstruct half1; 2: only half2; other: reconstruct all)
--class (-1) : Consider only this class (-1: use all classes)
--angpix (-1) : Pixel size in the reconstruction (take from first optics group by default)
```
####  CTF options 
```bash 
--ctf (false) : Apply CTF correction
--ctf_intact_first_peak (false) : Leave CTFs intact until first peak
--ctf_phase_flipped (false) : Images have been phase flipped
--only_flip_phases (false) : Do not correct CTF-amplitudes, only flip phases
```
####  Ewald-sphere correction options 
```bash 
--ewald (false) : Correct for Ewald-sphere curvature (developmental)
--mask_diameter (-1.) : Diameter (in A) of mask for Ewald-sphere curvature correction
--width_mask_edge (3) : Width (in pixels) of the soft edge on the mask
--reverse_curvature (false) : Try curvature the other way around
--newbox (-1) : Box size of reconstruction after Ewald sphere correction
--sectors (2) : Number of sectors for Ewald sphere correction
--skip_mask (false) : Do not apply real space mask during Ewald sphere correction
--skip_weighting (false) : Do not apply weighting during Ewald sphere correction
```
####  Helical options 
```bash 
--nr_helical_asu (1) : Number of helical asymmetrical units
--helical_rise (0.) : Helical rise (in Angstroms)
--helical_twist (0.) : Helical twist (in degrees, + for right-handedness)
```
####  Subtomogram averaging 
```bash 
--normalised_subtomo (false) : Have subtomograms been multiplicity normalised? (Default=False)
--skip_subtomo_multi (false) : Skip subtomo multiplicity correction? (For nomalised subtomos only)
--ctf3d_not_squared (false) : CTF3D files contain sqrt(CTF^2) patterns
```
####  Expert options 
```bash 
--subtract () : Subtract projections of this map from the images used for reconstruction
--NN (false) : Use nearest-neighbour instead of linear interpolation before gridding correction
--blob_r (1.9) : Radius of blob for gridding interpolation
--blob_m (0) : Order of blob for gridding interpolation
--blob_a (15) : Alpha-value of blob for gridding interpolation
--iter (10) : Number of gridding-correction iterations
--refdim (3) : Dimension of the reconstruction (2D or 3D)
--angular_error (0.) : Apply random deviations with this standard deviation (in degrees) to each of the 3 Euler angles
--shift_error (0.) : Apply random deviations with this standard deviation (in Angstrom) to each of the 2 translations
--fom_weighting (false) : Weight particles according to their figure-of-merit (_rlnParticleFigureOfMerit)
--fsc () : FSC-curve for regularized reconstruction
--3d_rot (false) : Perform 3D rotations instead of backprojections from 2D images
--reconstruct_ctf (-1) : Perform a 3D reconstruction from 2D CTF-images, with the given size in pixels
--ctf2 (false) : Reconstruct CTF^2 and then take the sqrt of that
--dont_skip_gridding (false) : Perform gridding in the reconstruction (obsolete?)
--debug () : Rootname for debug reconstruction files
--debug_ori_size (1) : Rootname for debug reconstruction files
--debug_size (1) : Rootname for debug reconstruction files
--reconstruct_noise () : Reconstruct noise using sigma2 values in this model STAR file
--read_weights (false) : Developmental: read freq. weight files
--write_debug_output (false) : Write out arrays with data and weight terms prior to reconstruct
--external_reconstruct (false) : Write out BP denominator and numerator for external_reconstruct program
--verb (1) : Verbosity
--version : Print RELION version and exit
```
---
### relion_refine | relion_refine_mpi

####  General options 
```bash 
--i () : Input particles (in a star-file)
--tomograms () : Star file with the tomograms, in case subtomos are handled as 2D stacks
--trajectories () : Star file with the tomogram motion trajectories
--ios () : Input tomo optimisation set file. It is used to set--i,--tomograms,--ref or--solvent_mask if they are not provided. Updated output optimiser set is created.
--o () : Output rootname
--iter (-1) : Maximum number of iterations to perform
--tau2_fudge (-1) : Regularisation parameter (values higher than 1 give more weight to the data)
--tau2_fudge_scheme () : Tau2 fudge factor updates scheme. Valid values are plain or &lt;deflate>-step. Where &lt;deflate> is the deflate factor during initial stage.
--K (1) : Number of references to be refined
--particle_diameter (-1) : Diameter of the circular mask that will be applied to the experimental images (in Angstroms)
--zero_mask (false) : Mask surrounding background in particles to zero (by default the solvent area is filled with random noise)
--flatten_solvent (false) : Perform masking on the references as well?
--solvent_mask (None) : User-provided mask for the references (default is to use spherical mask with particle_diameter)
--solvent_mask2 (None) : User-provided secondary mask (with its own average density)
--lowpass_mask (None) : User-provided mask for low-pass filtering
--lowpass (0) : User-provided cutoff for region specified above
--tau (None) : STAR file with input tau2-spectrum (to be kept constant)
--local_symmetry (None) : Local symmetry description file containing list of masks and their operators
--split_random_halves (false) : Refine two random halves of the data completely separately
--low_resol_join_halves (-1) : Resolution (in Angstrom) up to which the two random half-reconstructions will not be independent to prevent diverging orientations
--center_classes (false) : Re-center classes based on their center-of-mass?
```
####  Initialisation 
```bash 
--ref (None) : Image, stack or star-file with the reference(s). (Compulsory for 3D refinement!)
--denovo_3dref (false) : Make an initial 3D model from randomly oriented 2D particles
--offset (10) : Initial estimated stddev for the origin offsets (in Angstroms)
--firstiter_cc (false) : Perform CC-calculation in the first iteration (use this if references are not on the absolute intensity scale)
--ini_high (-1) : Resolution (in Angstroms) to which to limit refinement in the first iteration
```
####  Orientations 
```bash 
--oversampling (1) : Adaptive oversampling order to speed-up calculations (0=no oversampling, 1=2x, 2=4x, etc)
--healpix_order (2) : Healpix order for the angular sampling (before oversampling) on the (3D) sphere: hp2=15deg, hp3=7.5deg, etc
--psi_step (-1) : Sampling rate (before oversampling) for the in-plane angle (default=10deg for 2D, hp sampling for 3D)
--limit_tilt (-91) : Limited tilt angle: positive for keeping side views, negative for keeping top views
--sym (c1) : Symmetry group
--relax_sym () : Symmetry to be relaxed
--offset_range (6) : Search range for origin offsets (in pixels)
--offset_step (2) : Sampling rate (before oversampling) for origin offsets (in pixels)
--offset_range_x (-1) : Range for sampling offsets in X-direction (in Angstrom; default=auto)
--offset_range_y (-1) : Range for sampling offsets in Y-direction (in Angstrom; default=auto)
--offset_range_z (-1) : Range for sampling offsets in Z-direction (in Angstrom; default=auto)
--helical_offset_step (-1) : Sampling rate (before oversampling) for offsets along helical axis (in Angstroms)
--perturb (0.5) : Perturbation factor for the angular sampling (0=no perturb; 0.5=perturb)
--auto_refine (false) : Perform 3D auto-refine procedure?
--auto_sampling (false) : Perform auto-sampling (outside the 3D auto-refine procedure)?
--auto_local_healpix_order (4) : Minimum healpix order (before oversampling) from which autosampling procedure will use local searches
--sigma_ang (-1) : Stddev on all three Euler angles for local angular searches (of +/- 3 stddev)
--sigma_rot (-1) : Stddev on the first Euler angle for local angular searches (of +/- 3 stddev)
--sigma_tilt (-1) : Stddev on the second Euler angle for local angular searches (of +/- 3 stddev)
--sigma_psi (-1) : Stddev on the in-plane angle for local angular searches (of +/- 3 stddev)
--skip_align (false) : Skip orientational assignment (only classify)?
--skip_rotate (false) : Skip rotational assignment (only translate and classify)?
--bimodal_psi (false) : Do bimodal searches of psi angle?
```
####  Helical reconstruction (in development...) 
```bash 
--helix (false) : Perform 3D classification or refinement for helices?
--ignore_helical_symmetry (false) : Ignore helical symmetry?
--helical_nr_asu (1) : Number of new helical asymmetric units (asu) per box (1 means no helical symmetry is present)
--helical_twist_initial (0.) : Helical twist (in degrees, positive values for right-handedness)
--helical_twist_min (0.) : Minimum helical twist (in degrees, positive values for right-handedness)
--helical_twist_max (0.) : Maximum helical twist (in degrees, positive values for right-handedness)
--helical_twist_inistep (0.) : Initial step of helical twist search (in degrees)
--helical_rise_initial (0.) : Helical rise (in Angstroms)
--helical_rise_min (0.) : Minimum helical rise (in Angstroms)
--helical_rise_max (0.) : Maximum helical rise (in Angstroms)
--helical_rise_inistep (0.) : Initial step of helical rise search (in Angstroms)
--helical_nstart (1) : N-number for the N-start helix (only useful for rotational priors)
--helical_z_percentage (0.3) : This box length along the center of Z axis contains good information of the helix. Important in imposing and refining symmetry
--helical_inner_diameter (-1.) : Inner diameter of helical tubes in Angstroms (for masks of helical references and particles)
--helical_outer_diameter (-1.) : Outer diameter of helical tubes in Angstroms (for masks of helical references and particles)
--helical_symmetry_search (false) : Perform local refinement of helical symmetry?
--helical_sigma_distance (-1.) : Sigma of distance along the helical tracks
--helical_keep_tilt_prior_fixed (false) : Keep helical tilt priors fixed (at 90 degrees) in global angular searches?
--helical_exclude_resols () : Resolutions (in A) along helical axis to exclude from refinement (comma-separated pairs, e.g. 50,5)
--fourier_mask (None) : Originally-sized, FFTW-centred image with Fourier mask for Projector
```
####  Corrections 
```bash 
--ctf (false) : Perform CTF correction?
--pad_ctf (false) : Perform CTF padding to treat CTF aliaising better?
--ctf_intact_first_peak (false) : Ignore CTFs until their first peak?
--ctf_uncorrected_ref (false) : Have the input references not been CTF-amplitude corrected?
--ctf_phase_flipped (false) : Have the data been CTF phase-flipped?
--only_flip_phases (false) : Only perform CTF phase-flipping? (default is full amplitude-correction)
--norm (false) : Perform normalisation-error correction?
--scale (false) : Perform intensity-scale corrections on image groups?
--no_norm (false) : Switch off normalisation-error correction?
--no_scale (false) : Switch off intensity-scale corrections on image groups?
```
####  Stochastic Gradient Descent 
```bash 
--grad (false) : Perform gradient based optimisation (instead of default expectation-maximization)
--grad_em_iters (0) : Number of iterations at the end of a gradient refinement using Expectation-Maximization
--grad_ini_frac (0.3) : Fraction of iterations in the initial phase of refinement
--grad_fin_frac (0.2) : Fraction of iterations in the final phase of refinement
--grad_min_resol (20) : Adjusting the signal under-estimation during gradient optimization to this resolution.
--grad_ini_resol (-1) : Resolution cutoff during the initial gradient refinement iterations (A)
--grad_fin_resol (-1) : Resolution cutoff during the final gradient refinement iterations (A)
--grad_ini_subset (-1) : Mini-batch size during the initial gradient refinement iterations
--grad_fin_subset (-1) : Mini-batch size during the final gradient refinement iterations
--mu (0.9) : Momentum parameter for gradient refinement updates
--grad_stepsize (-1) : Step size parameter for gradient optimisation.
--grad_stepsize_scheme () : Gradient step size updates scheme. Valid values are plain or &lt;inflate>-step . Where &lt;inflate> is the initial inflate.
--grad_write_iter (10) : Write out model every so many iterations in SGD (default is writing out all iters)
--maxsig (-1) : Maximum number of most significant poses & translations to consider
--no_init_blobs (false) : Use this to switch off initializing models with random Gaussians (which is new in relion-4.0).
--som (false) : Calculate self-organizing map instead of classification.
--som_ini_nodes (2) : Number of initial SOM nodes.
--som_connectivity (5.0) : Number of average active neighbour connections.
--som_inactivity_threshold (0.01) : Threshold for inactivity before node is dropped.
--som_neighbour_pull (0.2) : Portion of gradient applied to connected nodes.
--class_inactivity_threshold (0) : Replace classes with little activity during gradient based classification.
```
####  Subtomogram averaging 
```bash 
--normalised_subtomo (false) : Have subtomograms been multiplicity normalised? (Default=False)
--skip_subtomo_multi (false) : Skip subtomo multiplicity correction
--ctf3d_not_squared (false) : CTF3D files contain sqrt(CTF^2) patterns
--subtomo_multi_thr (0.01) : Threshold to remove marginal voxels during expectation
```
####  Computation 
```bash 
--pool (1) : Number of images to pool for each thread task
--j (1) : Number of threads to run in parallel (only useful on multi-core machines)
--dont_combine_weights_via_disc (false) : Send the large arrays of summed weights through the MPI network, instead of writing large files to disc
--onthefly_shifts (false) : Calculate shifted images on-the-fly, do not store precalculated ones in memory
--no_parallel_disc_io (false) : Do NOT let parallel (MPI) processes access the disc simultaneously (use this option with NFS)
--preread_images (false) : Use this to let the leader process read all particles into memory. Be careful you have enough RAM for large data sets!
--scratch_dir () : If provided, particle stacks will be copied to this local scratch disk prior to refinement.
--keep_free_scratch (10) : Space available for copying particle stacks (in Gb)
--reuse_scratch (false) : Re-use data on scratchdir, instead of wiping it and re-copying all data.
--keep_scratch (false) : Don't remove scratch after convergence. Following jobs that use EXACTLY the same particles should use--reuse_scratch.
--fast_subsets (false) : Use faster optimisation by using subsets of the data in the first 15 iterations
--gpu (false) : Use available gpu resources for some calculations
--free_gpu_memory (0) : GPU device memory (in Mb) to leave free after allocation.
```
####  Expert options 
```bash 
--pad (2) : Oversampling factor for the Fourier transforms of the references
--ref_angpix (-1.) : Pixel size (in A) for the input reference (default is to read from header)
--NN (false) : Perform nearest-neighbour instead of linear Fourier-space interpolation?
--r_min_nn (10) : Minimum number of Fourier shells to perform linear Fourier-space interpolation
--verb (1) : Verbosity (1=normal, 0=silent)
--random_seed (-1) : Number for the random seed generator
--coarse_size (-1) : Maximum image size for the first pass of the adaptive sampling approach
--adaptive_fraction (0.999) : Fraction of the weights to be considered in the first pass of adaptive oversampling 
--maskedge (5) : Width of the soft edge of the spherical mask (in pixels)
--fix_sigma_noise (false) : Fix the experimental noise spectra?
--fix_sigma_offset (false) : Fix the stddev in the origin offsets?
--incr_size (10) : Number of Fourier shells beyond the current resolution to be included in refinement
--print_metadata_labels (false) : Print a table with definitions of all metadata labels, and exit
--print_symmetry_ops (false) : Print all symmetry transformation matrices, and exit
--strict_highres_exp (-1) : High resolution limit (in Angstrom) to restrict probability calculations in the expectation step
--strict_lowres_exp (-1) : Low resolution limit (in Angstrom) to restrict probability calculations in the expectation step
--dont_check_norm (false) : Skip the check whether the images are normalised correctly
--always_cc (false) : Perform CC-calculation in all iterations (useful for faster denovo model generation?)
--solvent_correct_fsc (false) : Correct FSC curve for the effects of the solvent mask?
--skip_maximize (false) : Skip maximization step (only write out data.star file)?
--failsafe_threshold (40) : Maximum number of particles permitted to be handled by fail-safe mode, due to zero sum of weights, before exiting with an error (GPU only).
--blush (false) : Perform the reconstruction with the Blush algorithm.
--blush_skip_spectral_trailing (false) : Skip spectral trailing during Blush reconstruction (WARNING: This may inflate resolution estimates)
--external_reconstruct (false) : Perform the reconstruction step outside relion_refine, e.g. for learned priors?)
--auto_iter_max (999) : In auto-refinement, stop at this iteration.
--auto_ignore_angles (false) : In auto-refinement, update angular sampling regardless of changes in orientations for convergence. This makes convergence faster.
--auto_resol_angles (false) : In auto-refinement, update angular sampling based on resolution-based required sampling. This makes convergence faster.
--allow_coarser_sampling (false) : In 2D/3D classification, allow coarser angular and translational samplings if accuracies are bad (typically in earlier iterations.
--trust_ref_size (false) : Trust the pixel and box size of the input reference; by default the program will die if these are different from the first optics group of the data
--nr_parts_sigma2noise (-1) : Number of particles (per optics group) for initial noise spectra estimation (default 1000 for SPA and 100 for STA).
--dont_skip_gridding (false) : Perform gridding in the reconstruction step (obsolete?)
```
####  MPI options 
```bash 
--halt_all_followers_except (-1) : For debugging: keep all followers except this one waiting
--keep_debug_reconstruct_files (false) : For debugging: keep temporary data and weight files for debug-reconstructions.
--version : Print RELION version and exit
```

---
### relion_run_ctffind | relion_run_ctffind_mpi

####  General options 
```bash 
####  CTF estimation 
```bash 
--i : STAR file with all input micrographs, or a unix wildcard to all micrograph files, e.g. "mics/*.mrc"
--use_noDW (false) : Estimate CTFs from rlnMicrographNameNoDW instead of rlnMicrographName (only after MotionCor2)
--o (CtfEstimate/) : Directory, where all output files will be stored
--only_make_star (false) : Don't estimate any CTFs, only join all logfile results in a STAR file
--only_do_unfinished (false) : Only estimate CTFs for those micrographs for which there is not yet a logfile with Final values.
--do_at_most (-1) : Only process up to this number of (unprocessed) micrographs.
--ctfWin (-1) : Size (in pixels) of a centered, squared window to use for CTF-estimation
```
####  Tomography-specific parameters 
```bash 
--localsearch_nominal_defocus (10000.) : If positive, search defoci (+/-) around rlnTomoNominalDefocus (in A)
--exp_factor_dose (100.) : If positive, use exponential factor by which to limit maxres per unit dose (maxres*=exp(dose/factor))
```
####  Microscopy parameters 
```bash 
--CS (-1) : Spherical Aberration (mm) 
--HT (-1) : Voltage (kV)
--AmpCnst (-1) : Amplitude constrast
--angpix (-1) : Pixel size in the input micrographs (A)
```
####  CTFFIND parameters 
```bash 
--ctffind_exe () : Location of ctffind executable (or through RELION_CTFFIND_EXECUTABLE environment variable)
--Box (512) : Size of the boxes to calculate FFTs
--ResMin (100) : Minimum resolution (in A) to include in calculations
--ResMax (7) : Maximum resolution (in A) to include in calculations
--dFMin (10000) : Minimum defocus value (in A) to search
--dFMax (50000) : Maximum defocus value (in A) to search
--FStep (250) : defocus step size (in A) for search
--dAst (0) : amount of astigmatism (in A)
```
####  CTFFIND4 parameters 
```bash 
--is_ctffind4 (false) : The provided CTFFIND executable is CTFFIND4 (version 4.1+)
--use_given_ps (false) : Use pre-calculated power spectra?
--do_movie_thon_rings (false) : Calculate Thon rings from movie frames?
--avg_movie_frames (1) : Average over how many movie frames (try to get 4 e-/A2)
--movie_rootname (_movie.mrcs) : Rootname plus extension for movies
--do_phaseshift (false) : Estimate the phase shift in the images (e.g. from a phase-plate)
--phase_min (0.) : Minimum phase shift (in degrees)
--phase_max (180.) : Maximum phase shift (in degrees)
--phase_step (10.) : Step in phase shift (in degrees)
--j (1) : Number of threads (for CTFIND4 only)
--fast_search (false) : Disable "Slower, more exhaustive search" in CTFFIND4.1 (faster but less accurate)
--version : Print RELION version and exit
```
---
### relion_run_motioncorr | relion_run_motioncorr_mpi

```bash
No help
```

---
### relion_schemer

####  General options 
```bash 
--scheme : Directory name of the scheme
--copy () : Make a copy of the scheme into this directory
```
####  Add elements to the scheme 
```bash 
--add () : Specify category of element to add to the scheme (variable, operator, job, edge or fork)
--type () : Specify type of that element to add to the scheme
--i () : Specify input to the element 
--i2 () : Specify 2nd input to the element 
--bool () : Name of boolean variable (for forks)
--o () : Specify output of the element 
--o2 () : Specify 2nd output of the element 
--name () : Name of the variable, operator or job to be added
--value () : Value of the variable to be added
--original_value () : Original value of the variable to be added
--mode () : Mode (for jobs): new or continue
```
####  Set values of variables in the scheme 
```bash 
--reset (false) : Reset all variables to their original values
--abort (false) : Abort a scheme that is running
--set_var () : Name of a variable to set (using also the--value argument)
--set_job_mode () : Name of a job whose mode to set (using also the--value argument)
--set_has_started () : Name of a job whose has_started variable to set (using also the--value argument)
--set_current_node () : Name of a node to which to set current_node
```
####  Run the schemer within a pipeline 
```bash 
--run (false) : Run the schemer
--verb (1) : Running verbosity: 0, 1, 2 or 3)
--run_pipeline (default) : Name of the pipeline in which to run this scheme
--version : Print RELION version and exit
```
---
### relion_stack_create

####  General options 
```bash 
--i : Input STAR file with the images (as rlnImageName) to be saved in a stack
--o (output) : Output rootname
--split_per_micrograph (false) : Write out separate stacks for each micrograph (needs rlnMicrographName in STAR file)
--apply_transformation (false) : Apply the inplane-transformations (needs _rlnOriginX/Y and _rlnAnglePsi in STAR file) by real space interpolation
--apply_rounded_offsets_only (false) : Apply the rounded translations only (so-recentering without interpolation; needs _rlnOriginX/Y in STAR file)
--ignore_optics (false) : Ignore optics groups. This allows you to read and write RELION 3.0 STAR files but does NOT allow you to convert 3.1 STAR files back to the 3.0 format.
--one_by_one (false) : Write particles one by one. This saves memory but can be slower.
--float16 (false) : Write images in 16bit float format (default is 32bit).
--version : Print RELION version and exit
```
---
### relion_star_datablock_ctfdat
```
Nothing?
```
---
### relion_star_datablock_singlefiles

```
--help 
```

---
### relion_star_datablock_stack

```
Nothing?
```

---
### relion_star_handler

####  General options 
```bash 
--i : Input STAR file(s)
--o (out.star) : Output STAR file
--ignore_optics (false) : Provide this option for relion-3.0 functionality, without optics groups
--angpix (1.) : Pixel size in Angstrom, for when ignoring the optics groups in the input star file
--i_tablename () : If ignoring optics, then read table with this name
```
####  Compare options 
```bash 
--compare () : STAR file name to compare the input STAR file with
--label1 () : 1st metadata label for the comparison (may be string, int or RFLOAT)
--label2 () : 2nd metadata label for the comparison (RFLOAT only) for 2D/3D-distance)
--label3 () : 3rd metadata label for the comparison (RFLOAT only) for 3D-distance)
--max_dist (0.) : Maximum distance to consider a match (for int and RFLOAT only)
```
####  Select options 
```bash 
--select () : Metadata label (number) to base output selection on (e.g. rlnCtfFigureOfMerit)
--minval (-99999999.) : Minimum acceptable value for this label (inclusive)
--maxval (99999999.) : Maximum acceptable value for this label (inclusive)
--select_by_str () : Metadata label (string) to base output selection on (e.g. rlnMicrographname)
--select_include () : select rows that contains this string in--select_by_str 
--select_exclude () : exclude rows that contains this string in--select_by_str 
```
####  Discard based on image statistics options 
```bash 
--discard_on_stats (false) : Discard images if their average/stddev deviates too many sigma from the ensemble average
--discard_label (rlnImageName) : MetaDataLabel that points to the images to be used for discarding based on statistics
--discard_sigma (4.) : Discard images with average or stddev values that lie this many sigma away from the ensemble average
```
####  Combine options 
```bash 
--combine (false) : Combine input STAR files (multiple individual filenames, all within double-quotes after--i)
--combine_picks (false) : Combine input manual/autopick STAR files (multiple individual filenames, all within double-quotes after--i)
--check_duplicates () : MetaDataLabel (for a string only!) to check for duplicates, e.g. rlnImageName
```
####  Split options 
```bash 
--split (false) : Split the input STAR file into one or more smaller output STAR files
--random_order (false) : Perform splits on randomised order of the input STAR file
--random_seed (-1) : Random seed for randomisation.
--nr_split (-1) : Split into this many equal-sized STAR files
--size_split (-1) : AND/OR split into subsets of this many lines
```
####  Operate options 
```bash 
--operate () : Operate on this metadata label
--operate2 () : Operate also on this metadata label
--operate3 () : Operate also on this metadata label
--set_to () : Set all the values for the--operate label(s) to this value
--multiply_by (1.) : Multiply all the values for the--operate label(s) by this value
--add_to (0.) : Add this value to all the values for the--operate label(s)
```
####  Center options 
```bash 
--center (false) : Perform centering of particles according to a position in the reference.
--center_X (0.) : X-coordinate in the reference to center particles on (in pix)
--center_Y (0.) : Y-coordinate in the reference to center particles on (in pix)
--center_Z (0.) : Z-coordinate in the reference to center particles on (in pix)
```
####  Column options 
```bash 
--remove_column () : Remove the column with this metadata label from the input STAR file.
--add_column () : Add a column with this metadata label from the input STAR file.
--add_column_value () : Set this value in all rows for the added column
--copy_column_from () : Copy values in this column to the added column
--hist_column () : Calculate histogram of values in the column with this metadata label
--in_percent (false) : Show a histogram in percent (need--hist_column)
--show_cumulative (false) : Show a histogram of cumulative distribution (need--hist_column)
--hist_bins (-1) : Number of bins for the histogram. By default, determined automatically by Freedman–Diaconis rule.
--hist_min (-inf) : Minimum value for the histogram (needs--hist_bins)
--hist_max (inf) : Maximum value for the histogram (needs--hist_bins)
```
####  Duplicate removal 
```bash 
--remove_duplicates (-1) : Remove duplicated particles within this distance [Angstrom]. Negative values disable this.
--image_angpix (-1) : For down-sampled particles, specify the pixel size [A/pix] of the original images used in the Extract job
--version : Print RELION version and exit
```
---
### relion_star_loopheader
```
data_
loop_
_--help
```
---
### relion_star_plottable
 ** Written datafile:--help--.dat
 ** Running: gnuplot -persist gnuplot.plt 
 ** Alternatively, inside an interactive gnuplot session type: load "gnuplot.plt"

---
### relion_star_printtable

```
 === Usage: === 
 /usr/local/relion5/bin/relion_star_printtable &lt;starfile> &lt;tablename> [&lt;label1> &lt;label2> ...]
 
 === Purpose: === 
 This (bash) script prints the contents of a datablock (with name tablename) from a starfile
 If any labels are given, then only those will be printed 
 
 === Example: === 
 /usr/local/relion5/bin/relion_star_printtable run3_it024_model.star data_model_class_1 rlnResolution rlnSsnrMap
 (NOTE: not _rlnResolution)
 
 === Limitations: === 
 This program makes a temporary directory under $TMPDIR. This folder must be writable and have sufficient space.
```

 This program does not perform any error checks.
 When specified table and/or column(s) are absent in the input, the program might give incorrect results.
 In older versions, table names and column names could match only partially. For example, rlnFourierShellCorrelationCorrected matched rlnFourierShellCorrelation. This was dangerous and the match is exact now.
 
 To address these issues, this program will be completely re-written in the next major update (RELION 3.2).
 In the new version, the errors are handled more strictly. Please update your scripts to prepare for transition.


---
### relion_suggest_tvalue

####  Options 
```bash 
--map : Consensus map
--mask : Mask used for focussed classification/refinement
--T (4) : Standard T-value
--try (10) : Number of times to position mask randomly to find a high-power density area
--version : Print RELION version and exit
```
---
### relion_tiltpair_plot

####  General options 
```bash 
--u : Input STAR file with untilted particles
--t : Input STAR file with tilted particles
--o (tiltpair.eps) : Output EPS file 
--sym (C1) : Symmetry point group
--exp_tilt (0.) : Choose symmetry operator that gives tilt angle closest to this value
--exp_beta (0.) : Choose symmetry operator that gives beta angle closest to this value
--dist_from_alpha (0.) : Direction (alpha angle) of tilt axis from which to calculate distance
--dist_from_tilt (0.) : Tilt angle from which to calculate distance
--max_tilt (90.) : Maximum tilt angle to plot in the EPS file
--spot_radius (3) : Radius in pixels of the spots in the tiltpair plot
--version : Print RELION version and exit
```
---
#### #### ####  HELIX #### #### ####

---
### relion_helix_toolbox

####  Show usage 
```bash 
--function_help (false) : Show usage for the selected function (FEB 19, 2017)
```
####  List of functions (alphabetically ordered) 
```bash 
--check (false) : Check parameters for 3D helical reconstruction in RELION
--cut_out (false) : Cut out a small part of the helix
--cylinder (false) : Create a cylinder as 3D initial reference
--impose (false) : Impose helical symmetry (in real space)
--interpo (false) : Interpolate 3D curve for 3D helical sub-tomogram extraction
--norm (false) : Normalise 2D/3D helical segments in a STAR file
--pdb_helix (false) : Simulate a helix from a single PDB file of protein molecule
--remove_bad_ctf (false) : Remove micrographs with poor-quality CTF
--remove_bad_tilt (false) : Remove helical segments with large tilt angle deviation (away from 90 degrees)
--remove_bad_psi (false) : Remove helical segments with large psi angle deviation (away from psi prior)
--search (false) : Local search of helical symmetry
--select_3dtomo (false) : Select 3D subtomograms given 2D projections
--simulate_helix (false) : Create a helical 3D reference of spheres
--simulate_segments (false) : Simulate helical segments using a STAR file
--sort_tube_id (false) : Sort segments in _data.star file according to helical tube IDs
--spherical_mask (false) : Apply soft spherical mask to 3D helical reference
--average_au_2d (false) : Average multiple asymmetrical units in 2D along the helical axis?
```
####  List of functions which can be called in Relion GUI 
```bash 
--combine_gctf (false) : Combine Autopicker priors (tilt and psi) with Gctf local search results
--central_mask (false) : Crop the central part of a helix
--coords_emn2rln (false) : Convert EMAN2 coordinates of helical segments into RELION STAR format
--coords_xim2rln (false) : Convert XIMDISP coordinates of helical segments into RELION STAR format
--divide (false) : Divide one huge STAR file into many small ones
--extract_emn (false) : Extract EMAN2 coordinates of helical segments from specified straight tubes
--extract_rln (false) : Extract RELION coordinates of helical segments from specified straight tubes
--extract_xim (false) : Extract XIMDISP coordinates of helical segments from specified straight tubes
--impose_fourier (false) : Impose helical symmetry (simulate what is done in 3D reconstruction in Fourier space)
--init_tilt (false) : Set tilt angles to 90 degrees for all helical segments
--merge (false) : Merge small STAR files into a huge one
--set_xmipp_origin (false) : Set Xmipp origin
--debug (false) : (Debug only)
```
####  Parameters (alphabetically ordered) 
```bash 
--3d_tomo (false) : Simulate 3D subtomograms using a STAR file?
--ang (91.) : Cut out a small part of the helix within this angle (in degrees)
--angpix (-1.) : Pixel size (in Angstroms)
--bimodal (false) : Do bimodal searches of tilt and psi angles in 3D helical reconstruction?
--bin (1) : Binning factor used in manual segment picking
--boxdim (-1) : Box size (in pixels)
--center_pdb (false) : Translate all atoms in the original PDB to the center of mass of this molecule?
--ctf_fom_min (-999) : Minimum figure-of-merit - threshold used in removing micrographs with bad CTF
--cyl_inner_diameter (-1) : Inner diameter of the cylindrical mask (in Angstroms)
--cyl_outer_diameter (-1) : Outer diameter of the cylindrical mask (in Angstroms)
--df_min (-999999.) : Minimum defocus (in Angstroms)
--df_max (999999.) : Maximum defocus (in Angstroms)
--EPA_lowest_res (999) : Lowest EPA resolution (in Angstroms) - threshold used in removing micrographs with bad CTF
--i (file.in) : Input file
--i1 (file01.in) : Input file #1
--i2 (file02.in) : Input file #2
--i_root (_rootnameIn.star) : Rootname of input files
--i1_root (_rootnameIn01.star) : Rootname #1 of input files
--i2_root (_rootnameIn02.star) : Rootname #2 of input files
--ignore_helical_symmetry (false) : Ignore helical symmetry in 3D reconstruction?
--nr_asu (1) : Number of helical asymmetrical units
--nr_outfiles (10) : Number of output files
--nr_subunits (-1) : Number of helical subunits
--nr_tubes (-1) : Number of helical tubes
--o (file.out) : Output file
--o_root (_rootnameOut.star) : Rootname of output files
--polar (false) : Construct a 3D reference for helical reconstruction with polarity along Z axis?
--psi_max_dev (15.) : Maximum deviation of psi angles allowed (away from psi prior)
--random_seed (-1) : Random seed (set to system time if negative)
--rise (-1) : Helical rise (in Angstroms)
--rise_inistep (-1) : Initial step of helical rise search (in Angstroms)
--rise_min (-1) : Minimum helical rise (in Angstroms)
--rise_max (-1) : Maximum helical rise (in Angstroms)
--seam_nr_filaments (-1) : Number of filaments in a helix with seam (>= 2)
--search_sym (false) : Perform local searches of helical symmetry in 3D reconstruction?
--segments (false) : Cut helical tubes into segments?
--sigma_offset (5.) : Sigma of translational offsets (in pixels)
--sigma_psi (5.) : Sigma of psi angles (in degrees)
--sigma_tilt (5.) : Sigma of tilt angles (in degrees)
--sphere_percentage (0.9) : Diameter of spherical mask divided by the box size (0.10~0.90 or 0.01~0.99)
--subunit_diameter (-1) : Diameter of helical subunits (in Angstroms)
--sym_Cn (1) : Rotational symmetry Cn
--tilt_max_dev (15.) : Maximum deviation of tilt angles allowed (away from +90 degrees)
--topbottom_ratio (0.5) : Top-bottom width ratio for construction of polarised helical reference
--twist (-1) : Helical twist (in degrees, + for right-handedness)
--twist_inistep (-1) : Initial step of helical twist search (in degrees)
--twist_min (-1) : Minimum helical twist (in degrees, + for right-handedness)
--twist_max (-1) : Maximum helical twist (in degrees, + for right-handedness)
--verb (false) : Detailed screen output?
--white_noise (1.) : Standard deviation of added white Gaussian noise
--width (5.) : Width of cosine soft edge (in pixels)
--xdim (4096) : Dimension X (in pixels) of the micrographs
--ydim (4096) : Dimension Y (in pixels) of the micrographs
--z_percentage (0.3) : Percentage of cropped length (along Z axis, 0.1~0.9)
--version : Print RELION version and exit
```
---
### relion_helix_vote_classes

####  General options 
```bash 
--i : The _data.star file with the classes to be analysed
--nr_classes : Number of classes in the input star file
--coord_suffix () : The suffix for the coordinate files, e.g. "_picked.star" or ".box"
--pick () : Alternative to coord_suffix: a 2-column STAR file with micrographs and coordinate files
--o (HelixAnalyseClasses/) : Output directory name
--groups () : A string with grouping of comma-separated class numbers (with ':' for separation of groups, e.g. 1,4,5:6,2)
--group_names () : A string with :-separated names for all groups (e.g. phf:sf)
--voting_threshold (0.0) : Minimum fraction to assign a helix to a group
--consistency_check (0.05) : Check this fraction of particles to be on line of start-end coordinates
--min_nr_picks (-1) : Select filaments that have at least this many picks for the group indicated below
--min_picks_group (-1) : Number of the group (first one is 1) to select based on minimum number of particles
--norm (false) : Perform normalisation before voting?
--verb (1) : Verbosity
--version : Print RELION version and exit


