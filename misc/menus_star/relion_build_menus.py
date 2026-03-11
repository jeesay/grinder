import relion_h as rh
import relion_option as rho
import relion_window as rwi
import relion_spa_gui as rjo
import relion_spa_commands_2 as rcmd

################## UTILITIES ##################

def create_tool(toolid,tabs):
    tool = rho.Tool(toolid)
    for tid in tabs:
         tool.add_builtin_tab(tid)
    return tool

def create_widget(job_option):
    pass

def write_starfile(t,filename,flag_mpi, flag_thread):
    print('write',filename)
    with open(filename, 'w') as f:
        f.write(t.to_star())

def update_fieldset(tool,   fs,jo,params):
    # fieldset = rho.Table(fs_data.fsid, fs_data.fsname, icon = "", widget = "fieldset")
    removed = []
    fs_options = []
    for wdgt in fs:
        if wdgt.id in params:
            # Create the widget with joboptions
            if jo[wdgt.id].widget == 'node':
                jo[wdgt.id].widget = 'file'
            wdgt.set_options(jo[wdgt.id])
            # Create the widget select + options 
            if jo[wdgt.id].widget == 'select':
                fs_opt = rwi.Fieldset(fs, wdgt.id,"Options")
                fs_opt.group = rwi.group8
                fs_opt.current_group = rwi.group8
                for i,opt in enumerate(jo[wdgt.id].radio_options):
                    wopt = rwi.Widget(fs,f'{wdgt.id}_opt_{i:02}',fs.parent)
                    wopt.set_options(opt)
                    fs_opt.append(wopt)
                fs_options.append(fs_opt)

            # Append widget to fieldset
            # fieldset.append_widget(fs_data.fsid,w)
        else:
            removed.append(wdgt.id)
    print('REMOVED',removed)
    for rm in removed:
        fs.delete(rm)

    # If fieldset not empty, append to tab
    tab = 'io' if fs.fsid == 'indata' else 'settings'
    if not fs.is_empty():
        tool.append_fieldset(fs,tab)
    if len(fs_options) > 0:
        for fo in fs_options:
            tool.append_fieldset(fo,tab)
    return tool

        
def update_system_fieldset(tool, has_mpi, has_thread, fs,jo, prog, params):
    # Create fieldset `outdata`
    # fout = rwi.Fieldset(fs.parent,"outdata","Output Data",icon="bi-box-arrow-down")
    # fout.display = 'hidden'
    # fout.group = rwi.group6
    # fout.current_group = rwi.group6
    # tool.append_fieldset(fout,'io')
    # Create fieldset `nodes`
    fnod = rwi.Fieldset(fs.parent,"nodes","Nodes",icon="bi-controller")
    fnod.display = "hidden"
    fnod.group = rwi.group6
    fnod.current_group = rwi.group6
    tool.append_fieldset(fnod,'io')
    for nod in prog.commands[0].innodes:
        wdgt = rwi.Widget(fnod,'?',fnod)
        wdgt.id = nod.id
        wdgt.widget = 'innode'
        wdgt.label = nod.id
        wdgt.arg0 = nod.nodetype
        wdgt.value = nod.name
        fnod.append(wdgt,force=True)
    for nod in prog.commands[0].outnodes:
        wdgt = rwi.Widget(fnod,'?',fnod)
        wdgt.id = nod.id
        wdgt.widget = 'outnode'
        wdgt.label = nod.id
        wdgt.arg0 = nod.nodetype
        wdgt.value = nod.name
        fnod.append(wdgt,force=True)
    # Create fieldset `system`
    fsys = rwi.Fieldset(fs.parent,"system","System",icon="bi-incognito")
    fsys.display = 'hiddden'
    fsys.group = rwi.group7
    fsys.current_group = rwi.group7
    print('FSYS')
    # Append widgets
    for wid,wv in params:
        wdgt = rwi.Widget(fsys,wid,fsys)
        wdgt.set_options(jo[wid])
        wdgt.widget = 'bool'
        wdgt.value = str(wv).lower()
        wdgt.group = fsys
        fsys.append(wdgt,force=True)
    tool.append_fieldset(fsys,'io')
    # Create fieldset `scripting`
    fcli = rwi.ArgSet(fs.parent,f'{tool.toolid}_prgm',"Script",type="cli")
    fcli.group = rwi.group8
    fcli.current_group = rwi.group8
    tool.append_fieldset(fcli,'io')
    for p in prog.commands[0].progs:
        fcli.append(p)
    # Create fieldset `cli`
    fcli = rwi.Fieldset(fs.parent,f'{tool.toolid}_cmd',"Check command",type="cli")
    fcli.group = rwi.group9
    fcli.current_group = rwi.group9
    tool.append_fieldset(fcli,'io')

    fs_compute = None
    if (has_mpi or has_thread) and fs_compute == None :
        # create mpi 
        fs_compute = rwi.Fieldset(fs, 'parallel_computing',"Parallel Computing")
        tool.append_fieldset(fs_compute,'settings')
    if has_mpi :
        # create mpi
        wmpi = rwi.Widget(fs,'nr_mpi',fs_compute.parent)
        jo = rho.JobOption()
        jo.init_slider("Number of MPI procs:", '{QSUB_NRMPI_VAL}', 1, '{RELION_MPI_MAX}', 1, "Number of MPI nodes to use in parallel. When set to 1, MPI will not be used. The maximum can be set through the environment variable RELION_MPI_MAX.")
        wmpi.set_options(jo)
        fs_compute.append(wmpi)
    if has_thread :
        # create thread
        wthread = rwi.Widget(fs,'nr_threads',fs_compute.parent)
        jo = rho.JobOption()
        jo.init_slider("Number of threads:", '{QSUB_NRTHREADS_VAL}', 1, "{RELION_THREAD_MAX}", 1, "Number of shared-memory (POSIX) threads to use in parallel. When set to 1, no multi-threading will be used. The maximum can be set through the environment variable RELION_THREAD_MAX.")
        wthread.set_options(jo)
        fs_compute.append(wthread)
    return tool


################## RELION SPA FUNCTIONS ##################

