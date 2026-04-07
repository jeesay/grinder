data_
#
_id       refine3d
_label    'Refine3D'
_widget    radio
_parent   refine
_help     ''
_comment  'use_gctf'
_proc_id  0
_labelnew     "relion.import.zzz"                        # PROC_IMPORT_LABELNEW - Import any file as a Node of a given type
_innode       "MicrographMovieGroupMetadata.star.relion" # LABEL_MOVIES_CPIPE
_outnode      "MicrographMovieGroupMetadata.star.relion" # LABEL_IMPORT_MOVIES
_dirname      "Import"                                   # PROC_IMPORT_DIRNAME - Import any file as a Node of a given type
_hidden_name  '.gui_zzz'
#
loop_
_groups.id
_groups.label
_groups.icon
_groups.widget
_groups.default
_groups.parent
_groups.help
io       'I/O'                    bi-arrow-down-up       tab ? ? ?
settings 'Settings'               bi-nut                 tab ? ? ?
display  'Display'                bi-palette             tab ? ? ?
compute  'Compute'                bi-cpu                 tab ? ? ?
running  'Running'                bi-send                tab ? ? ?
result   'Results'                bi-eye                 tab ? ? ?
indata   'Input'                  bi-arrow-bar-down      fieldset ?      io       ?
cont     'Continue Job'           bi-send-plus           fieldset hidden io       ?
outdata  'Output and System'      bi-terminal            fieldset ?      io       ?
general  'General'                bi-chat-right-text     fieldset ?      settings ?
other    'Other Parameters'       bi-chat-right-dots     fieldset ?      settings ?
disk     'Disk Access'            bi-database            fieldset ?      compute  ?    
gpu      'Use GPU Acceleration?'  bi-gpu-card            switch   false  compute  'If set to Yes, the job will try to use GPU acceleration.'
process  'Processes'              bi-gear-fill           fieldset ?      compute  ?
do_queue 'Submit to queue?'       bi-box-arrow-in-right  switch   false  running  'If set to Yes, the job will be submitted to a queue, otherwise the job will be executed locally. Note that only MPI jobs may be sent to a queue. The default can be set through the environment variable RELION_QUEUE_USE.'
command  'Check Command'          bi-terminal-plus       cli      ?      running  'RELION Command as it appears in `note.txt`'
exec     'Execute Command'        bi-send-plus           toolbar  ?      running  'No help'
#
loop_
_indata.id
_indata.label
_indata.widget
_indata.default  # None
_indata.arg0     # Status
_indata.arg1     # Placeholder
_indata.arg2     # Node Type
_indata.help
input_star_mics "Input micrographs STAR file:" file "" required "STAR files (*.star)" LABEL_MICS_CPIPE "A STAR file with all micrographs to run CTFFIND or Gctf on"
#
loop_
_outdata.id
_outdata.label
_outdata.widget
_outdata.default  # None
_outdata.arg0     # filetype
_outdata.arg1     # placeholder
_outdata.arg2     # Directory
_outdata.help
#
prockey       "Process key:"       string_ro PROC_CTFFIND     ? ? ? ?
procid        "Process ID:"        string_ro "2"  ? ? ? ?
labelnew      "Process Label:"     string_ro "relion.ctffind"  ? ? ? ?
has_mpi       "Use mpi?"           string_ro "true"  ? ? ? ?
has_thread    "Use threads?"       string_ro "false" ? ? ? ?
dirname       "Output Directory:"  string_ro "CtfFind" PROC_IMPORT_DIRNAME ? ? ?
outkey0       "Output Node0:"      string_ro LABEL_CTFFIND_MICS  ? ? ? ?
outval0       "Output NodeVal0:"   string_ro "MicrographGroupMetadata.star.relion.ctf"  ? ? ? ?
outfile0      "Output NodeFile0:"  string_ro "micrographs_ctf.star" ? ? ? ?
outkey1       "Output Node1:"      string_ro LABEL_CTFFIND_LOG      ? ? ? ?
outval1       "Output NodeVal1:"   string_ro "LogFile.pdf.relion.ctffind" ? ? ? ?
outfile1      "Output NodeFile1:"  string_ro "logfile.pdf"          ? ? ? ?
#
#
# Command Options
#
loop_
_general.id
_general.label
_general.widget
_general.default
_general.arg0
_general.arg1
_general.arg2
_general.help
fn_img   "Input images STAR file:"    file    LABEL_PARTS_CPIPE    "STAR files (*.star)"    1    ?    "A STAR file with all images (and their metadata)."
fn_cont   "Continue from here: "    file    ?    "STAR Files (*_it*_optimiser.star)"    CURRENT_ODIR    ?
;
Select the *_optimiser.star file for the iteration from which you want to continue a previous run. Note that the Output 
rootname of the continued run and the rootname of the previous run cannot be the same. If they are the same, the program 
will automatically add a '_ctX' to the output rootname, with X being the iteration from which one continues the previous run.
;
fn_ref   "Reference map:"    file    LABEL_MAP_CPIPE    "Image Files (*.{spi,vol,mrc})"    1    ?
;
A 3D map in MRC/Spider format.     Make sure this map has the same dimensions and the same pixel size as your input images, 
or specify that one can resize the reference if needed.
;
fn_mask   "Reference mask (optional):"    file    LABEL_MASK_CPIPE    "Image Files (*.{spi,vol,msk,mrc})"    1    ?
;
If no mask is provided, a soft spherical mask based on the particle diameter will be used.
Otherwise, provide a Spider/mrc map containing a (soft) mask with the same dimensions as the reference(s), and values between 
0 and 1, with 1 being 100% protein and 0 being 100% solvent. The reconstructed reference map will be multiplied by this mask.
In some cases, for example for non-empty icosahedral viruses, it is also useful to use a second mask. For all white (value 1) 
pixels in this second mask the corresponding pixels in the reconstructed map are set to the average value of these pixels. 
Thereby, for example, the higher density inside the virion may be set to a constant. Note that this second mask should have 
one-values inside the virion and zero-values in the capsid and the solvent areas. To use a second mask, use the additional 
option --solvent_mask2, which may given in the Additional arguments line (in the Running tab).
;
ref_correct_greyscale   "Ref. map is on absolute greyscale?"    bool    false    ?    ?    ?
;
Probabilities are calculated based on a Gaussian noise model, which contains a squared difference term between the reference 
and the experimental image. This has a consequence that the reference needs to be on the same absolute intensity grey-scale as 
the experimental images. RELION and XMIPP reconstruct maps at their absolute intensity grey-scale. Other packages may perform 
internal normalisations of the reference density, which will result in incorrect grey-scales. Therefore: if the map was 
reconstructed in RELION or in XMIPP, set this option to Yes, otherwise set it to No. If set to No, RELION will use a (grey-scale 
invariant) cross-correlation criterion in the first iteration, and prior to the second iteration the map will be filtered again 
using the initial low-pass filter. Thisrh.PROCedure is relatively quick and typically does not negatively affect the outcome of
 the subsequent MAP refinement. Therefore, if in doubt it is recommended to set this option to No.
