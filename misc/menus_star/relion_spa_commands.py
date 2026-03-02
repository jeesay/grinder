import os
import relion_h as rh
# import relion_option as ro
import relion_command as rc

#############
joboptions = {}
is_continue = False

def initialisePipeline(outputname,job_counter):
    job_counter += 1
    outputname = ""
    

def clear(labelnew):
    _script = rc.Script()
    _cli = _script.new_command()
    _cli.id = labelnew
    return (_script,_cli)
  
def exists(v):
    return True

def get_str(v):
    return v

def get_bool(v):
    return v

def getHealPixOrder(s):
    for i in range(10):
        if s == job_sampling_options[i]:
            return i + 1
    return -1

def getCtfFitString(s):
    if s == job_ctffit_options[0]:
        return "f"
    elif s == job_ctffit_options[1]:
        return "m"
    elif s == job_ctffit_options[2]:
        return "p"
    else:
        return ""

def getTomoInputCommmand(*args):
    return ""

def integerToString(v):
    return v

def floatToString(v):
    return v

########################################################################################################
# 
########################################################################################################

def getCommandsImportJobRaw(outputname, label, job_counter=-1):
    script, cli = clear(label)
    cli.add_prog(rc.Prog("relion_import"))
    
    fn_out = ""
    fn_in = ""

    do_raw = get_bool("do_raw")
    do_other = get_bool("do_other")


    # USELESS ERROR
    # if do_raw and do_other:
    #     error_message = "ERROR: you cannot import BOTH raw movies/micrographs AND other node types at the same time..."
    #     return "", "", error_message
    
    # if not do_raw and not do_other:
    #     error_message = "ERROR: nothing to do... "
    #     return "", "", error_message

    # if do_raw:
    fn_in = get_str("fn_in_raw")
    
    # USELESS - The web server forbids outside public/project folder
    # if "../" in fn_in:
    #         error_message = "ERROR: don't import files outside the project directory.\\nPlease make a symbolic link by an absolute path before importing."
    #         return "", "", error_message
    
    # if fn_in.startswith("/"):
    #         error_message = "ERROR: please import files by a relative path.\\nIf you want to import files outside the project directory, make a symbolic link by an absolute path and\\nimport the symbolic link by a relative path."
    #         return "", "", error_message


    fn_out = "movies.star"
    nod = rc.Node(outputname + fn_out, rh.LABEL_IMPORT_MOVIES)
    new_arg = rc.Flag("--do_movies","","is_multiframe", True )
    new_arg.add_outnode(nod)
    cli.args.append(new_arg)

    fn_out = "micrographs.star"
    nod = rc.Node(outputname + fn_out, rh.LABEL_IMPORT_MICS)
    new_arg = rc.Flag("--do_micrographs","","is_multiframe",  False)
    new_arg.add_outnode(nod)
    cli.args.append(new_arg)

#    USELESS
#    optics_group = get_str("optics_group_name")
#    if not optics_group:
#        error_message = "ERROR: please specify an optics group name."
#        return "", "", error_message
    
    new_arg = rc.Param("--optics_group_name", "optics_group_name", assertion="required")
    cli.args.append(new_arg)
        
    fn_mtf = get_str("fn_mtf")
    # if len(fn_mtf) > 0:
    new_arg = rc.Flag("--optics_group_mtf","","ne,{fn_mtf},null",True)
    cli.args.append(new_arg) 

    new_arg = rc.Param("--angpix","angpix")
    cli.args.append(new_arg) 
    new_arg = rc.Param("--kV","kV")
    cli.args.append(new_arg) 
    new_arg = rc.Param("--Cs", "Cs")
    cli.args.append(new_arg) 
    new_arg = rc.Param("--Q0", "Q0")
    cli.args.append(new_arg) 
    new_arg = rc.Param("--beamtilt_x","beamtilt_x")
    cli.args.append(new_arg) 
    new_arg = rc.Param("--beamtilt_y","beamtilt_y")
    cli.args.append(new_arg) 

    # Now finish the command call to relion_import program, which does the actual copying
    new_arg = rc.Param(" --i","fn_in")
    cli.args.append(new_arg) 
    new_arg = rc.Param(f" --odir {outputname}{{counter}}", "")
    cli.args.append(new_arg) 
    new_arg = rc.Param(" --ofile ","fn_out")
    cli.args.append(new_arg) 
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.args.append(new_arg) 


    # if (is_continue)
	# 	command += " --continue ";
    return script

    
def getCommandsImportJobParticles(outputname, label, job_counter=-1):
    
    script, cli = clear(label)
    cli.add_prog(rc.Prog("relion_import"))
    fn_out = ""
    fn_in = ""

    do_raw = get_bool("do_raw")
    do_other = get_bool("do_other")

    # USELESS ERROR
    # if do_raw and do_other:
    #     error_message = "ERROR: you cannot import BOTH raw movies/micrographs AND other node types at the same time..."
    #     return "", "", error_message
    #
    # if not do_raw and not do_other:
    #     error_message = "ERROR: nothing to do... "
    #     return "", "", error_message


    # if do_other:
    fn_in = get_str("fn_in_other")
    node_type = get_str("node_type")
    
    # if node_type == "Particle coordinates (*.box, *_pick.star)":
    suffix = fn_in.split('*')[-1] if '*' in fn_in else fn_in
    fn_out = "coords_suffix" + suffix
    cli.add_outnode(rc.Node(outputname + fn_out, rh.LABEL_IMPORT_COORDS))
    new_arg = rc.Param("--do_coordinates ","")

    # else:
    #     fn_out = os.path.basename(fn_in)
        
    #     mynodetype = ""
    #     if node_type == "Particles STAR file (.star)":
    #         mynodetype = rh.LABEL_IMPORT_PARTS
    #     elif node_type == "Multiple (2D or 3D) references (.star or .mrcs)":
    #         mynodetype = rh.LABEL_IMPORT_2DIMG
    #     elif node_type == "3D reference (.mrc)":
    #         mynodetype = rh.LABEL_IMPORT_MAP
    #     elif node_type == "3D mask (.mrc)":
    #         mynodetype = rh.LABEL_IMPORT_MASK
    #     elif node_type == "Micrographs STAR file (.star)":
    #         mynodetype = rh.LABEL_IMPORT_MICS
    #     elif node_type == "Unfiltered half-map (unfil.mrc)":
    #         mynodetype = rh.LABEL_IMPORT_HALFMAP
    #     else:
    #         error_message = "Unrecognized menu option for node_type = " + node_type
    #         return "", "", error_message
        
    #     cli.add_outnode(rc.Node(outputname + fn_out, mynodetype))
        
    # if mynodetype == rh.LABEL_HALFMAP_CPIPE or mynodetype == rh.LABEL_IMPORT_HALFMAP:
    #     fn_inb = os.path.basename(fn_in)
    #     if "half1" in fn_inb:
    #         fn_inb = fn_inb.replace("half1", "half2")
    #     elif "half2" in fn_inb:
    #         fn_inb = fn_inb.replace("half2", "half1")
        
    #     cli.add_outnode(rc.Node(outputname + fn_inb, mynodetype))
    #     new_arg = rc.Param("--do_halfmaps","")
    
    # elif mynodetype == rh.LABEL_PARTS_CPIPE or mynodetype == rh.LABEL_IMPORT_PARTS:
    new_arg = rc.Param("--do_particles","")
    optics_group = get_str("optics_group_particles")
    new_arg = rc.Param("--optics_group_name ","optics_group_particles")
                
    return script

def getCommandsImportJobOther(outputname, label, job_counter=-1):
    
    script, cli = clear(label)
    cli.add_prog(rc.Prog("relion_import"))
    fn_out = ""
    fn_in = ""

    do_raw = get_bool("do_raw")
    do_other = get_bool("do_other")

    # USELESS ERROR
    # if do_raw and do_other:
    #     error_message = "ERROR: you cannot import BOTH raw movies/micrographs AND other node types at the same time..."
    #     return "", "", error_message
    #
    # if not do_raw and not do_other:
    #     error_message = "ERROR: nothing to do... "
    #     return "", "", error_message


    # if do_other:
    fn_in = get_str("fn_in_other")
    node_type = get_str("node_type")
    
    if node_type == "Particle coordinates (*.box, *_pick.star)":
        suffix = fn_in.split('*')[-1] if '*' in fn_in else fn_in
        fn_out = "coords_suffix" + suffix
        cli.add_outnode(rc.Node(outputname + fn_out, rh.LABEL_IMPORT_COORDS))
        new_arg = rc.Param("--do_coordinates ","")
    else:
        fn_out = os.path.basename(fn_in)
        
        mynodetype = ""
        if node_type == "Particles STAR file (.star)":
            mynodetype = rh.LABEL_IMPORT_PARTS
        elif node_type == "Multiple (2D or 3D) references (.star or .mrcs)":
            mynodetype = rh.LABEL_IMPORT_2DIMG
        elif node_type == "3D reference (.mrc)":
            mynodetype = rh.LABEL_IMPORT_MAP
        elif node_type == "3D mask (.mrc)":
            mynodetype = rh.LABEL_IMPORT_MASK
        elif node_type == "Micrographs STAR file (.star)":
            mynodetype = rh.LABEL_IMPORT_MICS
        elif node_type == "Unfiltered half-map (unfil.mrc)":
            mynodetype = rh.LABEL_IMPORT_HALFMAP
        else:
            error_message = "Unrecognized menu option for node_type = " + node_type
            return "", "", error_message
        
        cli.add_outnode(rc.Node(outputname + fn_out, mynodetype))
        
    if mynodetype == rh.LABEL_HALFMAP_CPIPE or mynodetype == rh.LABEL_IMPORT_HALFMAP:
        fn_inb = os.path.basename(fn_in)
        if "half1" in fn_inb:
            fn_inb = fn_inb.replace("half1", "half2")
        elif "half2" in fn_inb:
            fn_inb = fn_inb.replace("half2", "half1")
        
        cli.add_outnode(rc.Node(outputname + fn_inb, mynodetype))
        new_arg = rc.Param("--do_halfmaps","")
    
    elif mynodetype == rh.LABEL_PARTS_CPIPE or mynodetype == rh.LABEL_IMPORT_PARTS:
            new_arg = rc.Param("--do_particles","")
            optics_group = get_str("optics_group_particles")
            new_arg = rc.Param("--optics_group_name ","optics_group_particles")
                
    
    return script


def getCommandsMotioncorrJob(outputname,label,job_counter=-1):

    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)

    cli.add_prog(rc.Prog("`which relion_run_motioncorr_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_run_motioncorr`","use_mpi",False))

    #  I/O
#    if joboptions["input_star_mics"] == ""):
#        error_message = "ERROR: empty field for input STAR file..."
#        return False
    new_arg = rc.Param("--i ", "input_star_mics",assertion="required")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["input_star_mics"].getString(), joboptions["input_star_mics"].node_type)
    cli.add_innode(node)

    new_arg = rc.Param("--o ",outputname)
    cli.args.append(new_arg)

    node2 = rc.Node (outputname + "corrected_micrographs.star", rh.LABEL_MOCORR_MICS)
    cli.add_outnode(node2)
    node4 = rc.Node(outputname + "logfile.pdf", rh.LABEL_MOCORR_LOG)
    cli.add_outnode(node4)

    new_arg = rc.Param("--first_frame_sum ", "first_frame_sum")
    cli.args.append(new_arg)
    new_arg = rc.Param("--last_frame_sum ", "last_frame_sum")
    cli.args.append(new_arg)

#   if joboptions["do_own_motioncor"].getBoolean():
    new_arg = rc.Flag("--use_own "," ","do_own_motioncor",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--j ", "nr_threads")
    cli.args.append(new_arg)
#   if joboptions["do_float16"].getBoolean())
    if not joboptions["do_save_ps"].getBoolean():
        error_message = "When writing to float16, you have to write power spectra for CTFFIND-4.1."
        return False
        
    new_arg = rc.Param("--float16","")
    cli.args.append(new_arg)
    
#   if (joboptions["fn_defect"].length() > 0)
    new_arg = rc.Param("--defect_file ", "fn_defect",assertion="required")
    cli.args.append(new_arg)

    new_arg = rc.Param("--bin_factor ", "bin_factor")
    cli.args.append(new_arg)
    new_arg = rc.Param("--bfactor ", "bfactor")
    cli.args.append(new_arg)
    new_arg = rc.Param("--dose_per_frame ", "dose_per_frame")
    cli.args.append(new_arg)
    new_arg = rc.Param("--preexposure ", "pre_exposure")
    cli.args.append(new_arg)
    new_arg = rc.Param("--patch_x ", "patch_x")
    cli.args.append(new_arg)
    new_arg = rc.Param("--patch_y ", "patch_y")
    cli.args.append(new_arg)
    new_arg = rc.Param("--eer_grouping ", "eer_grouping")
    cli.args.append(new_arg)

#   if joboptions["group_frames"].getNumber(error_message) > 1.)
    new_arg = rc.Param("--group_frames ", "group_frames",assertion="is_positive")
    cli.args.append(new_arg)

#    if (joboptions["fn_gain_ref"].length() > 0)
#        int gain_rot = -1, gain_flip = -1
#        for (int i = 0 i <= 3 i += 1)
#            if strcmp((joboptions["gain_rot"].c_str(), job_gain_rotation_options[i].c_str()) == 0)
#                gain_rot = i
#                break
#                    
#        for (int i = 0 i <= 2 i += 1)
#            if strcmp((joboptions["gain_flip"]flip_options[i].c_str()) == 0)
#                gain_flip = i
#                break
#                    
#        if gain_rot == -1 or gain_flip == -1)
#            REPORT_ERROR("Illegal gain_rot and/or gain_flip.")

    new_arg = rc.Param("--gainref ", "fn_gain_ref")
    cli.args.append(new_arg)
    new_arg = rc.Param("--gain_rot ","gain_rot",assertion="is_positive")
    cli.args.append(new_arg)
    new_arg = rc.Param("--gain_flip ","gain_flip",assertion="is_positive")
    cli.args.append(new_arg)
    
#    if !is_tomo and joboptions["do_dose_weighting"].getBoolean())
    new_arg = rc.Flag("--dose_weighting ","do_dose_weighting",True)
#   if joboptions["do_save_noDW"].getBoolean())
    new_arg = rc.Flag("--save_noDW ","do_save_noDW",True)
            
#   if joboptions["do_save_ps"].getBoolean())
#        if not joboptions["do_own_motioncor"].getBoolean())
#              error_message = "'Save sum of power spectra' is not available with UCSF MotionCor2."
#        return False
        
        
    # Calculation must be done in a wrapper to RELION_MOTIONCOR
    # dose_for_ps = joboptions["group_for_ps"].getNumber(error_message)
    # if error_message != "":
    #     return False

    # float dose_rate = 1.0
    # if (!is_tomo)
    #         dose_rate = joboptions["dose_per_frame"].getNumber(error_message)
    #         if error_message != "":
    #             return False
    # if (dose_rate <= 0)
    #             error_message = "Please specify the dose rate to calculate the grouping for power spectra."
    #     return False
    #         if dose_for_ps <= 0)
    #             error_message = "Invalid dose for the grouping for power spectra."
    #     return False
    
    # int grouping_for_ps = ROUND(dose_for_ps / dose_rate)
    # if grouping_for_ps == 0)
    #     grouping_for_ps = 1

    # new_arg = rc.Param("--grouping_for_ps ","grouping_for_ps")

#    if (is_continue)
    new_arg = rc.Flag("--only_do_unfinished ","is_continue", True)

    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return script
    
def getCommandsMotioncorrJob_MC2(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)

    
    rc.Prog("`which relion_run_motioncorr_mpi`","use_mpi",True)
    rc.Prog("`which relion_run_motioncorr`","use_mpi",False)

    #  I/O
#    if joboptions["input_star_mics"] == ""):
#        error_message = "ERROR: empty field for input STAR file..."
#        return False
    new_arg = rc.Param("--i ", "input_star_mics",assertion="required")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["input_star_mics"].getString(), joboptions["input_star_mics"].node_type)
    cli.add_innode(node)

    new_arg = rc.Param("--o ",outputname)
    cli.args.append(new_arg)

    node2 = rc.Node(outputname + "corrected_micrographs.star", rh.LABEL_MOCORR_MICS)
    cli.add_outnode(node2)
    node4 = rc.Node(outputname + "logfile.pdf", rh.LABEL_MOCORR_LOG)
    cli.add_outnode(node4)

    new_arg = rc.Param("--first_frame_sum ", "first_frame_sum")
    cli.args.append(new_arg)
    new_arg = rc.Param("--last_frame_sum ", "last_frame_sum")
    cli.args.append(new_arg)

    # MotionCor2
    cli.label(".motioncor2","do_own_motioncor",False)

    new_arg = rc.Param("--use_motioncor2 ","do_own_motioncor",False)
    cli.args.append(new_arg)
    new_arg = rc.Param("--motioncor2_exe ", "fn_motioncor2_exe")
    cli.args.append(new_arg)

#   USELESS
#   if joboptions["do_float16"].getBoolean())
#       error_message = "ERROR: MotionCor2 cannot write float16 files."
#       return False
        
#    if (joboptions["other_motioncor2_args").length() > 0)
    new_arg = rc.Param("--other_motioncor2_args ", "other_motioncor2_args",assertion="required")
    cli.args.append(new_arg)

    #  Which GPUs to use?
    new_arg = rc.Param("--gpu", "gpu_ids")
    cli.args.append(new_arg)
    
#   if (joboptions["fn_defect"].length() > 0)
    new_arg = rc.Param("--defect_file ", "fn_defect",assertion="is_positive")
    cli.args.append(new_arg)

    new_arg = rc.Param("--bin_factor ", "bin_factor")
    cli.args.append(new_arg)
    new_arg = rc.Param("--bfactor ", "bfactor")
    cli.args.append(new_arg)
    new_arg = rc.Param("--dose_per_frame ", "dose_per_frame")
    cli.args.append(new_arg)
    new_arg = rc.Param("--preexposure ", "pre_exposure")
    cli.args.append(new_arg)
    new_arg = rc.Param("--patch_x ", "patch_x")
    cli.args.append(new_arg)
    new_arg = rc.Param("--patch_y ", "patch_y")
    cli.args.append(new_arg)
    new_arg = rc.Param("--eer_grouping ", "eer_grouping")
    cli.args.append(new_arg)

#   if joboptions["group_frames"].getNumber(error_message) > 1.)
    new_arg = rc.Param("--group_frames ", "group_frames",assertion="is_positive")
    cli.args.append(new_arg)