def initialiseImportJob(has_mpi = False, has_thread = False):
    # has_gpu = False
    # has_diskio = False
    origin = ["do_raw", "fn_in_raw", "is_multiframe", 
              "optics_group_name", "fn_mtf", "angpix", "beamtilt_x", "beamtilt_y", 
              "do_other", "fn_in_other", "node_type", "optics_group_particles"]

    # Remove duplicates
    keys_raw =  ["fn_in_raw", "is_multiframe", 
              "optics_group_name", "fn_mtf", "angpix", "beamtilt_x", "beamtilt_y"]
    
    keys_ptcls = ["fn_in_other", "node_type", "optics_group_particles"]
    keys_other = ["fn_in_other", "node_type", "optics_group_particles"]
    

    unused_raw = ["do_other", "fn_in_other", "node_type", "optics_group_particles", 
              "node_type", "optics_group_particles"]
    unused_ptcls =["do_raw", "fn_in_raw", "is_multiframe", 
              "optics_group_name", "fn_mtf", "angpix", "beamtilt_x", "beamtilt_y", ]
    unused_other = ["do_raw", "fn_in_raw", "is_multiframe", 
              "optics_group_name", "fn_mtf", "angpix", "beamtilt_x", "beamtilt_y"]

    system_raw = [("do_raw", True), ("do_other", False)]
    system_other = [("do_raw", False), ("do_other", True)]

    ##### IMPORT RAW 
    # 1. Create tool and tabs
    tool = create_tool('import_mov',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseImportJob(False)
    # 3. Build
    groups = rwi.initialiseImportWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_raw)

    tool = update_system_fieldset(tool, has_mpi, has_thread, groups.groups[0], jo, system_raw)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/01_import/01.star',has_mpi, has_thread)

    #####  Import PARTICLES 

    # 1. Create tool and tabs
    tool = create_tool('import_ptcls',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseImportJob(False, "ptcls")
    # 3. Build
    groups = rwi.initialiseImportWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_ptcls)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_other)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/01_import/02.star',has_mpi, has_thread)

    #####  Import OTHER 

    # 1. Create tool and tabs
    tool = create_tool('import_other',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseImportJob(False, "other")
    # 3. Build
    groups = rwi.initialiseImportWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_other)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_other)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/01_import/03.star',has_mpi, has_thread)

def initialiseMotioncorrJob(has_mpi = True, has_thread = True):

    # has_gpu = False
    # has_diskio = False
    origin = ["input_star_mics", "input_star_mics", "first_frame_sum", "last_frame_sum", 
              "eer_grouping", "do_float16", "do_even_odd_split", "bfactor", "patch_x", "patch_y", 
              "group_frames", "bin_factor", "fn_gain_ref", "gain_rot", "gain_flip", "do_own_motioncor", 
              "fn_motioncor2_exe", "fn_defect", "gpu_ids", "other_motioncor2_args", "do_dose_weighting", "do_save_noDW",
              "dose_per_frame", "pre_exposure", "do_save_ps", "group_for_ps", "group_for_ps"]

    keys_rln = ["input_star_mics", "first_frame_sum", "last_frame_sum", 
              "eer_grouping", "do_float16", "do_even_odd_split", "bfactor", "patch_x", "patch_y", 
              "group_frames", "bin_factor", "fn_gain_ref", "gain_rot", "gain_flip", "do_dose_weighting", "do_save_noDW",
              "dose_per_frame", "pre_exposure", "do_save_ps", "group_for_ps", "group_for_ps"]
    keys_ucsf = ["input_star_mics","first_frame_sum", "last_frame_sum", 
              "eer_grouping", "do_float16", "do_even_odd_split", "bfactor", "patch_x", "patch_y", 
              "group_frames", "bin_factor", "fn_gain_ref", "gain_rot", "gain_flip",
              "fn_motioncor2_exe", "fn_defect", "gpu_ids", "other_motioncor2_args", "do_dose_weighting", "do_save_noDW",
              "dose_per_frame", "pre_exposure", "do_save_ps", "group_for_ps", "group_for_ps"]
    
    unused_rln = ["do_own_motioncor", "fn_motioncor2_exe", "fn_defect", "gpu_ids", "other_motioncor2_args"]
    unused_ucsf = ["do_own_motioncor"]

    system_rln = [("do_own_motioncor",True)]
    system_ucsf = [("do_own_motioncor",False)]

    #####   RELION implementation
    # 1. Create tool and tabs
    tool = create_tool('rln_mc',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseMotioncorrJob(False)
    # 3. Read the commands
    outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/${RELION_NEW_JOB}/'
    prog = rcmd.getCommandsMotioncorrJob(jo,outputname)
    # 4. Build
    groups = rwi.initialiseMotioncorrWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_rln)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, prog, system_rln)

    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/02_preprocess/01.star',has_mpi, has_thread)

    #####   UCSF implementation
    # 1. Create tool and tabs
    tool = create_tool('ucsf_mc',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseMotioncorrJob(False)
    # 3. Read the commands
    outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/${RELION_NEW_JOB}/'
    prog = rcmd.getCommandsMotioncorrJob(jo,outputname)
    # 4. Build
    groups = rwi.initialiseMotioncorrWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_ucsf)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, prog, system_ucsf)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/02_preprocess/02.star',has_mpi, has_thread)

def initialiseCtffindJob(has_mpi = True, has_thread = False):
    # has_gpu = False
    # has_diskio = False
    origin = ["input_star_mics", "input_star_mics", "do_phaseshift", "phase_min", "phase_max", "phase_step",
              "dast", "use_given_ps", "fn_ctffind_exe", "slow_search", "box", "resmin", "resmax", "dfmin",
              "dfmax", "dfstep", "localsearch_nominal_defocus", "exp_factor_dose", "ctf_win"]
    
    keys = ["input_star_mics", "input_star_mics", "do_phaseshift", "phase_min", "phase_max", "phase_step",
              "dast", "use_given_ps", "fn_ctffind_exe", "slow_search", "box", "resmin", "resmax", "dfmin",
              "dfmax", "dfstep", "localsearch_nominal_defocus", "exp_factor_dose", "ctf_win"]
    
    unused = []
    system = []

    # 1. Create tool and tabs
    tool = create_tool('ctf',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseCtffindJob(False)
    # 3. Build
    groups = rwi.initialiseCtffindWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/02_preprocess/03.star',has_mpi, has_thread)


def initialiseManualpickJob(has_mpi = False, has_thread = False):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_in", "diameter", "micscale", "sigma_contrast", "white_val", "black_val", "lowpass", 
              "highpass", "angpix", "do_topaz_denoise", "do_startend", "do_fom_threshold", "minimum_pick_fom",
              "do_color", "color_label", "fn_color", "blue_value", "red_value"]