;
trust_ref_size   "Resize reference if needed?"    bool    true    ?    ?    ?
;
If True, and if the input reference map (and mask) do not have the same pixel size and/or box size, then they will be re-scaled 
and re-boxed accordingly. If this option is set to False, then the program will die with an error if the reference does not have 
the correct pixel and/or box size.
;
ini_high   "Initial low-pass filter (A):"    range    60    0    200    5
;
It is recommended to strongly low-pass filter your initial reference map. If it has not yet been low-pass filtered, it may be
 done internally using this option. If set to 0, no low-pass filter will be applied to the initial reference(s).
;
sym_name   "Symmetry:"    string    C1    ?    ?    ?
;
If the molecule is asymmetric, set Symmetry group to C1. Note their are multiple possibilities for icosahedral symmetry: 
 * I1: No-Crowther 222 (standard in Heymann, Chagoyen & Belnap, JSB, 151 (2005) 196–207) 
 * I2: Crowther 222 
 * I3: 52-setting (as used in SPIDER?)
 * I4: A different 52 setting 
 The command 'relion_refine --sym D2 --print_symmetry_ops' prints a list of all symmetry operators for symmetry group D2. 
 RELION uses XMIPP's libraries for symmetry operations. Therefore, look at the XMIPP Wiki for more details: 
  http:#xmipp.cnb.csic.es/twiki/bin/view/Xmipp/WebHome?topic=Symmetry