#    if (joboptions["fn_gain_ref"].length() > 0)
#        int gain_rot = -1, gain_flip = -1
#        for (int i = 0 i <= 3 i += 1)
#            if strcmp((joboptions["gain_rot"].c_str(), job_gain_rotation_options[i].c_str()) == 0)
#                gain_rot = i
#                break
#                    
#        for (int i = 0 i <= 2 i += 1)
#            if strcmp((joboptions["gain_flip"]flip_options[i].c_str()) == 0)
#                gain_flip = i
#                break
#                    
#        if gain_rot == -1 or gain_flip == -1)
#            REPORT_ERROR("Illegal gain_rot and/or gain_flip.")

    new_arg = rc.Param("--gainref ", "fn_gain_ref")
    cli.args.append(new_arg)
    new_arg = rc.Param("--gain_rot ","gain_rot",assertion="is_positive")
    cli.args.append(new_arg)
    new_arg = rc.Param("--gain_flip ","gain_flip",assertion="is_positive")
    cli.args.append(new_arg)
    
#    if !is_tomo and joboptions["do_dose_weighting"].getBoolean())
    new_arg = rc.Flag("--dose_weighting ","do_dose_weighting",True)
#   if joboptions["do_save_noDW"].getBoolean())
    new_arg = rc.Flag("--save_noDW ","do_save_noDW",True)
            
#   if joboptions["do_save_ps"].getBoolean())
#        if not joboptions["do_own_motioncor"].getBoolean())
#              error_message = "'Save sum of power spectra' is not available with UCSF MotionCor2."
#        return False
        
        
# Calculation must be done in a wrapper to RELION_MOTIONCOR
#         dose_for_ps = joboptions["group_for_ps"].getNumber(error_message)
#         if error_message != "":
#             return False

#         float dose_rate = 1.0
#         if not is_tomo:
#                 dose_rate = joboptions["dose_per_frame"].getNumber(error_message)
#                 if error_message != "":
#                     return False
#         if dose_rate <= 0:
#                     error_message = "Please specify the dose rate to calculate the grouping for power spectra."
#             return False
#                 if dose_for_ps <= 0:
#                     error_message = "Invalid dose for the grouping for power spectra."
#             return False
        
#         int grouping_for_ps = ROUND(dose_for_ps / dose_rate)
#         if grouping_for_ps == 0:
#             grouping_for_ps = 1

#         new_arg = rc.Param("--grouping_for_ps ","grouping_for_ps")
#

#    if (is_continue)
    new_arg = rc.Flag("--only_do_unfinished ","is_continue", True)

    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    return script
    

def getCommandsCtffindJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    outputName = outputname
    # if is_tomo:
    #         rc.Node node(outputname + "tilt_series_ctf.star", rh.LABEL_CTFFIND_TOMOGRAMS)
    #     cli.add_outnode(node)
    #     else
    node = rc.Node(outputname + "micrographs_ctf.star", rh.LABEL_CTFFIND_MICS)
    cli.add_outnode(node)
    
    #  PDF with histograms of the eigenvalues
    node3 = rc.Node(outputname + "logfile.pdf", rh.LABEL_CTFFIND_LOG)
    cli.add_outnode(node3)

    rc.Prog("`which relion_run_ctffind_mpi`","use_mpi",True)
    rc.Prog("`which relion_run_ctffind`","use_mpi",False)

    #  I/O
#    if joboptions["input_star_mics"] == "")
#            error_message = "ERROR: empty field for input STAR file..."
#        return False
    new_arg = rc.Param("--i ", "input_star_mics",assertion="required")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["input_star_mics"].getString(), joboptions["input_star_mics"].node_type)
    cli.add_innode(node)

    new_arg = rc.Param("--o ",outputname)
    cli.args.append(new_arg)
    new_arg = rc.Param("--Box ", "box")
    cli.args.append(new_arg)
    new_arg = rc.Param("--ResMin ", "resmin")
    cli.args.append(new_arg)
    new_arg = rc.Param("--ResMax ", "resmax")
    cli.args.append(new_arg)
    new_arg = rc.Param("--dFMin ", "dfmin")
    cli.args.append(new_arg)
    new_arg = rc.Param("--dFMax ", "dfmax")
    cli.args.append(new_arg)
    new_arg = rc.Param("--FStep ", "dfstep")
    cli.args.append(new_arg)
    new_arg = rc.Param("--dAst ", "dast")
    cli.args.append(new_arg)

#   if joboptions["use_noDW"].getBoolean():
    new_arg = rc.Flag("--use_noDW ","use_noDW",True)

#   if joboptions["do_phaseshift"].getBoolean())
    new_arg = rc.Flag("--do_phaseshift ","do_phaseshift",True)
    new_arg = rc.Flag("--phase_min ", "phase_min","do_phaseshift",True)
    cli.args.append(new_arg)
    new_arg = rc.Flag("--phase_max ", "phase_max","do_phaseshift",True)
    cli.args.append(new_arg)
    new_arg = rc.Flag("--phase_step ", "phase_step","do_phaseshift",True)
    cli.args.append(new_arg)
    
    label += ".ctffind4"

    new_arg = rc.Param("--ctffind_exe ", "fn_ctffind_exe")
    cli.args.append(new_arg)
    new_arg = rc.Param("--ctfWin ", "ctf_win")
    cli.args.append(new_arg)
    new_arg = rc.Param("--is_ctffind4 ","")
#   if not joboptions["slow_search"].getBoolean())
    new_arg = rc.Flag("--fast_search ","slow_search",True)
#   if joboptions["use_given_ps"].getBoolean())
    new_arg = rc.Param("--use_given_ps ","use_given_ps",True)

    new_arg = rc.Param("--only_do_unfinished ","is_continue",True)

    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    return script

def getCommandsManualpickJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    cli.add_prog(rc.Prog("`which relion_manualpick`"))

#    if joboptions["fn_in"] == "")
#            error_message = "ERROR: empty field for input STAR file..."
#        return False
    
    new_arg = rc.Param("--i ", "fn_in",assertion="required")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["fn_in"].getString(), joboptions["fn_in"].node_type)
    cli.add_innode(node)

    new_arg = rc.Param("--odir ", outputname)
    new_arg = rc.Param("--pickname manualpick","")

    #  Allow saving, and always save default selection file upon launching the program
    fn_outstar = outputname + "micrographs_selected.star"
    node3 = rc.Node(fn_outstar, rh.LABEL_MANPICK_MICS)
    cli.add_outnode(node3)
    new_arg = rc.Param("--allow_save --fast_save --selection ", fn_outstar)

    new_arg = rc.Param("--scale ", "micscale")
    cli.args.append(new_arg)
    new_arg = rc.Param("--sigma_contrast ", "sigma_contrast")
    cli.args.append(new_arg)
    new_arg = rc.Param("--black ", "black_val")
    cli.args.append(new_arg)
    new_arg = rc.Param("--white ", "white_val")
    cli.args.append(new_arg)

#   if joboptions["do_topaz_denoise"].getBoolean())
    new_arg = rc.Flag("--topaz_denoise","do_topaz_denoise",True)
#   if joboptions["lowpass"].getNumber(error_message) > 0.)
    new_arg = rc.Param("--lowpass ", "lowpass",assertion="is_positive")
    cli.args.append(new_arg)
#   if joboptions["highpass"].getNumber(error_message) > 0.)
    new_arg = rc.Param("--highpass ", "highpass", assertion="is_positive")
    cli.args.append(new_arg)
#   if joboptions["angpix"].getNumber(error_message) > 0.)
    new_arg = rc.Param("--angpix ", "angpix", assertion="is_positive")
    cli.args.append(new_arg)

#   if joboptions["do_fom_threshold"].getBoolean())
    new_arg = rc.Flag("--minimum_pick_fom ", "minimum_pick_fom","do_fom_threshold",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--particle_diameter ", "diameter")
    cli.args.append(new_arg)

#    if joboptions["do_startend"].getBoolean())
#            label += ".helical"

#        new_arg = rc.Param("--pick_start_end ","do_startend",True)

#        #  new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
#        rc.Node node2(outputname + "manualpick.star", rh.LABEL_MANPICK_COORDS_HELIX)
#        cli.add_outnode(node2)
#    
#    else
        #  new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
    node2 = rc.Node(outputname + "manualpick.star", rh.LABEL_MANPICK_COORDS)
    cli.add_outnode(node2)
    
#    if joboptions["do_color"].getBoolean())
    new_arg = rc.Param("--color_label ", "color_label","do_color",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--blue ", "blue_value")
    cli.args.append(new_arg)
    new_arg = rc.Param("--red ", "red_value")
    cli.args.append(new_arg)
#   if joboptions["fn_color"].length() > 0)
    new_arg = rc.Param("--color_star ", "","fn_color",True)
    cli.args.append(new_arg)
    
    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return script

def getCommandsAutopickContinueJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)

    if is_continue and joboptions["continue_manual"].getBoolean(): 
        label += ".continuemanual"

        cli.prog(rc.Prog("`which relion_manualpick`"))

        new_arg = rc.Param("--i ", "fn_input_autopick")
        cli.args.append(new_arg)
        new_arg = rc.Param("--odir ",outputname)
        cli.args.append(new_arg)
        new_arg = rc.Param("--pickname autopick","")
        cli.args.append(new_arg)

        node = rc.Node(joboptions["fn_input_autopick"].getString(), joboptions["fn_input_autopick"].node_type)
        cli.add_innode(node)

        #  Output new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
        node2 = rc.Node (outputname + "autopick.star", rh.LABEL_AUTOPICK_COORDS)
        cli.add_outnode(node2)

        #  The output micrographs selection
        fn_outstar = outputname + "micrographs_selected.star"
        node3 = rc.Node(fn_outstar, rh.LABEL_AUTOPICK_MICS)
        cli.add_outnode(node3)
        new_arg = rc.Param("--allow_save  --selection ",fn_outstar)

        #  A manualpicker jobwindow for display of micrographs....
        fn_job = ".gui_manualpick"
        if exists(fn_job + "job.star") or exists(fn_job + "run.job"):
            # RelionJob manualpickjob
            iscont = False
            manualpickjob.read(fn_job.c_str(), iscont, True) #  true means do initialise

            new_arg = rc.Param("--scale ",manualpickjob.joboptions["micscale"])
            cli.args.append(new_arg)
            new_arg = rc.Param("--sigma_contrast " + manualpickjob.joboptions["sigma_contrast"])
            cli.args.append(new_arg)
            new_arg = rc.Param("--black " + manualpickjob.joboptions["black_val"])
            cli.args.append(new_arg)
            new_arg = rc.Param("--white " + manualpickjob.joboptions["white_val"])
            cli.args.append(new_arg)

            if manualpickjob.joboptions["do_startend"].getBoolean():
                new_arg = rc.Param("--pick_start_end ","")
                if manualpickjob.joboptions["do_topaz_denoise"].getBoolean():
                    new_arg = rc.Param("--topaz_denoise ","")
                else:
                    error_message = ""
                mylowpass = manualpickjob.joboptions["lowpass"].getNumber(error_message)
                if mylowpass > 0.:
                    new_arg = rc.Param("--lowpass ", manualpickjob.joboptions["lowpass"])
                    cli.args.append(new_arg)

                myhighpass = manualpickjob.joboptions["highpass"].getNumber(error_message)
                if myhighpass > 0.:
                    new_arg = rc.Param("--highpass " + manualpickjob.joboptions["highpass"])
                    cli.args.append(new_arg)

                myangpix = manualpickjob.joboptions["angpix"].getNumber(error_message)
                if myangpix > 0.:
                    new_arg = rc.Param("--angpix " + manualpickjob.joboptions["angpix"])
                    cli.args.append(new_arg)
            
            new_arg = rc.Param("--particle_diameter ", manualpickjob.joboptions["diameter"])
            cli.args.append(new_arg)
            if manualpickjob.joboptions["do_fom_threshold"].getBoolean():
                new_arg = rc.Param("--minimum_pick_fom ",manualpickjob.joboptions["minimum_pick_fom"])
                cli.args.append(new_arg)
            
            if manualpickjob.joboptions["do_color"].getBoolean():
                new_arg = rc.Param("--color_label ", manualpickjob.joboptions["color_label"])
                cli.args.append(new_arg)
                new_arg = rc.Param("--blue ", manualpickjob.joboptions["blue_value"])
                cli.args.append(new_arg)
                new_arg = rc.Param("--red ", manualpickjob.joboptions["red_value"])
                cli.args.append(new_arg)
                if manualpickjob.joboptions["fn_color"].length() > 0:
                    new_arg = rc.Param("--color_star ", manualpickjob.joboptions["fn_color"])
                    cli.args.append(new_arg)
                else:
                    #  Just use some defaults if no .gui_manualpickjob.star exists
                    new_arg = rc.Param("--scale","0.25")
                    new_arg = rc.Param("--sigma_contrast", "3")
                    new_arg = rc.Param("--lowpass","20")
                    new_arg = rc.Param("--particle_diameter","100")

    return script
        
def getCommandsAutopickTopazTrainJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)

    #  Run autopicking
    if joboptions["nr_mpi"].getNumber(error_message) > 1:
        command="`which relion_autopick_mpi`"
    else:
        command="`which relion_autopick`"
    if error_message != "":
        return False

    # #  Input
    # icheck = 0
    # if joboptions["do_log"].getBoolean():
    #     icheck += 1
    # if joboptions["do_topaz"].getBoolean(): 
    #     icheck += 1
    # if joboptions["do_refs"].getBoolean():
    #     icheck +=1

    # if  icheck != 1:
    #     error_message = "ERROR: On the I/O tab specify (only) one of three methods: template-matching, LoG or topaz ..."
    #     return False
    
    if joboptions["fn_input_autopick"] == "" :
        error_message = "ERROR: empty field for input STAR file..."
        return False
    
    new_arg = rc.Param("--fn_topaz_exe ", "fn_topaz_exe")
    cli.args.append(new_arg)
    new_arg = rc.Param("--i ", "fn_input_autopick")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["fn_input_autopick"].getString(), joboptions["fn_input_autopick"].node_type)
    cli.add_innode(node)

    if not (joboptions["do_topaz"].getBoolean() and joboptions["do_topaz_train"].getBoolean()):
    
        #  Output new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
        node3 = rc.Node(outputname + "autopick.star", rh.LABEL_AUTOPICK_COORDS)
        cli.add_outnode(node3)

        #  PDF with histograms of the eigenvalues
        node3b = rc.Node(outputname + "logfile.pdf", rh.LABEL_AUTOPICK_LOG)
        cli.add_outnode(node3b)
    
    new_arg = rc.Param("--odir ", outputname)
    new_arg = rc.Param("--pickname", "autopick")

    if joboptions["do_topaz"].getBoolean():
    
        label += ".topaz"

        # icheck = 0
        # if joboptions["do_topaz_train"].getBoolean():
        #         icheck += 1
        # if joboptions["do_topaz_pick"].getBoolean(): 
        #         icheck += 1
        # if  icheck != 1:
        #     error_message = "ERROR: On the Topaz tab specify (only) one of two methods: training or picking..."
        #     return False
        
        # if joboptions["topaz_particle_diameter"].getNumber(error_message) > 0.:
        new_arg = rc.Param("--particle_diameter ", "topaz_particle_diameter",assertion="is_positive")
        cli.args.append(new_arg)
        if error_message != "": 
            return False

        if joboptions["do_topaz_train"].getBoolean():
        
            label += ".train"

            if not joboptions["use_gpu"].getBoolean():
                error_message ="ERROR: For Topaz training, specify which GPUs to use on the autopicking tab for Topaz picking GPU usage is optional"
                return False
            
            new_arg = rc.Flag("--topaz_train","","do_topaz_train",True)

            if joboptions["topaz_nr_particles"].getNumber(error_message) > 0.:
                new_arg = rc.Param("--topaz_nr_particles ", "topaz_nr_particles")
                cli.args.append(new_arg)

            if error_message != "": 
                return False

            if joboptions["do_topaz_train_parts"].getBoolean():
                new_arg = rc.Flag("--topaz_train_parts ", "topaz_train_parts","do_topaz_train_parts",True)
                cli.args.append(new_arg)
                #  Output new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
                nodet = rc.Node(outputname + "input_training_coords.star", rh.LABEL_COORDS_CPIPE)
                cli.add_outnode(nodet)

            else:
                new_arg = rc.Param("--topaz_train_picks ", "topaz_train_picks")
                cli.args.append(new_arg)
    return script

def getCommandsAutopickTopazPickJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)

    # elif joboptions["do_topaz_pick"].getBoolean():
    #     label += ".pick"

    new_arg = rc.Param("--topaz_extract","")
    # if joboptions["topaz_model"] != "":
    new_arg = rc.Param("--topaz_model ", "topaz_model",assertion="required")
    cli.args.append(new_arg)

    if joboptions["do_topaz_filaments"].getBoolean():
        new_arg = rc.Param("--helix ","")
        cli.args.append(new_arg)
        new_arg = rc.Param("--topaz_threshold ", "topaz_filament_threshold")
        cli.args.append(new_arg)
        # if joboptions["topaz_hough_length"].getNumber(error_message) > 0.:
        new_arg = rc.Param("--helical_tube_length_min ", "topaz_hough_length",assertion="is_positive")
        cli.args.append(new_arg)
    
    
    # if joboptions["topaz_other_args"].length() > 0:
    new_arg = rc.Param("--topaz_args ", "topaz_other_args",assertion="required")
    cli.args.append(new_arg)

    #  GPU-stuff
    # if joboptions["use_gpu"].getBoolean():
    new_arg = rc.Flag("--gpu", "gpu_ids","use_gpu",True)
    cli.args.append(new_arg)
            
    return script

def getCommandsAutopickLoGJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)

    # USELESS
    # if joboptions["do_log"].getBoolean():
    #     if joboptions["use_gpu"].getBoolean():
    #             error_message ="ERROR: The Laplacian-of-Gaussian picker does not support GPU."
    # return False
    
    label += ".log"

    new_arg = rc.Param("--LoG ","")
    new_arg = rc.Param("--LoG_diam_min ", "log_diam_min")
    cli.args.append(new_arg)
    new_arg = rc.Param("--LoG_diam_max ", "log_diam_max")
    cli.args.append(new_arg)
    new_arg = rc.Param("--shrink 0 --lowpass ", "log_maxres")
    cli.args.append(new_arg)
    new_arg = rc.Param("--LoG_adjust_threshold ", "log_adjust_thr")
    cli.args.append(new_arg)
    if joboptions["log_upper_thr"].getNumber(error_message) < 999.:
        new_arg = rc.Param("--LoG_upper_threshold ", "log_upper_thr")
    cli.args.append(new_arg)
    if error_message != "": 
        return False

    # if joboptions["log_invert"].getBoolean():
        new_arg = rc.Flag("--Log_invert ","","log_invert",True)
        cli.args.append(new_arg)
    elif joboptions["do_refs"].getBoolean():
            if joboptions["do_ref3d"].getBoolean():
                if joboptions["fn_ref3d_autopick"] == "":
                    error_message ="ERROR: empty field for 3D reference..."
                    return False
    return script