def initialiseAutopickJob(has_mpi = True, has_thread = False):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_input_autopick", "angpix", "continue_manual", "do_log", "log_diam_min", "log_diam_max", 
              "log_invert", "log_maxres", "log_adjust_thr", "log_upper_thr", "do_topaz", "do_topaz_train", 
              "topaz_train_picks", "do_topaz_train_parts", "topaz_train_parts", "do_topaz_pick", "topaz_particle_diameter", 
              "topaz_nr_particles", "topaz_model", "fn_topaz_exe", "do_topaz_filaments", "topaz_filament_threshold", 
              "topaz_hough_length", "topaz_other_args", "do_refs", "fn_refs_autopick", "do_ref3d", "fn_ref3d_autopick", 
              "ref3d_symmetry", "ref3d_sampling", "lowpass", "highpass", "angpix_ref", "psi_sampling_autopick", "do_invert_refs", 
              "do_ctf_autopick", "do_ignore_first_ctfpeak_autopick", "threshold_autopick", "mindist_autopick", "maxstddevnoise_autopick", 
              "minavgnoise_autopick", "do_write_fom_maps", "do_read_fom_maps", "shrink", "use_gpu", "gpu_ids", "do_pick_helical_segments", 
              "do_amyloid", "helical_tube_outer_diameter", "helical_nr_asu", "helical_rise", "helical_tube_kappa_max", 
              "helical_tube_length_min"]
    
    keys_log = ["fn_input_autopick", "angpix", "log_diam_min", "log_diam_max", 
              "log_invert", "log_maxres", "log_adjust_thr", "log_upper_thr", "threshold_autopick", "mindist_autopick", "maxstddevnoise_autopick", 
              "minavgnoise_autopick", "do_write_fom_maps", "do_read_fom_maps", "shrink"]
    
    keys_ref2d = ["fn_input_autopick", "angpix", "fn_refs_autopick", "lowpass", "highpass", "angpix_ref", "psi_sampling_autopick", "do_invert_refs", 
              "do_ctf_autopick", "do_ignore_first_ctfpeak_autopick", "threshold_autopick", "mindist_autopick", "maxstddevnoise_autopick", 
              "minavgnoise_autopick", "do_write_fom_maps", "do_read_fom_maps", "shrink", "use_gpu", "gpu_ids", ]
    keys_ref3d = ["fn_input_autopick", "angpix", "fn_ref3d_autopick", 
              "ref3d_symmetry", "ref3d_sampling", "lowpass", "highpass", "angpix_ref", "psi_sampling_autopick", "do_invert_refs", 
              "do_ctf_autopick", "do_ignore_first_ctfpeak_autopick", "threshold_autopick", "mindist_autopick", "maxstddevnoise_autopick", 
              "minavgnoise_autopick", "do_write_fom_maps", "do_read_fom_maps", "shrink", "use_gpu", "gpu_ids", ]
    
    keys_topaz_train = ["fn_input_autopick", "angpix", 
              "topaz_train_picks", "do_topaz_train_parts", "topaz_train_parts", "topaz_particle_diameter", 
              "topaz_nr_particles", "fn_topaz_exe", "topaz_other_args", "threshold_autopick", "mindist_autopick", "maxstddevnoise_autopick", 
              "minavgnoise_autopick", "do_write_fom_maps", "do_read_fom_maps", "shrink", "use_gpu", "gpu_ids"]
    keys_topaz_pick = ["fn_input_autopick", "angpix", "do_topaz_pick", "topaz_particle_diameter", 
              "topaz_model", "fn_topaz_exe", "do_topaz_filaments", "topaz_filament_threshold", 
              "topaz_hough_length", "topaz_other_args", "threshold_autopick", "mindist_autopick", "maxstddevnoise_autopick", 
              "minavgnoise_autopick", "do_write_fom_maps", "do_read_fom_maps", "shrink", "use_gpu", "gpu_ids"]
    
    unused_log = ["continue_manual", "do_topaz", "do_topaz_train", 
              "topaz_train_picks", "do_topaz_train_parts", "topaz_train_parts", "do_topaz_pick", "topaz_particle_diameter", 
              "topaz_nr_particles", "topaz_model", "fn_topaz_exe", "do_topaz_filaments", "topaz_filament_threshold", 
              "topaz_hough_length", "topaz_other_args", "do_refs", "fn_refs_autopick", "do_ref3d", "fn_ref3d_autopick", 
              "ref3d_symmetry", "ref3d_sampling", "lowpass", "highpass", "angpix_ref", "psi_sampling_autopick", "do_invert_refs", 
              "do_ctf_autopick", "do_ignore_first_ctfpeak_autopick", "use_gpu", "gpu_ids", "do_pick_helical_segments", 
              "do_amyloid", "helical_tube_outer_diameter", "helical_nr_asu", "helical_rise", "helical_tube_kappa_max", 
              "helical_tube_length_min"]
    unused_ref2d = ["continue_manual", "do_log", "log_diam_min", "log_diam_max", 
              "log_invert", "log_maxres", "log_adjust_thr", "log_upper_thr", "do_topaz", "do_topaz_train", 
              "topaz_train_picks", "do_topaz_train_parts", "topaz_train_parts", "do_topaz_pick", "topaz_particle_diameter", 
              "topaz_nr_particles", "topaz_model", "fn_topaz_exe", "do_topaz_filaments", "topaz_filament_threshold", 
              "topaz_hough_length", "topaz_other_args", "do_ref3d", "fn_ref3d_autopick", 
              "ref3d_symmetry", "ref3d_sampling", "do_pick_helical_segments", 
              "do_amyloid", "helical_tube_outer_diameter", "helical_nr_asu", "helical_rise", "helical_tube_kappa_max", 
              "helical_tube_length_min"]
    unused_ref3d = ["continue_manual", "do_log", "log_diam_min", "log_diam_max", 
              "log_invert", "log_maxres", "log_adjust_thr", "log_upper_thr", "do_topaz", "do_topaz_train", 
              "topaz_train_picks", "do_topaz_train_parts", "topaz_train_parts", "do_topaz_pick", "topaz_particle_diameter", 
              "topaz_nr_particles", "topaz_model", "fn_topaz_exe", "do_topaz_filaments", "topaz_filament_threshold", 
              "topaz_hough_length", "topaz_other_args", "fn_refs_autopick", "do_pick_helical_segments", 
              "do_amyloid", "helical_tube_outer_diameter", "helical_nr_asu", "helical_rise", "helical_tube_kappa_max", 
              "helical_tube_length_min"]
    unused_topaz_train = ["continue_manual", "do_log", "log_diam_min", "log_diam_max", 
              "log_invert", "log_maxres", "log_adjust_thr", "log_upper_thr", "do_topaz_pick", "topaz_model", "do_topaz_filaments", "topaz_filament_threshold", 
              "topaz_hough_length", "do_refs", "fn_refs_autopick", "do_ref3d", "fn_ref3d_autopick", 
              "ref3d_symmetry", "ref3d_sampling", "lowpass", "highpass", "angpix_ref", "psi_sampling_autopick", "do_invert_refs", 
              "do_ctf_autopick", "do_ignore_first_ctfpeak_autopick", "do_pick_helical_segments", 
              "do_amyloid", "helical_tube_outer_diameter", "helical_nr_asu", "helical_rise", "helical_tube_kappa_max", 
              "helical_tube_length_min"]
    unused_topaz_pick = ["continue_manual", "do_log", "log_diam_min", "log_diam_max", 
              "log_invert", "log_maxres", "log_adjust_thr", "log_upper_thr", "do_topaz_train", 
              "topaz_train_picks", "do_topaz_train_parts", "topaz_train_parts", "topaz_nr_particles", "do_refs", "fn_refs_autopick", "do_ref3d", "fn_ref3d_autopick", 
              "ref3d_symmetry", "ref3d_sampling", "lowpass", "highpass", "angpix_ref", "psi_sampling_autopick", "do_invert_refs", 
              "do_ctf_autopick", "do_ignore_first_ctfpeak_autopick", "do_pick_helical_segments", 
              "do_amyloid", "helical_tube_outer_diameter", "helical_nr_asu", "helical_rise", "helical_tube_kappa_max", 
              "helical_tube_length_min"]

    system_log = [("do_log", True), ("do_refs", False), ("do_ref3d", False), ("do_topaz_train", False), ("do_topaz_pick", False)]
    system_ref2d = [("do_log", False), ("do_refs", True), ("do_ref3d", False), ("do_topaz_train", False), ("do_topaz_pick", False)]
    system_ref3d = [("do_log", False), ("do_refs", False), ("do_ref3d", True), ("do_topaz_train", False), ("do_topaz_pick", False)]
    system_topaz_train = [("do_log", False), ("do_refs", False), ("do_ref3d", False), ("do_topaz_train", True), ("do_topaz_pick", False)]
    system_topaz_pick = [("do_log", False), ("do_refs", False), ("do_ref3d", False), ("do_topaz_train", False), ("do_topaz_pick", True)]

    #####  Laplacian of Gaussian
    # 1. Create tool and tabs
    tool = create_tool('log_filter',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseAutopickJob(False)
    # 3. Build
    groups = rwi.initialiseAutopickWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_log)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_log)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/03_particles/01.star',has_mpi, has_thread)

    #####  2D References
    # 1. Create tool and tabs
    tool = create_tool('ref2d',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseAutopickJob(False)
    # 3. Build
    groups = rwi.initialiseAutopickWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_ref2d)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_ref2d)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/03_particles/02.star',has_mpi, has_thread)

    #####  3D References
    # 1. Create tool and tabs
    tool = create_tool('ref3d',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseAutopickJob(False)
    # 3. Build
    groups = rwi.initialiseAutopickWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_ref3d)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_ref3d)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/03_particles/03.star',has_mpi, has_thread)

    #####  Topaz Training
    # 1. Create tool and tabs
    tool = create_tool('topaz_train',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseAutopickJob(False)
    # 3. Build
    groups = rwi.initialiseAutopickWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_topaz_train)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_topaz_train)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/03_particles/04.star',has_mpi, has_thread)

    #####  Topaz Picker
    # 1. Create tool and tabs
    tool = create_tool('topaz_pick',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseAutopickJob(False)
    # 3. Build
    groups = rwi.initialiseAutopickWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_topaz_pick)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_topaz_pick)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/03_particles/05.star',has_mpi, has_thread)