;
do_ctf_correction   "Do CTF-correction?"    bool    true    ?    ?    ?
;
If set to Yes, CTFs will be applied to the projections of the map. This requires that CTF information is present in the 
input STAR file.
;
ctf_intact_first_peak   "Ignore CTFs until first peak?"    bool    false    ?    ?    ?
;
If set to Yes, then CTF-amplitude correction will only be performed from the first peak of each CTF onward. This can be 
useful if the CTF model is inadequate at the lowest resolution. Still, in general using higher amplitude contrast on the
 CTFs (e.g. 10-20%) often yields better results. Therefore, this option is not generally recommended: try increasing 
 amplitude contrast (in your input STAR file) first!
;
particle_diameter   "Mask diameter (A):"    range    200    0    1000    10
;
The experimental images will be masked with a soft circular mask with this diameter. Make sure this radius is not set too 
small because that may mask away part of the signal! If set to a value larger than the image size no masking will be performed.

The same diameter will also be used for a spherical mask of the reference structures if no user-provided mask is specified.
;
do_zero_mask   "Mask individual particles with zeros?"    bool    true    ?    ?    ?
;
If set to Yes, then in the individual particles, the area outside a circle with the radius of the particle will be set to 
zeros prior to taking the Fourier transform. This will remove noise and therefore increase sensitivity in the alignment and 
classification. However, it will also introduce correlations between the Fourier components that are not modelled. When set 
to No, then the solvent area is filled with random noise, which prevents introducing correlations.High-resolution refinements 
(e.g. ribosomes or other large complexes in 3D auto-refine) tend to work better when filling the solvent area with random noise
 (i.e. setting this option to No), refinements of smaller complexes and most classifications go better when using zeros 
 (i.e. setting this option to Yes).
;
do_solvent_fsc   "Use solvent-flattened FSCs?"    bool    false    ?    ?    ?
;
If set to Yes, then instead of using unmasked maps to calculate the gold-standard FSCs during refinement, masked half-maps are
used and a post-processing-like correction of the FSC curves (with phase-randomisation) is performed every iteration. This 
only works when a reference mask is provided on the I/O tab. This may yield higher-resolution maps, especially when the mask 
contains only a relatively small volume inside the box.
;
do_blush   "Use Blush regularisation?"    bool    false    ?    ?    ?
;
If set to Yes, relion_refine will use a neural network to perform regularisation by denoising at every iteration, instead of 
the standard smoothness regularisation.
;
sampling   "Initial angular sampling:"    select    "7.5 degrees"    sampling_opt    ?    ?
;
There are only a few discrete angular samplings possible because we use the HealPix library to generate the sampling of the 
first two Euler angles on the sphere. The samplings are approximate numbers and vary slightly over the sphere.

Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.
;
offset_range   "Initial offset range (pix):"    range    5    0    30    1
;
Probabilities will be calculated only for translations in a circle with this radius (in pixels). The center of this circle 
changes at every iteration and is placed at the optimal translation for each image in the previous iteration.

 Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.