def getCommandsAutopickRef3DJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)

    label += ".ref3d"

    new_arg = rc.Param("--ref ", "fn_ref3d_autopick")
    cli.args.append(new_arg)
    node2 = rc.Node(joboptions["fn_ref3d_autopick"].getString(), rh.LABEL_MAP_CPIPE)
    cli.add_innode(node2)
    new_arg = rc.Param("--sym ", "ref3d_symmetry")
    cli.args.append(new_arg)

    #  Sampling
    ref3d_sampling = rho.getHealPixOrder(joboptions["ref3d_sampling"])
    cli.args.append(new_arg)
    if ref3d_sampling <= 0:
        error_message = "Wrong choice for ref3d_sampling"
        return False
                
        new_arg = rc.Param("--healpix_order ", "ref3d_sampling")
    else:
        if joboptions["fn_refs_autopick"] == "":
            error_message ="ERROR: empty field for references..."
            return False
    return script
                
def getCommandsAutopickRef2DJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)

    label += ".ref2d"

    new_arg = rc.Param("--ref ", "fn_refs_autopick")
    cli.args.append(new_arg)
    node2 = rc.Node(joboptions["fn_refs_autopick"].getString(), rh.LABEL_2DIMGS_CPIPE)
    cli.add_innode(node2)
            
    if joboptions["do_invert_refs"].getBoolean():
        new_arg = rc.Param("--invert ","")

        if joboptions["do_ctf_autopick"].getBoolean():
            new_arg = rc.Param("--ctf ","")
            cli.args.append(new_arg)
            if joboptions["do_ignore_first_ctfpeak_autopick"].getBoolean():
                new_arg = rc.Param("--ctf_intact_first_peak ","")
                cli.args.append(new_arg)
                new_arg = rc.Param("--ang ", "psi_sampling_autopick")
                cli.args.append(new_arg)

            new_arg = rc.Param("--shrink ", "shrink")
            cli.args.append(new_arg)
            # if joboptions["lowpass"].getNumber(error_message) > 0.:
            new_arg = rc.Flag("--lowpass ", "lowpass","is_positive",True)
            cli.args.append(new_arg)
            if error_message != "": 
                return False

            # if joboptions["highpass"].getNumber(error_message) > 0.:
            new_arg = rc.Flag("--highpass ", "highpass","is_positive",True)
            cli.args.append(new_arg)
            if error_message != "":
                return False

            # if joboptions["angpix"].getNumber(error_message) > 0.:
            new_arg = rc.Flag("--angpix ", "angpix","is_positive",True)
            cli.args.append(new_arg)
            if error_message != "": 
                return False

            # if joboptions["angpix_ref"].getNumber(error_message) > 0.:
            new_arg = rc.Flag("--angpix_ref ", "angpix_ref","is_positive",True)
            cli.args.append(new_arg)
            if error_message != "":
                return False

            new_arg = rc.Param("--threshold ", "threshold_autopick")
            cli.args.append(new_arg)
            if joboptions["do_pick_helical_segments"].getBoolean():
                new_arg = rc.Param("--min_distance ",floatToString(joboptions["helical_nr_asu"].getNumber(error_message) * joboptions["helical_rise"].getNumber(error_message))
                )
            else:
                new_arg = rc.Param("--min_distance ", "mindist_autopick")
                cli.args.append(new_arg)
            if error_message != "":
                return False

            new_arg = rc.Param("--max_stddev_noise ", "maxstddevnoise_autopick")
            cli.args.append(new_arg)
            if joboptions["minavgnoise_autopick"].getNumber(error_message) > -900.:
                new_arg = rc.Flag("--min_avg_noise ", "minavgnoise_autopick","is_less",-900.)
                cli.args.append(new_arg)
            if error_message != "": 
                return False

            #  Helix
            if joboptions["do_pick_helical_segments"].getBoolean():
                new_arg = rc.Param("--helix","")
                if joboptions["do_amyloid"].getBoolean():
                    new_arg = rc.Param("--amyloid","")
                new_arg = rc.Param("--helical_tube_outer_diameter ", "helical_tube_outer_diameter")
                cli.args.append(new_arg)
                new_arg = rc.Param("--helical_tube_kappa_max ", "helical_tube_kappa_max")
                cli.args.append(new_arg)
                new_arg = rc.Param("--helical_tube_length_min ", "helical_tube_length_min")
                cli.args.append(new_arg)
            
            #  GPU-stuff
            # if joboptions["use_gpu"].getBoolean():
            #  for the moment always use --shrink 0 with GPUs ...
            new_arg = rc.Param("--gpu", "gpu_ids","use_gpu",True)
            cli.args.append(new_arg)
            
        
        if joboptions["do_refs"].getBoolean() or joboptions["do_log"].getBoolean():
        
            #  Although mainly for debugging, LoG-picking does have write/read_fom_maps...
            # if joboptions["do_write_fom_maps"].getBoolean():
            new_arg = rc.Param("--write_fom_maps ","","do_write_fom_maps",True)

            # if joboptions["do_read_fom_maps"].getBoolean():
            new_arg = rc.Param("--read_fom_maps ","","do_read_fom_maps",True)

            if is_continue and not (joboptions["do_read_fom_maps"].getBoolean() or joboptions["do_write_fom_maps"].getBoolean()):
                new_arg = rc.Param("--only_do_unfinished ","")
            elif joboptions["do_topaz"].getBoolean():
                    if is_continue:
                        new_arg = rc.Param("--only_do_unfinished ","")
            
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return script

def getCommandsExtractJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    cli.add_prog(rc.Prog("`which relion_preprocess_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_preprocess`","use_mpi",True))

    #  Input
#    if joboptions["star_mics") == "")
#            error_message = "ERROR: empty field for input STAR file..."
#        return False
    new_arg = rc.Param("--i ", "star_mics",assertion="required")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["star_mics"].getString(), joboptions["star_mics"].node_type)
    cli.add_innode(node)

    if joboptions["do_reextract"].getBoolean():
            if joboptions["fndata_reextract"] == "":
                    error_message = "ERROR: empty field for refined particles STAR file..."
            return False
        
    if joboptions["do_reset_offsets"].getBoolean() and joboptions["do_recenter"].getBoolean():
        error_message = "ERROR: you cannot both reset refined offsets and recenter on refined coordinates, choose one..."
        return False
        
    # label += ".reextract"

    new_arg = rc.Param("--reextract_data_star ", "fndata_reextract")
    cli.args.append(new_arg)
    node2 = rc.Node(joboptions["fndata_reextract"].getString(), joboptions["fndata_reextract"].node_type)
    cli.add_innode(node2)
    # if joboptions["do_reset_offsets"].getBoolean())
    new_arg = rc.Flag("--reset_offsets","","do_reset_offsets", True)
    # elif joboptions["do_recenter"].getBoolean())
    new_arg = rc.Flag("--recenter","","do_recenter",True)
    new_arg = rc.Flag("--recenter_x ", "recenter_x","do_recenter",True)
    cli.args.append(new_arg)
    new_arg = rc.Flag("--recenter_y ", "recenter_y","do_recenter",True)
    cli.args.append(new_arg)
    new_arg = rc.Flag("--recenter_z ", "recenter_z","do_recenter",True)
    cli.args.append(new_arg)
    # else
    mylist = joboptions["coords_suffix"]
    if mylist == "":
        error_message = "ERROR: empty field for coordinate STAR file..."
        return False
    
    #  Attempt at backwards compatibility
    if mylist.contains("coords_suffix"):
        new_arg = rc.Param("--coord_dir ", mylist.beforeLastOf("/") + "/")
        new_arg = rc.Param("--coord_suffix ", (mylist.afterLastOf("/")).without("coords_suffix"))
    else:
        new_arg = rc.Param("--coord_list ",mylist)
        node2 = rc.Node(mylist, joboptions["coords_suffix"].node_type)
        cli.add_innode(node2)
    
    #  Output
    fn_ostar = outputname + "particles.star"

    new_arg = rc.Param("--part_star ",fn_ostar)

    if joboptions["do_reextract"].getBoolean():
        fn_pickstar = outputname + "extractpick.star"
        node = rc.Node (fn_pickstar, rh.LABEL_EXTRACT_COORDS_REEX)
        cli.add_outnode(node)
        new_arg = rc.Flag("--pick_star ",fn_pickstar,"do_reextract",True)
        cli.args.append(new_arg)

    if joboptions["do_extract_helix"].getBoolean() and joboptions["do_extract_helical_tubes"].getBoolean():
        fn_pickstar = outputname + "extractpick.star"
        node = rc.Node (fn_pickstar, rh.LABEL_EXTRACT_COORDS_HELIX)
        cli.add_outnode(node)
        new_arg = rc.Param("--pick_star ", "do_extract_helix",fn_pickstar)
        cli.args.append(new_arg)   

    new_arg = rc.Param("--part_dir ", outputname)
    cli.args.append(new_arg)
    new_arg = rc.Param("--extract","")
    cli.args.append(new_arg)
    new_arg = rc.Param("--extract_size ", "extract_size")
    cli.args.append(new_arg)

    # if joboptions["do_fom_threshold"].getBoolean():
    new_arg = rc.Param("--minimum_pick_fom ", "minimum_pick_fom","do_fom_threshold",True)
    cli.args.append(new_arg)
    
    # if joboptions["do_float16"].getBoolean():
    new_arg = rc.Param("--float16 ","","do_float16",True)
    
    #  Operate stuff
    #  Get an integer number for the bg_radius
    if joboptions["bg_diameter"].getNumber(error_message) < 0.:
        bg_radius =  0.75 * joboptions["extract_size"].getNumber(error_message)
    else:
        bg_radius = joboptions["bg_diameter"].getNumber(error_message)

    if error_message != "":
        return False

    bg_radius /= 2. #  Go from diameter to radius
    # if joboptions["do_rescale"].getBoolean():
    new_arg = rc.Param("--scale ", "rescale","do_rescale",True)
    cli.args.append(new_arg)
    bg_radius *= joboptions["rescale"].getNumber(error_message)
    if error_message != "":
        return False

    bg_radius /= joboptions["extract_size"].getNumber(error_message)
    if error_message != "":
        return False
        # if joboptions["do_norm"].getBoolean():
            #  Get an integer number for the bg_radius
            # bg_radius = (int)bg_radius
        new_arg = rc.Param("--norm --bg_radius ", floatToString(bg_radius),"do_norm",True)
        new_arg = rc.Param("--white_dust ", "white_dust")
        cli.args.append(new_arg)
        new_arg = rc.Param("--black_dust ", "black_dust")
        cli.args.append(new_arg)
        # if joboptions["do_invert"].getBoolean():
        new_arg = rc.Param("--invert_contrast ","","do_invert",True)

def getCommandsExtractHelixJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    cli.add_prog(rc.Prog("`which relion_preprocess_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_preprocess`","use_mpi",True))
    #  Helix
    if joboptions["do_extract_helix"].getBoolean():
        node3 = rc.Node (fn_ostar, rh.LABEL_EXTRACT_PARTS_HELIX)
        cli.add_outnode(node3)

        label += ".helical"

        new_arg = rc.Param("--helix","")
        new_arg = rc.Param("--helical_outer_diameter ", "helical_tube_outer_diameter")
        cli.args.append(new_arg)
        # if joboptions["helical_bimodal_angular_priors"].getBoolean():
        new_arg = rc.Param("--helical_bimodal_angular_priors","","helical_bimodal_angular_priors",True)
        cli.args.append(new_arg)
        # if joboptions["do_extract_helical_tubes"].getBoolean())
        new_arg = rc.Param("--helical_tubes","","do_extract_helical_tubes",True)
        cli.args.append(new_arg)
        # if joboptions["do_cut_into_segments"].getBoolean():
        new_arg = rc.Param("--helical_cut_into_segments","","do_cut_into_segments",True)
        cli.args.append(new_arg)
        new_arg = rc.Param("--helical_nr_asu ", "helical_nr_asu","do_cut_into_segments",True)
        cli.args.append(new_arg)
        new_arg = rc.Param("--helical_rise ", "helical_rise","do_cut_into_segments",True)
        cli.args.append(new_arg)
        # else
        new_arg = rc.Param("--helical_nr_asu 1 --helical_rise 1","","do_cut_into_segments",False)
        # else
        node3 = rc.Node(fn_ostar, rh.LABEL_EXTRACT_PARTS)
        cli.add_outnode(node3)
    

    if is_continue:
        new_arg = rc.Param("--only_do_unfinished ","")

    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    if joboptions["do_reextract"].getBoolean():
        node = rc.Node(outputname + "reextract.star", rh.LABEL_EXTRACT_COORDS_REEX)
        cli.add_outnode(node)
    
    if joboptions["do_extract_helix"].getBoolean() and joboptions["do_extract_helical_tubes"].getBoolean():
        node = rc.Node (outputname + "helix_segments.star", rh.LABEL_EXTRACT_COORDS_HELIX)
        cli.add_outnode(node)
    
    return script

def getCommandsSelectFilamentJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    if joboptions["fn_model"] == "" and joboptions["fn_mic"] == "" and joboptions["fn_data"] == "":
        #  Nothing was selected...
        error_message = "Please select an input file."
        return False
    
    # USELESS
    # c = 0
    # if joboptions["do_select_values"].getBoolean(): 
    #     c += 1
    # if joboptions["do_discard"].getBoolean(): 
    #     c += 1
    # if joboptions["do_split"].getBoolean(): 
    #     c += 1
    # if joboptions["do_remove_duplicates"].getBoolean(): 
    #     c += 1
    # if joboptions["do_filaments"].getBoolean(): 
    #     c += 1
    # if c > 1:
    #     error_message = "You cannot do many tasks simultaneously..."
    #     return False
    
#    if joboptions["do_filaments"].getBoolean())
#    label += ".filamentsdendrogram"
    cli.add_prog(rc.Prog("`which relion_filament_selection`"))

    if joboptions["fn_mic"] != "" or joboptions["fn_data"] != "":
        error_message = "ERROR: Filament selection by dendrogram analysis is only possible for optimiser STAR files..."
        return False
        
        if joboptions["fn_model"] == "":
            error_message = "ERROR: Filament selection by dendrogram analysis needs an optimiser STAR file..."
            return False
        
        node = rc.Node(joboptions["fn_model"].getString(), joboptions["fn_model"].node_type)
        cli.add_innode(node)

        fn_out = outputname + "run_optimiser.star"
        node2 = rc.Node(fn_out, rh.LABEL_SELECT_OPT)
        cli.add_outnode(node2)

        node3 = rc.Node(outputname + "logfile.pdf", rh.LABEL_SELECT_LOG)
        cli.add_outnode(node3)

        new_arg = rc.Param(" -i ", "fn_model")
        cli.args.append(new_arg)
        new_arg = rc.Param(" -o ",outputname)
        new_arg = rc.Param(" -t ", "dendrogram_threshold")
        cli.args.append(new_arg)
        new_arg = rc.Param(" -c ", "dendrogram_minclass")
        cli.args.append(new_arg)

    return script

def getCommandsSelectDuplicateJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    if joboptions["fn_model"] == "" and joboptions["fn_mic"] == "" and joboptions["fn_data"] == "":
        #  Nothing was selected...
        error_message = "Please select an input file."
        return False
    
   
    # elif joboptions["do_remove_duplicates"].getBoolean():
    #    label += ".removeduplicates"

        #  Remove duplicates
        cli.add_prog(rc.prog("`which relion_star_handler`"))

        if joboptions["fn_mic"] != "" or joboptions["fn_model"] != "":
            error_message = "ERROR: Duplicate removal is only possible for particle STAR files..."
            return False
        
        if joboptions["fn_data"] == "":
            error_message = "ERROR: Duplicate removal needs a particle STAR file..."
            return False
        
        node = rc.Node(joboptions["fn_data"].getString(), joboptions["fn_data"].node_type)
        cli.add_innode(node)
        new_arg = rc.Param("--i ", "fn_data")
        cli.args.append(new_arg)

        fn_out = outputname + "particles.star"
        node2 = rc.Node(fn_out, rh.LABEL_SELECT_PARTS)
        cli.add_outnode(node2)
        new_arg = rc.Param("--o ", fn_out)

        new_arg = rc.Param("--remove_duplicates ", "duplicate_threshold")
        cli.args.append(new_arg)
        if joboptions["image_angpix"].getNumber(error_message) > 0:
            new_arg = rc.Param("--image_angpix ", "image_angpix","is_positive",True)
            cli.args.append(new_arg)
        if error_message != "":
            return False
        
    return script

def getCommandsSelectDuplicateJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)

    if joboptions["do_select_values"].getBoolean() or joboptions["do_discard"].getBoolean() or joboptions["do_split"].getBoolean():
        #  Value-based selection
        command="`which relion_star_handler`"

        if joboptions["fn_model"] != "":
            error_message = "ERROR: Value-selection or subset splitting is only possible for micrograph or particle STAR files..."
            return False
        
        fn_out = ''
        if joboptions["fn_mic"] != "":
            node = rc.Node(joboptions["fn_mic"].getString(), joboptions["fn_mic"].node_type)
            cli.add_innode(node)
            new_arg = rc.Param("--i ", "fn_mic")
            cli.args.append(new_arg)
            fn_out = outputname+"micrographs.star"

        elif joboptions["fn_data"] != "":
            node = rc.Node(joboptions["fn_data"].getString(), joboptions["fn_data"].node_type)
            cli.add_innode(node)
            new_arg = rc.Param("--i ", "fn_data")
            cli.args.append(new_arg)
            fn_out = outputname+"particles.star"
            new_arg = rc.Param("--o ",fn_out)

        if joboptions["do_select_values"].getBoolean() or joboptions["do_discard"].getBoolean():
        
            if joboptions["fn_mic"] != "":
                node2 = rc.Node (fn_out, rh.LABEL_SELECT_MICS)
                cli.add_outnode(node2)
            elif joboptions["fn_data"] != "":
                node2 = rc.Node(fn_out, rh.LABEL_SELECT_PARTS)
                cli.add_outnode(node2)
    return script

def getCommandsSelectOnValueJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    if joboptions["fn_model"] == "" and joboptions["fn_mic"] == "" and joboptions["fn_data"] == "":
        #  Nothing was selected...
        error_message = "Please select an input file."
        return False
    
   
    # if joboptions["do_select_values"].getBoolean())
    #   label += ".onvalue"

    new_arg = rc.Param("--select ", "select_label")
    cli.args.append(new_arg)
    new_arg = rc.Param("--minval ", "select_minval")
    cli.args.append(new_arg)
    new_arg = rc.Param("--maxval ", "select_maxval")
    cli.args.append(new_arg)

def getCommandsSelectDiscardJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)    
    
    # elif joboptions["do_discard"].getBoolean())
    #    label += ".discard"

    new_arg = rc.Param("--discard_on_stats ","")
    cli.args.append(new_arg)
    new_arg = rc.Param("--discard_label ", "discard_label")
    cli.args.append(new_arg)
    new_arg = rc.Param("--discard_sigma ", "discard_sigma")
    cli.args.append(new_arg)
            
def getCommandsSelectSplitJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    if joboptions["fn_model"] == "" and joboptions["fn_mic"] == "" and joboptions["fn_data"] == "":
        #  Nothing was selected...
        error_message = "Please select an input file."
        return False
    
   
    # if joboptions["do_split"].getBoolean())
    #    label += ".split"

    nr_split=0
    new_arg = rc.Param("--split ","")
    cli.args.append(new_arg)
    # if joboptions["do_random"].getBoolean())
    new_arg = rc.Flag("--random_order ","","do_random",True)
    cli.args.append(new_arg)

    if joboptions["nr_split"].getNumber(error_message) <= 0 and joboptions["split_size"].getNumber(error_message) <= 0 \
        and not joboptions["nr_split"].isSchedulerVariable() and not joboptions["split_size"].isSchedulerVariable():
            error_message = "ERROR: When splitting the input STAR file into subsets, set nr_split and/or split_size to a positive value"
            return False
            
    if joboptions["nr_split"].getNumber(error_message) > 0 and not joboptions["nr_split"].isSchedulerVariable():
        if error_message != "": 
            return False

        nr_split = joboptions["nr_split"].getNumber(error_message)
        new_arg = rc.Param("--nr_split ", "nr_split")
        cli.args.append(new_arg)
        if joboptions["split_size"].getNumber(error_message) > 0 and not joboptions["split_size"].isSchedulerVariable():
            if error_message != "":
                return False

        new_arg = rc.Param("--size_split ", "split_size")
        cli.args.append(new_arg)

    return script
    
        #  As of relion-3.1, star_handler will write out a star file with the output nodes, which will be read by the pipeliner


def getCommandsSelectRankerJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    if joboptions["fn_model"] == "" and joboptions["fn_mic"] == "" and joboptions["fn_data"] == "":
        #  Nothing was selected...
        error_message = "Please select an input file."
        return False
    
    #  Automated 2D class selection through the class_ranker
    # if joboptions["do_class_ranker"].getBoolean())
    #    label += ".class2dauto"

    if joboptions["fn_model"] == "":
        error_message = "ERROR: When using automatically selecting 2D classes, one needs to provide an optimiser.star file"
        return False
            
    if joboptions["do_regroup"].getBoolean() or joboptions["do_recenter"].getBoolean():
        error_message = "ERROR: regrouping and recentering have not been implemented in class_ranker."
        return False
            
    cli.add_prog(rc.Prog("`which relion_class_ranker`"))

    #  input
    new_arg = rc.Param("--opt ", "fn_model")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["fn_model"].getString(), joboptions["fn_model"].node_type)
    cli.add_innode(node)

    # output
    new_arg = rc.Param("--o ",outputname)
    cli.args.append(new_arg)
    new_arg = rc.Param("--fn_sel_parts particles.star --fn_sel_classavgs class_averages.star","")
    cli.args.append(new_arg)

    if joboptions["select_nr_parts"].getNumber(error_message) > 0:
        new_arg = rc.Param("--select_min_nr_particles ", "select_nr_parts")
        cli.args.append(new_arg)
    elif joboptions["select_nr_classes"].getNumber(error_message) > 0:
        new_arg = rc.Param("--select_min_nr_classes ", "select_nr_classes")
        cli.args.append(new_arg)
            
    fn_parts = outputname+"particles.star"
    node2 = rc.Node(fn_parts, rh.LABEL_SELECT_PARTS)
    cli.add_outnode(node2)

    fn_imgs = outputname+"class_averages.star"
    node3 = rc.Node(fn_imgs, rh.LABEL_SELECT_CLAVS)
    cli.add_outnode(node3)

    #  Also save optimiser.star, which could be used for next manual selection (but ordered for examples on the new scores)
    new_arg = rc.Param("--fn_root rank","")

    #  Only save the 2D class averages for 2D jobs
    fn_opt = outputname+"rank_optimiser.star"
    node4 = rc.Node(fn_opt, rh.LABEL_SELECT_OPT)
    cli.add_outnode(node4)

    #  perform the actual prediction and selection
    new_arg = rc.Param("--do_granularity_features ","")
    cli.args.append(new_arg)
    new_arg = rc.Param("--auto_select ","")
    cli.args.append(new_arg)
    new_arg = rc.Param("--min_score ", "rank_threshold")
    cli.args.append(new_arg)

    return script

def getCommandsSelectInteractiveJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    if joboptions["fn_model"] == "" and joboptions["fn_mic"] == "" and joboptions["fn_data"] == "":
        #  Nothing was selected...
        error_message = "Please select an input file."
        return False
    
        
    #  Interactive selection
    label += ".interactive"

    command="`which relion_display`"

    #  I/O
    # if joboptions["fn_model"] != "":
    new_arg = rc.Param("--gui --i ", "fn_model",assertion="required")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["fn_model"].getString(), joboptions["fn_model"].node_type)
    cli.add_innode(node)

    fn_parts = outputname+"particles.star"
    new_arg = rc.Param("--allow_save --fn_parts ",fn_parts)
    node2 = rc.Node(fn_parts, rh.LABEL_SELECT_PARTS)
    cli.add_outnode(node2)

    #  Only save the 2D class averages for 2D jobs
    fnt = joboptions["fn_model"]
    if fnt.contains("Class2D/"):
        fn_imgs = outputname+"class_averages.star"
        new_arg = rc.Param("--fn_imgs ",fn_imgs)
        node3 = rc.Node(fn_imgs, rh.LABEL_SELECT_CLAVS)
        cli.add_outnode(node3)

        # if joboptions["do_recenter"].getBoolean())
        new_arg = rc.Flag("--recenter ","","do_recenter",True)
    # elif joboptions["fn_mic"] != "":
    new_arg = rc.Param("--gui --i ", "fn_mic",assertion="required")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["fn_mic"].getString(), joboptions["fn_mic"].node_type)
    cli.add_innode(node)

    fn_mics = outputname+"micrographs.star"
    new_arg = rc.Param("--allow_save --fn_imgs ",fn_mics,"fn_mic","required")
    node2 = rc.Node(fn_mics, rh.LABEL_SELECT_MICS)
    cli.add_outnode(node2)
        
    # elif joboptions["fn_data"] != "":
    new_arg = rc.Param("--gui --i ", "fn_data",assertion="required")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["fn_data"].getString(), joboptions["fn_data"].node_type)
    cli.add_innode(node)

    fn_parts = outputname+"particles.star"
    new_arg = rc.Flag("--allow_save --fn_imgs ", fn_parts,"fn_data","required")
    node2 = rc.Node(fn_parts, rh.LABEL_SELECT_PARTS)
    cli.add_outnode(node2)
                    
    #  Re-grouping
    # if joboptions["do_regroup"].getBoolean():
    #     if joboptions["fn_model"] == "":
    #         error_message = "Re-grouping only works for model.star/optimiser.star files..."
    #         return False
    new_arg = rc.Flag("--regroup ", "nr_groups","do_regroup",True)
    cli.args.append(new_arg)
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    return script

def getCommandsClass2DJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    cli.add_prog(rc.Prog("`which relion_refine_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_refine`","use_mpi",False))

    fn_run = "run"
    if is_continue:
        if joboptions["fn_cont"] == "":
            error_message = "ERROR: empty field for continuation STAR file..."
            return False
        pos_it = joboptions["fn_cont"].rfind("_it")
        pos_op = joboptions["fn_cont"].rfind("_optimiser")
        if pos_it < 0 or pos_op < 0:
            error_message = "Warning: invalid optimiser.star filename provided for continuation run!"
            return False
        #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
        # int it = (int)textToFloat((joboptions["fn_cont"].substr(pos_it+3, 6)).c_str())
        # fn_run += "_ct" + floatToString(it)
        new_arg = rc.Param("--continue ", "fn_cont")
        cli.args.append(new_arg)
    
    new_arg = rc.Param("--o ",outputname + fn_run)

    my_classes = joboptions["nr_classes"].getNumber(error_message)
    if error_message != "":
        return False

    #  Optimisation
    my_iter = 0
    if joboptions["do_em"].getBoolean():
        if joboptions["do_grad"].getBoolean():
            error_message = "You cannot specify to use both the EM and the VDAM algorithm!"
            return False
        
        new_arg = rc.Param("--iter ", "nr_iter_em")
        cli.args.append(new_arg)

        my_iter = joboptions["nr_iter_em"].getNumber(error_message)
        if error_message != "": 
            return False
        elif joboptions["do_grad"].getBoolean():
            if joboptions["nr_mpi"].getNumber(error_message) > 1:
                error_message = "Gradient refinement (running the VDAM algorithm) is not supported together with MPI."
                return False
        
        new_arg = rc.Param("--grad --class_inactivity_threshold 0.1 --grad_write_iter 10","")
        cli.args.append(new_arg)
        new_arg = rc.Param("--iter ", "nr_iter_grad")
        cli.args.append(new_arg)

        my_iter = joboptions["nr_iter_grad"].getNumber(error_message)
        if error_message != "":
            return False
        else:
            error_message = "You need to specify to use either the EM or the VDAM algorithm"
            return False
    
    outputNodes = getOutputNodesRefine(outputname + fn_run, "Class2D", my_iter, my_classes, 2, 1, is_tomo)

    if not is_continue:
        # if joboptions["fn_img"] == "":
        #         error_message = "ERROR: empty field for input STAR file..."
        #         return False
        new_arg = rc.Param("--i ", "fn_img",assertion="required")
        cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_img"].getString(), joboptions["fn_img"].node_type)
        cli.add_innode(node)
    
    #  Always do compute stuff
#   if not joboptions["do_combine_thru_disc"].getBoolean())
    new_arg = rc.Flag("--dont_combine_weights_via_disc","","do_combine_thru_disc",False)
#   if not joboptions["do_parallel_discio"].getBoolean())
    new_arg = rc.Flag("--no_parallel_disc_io","","do_parallel_discio",False)
#   if joboptions["do_preread_images"].getBoolean())
    new_arg = rc.Flag("--preread_images ", "","do_preread_images", True)