def initialiseExtractJob(has_mpi = True, has_thread = False):

    # has_gpu = False
    # has_diskio = False
    origin = ["star_mics", "coords_suffix", "do_reextract", "fndata_reextract", "do_reset_offsets",
                "do_recenter", "recenter_x", "recenter_y", "recenter_z", "extract_size", "do_invert",
                "do_float16", "do_norm", "bg_diameter", "white_dust", "black_dust", "do_rescale", "rescale", 
                "do_fom_threshold", "minimum_pick_fom", "do_extract_helix", "helical_tube_outer_diameter",
                "helical_bimodal_angular_priors", "do_extract_helical_tubes", "do_cut_into_segments", 
                "helical_nr_asu", "helical_rise"]
    
    keys = ["star_mics", "coords_suffix", "extract_size", "do_invert",
                "do_float16", "do_norm", "bg_diameter", "white_dust", "black_dust", "do_rescale", "rescale", 
                "do_fom_threshold", "minimum_pick_fom"]

    keys_re = ["star_mics", "coords_suffix", "fndata_reextract", "do_reset_offsets",
                "do_recenter", "recenter_x", "recenter_y", "recenter_z", "extract_size", "do_invert",
                "do_float16", "do_norm", "bg_diameter", "white_dust", "black_dust", "do_rescale", "rescale", 
                "do_fom_threshold", "minimum_pick_fom"]
    
    unused = ["do_reextract", "fndata_reextract", "do_reset_offsets",
                "do_recenter", "recenter_x", "recenter_y", "recenter_z", "do_extract_helix", "helical_tube_outer_diameter",
                "helical_bimodal_angular_priors", "do_extract_helical_tubes", "do_cut_into_segments", 
                "helical_nr_asu", "helical_rise"]
    unused_re = ["do_extract_helix", "helical_tube_outer_diameter",
                "helical_bimodal_angular_priors", "do_extract_helical_tubes", "do_cut_into_segments", 
                "helical_nr_asu", "helical_rise"]

    system = [("do_reextract", False)]
    system_re =[("do_reextract", True)]

    #####  EXTRACT PARTICLES
    # 1. Create tool and tabs
    tool = create_tool('extract_ptcls',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseExtractJob(False)
    # 3. Build
    groups = rwi.initialiseExtractWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/03_particles/06.star',has_mpi, has_thread)

    #####  RE-EXTRACT PARTICLES
    # 1. Create tool and tabs
    tool = create_tool('reextract_ptcls',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseExtractJob(False)
    # 3. Build
    groups = rwi.initialiseExtractWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_re)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_re)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/03_particles/07.star',has_mpi, has_thread)


def initialiseSelectJob(has_mpi = False, has_thread = False):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_model", "fn_mic", "fn_data", "do_class_ranker", "rank_threshold", "select_nr_parts", 
              "select_nr_classes", "do_recenter", "do_regroup", "nr_groups", "do_select_values", "select_label", 
              "select_minval", "select_maxval", "do_discard", "discard_label", "discard_sigma", "do_split", 
              "do_random", "split_size", "nr_split", "do_remove_duplicates", "duplicate_threshold", "image_angpix", 
              "do_filaments", "dendrogram_threshold", "dendrogram_minclass"]
    
    keys_class = ["fn_model", "do_class_ranker", "rank_threshold", "select_nr_parts", 
              "select_nr_classes", "do_recenter", "do_regroup", "nr_groups", "do_select_values", "select_label", 
              "select_minval", "select_maxval", "do_discard", "discard_label", "discard_sigma", "do_split", 
              "do_random", "split_size", "nr_split", "do_remove_duplicates", "duplicate_threshold", "image_angpix", 
              "do_filaments", "dendrogram_threshold", "dendrogram_minclass"]
    keys_mic = ["fn_mic", "do_class_ranker", "rank_threshold", "select_nr_parts", 
              "select_nr_classes", "do_recenter", "do_regroup", "nr_groups", "do_select_values", "select_label", 
              "select_minval", "select_maxval", "do_discard", "discard_label", "discard_sigma", "do_split", 
              "do_random", "split_size", "nr_split", "do_remove_duplicates", "duplicate_threshold", "image_angpix", 
              "do_filaments", "dendrogram_threshold", "dendrogram_minclass"]
    keys_ptcls = ["fn_data", "do_class_ranker", "rank_threshold", "select_nr_parts", 
              "select_nr_classes", "do_recenter", "do_regroup", "nr_groups", "do_select_values", "select_label", 
              "select_minval", "select_maxval", "do_discard", "discard_label", "discard_sigma", "do_split", 
              "do_random", "split_size", "nr_split", "do_remove_duplicates", "duplicate_threshold", "image_angpix", 
              "do_filaments", "dendrogram_threshold", "dendrogram_minclass"]

    unused = []

    system = []
    
    ##### SUBSET SELECTION CLASSES
    # 1. Create tool and tabs
    tool = create_tool('subselect_class',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseSelectJob(False)
    # 3. Build
    groups = rwi.initialiseSelectWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_class)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/08_tools/01.star',has_mpi, has_thread)

    ##### SUBSET SELECTION FROM MICROGRAPHS
    # 1. Create tool and tabs
    tool = create_tool('subselect_mic',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseSelectJob(False)
    # 3. Build
    groups = rwi.initialiseSelectWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_mic)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/08_tools/02.star',has_mpi, has_thread)

    ##### SUBSET SELECTION FROM PARTICLES
    # 1. Create tool and tabs
    tool = create_tool('subselect_ptcls',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseSelectJob(False)
    # 3. Build
    groups = rwi.initialiseSelectWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_ptcls)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/08_tools/03.star',has_mpi, has_thread)