;
offset_step   "Initial offset step (pix):"    range    1    0.1    5    0.1
;
Translations will be sampled with this step-size (in pixels).Translational sampling is also done using the adaptive approach. 
Therefore, if adaptive=1, the translations will first be evaluated on a 2x coarser grid.
 Note that this will only be the value for the first few iteration(s): the sampling rate will be increased automatically after that.
;
auto_local_sampling   "Local searches from auto-sampling:"    radio    "1.8 degrees"    ?    ?    ?
;
In the automatedrh.PROCedure to increase the angular samplings, local angular searches of -6/+6 times the sampling rate will 
be used from this angular sampling rate onwards. For most lower-symmetric particles a value of 1.8 degrees will be sufficient.
Perhaps icosahedral symmetries may benefit from a smaller value such as 0.9 degrees.
;
auto_local_sampling_opt_00  "30 degrees"    option    0    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_01  "15 degrees"    option    1    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_02  "7.5 degrees"    option    2    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_03  "3.7 degrees"    option    3    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_04  "1.8 degrees"    option    4    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_05  "0.9 degrees"    option    5    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_06  "0.5 degrees"    option    6    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_07  "0.2 degrees"    option    7    auto_local_sampling    ?    ?   ?
auto_local_sampling_opt_08  "0.1 degrees"    option    8    auto_local_sampling    ?    ?   ?
relax_sym   "Relax symmetry:"    string   "?"   ?    ?    ?
;
With this option, poses related to the standard local angular search range by the given point group will also be explored. 
For example, if you have a pseudo-symmetric dimer A-A', refinement or classification in C1 with symmetry relaxation by C2 
might be able to improve distinction between A and A'. Note that the reference must be more-or-less aligned to the convention 
of (pseudo-)symmetry operators. For details, see Ilca et al 2019 and Abrishami et al 2020 cited in the About dialog.
;
auto_faster   "Use finer angular sampling faster?"    bool    false    ?    ?    ?
;
If set to Yes, then let auto-refinementrh.PROCeed faster with finer angular samplings. Two additional command-line options will 
be passed to the refine program: 
 
 --auto_ignore_angles lets angular sampling go down despite changes still happening in the angles 
 
 --auto_resol_angles lets angular sampling go down if the current resolution already requires that sampling at the edge of the particle.  

 This option will make the computation faster, but hasn't been tested for many cases for potential loss in reconstruction quality 
 upon convergence.
;
do_helix   "Do helical reconstruction?"    bool    false    ?    ?    ?    "If set to Yes, then perform 3D helical reconstruction."
helical_tube_inner_diameter   "Tube diameter - inner (A):"    string    -1    ?    ?    ?
;
Inner and outer diameter (in Angstroms) of the reconstructed helix spanning across Z axis. Set the inner diameter to negative value 
if the helix is not hollow in the center. The outer diameter should be slightly larger than the actual width of helical tubes because 
it also decides the shape of 2D particle mask for each segment. If the psi priors of the extracted segments are not accurate enough 
due to high noise level or flexibility of the structure, then set the outer diameter to a large value.
;
helical_tube_outer_diameter   "Tube diameter - outer (A):"    string    -1    ?    ?    ?
;
Inner and outer diameter (in Angstroms) of the reconstructed helix spanning across Z axis. Set the inner diameter to negative value 
if the helix is not hollow in the center. The outer diameter should be slightly larger than the actual width of helical tubes because 
it also decides the shape of 2D particle mask for each segment. If the psi priors of the extracted segments are not accurate enough 
due to high noise level or flexibility of the structure, then set the outer diameter to a large value.
;
range_rot   "Angular search range - rot (deg):"    string    -1    ?    ?    ?
;
Local angular searches will be performed within +/- of the given amount (in degrees) from the optimal orientation in the previous 
iteration. The default negative value means that no local searches will be performed. A Gaussian prior will be applied, so that 
orientations closer to the optimal orientation in the previous iteration will get higher weights than those further away.