#    elif joboptions["scratch_dir"] != "")
    new_arg = rc.Flag("--scratch_dir ","scratch_dir","scratch_dir",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--pool ", "nr_pool")
    cli.args.append(new_arg)
    #  Takanori observed bad 2D classifications with pad1, so use pad2 always. Memory isnt a problem here anyway.
    new_arg = rc.Param("--pad","2")
    cli.args.append(new_arg)

    #  CTF stuff
    if not is_continue:
        # if joboptions["do_ctf_correction"].getBoolean():
        new_arg = rc.Param("--ctf ","","do_ctf_correction",True)
        # if joboptions["ctf_intact_first_peak"].getBoolean():
        new_arg = rc.Param("--ctf_intact_first_peak ","","ctf_intact_first_peak",True)
            
    new_arg = rc.Param("--tau2_fudge ", "tau_fudge")
    cli.args.append(new_arg)
    new_arg = rc.Param("--particle_diameter ", "particle_diameter")
    cli.args.append(new_arg)
    if not is_continue:
        new_arg = rc.Param("--K ", "nr_classes")
        cli.args.append(new_arg)
        #  Always flatten the solvent
        new_arg = rc.Param("--flatten_solvent ","")
        # if joboptions["do_zero_mask"].getBoolean():
        new_arg = rc.Param("--zero_mask ","","do_zero_mask",True)
        cli.args.append(new_arg)
        # if joboptions["highres_limit"].getNumber(error_message) > 0:
        new_arg = rc.Flag("--strict_highres_exp ", "highres_limit","highres_limit","is_positive")
        cli.args.append(new_arg)
        if error_message != "":
            return False

    
    # if joboptions["do_center"].getBoolean():
    new_arg = rc.Param("--center_classes ","","do_center",True)
    cli.args.append(new_arg)
    #  Sampling
    iover = 1.0
    new_arg = rc.Param("--oversampling ",iover)
    cli.args.append(new_arg)

    # if not joboptions["dont_skip_align"].getBoolean():
    new_arg = rc.Param("--skip_align ","","dont_skip_align",True)
    cli.args.append(new_arg)
    # else
    #  The sampling given in the GUI will be the oversampled one!
    new_arg = rc.Param("--psi_step ","psi_sampling" * pow(2., iover),"dont_skip_align",True)
    if error_message != "":
        return False

    #  Offset range
    new_arg = rc.Param("--offset_range ", "offset_range")
    cli.args.append(new_arg)
    #  The sampling given in the GUI will be the oversampled one!
    new_arg = rc.Param("--offset_step ","offset_step" * pow(2., iover))
    if error_message != "":
        return False

    # if joboptions["allow_coarser"].getBoolean())
    new_arg = rc.Param("--allow_coarser_sampling","","allow_coarser",True)
    cli.args.append(new_arg)        
    
    #  Helix
    if joboptions["do_helix"].getBoolean():
        label += ".helical"

        new_arg = rc.Param("--helical_outer_diameter ", "helical_tube_outer_diameter")
        cli.args.append(new_arg)

        if joboptions["dont_skip_align"].getBoolean():
            # if joboptions["do_bimodal_psi"].getBoolean():
            new_arg = rc.Param("--bimodal_psi","","do_bimodal_psi",True)

            val = joboptions["range_psi"].getNumber(error_message)
            if error_message != "":
                return False

            val = 0. if val < 0. else val
            val = 90. if val > 90. else val
            new_arg = rc.Param("--sigma_psi ",floatToString(val / 3.))

            if joboptions["do_restrict_xoff"].getBoolean():
                new_arg = rc.Param("--helix --helical_rise_initial ", "helical_rise")
                cli.args.append(new_arg)
                        
    #  Always do norm and scale correction
    if not is_continue:
        new_arg = rc.Param("--norm --scale ","")
        cli.args.append(new_arg)

    #  Running stuff
    new_arg = rc.Param("--j ", "nr_threads")
    cli.args.append(new_arg)

    #  GPU-stuff
    # if joboptions["use_gpu"].getBoolean():
    new_arg = rc.Param("--gpu", "gpu_ids","use_gpu",True)
    cli.args.append(new_arg)
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    return script

def getCommandsInimodelJob(outputname,label,job_counter=-1):
    script, cli = clear(label)

    initialisePipeline(outputname, job_counter)
    is_tomo = False

#   USELESS
#   if joboptions["nr_mpi"].getNumber(error_message) > 1)
#            error_message = "Gradient refinement is not supported together with MPI."
#        return False
#        if (error_message != "":
#           return False

    #  Quickly remove RELION_JOB_EXIT_SUCCESS
    command0 = script.new_command()
    command0.add_prog("rm -f " + outputname + 'RELION_JOB_EXIT_SUCCESS')
    # commands.push_back(command0)

    cli.add_prog(rc.Prog("`which relion_refine`"))

    fn_sym = joboptions["sym_name"]

    fn_run = "run"
    if is_continue:
        if joboptions["fn_cont"]== "":
                error_message = "ERROR: empty field for continuation STAR file..."
        return False

        pos_it = joboptions["fn_cont"].rfind("_it")
        pos_op = joboptions["fn_cont"].rfind("_optimiser")
        if pos_it < 0 or pos_op < 0:
            # std::cerr << "Warning: invalid optimiser.star filename provided for continuation run: " << joboptions["fn_cont"] << std::endl
            pass
            
        #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
        # int it = (int)textToFloat((joboptions["fn_cont"].substr(pos_it+3, 6)).c_str())
        # fn_run += "_ct" + floatToString(it)
        new_arg = rc.Param("--continue ", "fn_cont")
        cli.args.append(new_arg)

    
    new_arg = rc.Param("--o " + outputname + fn_run)
    cli.args.append(new_arg)
    new_arg = rc.Param("--iter ", "nr_iter")
    cli.args.append(new_arg)

    # if is_tomo:
    #     label += ".tomo"

    total_nr_iter = joboptions["nr_iter"].getNumber(error_message)
    if error_message != "":
        return False
    nr_classes = joboptions["nr_classes"].getNumber(error_message)
    if error_message != "":
        return False

    if not is_continue:
        new_arg = rc.Param("--grad --denovo_3dref ","")

        if is_tomo:
            error_message = getTomoInputCommmand(True, command, rh.HAS_COMPULSORY, rh.HAS_COMPULSORY, rh.HAS_NOT, rh.HAS_NOT)
            if error_message != "":
                return False

            node1 = rc.Node( outputname + fn_run + "_optimisation_set.star", rh.LABEL_INIMOD_OPTSET)
            cli.add_outnode(node1)

            sigma = joboptions["sigma_tilt"].getNumber(error_message)
            if error_message != "":
                return False
            if sigma > 0.:
                new_arg = rc.Param("--sigma_tilt ", "sigma_tilt")
                cli.args.append(new_arg)
            
            else:
                if joboptions["fn_img"] == "":
                    error_message = "ERROR: empty field for input STAR file..."
                    return False
                else:
                    new_arg = rc.Param("--i ", "fn_img")
                    cli.args.append(new_arg)
                node = rc.Node(joboptions["fn_img"].getString(), joboptions["fn_img"].node_type)
                cli.add_innode(node)
                    
        #  CTF stuff
        # if joboptions["do_ctf_correction"].getBoolean():
        new_arg = rc.Param("--ctf","","do_ctf_correction",True)
        cli.args.append(new_arg)
        #    if joboptions["ctf_intact_first_peak"].getBoolean():
        new_arg = rc.Param("--ctf_intact_first_peak","","ctf_intact_first_peak",True)
        cli.args.append(new_arg)
        new_arg = rc.Param("--K ", "nr_classes")
        cli.args.append(new_arg)
        # if joboptions["do_run_C1"].getBoolean():
        new_arg = rc.Flag("--sym C1 ","","do_run_C1",True)
        cli.args.append(new_arg)
        # else:
        new_arg = rc.Flag("--sym ","fn_sym","do_run_C1",False)
        cli.args.append(new_arg)
        
        # if joboptions["do_solvent"].getBoolean():
        new_arg = rc.Param("--flatten_solvent ","","do_solvent",True)
        cli.args.append(new_arg)
        new_arg = rc.Param("--zero_mask ","")
        cli.args.append(new_arg)
    
    #  Always do compute stuff
#   if not joboptions["do_combine_thru_disc"].getBoolean())
    new_arg = rc.Flag("--dont_combine_weights_via_disc","","do_combine_thru_disc",False)
#   if not joboptions["do_parallel_discio"].getBoolean())
    new_arg = rc.Flag("--no_parallel_disc_io","","do_parallel_discio",False)
#   if joboptions["do_preread_images"].getBoolean())
    new_arg = rc.Flag("--preread_images ", "","do_preread_images", True)
#    elif joboptions["scratch_dir"] != "")
    new_arg = rc.Flag("--scratch_dir ","scratch_dir","scratch_dir",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--pool ", "nr_pool")
    cli.args.append(new_arg)
    #  Pad 1
    new_arg = rc.Param("--pad","1")
    cli.args.append(new_arg)

    #  Optimisation
    new_arg = rc.Param("--particle_diameter ", "particle_diameter")
    cli.args.append(new_arg)
    new_arg = rc.Param("--oversampling 1  --healpix_order 1  --offset_range 6  --offset_step 2 --auto_sampling ","")
    new_arg = rc.Param("--tau2_fudge ", "tau_fudge")
    cli.args.append(new_arg)

    #  Running stuff
    new_arg = rc.Param("--j ", "nr_threads")
    cli.args.append(new_arg)

    #  GPU-stuff
    # if joboptions["use_gpu"].getBoolean():
    new_arg = rc.Param("--gpu", "gpu_ids","use_gpu",True)
    cli.args.append(new_arg)
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    fn_model = None
    fn_model.compose(outputname + fn_run + "_it", total_nr_iter,"",3)
    fn_model+="_model.star"

    #  Align with symmetry axes and apply symmetry
    command2 = "`which relion_align_symmetry`"
    command2 += "--i " + fn_model
    command2 += "--o " + outputname + "initial_model.mrc"

    if  joboptions["do_run_C1"].getBoolean() and not (fn_sym == "C1" or fn_sym == "c1") :
        command2 += "--sym ", "sym_name"
        cli.args.append(new_arg)
    else:
        command2 += "--sym C1 "
        command2 += "--apply_sym --select_largest_class "
    commands.push_back(command2)

    #  And re-introduce RELION_JOB_EXIT_SUCCESS
    F = "touch " + outputname + RELION_JOB_EXIT_SUCCESS
    commands.push_back(commandF)

    #  Output nodes
    node2 = rc.Node(outputname + "initial_model.mrc", rh.LABEL_INIMOD_MAP)
    cli.add_outnode(node2)

    #  If doing more than 1 class, make them all available (one of them will be the same as initial_model.mrc)
    if nr_classes > 1:
        for iclass in range(len(nr_classes)):
                fn_tmp = ''
                fn_tmp.compose(outputname + fn_run + "_it", total_nr_iter, "", 3)
                fn_tmp.compose(fn_tmp + "_class", iclass+1, "mrc", 3)
                node3 = rc.Node (fn_tmp, rh.LABEL_INIMOD_MAP)
                cli.add_outnode(node3)
            
    return script

def getCommandsClass3DJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    rc.Prog("`which relion_refine_mpi`","use_mpi",True)
    rc.Prog("`which relion_refine`","use_mpi",True)

    fn_run = "run"
    if is_continue:
        if joboptions["fn_cont"] == "":
            error_message = "ERROR: empty field for continuation STAR file..."
            return False
        pos_it = joboptions["fn_cont"].rfind("_it")
        pos_op = joboptions["fn_cont"].rfind("_optimiser")
        if pos_it < 0 or pos_op < 0:
            err = 'std::cerr << "Warning: invalid optimiser.star filename provided for continuation run: " << joboptions["fn_cont"] << std::endl'
        #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
        # int it = (int)textToFloat((joboptions["fn_cont"].substr(pos_it+3, 6)).c_str():
        # fn_run += "_ct" + floatToString(it)
        new_arg = rc.Param("--continue ", "fn_cont")
        cli.args.append(new_arg)

    
    new_arg = rc.Param("--o ", outputname + fn_run)

    my_iter = joboptions["nr_iter"].getNumber(error_message)
    if error_message != "":
        return False

    my_classes = joboptions["nr_classes"].getNumber(error_message)
    if error_message != "":
        return False

    outputNodes = getOutputNodesRefine(outputname + fn_run, "Class3D", my_iter, my_classes, 3, 1, is_tomo)

    if not is_continue:
        if is_tomo:
            error_message = getTomoInputCommmand(true, command, HAS_COMPULSORY, HAS_COMPULSORY, HAS_NOT, HAS_NOT)
            if error_message != "":
                return False

            node1 = rc.Node( outputname + fn_run + "_optimisation_set.star", rh.LABEL_CLASS3D_OPTSET)
            cli.add_outnode(node1)

            sigma = joboptions["sigma_tilt"].getNumber(error_message)
            if error_message != "":
                return False
            if sigma > 0.:
                new_arg = rc.Param("--sigma_tilt ", "sigma_tilt")
                cli.args.append(new_arg)
            else:
                if joboptions["fn_img"] == "":
                    error_message = "ERROR: empty field for input STAR file..."
                    return False
                else:
                    new_arg = rc.Param("--i ", "fn_img")
                    cli.args.append(new_arg)
                    node = rc.Node(joboptions["fn_img"].getString(), joboptions["fn_img"].node_type)
                    cli.add_innode(node)
                    
        if joboptions["fn_ref"] == "":
            error_message = "ERROR: empty field for reference."
            return False
        else:
            new_arg = rc.Param("--ref ", "fn_ref")
            cli.args.append(new_arg)
            if joboptions["fn_ref"] != "None":
                node = rc.Node(joboptions["fn_ref"].getString(), joboptions["fn_ref"].node_type)
                cli.add_innode(node)
                # if not joboptions["ref_correct_greyscale"].getBoolean():
                new_arg = rc.Param("--firstiter_cc","","ref_correct_greyscale",False)
                cli.args.append(new_arg)
            # if joboptions["trust_ref_size"].getBoolean():
            new_arg = rc.Param("--trust_ref_size","","trust_ref_size",True)
        
        # if joboptions["ini_high"].getNumber(error_message) > 0.:
        new_arg = rc.Param("--ini_high ", "ini_high",assertion="is_positive")
        cli.args.append(new_arg)
        if error_message != "":
            return False

    
    #  Always do compute stuff
#   if not joboptions["do_combine_thru_disc"].getBoolean())
    new_arg = rc.Flag("--dont_combine_weights_via_disc","","do_combine_thru_disc",False)
#   if not joboptions["do_parallel_discio"].getBoolean())
    new_arg = rc.Flag("--no_parallel_disc_io","","do_parallel_discio",False)
#   if joboptions["do_preread_images"].getBoolean())
    new_arg = rc.Flag("--preread_images ", "","do_preread_images", True)
#    elif joboptions["scratch_dir"] != "")
    new_arg = rc.Flag("--scratch_dir ","scratch_dir","scratch_dir",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--pool ", "nr_pool")
    cli.args.append(new_arg)
    new_arg = rc.Param("--pad","1","do_pad1",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--pad","2", "do_pad1", False)
    cli.args.append(new_arg)


    #  CTF stuff
    if not is_continue:
        # if joboptions["do_ctf_correction"].getBoolean():
        new_arg = rc.Param("--ctf","","do_ctf_correction",True)
        cli.args.append(new_arg)
        #    if joboptions["ctf_intact_first_peak"].getBoolean())
        new_arg = rc.Param("--ctf_intact_first_peak","","ctf_intact_first_peak",True)
        cli.args.append(new_arg)
    #  Optimisation
    new_arg = rc.Param("--iter ", "nr_iter")
    cli.args.append(new_arg)
    new_arg = rc.Param("--tau2_fudge ", "tau_fudge")
    cli.args.append(new_arg)
    new_arg = rc.Param("--particle_diameter ", "particle_diameter")
    cli.args.append(new_arg)
    if not is_continue:
        # if joboptions["do_fast_subsets"].getBoolean():
        new_arg = rc.Flag("--fast_subsets ","","do_fast_subsets",True)
        cli.args.append(new_arg)
        new_arg = rc.Param("--K ", "nr_classes")
        cli.args.append(new_arg)
        #  Always flatten the solvent
        new_arg = rc.Param("--flatten_solvent","")
        cli.args.append(new_arg)
        # if joboptions["do_zero_mask"].getBoolean():
        new_arg = rc.Param("--zero_mask","","do_zero_mask",True)
        # if joboptions["highres_limit"].getNumber(error_message) > 0:
        new_arg = rc.Param("--strict_highres_exp ", "highres_limit",assertion="is_positive")
        cli.args.append(new_arg)
        if error_message != "":
            return False
    
    # if joboptions["do_blush"].getBoolean():
    new_arg = rc.Param("--blush ","","do_blush",True)

    # if joboptions["fn_mask"].length() > 0:
    new_arg = rc.Param("--solvent_mask ", "fn_mask",assertion="required")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["fn_mask"].getString(), joboptions["fn_mask"].node_type)
    cli.add_innode(node)
    
    #  Sampling
    if not joboptions["dont_skip_align"].getBoolean():
        new_arg = rc.Param("--skip_align ","","dont_skip_align",True)
    else:
        iover = 1
        new_arg = rc.Param("--oversampling ", iover)
        sampling = rho.getHealPixOrder(joboptions["sampling"])
        if sampling <= 0:
            error_message = "Wrong choice for sampling"
            return False
                #  The sampling given in the GUI will be the oversampled one!
        new_arg = rc.Param("--healpix_order ",integerToString(sampling - iover))

        #  Manually input local angular searches
        if joboptions["do_local_ang_searches"].getBoolean():
            new_arg = rc.Param("--sigma_ang " + floatToString(joboptions["sigma_angles"].getNumber(error_message) / 3.))
            # if joboptions["relax_sym"].length() > 0:
            new_arg = rc.Param("--relax_sym ", "relax_sym",assertion="required")
            cli.args.append(new_arg)

        if error_message != "":
            return False
        
        #  Offset range
        new_arg = rc.Param("--offset_range ", "offset_range")
        cli.args.append(new_arg)
        #  The sampling given in the GUI will be the oversampled one!
        new_arg = rc.Param("--offset_step " +  floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover)))
        if error_message != "":
            return False

        # if joboptions["allow_coarser"].getBoolean():
        new_arg = rc.Flag("--allow_coarser_sampling","","allow_coarser",True)
        cli.args.append(new_arg)    

    #  Provide symmetry, and always do norm and scale correction
    if not is_continue:
        new_arg = rc.Param("--sym ", "sym_name")
        cli.args.append(new_arg)
        new_arg = rc.Param("--norm --scale ","")
        cli.args.append(new_arg)
    
    if  (not is_continue) and (joboptions["do_helix"].getBoolean()) :
        label += ".helical"

        new_arg = rc.Param("--helix","")

        inner_diam = joboptions["helical_tube_inner_diameter"].getNumber(error_message)
        if error_message != "":
            return False
        if inner_diam > 0.:
            new_arg = rc.Param("--helical_inner_diameter ", "helical_tube_inner_diameter")
            cli.args.append(new_arg)

        new_arg = rc.Param("--helical_outer_diameter ", "helical_tube_outer_diameter")
        cli.args.append(new_arg)
        # if joboptions["do_apply_helical_symmetry"].getBoolean():
        new_arg = rc.Flag("--helical_nr_asu ", "helical_nr_asu","do_apply_helical_symmetry",True)
        cli.args.append(new_arg)
        new_arg = rc.Param("--helical_twist_initial ", "helical_twist_initial")
        cli.args.append(new_arg)
        new_arg = rc.Param("--helical_rise_initial ", "helical_rise_initial")
        cli.args.append(new_arg)

        myz = joboptions["helical_z_percentage"].getNumber(error_message) / 100.
        if error_message != "":
            return False
        
        new_arg = rc.Param("--helical_z_percentage ",floatToString(myz))
        cli.args.append(new_arg)

        if joboptions["do_local_search_helical_symmetry"].getBoolean():
            new_arg = rc.Param("--helical_symmetry_search","")
            cli.args.append(new_arg)
            new_arg = rc.Param("--helical_twist_min ", "helical_twist_min")
            cli.args.append(new_arg)
            new_arg = rc.Param("--helical_twist_max ", "helical_twist_max")
            cli.args.append(new_arg)

            twist_inistep = joboptions["helical_twist_inistep"].getNumber(error_message)
            if error_message != "":
                return False
            if twist_inistep > 0.:
                new_arg = rc.Param("--helical_twist_inistep ", "helical_twist_inistep")
                cli.args.append(new_arg)

                new_arg = rc.Param("--helical_rise_min ", "helical_rise_min")
                cli.args.append(new_arg)
                new_arg = rc.Param("--helical_rise_max ", "helical_rise_max")
                cli.args.append(new_arg)

                rise_inistep = joboptions["helical_rise_inistep"].getNumber(error_message)
                if error_message != "":
                    return False
                if rise_inistep > 0.:
                    new_arg = rc.Param("--helical_rise_inistep ", "helical_rise_inistep")
                    cli.args.append(new_arg)
                else:
                    new_arg = rc.Param("--ignore_helical_symmetry","")

        # if joboptions["keep_tilt_prior_fixed"].getBoolean():
        new_arg = rc.Param("--helical_keep_tilt_prior_fixed","","keep_tilt_prior_fixed",True)
        if  (joboptions["dont_skip_align"].getBoolean()) and (not joboptions["do_local_ang_searches"].getBoolean()):
            val = joboptions["range_tilt"].getNumber(error_message)
            if error_message != "":
                return False
            
            val = 0. if val < 0. else val
            val = 90. if val > 90. else val
            new_arg = rc.Param("--sigma_tilt ",floatToString(val / 3.))

            val = joboptions["range_psi"].getNumber(error_message)
            if error_message != "":
                return False
            
            val = 0. if val < 0. else val
            val = 90. if val > 90. else val
            new_arg = rc.Param("--sigma_psi ", floatToString(val / 3.))

            val = joboptions["range_rot"].getNumber(error_message)
            if error_message != "":
                return False
            
            val = 0. if val < 0. else val
            val = 90. if val > 90. else val
            new_arg = rc.Param("--sigma_rot ", floatToString(val / 3.))

            val = joboptions["helical_range_distance"].getNumber(error_message)
            if error_message != "":
                return False
            if val > 0.:
                new_arg = rc.Param("--helical_sigma_distance ", floatToString(val / 3.))
            
    #  Running stuff
    new_arg = rc.Param("--j ", "nr_threads")
    cli.args.append(new_arg)

    #  GPU-stuff
    # if joboptions["use_gpu"].getBoolean())
    if not joboptions["dont_skip_align"].getBoolean():
        error_message = "ERROR: you cannot use GPUs when skipping image alignments."
        return False
    new_arg = rc.Param("--gpu", "gpu_ids","use_gpu",True)
    cli.args.append(new_arg)
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return script

def getCommandsAutorefineJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    rc.Prog("`which relion_refine_mpi`","use_mpi",True)
    rc.Prog("`which relion_refine`","use_mpi",False)

    fn_run = "run"
    if is_continue:
        if joboptions["fn_cont"] == "":
            error_message = "ERROR: empty field for continuation STAR file..."
            return False
        
        pos_it = joboptions["fn_cont"].rfind("_it")
        pos_op = joboptions["fn_cont"].rfind("_optimiser")
        if pos_it < 0 or pos_op < 0:
            error_message = "Invalid optimiser.star filename provided for auto-refine continuation run: ", "fn_cont"
            return False
        
        #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
        # int it = (int)textToFloat((joboptions["fn_cont"].substr(pos_it+3, 6)).c_str())
        # fn_run += "_ct" + floatToString(it)
        new_arg = rc.Param("--continue ", "fn_cont")
        cli.args.append(new_arg)

    
    new_arg = rc.Param("--o ", outputname + fn_run)
    cli.args.append(new_arg)
    #  TODO: add bodies!! (probably in next version)
    outputNodes = getOutputNodesRefine(outputname + fn_run, "Refine3D", -1, 1, 3, 1, is_tomo)

    if is_tomo:
        label += ".tomo"

    if not is_continue:
        new_arg = rc.Param("--auto_refine --split_random_halves")

        if is_tomo:
            error_message = getTomoInputCommmand(true, command, HAS_COMPULSORY, HAS_COMPULSORY, HAS_NOT, HAS_NOT)
            if error_message != "":
                return False

            node1 = rc.Node( outputname + fn_run + "_optimisation_set.star", rh.LABEL_REFINE3D_OPTSET)
            cli.add_outnode(node1)

            sigma = joboptions["sigma_tilt"].getNumber(error_message)
            if error_message != "":
                return False
            if sigma > 0.:
                new_arg = rc.Param("--sigma_tilt ", "sigma_tilt")
                cli.args.append(new_arg)
            
            else:
                if joboptions["fn_img"] == "":
                    error_message = "ERROR: empty field for input STAR file..."
                    return False
                else:
                    new_arg = rc.Param("--i ", "fn_img")
                    cli.args.append(new_arg)
                node = rc.Node(joboptions["fn_img"].getString(), joboptions["fn_img"].node_type)
                cli.add_innode(node)
                    
        if joboptions["fn_ref"] == "":
            error_message = "ERROR: empty field for input reference..."
            return False
        else:
            new_arg = rc.Param("--ref ", "fn_ref")
            cli.args.append(new_arg)
            if joboptions["fn_ref"] != "None":
                node = rc.Node(joboptions["fn_ref"].getString(), joboptions["fn_ref"].node_type)
                cli.add_innode(node)
                # if not joboptions["ref_correct_greyscale"].getBoolean():
                new_arg = rc.Param("--firstiter_cc","","ref_correct_greyscale",False)

            if joboptions["trust_ref_size"].getBoolean():
                new_arg = rc.Param("--trust_ref_size","","trust_ref_size")

                # if joboptions["ini_high"].getNumber(error_message) > 0.:
                #     if error_message != "":
                #         return False
                new_arg = rc.Param("--ini_high ", "ini_high",assertion="is_positive")
                cli.args.append(new_arg)
        
    
    if joboptions["do_blush"].getBoolean():
        new_arg = rc.Param("--blush ","","do_blush",True)
    
    #  Always do compute stuff
#   if not joboptions["do_combine_thru_disc"].getBoolean())
    new_arg = rc.Flag("--dont_combine_weights_via_disc","","do_combine_thru_disc",False)
#   if not joboptions["do_parallel_discio"].getBoolean())
    new_arg = rc.Flag("--no_parallel_disc_io","","do_parallel_discio",False)
#   if joboptions["do_preread_images"].getBoolean())
    new_arg = rc.Flag("--preread_images ", "","do_preread_images", True)
#    elif joboptions["scratch_dir"] != "")
    new_arg = rc.Flag("--scratch_dir ","scratch_dir","scratch_dir",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--pool ", "nr_pool")
    cli.args.append(new_arg)
    new_arg = rc.Param("--pad","1","do_pad1",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--pad","2", "do_pad1", False)
    cli.args.append(new_arg)
    
    # if joboptions["auto_faster"].getBoolean():
    new_arg = rc.Param("--auto_ignore_angles --auto_resol_angles","","auto_faster",True)
    
    #  CTF stuff
    if not is_continue:
        # if joboptions["do_ctf_correction"].getBoolean())
        new_arg = rc.Param("--ctf","","do_ctf_correction",True)
        #    if joboptions["ctf_intact_first_peak"].getBoolean())
        new_arg = rc.Param("--ctf_intact_first_peak","","ctf_intact_first_peak",True)
            
    #  Optimisation
    new_arg = rc.Param("--particle_diameter ", "particle_diameter")
    cli.args.append(new_arg)
#    if !is_continue)
    #  Always flatten the solvent
    new_arg = rc.Param("--flatten_solvent","")
#   if joboptions["do_zero_mask"].getBoolean())
    new_arg = rc.Flag("--zero_mask","do_zero_mask",True)
#   if joboptions["fn_mask"].length() > 0)
    new_arg = rc.Param("--solvent_mask ", "fn_mask",assertion="required")
    cli.args.append(new_arg)

#   if joboptions["do_solvent_fsc"].getBoolean())
    new_arg = rc.Param("--solvent_correct_fsc ","","do_solvent_fsc",True)
    cli.args.append(new_arg)

    node = rc.Node(joboptions["fn_mask"].getString(), joboptions["fn_mask"].node_type)
    cli.add_innode(node)
    
#    if !is_continue)
    #  Sampling
    iover = 1
    new_arg = rc.Param("--oversampling ",iover)

    sampling = getHealPixOrder(joboptions["sampling"])
    if sampling <= 0:
        error_message = "Wrong choice for sampling"
        return False
    #  The sampling given in the GUI will be the oversampled one!
    new_arg = rc.Param("--healpix_order ",integerToString(sampling - iover))

    #  Minimum sampling rate to perform local searches (may be changed upon continuation
    auto_local_sampling = getHealPixOrder(joboptions["auto_local_sampling"])
    if auto_local_sampling <= 0:
        error_message = "Wrong choice for auto_local_sampling"
        return False
    #  The sampling given in the GUI will be the oversampled one!
    new_arg = rc.Param("--auto_local_healpix_order " ,integerToString(auto_local_sampling - iover))

    #  Offset range
    new_arg = rc.Param("--offset_range ", "offset_range")
    cli.args.append(new_arg)
    #  The sampling given in the GUI will be the oversampled one!
    new_arg = rc.Param("--offset_step ",floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover)))
    if error_message != "":
        return False

    new_arg = rc.Param("--sym ", "sym_name")
    cli.args.append(new_arg)
    #  Always join low-res data, as some D&I point group refinements may fall into different hands!
    new_arg = rc.Param("--low_resol_join_halves","40")
    new_arg = rc.Param("--norm --scale ","")

    #  Helix
    if joboptions["do_helix"].getBoolean():
        label += ".helical"

        new_arg = rc.Param("--helix","")

        inner_diam = joboptions["helical_tube_inner_diameter"].getNumber(error_message)
        if error_message != "":
            return False
            if inner_diam > 0.:
                new_arg = rc.Param("--helical_inner_diameter ", "helical_tube_inner_diameter")
                cli.args.append(new_arg)

            new_arg = rc.Param("--helical_outer_diameter ", "helical_tube_outer_diameter")
            cli.args.append(new_arg)
            if joboptions["do_apply_helical_symmetry"].getBoolean():
                new_arg = rc.Param("--helical_nr_asu ", "helical_nr_asu")
                cli.args.append(new_arg)
                new_arg = rc.Param("--helical_twist_initial ", "helical_twist_initial")
                cli.args.append(new_arg)
                new_arg = rc.Param("--helical_rise_initial ", "helical_rise_initial")
                cli.args.append(new_arg)

                myz = joboptions["helical_z_percentage"].getNumber(error_message) / 100.
                if error_message != "":
                    return False
                new_arg = rc.Param("--helical_z_percentage ",floatToString(myz))

                if joboptions["do_local_search_helical_symmetry"].getBoolean():
                    new_arg = rc.Param("--helical_symmetry_search","")
                    new_arg = rc.Param("--helical_twist_min ", "helical_twist_min")
                    cli.args.append(new_arg)
                    new_arg = rc.Param("--helical_twist_max ", "helical_twist_max")
                    cli.args.append(new_arg)

                    twist_inistep = joboptions["helical_twist_inistep"].getNumber(error_message)
                    if error_message != "":
                        return False
                    if twist_inistep > 0.:
                        new_arg = rc.Param("--helical_twist_inistep ", "helical_twist_inistep")
                        cli.args.append(new_arg)

                    new_arg = rc.Param("--helical_rise_min ", "helical_rise_min")
                    cli.args.append(new_arg)
                    new_arg = rc.Param("--helical_rise_max ", "helical_rise_max")
                    cli.args.append(new_arg)

                    rise_inistep = joboptions["helical_rise_inistep"].getNumber(error_message)
                    if error_message != "":
                        return False
                    if rise_inistep > 0.:
                        new_arg = rc.Param("--helical_rise_inistep ", "helical_rise_inistep")
                        cli.args.append(new_arg)
                    else:
                        new_arg = rc.Param("--ignore_helical_symmetry","")

            val = 0
            if sampling != auto_local_sampling:
                val = joboptions["range_tilt"].getNumber(error_message)
                if error_message != "":
                    return False
                val =  0. if val < 0. else val
                val = 90. if val > 90. else val
                new_arg = rc.Param("--sigma_tilt ", floatToString(val / 3.))

                val = joboptions["range_psi"].getNumber(error_message)
                if error_message != "":
                    return False
                val =  0. if val < 0. else val
                val = 90. if val > 90. else val
                new_arg = rc.Param("--sigma_psi ", floatToString(val / 3.))

                val = joboptions["range_rot"].getNumber(error_message)
                if error_message != "":
                    return False
                val =  0. if val < 0. else val
                val = 90. if val > 90. else val
                new_arg = rc.Param("--sigma_rot ", floatToString(val / 3.))
            
            val = joboptions["helical_range_distance"].getNumber(error_message)
            if error_message != "":
                return False
            if val > 0.:
                new_arg = rc.Param("--helical_sigma_distance ", floatToString(val / 3.))

            # if joboptions["keep_tilt_prior_fixed"].getBoolean():
            new_arg = rc.Param("--helical_keep_tilt_prior_fixed","","keep_tilt_prior_fixed", True)
            
    if joboptions["relax_sym"].length() > 0:
        new_arg = rc.Param("--relax_sym ", "relax_sym")
        cli.args.append(new_arg)

    #  Running stuff
    new_arg = rc.Param("--j ", "nr_threads")
    cli.args.append(new_arg)

    #  GPU-stuff
    # if joboptions["use_gpu"].getBoolean())
    new_arg = rc.Flag("--gpu", "gpu_ids","use_gpu",True)
    cli.args.append(new_arg)
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return script

def getCommandsMultiBodyJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    if not exists(joboptions["fn_bodies"]):
        error_message = "ERROR: you have to specify an existing body STAR file."
        return False
    
    if is_continue and joboptions["fn_cont"] == "" and not joboptions["do_analyse"].getBoolean():
        error_message = "ERROR: either specify a optimiser file to continue multibody refinement from OR run flexibility analysis..."
        return False
    
    fn_run = ""
    if not is_continue or (is_continue and joboptions["fn_cont"] != ""):
        if joboptions["nr_mpi"].getNumber(error_message) > 1:
            command="`which relion_refine_mpi`"
        else:
            command="`which relion_refine`"
        if error_message != "":
            return False

        MD = None # MetaDataTable
        MD.read(joboptions["fn_bodies"])
        nr_bodies = MD.numberOfObjects()

        if is_continue:
            pos_it = joboptions["fn_cont"].rfind("_it")
            pos_op = joboptions["fn_cont"].rfind("_optimiser")
            if pos_it < 0 or pos_op < 0:
                err = 'std::cerr << "Warning: invalid optimiser.star filename provided for continuation run: " << joboptions["fn_cont"]<< std::endl'
            it = textToFloat((joboptions["fn_cont"].substr(pos_it+3, 6)).c_str())
            fn_run = "run_ct" + floatToString(it)
            new_arg = rc.Param("--continue ", "fn_cont")
            cli.args.append(new_arg)
            new_arg = rc.Param("--o ", outputname + fn_run)
            outputNodes = getOutputNodesRefine(outputname + fn_run, "MultiBody", -1, 1, 3, nr_bodies, is_tomo)

        else:
            fn_run = "run"
            new_arg = rc.Param("--continue ", "fn_in")
            cli.args.append(new_arg)
            new_arg = rc.Param("--o ", outputname + fn_run)
            cli.args.append(new_arg)
            outputNodes = getOutputNodesRefine(outputname + "run", "MultiBody", -1, 1, 3, nr_bodies, is_tomo)
            new_arg = rc.Param("--solvent_correct_fsc --multibody_masks ", "fn_bodies")
            cli.args.append(new_arg)

            node = rc.Node(joboptions["fn_in"].getString(), rh.LABEL_REFINE3D_OPT)
            cli.add_innode(node)

            #  Sampling
            iover = 1
            new_arg = rc.Param("--oversampling ", floatToString(iover))
            sampling = getHealPixOrder(joboptions["sampling"])
            if sampling <= 0:
                error_message = "Wrong choice for sampling"
                return False
            #  The sampling given in the GUI will be the oversampled one!
            new_arg = rc.Param("--healpix_order ", integerToString(sampling - iover))
            cli.args.append(new_arg)
            #  Always perform local searches!
            new_arg = rc.Param("--auto_local_healpix_order ", integerToString(sampling - iover))
            cli.args.append(new_arg)
            #  Offset range
            new_arg = rc.Param("--offset_range ", "offset_range")
            cli.args.append(new_arg)
            #  The sampling given in the GUI will be the oversampled one!
            new_arg = rc.Param("--offset_step " + floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover)))
            if error_message != "":
                return False
        
        # if joboptions["do_blush"].getBoolean():
        new_arg = rc.Param("--blush ","","do_blush",True)

        # if joboptions["do_subtracted_bodies"].getBoolean())
        new_arg = rc.Param("--reconstruct_subtracted_bodies ", "", "do_subtracted_bodies", True)

    #  Always do compute stuff