def initialiseClass2DJob(has_mpi = True, has_thread = True):
    # has_gpu = False
    # has_diskio = False
    origin = ["fn_img", "fn_cont", "do_ctf_correction", "ctf_intact_first_peak", "nr_classes", "tau_fudge", "do_em", 
              "nr_iter_em", "do_grad", "nr_iter_grad", "particle_diameter", "do_zero_mask", "highres_limit", "do_center", 
              "dont_skip_ali gn", "psi_sampling", "offset_range", "offset_step", "allow_coarser", "do_helix", 
              "helical_tube_outer_diameter", "do_bimodal_psi", "range_psi", "do_restrict_xoff", "helical_rise", 
              "nr_pool", "do_parallel_discio", "do_preread_images", "scratch_dir", "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    
    keys_em = ["fn_img", "do_ctf_correction", "ctf_intact_first_peak", "nr_classes", "tau_fudge",  
              "nr_iter_em", "particle_diameter", "do_zero_mask", "highres_limit", "do_center", 
              "dont_skip_align", "psi_sampling", "offset_range", "offset_step", "allow_coarser",
              "nr_pool", "do_parallel_discio", "do_preread_images", "scratch_dir", "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    
    keys_vdam = ["fn_img", "do_ctf_correction", "ctf_intact_first_peak", "nr_classes", "tau_fudge", 
              "nr_iter_grad", "particle_diameter", "do_zero_mask", "highres_limit", "do_center", 
              "dont_skip_align", "psi_sampling", "offset_range", "offset_step", "allow_coarser", 
              "nr_pool", "do_parallel_discio", "do_preread_images", "scratch_dir", "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    
    unused_em = ["fn_cont", "do_grad", "nr_iter_grad", "do_helix", 
              "helical_tube_outer_diameter", "do_bimodal_psi", "range_psi", "do_restrict_xoff", "helical_rise"]
    unused_vdam = ["fn_cont", "do_em", "nr_iter_em", "do_helix", 
              "helical_tube_outer_diameter", "do_bimodal_psi", "range_psi", "do_restrict_xoff", "helical_rise"]
    
    system_em = [("do_em",True),("do_grad",False)]
    system_vdam = [("do_em",False),("do_grad",True)]

    #####  EM Algorithm 
    # 1. Create tool and tabs
    tool = create_tool('class2d_em',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseClass2DJob(False)
    # 3. Build
    groups = rwi.initialiseClass2DWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_em)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_em)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/03_particles/08.star',has_mpi, has_thread)

    #####  VDAM Algorithm 

    # 1. Create tool and tabs
    tool = create_tool('class2d_vdam',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseClass2DJob(False)
    # 3. Build
    groups = rwi.initialiseClass2DWindow()
    for fs_params in groups:
        tool = update_fieldset(tool,   fs_params,jo,keys_vdam)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_vdam)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/03_particles/09.star',has_mpi, has_thread)

def initialiseInimodelJob(has_mpi = True, has_thread = True):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_img", "fn_cont", "nr_iter", "tau_fudge", "nr_classes", "sym_name", "particle_diameter", "do_solvent", 
              "sigma_tilt", "do_ctf_correction", "ctf_intact_first_peak", "do_parallel_discio", "nr_pool", "do_preread_images", 
              "scratch_dir", "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    
    keys = ["fn_img", "nr_iter", "tau_fudge", "nr_classes", "sym_name", "particle_diameter", "do_solvent", 
            "do_ctf_correction", "ctf_intact_first_peak", "do_parallel_discio", "nr_pool", "do_preread_images", 
              "scratch_dir", "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    
    unused = ["fn_cont", "sigma_tilt"]
    system = []

    # 1. Create tool and tabs
    tool = create_tool('inimodel',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseInimodelJob(False)
    # 3. Build
    groups = rwi.initialiseInimodelWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/04_3d/01.star',has_mpi, has_thread)
1

def initialiseClass3DJob(has_mpi = True, has_thread = True):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_img", "fn_cont", "fn_ref", "fn_mask", "ref_correct_greyscale", "trust_ref_size", "ini_high", "sym_name", 
              "do_ctf_correction", "ctf_intact_first_peak", "nr_classes", "tau_fudge", "nr_iter", "do_fast_subsets", 
              "particle_diameter", "do_zero_mask", "highres_limit", "do_blush", "dont_skip_align", "sampling", "offset_range", 
              "offset_step", "do_local_ang_searches", "sigma_angles", "allow_coarser", "relax_sym", "sigma_tilt", "do_helix", 
              "helical_tube_inner_diameter", "helical_tube_outer_diameter", "range_rot", "range_tilt", "range_psi", 
              "do_apply_helical_symmetry", "helical_nr_asu", "helical_twist_initial", "helical_rise_initial", "helical_z_percentage", 
              "do_local_search_helical_symmetry", "helical_twist_min", "helical_twist_max", "helical_twist_inistep", "helical_rise_min", 
              "helical_rise_max", "helical_rise_inistep", "helical_range_distance", "keep_tilt_prior_fixed", "do_parallel_discio", "nr_pool", 
              "do_pad1", "do_preread_images", "scratch_dir", "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    
    keys_align = ["fn_img", "fn_ref", "fn_mask", "ref_correct_greyscale", "trust_ref_size", "ini_high", "sym_name", 
              "do_ctf_correction", "ctf_intact_first_peak", "nr_classes", "tau_fudge", "nr_iter", "do_fast_subsets", 
              "particle_diameter", "do_zero_mask", "highres_limit", "do_blush", "sampling", "offset_range", 
              "offset_step", "do_local_ang_searches", "sigma_angles", "allow_coarser", "relax_sym", "do_parallel_discio", "nr_pool", 
              "do_pad1", "do_preread_images", "scratch_dir", "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    keys_skip = ["fn_img", "fn_ref", "fn_mask", "ref_correct_greyscale", "trust_ref_size", "ini_high", "sym_name", 
              "do_ctf_correction", "ctf_intact_first_peak", "nr_classes", "tau_fudge", "nr_iter", "do_fast_subsets", 
              "particle_diameter", "do_zero_mask", "highres_limit", "do_blush", "do_parallel_discio", "nr_pool", 
              "do_pad1", "do_preread_images", "scratch_dir", "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    
    unused_align = ["fn_cont", "sigma_tilt", "do_helix", 
              "helical_tube_inner_diameter", "helical_tube_outer_diameter", "range_rot", "range_tilt", "range_psi", 
              "do_apply_helical_symmetry", "helical_nr_asu", "helical_twist_initial", "helical_rise_initial", "helical_z_percentage", 
              "do_local_search_helical_symmetry", "helical_twist_min", "helical_twist_max", "helical_twist_inistep", "helical_rise_min", 
              "helical_rise_max", "helical_rise_inistep", "helical_range_distance", "keep_tilt_prior_fixed"]
    unused_skip = ["fn_cont", "dont_skip_align", "sampling", "offset_range", 
              "offset_step", "do_local_ang_searches", "sigma_angles", "allow_coarser", "relax_sym", "sigma_tilt", "do_helix", 
              "helical_tube_inner_diameter", "helical_tube_outer_diameter", "range_rot", "range_tilt", "range_psi", 
              "do_apply_helical_symmetry", "helical_nr_asu", "helical_twist_initial", "helical_rise_initial", "helical_z_percentage", 
              "do_local_search_helical_symmetry", "helical_twist_min", "helical_twist_max", "helical_twist_inistep", "helical_rise_min", 
              "helical_rise_max", "helical_rise_inistep", "helical_range_distance", "keep_tilt_prior_fixed"]

    system_align = [("dont_skip_align", True)]
    system_skip = [("dont_skip_align", False)]

    ##### 3D CLASS WITH IMAGE ALIGNMENT
    # 1. Create tool and tabs
    tool = create_tool('3d_align',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseClass3DJob(False)
    # 3. Build
    groups = rwi.initialiseClass3DWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_align)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_align)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/04_3d/02.star',has_mpi, has_thread)

    #####  3D CLASS WITHOUT IMAGE ALIGNMENT
    # 1. Create tool and tabs
    tool = create_tool('3d_skip_align',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseClass3DJob(False)
    # 3. Build
    groups = rwi.initialiseClass3DWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_skip)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_skip)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/04_3d/03.star',has_mpi, has_thread)



def initialiseAutorefineJob(has_mpi = True, has_thread = True):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_img", "fn_cont", "fn_ref", "fn_mask", "ref_correct_greyscale", "trust_ref_size", "ini_high", "sym_name", 
              "do_ctf_correction", "ctf_intact_first_peak", "particle_diameter", "do_zero_mask", "do_solvent_fsc", "do_blush", 
              "sampling", "offset_range", "offset_step", "auto_local_sampling", "relax_sym", "auto_faster", "sigma_tilt", "do_helix", 
              "helical_tube_inner_diameter", "helical_tube_outer_diameter", "range_rot", "range_tilt", "range_psi", "do_apply_helical_symmetry", 
              "helical_nr_asu", "helical_twist_initial", "helical_rise_initial", "helical_z_percentage", "do_local_search_helical_symmetry", 
              "helical_twist_min", "helical_twist_max", "helical_twist_inistep", "helical_rise_min", "helical_rise_max", "helical_rise_inistep", 
              "helical_range_distance", "keep_tilt_prior_fixed", "do_parallel_discio", "nr_pool", "do_pad1", "do_preread_images", "scratch_dir", 
              "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    
    keys = ["fn_img", "fn_ref", "fn_mask", "ref_correct_greyscale", "trust_ref_size", "ini_high", "sym_name", 
              "do_ctf_correction", "ctf_intact_first_peak", "particle_diameter", "do_zero_mask", "do_solvent_fsc", "do_blush", 
              "sampling", "offset_range", "offset_step", "auto_local_sampling", "relax_sym", "auto_faster", "do_parallel_discio", "nr_pool", "do_pad1", "do_preread_images", "scratch_dir", 
              "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    
    unused = ["fn_cont", "sigma_tilt", "do_helix", 
              "helical_tube_inner_diameter", "helical_tube_outer_diameter", "range_rot", "range_tilt", "range_psi", "do_apply_helical_symmetry", 
              "helical_nr_asu", "helical_twist_initial", "helical_rise_initial", "helical_z_percentage", "do_local_search_helical_symmetry", 
              "helical_twist_min", "helical_twist_max", "helical_twist_inistep", "helical_rise_min", "helical_rise_max", "helical_rise_inistep", 
              "helical_range_distance", "keep_tilt_prior_fixed"]
    system = []

    # 1. Create tool and tabs
    tool = create_tool('autorefine',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseAutorefineJob(False)
    # 3. Build
    groups = rwi.initialiseAutorefineWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/04_3d/04.star',has_mpi, has_thread)



def initialiseMultiBodyJob(has_mpi = True, has_thread = True):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_in", "fn_cont", "fn_bodies", "do_subtracted_bodies", "do_blush", "sampling", "offset_range", "offset_step", 
              "do_analyse", "nr_movies", "do_select", "select_eigenval", "eigenval_min", "eigenval_max", "do_parallel_discio",
              "nr_pool", "do_pad1", "do_preread_images", "scratch_dir", "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    
    keys_flex = ["fn_in", "fn_bodies", "do_subtracted_bodies", "do_blush", "sampling", "offset_range", "offset_step", 
              "nr_movies", "do_select", "select_eigenval", "eigenval_min", "eigenval_max", "do_parallel_discio",
              "nr_pool", "do_pad1", "do_preread_images", "scratch_dir", "do_combine_thru_disc", "use_gpu", "gpu_ids"]
    
    keys_no_flex = ["fn_in", "fn_bodies", "do_subtracted_bodies", "do_blush", "sampling", "offset_range", "offset_step", 
              "do_parallel_discio", "nr_pool", "do_pad1", "do_preread_images", "scratch_dir", "do_combine_thru_disc", "use_gpu", "gpu_ids"]

    unused_flex = ["fn_cont", ]
    unused_no_flex = ["fn_cont", "do_analyse", "nr_movies", "do_select", "select_eigenval", "eigenval_min", "eigenval_max"]

    system_flex = [("do_analyse", True)]
    system_no_flex = [("do_analyse", False)]


    #####  MULTI-BODY WITH FLEXIBILITY ANALYSIS
    # 1. Create tool and tabs
    tool = create_tool('multibody_flex',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseMultiBodyJob(False)
    # 3. Build
    groups = rwi.initialiseMultiBodyWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_flex)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_flex)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/04_3d/05.star',has_mpi, has_thread)

    #####  MULTI-BODY
    # 1. Create tool and tabs
    tool = create_tool('multibody',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseMultiBodyJob(False)
    # 3. Build
    groups = rwi.initialiseMultiBodyWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_no_flex)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_no_flex)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/04_3d/06.star',has_mpi, has_thread)


def initialiseMaskcreateJob(has_mpi = False, has_thread = True):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_in", "lowpass_filter", "angpix", "inimask_threshold", "extend_inimask", "width_mask_edge", "do_helix", 
              "helical_z_percentage"]

    keys = ["fn_in", "lowpass_filter", "angpix", "inimask_threshold", "extend_inimask", "width_mask_edge"]
    
    unused = ["do_helix", "helical_z_percentage"]
    system = []

    # 1. Create tool and tabs
    tool = create_tool('mask_create',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseMaskcreateJob(False)
    # 3. Build
    groups = rwi.initialiseMaskcreateWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/06_enhance/01.star',has_mpi, has_thread)


def initialiseJoinstarJob(has_mpi = False, has_thread = False):

    # has_gpu = False
    # has_diskio = False
    origin = ["do_part", "fn_part1", "fn_part2", "fn_part3", "fn_part4", "do_mic", "fn_mic1", "fn_mic2", "fn_mic3", "fn_mic4", 
              "do_mov", "fn_mov1", "fn_mov2", "fn_mov3", "fn_mov4"]
    
    keys_ptcls = ["fn_part1", "fn_part2", "fn_part3", "fn_part4"]
    keys_mic = ["fn_mic1", "fn_mic2", "fn_mic3", "fn_mic4"]
    keys_mov = ["fn_mov1", "fn_mov2", "fn_mov3", "fn_mov4"]
    
    unused_ptcls = ["do_mic", "fn_mic1", "fn_mic2", "fn_mic3", "fn_mic4", 
              "do_mov", "fn_mov1", "fn_mov2", "fn_mov3", "fn_mov4"]
    unused_mic = ["do_part", "fn_part1", "fn_part2", "fn_part3", "fn_part4", "do_mov", "fn_mov1", "fn_mov2", "fn_mov3", "fn_mov4"]
    unused_mov = ["do_part", "fn_part1", "fn_part2", "fn_part3", "fn_part4", "do_mic", "fn_mic1", "fn_mic2", "fn_mic3", "fn_mic4"]

    system_ptcls = [("do_part", True), ("do_mic", False), ("do_mov", False)]
    system_mic = [("do_part", False), ("do_mic", True), ("do_mov", False)]
    system_mov = [("do_part", False), ("do_mic", False), ("do_mov", True)]

    #####  JOIN PARTICLES
    # 1. Create tool and tabs
    tool = create_tool('join_ptcls',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseJoinstarJob(False)
    # 3. Build
    groups = rwi.initialiseJoinstarWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_ptcls)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_ptcls)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/08_tools/04.star',has_mpi, has_thread)

        #####  JOIN MICROGRAPHS
    # 1. Create tool and tabs
    tool = create_tool('join_mics',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseJoinstarJob(False)
    # 3. Build
    groups = rwi.initialiseJoinstarWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_mic)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_mic)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/08_tools/05.star',has_mpi, has_thread)

    #####  JOIN MOVIES
    # 1. Create tool and tabs
    tool = create_tool('join_movs',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseJoinstarJob(False)
    # 3. Build
    groups = rwi.initialiseJoinstarWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_mov)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_mov)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/08_tools/06.star',has_mpi, has_thread)


