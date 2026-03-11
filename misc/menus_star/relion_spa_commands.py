import os
import relion_h as rh
import relion_option as rjo
import relion_command as rc

#############

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
        if s == rh.job_sampling_options[i]:
            return i + 1
    return -1

def getCtfFitString(s):
    if s == rh.job_ctffit_options[0]:
        return "f"
    elif s == rh.job_ctffit_options[1]:
        return "m"
    elif s == rh.job_ctffit_options[2]:
        return "p"
    else:
        return ""

def getTomoInputCommmand(*args):
    return ""

def integerToString(v):
    return v

def floatToString(v):
    return v

def getCommandsImportJob(joboptions,outputname, label="none", job_counter=-1):
    script, cli = clear(label)
    cli.add_prog(rc.Prog("relion_import"))

    # Movies
    fn_out = "movies.star"
    nod = rc.Node(outputname + fn_out, rh.LABEL_IMPORT_MOVIES)
    nod.flag("is_multiframe", True )
    cli.add_outnode(nod)
    new_arg = rc.Flag("--do_movies","","is_multiframe", True )
    cli.append_arg(new_arg)
    # Micrographs
    fn_out = "micrographs.star"
    nod = rc.Node(outputname + fn_out, rh.LABEL_IMPORT_MICS)
    nod.flag("is_multiframe", False )
    cli.add_outnode(nod)
    new_arg = rc.Flag("--do_micrographs","","is_multiframe",  False)
    cli.append_arg(new_arg)
    # Optics group
    new_arg = rc.Param("--optics_group_name", "optics_group_name", assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--optics_group_mtf","","fn_mtf","not_empty")
    cli.append_arg(new_arg) 
    new_arg = rc.Param("--angpix","angpix")
    cli.append_arg(new_arg) 
    new_arg = rc.Param("--kV","kV")
    cli.append_arg(new_arg) 
    new_arg = rc.Param("--Cs", "Cs")
    cli.append_arg(new_arg) 
    new_arg = rc.Param("--Q0", "Q0")
    cli.append_arg(new_arg) 
    new_arg = rc.Param("--beamtilt_x","beamtilt_x")
    cli.append_arg(new_arg) 
    new_arg = rc.Param("--beamtilt_y","beamtilt_y")
    cli.append_arg(new_arg) 

    # node_type == "Particle coordinates (*.box, *_pick.star)")
    fn_out = fn_out = "coords_suffix" + "{fn_in_other}"
    nod = rc.Node(outputname + fn_out, rh.LABEL_IMPORT_COORDS)
    nod.flag("node_type","LABEL_IMPORT_COORDS")
    cli.add_outnode(nod)
    new_arg = rc.Param("--do_coordinates","")
    cli.append_arg(new_arg)
    # Other
    fn_out = "{fn_in_other}"
	# node_type == "Particles STAR file (.star)")
    mynodetype = rh.LABEL_IMPORT_PARTS
    nod = rc.Node(outputname + fn_out, mynodetype)
    nod.flag("node_type","LABEL_IMPORT_PARTS")
    cli.add_outnode(nod)
    # node_type == "Multiple (2D or 3D) references (.star or .mrcs)")
    mynodetype = rh.LABEL_IMPORT_2DIMG
    nod = rc.Node(outputname + fn_out, mynodetype)
    nod.flag("node_type","LABEL_IMPORT_2DIMG")
    cli.add_outnode(nod)
     # (node_type == "3D reference (.mrc)")
    mynodetype = rh.LABEL_IMPORT_MAP
    nod = rc.Node(outputname + fn_out, mynodetype)
    nod.flag("node_type","LABEL_IMPORT_MAP")
    cli.add_outnode(nod)
     # node_type == "3D mask (.mrc)")
    mynodetype = rh.LABEL_IMPORT_MASK
    nod = rc.Node(outputname + fn_out, mynodetype)
    nod.flag("node_type","LABEL_IMPORT_MASK")
    cli.add_outnode(nod)
    # node_type == "Micrographs STAR file (.star)")
    mynodetype = rh.LABEL_IMPORT_MICS
    nod = rc.Node(outputname + fn_out, mynodetype)
    nod.flag("node_type","LABEL_IMPORT_MICS")
    cli.add_outnode(nod)
    # node_type == "Unfiltered half-map (unfil.mrc)")
    mynodetype = rh.LABEL_IMPORT_HALFMAP
    nod = rc.Node(outputname + fn_out, mynodetype)
    nod.flag("node_type","LABEL_IMPORT_HALFMAP")
    cli.add_outnode(nod)
    new_arg = rc.Flag("--do_halfmaps","","node_type","LABEL_IMPORT_HALFMAP")
    cli.append_arg(new_arg)

    # Particles LABEL_PARTS_CPIPE
    mynodetype = rh.LABEL_PARTS_CPIPE
    nod = rc.Node(outputname + fn_out, mynodetype)
    nod.flag("node_type","LABEL_PARTS_CPIPE")
    cli.add_outnode(nod)
    new_arg = rc.Flag("--do_particles","","node_type","LABEL_PARTS_CPIPE")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--optics_group_name ","optics_group_particles","node_type","LABEL_PARTS_CPIPE")
    cli.append_arg(new_arg)

    new_arg = rc.Param("--i ","fn_in")
    new_arg = rc.Param("--odir", "outputname")
    new_arg = rc.Param("--ofile ","fn_out")
                       
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script


def getCommandsMotioncorrJob_Own(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    cli.main_prog(rc.Prog("mpirun -n {nr_mpi} `which relion_run_motioncorr_mpi`","use_mpi",True))
    cli.secondary_prog(rc.Prog("`which relion_run_motioncorr`","use_mpi",False))
#        # return False
    new_arg = rc.Param("--i ", "input_star_mics",assertion="required")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["input_star_mics"].getString(), joboptions["input_star_mics"].nodetype,"input_star_mics","input_star_mics")
    cli.add_innode(node)
    new_arg = rc.Param("--o ",outputname)
    cli.append_arg(new_arg)
    node2 = rc.Node (outputname + "corrected_micrographs.star", rh.LABEL_MOCORR_MICS)
    cli.add_outnode(node2)
    node4 = rc.Node(outputname + "logfile.pdf", rh.LABEL_MOCORR_LOG)
    cli.add_outnode(node4)
    new_arg = rc.Param("--first_frame_sum ", "first_frame_sum")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--last_frame_sum ", "last_frame_sum")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--use_own "," ","do_own_motioncor",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--j ", "nr_threads")
    cli.append_arg(new_arg)

    new_arg = rc.Param("--float16","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--defect_file ", "fn_defect",assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--bin_factor ", "bin_factor")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--bfactor ", "bfactor")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--dose_per_frame ", "dose_per_frame")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--preexposure ", "pre_exposure")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--patch_x ", "patch_x")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--patch_y ", "patch_y")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--eer_grouping ", "eer_grouping")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--group_frames ", "group_frames",assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--gainref ", "fn_gain_ref")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--gain_rot ","gain_rot",assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--gain_flip ","gain_flip",assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--dose_weighting ","do_dose_weighting",True)
    new_arg = rc.Flag("--save_noDW ","do_save_noDW",True)
    #      # return False
    #     # return False
    #             # return False
    #     # return False
    #     # return False
    # new_arg = rc.Param("--grouping_for_ps ","grouping_for_ps")
    new_arg = rc.Flag("--only_do_unfinished ","is_continue", True)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script


def getCommandsMotioncorrJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    cli.main_prog(rc.Prog("mpirun -n {nr_mpi} `which relion_run_motioncorr_mpi`","use_mpi",True))
    cli.secondary_prog(rc.Prog("`which relion_run_motioncorr`","use_mpi",False))
#        # return False

    new_arg = rc.Param("--i ", "input_star_mics",assertion="required")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["input_star_mics"].getString(), joboptions["input_star_mics"].nodetype,"input_star_mics")
    cli.add_innode(node)
    new_arg = rc.Param("--o ",outputname)
    cli.append_arg(new_arg)
    node2 = rc.Node(outputname + "corrected_micrographs.star", rh.LABEL_MOCORR_MICS)
    cli.add_outnode(node2)
    node4 = rc.Node(outputname + "logfile.pdf", rh.LABEL_MOCORR_LOG)
    cli.add_outnode(node4)
    new_arg = rc.Param("--first_frame_sum ", "first_frame_sum")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--last_frame_sum ", "last_frame_sum")
    cli.append_arg(new_arg)
    cli.label(".motioncor2","do_own_motioncor",False)
    new_arg = rc.Flag("--use_motioncor2 ","","do_own_motioncor",False)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--motioncor2_exe ", "fn_motioncor2_exe","do_own_motioncor",False)
    cli.append_arg(new_arg)
#       # return False
    new_arg = rc.Flag("--other_motioncor2_args ", "other_motioncor2_args","do_own_motioncor",False)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--gpu", "gpu_ids","do_own_motioncor",False)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--defect_file ", "fn_defect",assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--bin_factor ", "bin_factor")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--bfactor ", "bfactor")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--dose_per_frame ", "dose_per_frame")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--preexposure ", "pre_exposure")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--patch_x ", "patch_x")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--patch_y ", "patch_y")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--eer_grouping ", "eer_grouping")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--group_frames ", "group_frames",assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--gainref ", "fn_gain_ref")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--gain_rot ","gain_rot",assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--gain_flip ","gain_flip",assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--dose_weighting ","","do_dose_weighting",True)
    new_arg = rc.Flag("--save_noDW ","","do_save_noDW",True)

    new_arg = rc.Flag("--only_do_unfinished ","","is_continue", True)
    new_arg = rc.Param("{other_args}","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pipeline-control", outputname)
    cli.append_arg(new_arg)
    return script


def getCommandsCtffindJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    outputName = outputname
    #         rc.Node node(outputname + "tilt_series_ctf.star", rh.LABEL_CTFFIND_TOMOGRAMS)
    #     cli.add_outnode(node)
    node = rc.Node(outputname + "micrographs_ctf.star", rh.LABEL_CTFFIND_MICS)
    cli.add_outnode(node)
    node3 = rc.Node(outputname + "logfile.pdf", rh.LABEL_CTFFIND_LOG)
    cli.add_outnode(node3)
    rc.Prog("`which relion_run_ctffind_mpi`","use_mpi",True)
    rc.Prog("`which relion_run_ctffind`","use_mpi",False)
#        # return False
    new_arg = rc.Param("--i ", "input_star_mics",assertion="required")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["input_star_mics"].getString(), joboptions["input_star_mics"].nodetype,"input_star_mics")
    cli.add_innode(node)
    new_arg = rc.Param("--o ",outputname)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--Box ", "box")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ResMin ", "resmin")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ResMax ", "resmax")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--dFMin ", "dfmin")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--dFMax ", "dfmax")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--FStep ", "dfstep")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--dAst ", "dast")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--use_noDW ","use_noDW",True)
    new_arg = rc.Flag("--do_phaseshift ","do_phaseshift",True)
    new_arg = rc.Flag("--phase_min ", "phase_min","do_phaseshift",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--phase_max ", "phase_max","do_phaseshift",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--phase_step ", "phase_step","do_phaseshift",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ctffind_exe ", "fn_ctffind_exe")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ctfWin ", "ctf_win")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--is_ctffind4 ","")
    new_arg = rc.Flag("--fast_search ","slow_search",True)
    new_arg = rc.Param("--use_given_ps ","use_given_ps",True)
    new_arg = rc.Param("--only_do_unfinished ","is_continue",True)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsManualpickJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    cli.add_prog(rc.Prog("`which relion_manualpick`"))
#        # return False
    new_arg = rc.Param("--i ", "fn_in",assertion="required")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_in"].getString(), joboptions["fn_in"].nodetype,"fn_in")
    cli.add_innode(node)
    new_arg = rc.Param("--odir ", outputname)
    new_arg = rc.Param("--pickname manualpick","")
    fn_outstar = outputname + "micrographs_selected.star"
    node3 = rc.Node(fn_outstar, rh.LABEL_MANPICK_MICS)
    cli.add_outnode(node3)
    new_arg = rc.Param("--allow_save --fast_save --selection ", fn_outstar)
    new_arg = rc.Param("--scale ", "micscale")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--sigma_contrast ", "sigma_contrast")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--black ", "black_val")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--white ", "white_val")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--topaz_denoise","do_topaz_denoise",True)
    new_arg = rc.Param("--lowpass ", "lowpass",assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--highpass ", "highpass", assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--angpix ", "angpix", assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--minimum_pick_fom ", "minimum_pick_fom","do_fom_threshold",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--particle_diameter ", "diameter")
    cli.append_arg(new_arg)
