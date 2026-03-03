TOGGLE_UNKNOWN = 0
TOGGLE_DEACTIVATE = 1
TOGGLE_LEAVE_ACTIVE = 2
TOGGLE_REACTIVATE = 3

group_unk,group0, group1, group2, group3, group4, group5, group6, group7, group8 = [-1,0,1,2,3,4,5,6,7,8]

class Widget:
    def __init__(self,parent,id,group,toggle=TOGGLE_UNKNOWN,flag=False):
        self.id = id
        # self.parent = parent
        self.toggle = toggle
        self.group = group
        self.flag = flag
        self.label = '"No label"'
        self.widget = '?'
        self.value = '?'
        self.arg0 = '?'
        self.arg1 = '?'
        self.arg2 = '?'
        self.help = '"No Help"'

    # Copy from joboption
    def set_options(self,jo):
        self.label = f'"{jo.label}"'
        self.widget = jo.widget
        self.value = jo.value
        self.arg0 = jo.arg0 if isinstance(jo.arg0, int) or isinstance(jo.arg0, float) else f'"{jo.arg0}"'
        self.arg1 = jo.arg1
        self.arg2 = jo.arg2
        self.help = jo.help

    def to_star(self):
        if self.help[0] == ';':
            return f'{self.id:<20} {self.label:<35} {self.widget:<10} {self.value:<15} {self.arg0:<15} {self.arg1:<15} {self.arg2:<15}\n{self.help}\n'
        elif len(self.help) > 60:
            helptxt = '\n; ' + '.\n'.join(self.help.split('. ')) + '\n;'
            return f'{self.id:<20} {self.label:<35} {self.widget:<10} {self.value:<15} {self.arg0:<15} {self.arg1:<15} {self.arg2:<15} {helptxt}\n'
        else:
            return f'{self.id:<20} {self.label:<35} {self.widget:<10} {self.value:<15} {self.arg0:<15} {self.arg1:<15} {self.arg2:<15} "{self.help}"\n'
    
    def __repr__(self):
        return self.__dict__
    
    def __str__(self):
        return str(self.__dict__)

class Fieldset:
    def __init__(self,parent,id="general",name='General',type="fieldset",icon="?"):
        self.fsid = id
        self.parent = parent # group of fieldset
        self.fsname = f'"{name}"'   # aka label
        self.group = parent.current_group
        self.default = '?'
        self.help = '?'
        self.widget = type
        self.icon = 'bi-chat-right-text' if icon == '?' else icon

        self.widgets = []

    @property
    def current_group(self):
        return self.parent.current_group
    
    @current_group.setter
    def current_group(self,grp):
        self.parent.current_group = grp
    
    def append(self,w,force=False):
        if not force and len(self.widgets) == 0 and w.id[0:3] == 'do_':
            self.fsid = w.id[3:]
            self.fsname = ' '.join([word.capitalize() for word in w.id[3:].replace('_',' ').split(' ')])
            self.fsname = f'"{self.fsname}"'
        self.widgets.append(w)

    def delete(self,widget_id):
        index = [ x.id for x in self.widgets ].index(widget_id)
        del self.widgets[index]

    def end(self):
        # Finalize something
        self.parent.append(self)

    def is_empty(self):
        return len(self.widgets) == 0

    def __iter__(self):
            for fs in self.widgets:
                yield fs

    def __len__(self):
        return len(self.widgets)
    
    def to_star(self):
        header = f'loop_\n_{self.fsid}.id\n_{self.fsid}.label\n_{self.fsid}.widget\n_{self.fsid}.default\n_{self.fsid}.arg0\n_{self.fsid}.arg1\n_{self.fsid}.arg2\n_{self.fsid}.help\n'
        content = ''.join([w.to_star() for w in self.widgets])
        return header + content + '#\n'

    def __repr__(self):
        return f'**{self.widget.capitalize()}**{self.fsid}:{self.fsname}[{len(self.widgets)}]\n' + '\n'.join([str(w) for w in self.widgets]) + '\n'

class FsGroup:
    def __init__(self):
        self.groups = [] # List of Fieldset
        self.current_group = group1
        self.param_count = 1

    def get(self,index):
        return self.groups[index]
    
    def append(self,fs):
        if any(f.fsid == 'general' for f in self.groups) and fs.fsid == 'general':
            fs.fsid = f'params_{self.param_count:02}'
            fs.fsname = '"Parameters"'
            self.param_count += 1
        self.groups.append(fs)

    def __iter__(self):
            for fs in self.groups:
                yield fs

    def __len__(self):
        return len(self.groups)
    
    def __repr__(self):
        return '\n'.join([str(fs) for fs in self.groups])

def place(parent,id,toggle=TOGGLE_UNKNOWN,grp=group_unk,flag=True,force=False):
    if 'fn_in' in id or 'input_' in id or "fn_img" in id or "fn_cont" in id or id == "fn_ref" or id == "fn_mask":
        parent.fsid = 'indata'
        parent.fsname = '"Input Data"'
        parent.icon = 'bi-box-arrow-in-down'
    fs = parent
    if grp == group_unk:
        grp = fs.current_group  
    elif parent.group != grp and len(fs) == 0:
        fs.group = grp
        fs.current_group = grp
    elif parent.group != grp:
        parent.end()
        fs = Fieldset(parent.parent)
        fs.group = grp
        fs.current_group = grp
        # parent.parent.current_group = grp

    fs.append(Widget(parent,id,grp, toggle, flag),force)
    return fs

def place2(parent,id1,id2,label,toggle):
    # two widgets
    parent.append(Widget(parent,id1,parent.group,toggle))
    parent.append(Widget(parent,id2,parent.group,toggle))
    return parent

def place3(parent,id1,id2,id3,label,toggle):
    # three widgets
    parent.append(Widget(parent,id1,parent.group,toggle))
    parent.append(Widget(parent,id2,parent.group,toggle))
    parent.append(Widget(parent,id3,parent.group,toggle))
    return parent

def placeTomoInput(has_tomograms, has_particles, has_trajectories, has_manifolds):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"in_optimisation", TOGGLE_DEACTIVATE)
    grp = place(grp,"use_direct_entries", TOGGLE_DEACTIVATE, group0, False)
    if has_particles:
        grp = place(grp,"in_particles", TOGGLE_DEACTIVATE)
    if has_tomograms:
        grp = place(grp,"in_tomograms", TOGGLE_DEACTIVATE)
    if has_trajectories:
        grp = place(grp,"in_trajectories", TOGGLE_DEACTIVATE)
    if has_manifolds:
        grp = place(grp,"in_manifolds", TOGGLE_DEACTIVATE)
    grp.end()
    
    return groups