def initialiseSubtractJob(has_mpi = True, has_thread = False):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_opt", "fn_mask", "do_data", "fn_data", "do_float16", "do_fliplabel", "fn_fliplabel", "do_center_mask", 
              "do_center_xyz", "center_x", "center_y", "center_z", "new_box"] 
    
    keys_mask = ["fn_opt", "fn_mask", "do_data", "fn_data", "do_float16", "do_fliplabel", "fn_fliplabel", "new_box"] 
    keys_coor = ["fn_opt", "fn_mask", "do_data", "fn_data", "do_float16", "do_fliplabel", "fn_fliplabel", "center_x", "center_y", "center_z", "new_box"] 
    
    unused_mask = ["do_center_xyz", "center_x", "center_y", "center_z"]
    unsued_coor = ["do_center_mask"]

    system_mask = [("do_center_mask", True), ("do_center_xyz", False)]
    system_coor = [("do_center_mask", False), ("do_center_xyz", True)]

    #####  CENTER SUBSTRACTED IMAGES ON MASK
    # 1. Create tool and tabs
    tool = create_tool('sub_mask',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseSubtractJob(False)
    # 3. Build
    groups = rwi.initialiseSubtractWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_mask)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_mask)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/06_enhance/02.star',has_mpi, has_thread)

    #####  CENTER ON COORDINATES
    # 1. Create tool and tabs
    tool = create_tool('sub_coor',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseSubtractJob(False)
    # 3. Build
    groups = rwi.initialiseSubtractWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_coor)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_coor)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/06_enhance/03.star',has_mpi, has_thread)