#   if not joboptions["do_combine_thru_disc"].getBoolean())
    new_arg = rc.Flag("--dont_combine_weights_via_disc","","do_combine_thru_disc",False)
#   if not joboptions["do_parallel_discio"].getBoolean())
    new_arg = rc.Flag("--no_parallel_disc_io","","do_parallel_discio",False)
#   if joboptions["do_preread_images"].getBoolean())
    new_arg = rc.Flag("--preread_images ", "","do_preread_images", True)
#    elif joboptions["scratch_dir"] != "")
    new_arg = rc.Flag("--scratch_dir ","scratch_dir","scratch_dir",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--pool ", "nr_pool")
    cli.args.append(new_arg)
    new_arg = rc.Param("--pad","1","do_pad1",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--pad","2", "do_pad1", False)
    cli.args.append(new_arg)
    

    #  Running stuff
    new_arg = rc.Param("--j ", "nr_threads")
    cli.args.append(new_arg)

    #  GPU-stuff
    # if joboptions["use_gpu"].getBoolean())
    new_arg = rc.Param("--gpu", "gpu_ids","use_gpu",True)
    cli.args.append(new_arg)
        
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

     #  end if !is_continue or (is_continue and joboptions["fn_cont"]!= "")

    if joboptions["do_analyse"].getBoolean():
        cli.add_prog(rc.Prog("`which relion_flex_analyse`"))

        #  If we had performed relion_refine command, then fn_run would be set now
        #  Otherwise, we have to search for _model.star files that do NOT have a _it??? specifier
        if fn_run == "":
            fn_wildcard = outputname + "run*_model.star"
            fns_model = [] # std::vector<FileName> 
            fns_ok = '' # std::vector<FileName> 
            fn_wildcard.globFiles(fns_model)
            for i in range(len(fns_model)):
                if not fns_model[i].contains("_it"):
                    fns_ok.push_back(fns_model[i])
                    if fns_ok.size() == 0:
                        error_message = "ERROR: cannot find appropriate model.star file in the output directory"
                        return False
                    if fns_ok.size() > 1:
                        error_message = "ERROR: there are more than one model.star files (without '_it' specifiers) in the output directory. Move all but one out of the way."
                        return False
                    fn_run = fns_ok[0].beforeFirstOf("_model.star")
                else:
                    fn_run = outputname + fn_run

        #  General I/O
        new_arg = rc.Param("--PCA_orient ","")
        new_arg = rc.Param("--model ",fn_run + "_model.star")
        new_arg = rc.Param("--data ", fn_run + "_data.star")
        new_arg = rc.Param("--bodies ", "fn_bodies")
        cli.args.append(new_arg)
        new_arg = rc.Param("--o ",outputname + "analyse")

        #  Eigenvector movie maps
        # if joboptions["nr_movies"].getNumber(error_message) > 0:
        new_arg = rc.Param("--do_maps ","","nr_movies",assertion="is_positive")
        cli.args.append(new_arg)
        new_arg = rc.Param("--k ", "nr_movies",assertion="is_positive")
        cli.args.append(new_arg)
        if error_message != "":
            return False

        #  Selection
        if joboptions["do_select"].getBoolean():
            minval = joboptions["eigenval_min"].getNumber(error_message)
            if error_message != "":
                return False

            maxval = joboptions["eigenval_max"].getNumber(error_message)
            if error_message != "":
                return False

            if  minval >= maxval:
                error_message = "ERROR: the maximum eigenvalue should be larger than the minimum one!"
                return False
            
            new_arg = rc.Param("--select_eigenvalue ", "select_eigenval")
            cli.args.append(new_arg)
            new_arg = rc.Param("--select_eigenvalue_min ", "eigenval_min")
            cli.args.append(new_arg)
            new_arg = rc.Param("--select_eigenvalue_max ", "eigenval_max")
            cli.args.append(new_arg)

            #  Add output node: selected particles star file
            fnt = outputname + "analyse_eval" + integerToString(joboptions["select_eigenval"].getNumber(error_message),3)+"_select"
            if error_message != "":
                return False

            min = ROUND(joboptions["eigenval_min"].getNumber(error_message))
            if error_message != "":
                return False

            max = ROUND(joboptions["eigenval_max"].getNumber(error_message))
            if error_message != "":
                return False

            if min > -99998:
                fnt += "_min"+integerToString(min)
            if max < 99998:
                fnt += "_max"+integerToString(max)
            fnt += ".star"
            node2 = rc.Node (fnt, rh.LABEL_MULTIBODY_SEL_PARTS)
            cli.add_outnode(node2)

        
        #  PDF with histograms of the eigenvalues
        node3 = rc.Node (outputname + "analyse_logfile.pdf", rh.LABEL_MULTIBODY_FLEXLOG)
        cli.add_outnode(node3)

    return script

def getCommandsMaskcreateJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    command="`which relion_mask_create`"

    #  I/O
    # if joboptions["fn_in"] == "":
    #     error_message = "ERROR: empty field for input STAR file..."
    #     return False
    new_arg = rc.Param("--i ", "fn_in",assertion="required")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["fn_in"].getString(), joboptions["fn_in"].node_type)
    cli.add_innode(node)

    new_arg = rc.Param("--o ",outputname + "mask.mrc")
    cli.args.append(new_arg)

    node2 = rc.Node (outputname + "mask.mrc", rh.LABEL_MASK3D_MASK)
    cli.add_outnode(node2)

    # if joboptions["lowpass_filter"].getNumber(error_message) > 0:
    new_arg = rc.Param("--lowpass ", "lowpass_filter",assertion="is_positive")
    cli.args.append(new_arg)
    if error_message != "":
        return False

    # if joboptions["angpix"].getNumber(error_message) > 0:
    new_arg = rc.Param("--angpix ", "angpix",assertion="is_positive")
    cli.args.append(new_arg)
    if error_message != "":
        return False

    new_arg = rc.Param("--ini_threshold ", "inimask_threshold")
    cli.args.append(new_arg)
    new_arg = rc.Param("--extend_inimask ", "extend_inimask")
    cli.args.append(new_arg)
    new_arg = rc.Param("--width_soft_edge ", "width_mask_edge")
    cli.args.append(new_arg)

    if joboptions["do_helix"].getBoolean():
        new_arg = rc.Param("--helix --z_percentage ", joboptions["helical_z_percentage"].getNumber(error_message) / 100.)
        if error_message != "":
            return False
    
    #  Running stuff
    new_arg = rc.Param("--j ", "nr_threads")
    cli.args.append(new_arg)

    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return script

def getCommandsJoinstarJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    command="`which relion_star_handler`"

    ii = 0
    if joboptions["do_part"].getBoolean():
        ii += 1
        label += ".particles"
    if joboptions["do_mic"].getBoolean():
        ii += 1
        label += ".micrographs"
    if joboptions["do_mov"].getBoolean():
        ii += 1
        label += ".movies"
    
    if ii == 0:
        error_message = "You've selected no type of files for joining. Select a single type!"
        return False
    
    if ii > 1:
        error_message = "You've selected more than one type of files for joining. Only select a single type!"
        return False
    
    #  I/O
    if joboptions["do_part"].getBoolean():
        if joboptions["fn_part1"] == "" or joboptions["fn_part2"]== "":
            error_message = "ERROR: empty field for first or second input STAR file..."
            return False
        new_arg = rc.Param("--combine --i \" ", "fn_part1")
        cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_part1"].getString(), joboptions["fn_part1"].node_type)
        cli.add_innode(node)
        new_arg = rc.Param(" ", "fn_part2")
        cli.args.append(new_arg)
        node2 = rc.Node(joboptions["fn_part2"].getString(), joboptions["fn_part2"].node_type)
        cli.add_innode(node2)
        if joboptions["fn_part3"] != "":
            new_arg = rc.Param(" ", "fn_part3")
            cli.args.append(new_arg)
            node3 = rc.Node(joboptions["fn_part3"], joboptions["fn_part3"].node_type)
            cli.add_innode(node3)
        if joboptions["fn_part4"] != "":
            new_arg = rc.Param(" ", "fn_part4")
            cli.args.append(new_arg)
            node4 = rc.Node(joboptions["fn_part4"].getString(), joboptions["fn_part4"].node_type)
            cli.add_innode(node4)
            # new_arg = rc.Param(" \" "

        #  Check for duplicates
        new_arg = rc.Param("--check_duplicates rlnImageName ","")
        new_arg = rc.Param("--o ", outputname + "join_particles.star")
        node5 = rc.Node (outputname + "join_particles.star", joboptions["fn_part1"].node_type)
        cli.add_outnode(node5)

    elif joboptions["do_mic"].getBoolean():
        if joboptions["fn_mic1"] == "" or joboptions["fn_mic2"] == "":
            error_message = "ERROR: empty field for first or second input STAR file..."
            return False
        new_arg = rc.Param("--combine --i \" ", "fn_mic1")
        cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_mic1"].getString(), joboptions["fn_mic1"].node_type)
        cli.add_innode(node)
        new_arg = rc.Param(" ", "fn_mic2")
        cli.args.append(new_arg)
        node2 = rc.Node(joboptions["fn_mic2"].getString(), joboptions["fn_mic2"].node_type)
        cli.add_innode(node2)
        if joboptions["fn_mic3"] != "":
            new_arg = rc.Param(" ", "fn_mic3")
            cli.args.append(new_arg)
            node3 = rc.Node(joboptions["fn_mic3"].getString(), joboptions["fn_mic3"].node_type)
            cli.add_innode(node3)
        if joboptions["fn_mic4"] != "":
            new_arg = rc.Param(" ", "fn_mic4")
            cli.args.append(new_arg)
            node4 = rc.Node(joboptions["fn_mic4"].getString(), joboptions["fn_mic4"].node_type)
            cli.add_innode(node4)
            # new_arg = rc.Param(" \" "

        #  Check for duplicates
        new_arg = rc.Param("--check_duplicates rlnMicrographName ","")
        new_arg = rc.Param("--o ", outputname + "join_mics.star")
        node5 = rc.Node(outputname + "join_mics.star", joboptions["fn_mic1"].node_type)
        cli.add_outnode(node5)

    elif joboptions["do_mov"].getBoolean():
        if joboptions["fn_mov1"] == "" or joboptions["fn_mov2"] == "":
            error_message = "ERROR: empty field for first or second input STAR file..."
            return False
        new_arg = rc.Param("--combine --i \" ", "fn_mov1")
        cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_mov1"].getString(), joboptions["fn_mov1"].node_type)
        cli.add_innode(node)
        new_arg = rc.Param(" ", "fn_mov2")
        cli.args.append(new_arg)
        node2 = rc.Node (joboptions["fn_mov2"].getStrin(), joboptions["fn_mov2"].node_type)
        cli.add_innode(node2)
        if joboptions["fn_mov3"] != "":
            new_arg = rc.Param(" ", "fn_mov3")
            cli.args.append(new_arg)
            node3 = rc.Node(joboptions["fn_mov3"].getString(), joboptions["fn_mov3"].node_type)
            cli.add_innode(node3)
        if joboptions["fn_mov4"] != "":
            new_arg = rc.Param(" ", "fn_mov4")
            cli.args.append(new_arg)
            node4 = rc.Node(joboptions["fn_mov4"].getString(), joboptions["fn_mov4"].node_type)
            cli.add_innode(node4)
            # new_arg = rc.Param(" \" "

        #  Check for duplicates
        new_arg = rc.Param("--check_duplicates rlnMicrographMovieName ","")
        new_arg = rc.Param("--o ", outputname + "join_movies.star")
        node5 = rc.Node(outputname + "join_movies.star", joboptions["fn_mov1"].node_type)
        cli.add_outnode(node5)
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return script

def getCommandsSubtractJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    if joboptions["do_fliplabel"].getBoolean():
        if joboptions["nr_mpi"].getNumber(error_message) > 1:
            error_message = "You cannot use MPI parallelization to revert particle labels."
            return False
        
        node = rc.Node(joboptions["fn_fliplabel"].getString(), joboptions["fn_fliplabel"].node_type)
        cli.add_innode(node)

        node2 = rc.Node(outputname + "original.star", rh.LABEL_SUBTRACT_REVERTED)
        cli.add_outnode(node2)

        label += ".revert"

        cli.add_prog(rc.Prog("`which relion_particle_subtract`"))
        new_arg = rc.Param("--revert ", "fn_fliplabel")
        cli.args.append(new_arg) + "--o " + outputname
    else:
        if joboptions["nr_mpi"].getNumber(error_message) > 1:
            command="`which relion_particle_subtract_mpi`"
        else:
            command="`which relion_particle_subtract`"
        if error_message != "":
            return False

        #  I/O
        if joboptions["fn_opt"] == "":
            error_message = "ERROR: empty field for input optimiser.star..."
            return False
        new_arg = rc.Param("--i ", "fn_opt")
        cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_opt"].getString(), rh.LABEL_OPTIMISER_CPIPE)
        cli.add_innode(node)

        if joboptions["fn_mask"] != "":
            new_arg = rc.Param("--mask ", "fn_mask")
            cli.args.append(new_arg)
            node2 = rc.Node(joboptions["fn_mask"].getString(), joboptions["fn_mask"].node_type)
            cli.add_innode(node2)
            if joboptions["do_data"].getBoolean():
                if joboptions["fn_data"] == "":
                    error_message = "ERROR: empty field for the input particle STAR file..."
                    return False
            new_arg = rc.Flag("--data ", "fn_data","do_data",True,assertion="required")
            cli.args.append(new_arg)
            node3 = rc.Node (joboptions["fn_data"].getString(), joboptions["fn_data"].node_type)
            cli.add_innode(node3)
        
        new_arg = rc.Param("--o ", outputname)
        node4 = rc.Node(outputname + "particles_subtracted.star", rh.LABEL_SUBTRACT_SUBTRACTED)
        cli.add_outnode(node4)

        if joboptions["do_center_mask"].getBoolean():
            new_arg = rc.Param("--recenter_on_mask","")
        elif joboptions["do_center_xyz"].getBoolean():
            new_arg = rc.Param("--center_x ", "center_x")
            cli.args.append(new_arg)
            new_arg = rc.Param("--center_y ", "center_y")
            cli.args.append(new_arg)
            new_arg = rc.Param("--center_z ", "center_z")
            cli.args.append(new_arg)
        
        # if joboptions["do_float16"].getBoolean():
        new_arg = rc.Flag("--float16 ","","do_float16",True)
        
        if joboptions["new_box"].getNumber(error_message) > 0:
            new_arg = rc.Param("--new_box ", "new_box")
            cli.args.append(new_arg)
            if error_message != "":
                return False

    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return script

def getCommandsPostprocessJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    command="`which relion_postprocess`"

    #  Input mask
    if joboptions["fn_mask"]  == "":
        error_message = "ERROR: empty field for input mask..."
        return False
    new_arg = rc.Param("--mask ", "fn_mask")
    cli.args.append(new_arg)
    node3 = rc.Node (joboptions["fn_mask"].getString(), joboptions["fn_mask"].node_type)
    cli.add_innode(node3)

    #  Input half map (one of them)
    fn_half1 = joboptions["fn_in"]
    fn_half2 = ''

    if fn_half1 == "":
        error_message = "ERROR: empty field for input half-map..."
        return False
    
    if fn_half1 != "":
        if not fn_half1.getTheOtherHalf(fn_half2):
            error_message = "ERROR: cannot find 'half' substring in the input filename..."
            return False
        
        node = rc.Node (fn_half1, joboptions["fn_in"].node_type)
        cli.add_innode(node)
        new_arg = rc.Param("--i ", fn_half1)
    
    #  The output name contains a directory: use it for output
    new_arg = rc.Param("--o ", outputname + "postprocess")
    cli.args.append(new_arg)
    new_arg = rc.Param("  --angpix ", "angpix")
    cli.args.append(new_arg)
    node1 = rc.Node(outputname+"postprocess.mrc", rh.LABEL_POST_MAP)
    cli.add_outnode(node1)
    node2 = rc.Node(outputname+"postprocess_masked.mrc", rh.LABEL_POST_MASKED)
    cli.add_outnode(node2)

    node2b = rc.Node(outputname+"logfile.pdf", rh.LABEL_POST_LOG)
    cli.add_outnode(node2b)

    node2c = rc.Node (outputname+"postprocess.star", rh.LABEL_POST_POST)
    cli.add_outnode(node2c)

    #  Sharpening
    if joboptions["fn_mtf"].length() > 0:
        new_arg = rc.Param("--mtf ", "fn_mtf")
        cli.args.append(new_arg)
        new_arg = rc.Param("--mtf_angpix ", "mtf_angpix")
        cli.args.append(new_arg)
        # if joboptions["do_auto_bfac"].getBoolean():
        new_arg = rc.Flag("--auto_bfac ","","do_auto_bfac",True)
        cli.args.append(new_arg)
        new_arg = rc.Param("--autob_lowres ", "autob_lowres")
        cli.args.append(new_arg)
        # if joboptions["do_adhoc_bfac"].getBoolean():
        new_arg = rc.Flag("--adhoc_bfac ", "adhoc_bfac","do_adhoc_bfac",True)
        cli.args.append(new_arg)
    
    #  Filtering
    # if joboptions["do_skip_fsc_weighting"].getBoolean())
    new_arg = rc.Flag("--skip_fsc_weighting ","","do_skip_fsc_weighting",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--low_pass " , "low_pass")
    cli.args.append(new_arg)
    
    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    return script

def getCommandsLocalresJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    if joboptions["do_resmap_locres"].getBoolean() == joboptions["do_relion_locres"].getBoolean():
        error_message = "ERROR: choose either ResMap or Relion for local resolution estimation"
        return False
    
    if joboptions["fn_in"] == "":
        error_message = "ERROR: empty field for input half-map..."
        return False
    
    #  Get the two half-reconstruction names from the single one
    fn_half1 = joboptions["fn_in"]
    fn_half2 = ''
    if fn_half1.getTheOtherHalf(fn_half2):
        error_message = "ERROR: cannot find 'half' substring in the input filename..."
        return False
    
    node = rc.Node(joboptions["fn_in"].getString(), joboptions["fn_in"].node_type)
    cli.add_innode(node)

    if joboptions["do_resmap_locres"].getBoolean():
        label += ".resmap"

        #  ResMap wrapper
        if joboptions["fn_resmap"].length() == 0:
            error_message = "ERROR: please provide an executable for the ResMap program."
            return False
        
        if joboptions["fn_mask"] == "":
            error_message = "ERROR: Please provide an input mask for ResMap local-resolution estimation."
            return False
        
        if joboptions["do_queue"].getBoolean():
            error_message = "ERROR: You cannot submit a ResMap job to the queue, as it needs user interaction."
            return False
        
        if joboptions["nr_mpi"].getNumber(error_message) > 1:
            error_message = "You cannot use more than 1 MPI processor for the ResMap wrapper..."
            return False
                
        if error_message != "":
            return False

        #  Make symbolic links to the half-maps in the output directory
        cli.add_prog(rc.Prog("ln -s ../../" + fn_half1 + " " + outputname + "half1.mrc"))
        cli.add_prog(rc.Prog("ln -s ../../" + fn_half2 + " " + outputname + "half2.mrc"))

        node2 = rc.Node(joboptions["fn_mask"].getString(), joboptions["fn_mask"].node_type)
        cli.add_innode(node2)

        node3 = rc.Node(outputname + "half1_resmap.mrc", rh.LABEL_LOCRES_RESMAP)
        cli.add_outnode(node3)

        command = joboptions["fn_resmap"]
        new_arg = rc.Param("--maskVol=", "fn_mask")
        cli.args.append(new_arg)
        new_arg = rc.Param("--noguiSplit ",outputname + "half1.mrc " +  outputname + "half2.mrc")
        new_arg = rc.Param("--vxSize=", "angpix")
        cli.args.append(new_arg)
        new_arg = rc.Param("--pVal=", "pval")
        cli.args.append(new_arg)
        new_arg = rc.Param("--minRes=", "minres")
        cli.args.append(new_arg)
        new_arg = rc.Param("--maxRes=", "maxres")
        cli.args.append(new_arg)
        new_arg = rc.Param("--stepRes=", "stepres")
        cli.args.append(new_arg)

    elif joboptions["do_relion_locres"].getBoolean():
        #  Relion postprocessing
        label += ".own"

        if joboptions["nr_mpi"].getNumber(error_message) > 1:
            command="`which relion_postprocess_mpi`"
        else:
            command="`which relion_postprocess`"
        if error_message != "":
            return False

        new_arg = rc.Param("--locres --i ", "fn_in")
        cli.args.append(new_arg)
        new_arg = rc.Param("--o ", outputname + "relion")
        new_arg = rc.Param("--angpix ", "angpix")
        cli.args.append(new_arg)
        # new_arg = rc.Param("--locres_sampling ", "locres_sampling")
        # cli.args.append(new_arg)
        # new_arg = rc.Param("--locres_randomize_at ", "randomize_at")
        # cli.args.append(new_arg)
        new_arg = rc.Param("--adhoc_bfac ", "adhoc_bfac")
        cli.args.append(new_arg)
        # if joboptions["fn_mtf"] != "":
        new_arg = rc.Param("--mtf ", "fn_mtf",assertion="required")
        cli.args.append(new_arg)

        if joboptions["fn_mask"] != "":
            new_arg = rc.Param("--mask ", "fn_mask")
            cli.args.append(new_arg)
            node0 = rc.Node (outputname+"histogram.pdf", rh.LABEL_LOCRES_LOG)
            cli.add_outnode(node0)
        
        node1 = rc.Node(outputname+"relion_locres_filtered.mrc", rh.LABEL_LOCRES_FILTMAP)
        cli.add_outnode(node1)
        node2 = rc.Node(outputname+"relion_locres.mrc", rh.LABEL_LOCRES_RESMAP)
        cli.add_outnode(node2)
    
    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    return script

def getCommandsDynaMightJob(outputname, label, job_counter):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    command = joboptions["fn_dynamight_exe"]

    if not is_continue:
        #  New jobs need to add the input nodes

        node = rc.Node(joboptions["fn_star"].getString(), joboptions["fn_star"].node_type)
        cli.add_innode(node)
        node2 = rc.Node (joboptions["fn_map"].getString(), joboptions["fn_map"].node_type)
        cli.add_innode(node2)
    #     /*
    #     if joboptions["fn_mask")
    # cli.args.append(new_arg) != "")
    #                 rc.Node node3(joboptions["fn_mask")
    # cli.args.append(new_arg), joboptions["fn_mask"].node_type)
    #         cli.add_innode(node3)
    #             */
    else:
        c = 0
        if joboptions["do_visualize"].getBoolean():
            c += 1
        if joboptions["do_inverse"].getBoolean():
            c += 1
        if joboptions["do_reconstruct"].getBoolean():
            c += 1
        if c == 0:
            error_message = "You need to select at least one task on one of the tabs..."
            return False
        if c > 1:
            error_message = "You can not perform more than one task simultaneously..."
            return False
            
    if not is_continue or not (joboptions["do_visualize"].getBoolean() or joboptions["do_inverse"].getBoolean() or joboptions["do_reconstruct"].getBoolean()):
        new_arg = rc.Param(" optimize-deformations ","")
        new_arg = rc.Param("--refinement-star-file ", "fn_star")
        cli.args.append(new_arg)
        new_arg = rc.Param("--output-directory ", outputname)
        new_arg = rc.Param("--initial-model ", "fn_map")
        cli.args.append(new_arg)
        new_arg = rc.Param("--n-gaussians ", "nr_gaussians")
        cli.args.append(new_arg)
        #if joboptions["initial_threshold"] != "":
        new_arg = rc.Param("--initial-threshold ", "initial_threshold",assertion="required")
        cli.args.append(new_arg)
        new_arg = rc.Param("--regularization-factor " , "reg_factor")
        cli.args.append(new_arg)
        new_arg = rc.Param("--n-threads ", "nr_threads")
        cli.args.append(new_arg)

        # if joboptions["do_preload"].getBoolean():
        new_arg = rc.Param("--preload-images ","","do_preload",True)

        # if joboptions["fn_mask"] != "")
        #     new_arg = rc.Param("--mask-file ", "fn_mask")
        # cli.args.append(new_arg)

    # elif joboptions["do_visualize"].getBoolean():
    new_arg = rc.Param(" explore-latent-space ",outputname,"do_visualize",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--half-set ", "halfset","do_visualize",True)
    cli.args.append(new_arg)

    #   if joboptions["fn_checkpoint"] != "")
    new_arg = rc.Param("--checkpoint-file ", "fn_checkpoint","do_visualize",True,assertion="required")
    cli.args.append(new_arg)

        # if joboptions["fn_mask"]!= "")
        #     new_arg = rc.Param("--mask-file ", "fn_mask")
        # cli.args.append(new_arg)
    #   elif joboptions["do_inverse"].getBoolean())
    new_arg = rc.Param(" optimize-inverse-deformations ", outputname,"do_inverse",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--n-epochs ", "nr_epochs")
    cli.args.append(new_arg)

    #    if joboptions["fn_checkpoint"] != "":
    new_arg = rc.Param("--checkpoint-file ", "fn_checkpoint",assertion="required")
    cli.args.append(new_arg)

    #   if joboptions["do_store_deform"].getBoolean())
    new_arg = rc.Flag("--save-deformations ","","do_store_deform",True)
    cli.args.append(new_arg)
    #   if joboptions["do_preload"].getBoolean())
    new_arg = rc.Flag("--preload-images","","do_preload",True)
    cli.args.append(new_arg)
    #   elif joboptions["do_reconstruct"].getBoolean())
    new_arg = rc.Flag(" deformable-backprojection ", outputname,"do_reconstruct",True)
    cli.args.append(new_arg)
    new_arg = rc.Param("--batch-size ", "backproject_batchsize")
    cli.args.append(new_arg)

    #    if joboptions["fn_checkpoint"] != "":
    new_arg = rc.Param("--checkpoint-file ", "fn_checkpoint",assertion="required")
    cli.args.append(new_arg)

    #    if joboptions["do_preload"].getBoolean())
    new_arg = rc.Flag("--preload-images","","do_preload",True)
    cli.args.append(new_arg)

        # if joboptions["fn_mask"] != "")
        #     new_arg = rc.Param("--mask-file ", "fn_mask")
        #     cli.args.append(new_arg)

    onode = rc.Node (outputname + "backprojection/map_half1.mrc", rh.LABEL_DYNAMIGHT_HALFMAP)
    cli.add_outnode(onode)
    onode2 = rc.Node (outputname + "backprojection/map_half2.mrc", rh.LABEL_DYNAMIGHT_HALFMAP)
    cli.add_outnode(onode2)

    
    # if joboptions["gpu_id"] != "")
    new_arg = rc.Param("--gpu-id ", "gpu_id",assertion="required")
    cli.args.append(new_arg)

    #  Other arguments for model_angelo
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    #  Besides

    # return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message, true)
    return script

def getCommandsModelAngeloJob(outputname, label, job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)

    outputmodel = outputname
    outputmodel = (outputmodel.afterFirstOf("/")).beforeLastOf("/")
    outputmodel = outputname + outputmodel + ".cif"

    #  Only run model building for new job or if output.cif is not there yet.
    if not is_continue or not exists(outputmodel):
        #  Run on a map
        node = rc.Node(joboptions["fn_map"].getString(), joboptions["fn_map"].node_type)
        cli.add_innode(node)

    cli.add_prog(rc.Prog(joboptions["fn_modelangelo_exe"]))
    cli.args.append(new_arg)
    if joboptions["p_seq"] != "" or joboptions["d_seq"] != "" or joboptions["r_seq"] != "":
        new_arg = rc.Param(" build ","")

        if joboptions["p_seq"] != "" :
            #  Run with a protein sequence file
            node2 = rc.Node (joboptions["p_seq"].getString(), joboptions["p_seq"].node_type)
            cli.add_innode(node2)

            new_arg = rc.Param(" -pf ", "p_seq",assertion="is_field_empty")
            cli.args.append(new_arg)
        
        if joboptions["d_seq"] != "":
            #  Run with a DNA sequence file
            node2 = rc.Node(joboptions["d_seq"].getString(), joboptions["d_seq"].node_type)
            cli.add_innode(node2)

            new_arg = rc.Param(" -df ", "d_seq",assertion="required")
            cli.args.append(new_arg)
        
        if joboptions["r_seq"] != "":
            #  Run with a protein sequence file
            node2 = rc.Node (joboptions["r_seq"].getString(), joboptions["r_seq"].node_type)
            cli.add_innode(node2)

            new_arg = rc.Param(" -rf ", "r_seq",assertion="required")
            cli.args.append(new_arg)
    
    else:
        new_arg = rc.Param(" build_no_seq ","")
        cli.args.append(new_arg)   

    new_arg = rc.Param(" -v ", "fn_map")
    cli.args.append(new_arg)
    new_arg = rc.Param(" -o ",outputname)
    new_arg = rc.Param(" -d ", "gpu_id")
    cli.args.append(new_arg)

    node3 = rc.Node(outputmodel, rh.LABEL_ATOMCOORDS_CPIPE)
    cli.add_outnode(node3)

    #  Other arguments for model_angelo
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
            
    #  If no sequence was provided, but a library was provided, then also run an HMM search
    if joboptions["do_hhmer"].getBoolean():
        if joboptions["fn_lib"] == "":
            error_message = "ERROR: you need to provide a library to perform the HMM search against."
            return False

        command2 = joboptions["fn_modelangelo_exe"]

        command2 += " hmm_search "
        command2 += " -i " + outputname
        command2 += " -f ", "fn_lib"
        command2 += " -o " + outputname
        command2 += " -a ", "alphabet"

        # HMMSearch parameters
        command2 += "--F1 ", "F1"
        command2 += "--F2 ", "F2"
        command2 += "--F3 ", "F3"
        command2 += "--E ", "E"

        #  Other arguments for model_angelo
        command2 += " ", "other_args"
        commands.push_back(command2)
    
    # return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message, true)
    return script

def getCommandsMotionrefineJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    cli.add_prog(rc.Prog("`which relion_motion_refine_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_motion_refine`","use_mpi",False))

    if joboptions["fn_data"] == "":
        error_message = "ERROR: empty field for input particle STAR file..."
        return False
    if joboptions["fn_mic"] == "":
        error_message = "ERROR: empty field for input micrograph STAR file..."
        return False
    if joboptions["fn_post"] == "":
        error_message = "ERROR: empty field for input PostProcess STAR file..."
        return False
    
    if joboptions["do_param_optim"].getBoolean() and joboptions["do_polish"].getBoolean():
        error_message = "ERROR: Choose either parameter training or polishing, not both."
        return False
    
    if not joboptions["do_param_optim"].getBoolean() and not joboptions["do_polish"].getBoolean():
        error_message = "ERROR: nothing to do, choose either parameter training or polishing."
        return False
    
    if (joboptions["eval_frac"].getNumber(error_message) <= 0.1 or joboptions["eval_frac"].getNumber(error_message) > 0.9 ) \
            and not joboptions["eval_frac"].isSchedulerVariable():
        error_message = "ERROR: the fraction of Fourier pixels used for evaluation should be between 0.1 and 0.9."
        return False
        if error_message != "":
            return False

    node = rc.Node(joboptions["fn_data"].getString(), joboptions["fn_data"].node_type)
    cli.add_innode(node)

    node2 = rc.Node (joboptions["fn_post"].getString(), joboptions["fn_post"].node_type)
    cli.add_innode(node)

    new_arg = rc.Param("--i ", "fn_data")
    cli.args.append(new_arg)
    new_arg = rc.Param("--f ", "fn_post")
    cli.args.append(new_arg)
    new_arg = rc.Param("--corr_mic ", "fn_mic")
    cli.args.append(new_arg)
    new_arg = rc.Param("--first_frame ", "first_frame")
    cli.args.append(new_arg)
    new_arg = rc.Param("--last_frame ", "last_frame")
    cli.args.append(new_arg)
    new_arg = rc.Param("--o ", outputname)
    cli.args.append(new_arg)

    # if joboptions["do_float16"].getBoolean():
    new_arg = rc.Flag("--float16 ","","do_float16",True)
    
    if joboptions["do_param_optim"].getBoolean():
        label += ".train"

        #  Estimate meta-parameters
        align_frac = 1.0 - joboptions["eval_frac"].getNumber(error_message)
        if error_message != "":
            return False
        new_arg = rc.Param("--min_p ", "optim_min_part")
        cli.args.append(new_arg)
        new_arg = rc.Param("--eval_frac ", "eval_frac")
        cli.args.append(new_arg)
        new_arg = rc.Param("--align_frac ", floatToString(align_frac))
        cli.args.append(new_arg)        

        if joboptions["sigma_acc"].getNumber(error_message) < 0:
            new_arg = rc.Flag("--params2 ","","sigma_acc","is_lt",0)
        else:
            new_arg = rc.Flag("--params3 ","","sigma_acc","is_ge",0)
        if error_message != "":
            return False

        node5 = rc.Node(outputname+"opt_params_all_groups.txt", rh.LABEL_POLISH_PARAMS)
        cli.add_outnode(node5)

    elif joboptions["do_polish"].getBoolean():
        # if joboptions["do_own_params"].getBoolean():
        #  User-specified Parameters
        new_arg = rc.Param("--s_vel ", "sigma_vel","do_own_params",True)
        cli.args.append(new_arg)
        new_arg = rc.Param("--s_div ", "sigma_div","do_own_params",True)
        cli.args.append(new_arg)
        new_arg = rc.Param("--s_acc ", "sigma_acc","do_own_params",True)
        cli.args.append(new_arg)
    else:
        if joboptions["opt_params"] == "":
            error_message = "ERROR: Please specify an optimised parameter file OR choose 'use own paramaeters' and set three sigma values."
            return False
        new_arg = rc.Param("--params_file ", "opt_params",assertion="required")
        cli.args.append(new_arg)
        
        new_arg = rc.Param("--combine_frames","")
        cli.args.append(new_arg)
        new_arg = rc.Param("--bfac_minfreq ", "minres")
        cli.args.append(new_arg)
        new_arg = rc.Param("--bfac_maxfreq ", "maxres")
        cli.args.append(new_arg)

        window = ROUND(joboptions["extract_size"].getNumber(error_message))
        if error_message != "":
            return False

        scale = ROUND(joboptions["rescale"].getNumber(error_message))
        if error_message != "":
            return False

        if window * scale <= 0:
            error_message = "ERROR: Please specify both the extraction box size and the downsampled size, or leave both the default (-1)"
            return False
        
        if window > 0 and scale > 0:
            if window % 2 != 0:
                error_message = "ERROR: The extraction box size must be an even number"
                return False
            new_arg = rc.Param("--window ", "extract_size")
            cli.args.append(new_arg)

            if scale % 2 != 0:
                error_message = "ERROR: The downsampled box size must be an even number."
                return False
            
            if scale > window:
                error_message = "ERROR: The downsampled box size cannot be larger than the extraction size."
                return False
            new_arg = rc.Param("--scale ", "rescale")
            cli.args.append(new_arg)
        
        node6 = rc.Node(outputname+"logfile.pdf", rh.LABEL_POLISH_LOG)
        cli.add_outnode(node6)

        node7 = rc.Node (outputname+"shiny.star", rh.LABEL_POLISH_PARTS)
        cli.add_outnode(node7)
    
    #  If this is a continue job, then only process unfinished micrographs
    if is_continue:
        new_arg = rc.Param("--only_do_unfinished ","")

    #  Running stuff
    new_arg = rc.Param("--j ", "nr_threads")
    cli.args.append(new_arg)

    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    return script

def getCommandsCtfrefineJob(outputname,label,job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    cli.add_prog(rc.Prog("`which relion_ctf_refine_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_ctf_refine`","use_mpi",False))

    if joboptions["fn_data"] == "":
        error_message = "ERROR: empty field for input particle STAR file..."
        return False
    if joboptions["fn_post"] == "":
        error_message = "ERROR: empty field for input PostProcess STAR file..."
        return False
    
    if not joboptions["do_aniso_mag"].getBoolean() and \
        not joboptions["do_ctf"].getBoolean() and \
        not joboptions["do_tilt"].getBoolean() and \
        not joboptions["do_4thorder"].getBoolean():
            error_message = "ERROR: you haven't selected to fit anything..."
            return False
    
    if not joboptions["do_aniso_mag"].getBoolean() and joboptions["do_ctf"].getBoolean() and \
        joboptions["do_defocus"] == job_ctffit_options[0] and \
        joboptions["do_astig"] == job_ctffit_options[0] and \
        joboptions["do_bfactor"] == job_ctffit_options[0] and \
        joboptions["do_phase"]== job_ctffit_options[0]:
            error_message = "ERROR: you did not select any CTF parameter to fit. Either switch off CTF parameter fitting, or select one to fit."
            return False
    
    node = rc.Node(joboptions["fn_data"].getString(), joboptions["fn_data"].node_type)
    cli.add_innode(node)

    node2 = rc.Node (joboptions["fn_post"].getString(), joboptions["fn_post"].node_type)
    cli.add_innode(node)

    node6 = rc.Node (outputname+"logfile.pdf", rh.LABEL_CTFREFINE_LOG)
    cli.add_outnode(node6)

    new_arg = rc.Param("--i ", "fn_data")
    cli.args.append(new_arg)
    new_arg = rc.Param("--f ", "fn_post")
    cli.args.append(new_arg)
    new_arg = rc.Param("--o ", outputname)

    #  Always either do anisotropic magnification, or CTF,tilt-odd,even
    if joboptions["do_aniso_mag"].getBoolean():
        label += ".anisomag"

        new_arg = rc.Flag("--fit_aniso","","do_aniso_mag",True)
        cli.args.append(new_arg)
        new_arg = rc.Flag("--kmin_mag ", "minres","do_aniso_mag",True)
        cli.args.append(new_arg)

        node5 = rc.Node (outputname+"particles_ctf_refine.star", rh.LABEL_CTFREFINE_ANISOPARTS)
        cli.add_outnode(node5)

    else:
        node5 = rc.Node(outputname+"particles_ctf_refine.star", rh.LABEL_CTFREFINE_REFINEPARTS)
        cli.add_outnode(node5)

        if joboptions["do_ctf"].getBoolean():
            new_arg = rc.Param("--fit_defocus --kmin_defocus ", "minres")
            cli.args.append(new_arg)
            fit_options = ""
            fit_options += getCtfFitString(joboptions["do_phase"])
            fit_options += getCtfFitString(joboptions["do_defocus"])
            fit_options += getCtfFitString(joboptions["do_astig"])
            fit_options += "f" #  always have Cs refinement switched off
            fit_options += getCtfFitString(joboptions["do_bfactor"])
            if fit_options.size() != 5:
                error_message = "Wrong CTF fitting options"
                return False
            
            new_arg = rc.Param("--fit_mode ", fit_options)
        
        #  do not allow anisotropic magnification to be done simultaneously with higher-order aberrations
        # if joboptions["do_tilt"].getBoolean():
        new_arg = rc.Flag("--fit_beamtilt","","do_tilt",True)
        cli.args.append(new_arg)
        new_arg = rc.Flag("--kmin_tilt ", "minres","do_tilt",True)
        cli.args.append(new_arg)

        # if joboptions["do_trefoil"].getBoolean():
        new_arg = rc.Flag("--odd_aberr_max_n","3""do_trefoil",True)
                    
        if joboptions["do_4thorder"].getBoolean():
            new_arg = rc.Param("--fit_aberr","","do_4thorder",True)
            
    #  If this is a continue job, then only process unfinished micrographs
    if is_continue:
        new_arg = rc.Param("--only_do_unfinished ","")
    
    #  Running stuff
    new_arg = rc.Param("--j ", "nr_threads")
    cli.args.append(new_arg)

    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    return script

# USELESS
# def getCommandsExternalJob(outputname,label,job_counter=-1):
#     script, cli = clear(label)
#     initialisePipeline(outputname, job_counter)
    

#     if joboptions["fn_exe")
#     cli.args.append(new_arg) == "")
#             error_message = "ERROR: empty field for the external executable script..."
#         return False
    
#     command=joboptions["fn_exe")
#     cli.args.append(new_arg)
#     new_arg = rc.Param("--o " + outputname

#     #  Optional input nodes
#     if joboptions["in_mov")
#     cli.args.append(new_arg) != "")
#             node = rc.Node(joboptions["in_mov")
#     cli.args.append(new_arg), joboptions["in_mov"].node_type)
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_movies ", "in_mov")
#     cli.args.append(new_arg)
#         if joboptions["in_mic")
#     cli.args.append(new_arg) != "")
#             node = rc.Node(joboptions["in_mic")
#     cli.args.append(new_arg), joboptions["in_mic"].node_type)
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_mics ", "in_mic")
#     cli.args.append(new_arg)
#         if joboptions["in_part")
#     cli.args.append(new_arg) != "")
#             node = rc.Node(joboptions["in_part")
#     cli.args.append(new_arg), joboptions["in_part"].node_type)
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_parts ", "in_part")
#     cli.args.append(new_arg)
#         if joboptions["in_coords")
#     cli.args.append(new_arg) != "")
#             node = rc.Node(joboptions["in_coords")
#     cli.args.append(new_arg), joboptions["in_coords"].node_type)
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_coords ", "in_coords")
#     cli.args.append(new_arg)
#         if joboptions["in_3dref")
#     cli.args.append(new_arg) != "")
#             node = rc.Node(joboptions["in_3dref")
#     cli.args.append(new_arg), joboptions["in_3dref"].node_type)
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_3dref ", "in_3dref")
#     cli.args.append(new_arg)
#         if joboptions["in_mask")
#     cli.args.append(new_arg) != "")
#             node = rc.Node(joboptions["in_mask")
#     cli.args.append(new_arg), joboptions["in_mask"].node_type)
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_mask ", "in_mask")
#     cli.args.append(new_arg)
    
#     #  Optional arguments
#     if joboptions["param1_label")
#     cli.args.append(new_arg) != "")
#             new_arg = rc.Param("--", "param1_label")
#     cli.args.append(new_arg) + " ", "param1_value")
#     cli.args.append(new_arg)
#         if joboptions["param2_label")
#     cli.args.append(new_arg) != "")
#             new_arg = rc.Param("--", "param2_label")
#     cli.args.append(new_arg) + " ", "param2_value")
#     cli.args.append(new_arg)
#         if joboptions["param3_label")
#     cli.args.append(new_arg) != "")
#             new_arg = rc.Param("--", "param3_label")
#     cli.args.append(new_arg) + " ", "param3_value")
#     cli.args.append(new_arg)
#         if joboptions["param4_label")
#     cli.args.append(new_arg) != "")
#             new_arg = rc.Param("--", "param4_label")
#     cli.args.append(new_arg) + " ", "param4_value")
#     cli.args.append(new_arg)
#         if joboptions["param5_label")
#     cli.args.append(new_arg) != "")
#             new_arg = rc.Param("--", "param5_label")
#     cli.args.append(new_arg) + " ", "param5_value")
#     cli.args.append(new_arg)
#         if joboptions["param6_label")
#     cli.args.append(new_arg) != "")
#             new_arg = rc.Param("--", "param6_label")
#     cli.args.append(new_arg) + " ", "param6_value")
#     cli.args.append(new_arg)
#         if joboptions["param7_label")
#     cli.args.append(new_arg) != "")
#             new_arg = rc.Param("--", "param7_label")
#     cli.args.append(new_arg) + " ", "param7_value")
#     cli.args.append(new_arg)
#         if joboptions["param8_label")
#     cli.args.append(new_arg) != "")
#             new_arg = rc.Param("--", "param8_label")
#     cli.args.append(new_arg) + " ", "param8_value")
#     cli.args.append(new_arg)
#         if joboptions["param9_label")
#     cli.args.append(new_arg) != "")
#             new_arg = rc.Param("--", "param9_label")
#     cli.args.append(new_arg) + " ", "param9_value")
#     cli.args.append(new_arg)
#         if joboptions["param10_label")
#     cli.args.append(new_arg) != "")
#             new_arg = rc.Param("--", "param10_label")
#     cli.args.append(new_arg) + " ", "param10_value")
#     cli.args.append(new_arg)
    
#     #  Running stuff
#     new_arg = rc.Param("--j ", "nr_threads")
#     cli.args.append(new_arg)

#     #  Other arguments for extraction
#     new_arg = rc.Param(" ", "other_args")
#     cli.args.append(new_arg)
    
#     return script



def getCommands(cmdtype,subtype):

    result = False
    commands = None
    final_command = None
    do_makedir = None
    job_counter = None
    error_message = None
    outputname =  rh.proc_type2dirname(rh.PROC_IMPORT) + '/RELION_NEW_JOB'
    if cmdtype == rh.PROC_IMPORT:
        if subtype == rh.PROC_IMPORT_RAW_GRR:
            result = getCommandsImportJobRaw(outputname,subtype)
        elif subtype == rh.PROC_IMPORT_OTHER_GRR:
            result = getCommandsImportJobOther(outputname,subtype)
    elif cmdtype == rh.PROC_MOTIONCORR:
        result = getCommandsMotioncorrJob(outputname,subtype)
    elif cmdtype == rh.PROC_CTFFIND:
        result = getCommandsCtffindJob(outputname,subtype)
    elif cmdtype == rh.PROC_MANUALPICK:
        result = getCommandsManualpickJob(outputname,subtype)
    elif cmdtype == rh.PROC_AUTOPICK:
        result = getCommandsAutopickJob(outputname,subtype)
    elif cmdtype == rh.PROC_EXTRACT:
        result = getCommandsExtractJob(outputname,subtype)
    elif cmdtype == rh.PROC_CLASSSELECT:
        result = getCommandsSelectJob(outputname,subtype)
    elif cmdtype == rh.PROC_2DCLASS:
        result = getCommandsClass2DJob(outputname,subtype)
    elif cmdtype == rh.PROC_INIMODEL:
        result = getCommandsInimodelJob(outputname,subtype)
    elif cmdtype == rh.PROC_3DCLASS:
        result = getCommandsClass3DJob(outputname,subtype)
    elif cmdtype == rh.PROC_3DAUTO:
        result = getCommandsAutorefineJob(outputname,subtype)
    elif cmdtype == rh.PROC_MULTIBODY:
        result = getCommandsMultiBodyJob(outputname,subtype)
    elif cmdtype == rh.PROC_MASKCREATE:
        result = getCommandsMaskcreateJob(outputname,subtype)
    elif cmdtype == rh.PROC_JOINSTAR:
        cmdtype = getCommandsJoinstarJob(outputname,subtype)
    elif cmdtype == rh.PROC_SUBTRACT:
        cmdtype = getCommandsSubtractJob(outputname,subtype)
    elif cmdtype == rh.PROC_POST:
        result = getCommandsPostprocessJob(outputname,subtype)
    elif cmdtype == rh.PROC_RESMAP:
        result = getCommandsLocalresJob(outputname,subtype)
    elif cmdtype == rh.PROC_MOTIONREFINE:
        result = getCommandsMotionrefineJob(outputname,subtype)
    elif cmdtype == rh.PROC_CTFREFINE:
        result = getCommandsCtfrefineJob(outputname,subtype)
    elif cmdtype == rh.PROC_DYNAMIGHT:
        result = getCommandsDynaMightJob(outputname,subtype)
    elif cmdtype == rh.PROC_MODELANGELO:
        result = getCommandsModelAngeloJob(outputname,subtype)
    else:
        print('ERROR: Unknown Command')

    return result
    
# Main

cmd = getCommands(rh.PROC_IMPORT, rh.PROC_IMPORT_RAW_GRR)
print(cmd)