######################  INITIALISE ##################""""""
def initialiseImportWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"do_raw", TOGGLE_DEACTIVATE, group1, False)
    grp.end()
    grp = Fieldset(groups)
    grp = place(grp,"fn_in_raw")
    grp = place(grp,"is_multiframe")
    grp.end()

    grp = Fieldset(groups,"optics_group","Optics Group",icon="bi-eye")
    grp = place(grp,"optics_group_name")
    grp = place(grp,"fn_mtf")
    grp = place(grp,"angpix")
    grp = place(grp,"kV")
    grp = place(grp,"Cs")
    grp = place(grp,"Q0")
    grp = place(grp,"beamtilt_x")
    grp = place(grp,"beamtilt_y")
    # grp = place(grp,"do_other", TOGGLE_DEACTIVATE, group2, False)
    grp.end()
    
    grp = Fieldset(groups, "do_other", "Import other node types", type="switch")
    grp = place(grp,"fn_in_other")
    grp = place(grp,"node_type")
    # grp.end()
    
    # grp = Fieldset(groups)
    grp = place(grp,"optics_group_particles")
    grp.end()
    

    return groups

def initialiseMotioncorrWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"input_star_mics", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    if not is_tomo:
        grp = place(grp,"first_frame_sum", TOGGLE_DEACTIVATE)
    if not is_tomo:
        grp = place(grp,"last_frame_sum", TOGGLE_DEACTIVATE)
    if not is_tomo:
        grp = place(grp,"dose_per_frame", TOGGLE_DEACTIVATE)
    if not is_tomo:
        grp = place(grp,"pre_exposure", TOGGLE_DEACTIVATE)
    grp = place(grp,"eer_grouping", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_float16", TOGGLE_DEACTIVATE)
    if is_tomo:
        grp = place(grp,"do_even_odd_split")
    grp.end()
    
    grp = Fieldset(groups,"do_dose_weighting","Dose Weighting",type="switch")
    #grp = place(grp,"do_dose_weighting", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"do_save_noDW", TOGGLE_DEACTIVATE,force=True)
    grp.end()
    
    grp = Fieldset(groups,"do_save_ps","Save Power Spectrum",type="switch")
    # grp = place(grp,"do_save_ps", TOGGLE_DEACTIVATE, group2)
    grp = place(grp,"group_for_ps", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"bfactor", TOGGLE_DEACTIVATE)
    grp = place2(grp,"patch_x", "patch_y", "Number of patches X, Y", TOGGLE_DEACTIVATE)
    grp = place(grp,"group_frames", TOGGLE_DEACTIVATE)
    grp = place(grp,"bin_factor", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_gain_ref", TOGGLE_DEACTIVATE)
    grp = place(grp,"gain_rot", TOGGLE_DEACTIVATE)
    grp = place(grp,"gain_flip", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_defect", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups,"do_own_motioncor","RELIONS's implementation")
    # grp = place(grp,"do_own_motioncor", TOGGLE_DEACTIVATE, group4, True)
    grp = place(grp,"fn_motioncor2_exe", TOGGLE_DEACTIVATE)
    grp = place(grp,"gpu_ids")
    grp = place(grp,"other_motioncor2_args", TOGGLE_DEACTIVATE)

    grp.end()
    
    return groups

def initialiseCtffindWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"input_star_mics", TOGGLE_DEACTIVATE)
    if not is_tomo:
        grp = place(grp,"use_noDW", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups,"do_phaseshift","Estimate phase shifts", type="switch")
    # grp = place(grp,"do_phaseshift", TOGGLE_DEACTIVATE, group1)
    grp = place3(grp, "phase_min", "phase_max", "phase_step", "Phase shift - Min, Max, Step (deg)", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"dast", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_ctffind_exe", TOGGLE_DEACTIVATE)
    grp = place(grp,"use_given_ps", TOGGLE_DEACTIVATE)
    grp = place(grp,"slow_search", TOGGLE_DEACTIVATE)
    grp = place(grp,"ctf_win", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"box", TOGGLE_DEACTIVATE)
    grp = place(grp,"resmin", TOGGLE_DEACTIVATE)
    grp = place(grp,"resmax", TOGGLE_DEACTIVATE)
    grp = place(grp,"dfmin", TOGGLE_DEACTIVATE)
    grp = place(grp,"dfmax", TOGGLE_DEACTIVATE)
    grp = place(grp,"dfstep", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"localsearch_nominal_defocus", TOGGLE_DEACTIVATE)
    grp = place(grp,"exp_factor_dose", TOGGLE_DEACTIVATE)

    grp.end()
    
    return groups

def initialiseManualpickWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_in", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place (grp, "do_startend")
    grp.end()
    
    grp = Fieldset(groups, "do_fom_threshold", "Use autopick FOM threshold", type="switch")
    # grp = place(grp,"do_fom_threshold", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"minimum_pick_fom", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"diameter")
    grp = place(grp,"micscale")
    grp = place(grp,"sigma_contrast")
    grp = place(grp,"white_val")
    grp = place(grp,"black_val")
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"lowpass")
    grp = place(grp,"highpass")
    grp = place(grp,"angpix")
    grp = place(grp,"do_topaz_denoise", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups, "do_color", "Blue<>red color particles", type="switch")
    # grp = place(grp,"do_color", TOGGLE_LEAVE_ACTIVE, group3)
    grp = place(grp,"color_label")
    grp = place(grp,"fn_color")
    grp = place(grp,"blue_value")
    grp = place(grp,"red_value")

    grp.end()
    
    return groups

def initialiseAutopickWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_input_autopick", TOGGLE_DEACTIVATE)
    grp = place(grp,"angpix", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"do_refs", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_log", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_topaz", TOGGLE_DEACTIVATE)
    grp = place(grp,"continue_manual", TOGGLE_REACTIVATE)
    grp = place(grp,"log_diam_min", TOGGLE_DEACTIVATE)
    grp = place(grp,"log_diam_max", TOGGLE_DEACTIVATE)
    grp = place(grp,"log_invert", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"log_maxres", TOGGLE_DEACTIVATE)
    grp = place(grp,"log_adjust_thr")
    grp = place(grp,"log_upper_thr")
    grp = place(grp,"fn_topaz_exe", TOGGLE_DEACTIVATE)
    grp = place(grp,"topaz_particle_diameter", TOGGLE_DEACTIVATE)
    grp.end()

    grp = Fieldset(groups)
    grp = place(grp,"do_topaz_train", TOGGLE_DEACTIVATE, group5)
    grp = place(grp,"topaz_nr_particles", TOGGLE_DEACTIVATE)
    grp = place(grp,"topaz_train_picks", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_topaz_train_parts", TOGGLE_DEACTIVATE, group6)
    grp = place(grp,"topaz_train_parts", TOGGLE_DEACTIVATE)
    grp.end()

    grp = Fieldset(groups)
    grp = place(grp,"do_topaz_pick", TOGGLE_DEACTIVATE, group7)
    grp = place(grp,"topaz_model", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_topaz_filaments", TOGGLE_DEACTIVATE, group8)
    grp = place2(grp,"topaz_filament_threshold", "topaz_hough_length", "Threshold, Hough length (A)", TOGGLE_DEACTIVATE)
    grp.end()

    grp = Fieldset(groups)
    grp = place(grp,"topaz_other_args", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_refs_autopick", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_ref3d", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"fn_ref3d_autopick", TOGGLE_DEACTIVATE)
    grp = place(grp,"ref3d_symmetry", TOGGLE_DEACTIVATE)
    grp = place(grp,"ref3d_sampling", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"lowpass", TOGGLE_DEACTIVATE)
    grp = place(grp,"highpass", TOGGLE_DEACTIVATE)
    grp = place(grp,"angpix_ref", TOGGLE_DEACTIVATE)
    grp = place(grp,"psi_sampling_autopick", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_invert_refs", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_ctf_autopick", TOGGLE_DEACTIVATE, group2)
    grp = place(grp,"do_ignore_first_ctfpeak_autopick", TOGGLE_DEACTIVATE) 
    # (current_y, "Ignore CTFs until first peak?", False,"Set this to Yes, only if this option was also used to generate the references.")
    grp = place(grp,"threshold_autopick")
    grp = place(grp,"mindist_autopick")
    grp = place(grp,"maxstddevnoise_autopick")
    grp = place(grp,"minavgnoise_autopick")
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"do_write_fom_maps")
    grp = place(grp,"do_read_fom_maps")
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"shrink", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups,"gpu","GPU")
    grp = place(grp,"use_gpu", TOGGLE_LEAVE_ACTIVE, group3)
    grp = place(grp,"gpu_ids")
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"do_pick_helical_segments", TOGGLE_DEACTIVATE, group4)
    grp = place(grp,"helical_tube_outer_diameter")
    grp = place(grp,"helical_tube_length_min")
    grp = place(grp,"helical_tube_kappa_max")
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"helical_nr_asu")
    grp = place(grp,"helical_rise")
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"do_amyloid")

    grp.end()
    
    return groups

def initialiseExtractWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"star_mics", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"coords_suffix", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups, "do_reextract", "OR re-extract refined particles", type="switch")
    # grp = place(grp,"do_reextract", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"fndata_reextract", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_reset_offsets", TOGGLE_DEACTIVATE)
    grp.end()

    grp = Fieldset(groups, "do_recenter", "Re-center refined coordinates", type="switch")
    # grp = place(grp,"do_recenter", TOGGLE_DEACTIVATE, group7)
    grp = place3(grp, "recenter_x","recenter_y", "recenter_z", "Recenter on - X, Y, Z (pix):", TOGGLE_DEACTIVATE)
    
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"do_float16", TOGGLE_DEACTIVATE)
    # (current_y,"Particle box size (pix):", 128, 64, 512, 8, "Size of the extracted particles (in pixels). This should be an even number!")
    grp = place(grp,"extract_size", TOGGLE_DEACTIVATE) 
    # (current_y, "Invert contrast?", True, "If set to Yes, the contrast in the particles will be inverted.")
    grp = place(grp,"do_invert", TOGGLE_DEACTIVATE) 
    grp.end()
    
    grp = Fieldset(groups, "do_norm", "Normalize particles?", type="switch")
    # grp = place(grp,"do_norm", TOGGLE_DEACTIVATE, group3)
    # (current_y, "Diameter background circle (pix): ", -1, -1, 600, 10, 
    # "Particles will be normalized to a mean value of zero and a standard-deviation of one for all pixels in the background area.\
    grp = place(grp,"bg_diameter", TOGGLE_DEACTIVATE) 
    # (current_y, "Stddev for white dust removal: ", -1, -1, 10, 0.1, "Remove very white pixels from the extracted particles. \
    # Pixels values higher than this many times the image stddev will be regrp = placed with values from a Gaussian distribution. 
    # \n \n Use negative value to switch off dust removal.")
    grp = place(grp,"white_dust", TOGGLE_DEACTIVATE) 
    # (current_y, "Stddev for black dust removal: ", -1, -1, 10, 0.1, "Remove very black pixels from the extracted particles. \
    # Pixels values higher than this many times the image stddev will be regrp = placed with values from a Gaussian distribution. \n \n 
    # Use negative value to switch off dust removal.")
    grp = place(grp,"black_dust", TOGGLE_DEACTIVATE) 
    grp.end()
    
    grp = Fieldset(groups, "do_rescale", "Rescale particles?", type="switch")
    # grp = place(grp,"do_rescale", TOGGLE_DEACTIVATE, group4)
    grp = place(grp,"rescale", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups, "do_fom_threshold", "Use autopick FOM threshold?", type="switch")
    # grp = place(grp,"do_fom_threshold", TOGGLE_DEACTIVATE, group7)
    grp = place(grp,"minimum_pick_fom", TOGGLE_DEACTIVATE)
    grp.end()

    grp = Fieldset(groups, "do_extract_helix", "Extract helical segments", type="switch")
    # grp = place(grp,"do_extract_helix", TOGGLE_DEACTIVATE, group5)
    grp = place(grp,"helical_tube_outer_diameter", TOGGLE_DEACTIVATE)
    # grp.end()
    
    # grp = Fieldset(groups)
    grp = place(grp,"helical_bimodal_angular_priors", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups, "do_extract_helical_tubes", "Coordinates are start-end only?", type="switch")
    # grp = place(grp,"do_extract_helical_tubes", TOGGLE_DEACTIVATE, group6)
    grp = place(grp,"do_cut_into_segments", TOGGLE_DEACTIVATE)
    grp = place(grp,"helical_nr_asu", TOGGLE_DEACTIVATE)
    grp = place(grp,"helical_rise", TOGGLE_DEACTIVATE)
    grp.end()
    

    return groups

def initialiseSelectWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_model", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mic", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_data", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_class_ranker", "Automatically select 2D classes?", type="switch")
    # grp = place(grp,"do_class_ranker", TOGGLE_DEACTIVATE, group6)
    grp = place(grp,"rank_threshold", TOGGLE_DEACTIVATE)
    grp = place(grp,"select_nr_parts", TOGGLE_DEACTIVATE)
    grp = place(grp,"select_nr_classes", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_recenter", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups,"do_regroup", "Regroup the particles?", type="switch")
    # grp = place(grp,"do_regroup", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"nr_groups", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_select_values", "Select based on metadata values?", type="switch")
    # grp = place(grp,"do_select_values", TOGGLE_DEACTIVATE, group3)
    grp = place(grp,"select_label", TOGGLE_DEACTIVATE)
    grp = place(grp,"select_minval", TOGGLE_DEACTIVATE)
    grp = place(grp,"select_maxval", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_discard", "OR: select on image statistics?", type="switch")
    # grp = place(grp,"do_discard", TOGGLE_DEACTIVATE, group4)
    grp = place(grp,"discard_label", TOGGLE_DEACTIVATE)
    grp = place(grp,"discard_sigma", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_split", "OR: split into subsets?", type="switch")
    # grp = place(grp,"do_split", TOGGLE_DEACTIVATE, group5)
    grp = place(grp,"do_random", TOGGLE_DEACTIVATE)
    grp = place(grp,"split_size", TOGGLE_DEACTIVATE)
    grp = place(grp,"nr_split", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_remove_duplicates", "OR: remove duplicates?", type="switch")
    # grp = place(grp,"do_remove_duplicates", TOGGLE_DEACTIVATE, group2)
    grp = place(grp,"duplicate_threshold", TOGGLE_DEACTIVATE)
    grp = place(grp,"image_angpix", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_filaments", "OR: select filaments by dendrogram?", type="switch")
    # grp = place(grp,"do_filaments", TOGGLE_DEACTIVATE, group3)
    grp = place(grp,"dendrogram_threshold", TOGGLE_LEAVE_ACTIVE)
    grp = place(grp,"dendrogram_minclass", TOGGLE_LEAVE_ACTIVE)

    grp.end()
    

    return groups

def initialiseClass2DWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_img", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"fn_cont", TOGGLE_REACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_ctf_correction", " Do CTF-correction?", type="switch")
    # grp = place(grp,"do_ctf_correction", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"ctf_intact_first_peak", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"nr_classes", TOGGLE_DEACTIVATE)
    grp = place(grp,"tau_fudge")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_em", TOGGLE_DEACTIVATE, group2)
    grp = place(grp,"nr_iter_em")
    grp = place(grp,"do_grad", TOGGLE_DEACTIVATE, group5)
    grp = place(grp,"nr_iter_grad")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"particle_diameter")
    grp = place(grp,"do_zero_mask", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"highres_limit", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_center")
    grp.end()
    
    grp =Fieldset(groups, "dont_skip_align", "Perform image alignment?", type="switch")
    # grp = place(grp,"dont_skip_align", TOGGLE_LEAVE_ACTIVE, group3)
    grp = place(grp,"psi_sampling")
    grp = place(grp,"offset_range")
    grp = place(grp,"offset_step")
    # grp.end()
    
    # grp =Fieldset(groups)
    grp = place(grp,"allow_coarser")
    grp.end()

    grp =Fieldset(groups, "do_helix", "Classify 2D helical segments?", type="switch")
    # grp = place(grp,"do_helix", TOGGLE_DEACTIVATE, group4)
    grp = place(grp,"helical_tube_outer_diameter")
    grp = place(grp,"do_bimodal_psi")
    grp = place(grp,"range_psi")
    grp.end()

    grp =Fieldset(groups, "do_restrict_xoff", "Restrict helical offsets to rise", type="switch")
    # grp = place(grp,"do_restrict_xoff", TOGGLE_LEAVE_ACTIVE, group7)
    grp = place(grp,"helical_rise", TOGGLE_LEAVE_ACTIVE)
    grp.end()

    grp = Fieldset(groups,"diskio","Disk Management")
    grp = place(grp,"do_parallel_discio")
    grp = place(grp,"nr_pool")
    grp = place(grp,"do_preread_images", TOGGLE_LEAVE_ACTIVE, group5, True)
    grp = place(grp,"scratch_dir")
    grp = place(grp,"do_combine_thru_disc")
    grp.end()
    
    grp =Fieldset(groups,"gpu","GPU")
    grp = place(grp,"use_gpu", TOGGLE_LEAVE_ACTIVE, group6)
    grp = place(grp,"gpu_ids", TOGGLE_LEAVE_ACTIVE)

    grp.end()
    
    return groups

def initialiseInimodelWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    if is_tomo :
        grp = placeTomoInput(True, True, True, False)
    grp = place(grp,"fn_img", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"fn_cont", TOGGLE_REACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_ctf_correction", "Do CTF-correction?", type="switch")
    # grp = place(grp,"do_ctf_correction", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"ctf_intact_first_peak", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"nr_iter")
    grp = place(grp,"tau_fudge")
    grp = place(grp,"nr_classes", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"particle_diameter")
    grp = place(grp,"do_solvent", TOGGLE_DEACTIVATE)
    grp = place(grp,"sym_name", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_run_C1", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"sigma_tilt", TOGGLE_DEACTIVATE)
    grp.end()

    grp = Fieldset(groups,"diskio","Disk Management")
    grp = place(grp,"do_parallel_discio")
    grp = place(grp,"nr_pool")
    grp = place(grp,"do_preread_images", TOGGLE_LEAVE_ACTIVE, group5, True)
    grp = place(grp,"scratch_dir")
    grp = place(grp,"do_combine_thru_disc")
    grp.end()
    
    grp =Fieldset(groups,"gpu","GPU")
    grp = place(grp,"use_gpu", TOGGLE_LEAVE_ACTIVE, group6)
    grp = place(grp,"gpu_ids", TOGGLE_LEAVE_ACTIVE)

    grp.end()
    

    return groups

def initialiseClass3DWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    if is_tomo :
        grp = placeTomoInput(True, True, True, False)
    grp = place(grp,"fn_img", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"fn_ref", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mask")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"fn_cont", TOGGLE_REACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"ref_correct_greyscale", TOGGLE_DEACTIVATE)
    grp = place(grp,"trust_ref_size", TOGGLE_DEACTIVATE)
    grp = place(grp,"ini_high", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"sym_name", TOGGLE_DEACTIVATE)
    grp.end()

    grp =Fieldset(groups, "do_ctf_correction", "Do CTF-correction?", type="switch")
    # grp = place(grp,"do_ctf_correction", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"ctf_intact_first_peak", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"nr_classes", TOGGLE_DEACTIVATE)
    grp = place(grp,"tau_fudge")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"nr_iter")
    grp = place(grp,"do_fast_subsets", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"particle_diameter")
    grp = place(grp,"do_zero_mask", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"highres_limit", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_blush", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "dont_skip_align", "Perform image alignment?", type="switch")
    # grp = place(grp,"dont_skip_align", TOGGLE_LEAVE_ACTIVE, group3)
    grp = place(grp,"sampling")
    grp = place(grp,"offset_range")
    grp = place(grp,"offset_step")

    # grp =Fieldset(groups)
    grp = place(grp,"allow_coarser")
    grp.end()

    grp = Fieldset(groups, "do_local_ang_searches", "Perform local angular searches?", type="switch")
    # grp = place(grp,"do_local_ang_searches", TOGGLE_LEAVE_ACTIVE, group4)
    grp = place(grp,"sigma_angles")
    grp = place(grp,"relax_sym")
    grp.end()
    

    
    grp =Fieldset(groups)
    grp = place(grp,"sigma_tilt", TOGGLE_DEACTIVATE)
    # helix_text", TOGGLE_DEACTIVATE) # (current_y, "Nov 21, 2015")
    grp.end()
    
    grp =Fieldset(groups, "do_helix", "Do helical reconstruction?", type="switch")
    # grp = place(grp,"do_helix", TOGGLE_DEACTIVATE, group5)
    grp = place2(grp,"helical_tube_inner_diameter", "helical_tube_outer_diameter", "Tube diameter - inner, outer (A):", TOGGLE_DEACTIVATE)
    grp = place3(grp, "range_rot", "range_tilt", "range_psi", "Angular search range - rot, tilt, psi (deg):", TOGGLE_DEACTIVATE)
    grp = place(grp,"helical_range_distance", TOGGLE_DEACTIVATE)
    grp = place(grp,"keep_tilt_prior_fixed", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_apply_helical_symmetry", "Apply helical symmetry?", type="switch")
    # grp = place(grp,"do_apply_helical_symmetry", TOGGLE_DEACTIVATE, group8)
    grp = place(grp,"helical_nr_asu", TOGGLE_DEACTIVATE)
    grp = place2(grp,"helical_twist_initial", "helical_rise_initial", "Initial twist (deg), rise (A):", TOGGLE_DEACTIVATE)
    grp = place(grp,"helical_z_percentage", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_local_search_helical_symmetry", "Do local searches of symmetry?", type="switch")
    # grp = place(grp,"do_local_search_helical_symmetry", TOGGLE_DEACTIVATE, group6)
    grp = place3(grp, "helical_twist_min","helical_twist_max", "helical_twist_inistep", "Twist search - Min, Max, Step (deg):", TOGGLE_DEACTIVATE)
    grp = place3(grp, "helical_rise_min", "helical_rise_max", "helical_rise_inistep", "Rise search - Min, Max, Step (A):", TOGGLE_DEACTIVATE)
    grp.end()

    grp = Fieldset(groups,"diskio","Disk Management")
    grp = place(grp,"do_parallel_discio")
    grp = place(grp,"nr_pool")
    grp = place(grp,"do_pad1")
    grp = place(grp,"do_preread_images", TOGGLE_LEAVE_ACTIVE, group7, True)
    grp = place(grp,"scratch_dir")
    grp = place(grp,"do_combine_thru_disc")
    grp.end()
    
    grp =Fieldset(groups,"gpu","GPU")
    grp = place(grp,"use_gpu", TOGGLE_LEAVE_ACTIVE, group8)
    grp = place(grp,"gpu_ids")

    grp.end()
    

    return groups

def initialiseAutorefineWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = placeTomoInput(True, True, True, False)
    grp = place(grp,"fn_img", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"fn_ref", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mask")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"fn_cont", TOGGLE_REACTIVATE)
    grp = place(grp,"ref_correct_greyscale", TOGGLE_DEACTIVATE)
    grp = place(grp,"trust_ref_size", TOGGLE_DEACTIVATE)
    grp = place(grp,"ini_high", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"sym_name", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_ctf_correction", "Do CTF-correction?", type="switch")
    # grp = place(grp,"do_ctf_correction", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"ctf_intact_first_peak", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"particle_diameter")
    grp = place(grp,"do_zero_mask", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_solvent_fsc")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_blush", TOGGLE_DEACTIVATE)
    grp = place(grp,"sampling", TOGGLE_DEACTIVATE)
    grp = place(grp,"offset_range", TOGGLE_DEACTIVATE)
    grp = place(grp,"offset_step", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"auto_local_sampling", TOGGLE_DEACTIVATE)
    grp = place(grp,"relax_sym")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"auto_faster")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"sigma_tilt", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_helix", "Do helical reconstruction?", type="switch")
    # grp = place(grp,"do_helix", TOGGLE_DEACTIVATE, group2)
    grp = place2(grp,"helical_tube_inner_diameter", "helical_tube_outer_diameter", "Tube diameter - inner, outer (A):",TOGGLE_DEACTIVATE)
    grp = place3(grp, "range_rot", "range_tilt", "range_psi", "Angular search range - rot, tilt, psi (deg):", TOGGLE_DEACTIVATE)
    grp = place(grp,"helical_range_distance", TOGGLE_DEACTIVATE)
    grp = place(grp,"keep_tilt_prior_fixed", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_apply_helical_symmetry", "Apply helical symmetry?", type="switch" )
    # grp = place(grp,"do_apply_helical_symmetry", TOGGLE_DEACTIVATE, group5)
    grp = place(grp,"helical_nr_asu", TOGGLE_DEACTIVATE)
    grp = place2(grp,"helical_twist_initial", "helical_rise_initial", "Initial twist (deg), rise (A):",TOGGLE_DEACTIVATE)
    grp = place(grp,"helical_z_percentage", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_local_search_helical_symmetry", "Do local searches of symmetry?", type="switch")
    # grp = place(grp,"do_local_search_helical_symmetry", TOGGLE_DEACTIVATE, group3)
    grp = place3(grp, "helical_twist_min", "helical_twist_max", "helical_twist_inistep", "Twist search - Min, Max, Step (deg):", TOGGLE_DEACTIVATE)
    grp = place3(grp, "helical_rise_min", "helical_rise_max","helical_rise_inistep","Rise search - Min, Max, Step (A):", TOGGLE_DEACTIVATE)
    grp.end()

    grp = Fieldset(groups,"diskio","Disk Management")
    grp = place(grp,"do_parallel_discio")
    grp = place(grp,"nr_pool")
    grp = place(grp,"do_pad1")
    grp = place(grp,"do_preread_images", TOGGLE_LEAVE_ACTIVE, group4, True)
    grp = place(grp,"scratch_dir")
    grp = place(grp,"do_combine_thru_disc")
    grp.end()
    
    grp =Fieldset(groups,"gpu","GPU")
    grp = place(grp,"use_gpu", TOGGLE_LEAVE_ACTIVE, group5)
    grp = place(grp,"gpu_ids")

    grp.end()
    

    return groups

def initialiseMultiBodyWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_in", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_cont", TOGGLE_REACTIVATE)
    grp = place(grp,"fn_bodies", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_subtracted_bodies", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_blush", TOGGLE_DEACTIVATE)
    grp = place(grp,"sampling", TOGGLE_DEACTIVATE)
    grp = place(grp,"offset_range", TOGGLE_DEACTIVATE)
    grp = place(grp,"offset_step", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups,"do_analyse", "Run flexibility analysis?", type="switch")
    # grp = place(grp,"do_analyse", TOGGLE_LEAVE_ACTIVE, group5)
    grp = place(grp,"nr_movies")
    grp.end()
    
    grp =Fieldset(groups, "do_select", "Select particles based on eigenvalues?", type="switch")
    grp = place(grp,"do_select", TOGGLE_LEAVE_ACTIVE, group6)
    grp = place(grp,"select_eigenval")
    grp = place(grp,"eigenval_min")
    grp = place(grp,"eigenval_max")
    grp.end()

    grp = Fieldset(groups,"diskio","Disk Management")
    grp = place(grp,"do_parallel_discio")
    grp = place(grp,"nr_pool")
    grp = place(grp,"do_pad1")
    grp = place(grp,"do_preread_images", TOGGLE_LEAVE_ACTIVE, group7, True)
    grp = place(grp,"scratch_dir")
    grp = place(grp,"do_combine_thru_disc")
    grp.end()
    
    grp =Fieldset(groups,"gpu","GPU")
    grp = place(grp,"use_gpu", TOGGLE_LEAVE_ACTIVE, group4)
    grp = place(grp,"gpu_ids")

    grp.end()
    

    return groups

def initialiseMaskcreateWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_in", TOGGLE_DEACTIVATE) # (current_y, "Input 3D map:", NODE_3DREF, "", "MRC map files (*.mrc)", "Provide an input MRC map from which to start binarizing the map.")
    grp = place(grp,"lowpass_filter")
    grp = place(grp,"angpix")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"inimask_threshold")
    grp = place(grp,"extend_inimask")
    grp = place(grp,"width_mask_edge")
    grp.end()
    
    grp =Fieldset(groups, "do_helix", "Mask a 3D helix?", type="switch")
    # grp = place(grp,"do_helix", TOGGLE_LEAVE_ACTIVE, group1)
    grp = place(grp,"helical_z_percentage")

    grp.end()
    

    return groups

def initialiseJoinstarWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"do_part", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"fn_part1", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_part2", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_part3", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_part4", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_mic", TOGGLE_DEACTIVATE, group2)
    grp = place(grp,"fn_mic1", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mic2", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mic3", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mic4", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_mov", TOGGLE_DEACTIVATE, group3) # (current_y, "Combine movie STAR files?", False, "", mov_group)
    grp = place(grp,"fn_mov1", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mov2", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mov3", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mov4", TOGGLE_DEACTIVATE)

    grp.end()
    

    return groups

def initialiseSubtractWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_opt", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mask", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_data", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"fn_data", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_float16", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_fliplabel", TOGGLE_DEACTIVATE, group2)
    grp = place(grp,"fn_fliplabel", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_center_mask", TOGGLE_DEACTIVATE, group3, True)
    grp = place(grp,"do_center_xyz", TOGGLE_DEACTIVATE, group4)
    grp = place3(grp, "center_x", "center_y", "center_z", "Center coordinate - X, Y, Z (pix):", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"new_box", TOGGLE_DEACTIVATE)

    grp.end()
    

    return groups

def initialisePostprocessWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_in", TOGGLE_DEACTIVATE) # (current_y, "One of the 2 unfiltered half-maps:", NODE_HALFMAP, "", "MRC map files (*half1_class001_unfil.mrc)",  "Provide one of the two unfiltered half-reconstructions that were output upon convergence of a 3D auto-refine run.")
    grp = place(grp,"fn_mask", TOGGLE_DEACTIVATE) # (current_y, "Solvent mask:", NODE_MASK, "", "Image Files (*.{spi,vol,msk,mrc})", "Provide a soft mask where the protein is white (1) and the solvent is black (0). Often, the softer the mask the higher resolution estimates you will get. A soft edge of 5-10 pixels is often a good edge width.")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"angpix")
    grp = place(grp,"do_auto_bfac", TOGGLE_LEAVE_ACTIVE, group1)
    grp = place(grp,"autob_lowres")
    grp = place(grp,"do_adhoc_bfac", TOGGLE_LEAVE_ACTIVE, group2)
    grp = place(grp,"adhoc_bfac")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_skip_fsc_weighting", TOGGLE_LEAVE_ACTIVE, group3)
    grp = place(grp,"low_pass")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"fn_mtf")
    grp = place(grp,"mtf_angpix")

    grp.end()
    

    return groups

def initialiseLocresWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_in", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mask")
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"angpix", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_resmap_locres", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"fn_resmap", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"pval", TOGGLE_DEACTIVATE)
    grp = place(grp,"minres", TOGGLE_DEACTIVATE)
    grp = place(grp,"maxres", TOGGLE_DEACTIVATE)
    grp = place(grp,"stepres", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_relion_locres", TOGGLE_DEACTIVATE, group2)
    # grp = place(grp,"locres_sampling", TOGGLE_DEACTIVATE)
    # grp = place(grp,"randomize_at", TOGGLE_DEACTIVATE)
    # grp.end()
 
    grp = place(grp,"adhoc_bfac", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_mtf", TOGGLE_DEACTIVATE)

    grp.end()
    

    return groups

def initialiseMotionrefineWindow(is_tomo=False):
    """ Bayesian polishing """
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_mic", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_data", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_post", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"first_frame", TOGGLE_DEACTIVATE)
    grp = place(grp,"last_frame", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"extract_size", TOGGLE_DEACTIVATE)
    grp = place(grp,"rescale", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_float16", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_param_optim", "Train optimal parameters?", type="switch")
    # grp = place(grp,"do_param_optim", TOGGLE_LEAVE_ACTIVE, group2)
    grp = place(grp,"opt_params", TOGGLE_DEACTIVATE)
    
    grp = place(grp,"eval_frac")
    grp = place(grp,"optim_min_part")
    grp.end()
    
    grp =Fieldset(groups, "do_polish", "Perform particle polishing?", type="switch")
    # grp = place(grp,"do_polish", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"minres", TOGGLE_DEACTIVATE)
    grp = place(grp,"maxres", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups, "do_own_params", "OR use your own parameters?", type="switch")
    # grp = place(grp,"do_own_params", TOGGLE_DEACTIVATE, group4)
    grp = place(grp,"sigma_vel", TOGGLE_DEACTIVATE)
    grp = place(grp,"sigma_div", TOGGLE_DEACTIVATE)
    grp = place(grp,"sigma_acc", TOGGLE_DEACTIVATE)
    grp.end()
    
    return groups

def initialiseCtfrefineWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_data", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_post", TOGGLE_DEACTIVATE)
    grp.end()

    grp = Fieldset(groups)
    grp = place(grp,"do_aniso_mag", TOGGLE_LEAVE_ACTIVE, group3, True) # True means: activating aniso_mag will deactive higher-order aberrations
    grp.end()

    grp = Fieldset(groups, "do_ctf", "Perform CTF parameter fitting?", type="switch")
    # grp = place(grp,"do_ctf", TOGGLE_LEAVE_ACTIVE, group1)
    grp = place(grp,"do_defocus", TOGGLE_LEAVE_ACTIVE)
    grp = place(grp,"do_astig", TOGGLE_LEAVE_ACTIVE)
    grp = place(grp,"do_bfactor", TOGGLE_LEAVE_ACTIVE)
    grp = place(grp,"do_phase", TOGGLE_LEAVE_ACTIVE)
    grp.end()

    grp = Fieldset(groups, "do_tilt", "Estimate beamtilt?", type="switch")
    # grp = place(grp,"do_tilt", TOGGLE_LEAVE_ACTIVE, group4)
    grp = place(grp,"do_trefoil", TOGGLE_LEAVE_ACTIVE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"do_4thorder", TOGGLE_LEAVE_ACTIVE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"minres", TOGGLE_DEACTIVATE)

    grp.end()
    

    return groups

def initialiseDynaMightWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_star", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_map", TOGGLE_DEACTIVATE)
    # grp = place(grp,"fn_mask", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"nr_gaussians", TOGGLE_DEACTIVATE)
    grp = place(grp,"initial_threshold", TOGGLE_DEACTIVATE)
    grp = place(grp,"reg_factor", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = Fieldset(groups)
    grp = place(grp,"fn_dynamight_exe", TOGGLE_DEACTIVATE)
    grp = place(grp,"gpu_id")
    grp = place(grp,"do_preload")
    grp = place(grp,"fn_checkpoint", TOGGLE_REACTIVATE)
    grp.end()
    
    grp = Fieldset(groups)
    grp = place(grp,"do_visualize", TOGGLE_REACTIVATE, group1, False)
    grp = place(grp,"halfset")
    grp.end()
 
    grp = Fieldset(groups)
    grp = place(grp,"do_inverse", TOGGLE_REACTIVATE, group2, False)
    grp = place(grp,"nr_epochs")
    grp = place(grp,"do_store_deform")
    grp.end()
 
    grp = Fieldset(groups)
    grp = place(grp,"do_reconstruct",TOGGLE_REACTIVATE, group3, False)
    grp = place(grp,"backproject_batchsize")

    grp.end()
    

    return groups

def initialiseModelAngeloWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_map", TOGGLE_DEACTIVATE)
    grp = place(grp,"p_seq", TOGGLE_DEACTIVATE)
    grp = place(grp,"d_seq", TOGGLE_DEACTIVATE)
    grp = place(grp,"r_seq", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"fn_modelangelo_exe", TOGGLE_DEACTIVATE)
    grp = place(grp,"gpu_id", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_hhmer", TOGGLE_LEAVE_ACTIVE, group1, False)
    grp.end()
 
    grp = place(grp,"fn_lib", TOGGLE_LEAVE_ACTIVE)
    grp = place(grp,"alphabet", TOGGLE_LEAVE_ACTIVE)
    grp.end()
 
    grp = place(grp,"F1", TOGGLE_LEAVE_ACTIVE)
    grp = place(grp,"F2", TOGGLE_LEAVE_ACTIVE)
    grp = place(grp,"F3", TOGGLE_LEAVE_ACTIVE)
    grp = place(grp,"E", TOGGLE_LEAVE_ACTIVE)

    grp.end()
    

    return groups

def initialiseExternalWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"fn_exe", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"in_mov", TOGGLE_DEACTIVATE)
    grp = place(grp,"in_mic", TOGGLE_DEACTIVATE)
    grp = place(grp,"in_part", TOGGLE_DEACTIVATE)
    grp = place(grp,"in_coords", TOGGLE_DEACTIVATE)
    grp = place(grp,"in_3dref", TOGGLE_DEACTIVATE)
    grp = place(grp,"in_mask", TOGGLE_DEACTIVATE)
    grp = place2(grp,"param1_label", "param1_value", "Param1 label, value:", TOGGLE_LEAVE_ACTIVE)
    grp = place2(grp,"param2_label", "param2_value", "Param2 label, value:", TOGGLE_LEAVE_ACTIVE)
    grp = place2(grp,"param3_label", "param3_value", "Param3 label, value:", TOGGLE_LEAVE_ACTIVE)
    grp = place2(grp,"param4_label", "param4_value", "Param4 label, value:", TOGGLE_LEAVE_ACTIVE)
    grp = place2(grp,"param5_label", "param5_value", "Param5 label, value:", TOGGLE_LEAVE_ACTIVE)
    grp = place2(grp,"param6_label", "param6_value", "Param6 label, value:", TOGGLE_LEAVE_ACTIVE)
    grp = place2(grp,"param7_label", "param7_value", "Param7 label, value:", TOGGLE_LEAVE_ACTIVE)
    grp = place2(grp,"param8_label", "param8_value", "Param8 label, value:", TOGGLE_LEAVE_ACTIVE)
    grp = place2(grp,"param9_label", "param9_value", "Param9 label, value:", TOGGLE_LEAVE_ACTIVE)
    grp = place2(grp,"param10_label", "param10_value", "Param10 label, value:", TOGGLE_LEAVE_ACTIVE)

    grp.end()
    

    return groups


def initialiseTomoImportWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"movie_files", TOGGLE_DEACTIVATE)
    grp = place(grp,"images_are_motion_corrected", TOGGLE_DEACTIVATE)
    grp = place(grp,"mdoc_files", TOGGLE_DEACTIVATE)
    grp = place(grp,"optics_group_name", TOGGLE_DEACTIVATE)
    grp = place(grp,"prefix", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"angpix", TOGGLE_DEACTIVATE)
    grp = place(grp,"kV", TOGGLE_DEACTIVATE)
    grp = place(grp,"Cs", TOGGLE_DEACTIVATE)
    grp = place(grp,"Q0", TOGGLE_DEACTIVATE)
    grp = place(grp,"dose_rate", TOGGLE_DEACTIVATE)
    grp = place(grp,"dose_is_per_movie_frame", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"tilt_axis_angle", TOGGLE_DEACTIVATE)
    grp = place(grp,"mtf_file", TOGGLE_DEACTIVATE)
    grp = place(grp,"flip_tiltseries_hand", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_coords", TOGGLE_DEACTIVATE, group1, False)
    grp = place(grp,"in_coords", TOGGLE_DEACTIVATE)
    grp = place(grp,"remove_substring", TOGGLE_DEACTIVATE)
    grp = place(grp,"remove_substring2", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"is_center", TOGGLE_DEACTIVATE, group2, False)
    grp = place(grp,"scale_factor", TOGGLE_DEACTIVATE)
    grp = place(grp,"add_factor", TOGGLE_DEACTIVATE)

    grp.end()
    

    return groups

def initialiseTomoAlignTiltseriesWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"in_tiltseries", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"tomogram_thickness", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"fn_batchtomo_exe", TOGGLE_DEACTIVATE)
    grp = place(grp,"fn_aretomo_exe", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_imod_fiducials", TOGGLE_DEACTIVATE, group1, False)
    grp = place(grp,"fiducial_diameter", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_imod_patchtrack", TOGGLE_DEACTIVATE, group2, False)
    grp = place(grp,"patch_size", TOGGLE_DEACTIVATE)
    grp = place(grp,"patch_overlap", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_aretomo2", TOGGLE_DEACTIVATE, group3, False)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_aretomo_tiltcorrect", TOGGLE_DEACTIVATE, group4, False)
    grp = place(grp,"aretomo_tiltcorrect_angle", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"do_aretomo_ctf", TOGGLE_DEACTIVATE, group5, False)
    grp = place(grp,"do_aretomo_phaseshift", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"other_aretomo_args", TOGGLE_DEACTIVATE)
    grp = place(grp,"gpu_ids")

    grp.end()
    

    return groups

def initialiseTomoReconstructTomogramsWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"in_tiltseries", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"generate_split_tomograms", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"do_proj", TOGGLE_DEACTIVATE, group1, False)
    grp = place(grp,"centre_proj", TOGGLE_DEACTIVATE)
    grp = place(grp,"thickness_proj", TOGGLE_DEACTIVATE)
    grp = place(grp,"xdim", TOGGLE_DEACTIVATE)
    grp = place(grp,"ydim", TOGGLE_DEACTIVATE)
    grp = place(grp,"zdim", TOGGLE_DEACTIVATE)
    grp = place(grp,"binned_angpix", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place ("tiltangle_offset", TOGGLE_DEACTIVATE)
    grp = place(grp,"tomo_name")
    grp.end()
 
    grp = place(grp,"do_fourier", TOGGLE_DEACTIVATE, group2, False)
    grp = place(grp,"ctf_intact_first_peak", TOGGLE_DEACTIVATE)

    grp.end()
    

    return groups

def initialiseTomoDenoiseTomogramsWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"in_tomoset", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"cryocare_path")
    grp = place(grp,"gpu_ids")
    grp = place(grp,"do_cryocare_train", TOGGLE_DEACTIVATE, group1, False)
    grp.end()
 
    grp = place(grp,"tomograms_for_training", TOGGLE_DEACTIVATE)
    grp = place(grp,"number_training_subvolumes", TOGGLE_DEACTIVATE)
    grp = place(grp,"subvolume_dimensions", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_cryocare_predict", TOGGLE_DEACTIVATE, group2, False)
    grp.end()
 
    grp = place(grp,"care_denoising_model", TOGGLE_DEACTIVATE)
    grp = place3(grp, "ntiles_x", "ntiles_y", "ntiles_z", "Number of tiles in X,Y,Z:", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"denoising_tomo_name", TOGGLE_DEACTIVATE)

    grp.end()
    

    return groups

def initialiseTomoPickTomogramsWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"in_tomoset", TOGGLE_DEACTIVATE)
    # grp = place(grp,"cache_size", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"pick_mode", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"particle_spacing", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"in_star_file", TOGGLE_DEACTIVATE)

    grp.end()
    

    return groups

def initialiseTomoSubtomoWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = placeTomoInput(True, True, True, False)
    grp = place(grp,"binning", TOGGLE_DEACTIVATE)
    grp = place(grp,"box_size", TOGGLE_DEACTIVATE)
    grp = place(grp,"crop_size", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place ("max_dose", TOGGLE_DEACTIVATE)
    grp = place ("min_frames", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"do_stack2d", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_float16", TOGGLE_DEACTIVATE)

    grp.end()
    

    return groups

def initialiseTomoCtfRefineWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = placeTomoInput(True, True, True, False)
    grp = place(grp,"in_halfmaps", TOGGLE_DEACTIVATE)
    grp = place(grp,"in_refmask", TOGGLE_DEACTIVATE)
    grp = place(grp,"in_post", TOGGLE_DEACTIVATE)
    grp = place(grp,"box_size", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"do_defocus", TOGGLE_DEACTIVATE, group1)
    grp = place(grp,"focus_range", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_reg_def", TOGGLE_DEACTIVATE, group2)
    grp = place(grp,"lambda", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"do_scale", TOGGLE_DEACTIVATE, group3)
    grp = place(grp,"do_frame_scale", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_tomo_scale", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_odd_aberr", TOGGLE_DEACTIVATE, group3)
    grp = place(grp,"nr_odd_aberr", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"do_even_aberr", TOGGLE_DEACTIVATE, group4)
    grp = place(grp,"nr_even_aberr", TOGGLE_DEACTIVATE)

    grp.end()
    

    return groups

def initialiseTomoAlignWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = placeTomoInput(True, True, True, False)
    grp = place(grp,"in_halfmaps", TOGGLE_DEACTIVATE)
    grp = place(grp,"in_refmask", TOGGLE_DEACTIVATE)
    grp = place(grp,"in_post", TOGGLE_DEACTIVATE)
    grp = place(grp,"box_size", TOGGLE_DEACTIVATE)
    grp = place(grp,"max_error", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"do_shift_align", TOGGLE_DEACTIVATE, group3)
    grp = place(grp,"shift_align_type", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_motion", TOGGLE_DEACTIVATE, group2)
    grp.end()
 
    grp = place(grp,"sigma_vel", TOGGLE_DEACTIVATE)
    grp = place(grp,"sigma_div", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_sq_exp_ker", TOGGLE_DEACTIVATE)

    grp.end()
    

    return groups

def initialiseTomoReconParWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = placeTomoInput(True, True, True, False)
    grp = place(grp,"binning", TOGGLE_DEACTIVATE)
    grp = place(grp,"box_size", TOGGLE_DEACTIVATE)
    grp = place(grp,"crop_size", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"snr", TOGGLE_DEACTIVATE)
    grp.end()
 
    grp = place(grp,"sym_name", TOGGLE_DEACTIVATE)
    grp = place(grp,"do_helix", TOGGLE_DEACTIVATE, group1)
    grp.end()
 
    grp = place(grp,"helical_nr_asu")
    grp = place(grp,"helical_twist")
    grp = place(grp,"helical_rise")
    grp = place(grp,"helical_tube_outer_diameter")
    grp = place(grp,"helical_z_percentage")

    grp.end()
    

    return groups

def initialiseTomoExcludeTiltImagesWindow(is_tomo=False):
    groups = FsGroup()
    grp = Fieldset(groups)
    grp = place(grp,"in_tiltseries", TOGGLE_DEACTIVATE)
    grp.end()
    
    grp =Fieldset(groups)
    grp = place(grp,"cache_size", TOGGLE_DEACTIVATE)

if __name__ == '__main__' :
    is_tomo = False
    print("__________JOB IMPORT__________",'\n')
    fs_all = initialiseImportWindow()
    print(fs_all)
    print("__________JOB MOTIONCOR__________",'\n')
    fs_all = initialiseMotioncorrWindow()
    print(fs_all)
    print("__________JOB CTF ESTIMATION__________",'\n')
    fs_all = initialiseCtffindWindow()
    print(fs_all)
    print("__________JOB MANUAL PICK__________",'\n')
    fs_all = initialiseManualpickWindow()
    print(fs_all)
    print("__________JOB AUTOPICK__________",'\n')
    fs_all = initialiseAutopickWindow()
    print(fs_all)
    print("__________JOB EXTRACT__________",'\n')
    fs_all = initialiseExtractWindow()
    print(fs_all)
    print("__________JOB 2DCLASS__________",'\n')
    fs_all = initialiseClass2DWindow()
    print(fs_all)
    print("__________JOB 3D INITIAL REFERENCE__________",'\n')
    fs_all = initialiseInimodelWindow()
    print(fs_all)
    print("__________JOB 3DCLASS__________",'\n')
    fs_all = initialiseClass3DWindow()
    print(fs_all)

    # print(fs_all.get(1).to_star())