def initialisePostprocessJob(has_mpi = False, has_thread = False):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_in", "fn_mask", "angpix", "do_auto_bfac", "autob_lowres", "do_adhoc_bfac", "adhoc_bfac", "fn_mtf", "mtf_angpix", 
              "do_skip_fsc_weighting", "low_pass"]

    keys = ["fn_in", "fn_mask", "angpix", "do_auto_bfac", "autob_lowres", "do_adhoc_bfac", "adhoc_bfac", "fn_mtf", "mtf_angpix", 
              "do_skip_fsc_weighting", "low_pass"]

    unused = []
    system = []

    # 1. Create tool and tabs
    tool = create_tool('pprcss',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialisePostprocessJob(False)
    # 3. Build
    groups = rwi.initialisePostprocessWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/05_postprocess/01.star',has_mpi, has_thread)


def initialiseLocalresJob(has_mpi = True, has_thread = False):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_in", "angpix", "do_resmap_locres", "fn_resmap", "fn_mask", "pval", "minres", "maxres", "stepres", "do_relion_locres", 
              "locres_sampling", "randomize_at", "adhoc_bfac", "fn_mtf"]
    
    keys_resmap = ["fn_in", "angpix", "fn_resmap", "fn_mask", "pval", "minres", "maxres", "stepres"]
    keys_rln = ["fn_in", "angpix", "fn_mask", "adhoc_bfac", "fn_mtf"]

    unused_resmap = ["do_relion_locres", "adhoc_bfac", "fn_mtf", "locres_sampling", "randomize_at"]
    unused_rln = ["do_resmap_locres", "fn_resmap", "pval", "minres", "maxres", "stepres", "locres_sampling", "randomize_at"]

    system_resmap = [("do_resmap_locres", True), ("do_relion_locres", False)]
    system_rln = [("do_resmap_locres", False), ("do_relion_locres", True)]

    #####  ResMap LOCAL RESOLUTION
    # 1. Create tool and tabs
    tool = create_tool('resmap_locres',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseLocalresJob(False)
    # 3. Build
    groups = rwi.initialiseLocresWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_resmap)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_resmap)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/06_enhance/04.star',has_mpi, has_thread)

    #####  RELION LOCAL RESOLUTION
    # 1. Create tool and tabs
    tool = create_tool('rln_locres',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseLocalresJob(False)
    # 3. Build
    groups = rwi.initialiseLocresWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_rln)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_rln)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/06_enhance/05.star',has_mpi, has_thread)