#        new_arg = rc.Param("--pick_start_end ","do_startend",True)
#        rc.Node node2(outputname + "manualpick.star", rh.LABEL_MANPICK_COORDS_HELIX)
#        cli.add_outnode(node2)
    node2 = rc.Node(outputname + "manualpick.star", rh.LABEL_MANPICK_COORDS)
    cli.add_outnode(node2)
    new_arg = rc.Param("--color_label ", "color_label","do_color",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--blue ", "blue_value")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--red ", "red_value")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--color_star ", "","fn_color",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsAutopickContinueJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    cli.prog(rc.Prog("`which relion_manualpick`"))
    new_arg = rc.Param("--i ", "fn_input_autopick")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--odir ",outputname)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pickname autopick","")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_input_autopick"].getString(), joboptions["fn_input_autopick"].nodetype,"fn_input_autopick")
    cli.add_innode(node)
    node2 = rc.Node (outputname + "autopick.star", rh.LABEL_AUTOPICK_COORDS)
    cli.add_outnode(node2)
    #  The output micrographs selection
    fn_outstar = outputname + "micrographs_selected.star"
    node3 = rc.Node(fn_outstar, rh.LABEL_AUTOPICK_MICS)
    cli.add_outnode(node3)
    new_arg = rc.Param("--allow_save  --selection ",fn_outstar)
    new_arg = rc.Param("--scale ",manualpickjob.joboptions["micscale"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--sigma_contrast " + manualpickjob.joboptions["sigma_contrast"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--black " + manualpickjob.joboptions["black_val"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--white " + manualpickjob.joboptions["white_val"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pick_start_end ","")
    new_arg = rc.Param("--topaz_denoise ","")
    new_arg = rc.Param("--lowpass ", manualpickjob.joboptions["lowpass"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--highpass " + manualpickjob.joboptions["highpass"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--angpix " + manualpickjob.joboptions["angpix"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--particle_diameter ", manualpickjob.joboptions["diameter"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--minimum_pick_fom ",manualpickjob.joboptions["minimum_pick_fom"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--color_label ", manualpickjob.joboptions["color_label"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--blue ", manualpickjob.joboptions["blue_value"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--red ", manualpickjob.joboptions["red_value"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--color_star ", manualpickjob.joboptions["fn_color"])
    cli.append_arg(new_arg)
    new_arg = rc.Param("--scale","0.25")
    new_arg = rc.Param("--sigma_contrast", "3")
    new_arg = rc.Param("--lowpass","20")
    new_arg = rc.Param("--particle_diameter","100")
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsAutopickTopazTrainJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    #    # return False
    #     # return False
    #    # return False
    new_arg = rc.Param("--fn_topaz_exe ", "fn_topaz_exe")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--i ", "fn_input_autopick")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_input_autopick"].getString(), joboptions["fn_input_autopick"].nodetype,"fn_input_autopick")
    cli.add_innode(node)
    node3 = rc.Node(outputname + "autopick.star", rh.LABEL_AUTOPICK_COORDS)
    cli.add_outnode(node3)
    node3b = rc.Node(outputname + "logfile.pdf", rh.LABEL_AUTOPICK_LOG)
    cli.add_outnode(node3b)
    new_arg = rc.Param("--odir ", outputname)
    new_arg = rc.Param("--pickname", "autopick")
    #     # return False
    new_arg = rc.Param("--particle_diameter ", "topaz_particle_diameter",assertion="is_positive")
    cli.append_arg(new_arg)
    # return False
    #     # return False
    new_arg = rc.Flag("--topaz_train","","do_topaz_train",True)
    new_arg = rc.Param("--topaz_nr_particles ", "topaz_nr_particles")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Flag("--topaz_train_parts ", "topaz_train_parts","do_topaz_train_parts",True)
    cli.append_arg(new_arg)
    nodet = rc.Node(outputname + "input_training_coords.star", rh.LABEL_COORDS_CPIPE)
    cli.add_outnode(nodet)
    new_arg = rc.Param("--topaz_train_picks ", "topaz_train_picks")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsAutopickTopazPickJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    new_arg = rc.Param("--topaz_extract","")
    new_arg = rc.Param("--topaz_model ", "topaz_model",assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helix ","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--topaz_threshold ", "topaz_filament_threshold")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_tube_length_min ", "topaz_hough_length",assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--topaz_args ", "topaz_other_args",assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--gpu", "gpu_ids","use_gpu",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsAutopickLoGJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    # return False
    new_arg = rc.Param("--LoG ","")
    new_arg = rc.Param("--LoG_diam_min ", "log_diam_min")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--LoG_diam_max ", "log_diam_max")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--shrink 0 --lowpass ", "log_maxres")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--LoG_adjust_threshold ", "log_adjust_thr")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--LoG_upper_threshold ", "log_upper_thr")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Flag("--Log_invert ","","log_invert",True)
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsAutopickRef3DJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    new_arg = rc.Param("--ref ", "fn_ref3d_autopick")
    cli.append_arg(new_arg)
    node2 = rc.Node(joboptions["fn_ref3d_autopick"].getString(), rh.LABEL_MAP_CPIPE)
    cli.add_innode(node2)
    new_arg = rc.Param("--sym ", "ref3d_symmetry")
    cli.append_arg(new_arg)
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--healpix_order ", "ref3d_sampling")
    # return False
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsAutopickRef2DJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    new_arg = rc.Param("--ref ", "fn_refs_autopick")
    cli.append_arg(new_arg)
    node2 = rc.Node(joboptions["fn_refs_autopick"].getString(), rh.LABEL_2DIMGS_CPIPE)
    cli.add_innode(node2)
    new_arg = rc.Param("--invert ","")
    new_arg = rc.Param("--ctf ","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ctf_intact_first_peak ","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ang ", "psi_sampling_autopick")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--shrink ", "shrink")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--lowpass ", "lowpass","is_positive",True)
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Flag("--highpass ", "highpass","is_positive",True)
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Flag("--angpix ", "angpix","is_positive",True)
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Flag("--angpix_ref ", "angpix_ref","is_positive",True)
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--threshold ", "threshold_autopick")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--min_distance ",floatToString(joboptions["helical_nr_asu"].getNumber(error_message) * joboptions["helical_rise"].getNumber(error_message)))
    new_arg = rc.Param("--min_distance ", "mindist_autopick")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--max_stddev_noise ", "maxstddevnoise_autopick")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--min_avg_noise ", "minavgnoise_autopick","is_less",-900.)
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--helix","")
    new_arg = rc.Param("--amyloid","")
    new_arg = rc.Param("--helical_tube_outer_diameter ", "helical_tube_outer_diameter")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_tube_kappa_max ", "helical_tube_kappa_max")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_tube_length_min ", "helical_tube_length_min")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--gpu", "gpu_ids","use_gpu",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--write_fom_maps ","","do_write_fom_maps",True)
    new_arg = rc.Param("--read_fom_maps ","","do_read_fom_maps",True)
    new_arg = rc.Param("--only_do_unfinished ","")
    new_arg = rc.Param("--only_do_unfinished ","")
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsExtractJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    cli.add_prog(rc.Prog("`which relion_preprocess_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_preprocess`","use_mpi",True))
#        # return False
    new_arg = rc.Param("--i ", "star_mics",assertion="required")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["star_mics"].getString(), joboptions["star_mics"].nodetype,"star_mics")
    cli.add_innode(node)
    # return False
    # return False
    new_arg = rc.Param("--reextract_data_star ", "fndata_reextract")
    cli.append_arg(new_arg)
    node2 = rc.Node(joboptions["fndata_reextract"].getString(), joboptions["fndata_reextract"].nodetype,"fndata_reextract")
    cli.add_innode(node2)
    new_arg = rc.Flag("--reset_offsets","","do_reset_offsets", True)
    new_arg = rc.Flag("--recenter","","do_recenter",True)
    new_arg = rc.Flag("--recenter_x ", "recenter_x","do_recenter",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--recenter_y ", "recenter_y","do_recenter",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--recenter_z ", "recenter_z","do_recenter",True)
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--coord_dir ", mylist.beforeLastOf("/") + "/")
    new_arg = rc.Param("--coord_suffix ", (mylist.afterLastOf("/")).without("coords_suffix"))
    new_arg = rc.Param("--coord_list ",mylist)
    node2 = rc.Node(mylist, joboptions["coords_suffix"].nodetype,"coords_suffix")
    cli.add_innode(node2)
    fn_ostar = outputname + "particles.star"
    new_arg = rc.Param("--part_star ",fn_ostar)
    fn_pickstar = outputname + "extractpick.star"
    node = rc.Node (fn_pickstar, rh.LABEL_EXTRACT_COORDS_REEX)
    cli.add_outnode(node)
    new_arg = rc.Flag("--pick_star ",fn_pickstar,"do_reextract",True)
    cli.append_arg(new_arg)
    fn_pickstar = outputname + "extractpick.star"
    node = rc.Node (fn_pickstar, rh.LABEL_EXTRACT_COORDS_HELIX)
    cli.add_outnode(node)
    new_arg = rc.Param("--pick_star ", "do_extract_helix",fn_pickstar)
    cli.append_arg(new_arg)   
    new_arg = rc.Param("--part_dir ", outputname)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--extract","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--extract_size ", "extract_size")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--minimum_pick_fom ", "minimum_pick_fom","do_fom_threshold",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--float16 ","","do_float16",True)
    # return False
    new_arg = rc.Param("--scale ", "rescale","do_rescale",True)
    cli.append_arg(new_arg)
    # return False
    # return False
    new_arg = rc.Param("--norm --bg_radius ", "bg_radius","do_norm",True)
    new_arg = rc.Param("--white_dust ", "white_dust")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--black_dust ", "black_dust")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--invert_contrast ","","do_invert",True)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsExtractHelixJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    cli.add_prog(rc.Prog("`which relion_preprocess_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_preprocess`","use_mpi",True))
    node3 = rc.Node (fn_ostar, rh.LABEL_EXTRACT_PARTS_HELIX)
    cli.add_outnode(node3)
    new_arg = rc.Param("--helix","")
    new_arg = rc.Param("--helical_outer_diameter ", "helical_tube_outer_diameter")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_bimodal_angular_priors","","helical_bimodal_angular_priors",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_tubes","","do_extract_helical_tubes",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_cut_into_segments","","do_cut_into_segments",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_nr_asu ", "helical_nr_asu","do_cut_into_segments",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_rise ", "helical_rise","do_cut_into_segments",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_nr_asu 1 --helical_rise 1","","do_cut_into_segments",False)
    node3 = rc.Node(fn_ostar, rh.LABEL_EXTRACT_PARTS)
    cli.add_outnode(node3)
    new_arg = rc.Param("--only_do_unfinished ","")
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    node = rc.Node(outputname + "reextract.star", rh.LABEL_EXTRACT_COORDS_REEX)
    cli.add_outnode(node)
    node = rc.Node (outputname + "helix_segments.star", rh.LABEL_EXTRACT_COORDS_HELIX)
    cli.add_outnode(node)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsSelectFilamentJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    # return False
    #     # return False
    cli.add_prog(rc.Prog("`which relion_filament_selection`"))
    # return False
    #     # return False
    node = rc.Node(joboptions["fn_model"].getString(), joboptions["fn_model"].nodetype,"fn_model")
    cli.add_innode(node)
    fn_out = outputname + "run_optimiser.star"
    node2 = rc.Node(fn_out, rh.LABEL_SELECT_OPT)
    cli.add_outnode(node2)
    node3 = rc.Node(outputname + "logfile.pdf", rh.LABEL_SELECT_LOG)
    cli.add_outnode(node3)
    new_arg = rc.Param(" -i ", "fn_model")
    cli.append_arg(new_arg)
    new_arg = rc.Param(" -o ",outputname)
    new_arg = rc.Param(" -t ", "dendrogram_threshold")
    cli.append_arg(new_arg)
    new_arg = rc.Param(" -c ", "dendrogram_minclass")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsSelectDuplicateJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    # return False
    cli.add_prog(rc.prog("`which relion_star_handler`"))
    # return False
    # return False
    node = rc.Node(joboptions["fn_data"].getString(), joboptions["fn_data"].nodetype,"fn_data")
    cli.add_innode(node)
    new_arg = rc.Param("--i ", "fn_data")
    cli.append_arg(new_arg)
    fn_out = outputname + "particles.star"
    node2 = rc.Node(fn_out, rh.LABEL_SELECT_PARTS)
    cli.add_outnode(node2)
    new_arg = rc.Param("--o ", fn_out)
    new_arg = rc.Param("--remove_duplicates ", "duplicate_threshold")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--image_angpix ", "image_angpix","is_positive",True)
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsSelectDuplicateJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    # return False
    node = rc.Node(joboptions["fn_mic"].getString(), joboptions["fn_mic"].nodetype,"fn_mic")
    cli.add_innode(node)
    new_arg = rc.Param("--i ", "fn_mic")
    cli.append_arg(new_arg)
    fn_out = outputname+"micrographs.star"
    node = rc.Node(joboptions["fn_data"].getString(), joboptions["fn_data"].nodetype,"fn_data")
    cli.add_innode(node)
    new_arg = rc.Param("--i ", "fn_data")
    cli.append_arg(new_arg)
    fn_out = outputname+"particles.star"
    new_arg = rc.Param("--o ",fn_out)
    node2 = rc.Node (fn_out, rh.LABEL_SELECT_MICS)
    cli.add_outnode(node2)
    node2 = rc.Node(fn_out, rh.LABEL_SELECT_PARTS)
    cli.add_outnode(node2)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsSelectOnValueJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    # return False
    new_arg = rc.Param("--select ", "select_label")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--minval ", "select_minval")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--maxval ", "select_maxval")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsSelectDiscardJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)    
    new_arg = rc.Param("--discard_on_stats ","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--discard_label ", "discard_label")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--discard_sigma ", "discard_sigma")
    cli.append_arg(new_arg)
def getCommandsSelectSplitJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    # return False
    new_arg = rc.Param("--split ","")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--random_order ","","do_random",True)
    cli.append_arg(new_arg)
    # return False
    # return False
    new_arg = rc.Param("--nr_split ", "nr_split")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--size_split ", "split_size")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