These ranges will only be applied to the rot, tilt and psi angles in the first few iterations (global searches for orientations) in 
3D helical reconstruction. Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible structures 
and more memory and computation time will be used. A range of 15 degrees means sigma = 5 degrees.

These options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.
;
range_tilt   "Angular search range - tilt (deg):"    string    15    ?    ?    ?
;
Local angular searches will be performed within +/- the given amount (in degrees) from the optimal orientation in the previous 
iteration. A Gaussian prior (also see previous option) will be applied, so that orientations closer to the optimal orientation 
in the previous iteration will get higher weights than those further away.

These ranges will only be applied to the rot, tilt and psi angles in the first few iterations (global searches for orientations) 
in 3D helical reconstruction. Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible structures 
and more memory and computation time will be used. A range of 15 degrees means sigma = 5 degrees.
These options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.
;
range_psi   "Angular search range - psi (deg):"    string    10    ?    ?    ?
;
Local angular searches will be performed within +/- the given amount (in degrees) from the optimal orientation in the previous 
iteration. A Gaussian prior (also see previous option) will be applied, so that orientations closer to the optimal orientation 
in the previous iteration will get higher weights than those further away.
These ranges will only be applied to the rot, tilt and psi angles in the first few iterations (global searches for orientations) 
in 3D helical reconstruction. Values of 9 or 15 degrees are commonly used. Higher values are recommended for more flexible 
structures and more memory and computation time will be used. A range of 15 degrees means sigma = 5 degrees.