def initialiseDynaMightJob(has_mpi = False, has_thread = True):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_star", "fn_map", "fn_mask", "gpu_id", "do_preload", "fn_dynamight_exe", "nr_gaussians", "initial_threshold", 
              "reg_factor", "fn_checkpoint", "do_visualize", "halfset", "do_inverse", "nr_epochs", "do_store_deform", "do_reconstruct", 
              "backproject_batchsize"]
    
    keys = ["fn_star", "fn_map", "gpu_id", "do_preload", "fn_dynamight_exe", "nr_gaussians", "initial_threshold", 
              "reg_factor"]

    unused = ["fn_mask", "fn_checkpoint", "do_visualize", "halfset", "do_inverse", "nr_epochs", "do_store_deform", "do_reconstruct", 
              "backproject_batchsize"]
    system = []

     # 1. Create tool and tabs
    tool = create_tool('dynamight',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseDynaMightJob(False)
    # 3. Build
    groups = rwi.initialiseDynaMightWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/04_3d/07.star',has_mpi, has_thread)


def initialiseModelAngeloJob(has_mpi = False, has_thread = False):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_map", "p_seq", "d_seq", "r_seq", "fn_modelangelo_exe", "gpu_id", "do_hhmer", "fn_lib", "alphabet", "F1", "F2", "F3", "E"]
    unused = []
    system = []

    # 1. Create tool and tabs
    tool = create_tool('angelo',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseModelAngeloJob(False)
    # 3. Build
    groups = rwi.initialiseModelAngeloWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,origin)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/07_model/01.star',has_mpi, has_thread)


def initialiseMotionrefineJob(has_mpi = True, has_thread = True):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_mic", "fn_data", "fn_post", "do_float16", "first_frame", "last_frame", "extract_size", "rescale", "do_param_optim", 
              "eval_frac", "optim_min_part", "do_polish", "opt_params", "do_own_params", "sigma_vel", "sigma_div", "sigma_acc", "minres", 
              "maxres"]
    
    keys_ptcls = ["fn_mic", "fn_data", "fn_post", "do_float16", "first_frame", "last_frame", "extract_size", "rescale", "do_param_optim", 
              "eval_frac", "optim_min_part", "opt_params", "do_own_params", "sigma_vel", "sigma_div", "sigma_acc", "minres", 
              "maxres"]
    keys = ["fn_mic", "fn_data", "fn_post", "do_float16", "first_frame", "last_frame", "extract_size", "rescale", "do_param_optim", 
              "eval_frac", "optim_min_part"]

    unused_ptcls = []
    unused = ["do_polish", "opt_params", "do_own_params", "sigma_vel", "sigma_div", "sigma_acc", "minres", "maxres"]

    system_ptcls = [("do_polish", True)]
    system = [("do_polish", False)]
    ##### PERFORM PARTICLE POLISHING
    # 1. Create tool and tabs
    tool = create_tool('ptcls_polish',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseMotionrefineJob(False)
    # 3. Build
    groups = rwi.initialiseMotionrefineWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_ptcls)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_ptcls)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/05_postprocess/02.star',has_mpi, has_thread)

    #### OTHER POLISHING
    # 1. Create tool and tabs
    tool = create_tool('other_polish',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseMotionrefineJob(False)
    # 3. Build
    groups = rwi.initialiseMotionrefineWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/05_postprocess/03.star',has_mpi, has_thread)


def initialiseCtfrefineJob(has_mpi = True, has_thread = True):

    # has_gpu = False
    # has_diskio = False
    origin = ["fn_data", "fn_post", "minres", "do_ctf", "do_defocus", "do_astig", "do_bfactor", "do_phase", "do_aniso_mag", "do_tilt", 
              "do_trefoil", "do_4thorder"]
    
    keys_aniso = ["fn_data", "fn_post", "minres", "do_ctf", "do_defocus", "do_astig", "do_bfactor", "do_phase", "do_tilt", 
              "do_trefoil", "do_4thorder"]
    keys = ["fn_data", "fn_post", "minres"]

    unused_aniso = []
    unsued = ["do_ctf", "do_defocus", "do_astig", "do_bfactor", "do_phase", "do_aniso_mag", "do_tilt", 
              "do_trefoil", "do_4thorder"]

    system_aniso = [("do_aniso_mag", True)]
    system = [("do_aniso_mag", False)]

    #### CTF REFINEMENT WITH ANISOTROPIC MAGNIFICATION ESTIMATION
    # 1. Create tool and tabs
    tool = create_tool('anisomag',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseCtfrefineJob(False)
    # 3. Build
    groups = rwi.initialiseCtfrefineWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys_aniso)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system_aniso)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/05_postprocess/04.star',has_mpi, has_thread)

    #### CTF REFINEMENT
    # 1. Create tool and tabs
    tool = create_tool('ctfref',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseCtfrefineJob(False)
    # 3. Build
    groups = rwi.initialiseCtfrefineWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,keys)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/05_postprocess/05.star',has_mpi, has_thread)


def initialiseExternalJob(has_mpi = False, has_thread = False):
    # has_gpu = False
    # has_diskio = False
    origin = ["fn_exe", "in_mov", "in_mic", "in_part", "in_coords", "in_3dref", "in_mask", "param1_label", "param1_value", "param2_label", 
              "param2_value", "param3_label", "param3_value", "param4_label", "param4_value", "param5_label", "param5_value", "param6_label", 
              "param6_value", "param7_label", "param7_value", "param8_label", "param8_value", "param9_label", "param9_value", "param10_label", 
              "param10_value"]
    
    system = []

    # 1. Create tool and tabs
    tool = create_tool('external',['io','settings','log','dataviz'])
    # 2. Read the joboptions
    hidden_name,jo = rjo.initialiseExternalJob(False)
    # 3. Build
    groups = rwi.initialiseExternalWindow()
    for fs_params in groups:
        tool = update_fieldset(tool, fs_params,jo,origin)

    tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, system)

    # 4. Read the commands
    # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
    # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
    # 5. Create the `outdata`` fieldset
    # 6. Create the script
    # 7. Write the file `xx.star`
    write_starfile(tool,'./public/spa/08_tools/07.star',has_mpi, has_thread)


# def initialiseExternalJob(has_mpi = False, has_thread = True):
#     pass

################### TOMO ###################

def initialiseTomoImportJob(has_mpi = False, has_thread = False):
    pass

def initialiseTomoExcludeTiltImagesJob(has_mpi = False, has_thread = False):
    pass

def initialiseTomoAlignTiltSeriesJob(has_mpi = True, has_thread = False):
    pass

def initialiseTomoReconstructTomogramsJob(has_mpi = True, has_thread = True):
    pass

def initialiseTomoDenoiseTomogramsJob(has_mpi = False, has_thread = False):
    pass

def initialiseTomoPickTomogramsJob(has_mpi = False, has_thread = False):
    pass

def initialiseTomoExcludeTiltImagesJob(has_mpi = False, has_thread = False):
    pass

def initialiseTomoSubtomoJob(has_mpi = True, has_thread = True):
    pass

def initialiseTomoCtfRefineJob(has_mpi = True, has_thread = True):
    pass

def initialiseTomoAlignJob(has_mpi = True, has_thread = True):
    pass

def initialiseTomoReconPartJob(has_mpi = True, has_thread = True):
    pass


if __name__ == '__main__' :
    initialiseImportJob()
    initialiseMotioncorrJob()
    initialiseCtffindJob()
    # initialiseManualpickJob()
    initialiseAutopickJob()
    initialiseExtractJob()
    initialiseSelectJob()
    initialiseClass2DJob()
    initialiseInimodelJob()
    initialiseClass3DJob()
    initialiseAutorefineJob()
    initialiseMultiBodyJob()
    initialiseMaskcreateJob()
    initialiseJoinstarJob()
    initialiseSubtractJob()
    initialisePostprocessJob()
    initialiseLocalresJob()
    initialiseDynaMightJob()
    initialiseModelAngeloJob()
    initialiseMotionrefineJob()
    initialiseCtfrefineJob()
    initialiseExternalJob()