#  As of relion-3.1, star_handler will write out a star file with the output nodes, which will be read by the pipeliner
def getCommandsSelectRankerJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    # return False
    # return False
    # return False
    cli.add_prog(rc.Prog("`which relion_class_ranker`"))
    new_arg = rc.Param("--opt ", "fn_model")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_model"].getString(), joboptions["fn_model"].nodetype,"fn_model")
    cli.add_innode(node)
    # output
    new_arg = rc.Param("--o ",outputname)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--fn_sel_parts particles.star --fn_sel_classavgs class_averages.star","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--select_min_nr_particles ", "select_nr_parts")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--select_min_nr_classes ", "select_nr_classes")
    cli.append_arg(new_arg)
    fn_parts = outputname+"particles.star"
    node2 = rc.Node(fn_parts, rh.LABEL_SELECT_PARTS)
    cli.add_outnode(node2)
    fn_imgs = outputname+"class_averages.star"
    node3 = rc.Node(fn_imgs, rh.LABEL_SELECT_CLAVS)
    cli.add_outnode(node3)
    new_arg = rc.Param("--fn_root rank","")
    fn_opt = outputname+"rank_optimiser.star"
    node4 = rc.Node(fn_opt, rh.LABEL_SELECT_OPT)
    cli.add_outnode(node4)
    new_arg = rc.Param("--do_granularity_features ","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--auto_select ","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--min_score ", "rank_threshold")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsSelectInteractiveJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    # return False
    new_arg = rc.Param("--gui --i ", "fn_model",assertion="required")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_model"].getString(), joboptions["fn_model"].nodetype,"fn_model")
    cli.add_innode(node)
    fn_parts = outputname+"particles.star"
    new_arg = rc.Param("--allow_save --fn_parts ",fn_parts)
    node2 = rc.Node(fn_parts, rh.LABEL_SELECT_PARTS)
    cli.add_outnode(node2)
    fn_imgs = outputname+"class_averages.star"
    new_arg = rc.Param("--fn_imgs ",fn_imgs)
    node3 = rc.Node(fn_imgs, rh.LABEL_SELECT_CLAVS)
    cli.add_outnode(node3)
    new_arg = rc.Flag("--recenter ","","do_recenter",True)
    new_arg = rc.Param("--gui --i ", "fn_mic",assertion="required")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_mic"].getString(), joboptions["fn_mic"].nodetype,"fn_mic")
    cli.add_innode(node)
    fn_mics = outputname+"micrographs.star"
    new_arg = rc.Param("--allow_save --fn_imgs ",fn_mics,"fn_mic","required")
    node2 = rc.Node(fn_mics, rh.LABEL_SELECT_MICS)
    cli.add_outnode(node2)
    new_arg = rc.Param("--gui --i ", "fn_data",assertion="required")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_data"].getString(), joboptions["fn_data"].nodetype,"fn_data")
    cli.add_innode(node)
    fn_parts = outputname+"particles.star"
    new_arg = rc.Flag("--allow_save --fn_imgs ", fn_parts,"fn_data","required")
    node2 = rc.Node(fn_parts, rh.LABEL_SELECT_PARTS)
    cli.add_outnode(node2)
    #         # return False
    new_arg = rc.Flag("--regroup ", "nr_groups","do_regroup",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsClass2DJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    cli.add_prog(rc.Prog("`which relion_refine_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_refine`","use_mpi",False))
    # return False
    # return False
    #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
    new_arg = rc.Param("--continue ", "fn_cont")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--o ",outputname + fn_run)
    # return False
    #     # return False
    new_arg = rc.Param("--iter ", "nr_iter_em")
    cli.append_arg(new_arg)
    # return False
    # return False
    new_arg = rc.Param("--grad --class_inactivity_threshold 0.1 --grad_write_iter 10","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--iter ", "nr_iter_grad")
    cli.append_arg(new_arg)
    # return False
    # return False
    outputNodes = getOutputNodesRefine(outputname + fn_run, "Class2D", my_iter, my_classes, 2, 1, is_tomo)
    #         # return False
    new_arg = rc.Param("--i ", "fn_img",assertion="required")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_img"].getString(), joboptions["fn_img"].nodetype,"fn_img")
    cli.add_innode(node)
    new_arg = rc.Flag("--dont_combine_weights_via_disc","","do_combine_thru_disc",False)
    new_arg = rc.Flag("--no_parallel_disc_io","","do_parallel_discio",False)
    new_arg = rc.Flag("--preread_images ", "","do_preread_images", True)
    new_arg = rc.Flag("--scratch_dir ","scratch_dir","scratch_dir",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pool ", "nr_pool")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pad","2")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ctf ","","do_ctf_correction",True)
    new_arg = rc.Param("--ctf_intact_first_peak ","","ctf_intact_first_peak",True)
    new_arg = rc.Param("--tau2_fudge ", "tau_fudge")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--particle_diameter ", "particle_diameter")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--K ", "nr_classes")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--flatten_solvent ","")
    new_arg = rc.Param("--zero_mask ","","do_zero_mask",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--strict_highres_exp ", "highres_limit","highres_limit","is_positive")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--center_classes ","","do_center",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--oversampling ",iover)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--skip_align ","","dont_skip_align",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--psi_step ","psi_sampling" * pow(2., iover),"dont_skip_align",True)
    # return False
    new_arg = rc.Param("--offset_range ", "offset_range")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--offset_step ","offset_step" * pow(2., iover))
    # return False
    new_arg = rc.Param("--allow_coarser_sampling","","allow_coarser",True)
    cli.append_arg(new_arg)        
    new_arg = rc.Param("--helical_outer_diameter ", "helical_tube_outer_diameter")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--bimodal_psi","","do_bimodal_psi",True)
    # return False
    new_arg = rc.Param("--sigma_psi ",floatToString(val / 3.))
    new_arg = rc.Param("--helix --helical_rise_initial ", "helical_rise")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--norm --scale ","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--j ", "nr_threads")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--gpu", "gpu_ids","use_gpu",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsInimodelJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
#        # return False
#           # return False
    command0.add_prog("rm -f " + outputname + 'RELION_JOB_EXIT_SUCCESS')
    cli.add_prog(rc.Prog("`which relion_refine`"))
    # return False
    #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
    new_arg = rc.Param("--continue ", "fn_cont")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--o " + outputname + fn_run)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--iter ", "nr_iter")
    cli.append_arg(new_arg)
    # return False
    # return False
    new_arg = rc.Param("--grad --denovo_3dref ","")
    # return False
    node1 = rc.Node( outputname + fn_run + "_optimisation_set.star", rh.LABEL_INIMOD_OPTSET)
    cli.add_outnode(node1)
    # return False
    new_arg = rc.Param("--sigma_tilt ", "sigma_tilt")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--i ", "fn_img")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_img"].getString(), joboptions["fn_img"].nodetype,"fn_img")
    cli.add_innode(node)
    new_arg = rc.Param("--ctf","","do_ctf_correction",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ctf_intact_first_peak","","ctf_intact_first_peak",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--K ", "nr_classes")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--sym C1 ","","do_run_C1",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--sym ","fn_sym","do_run_C1",False)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--flatten_solvent ","","do_solvent",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--zero_mask ","")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--dont_combine_weights_via_disc","","do_combine_thru_disc",False)
    new_arg = rc.Flag("--no_parallel_disc_io","","do_parallel_discio",False)
    new_arg = rc.Flag("--preread_images ", "","do_preread_images", True)
    new_arg = rc.Flag("--scratch_dir ","scratch_dir","scratch_dir",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pool ", "nr_pool")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pad","1")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--particle_diameter ", "particle_diameter")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--oversampling 1  --healpix_order 1  --offset_range 6  --offset_step 2 --auto_sampling ","")
    new_arg = rc.Param("--tau2_fudge ", "tau_fudge")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--j ", "nr_threads")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--gpu", "gpu_ids","use_gpu",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    fn_model.compose(outputname + fn_run + "_it", total_nr_iter,"",3)
    command2 += "--o " + outputname + "initial_model.mrc"
    cli.append_arg(new_arg)
    F = "touch " + outputname + RELION_JOB_EXIT_SUCCESS
    node2 = rc.Node(outputname + "initial_model.mrc", rh.LABEL_INIMOD_MAP)
    cli.add_outnode(node2)
    fn_tmp.compose(outputname + fn_run + "_it", total_nr_iter, "", 3)
    node3 = rc.Node (fn_tmp, rh.LABEL_INIMOD_MAP)
    cli.add_outnode(node3)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsClass3DJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    rc.Prog("`which relion_refine_mpi`","use_mpi",True)
    rc.Prog("`which relion_refine`","use_mpi",True)
    # return False
    #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
    new_arg = rc.Param("--continue ", "fn_cont")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--o ", outputname + fn_run)
    # return False
    # return False
    outputNodes = getOutputNodesRefine(outputname + fn_run, "Class3D", my_iter, my_classes, 3, 1, is_tomo)
    # return False
    node1 = rc.Node( outputname + fn_run + "_optimisation_set.star", rh.LABEL_CLASS3D_OPTSET)
    cli.add_outnode(node1)
    # return False
    new_arg = rc.Param("--sigma_tilt ", "sigma_tilt")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--i ", "fn_img")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_img"].getString(), joboptions["fn_img"].nodetype,"fn_img")
    cli.add_innode(node)
    # return False
    new_arg = rc.Param("--ref ", "fn_ref")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_ref"].getString(), joboptions["fn_ref"].nodetype,"fn_ref")
    cli.add_innode(node)
    new_arg = rc.Param("--firstiter_cc","","ref_correct_greyscale",False)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--trust_ref_size","","trust_ref_size",True)
    new_arg = rc.Param("--ini_high ", "ini_high",assertion="is_positive")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Flag("--dont_combine_weights_via_disc","","do_combine_thru_disc",False)
    new_arg = rc.Flag("--no_parallel_disc_io","","do_parallel_discio",False)
    new_arg = rc.Flag("--preread_images ", "","do_preread_images", True)
    new_arg = rc.Flag("--scratch_dir ","scratch_dir","scratch_dir",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pool ", "nr_pool")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pad","1","do_pad1",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pad","2", "do_pad1", False)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ctf","","do_ctf_correction",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ctf_intact_first_peak","","ctf_intact_first_peak",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--iter ", "nr_iter")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--tau2_fudge ", "tau_fudge")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--particle_diameter ", "particle_diameter")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--fast_subsets ","","do_fast_subsets",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--K ", "nr_classes")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--flatten_solvent","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--zero_mask","","do_zero_mask",True)
    new_arg = rc.Param("--strict_highres_exp ", "highres_limit",assertion="is_positive")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--blush ","","do_blush",True)
    new_arg = rc.Param("--solvent_mask ", "fn_mask",assertion="required")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_mask"].getString(), joboptions["fn_mask"].nodetype,"fn_mask")
    cli.add_innode(node)
    new_arg = rc.Param("--skip_align ","","dont_skip_align",True)
    new_arg = rc.Param("--oversampling ", iover)
    # return False
    new_arg = rc.Param("--healpix_order ",integerToString(sampling - iover))
    new_arg = rc.Param("--sigma_ang " + floatToString(joboptions["sigma_angles"].getNumber(error_message) / 3.))
    new_arg = rc.Param("--relax_sym ", "relax_sym",assertion="required")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--offset_range ", "offset_range")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--offset_step " +  floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover)))
    # return False
    new_arg = rc.Flag("--allow_coarser_sampling","","allow_coarser",True)
    cli.append_arg(new_arg)    
    new_arg = rc.Param("--sym ", "sym_name")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--norm --scale ","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helix","")
    # return False
    new_arg = rc.Param("--helical_inner_diameter ", "helical_tube_inner_diameter")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_outer_diameter ", "helical_tube_outer_diameter")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--helical_nr_asu ", "helical_nr_asu","do_apply_helical_symmetry",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_twist_initial ", "helical_twist_initial")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_rise_initial ", "helical_rise_initial")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--helical_z_percentage ",floatToString(myz))
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_symmetry_search","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_twist_min ", "helical_twist_min")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_twist_max ", "helical_twist_max")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--helical_twist_inistep ", "helical_twist_inistep")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_rise_min ", "helical_rise_min")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_rise_max ", "helical_rise_max")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--helical_rise_inistep ", "helical_rise_inistep")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ignore_helical_symmetry","")
    new_arg = rc.Param("--helical_keep_tilt_prior_fixed","","keep_tilt_prior_fixed",True)
    # return False
    new_arg = rc.Param("--sigma_tilt ",floatToString(val / 3.))
    # return False
    new_arg = rc.Param("--sigma_psi ", floatToString(val / 3.))
    # return False
    new_arg = rc.Param("--sigma_rot ", floatToString(val / 3.))
    # return False
    new_arg = rc.Param("--helical_sigma_distance ", floatToString(val / 3.))
    new_arg = rc.Param("--j ", "nr_threads")
    cli.append_arg(new_arg)
     # return False
    new_arg = rc.Param("--gpu", "gpu_ids","use_gpu",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsAutorefineJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    rc.Prog("`which relion_refine_mpi`","use_mpi",True)
    rc.Prog("`which relion_refine`","use_mpi",False)
    # return False
    # return False
    #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
    new_arg = rc.Param("--continue ", "fn_cont")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--o ", outputname + fn_run)
    cli.append_arg(new_arg)
    outputNodes = getOutputNodesRefine(outputname + fn_run, "Refine3D", -1, 1, 3, 1, is_tomo)
    new_arg = rc.Param("--auto_refine --split_random_halves")
    # return False
    node1 = rc.Node( outputname + fn_run + "_optimisation_set.star", rh.LABEL_REFINE3D_OPTSET)
    cli.add_outnode(node1)
    # return False
    new_arg = rc.Param("--sigma_tilt ", "sigma_tilt")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--i ", "fn_img")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_img"].getString(), joboptions["fn_img"].nodetype,"fn_img")
    cli.add_innode(node)
    # return False
    new_arg = rc.Param("--ref ", "fn_ref")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_ref"].getString(), joboptions["fn_ref"].nodetype,"fn_ref")
    cli.add_innode(node)
    new_arg = rc.Param("--firstiter_cc","","ref_correct_greyscale",False)
    new_arg = rc.Param("--trust_ref_size","","trust_ref_size")
    #         # return False
    new_arg = rc.Param("--ini_high ", "ini_high",assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--blush ","","do_blush",True)
    new_arg = rc.Flag("--dont_combine_weights_via_disc","","do_combine_thru_disc",False)
    new_arg = rc.Flag("--no_parallel_disc_io","","do_parallel_discio",False)
    new_arg = rc.Flag("--preread_images ", "","do_preread_images", True)
    new_arg = rc.Flag("--scratch_dir ","scratch_dir","scratch_dir",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pool ", "nr_pool")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pad","1","do_pad1",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pad","2", "do_pad1", False)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--auto_ignore_angles --auto_resol_angles","","auto_faster",True)
    new_arg = rc.Param("--ctf","","do_ctf_correction",True)
    new_arg = rc.Param("--ctf_intact_first_peak","","ctf_intact_first_peak",True)
    new_arg = rc.Param("--particle_diameter ", "particle_diameter")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--flatten_solvent","")
    new_arg = rc.Flag("--zero_mask","do_zero_mask",True)
    new_arg = rc.Param("--solvent_mask ", "fn_mask",assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--solvent_correct_fsc ","","do_solvent_fsc",True)
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_mask"].getString(), joboptions["fn_mask"].nodetype,"fn_mask")
    cli.add_innode(node)
    new_arg = rc.Param("--oversampling ",iover)
    # return False
    new_arg = rc.Param("--healpix_order ",integerToString(sampling - iover))
    # return False
    new_arg = rc.Param("--auto_local_healpix_order " ,integerToString(auto_local_sampling - iover))
    new_arg = rc.Param("--offset_range ", "offset_range")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--offset_step ",floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover)))
    # return False
    new_arg = rc.Param("--sym ", "sym_name")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--low_resol_join_halves","40")
    new_arg = rc.Param("--norm --scale ","")
    new_arg = rc.Param("--helix","")
    # return False
    new_arg = rc.Param("--helical_inner_diameter ", "helical_tube_inner_diameter")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_outer_diameter ", "helical_tube_outer_diameter")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_nr_asu ", "helical_nr_asu")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_twist_initial ", "helical_twist_initial")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_rise_initial ", "helical_rise_initial")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--helical_z_percentage ",floatToString(myz))
    new_arg = rc.Param("--helical_symmetry_search","")
    new_arg = rc.Param("--helical_twist_min ", "helical_twist_min")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_twist_max ", "helical_twist_max")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--helical_twist_inistep ", "helical_twist_inistep")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_rise_min ", "helical_rise_min")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helical_rise_max ", "helical_rise_max")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--helical_rise_inistep ", "helical_rise_inistep")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--ignore_helical_symmetry","")
    # return False
    new_arg = rc.Param("--sigma_tilt ", floatToString(val / 3.))
    # return False
    new_arg = rc.Param("--sigma_psi ", floatToString(val / 3.))
    # return False
    new_arg = rc.Param("--sigma_rot ", floatToString(val / 3.))
    # return False
    new_arg = rc.Param("--helical_sigma_distance ", floatToString(val / 3.))
    new_arg = rc.Param("--helical_keep_tilt_prior_fixed","","keep_tilt_prior_fixed", True)
    new_arg = rc.Param("--relax_sym ", "relax_sym")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--j ", "nr_threads")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--gpu", "gpu_ids","use_gpu",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsMultiBodyJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    # return False
    # return False
    # return False
    new_arg = rc.Param("--continue ", "fn_cont")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--o ", outputname + fn_run)
    outputNodes = getOutputNodesRefine(outputname + fn_run, "MultiBody", -1, 1, 3, nr_bodies, is_tomo)
    new_arg = rc.Param("--continue ", "fn_in")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--o ", outputname + fn_run)
    cli.append_arg(new_arg)
    outputNodes = getOutputNodesRefine(outputname + "run", "MultiBody", -1, 1, 3, nr_bodies, is_tomo)
    new_arg = rc.Param("--solvent_correct_fsc --multibody_masks ", "fn_bodies")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_in"].getString(), rh.LABEL_REFINE3D_OPT)
    cli.add_innode(node)
    new_arg = rc.Param("--oversampling ", floatToString(iover))
    # return False
    new_arg = rc.Param("--healpix_order ", integerToString(sampling - iover))
    cli.append_arg(new_arg)
    new_arg = rc.Param("--auto_local_healpix_order ", integerToString(sampling - iover))
    cli.append_arg(new_arg)
    new_arg = rc.Param("--offset_range ", "offset_range")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--offset_step " + floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover)))
    # return False
    new_arg = rc.Param("--blush ","","do_blush",True)
    new_arg = rc.Param("--reconstruct_subtracted_bodies ", "", "do_subtracted_bodies", True)
    new_arg = rc.Flag("--dont_combine_weights_via_disc","","do_combine_thru_disc",False)
    new_arg = rc.Flag("--no_parallel_disc_io","","do_parallel_discio",False)
    new_arg = rc.Flag("--preread_images ", "","do_preread_images", True)
    new_arg = rc.Flag("--scratch_dir ","scratch_dir","scratch_dir",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pool ", "nr_pool")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pad","1","do_pad1",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pad","2", "do_pad1", False)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--j ", "nr_threads")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--gpu", "gpu_ids","use_gpu",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    cli.add_prog(rc.Prog("`which relion_flex_analyse`"))
    fn_wildcard = outputname + "run*_model.star"
    error_message = "ERROR: cannot find appropriate model.star file in the output directory"
    # return False
    error_message = "ERROR: there are more than one model.star files (without '_it' specifiers) in the output directory. Move all but one out of the way."
    # return False
    fn_run = outputname + fn_run
    new_arg = rc.Param("--PCA_orient ","")
    new_arg = rc.Param("--model ",fn_run + "_model.star")
    new_arg = rc.Param("--data ", fn_run + "_data.star")
    new_arg = rc.Param("--bodies ", "fn_bodies")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--o ",outputname + "analyse")
    new_arg = rc.Param("--do_maps ","","nr_movies",assertion="is_positive")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--k ", "nr_movies",assertion="is_positive")
    cli.append_arg(new_arg)
    # return False
    # return False
    # return False
    # return False
    new_arg = rc.Param("--select_eigenvalue ", "select_eigenval")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--select_eigenvalue_min ", "eigenval_min")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--select_eigenvalue_max ", "eigenval_max")
    cli.append_arg(new_arg)
    #  Add output node: selected particles star file
    fnt = outputname + "analyse_eval" + integerToString(joboptions["select_eigenval"].getNumber(error_message),3)+"_select"
    # return False
    # return False
    # return False
    node2 = rc.Node (fnt, rh.LABEL_MULTIBODY_SEL_PARTS)
    cli.add_outnode(node2)
    node3 = rc.Node (outputname + "analyse_logfile.pdf", rh.LABEL_MULTIBODY_FLEXLOG)
    cli.add_outnode(node3)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsMaskcreateJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    #     # return False
    new_arg = rc.Param("--i ", "fn_in",assertion="required")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_in"].getString(), joboptions["fn_in"].nodetype,"fn_in")
    cli.add_innode(node)
    new_arg = rc.Param("--o ",outputname + "mask.mrc")
    cli.append_arg(new_arg)
    node2 = rc.Node (outputname + "mask.mrc", rh.LABEL_MASK3D_MASK)
    cli.add_outnode(node2)
    new_arg = rc.Param("--lowpass ", "lowpass_filter",assertion="is_positive")
    cli.append_arg(new_arg)
        # return False
    new_arg = rc.Param("--angpix ", "angpix",assertion="is_positive")
    cli.append_arg(new_arg)
        # return False
    new_arg = rc.Param("--ini_threshold ", "inimask_threshold")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--extend_inimask ", "extend_inimask")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--width_soft_edge ", "width_mask_edge")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--helix --z_percentage ", joboptions["helical_z_percentage"].getNumber(error_message) / 100.)
    # return False
    new_arg = rc.Param("--j ", "nr_threads")
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsJoinstarJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    # return False
    # return False
        # return False
    new_arg = rc.Param("--combine --i \" ", "fn_part1")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_part1"].getString(), joboptions["fn_part1"].nodetype)
    cli.add_innode(node)
    new_arg = rc.Param(" ", "fn_part2")
    cli.append_arg(new_arg)
    node2 = rc.Node(joboptions["fn_part2"].getString(), joboptions["fn_part2"].nodetype)
    cli.add_innode(node2)
    new_arg = rc.Param(" ", "fn_part3")
    cli.append_arg(new_arg)
    node3 = rc.Node(joboptions["fn_part3"], joboptions["fn_part3"].nodetype)
    cli.add_innode(node3)
    new_arg = rc.Param(" ", "fn_part4")
    cli.append_arg(new_arg)
    node4 = rc.Node(joboptions["fn_part4"].getString(), joboptions["fn_part4"].nodetype)
    cli.add_innode(node4)
    # new_arg = rc.Param(" \" "
    new_arg = rc.Param("--check_duplicates rlnImageName ","")
    new_arg = rc.Param("--o ", outputname + "join_particles.star")
    node5 = rc.Node (outputname + "join_particles.star", joboptions["fn_part1"].nodetype)
    cli.add_outnode(node5)
        # return False
    new_arg = rc.Param("--combine --i \" ", "fn_mic1")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_mic1"].getString(), joboptions["fn_mic1"].nodetype)
    cli.add_innode(node)
    new_arg = rc.Param(" ", "fn_mic2")
    cli.append_arg(new_arg)
    node2 = rc.Node(joboptions["fn_mic2"].getString(), joboptions["fn_mic2"].nodetype)
    cli.add_innode(node2)
    new_arg = rc.Param(" ", "fn_mic3")
    cli.append_arg(new_arg)
    node3 = rc.Node(joboptions["fn_mic3"].getString(), joboptions["fn_mic3"].nodetype)
    cli.add_innode(node3)
    new_arg = rc.Param(" ", "fn_mic4")
    cli.append_arg(new_arg)
    node4 = rc.Node(joboptions["fn_mic4"].getString(), joboptions["fn_mic4"].nodetype)
    cli.add_innode(node4)
    # new_arg = rc.Param(" \" "
    new_arg = rc.Param("--check_duplicates rlnMicrographName ","")
    new_arg = rc.Param("--o ", outputname + "join_mics.star")
    node5 = rc.Node(outputname + "join_mics.star", joboptions["fn_mic1"].nodetype)
    cli.add_outnode(node5)
        # return False
    new_arg = rc.Param("--combine --i \" ", "fn_mov1")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_mov1"].getString(), joboptions["fn_mov1"].nodetype)
    cli.add_innode(node)
    new_arg = rc.Param(" ", "fn_mov2")
    cli.append_arg(new_arg)
    node2 = rc.Node (joboptions["fn_mov2"].getStrin(), joboptions["fn_mov2"].nodetype)
    cli.add_innode(node2)
    new_arg = rc.Param(" ", "fn_mov3")
    cli.append_arg(new_arg)
    node3 = rc.Node(joboptions["fn_mov3"].getString(), joboptions["fn_mov3"].nodetype)
    cli.add_innode(node3)
    new_arg = rc.Param(" ", "fn_mov4")
    cli.append_arg(new_arg)
    node4 = rc.Node(joboptions["fn_mov4"].getString(), joboptions["fn_mov4"].nodetype)
    cli.add_innode(node4)
    # new_arg = rc.Param(" \" "
    new_arg = rc.Param("--check_duplicates rlnMicrographMovieName ","")
    new_arg = rc.Param("--o ", outputname + "join_movies.star")
    node5 = rc.Node(outputname + "join_movies.star", joboptions["fn_mov1"].nodetype)
    cli.add_outnode(node5)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsSubtractJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
        # return False
    node = rc.Node(joboptions["fn_fliplabel"].getString(), joboptions["fn_fliplabel"].nodetype,"fn_fliplabel")
    cli.add_innode(node)
    node2 = rc.Node(outputname + "original.star", rh.LABEL_SUBTRACT_REVERTED)
    cli.add_outnode(node2)
    cli.add_prog(rc.Prog("`which relion_particle_subtract`"))
    new_arg = rc.Param("--revert ", "fn_fliplabel")
    cli.append_arg(new_arg) + "--o " + outputname
        # return False
        # return False
    new_arg = rc.Param("--i ", "fn_opt")
    cli.append_arg(new_arg)
    node = rc.Node(joboptions["fn_opt"].getString(), rh.LABEL_OPTIMISER_CPIPE)
    cli.add_innode(node)
    new_arg = rc.Param("--mask ", "fn_mask")
    cli.append_arg(new_arg)
    node2 = rc.Node(joboptions["fn_mask"].getString(), joboptions["fn_mask"].nodetype,"fn_mask")
    cli.add_innode(node2)
            # return False
    new_arg = rc.Flag("--data ", "fn_data","do_data",True,assertion="required")
    cli.append_arg(new_arg)
    node3 = rc.Node (joboptions["fn_data"].getString(), joboptions["fn_data"].nodetype,"fn_data")
    cli.add_innode(node3)
    new_arg = rc.Param("--o ", outputname)
    node4 = rc.Node(outputname + "particles_subtracted.star", rh.LABEL_SUBTRACT_SUBTRACTED)
    cli.add_outnode(node4)
    new_arg = rc.Param("--recenter_on_mask","")
    new_arg = rc.Param("--center_x ", "center_x")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--center_y ", "center_y")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--center_z ", "center_z")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--float16 ","","do_float16",True)
    new_arg = rc.Param("--new_box ", "new_box")
    cli.append_arg(new_arg)
        # return False
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsPostprocessJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
        # return False
    new_arg = rc.Param("--mask ", "fn_mask")
    cli.append_arg(new_arg)
    node3 = rc.Node (joboptions["fn_mask"].getString(), joboptions["fn_mask"].nodetype,"fn_mask")
    cli.add_innode(node3)
        # return False
            # return False
    node = rc.Node (fn_half1, joboptions["fn_in"].nodetype,"fn_in")
    cli.add_innode(node)
    new_arg = rc.Param("--i ", fn_half1)
    #  The output name contains a directory: use it for output
    new_arg = rc.Param("--o ", outputname + "postprocess")
    cli.append_arg(new_arg)
    new_arg = rc.Param("  --angpix ", "angpix")
    cli.append_arg(new_arg)
    node1 = rc.Node(outputname+"postprocess.mrc", rh.LABEL_POST_MAP)
    cli.add_outnode(node1)
    node2 = rc.Node(outputname+"postprocess_masked.mrc", rh.LABEL_POST_MASKED)
    cli.add_outnode(node2)
    node2b = rc.Node(outputname+"logfile.pdf", rh.LABEL_POST_LOG)
    cli.add_outnode(node2b)
    node2c = rc.Node (outputname+"postprocess.star", rh.LABEL_POST_POST)
    cli.add_outnode(node2c)
    new_arg = rc.Param("--mtf ", "fn_mtf")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--mtf_angpix ", "mtf_angpix")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--auto_bfac ","","do_auto_bfac",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--autob_lowres ", "autob_lowres")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--adhoc_bfac ", "adhoc_bfac","do_adhoc_bfac",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--skip_fsc_weighting ","","do_skip_fsc_weighting",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--low_pass " , "low_pass")
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script


def getCommandsLocalresJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    # return False
    # return False
    # return False
    node = rc.Node(joboptions["fn_in"].getString(), joboptions["fn_in"].nodetype,"fn_in")
    cli.add_innode(node)
    # return False
    # return False
    # return False
    # return False
    # return False
    #  Make symbolic links to the half-maps in the output directory
    cli.add_prog(rc.Prog("ln -s ../../" + fn_half1 + " " + outputname + "half1.mrc"))
    cli.add_prog(rc.Prog("ln -s ../../" + fn_half2 + " " + outputname + "half2.mrc"))
    node2 = rc.Node(joboptions["fn_mask"].getString(), joboptions["fn_mask"].nodetype,"fn_mask")
    cli.add_innode(node2)
    node3 = rc.Node(outputname + "half1_resmap.mrc", rh.LABEL_LOCRES_RESMAP)
    cli.add_outnode(node3)
    new_arg = rc.Param("--maskVol=", "fn_mask")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--noguiSplit ",outputname + "half1.mrc " +  outputname + "half2.mrc")
    new_arg = rc.Param("--vxSize=", "angpix")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--pVal=", "pval")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--minRes=", "minres")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--maxRes=", "maxres")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--stepRes=", "stepres")
    cli.append_arg(new_arg)
    # return False
    new_arg = rc.Param("--locres --i ", "fn_in")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--o ", outputname + "relion")
    new_arg = rc.Param("--angpix ", "angpix")
    cli.append_arg(new_arg)
    # new_arg = rc.Param("--locres_sampling ", "locres_sampling")
    # cli.append_arg(new_arg)
    # new_arg = rc.Param("--locres_randomize_at ", "randomize_at")
    # cli.append_arg(new_arg)
    new_arg = rc.Param("--adhoc_bfac ", "adhoc_bfac")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--mtf ", "fn_mtf",assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--mask ", "fn_mask")
    cli.append_arg(new_arg)
    node0 = rc.Node (outputname+"histogram.pdf", rh.LABEL_LOCRES_LOG)
    cli.add_outnode(node0)
    node1 = rc.Node(outputname+"relion_locres_filtered.mrc", rh.LABEL_LOCRES_FILTMAP)
    cli.add_outnode(node1)
    node2 = rc.Node(outputname+"relion_locres.mrc", rh.LABEL_LOCRES_RESMAP)
    cli.add_outnode(node2)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsDynaMightJob(joboptions,outputname, label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    node = rc.Node(joboptions["fn_star"].getString(), joboptions["fn_star"].nodetype,"fn_star")
    cli.add_innode(node)
    node2 = rc.Node (joboptions["fn_map"].getString(), joboptions["fn_map"].nodetype,"fn_map")
    cli.add_innode(node2)
# cli.append_arg(new_arg) != "")
#                 rc.Node node3(joboptions["fn_mask")
# cli.append_arg(new_arg), joboptions["fn_mask"].nodetype,"fn_mask")
#         cli.add_innode(node3)
        # return False
        # return False
    new_arg = rc.Param(" optimize-deformations ","")
    new_arg = rc.Param("--refinement-star-file ", "fn_star")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--output-directory ", outputname)
    new_arg = rc.Param("--initial-model ", "fn_map")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--n-gaussians ", "nr_gaussians")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--initial-threshold ", "initial_threshold",assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--regularization-factor " , "reg_factor")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--n-threads ", "nr_threads")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--preload-images ","","do_preload",True)
    #     new_arg = rc.Param("--mask-file ", "fn_mask")
    # cli.append_arg(new_arg)
    new_arg = rc.Param(" explore-latent-space ",outputname,"do_visualize",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--half-set ", "halfset","do_visualize",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--checkpoint-file ", "fn_checkpoint","do_visualize",True,assertion="required")
    cli.append_arg(new_arg)
        #     new_arg = rc.Param("--mask-file ", "fn_mask")
        # cli.append_arg(new_arg)
    new_arg = rc.Param(" optimize-inverse-deformations ", outputname,"do_inverse",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--n-epochs ", "nr_epochs")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--checkpoint-file ", "fn_checkpoint",assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--save-deformations ","","do_store_deform",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--preload-images","","do_preload",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag(" deformable-backprojection ", outputname,"do_reconstruct",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--batch-size ", "backproject_batchsize")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--checkpoint-file ", "fn_checkpoint",assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--preload-images","","do_preload",True)
    cli.append_arg(new_arg)
        #     new_arg = rc.Param("--mask-file ", "fn_mask")
        #     cli.append_arg(new_arg)
    onode = rc.Node (outputname + "backprojection/map_half1.mrc", rh.LABEL_DYNAMIGHT_HALFMAP)
    cli.add_outnode(onode)
    onode2 = rc.Node (outputname + "backprojection/map_half2.mrc", rh.LABEL_DYNAMIGHT_HALFMAP)
    cli.add_outnode(onode2)
    new_arg = rc.Param("--gpu-id ", "gpu_id",assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    # return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message, true)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsModelAngeloJob(joboptions,outputname, label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    outputmodel = outputname
    outputmodel = (outputmodel.afterFirstOf("/")).beforeLastOf("/")
    outputmodel = outputname + outputmodel + ".cif"
    #  Only run model building for new job or if output.cif is not there yet.
    if not is_continue or not exists(outputmodel):
        node = rc.Node(joboptions["fn_map"].getString(), joboptions["fn_map"].nodetype,"fn_map")
        cli.add_innode(node)
    cli.add_prog(rc.Prog(joboptions["fn_modelangelo_exe"]))
    cli.append_arg(new_arg)
    new_arg = rc.Param(" build ","")
    node2 = rc.Node (joboptions["p_seq"].getString(), joboptions["p_seq"].nodetype,"p_seq")
    cli.add_innode(node2)
    new_arg = rc.Param(" -pf ", "p_seq",assertion="is_field_empty")
    cli.append_arg(new_arg)
    node2 = rc.Node(joboptions["d_seq"].getString(), joboptions["d_seq"].nodetype,"d_seq")
    cli.add_innode(node2)
    new_arg = rc.Param(" -df ", "d_seq",assertion="required")
    cli.append_arg(new_arg)
    node2 = rc.Node (joboptions["r_seq"].getString(), joboptions["r_seq"].nodetype,"r_seq")
    cli.add_innode(node2)
    new_arg = rc.Param(" -rf ", "r_seq",assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Param(" build_no_seq ","")
    cli.append_arg(new_arg)   
    new_arg = rc.Param(" -v ", "fn_map")
    cli.append_arg(new_arg)
    new_arg = rc.Param(" -o ",outputname)
    new_arg = rc.Param(" -d ", "gpu_id")
    cli.append_arg(new_arg)
    node3 = rc.Node(outputmodel, rh.LABEL_ATOMCOORDS_CPIPE)
    cli.add_outnode(node3)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
        # return False
    command2 += " -i " + outputname
    command2 += " -o " + outputname
    # return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message, true)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsMotionrefineJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    cli.add_prog(rc.Prog("`which relion_motion_refine_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_motion_refine`","use_mpi",False))
        # return False
        # return False
        # return False
        # return False
        # return False
        # return False
            # return False
    node = rc.Node(joboptions["fn_data"].getString(), joboptions["fn_data"].nodetype,"fn_data")
    cli.add_innode(node)
    node2 = rc.Node (joboptions["fn_post"].getString(), joboptions["fn_post"].nodetype,"fn_post")
    cli.add_innode(node)
    new_arg = rc.Param("--i ", "fn_data")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--f ", "fn_post")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--corr_mic ", "fn_mic")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--first_frame ", "first_frame")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--last_frame ", "last_frame")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--o ", outputname)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--float16 ","","do_float16",True)
            # return False
    new_arg = rc.Param("--min_p ", "optim_min_part")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--eval_frac ", "eval_frac")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--align_frac ", floatToString(align_frac))
    cli.append_arg(new_arg)        
    new_arg = rc.Flag("--params2 ","","sigma_acc","is_lt",0)
    new_arg = rc.Flag("--params3 ","","sigma_acc","is_ge",0)
        # return False
    node5 = rc.Node(outputname+"opt_params_all_groups.txt", rh.LABEL_POLISH_PARAMS)
    cli.add_outnode(node5)
    new_arg = rc.Param("--s_vel ", "sigma_vel","do_own_params",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--s_div ", "sigma_div","do_own_params",True)
    cli.append_arg(new_arg)
    new_arg = rc.Param("--s_acc ", "sigma_acc","do_own_params",True)
    cli.append_arg(new_arg)
        # return False
    new_arg = rc.Param("--params_file ", "opt_params",assertion="required")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--combine_frames","")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--bfac_minfreq ", "minres")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--bfac_maxfreq ", "maxres")
    cli.append_arg(new_arg)
    # return False
    # return False
    # return False
    # return False
    new_arg = rc.Param("--window ", "extract_size")
    cli.append_arg(new_arg)
    # return False
    # return False
    new_arg = rc.Param("--scale ", "rescale")
    cli.append_arg(new_arg)
    node6 = rc.Node(outputname+"logfile.pdf", rh.LABEL_POLISH_LOG)
    cli.add_outnode(node6)
    node7 = rc.Node (outputname+"shiny.star", rh.LABEL_POLISH_PARTS)
    cli.add_outnode(node7)
    new_arg = rc.Param("--only_do_unfinished ","")
    new_arg = rc.Param("--j ", "nr_threads")
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