These options will be invalid if you choose to perform local angular searches or not to perform image alignment on 'Sampling' tab.
;
do_apply_helical_symmetry   "Apply helical symmetry?"    bool    true    ?    ?    ?
;
If set to Yes, helical symmetry will be applied in every iteration. Set to No if you have just started a project, helical symmetry 
is unknown or not yet estimated.
;
helical_nr_asu   "Number of unique asymmetrical units:"    range    1    1    100    1
;
Number of unique helical asymmetrical units in each segment box. If the inter-box distance (set in segment picking step) is 
100 Angstroms and the estimated helical rise is ~20 Angstroms, then set this value to 100 / 20 = 5 (nearest integer). This integer 
should not be less than 1. The correct value is essential in measuring the signal to noise ratio in helical reconstruction.
;
helical_twist_initial   "Initial helical twist (deg):"    string    0    ?    ?    ?
;
Initial helical symmetry. Set helical twist (in degrees) to positive value if it is a right-handed helix. Helical rise is a positive 
value in Angstroms. If local searches of helical symmetry are planned, initial values of helical twist and rise should be within 
their respective ranges.
;
helical_rise_initial   "Initial helical rise (A):"    string    0    ?    ?    ?
;
Initial helical symmetry. Set helical twist (in degrees) to positive value if it is a right-handed helix. Helical rise is a positive 
value in Angstroms. If local searches of helical symmetry are planned, initial values of helical twist and rise should be within 
their respective ranges.
;
helical_z_percentage   "Central Z length (%):"    range    30.0    5.0    80.0    1.0
;
Reconstructed helix suffers from inaccuracies of orientation searches. The central part of the box contains more reliable information
compared to the top and bottom parts along Z axis, where Fourier artefacts are also present if the number of helical asymmetrical 
units is larger than 1. Therefore, information from the central part of the box is used for searching and imposing helical symmetry 
in real space. Set this value (%) to the central part length along Z axis divided by the box size. Values around 30% are commonly used.
;
do_local_search_helical_symmetry   "Do local searches of symmetry?"    bool    false    ?    ?    ?
;
If set to Yes, then perform local searches of helical twist and rise within given ranges.
;
helical_twist_min   "Helical twist search (deg) - Min:"    string    0    ?    ?    ?
;
Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) to positive value if it is a right-handed 
helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). 
But it needs to be set manually if the default value does not guarantee convergence. The program cannot find a reasonable symmetry
if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical 
and point group symmetry are provided.
;
helical_twist_max   "Helical twist search (deg) - Max:"    string    0    ?    ?    ?
;
Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) to positive value if it is a right-handed 
helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). But 
it needs to be set manually if the default value does not guarantee convergence. The program cannot find a reasonable symmetry if the 
True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point 
group symmetry are provided.
;
helical_twist_inistep   "Helical twist search (deg) - Step:"    string    0    ?    ?    ?
;
Minimum, maximum and initial step for helical twist search. Set helical twist (in degrees) to positive value if it is a right-handed 
helix. Generally it is not necessary for the user to provide an initial step (less than 1 degree, 5~1000 samplings as default). But 
it needs to be set manually if the default value does not guarantee convergence. The program cannot find a reasonable symmetry if the 
True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point 
group symmetry are provided.
;
helical_rise_min   "Helical rise search (A) - Min:"    string    0    ?    ?    ?
;
Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. Generally it is not necessary 
for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set
manually if the default value does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical 
parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry 
are provided.
;
helical_rise_max   "Helical rise search (A) - Max:"    string    0    ?    ?    ?
;
Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. Generally it is not necessary 
for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set 
manually if the default value does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.
;
helical_rise_inistep   "Helical rise search (A) - Step:"    string    0    ?    ?    ?
;
Minimum, maximum and initial step for helical rise search. Helical rise is a positive value in Angstroms. Generally it is not necessary for the user to provide an initial step (less than 1% the initial helical rise, 5~1000 samplings as default). But it needs to be set manually if the default value does not guarantee convergence. The program cannot find a reasonable symmetry if the True helical parameters fall out of the given ranges. Note that the final reconstruction can still converge if wrong helical and point group symmetry are provided.
;
helical_range_distance   "Range factor of local averaging:"    range    -1.0    1.0    5.0    0.1
;
Local averaging of orientations and translations will be performed within a range of +/- this value * the box size. Polarities are also set to be the same for segments coming from the same tube during local refinement. Values of ~ 2.0 are recommended for flexible structures such as MAVS-CARD filaments, ParM, MamK, etc. This option might not improve the reconstructions of helices formed from curled 2D lattices (TMV and VipA/VipB). Set to negative to disable this option.
;
keep_tilt_prior_fixed   "Keep tilt-prior fixed:"    bool    true    ?    ?    ?
;
If set to yes, the tilt prior will not change during the optimisation. If set to No, at each iteration the tilt prior will move to the optimal tilt value for that segment from the previous iteration.
;
do_parallel_discio   "Use parallel disc I/O?"    bool    true    ?    ?    ?
;
If set to Yes, all MPI followers will read their own images from disc. Otherwise, only the leader will read images and send them through the network to the followers. Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.
;
nr_pool   "Number of pooled particles:"    range    3    1    16    1
;
Particles arerh.PROCessed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.
;
do_pad1   "Skip padding?"    bool    false    ?    ?    ?
;
If set to Yes, the calculations will not use padding in Fourier space for better interpolation in the references. Otherwise, references are padded 2x before Fourier transforms are calculated. Skipping padding (i.e. use --pad 1) gives nearly as good results as using --pad 2, but some artifacts may appear in the corners from signal that is folded back.
;
do_preread_images   "Pre-read all particles into RAM?"    bool    false    ?    ?    ?
;
If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. Because particles are read in float-precision, it will take ( N * box_size * box_size * 8 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM. 
 
 If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.
;
scratch_dir   "Copy particles to scratch directory:"    string    RELION_SCRATCH_DIR    ?    ?    ?
;
If a directory is provided here, then the job will create a sub-directory in it called relion_volatile. If that relion_volatile directory already exists, it will be wiped. Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory. Provided this directory is on a fast local drive (e.g. an SSD drive),rh.PROCessing in all the iterations will be faster. If the job finishes correctly, the relion_volatile directory will be wiped. If the job crashes, you may want to remove it yourself.
;
do_combine_thru_disc   "Combine iterations through disc?"    bool    false    ?    ?    ?
;
If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results. The MPI leader will read in all these files, combine them all, and write out a new file with the combined results. All MPI salves will then read in the combined results. This reduces heavy load on the network, but increases load on the disc I/O. This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step. It will depend on your system setup which is most efficient.
;
use_gpu   "Use GPU acceleration?"    bool    false    ?    ?    ?    "If set to Yes, the job will try to use GPU acceleration."
gpu_ids   "Which GPUs to use:"    string   ""  ?    ?    ?
;
This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','.  For example: '0,0:1,1:0,0:1,1'
;
#
loop_
_sampling.id
_sampling.label
_sampling.widget
_sampling.default
_sampling.arg0
_sampling.arg1
_sampling.arg2
_sampling.help
sampling_opt_00  "30 degrees"    option    0   ?    ?    ?   ?
sampling_opt_01  "15 degrees"    option    1   ?    ?    ?   ?
sampling_opt_02  "7.5 degrees"   option    2   ?    ?    ?   ?
sampling_opt_03  "3.7 degrees"   option    3   ?    ?    ?   ?
sampling_opt_04  "1.8 degrees"   option    4   ?    ?    ?   ?
sampling_opt_05  "0.9 degrees"   option    5   ?    ?    ?   ?
sampling_opt_06  "0.5 degrees"   option    6   ?    ?    ?   ?
sampling_opt_07  "0.2 degrees"   option    7   ?    ?    ?   ?
sampling_opt_08  "0.1 degrees"   option    8   ?    ?    ?   ?
#
loop_
_other.id
_other.label
_other.widget
_other.default
_other.arg0
_other.arg1
_other.arg2
_other.help
other_args 'Additional Arguments' string '' ? ? ? 'Additional arguments that need to be passed'
#
loop_
_disk.id
_disk.label
_disk.widget
_disk.default
_disk.arg0
_disk.arg1
_disk.arg2
_disk.help
do_parallel_discio 'Use parallel disc I/O?' bool true ? ? ?
; If set to Yes, all MPI followers will read images from disc. Otherwise, only the leader will read images and send them through the network to the followers. 
Parallel file systems like gluster of fhgfs are good at parallel disc I/O. NFS may break with many followers reading in parallel. If your datasets contain particles with different box sizes, you have to say Yes.
;
nr_pool 'Number of pooled particles:' range 3 1 16 1 
;Particles are processed in individual batches by MPI followers. During each batch, a stack of particle images is only opened and closed once to improve disk access times. \
All particle images of a single batch are read into memory together. The size of these batches is at least one particle per thread used. The nr_pooled_particles parameter controls how many particles are read together for each thread. If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together. \
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem. It has a modest cost of increased RAM usage.
;
do_preread_images 'Pre-read all particles into RAM?' bool false ? ? ?
;If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access. However, one should of course be careful with the amount of RAM available. 
Because particles are read in float-precision, it will take ( N * box_size * box_size * 4 / (1024 * 1024 * 1024) ) Giga-bytes to read N particles into RAM. 
For 100 thousand 200x200 images, that becomes 15Gb, or 60 Gb for the same number of 400x400 particles. 
Remember that running a single MPI follower on each node that runs as many threads as available cores will have access to all available RAM. 

If parallel disc I/O is set to No, then only the leader reads all particles into RAM and sends those particles through the network to the MPI followers during the refinement iterations.
;
scratch_dir 'Copy particles to scratch directory:' file default_scratch ? ? ?
;If a directory is provided here, then the job will create a sub-directory in it called relion_volatile. If that relion_volatile directory already exists, it will be wiped. Then, the program will copy all input particles into a large stack inside the relion_volatile subdirectory. 
Provided this directory is on a fast local drive (e.g. an SSD drive), processing in all the iterations will be faster. If the job finishes correctly, the relion_volatile directory will be wiped. If the job crashes, you may want to remove it yourself.
;
do_combine_thru_disc 'Combine iterations through disc?' bool false ? ? ? 
;If set to Yes, at the end of every iteration all MPI followers will write out a large file with their accumulated results. The MPI leader will read in all these files, combine them all, and write out a new file with the combined results. 
All MPI salves will then read in the combined results. This reduces heavy load on the network, but increases load on the disc I/O. 
This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step. It will depend on your system setup which is most efficient.
;
#
loop_
_gpu.id
_gpu.label
_gpu.widget
_gpu.default
_gpu.arg0
_gpu.arg1
_gpu.arg2
_gpu.help
gpu_ids 'Which GPUs to use:' string '' ? ? ?
;This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','. For example: '0,0:1,1:0,0:1,1'
;
#
loop_
_do_queue.id
_do_queue.label
_do_queue.widget
_do_queue.default
_do_queue.arg0
_do_queue.arg1
_do_queue.arg2
_do_queue.help
load_queue '' import './spa/00_home/qsub.star' ? ? ? ?
#
loop_
_process.id
_process.label
_process.widget
_process.default
_process.arg0
_process.arg1
_process.arg2
_process.help
nr_mpi "Number of MPI procs:" range '{QSUB_NRMPI_VAL}' 1 '{RELION_MPI_MAX}' 1 "Number of MPI nodes to use in parallel. When set to 1, MPI will not be used. The maximum can be set through the environment variable RELION_MPI_MAX."
nr_threads "Number of threads:" range '{QSUB_NRTHREADS_VAL}' 1 "{RELION_THREAD_MAX}" 1 "Number of shared-memory (POSIX) threads to use in parallel. When set to 1, no multi-threading will be used. The maximum can be set through the environment variable RELION_THREAD_MAX."
#
loop_
_cont.id
_cont.label
_cont.widget
_cont.default
_cont.arg0     # filetype
_cont.arg1     # placeholder
_cont.arg2     # directory
_cont.help
fn_cont "Continue from here: " file  ? ? "STAR Files (*_optimiser.star)" CURRENT_ODIR 
;Select the `*_optimiser.star` file for the iteration \
from which you want to continue a previous run. \
Note that the Output rootname of the continued run and the rootname of the previous run cannot be the same. \
If they are the same, the program will automatically add a `_ctX` to the output rootname, \
with X being the iteration from which one continues the previous run.
;
#
loop_
_exec.id
_exec.label
_exec.widget
_exec.default  # visibility
_exec.arg0     # ?
_exec.arg1     # icon
_exec.arg2     # parent
_exec.help
do_schedule 'Schedule' button true  ? bi-calendar-plus ? 'No help'
do_run      'Run!'     button true  ? bi-send          ? 'No help'
do_continue 'Continue' button false ? bi-send-plus  ? 'No help'
#
loop_
_command.type
_command.content
_command.flag
_command.bool
prog     '`which relion_run_ctffind_mpi`' nr_mpi 2+
prog     '`which relion_run_ctffind`' nr_mpi 1
io       '--i {input_star_mics} --o {dirname}/job{LAST_JOBID}' ? ?
param    '--Box {box} --ResMin {resmin} --ResMax {resmax}' ? ?
param    '--dFMin {dfmin} --dFMax {dfmax} --FStep {dfstep} --dAst {dast}' ? ?
flag     '--use_noDW' use_noDW  true 
flag     '--do_phaseshift --phase_min {phase_min} --phase_max {phase_max} --phase_step {phase_step}' do_phaseshift true
param    '--ctffind_exe {fn_ctffind_exe} --ctfWin {ctf_win} --is_ctffind4' ? ?
flag     '--fast_search' slow_search false
flag     '--use_given_ps' use_given_ps true
flag     '--only_do_unfinished ' is_continue true
param    '--j {nr_threads}' ? ?
param    '{other_args}'     ? ?
param    '--pipeline_control {dirname}/job{LAST_JOBID}' ? ?
#