def getCommandsCtfrefineJob(joboptions,outputname,label="none", job_counter=-1):
    script, cli = clear(label)
    initialisePipeline(outputname, job_counter)
    cli.add_prog(rc.Prog("`which relion_ctf_refine_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_ctf_refine`","use_mpi",False))
        # return False
        # return False
            # return False
            # return False
    node = rc.Node(joboptions["fn_data"].getString(), joboptions["fn_data"].nodetype,"fn_data")
    cli.add_innode(node)
    node2 = rc.Node (joboptions["fn_post"].getString(), joboptions["fn_post"].nodetype,"fn_post")
    cli.add_innode(node)
    node6 = rc.Node (outputname+"logfile.pdf", rh.LABEL_CTFREFINE_LOG)
    cli.add_outnode(node6)
    new_arg = rc.Param("--i ", "fn_data")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--f ", "fn_post")
    cli.append_arg(new_arg)
    new_arg = rc.Param("--o ", outputname)
    new_arg = rc.Flag("--fit_aniso","","do_aniso_mag",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--kmin_mag ", "minres","do_aniso_mag",True)
    cli.append_arg(new_arg)
    node5 = rc.Node (outputname+"particles_ctf_refine.star", rh.LABEL_CTFREFINE_ANISOPARTS)
    cli.add_outnode(node5)
    node5 = rc.Node(outputname+"particles_ctf_refine.star", rh.LABEL_CTFREFINE_REFINEPARTS)
    cli.add_outnode(node5)
    new_arg = rc.Param("--fit_defocus --kmin_defocus ", "minres")
    cli.append_arg(new_arg)
        # return False
    new_arg = rc.Param("--fit_mode ", fit_options)
    new_arg = rc.Flag("--fit_beamtilt","","do_tilt",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--kmin_tilt ", "minres","do_tilt",True)
    cli.append_arg(new_arg)
    new_arg = rc.Flag("--odd_aberr_max_n","3""do_trefoil",True)
    new_arg = rc.Param("--fit_aberr","","do_4thorder",True)
    new_arg = rc.Param("--only_do_unfinished ","")
    new_arg = rc.Param("--j ", "nr_threads")
    cli.append_arg(new_arg)
    new_arg = rc.Param(" ", "other_args")
    cli.append_arg(new_arg)
    new_arg = rc.Param(f" --pipeline-control {outputname}", "")
    cli.append_arg(new_arg)
    return script

# def getCommandsExternalJob(joboptions,outputname,label="none", job_counter=-1):
#     script, cli = clear(label)
#     initialisePipeline(outputname, job_counter)
#     cli.append_arg(new_arg) == "")
#         # return False
#     cli.append_arg(new_arg)
#     new_arg = rc.Param("--o " + outputname
#     cli.append_arg(new_arg) != "")
#             node = rc.Node(joboptions["in_mov")
#     cli.append_arg(new_arg), joboptions["in_mov"].nodetype,"in_mov")
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_movies ", "in_mov")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             node = rc.Node(joboptions["in_mic")
#     cli.append_arg(new_arg), joboptions["in_mic"].nodetype,"in_mic")
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_mics ", "in_mic")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             node = rc.Node(joboptions["in_part")
#     cli.append_arg(new_arg), joboptions["in_part"].nodetype,"in_part")
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_parts ", "in_part")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             node = rc.Node(joboptions["in_coords")
#     cli.append_arg(new_arg), joboptions["in_coords"].nodetype,"in_coords")
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_coords ", "in_coords")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             node = rc.Node(joboptions["in_3dref")
#     cli.append_arg(new_arg), joboptions["in_3dref"].nodetype)
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_3dref ", "in_3dref")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             node = rc.Node(joboptions["in_mask")
#     cli.append_arg(new_arg), joboptions["in_mask"].nodetype,"in_mask")
#         cli.add_innode(node)
#         new_arg = rc.Param("--in_mask ", "in_mask")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             new_arg = rc.Param("--", "param1_label")
#     cli.append_arg(new_arg) + " ", "param1_value")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             new_arg = rc.Param("--", "param2_label")
#     cli.append_arg(new_arg) + " ", "param2_value")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             new_arg = rc.Param("--", "param3_label")
#     cli.append_arg(new_arg) + " ", "param3_value")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             new_arg = rc.Param("--", "param4_label")
#     cli.append_arg(new_arg) + " ", "param4_value")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             new_arg = rc.Param("--", "param5_label")
#     cli.append_arg(new_arg) + " ", "param5_value")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             new_arg = rc.Param("--", "param6_label")
#     cli.append_arg(new_arg) + " ", "param6_value")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             new_arg = rc.Param("--", "param7_label")
#     cli.append_arg(new_arg) + " ", "param7_value")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             new_arg = rc.Param("--", "param8_label")
#     cli.append_arg(new_arg) + " ", "param8_value")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             new_arg = rc.Param("--", "param9_label")
#     cli.append_arg(new_arg) + " ", "param9_value")
#     cli.append_arg(new_arg)
#     cli.append_arg(new_arg) != "")
#             new_arg = rc.Param("--", "param10_label")
#     cli.append_arg(new_arg) + " ", "param10_value")
#     cli.append_arg(new_arg)
#     new_arg = rc.Param("--j ", "nr_threads")
#     cli.append_arg(new_arg)
#     new_arg = rc.Param(" ", "other_args")
#     cli.append_arg(new_arg)
#     return script



# Main
if __name__ == '__main__' :
    import relion_spa_gui as rjo
    import relion_option as rho
    import relion_build_menus as rmu
    import relion_window as rwi

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
        tool = rmu.create_tool('rln_mc',['io','settings','log','dataviz'])
        # 2. Read the joboptions
        hidden_name,jo = rjo.initialiseMotioncorrJob(False)
        # 3. Read the commands
        outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/${RELION_NEW_JOB}/'
        prog = getCommandsMotioncorrJob(jo,outputname)
        # 4. Build
        groups = rwi.initialiseMotioncorrWindow()
        for fs_params in groups:
            tool = rmu.update_fieldset(tool, fs_params, jo, keys_rln)

        tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, prog, system_rln)

        # 5. Write the file `xx.star`
        rmu.write_starfile(tool,'./grinder/public/spa/02_preprocess/99.star',has_mpi, has_thread)

        #####   UCSF implementation
        # 1. Create tool and tabs
        tool = rmu.create_tool('ucsf_mc',['io','settings','log','dataviz'])
        # 2. Read the joboptions
        hidden_name,jo = rjo.initialiseMotioncorrJob(False)
        # 3. Build
        groups = rwi.initialiseMotioncorrWindow()
        for fs_params in groups:
            tool = rmu.update_fieldset(tool,   fs_params,jo,keys_ucsf)

        tool = update_system_fieldset(tool, has_mpi, has_thread,  groups.groups[0], jo, prog, system_ucsf)

        # 4. Read the commands
        # outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/RELION_NEW_JOB'
        # prog = rcmd.getCommandsMotioncorrJob(outputname,rh.PROC_MOTIONCORR)
        # 5. Create the `outdata`` fieldset
        # 6. Create the script
        # 7. Write the file `xx.star`
        rmu.write_starfile(tool,'./grinder/public/spa/02_preprocess/98.star',has_mpi, has_thread)


    is_tomo = False
    _,jo = rjo.initialiseMotioncorrJob(is_tomo)
    print(jo["input_star_mics"])
    outputname =  rh.proc_type2dirname(rh.PROC_MOTIONCORR) + '/${RELION_NEW_JOB}/'
    result = getCommandsMotioncorrJob(jo,outputname)
    print(result)
    print(result.commands[0].outnodes)

    initialiseMotioncorrJob()