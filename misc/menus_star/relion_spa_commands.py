import relion_h as rh
# import relion_option as ro
import relion_command as rc


def initialisePipeline(outputname,job_counter):
    job_counter += 1
    outputname = ""
    

def clear(labelnew):
    _cli = rc.CLI()
    _cli.id = labelnew
  

def getCommandsImportJobRaw(outputname, label, job_counter=-1):

  
    cli = clear(label)
    
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
    nod = rc.Node(outputname + fn_out, rh.rh.LABEL_IMPORT_MOVIES)
    new_arg = rc.Flag("--do_movies","","is_multiframe", True )
    new_arg.add_outnode(nod)
    cli.args.append(new_arg)

    fn_out = "micrographs.star"
    nod = rc.Node(outputname + fn_out, rh.rh.LABEL_IMPORT_MICS)
    new_arg = rc.Flag("--do_micrographs","","is_multiframe",  False)
    new_arg.add_outnode(nod)
    cli.args.append(new_arg)

#    USELESS
#    optics_group = get_str("optics_group_name")
#    if not optics_group:
#        error_message = "ERROR: please specify an optics group name."
#        return "", "", error_message
    
    new_arg = rc.Param("--optics_group_name", "optics_group_name", assertion="is_field_not_empty")
    cli.args.append(new_arg)
        
    fn_mtf = get_str("fn_mtf")
    # if len(fn_mtf) > 0:
    new_arg = rc.Param("--optics_group_mtf","fn_mtf", assertion="is_field_not_empty")
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

    return cli


def getCommandsImportJobOther(outputname, label, job_counter=-1):
    
    cli = clear(label)
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
        outputNodes.append(Node(outputname + fn_out, rh.rh.LABEL_IMPORT_COORDS))
        new_arg = rc.Param(" --do_coordinates "
    else:
        fn_out = os.path.basename(fn_in)
        
        mynodetype = ""
        if node_type == "Particles STAR file (.star)":
            mynodetype = rh.rh.LABEL_IMPORT_PARTS
        elif node_type == "Multiple (2D or 3D) references (.star or .mrcs)":
            mynodetype = rh.rh.LABEL_IMPORT_2DIMG
        elif node_type == "3D reference (.mrc)":
            mynodetype = rh.rh.LABEL_IMPORT_MAP
        elif node_type == "3D mask (.mrc)":
            mynodetype = rh.rh.LABEL_IMPORT_MASK
        elif node_type == "Micrographs STAR file (.star)":
            mynodetype = rh.rh.LABEL_IMPORT_MICS
        elif node_type == "Unfiltered half-map (unfil.mrc)":
            mynodetype = rh.rh.LABEL_IMPORT_HALFMAP
        else:
            error_message = "Unrecognized menu option for node_type = " + node_type
            return "", "", error_message
        
        outputNodes.append(Node(outputname + fn_out, mynodetype))
        
        if mynodetype == rh.rh.LABEL_HALFMAP_CPIPE or mynodetype == rh.rh.LABEL_IMPORT_HALFMAP:
            fn_inb = os.path.basename(fn_in)
            if "half1" in fn_inb:
                fn_inb = fn_inb.replace("half1", "half2")
            elif "half2" in fn_inb:
                fn_inb = fn_inb.replace("half2", "half1")
            
            outputNodes.append(Node(outputname + fn_inb, mynodetype))
            new_arg = rc.Param(" --do_halfmaps"
        
        elif mynodetype == rh.rh.LABEL_PARTS_CPIPE or mynodetype == rh.rh.LABEL_IMPORT_PARTS:
                new_arg = rc.Param(" --do_particles"
                optics_group = get_str("optics_group_particles")
                if optics_group:
                    new_arg = rc.Param(' --optics_group_name "' + optics_group + '"'

    return cli
    
    
# Generate the correct commands
def getCommandsImportMovieJob(joboptions, do_makedir, job_counter):

    cli = clear(label)
    initialisePipeline(outputname, job_counter)

    command = rc.JobCommand("relion_import.movies",joboptions)

    fn_in = joboptions["fn_in_raw"]

    # if fn_in.rfind("../") != None: # Forbid at any place
    # error_message = "ERROR: don't import files outside the project directory.\nPlease make a symbolic link by an absolute path before importing."
    command.error("fn_in_raw","PATH_IN_PROJECTDIR")

#    if fn_in.rfind("/", 0) == 0: # Forbid only at the beginning
#        error_message = "ERROR: please import files by a relative path.\nIf you want to import files outside the project directory, make a symbolic link by an absolute path and\nimport the symbolic link by a relative path."
#        return False
    command.error("fn_in_raw","PATH_RELATIVE")

    # Import movies
    command.output( "movies.star","rh.LABEL_IMPORT_MOVIES")
    command.add("param", "--do_movies")

    optics_group = joboptions["optics_group_name"]
#    if optics_group == "":
#        error_message = "ERROR: please specify an optics group name."
#        return False
    command.error("optics_group_name","FIELD_REQUIRED")
    command.error("optics_group_name","FIELD_VALID")
    
#    if not optics_group.validateCharactersStrict(True): # True means: do_allow_double_dollar (for scheduler)
#        error_message = "ERROR: an optics group name may contain only numbers, alphabets and hyphen(-)."
#        return False

    command.add("param", "--optics_group_name ","optics_group_name")
#    if len(joboptions["fn_mtf"]) > 0:
    command.add("flag", "--optics_group_mtf ","fn_mtf","is_not_empty")
    
    command.add("param", "--angpix ","angpix")
    command.add("param", "--kV ","kV")
    command.add("param", "--Cs ","Cs")
    command.add("param", "--Q0 ","Q0")
    command.add("param", "--beamtilt_x ","beamtilt_x")
    command.add("param", "--beamtilt_y ","beamtilt_y")
    return command
    
# Generate the correct commands
def getCommandsImportMicroGraphJob(, job_counter):

    cli = clear(label)
    initialisePipeline(outputname, job_counter)

    command = rc.JobCommand("relion_import.movies",joboptions)

    fn_in = joboptions["fn_in_raw"]

    # if fn_in.rfind("../") != None: # Forbid at any place
    # error_message = "ERROR: don't import files outside the project directory.\nPlease make a symbolic link by an absolute path before importing."
    command.error("fn_in_raw","PATH_IN_PROJECTDIR")

    if fn_in.rfind("/", 0) == 0: # Forbid only at the beginning
        error_message = "ERROR: please import files by a relative path.\nIf you want to import files outside the project directory, make a symbolic link by an absolute path and\nimport the symbolic link by a relative path."
        return False

    fn_out = "micrographs.star"
    command.output("fn_out", "rh.LABEL_IMPORT_MICS")
    command.add("param", "--do_micrographs")
    
    optics_group = joboptions["optics_group_name"]
    if optics_group == "":
        error_message = "ERROR: please specify an optics group name."
        return False
    
    if not optics_group.validateCharactersStrict(True): # True means: do_allow_double_dollar (for scheduler)
        error_message = "ERROR: an optics group name may contain only numbers, alphabets and hyphen(-)."
        return False
    

    command.add("param", "--optics_group_name ","optics_group")
    if len(joboptions["fn_mtf"]) > 0:
        command.add("param", "--optics_group_mtf ","fn_mtf")
    
    command.add("param", "--angpix ","angpix")
    command.add("param", "--kV ","kV")
    command.add("param", "--Cs ","Cs")
    command.add("param", "--Q0 ","Q0")
    command.add("param", "--beamtilt_x ","beamtilt_x")
    command.add("param", "--beamtilt_y ","beamtilt_y")
    return command
    
# Generate the correct commands
def getCommandsImportOtherJob(outputname,label, job_counter=-1):

    cli = clear(label)
    initialisePipeline(outputname, job_counter)

    fn_in = joboptions["fn_in_other"]
    node_type = joboptions["node_type"]
    if node_type == "Particle coordinates (*.box, *_pick.star)":
        # Make a suffix file, which contains the actual suffix as a suffix
        # Get the coordinate-file suffix
        fn_out = "coords_suffix" + fn_in.afterLastOf("*")
        rc.Node node(outputname + fn_out, rh.LABEL_IMPORT_COORDS)
        outputNodes.push_back(node)
        command.add("param", "--do_coordinates")
    else:
        fn_out = "/" + fn_in
        fn_out = fn_out.afterLastOf("/")

        std::string mynodetype
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
            return False


        rc.Node node(outputname + fn_out, mynodetype)
        outputNodes.push_back(node)

        # Also get the other half-map
        if mynodetype == rh.LABEL_HALFMAP_CPIPE::
            FileName fn_inb = "/" + fn_in
            size_t pos = fn_inb.find("half1")
            if pos != std::string::npos:
                fn_inb.replace(pos, 5, "half2")
            else:
                pos = fn_inb.find("half2")
                if pos != std::string::npos:
                    fn_inb.replace(pos, 5, "half1")
                
            fn_inb = fn_inb.afterLastOf("/")
            rc.Node node2(outputname + fn_inb, mynodetype)
            outputNodes.push_back(node2)
            command.add("param", "--do_halfmaps")
        
        elif mynodetype == rh.LABEL_PARTS_CPIPE:
            command.add("--do_particles")
            FileName optics_group = joboptions["optics_group_particles"]
            if optics_group != "":
                if not optics_group.validateCharactersStrict():
                    error_message = "ERROR: an optics group name may contain only numbers, alphabets and hyphen(-)."
                    return False
                
                command.add("--particles_optics_group_name",optics_group)
        else:
            command.add("param", "--do_other")


    # Now finish the command call to relion_import program, which does the actual copying
    command.add("param", "--i","fn_in")
    command.add("param", "--odir","outputname")
    command.add("param", "--ofile", "fn_out")

    if is_continue:
        command.add("param", "--continue")

    return command
    

def getCommandsMotioncorrJob_Own(outputname,label,job_counter=-1):

    cli = clear(label)
    initialisePipeline(outputname, job_counter)

    cli.add_prog(rc.Prog("`which relion_run_motioncorr_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_run_motioncorr`","use_mpi",False))

    #  I/O
#    if joboptions["input_star_mics"] == ""):
#        error_message = "ERROR: empty field for input STAR file..."
#        return false
    new_arg = rc.Param(" --i ", "input_star_mics",assertion="is_field_not_empty")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["input_star_mics"].getString(), joboptions["input_star_mics"].node_type)
    inputNodes.push_back(node)

    new_arg = rc.Param(" --o ",outputname)
    cli.args.append(new_arg)

    rc.Node node2(outputname + "corrected_micrographs.star", rh.LABEL_MOCORR_MICS)
    outputNodes.push_back(node2)
    node4 = rc.Node(jo(outputname + "logfile.pdf", rh.LABEL_MOCORR_LOG)
    outputNodes.push_back(node4)

    new_arg = rc.Param(" --first_frame_sum ", "first_frame_sum")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --last_frame_sum ", "last_frame_sum")
    cli.args.append(new_arg)

#   if joboptions["do_own_motioncor"].getBoolean():
    new_arg = rc.Param(" --use_own "," ")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --j ", "nr_threads")
    cli.args.append(new_arg)
#    if joboptions["do_float16"].getBoolean())
                if !joboptions["do_save_ps"].getBoolean())
                        error_message = "When writing to float16, you have to write power spectra for CTFFIND-4.1."
            return false
        
    new_arg = rc.Param(" --float16","")
    cli.args.append(new_args)
    
#   if (joboptions["fn_defect"].length() > 0)
    new_arg = rc.Param(" --defect_file ", "fn_defect",assertion="is_field_not_empty")
    cli.args.append(new_arg)

    new_arg = rc.Param(" --bin_factor ", "bin_factor")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --bfactor ", "bfactor")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --dose_per_frame ", "dose_per_frame")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --preexposure ", "pre_exposure")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --patch_x ", "patch_x")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --patch_y ", "patch_y")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --eer_grouping ", "eer_grouping")
    cli.args.append(new_arg)

#   if joboptions["group_frames"].getNumber(error_message) > 1.)
    new_arg = rc.Param(" --group_frames ", "group_frames",assertion="is_positive")
    cli.args.append(new_arg)

#    if (joboptions["fn_gain_ref"].length() > 0)
#        int gain_rot = -1, gain_flip = -1
#        for (int i = 0 i <= 3 i++)
#            if strcmp((joboptions["gain_rot"].c_str(), job_gain_rotation_options[i].c_str()) == 0)
#                gain_rot = i
#                break
#                    
#        for (int i = 0 i <= 2 i++)
#            if strcmp((joboptions["gain_flip"]flip_options[i].c_str()) == 0)
#                gain_flip = i
#                break
#                    
#        if gain_rot == -1 || gain_flip == -1)
#            REPORT_ERROR("Illegal gain_rot and/or gain_flip.")

    new_arg = rc.Param(" --gainref ", "fn_gain_ref")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --gain_rot ","gain_rot",assertion="is_positive")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --gain_flip ","gain_flip",assertion="is_positive")
    cli.args.append(new_arg)
    
#    if !is_tomo && joboptions["do_dose_weighting"].getBoolean())
    new_arg = rc.Flag(" --dose_weighting ","do_dose_weighting",True)
#   if joboptions["do_save_noDW"].getBoolean())
    new_arg = rc.Flag(" --save_noDW ","do_save_noDW",True)
            
#   if joboptions["do_save_ps"].getBoolean())
#        if !joboptions["do_own_motioncor"].getBoolean())
#              error_message = "'Save sum of power spectra' is not available with UCSF MotionCor2."
#        return false
        
        
# Calculation must be done in a wrapper to RELION_MOTIONCOR
"""
        dose_for_ps = joboptions["group_for_ps"].getNumber(error_message)
        if error_message != "") return false

        float dose_rate = 1.0
        if (!is_tomo)
                dose_rate = joboptions["dose_per_frame"].getNumber(error_message)
                if error_message != "") return false
        if (dose_rate <= 0)
                    error_message = "Please specify the dose rate to calculate the grouping for power spectra."
            return false
                if dose_for_ps <= 0)
                    error_message = "Invalid dose for the grouping for power spectra."
            return false
        
        int grouping_for_ps = ROUND(dose_for_ps / dose_rate)
        if grouping_for_ps == 0)
            grouping_for_ps = 1

        new_arg = rc.Param(" --grouping_for_ps ","grouping_for_ps")
"""

#    if (is_continue)
    new_arg = rc.Param(" --only_do_unfinished ","is_continue", True)

    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return cli
    
def getCommandsMotioncorrJob_MC2(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)

    
    rc.Prog("`which relion_run_motioncorr_mpi`","use_mpi",True)
    rc.Prog("`which relion_run_motioncorr`","use_mpi",False)

    #  I/O
#    if joboptions["input_star_mics"] == ""):
#        error_message = "ERROR: empty field for input STAR file..."
#        return false
    new_arg = rc.Param(" --i ", "input_star_mics",assertion="is_field_not_empty")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["input_star_mics"].getString(), joboptions["input_star_mics"].node_type)
    inputNodes.push_back(node)

    new_arg = rc.Param(" --o ",outputname)
    cli.args.append(new_arg)

    rc.Node node2(outputname + "corrected_micrographs.star", rh.LABEL_MOCORR_MICS)
    outputNodes.push_back(node2)
    node4 = rc.Node(jo(outputname + "logfile.pdf", rh.LABEL_MOCORR_LOG)
    outputNodes.push_back(node4)

    new_arg = rc.Param(" --first_frame_sum ", "first_frame_sum")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --last_frame_sum ", "last_frame_sum")
    cli.args.append(new_arg)

    # MotionCor2
    cli.label(".motioncor2","do_own_motioncor",False)

    new_arg = rc.Param(" --use_motioncor2 ","do_own_motioncor",False)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --motioncor2_exe ", "fn_motioncor2_exe")
    cli.args.append(new_arg)

#   USELESS
#   if joboptions["do_float16"].getBoolean())
#       error_message = "ERROR: MotionCor2 cannot write float16 files."
#       return false
        
#    if (joboptions["other_motioncor2_args").length() > 0)
    new_arg = rc.Param(" --other_motioncor2_args ", "other_motioncor2_args",assertion="is_field_not_empty")
    cli.args.append(new_arg)

    #  Which GPUs to use?
    new_arg = rc.Param(" --gpu \"", "gpu_ids")
    cli.args.append(new_arg) + "\""
    
#   if (joboptions["fn_defect"].length() > 0)
    new_arg = rc.Param(" --defect_file ", "fn_defect",assertion="is_positive")
    cli.args.append(new_arg)

    new_arg = rc.Param(" --bin_factor ", "bin_factor")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --bfactor ", "bfactor")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --dose_per_frame ", "dose_per_frame")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --preexposure ", "pre_exposure")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --patch_x ", "patch_x")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --patch_y ", "patch_y")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --eer_grouping ", "eer_grouping")
    cli.args.append(new_arg)

#   if joboptions["group_frames"].getNumber(error_message) > 1.)
    new_arg = rc.Param(" --group_frames ", "group_frames",assertion="is_positive")
    cli.args.append(new_arg)

#    if (joboptions["fn_gain_ref"].length() > 0)
#        int gain_rot = -1, gain_flip = -1
#        for (int i = 0 i <= 3 i++)
#            if strcmp((joboptions["gain_rot"].c_str(), job_gain_rotation_options[i].c_str()) == 0)
#                gain_rot = i
#                break
#                    
#        for (int i = 0 i <= 2 i++)
#            if strcmp((joboptions["gain_flip"]flip_options[i].c_str()) == 0)
#                gain_flip = i
#                break
#                    
#        if gain_rot == -1 || gain_flip == -1)
#            REPORT_ERROR("Illegal gain_rot and/or gain_flip.")

    new_arg = rc.Param(" --gainref ", "fn_gain_ref")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --gain_rot ","gain_rot",assertion="is_positive")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --gain_flip ","gain_flip",assertion="is_positive")
    cli.args.append(new_arg)
    
#    if !is_tomo && joboptions["do_dose_weighting"].getBoolean())
    new_arg = rc.Flag(" --dose_weighting ","do_dose_weighting",True)
#   if joboptions["do_save_noDW"].getBoolean())
    new_arg = rc.Flag(" --save_noDW ","do_save_noDW",True)
            
#   if joboptions["do_save_ps"].getBoolean())
#        if !joboptions["do_own_motioncor"].getBoolean())
#              error_message = "'Save sum of power spectra' is not available with UCSF MotionCor2."
#        return false
        
        
# Calculation must be done in a wrapper to RELION_MOTIONCOR
"""
        dose_for_ps = joboptions["group_for_ps"].getNumber(error_message)
        if error_message != "") return false

        float dose_rate = 1.0
        if (!is_tomo)
                dose_rate = joboptions["dose_per_frame"].getNumber(error_message)
                if error_message != "") return false
        if (dose_rate <= 0)
                    error_message = "Please specify the dose rate to calculate the grouping for power spectra."
            return false
                if dose_for_ps <= 0)
                    error_message = "Invalid dose for the grouping for power spectra."
            return false
        
        int grouping_for_ps = ROUND(dose_for_ps / dose_rate)
        if grouping_for_ps == 0)
            grouping_for_ps = 1

        new_arg = rc.Param(" --grouping_for_ps ","grouping_for_ps")
"""

#    if (is_continue)
    new_arg = rc.Param(" --only_do_unfinished ","is_continue", True)

    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return cli
    

def getCommandsCtffindJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    outputName = outputname
    if is_tomo)
            rc.Node node(outputname + "tilt_series_ctf.star", rh.LABEL_CTFFIND_TOMOGRAMS)
        outputNodes.push_back(node)
        else
            rc.Node node(outputname + "micrographs_ctf.star", rh.LABEL_CTFFIND_MICS)
        outputNodes.push_back(node)
    
    #  PDF with histograms of the eigenvalues
    rc.Node node3(outputname + "logfile.pdf", rh.LABEL_CTFFIND_LOG)
    outputNodes.push_back(node3)

    rc.Prog("`which relion_run_ctffind_mpi`","use_mpi",True)
    rc.Prog("`which relion_run_ctffind`","use_mpi",False)

    #  I/O
#    if joboptions["input_star_mics"] == "")
#            error_message = "ERROR: empty field for input STAR file..."
#        return false
    new_arg = rc.Param(" --i ", "input_star_mics",assertion="is_field_not_empty")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["input_star_mics"].getString(), joboptions["input_star_mics"].node_type)
    inputNodes.push_back(node)

    new_arg = rc.Param(" --o ",outputname)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --Box ", "box")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --ResMin ", "resmin")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --ResMax ", "resmax")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --dFMin ", "dfmin")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --dFMax ", "dfmax")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --FStep ", "dfstep")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --dAst ", "dast")
    cli.args.append(new_arg)

#   if joboptions["use_noDW"].getBoolean():
    new_arg = rc.Flag(" --use_noDW ","use_noDW",True)

#   if joboptions["do_phaseshift"].getBoolean())
    new_arg = rc.True(" --do_phaseshift ","do_phaseshift",True)
    new_arg = rc.Flag(" --phase_min ", "phase_min","do_phaseshift",True)
    cli.args.append(new_arg)
    new_arg = rc.Flag(" --phase_max ", "phase_max","do_phaseshift",True)
    cli.args.append(new_arg)
    new_arg = rc.Flag(" --phase_step ", "phase_step","do_phaseshift",True)
    cli.args.append(new_arg)
    
    label += ".ctffind4"

    new_arg = rc.Param(" --ctffind_exe ", "fn_ctffind_exe")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --ctfWin ", "ctf_win")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --is_ctffind4 "
#   if !joboptions["slow_search"].getBoolean())
    new_arg = rc.Flag(" --fast_search ","slow_search",True)
#   if joboptions["use_given_ps"].getBoolean())
    new_arg = rc.Param(" --use_given_ps ","use_given_ps",True)

    new_arg = rc.Param(" --only_do_unfinished ","is_continue",True)

    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    return cli

def getCommandsManualpickJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    cli.add_prog(rc.Prog("`which relion_manualpick`")

#    if joboptions["fn_in"] == "")
#            error_message = "ERROR: empty field for input STAR file..."
#        return false
    
    new_arg = rc.Param(" --i ", "fn_in",assertion="is_field_not_empty")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["fn_in"].getString(), joboptions["fn_in"].node_type)
    inputNodes.push_back(node)

    new_arg = rc.Param(" --odir ", outputname)
    new_arg = rc.Param(" --pickname manualpick","")

    #  Allow saving, and always save default selection file upon launching the program
    FileName fn_outstar = outputname + "micrographs_selected.star"
    rc.Node node3(fn_outstar, rh.LABEL_MANPICK_MICS)
    outputNodes.push_back(node3)
    new_arg = rc.Param(" --allow_save --fast_save --selection " + fn_outstar

    new_arg = rc.Param(" --scale ", "micscale")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --sigma_contrast ", "sigma_contrast")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --black ", "black_val")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --white ", "white_val")
    cli.args.append(new_arg)

#   if joboptions["do_topaz_denoise"].getBoolean())
    new_arg = rc.Flag(" --topaz_denoise","do_topaz_denoise",True)
#   if joboptions["lowpass"].getNumber(error_message) > 0.)
    new_arg = rc.Param(" --lowpass ", "lowpass",assertion="is_positive")
    cli.args.append(new_arg)
#   if joboptions["highpass"].getNumber(error_message) > 0.)
    new_arg = rc.Param(" --highpass ", "highpass", assertion="is_positive")
    cli.args.append(new_arg)
#   if joboptions["angpix"].getNumber(error_message) > 0.)
    new_arg = rc.Param(" --angpix ", "angpix", assertion="is_positive")
    cli.args.append(new_arg)

#   if joboptions["do_fom_threshold"].getBoolean())
    new_arg = rc.Flag(" --minimum_pick_fom ", "minimum_pick_fom","do_fom_threshold",True)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --particle_diameter ", "diameter")
    cli.args.append(new_arg)

#    if joboptions["do_startend"].getBoolean())
#            label += ".helical"

#        new_arg = rc.Param(" --pick_start_end ","do_startend",True)

#        #  new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
#        rc.Node node2(outputname + "manualpick.star", rh.LABEL_MANPICK_COORDS_HELIX)
#        outputNodes.push_back(node2)
#    
#    else
        #  new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
    node2 = rc.Node(outputname + "manualpick.star", rh.LABEL_MANPICK_COORDS)
    outputNodes.push_back(node2)
    
#    if joboptions["do_color"].getBoolean())
    new_arg = rc.Param(" --color_label ", "color_label","do_color",True)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --blue ", "blue_value")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --red ", "red_value")
    cli.args.append(new_arg)
#   if joboptions["fn_color"].length() > 0)
    new_arg = rc.Param(" --color_star ", "","fn_color",True)
    cli.args.append(new_arg)
    
    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return cli

def getCommandsAutopickJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)

    
    if is_continue && joboptions["continue_manual"].getBoolean())
    
        label += ".continuemanual"

        cli.prog(rc.Prog("`which relion_manualpick`"))

        new_arg = rc.Param(" --i ", "fn_input_autopick")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --odir " + outputname
        new_arg = rc.Param(" --pickname autopick"

        node = rc.Node(joboptions["fn_input_autopick")
    cli.args.append(new_arg), joboptions["fn_input_autopick"].node_type)
        inputNodes.push_back(node)

        #  Output new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
        rc.Node node2(outputname + "autopick.star", rh.LABEL_AUTOPICK_COORDS)
        outputNodes.push_back(node2)

        #  The output micrographs selection
        FileName fn_outstar = outputname + "micrographs_selected.star"
        rc.Node node3(fn_outstar, rh.LABEL_AUTOPICK_MICS)
        outputNodes.push_back(node3)
        new_arg = rc.Param(" --allow_save  --selection " + fn_outstar

        #  A manualpicker jobwindow for display of micrographs....
        FileName fn_job = ".gui_manualpick"
        if exists(fn_job+"job.star") || exists(fn_job+"run.job"))
                    RelionJob manualpickjob
            bool iscont = false
            manualpickjob.read(fn_job.c_str(), iscont, true) #  true means do initialise

            new_arg = rc.Param(" --scale " + manualpickjob.joboptions["micscale")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --sigma_contrast " + manualpickjob.joboptions["sigma_contrast")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --black " + manualpickjob.joboptions["black_val")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --white " + manualpickjob.joboptions["white_val")
    cli.args.append(new_arg)

            if manualpickjob.joboptions["do_startend"].getBoolean())
                            new_arg = rc.Param(" --pick_start_end "
                        if manualpickjob.joboptions["do_topaz_denoise"].getBoolean())
                            new_arg = rc.Param(" --topaz_denoise "
                        else
                            std::string error_message = ""
                float mylowpass = manualpickjob.joboptions["lowpass"].getNumber(error_message)
                if mylowpass > 0.)
                    new_arg = rc.Param(" --lowpass " + manualpickjob.joboptions["lowpass")
    cli.args.append(new_arg)

                float myhighpass = manualpickjob.joboptions["highpass"].getNumber(error_message)
                if myhighpass > 0.)
                    new_arg = rc.Param(" --highpass " + manualpickjob.joboptions["highpass")
    cli.args.append(new_arg)

                float myangpix = manualpickjob.joboptions["angpix"].getNumber(error_message)
                if myangpix > 0.)
                    new_arg = rc.Param(" --angpix " + manualpickjob.joboptions["angpix")
    cli.args.append(new_arg)
            
            new_arg = rc.Param(" --particle_diameter " + manualpickjob.joboptions["diameter")
    cli.args.append(new_arg)
            if manualpickjob.joboptions["do_fom_threshold"].getBoolean())
                            new_arg = rc.Param(" --minimum_pick_fom " + manualpickjob.joboptions["minimum_pick_fom")
    cli.args.append(new_arg)
            
            if manualpickjob.joboptions["do_color"].getBoolean())
                            new_arg = rc.Param(" --color_label " + manualpickjob.joboptions["color_label")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --blue " + manualpickjob.joboptions["blue_value")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --red " + manualpickjob.joboptions["red_value")
    cli.args.append(new_arg)
                if manualpickjob.joboptions["fn_color")
    cli.args.append(new_arg).length() > 0)
                    new_arg = rc.Param(" --color_star " + manualpickjob.joboptions["fn_color")
    cli.args.append(new_arg)
            
                else
                    #  Just use some defaults if no .gui_manualpickjob.star exists
            new_arg = rc.Param(" --scale","0.25")
            new_arg = rc.Param(" --sigma_contrast", "3")
            new_arg = rc.Param(" --lowpass","20")
            new_arg = rc.Param(" --particle_diameter","100")
        
        else
            #  Run autopicking
        if joboptions["nr_mpi"].getNumber(error_message) > 1)
            command="`which relion_autopick_mpi`"
        else
            command="`which relion_autopick`"
        if error_message != "") return false

        #  Input
        int icheck = 0
        if joboptions["do_log"].getBoolean()) icheck++
        if joboptions["do_topaz"].getBoolean()) icheck++
        if joboptions["do_refs"].getBoolean()) icheck++

        if  icheck != 1)
                    error_message = "ERROR: On the I/O tab specify (only) one of three methods: template-matching, LoG or topaz ..."
            return false
        
        if joboptions["fn_input_autopick")
    cli.args.append(new_arg) == "" )
                    error_message = "ERROR: empty field for input STAR file..."
            return false
        
        new_arg = rc.Param(" --fn_topaz_exe ", "fn_topaz_exe")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --i ", "fn_input_autopick")
    cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_input_autopick")
    cli.args.append(new_arg), joboptions["fn_input_autopick"].node_type)
        inputNodes.push_back(node)

        if !(joboptions["do_topaz"].getBoolean() && joboptions["do_topaz_train"].getBoolean()))
        
            #  Output new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
            rc.Node node3(outputname + "autopick.star", rh.LABEL_AUTOPICK_COORDS)
            outputNodes.push_back(node3)

            #  PDF with histograms of the eigenvalues
            rc.Node node3b(outputname + "logfile.pdf", rh.LABEL_AUTOPICK_LOG)
            outputNodes.push_back(node3b)
        
        new_arg = rc.Param(" --odir " + outputname
        new_arg = rc.Param(" --pickname autopick"

        if joboptions["do_topaz"].getBoolean())
        
            label += ".topaz"

            icheck = 0
            if joboptions["do_topaz_train"].getBoolean()) icheck++
            if joboptions["do_topaz_pick"].getBoolean()) icheck++
            if  icheck != 1)
                            error_message = "ERROR: On the Topaz tab specify (only) one of two methods: training or picking..."
                return false
            
            if joboptions["topaz_particle_diameter"].getNumber(error_message) > 0.)
                new_arg = rc.Param(" --particle_diameter ", "topaz_particle_diameter")
    cli.args.append(new_arg)
            if error_message != "") return false

            if joboptions["do_topaz_train"].getBoolean())
            
                label += ".train"

                if !joboptions["use_gpu"].getBoolean())
                                    error_message ="ERROR: For Topaz training, specify which GPUs to use on the autopicking tab for Topaz picking GPU usage is optional"
                    return false
                
                new_arg = rc.Param(" --topaz_train"

                if joboptions["topaz_nr_particles"].getNumber(error_message) > 0.)
                    new_arg = rc.Param(" --topaz_nr_particles ", "topaz_nr_particles")
    cli.args.append(new_arg)
                if error_message != "") return false

                if joboptions["do_topaz_train_parts"].getBoolean())
                                    new_arg = rc.Param(" --topaz_train_parts ", "topaz_train_parts")
    cli.args.append(new_arg)
                    #  Output new version: no longer save coords_suffix nodetype, but 2-column list of micrographs and coordinate files
                    rc.Node nodet(outputname + "input_training_coords.star", rh.LABEL_COORDS_CPIPE)
                    outputNodes.push_back(nodet)

                                else
                                    new_arg = rc.Param(" --topaz_train_picks ", "topaz_train_picks")
    cli.args.append(new_arg)
                
                        else if joboptions["do_topaz_pick"].getBoolean())
                            label += ".pick"

                new_arg = rc.Param(" --topaz_extract"
                if joboptions["topaz_model")
    cli.args.append(new_arg) != "")
                    new_arg = rc.Param(" --topaz_model ", "topaz_model")
    cli.args.append(new_arg)

                if joboptions["do_topaz_filaments"].getBoolean())
                                    new_arg = rc.Param(" --helix "
                    new_arg = rc.Param(" --topaz_threshold ", "topaz_filament_threshold")
    cli.args.append(new_arg)
                    if joboptions["topaz_hough_length"].getNumber(error_message) > 0.)
                                            new_arg = rc.Param(" --helical_tube_length_min ", "topaz_hough_length")
    cli.args.append(new_arg)
                                    
            
            if (joboptions["topaz_other_args")
    cli.args.append(new_arg)).length() > 0)
                new_arg = rc.Param(" --topaz_args \" ", "topaz_other_args")
    cli.args.append(new_arg) + " \""

            #  GPU-stuff
            if joboptions["use_gpu"].getBoolean())
                            new_arg = rc.Param(" --gpu \"", "gpu_ids")
    cli.args.append(new_arg) + "\""
            
                else if joboptions["do_log"].getBoolean())
                    if joboptions["use_gpu"].getBoolean())
                            error_message ="ERROR: The Laplacian-of-Gaussian picker does not support GPU."
                return false
            
            label += ".log"

            new_arg = rc.Param(" --LoG "
            new_arg = rc.Param(" --LoG_diam_min ", "log_diam_min")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --LoG_diam_max ", "log_diam_max")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --shrink 0 --lowpass ", "log_maxres")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --LoG_adjust_threshold ", "log_adjust_thr")
    cli.args.append(new_arg)
            if joboptions["log_upper_thr"].getNumber(error_message) < 999.)
                new_arg = rc.Param(" --LoG_upper_threshold ", "log_upper_thr")
    cli.args.append(new_arg)
            if error_message != "") return false

            if joboptions["log_invert"].getBoolean())
                new_arg = rc.Param(" --Log_invert "
                else if joboptions["do_refs"].getBoolean())
                    if joboptions["do_ref3d"].getBoolean())
            
                if joboptions["fn_ref3d_autopick")
    cli.args.append(new_arg) == "")
                                    error_message ="ERROR: empty field for 3D reference..."
                    return false
                
                label += ".ref3d"

                new_arg = rc.Param(" --ref ", "fn_ref3d_autopick")
    cli.args.append(new_arg)
                rc.Node node2(joboptions["fn_ref3d_autopick")
    cli.args.append(new_arg), rh.LABEL_MAP_CPIPE)
                inputNodes.push_back(node2)
                new_arg = rc.Param(" --sym ", "ref3d_symmetry")
    cli.args.append(new_arg)

                #  Sampling
                int ref3d_sampling = JobOption::getHealPixOrder(joboptions["ref3d_sampling")
    cli.args.append(new_arg))
                if ref3d_sampling <= 0)
                                    error_message = "Wrong choice for ref3d_sampling"
                    return false
                
                new_arg = rc.Param(" --healpix_order " + integerToString(ref3d_sampling)
                        else
                            if joboptions["fn_refs_autopick")
    cli.args.append(new_arg) == "")
                                    error_message ="ERROR: empty field for references..."
                    return false
                
                label += ".ref2d"

                new_arg = rc.Param(" --ref ", "fn_refs_autopick")
    cli.args.append(new_arg)
                rc.Node node2(joboptions["fn_refs_autopick")
    cli.args.append(new_arg), rh.LABEL_2DIMGS_CPIPE)
                inputNodes.push_back(node2)
            
            if joboptions["do_invert_refs"].getBoolean())
                new_arg = rc.Param(" --invert "

            if joboptions["do_ctf_autopick"].getBoolean())
                            new_arg = rc.Param(" --ctf "
                if joboptions["do_ignore_first_ctfpeak_autopick"].getBoolean())
                    new_arg = rc.Param(" --ctf_intact_first_peak "
                        new_arg = rc.Param(" --ang ", "psi_sampling_autopick")
    cli.args.append(new_arg)

            new_arg = rc.Param(" --shrink ", "shrink")
    cli.args.append(new_arg)
            if joboptions["lowpass"].getNumber(error_message) > 0.)
                new_arg = rc.Param(" --lowpass ", "lowpass")
    cli.args.append(new_arg)
            if error_message != "") return false

            if joboptions["highpass"].getNumber(error_message) > 0.)
                new_arg = rc.Param(" --highpass ", "highpass")
    cli.args.append(new_arg)
            if error_message != "") return false

            if joboptions["angpix"].getNumber(error_message) > 0.)
                new_arg = rc.Param(" --angpix ", "angpix")
    cli.args.append(new_arg)
            if error_message != "") return false

            if joboptions["angpix_ref"].getNumber(error_message) > 0.)
                new_arg = rc.Param(" --angpix_ref ", "angpix_ref")
    cli.args.append(new_arg)
            if error_message != "") return false

            new_arg = rc.Param(" --threshold ", "threshold_autopick")
    cli.args.append(new_arg)
            if joboptions["do_pick_helical_segments"].getBoolean())
                new_arg = rc.Param(" --min_distance " + floatToString(joboptions["helical_nr_asu"].getNumber(error_message) * joboptions["helical_rise"].getNumber(error_message))
            else
                new_arg = rc.Param(" --min_distance ", "mindist_autopick")
    cli.args.append(new_arg)
            if error_message != "") return false

            new_arg = rc.Param(" --max_stddev_noise ", "maxstddevnoise_autopick")
    cli.args.append(new_arg)
            if joboptions["minavgnoise_autopick"].getNumber(error_message) > -900.)
                new_arg = rc.Param(" --min_avg_noise ", "minavgnoise_autopick")
    cli.args.append(new_arg)
            if error_message != "") return false

            #  Helix
            if joboptions["do_pick_helical_segments"].getBoolean())
                            new_arg = rc.Param(" --helix"
                if joboptions["do_amyloid"].getBoolean())
                    new_arg = rc.Param(" --amyloid"
                new_arg = rc.Param(" --helical_tube_outer_diameter ", "helical_tube_outer_diameter")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --helical_tube_kappa_max ", "helical_tube_kappa_max")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --helical_tube_length_min ", "helical_tube_length_min")
    cli.args.append(new_arg)
            
            #  GPU-stuff
            if joboptions["use_gpu"].getBoolean())
                            #  for the moment always use --shrink 0 with GPUs ...
                new_arg = rc.Param(" --gpu \"", "gpu_ids")
    cli.args.append(new_arg) + "\""
            
        
        if joboptions["do_refs"].getBoolean() || joboptions["do_log"].getBoolean())
        
            #  Although mainly for debugging, LoG-picking does have write/read_fom_maps...
            if joboptions["do_write_fom_maps"].getBoolean())
                new_arg = rc.Param(" --write_fom_maps "

            if joboptions["do_read_fom_maps"].getBoolean())
                new_arg = rc.Param(" --read_fom_maps "

            if is_continue && !(joboptions["do_read_fom_maps"].getBoolean() || joboptions["do_write_fom_maps"].getBoolean()))
                new_arg = rc.Param(" --only_do_unfinished "
                else if joboptions["do_topaz"].getBoolean())
                    if is_continue)
                new_arg = rc.Param(" --only_do_unfinished "
            
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return cli

def getCommandsExtractJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    cli.add_prog(rc.Prog("`which relion_preprocess_mpi`","use_mpi",True))
    cli.add_prog(rc.Prog("`which relion_preprocess`","use_mpi",True))

    #  Input
#    if joboptions["star_mics") == "")
#            error_message = "ERROR: empty field for input STAR file..."
#        return false
    new_arg = rc.Param(" --i ", "star_mics",assertion="is_field_not_empty")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["star_mics"].getString(), joboptions["star_mics"].node_type)
    inputNodes.push_back(node)

    if joboptions["do_reextract"].getBoolean())
            if joboptions["fndata_reextract")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for refined particles STAR file..."
            return false
        
        if joboptions["do_reset_offsets"].getBoolean() && joboptions["do_recenter"].getBoolean())
                    error_message = "ERROR: you cannot both reset refined offsets and recenter on refined coordinates, choose one..."
            return false
        
        label += ".reextract"

        new_arg = rc.Param(" --reextract_data_star ", "fndata_reextract")
    cli.args.append(new_arg)
        rc.Node node2(joboptions["fndata_reextract")
    cli.args.append(new_arg), joboptions["fndata_reextract"].node_type)
        inputNodes.push_back(node2)
        if joboptions["do_reset_offsets"].getBoolean())
                    new_arg = rc.Param(" --reset_offsets"
                else if joboptions["do_recenter"].getBoolean())
                    new_arg = rc.Param(" --recenter"
            new_arg = rc.Param(" --recenter_x ", "recenter_x")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --recenter_y ", "recenter_y")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --recenter_z ", "recenter_z")
    cli.args.append(new_arg)
                else
            FileName mylist = joboptions["coords_suffix")
    cli.args.append(new_arg)
        if mylist == "")
                    error_message = "ERROR: empty field for coordinate STAR file..."
            return false
                #  Attempt at backwards compatibility
        if mylist.contains("coords_suffix"))
                    new_arg = rc.Param(" --coord_dir " + mylist.beforeLastOf("/") + "/"
            new_arg = rc.Param(" --coord_suffix " + (mylist.afterLastOf("/")).without("coords_suffix")
                else
                    new_arg = rc.Param(" --coord_list " + mylist
                rc.Node node2(mylist, joboptions["coords_suffix"].node_type)
        inputNodes.push_back(node2)
    
    #  Output
    FileName fn_ostar = outputname + "particles.star"

    new_arg = rc.Param(" --part_star " + fn_ostar

    if joboptions["do_reextract"].getBoolean())
            FileName fn_pickstar = outputname + "extractpick.star"
        rc.Node node(fn_pickstar, rh.LABEL_EXTRACT_COORDS_REEX)
        outputNodes.push_back(node)
        new_arg = rc.Param(" --pick_star " + fn_pickstar
    
    if joboptions["do_extract_helix"].getBoolean() && joboptions["do_extract_helical_tubes"].getBoolean())
            FileName fn_pickstar = outputname + "extractpick.star"
        rc.Node node(fn_pickstar, rh.LABEL_EXTRACT_COORDS_HELIX)
        outputNodes.push_back(node)
        new_arg = rc.Param(" --pick_star " + fn_pickstar
    

    new_arg = rc.Param(" --part_dir " + outputname
    new_arg = rc.Param(" --extract"
    new_arg = rc.Param(" --extract_size ", "extract_size")
    cli.args.append(new_arg)

    if joboptions["do_fom_threshold"].getBoolean())
            new_arg = rc.Param(" --minimum_pick_fom ", "minimum_pick_fom")
    cli.args.append(new_arg)
    
    if joboptions["do_float16"].getBoolean())
            new_arg = rc.Param(" --float16 "
    
    #  Operate stuff
    #  Get an integer number for the bg_radius
    RFLOAT bg_radius = (joboptions["bg_diameter"].getNumber(error_message) < 0.) ? 0.75 * joboptions["extract_size"].getNumber(error_message) : joboptions["bg_diameter"].getNumber(error_message)
    if error_message != "") return false

    bg_radius /= 2. #  Go from diameter to radius
    if joboptions["do_rescale"].getBoolean())
            new_arg = rc.Param(" --scale ", "rescale")
    cli.args.append(new_arg)
        bg_radius *= joboptions["rescale"].getNumber(error_message)
        if error_message != "") return false

        bg_radius /= joboptions["extract_size"].getNumber(error_message)
        if error_message != "") return false
        if joboptions["do_norm"].getBoolean())
            #  Get an integer number for the bg_radius
        bg_radius = (int)bg_radius
        new_arg = rc.Param(" --norm --bg_radius " + floatToString(bg_radius)
        new_arg = rc.Param(" --white_dust ", "white_dust")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --black_dust ", "black_dust")
    cli.args.append(new_arg)
        if joboptions["do_invert"].getBoolean())
        new_arg = rc.Param(" --invert_contrast "

    #  Helix
    if joboptions["do_extract_helix"].getBoolean())
            rc.Node node3(fn_ostar, rh.LABEL_EXTRACT_PARTS_HELIX)
        outputNodes.push_back(node3)

        label += ".helical"

        new_arg = rc.Param(" --helix"
        new_arg = rc.Param(" --helical_outer_diameter ", "helical_tube_outer_diameter")
    cli.args.append(new_arg)
        if joboptions["helical_bimodal_angular_priors"].getBoolean())
            new_arg = rc.Param(" --helical_bimodal_angular_priors"
        if joboptions["do_extract_helical_tubes"].getBoolean())
                    new_arg = rc.Param(" --helical_tubes"
            if joboptions["do_cut_into_segments"].getBoolean())
                            new_arg = rc.Param(" --helical_cut_into_segments"
                new_arg = rc.Param(" --helical_nr_asu ", "helical_nr_asu")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --helical_rise ", "helical_rise")
    cli.args.append(new_arg)
                        else
                new_arg = rc.Param(" --helical_nr_asu 1 --helical_rise 1"
                else
            rc.Node node3(fn_ostar, rh.LABEL_EXTRACT_PARTS)
        outputNodes.push_back(node3)
    

    if is_continue)
        new_arg = rc.Param(" --only_do_unfinished "


    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    

    if joboptions["do_reextract"].getBoolean())
            rc.Node node(outputname + "reextract.star", rh.LABEL_EXTRACT_COORDS_REEX)
        outputNodes.push_back(node)
    
    if joboptions["do_extract_helix"].getBoolean() && joboptions["do_extract_helical_tubes"].getBoolean())
            rc.Node node(outputname + "helix_segments.star", rh.LABEL_EXTRACT_COORDS_HELIX)
        outputNodes.push_back(node)
    

    return cli

def getCommandsSelectJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    if joboptions["fn_model")
    cli.args.append(new_arg) == "" &&
            joboptions["fn_mic")
    cli.args.append(new_arg) == "" && joboptions["fn_data")
    cli.args.append(new_arg) == "")
            #  Nothing was selected...
        error_message = "Please select an input file."
        return false
    
    int c = 0
    if joboptions["do_select_values"].getBoolean()) c++
    if joboptions["do_discard"].getBoolean()) c++
    if joboptions["do_split"].getBoolean()) c++
    if joboptions["do_remove_duplicates"].getBoolean()) c++
    if joboptions["do_filaments"].getBoolean()) c++
    if c > 1)
            error_message = "You cannot do many tasks simultaneously..."
        return false
    
    if joboptions["do_filaments"].getBoolean())
            label += ".filamentsdendrogram"
        command="`which relion_filament_selection`"

        if joboptions["fn_mic")
    cli.args.append(new_arg) != "" || joboptions["fn_data")
    cli.args.append(new_arg) != "")
                    error_message = "ERROR: Filament selection by dendrogram analysis is only possible for optimiser STAR files..."
            return false
        
        if joboptions["fn_model")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: Filament selection by dendrogram analysis needs an optimiser STAR file..."
            return false
        
         node = rc.Node(joboptions["fn_model")
    cli.args.append(new_arg), joboptions["fn_model"].node_type)
        inputNodes.push_back(node)

        FileName fn_out = outputname + "run_optimiser.star"
        rc.Node node2(fn_out, rh.LABEL_SELECT_OPT)
        outputNodes.push_back(node2)

        rc.Node node3(outputname + "logfile.pdf", rh.LABEL_SELECT_LOG)
        outputNodes.push_back(node3)

        new_arg = rc.Param(" -i ", "fn_model")
    cli.args.append(new_arg)
        new_arg = rc.Param(" -o " + outputname
        new_arg = rc.Param(" -t ", "dendrogram_threshold")
    cli.args.append(new_arg)
        new_arg = rc.Param(" -c ", "dendrogram_minclass")
    cli.args.append(new_arg)

        else if joboptions["do_remove_duplicates"].getBoolean())
    
        label += ".removeduplicates"

        #  Remove duplicates
        command="`which relion_star_handler`"

        if joboptions["fn_mic")
    cli.args.append(new_arg) != "" || joboptions["fn_model")
    cli.args.append(new_arg) != "")
                    error_message = "ERROR: Duplicate removal is only possible for particle STAR files..."
            return false
        
        if joboptions["fn_data")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: Duplicate removal needs a particle STAR file..."
            return false
        
        node = rc.Node(joboptions["fn_data")
    cli.args.append(new_arg), joboptions["fn_data"].node_type)
        inputNodes.push_back(node)
        new_arg = rc.Param(" --i ", "fn_data")
    cli.args.append(new_arg)

        FileName fn_out = outputname+"particles.star"
        rc.Node node2(fn_out, rh.LABEL_SELECT_PARTS)
        outputNodes.push_back(node2)
        new_arg = rc.Param(" --o " + fn_out

        new_arg = rc.Param(" --remove_duplicates ", "duplicate_threshold")
    cli.args.append(new_arg)
        if joboptions["image_angpix"].getNumber(error_message) > 0)
            new_arg = rc.Param(" --image_angpix ", "image_angpix")
    cli.args.append(new_arg)
        if error_message != "") return false

        else if joboptions["do_select_values"].getBoolean() || joboptions["do_discard"].getBoolean() || joboptions["do_split"].getBoolean())
            #  Value-based selection
        command="`which relion_star_handler`"

        if joboptions["fn_model")
    cli.args.append(new_arg) != "")
                    error_message = "ERROR: Value-selection or subset splitting is only possible for micrograph or particle STAR files..."
            return false
        
        FileName fn_out
        if joboptions["fn_mic")
    cli.args.append(new_arg) != "")
                    node = rc.Node(joboptions["fn_mic")
    cli.args.append(new_arg), joboptions["fn_mic"].node_type)
            inputNodes.push_back(node)
            new_arg = rc.Param(" --i ", "fn_mic")
    cli.args.append(new_arg)
            fn_out = outputname+"micrographs.star"

                else if joboptions["fn_data")
    cli.args.append(new_arg) != "")
                    node = rc.Node(joboptions["fn_data")
    cli.args.append(new_arg), joboptions["fn_data"].node_type)
            inputNodes.push_back(node)
            new_arg = rc.Param(" --i ", "fn_data")
    cli.args.append(new_arg)
            fn_out = outputname+"particles.star"
                new_arg = rc.Param(" --o " + fn_out

        if joboptions["do_select_values"].getBoolean() || joboptions["do_discard"].getBoolean())
        
            if joboptions["fn_mic")
    cli.args.append(new_arg) != "")
                            rc.Node node2(fn_out, rh.LABEL_SELECT_MICS)
                outputNodes.push_back(node2)
                        else if joboptions["fn_data")
    cli.args.append(new_arg) != "")
                            rc.Node node2(fn_out, rh.LABEL_SELECT_PARTS)
                outputNodes.push_back(node2)
            
            if joboptions["do_select_values"].getBoolean())
                            label += ".onvalue"

                new_arg = rc.Param(" --select ", "select_label")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --minval ", "select_minval")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --maxval ", "select_maxval")
    cli.args.append(new_arg)
                        else if joboptions["do_discard"].getBoolean())
                            label += ".discard"

                new_arg = rc.Param(" --discard_on_stats "
                new_arg = rc.Param(" --discard_label ", "discard_label")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --discard_sigma ", "discard_sigma")
    cli.args.append(new_arg)
            
                else if joboptions["do_split"].getBoolean())
        
            label += ".split"

            int nr_split=0
            new_arg = rc.Param(" --split "
            if joboptions["do_random"].getBoolean())
                            new_arg = rc.Param(" --random_order "
            
            if joboptions["nr_split"].getNumber(error_message) <= 0 && joboptions["split_size"].getNumber(error_message) <= 0
                    && !joboptions["nr_split"].isSchedulerVariable() && !joboptions["split_size"].isSchedulerVariable())
                            error_message = "ERROR: When splitting the input STAR file into subsets, set nr_split and/or split_size to a positive value"
                return false
            
            if joboptions["nr_split"].getNumber(error_message) > 0 && !joboptions["nr_split"].isSchedulerVariable())
                            if error_message != "") return false

                nr_split = joboptions["nr_split"].getNumber(error_message)
                new_arg = rc.Param(" --nr_split ", "nr_split")
    cli.args.append(new_arg)
                        if joboptions["split_size"].getNumber(error_message) > 0 && !joboptions["split_size"].isSchedulerVariable())
                            if error_message != "") return false

                new_arg = rc.Param(" --size_split ", "split_size")
    cli.args.append(new_arg)
            
            #  As of relion-3.1, star_handler will write out a star file with the output nodes, which will be read by the pipeliner
                else
    
        #  Automated 2D class selection through the class_ranker
        if joboptions["do_class_ranker"].getBoolean())
        
            label += ".class2dauto"

            if joboptions["fn_model")
    cli.args.append(new_arg) == "")
                            error_message = "ERROR: When using automatically selecting 2D classes, one needs to provide an optimiser.star file"
                return false
            
            if joboptions["do_regroup"].getBoolean() || joboptions["do_recenter"].getBoolean())
                            error_message = "ERROR: regrouping and recentering have not been implemented in class_ranker."
                return false
            
            cli = rc.Prog("`which relion_class_ranker`"

            #  input
            new_arg = rc.Param(" --opt ", "fn_model")
    cli.args.append(new_arg)
            node = rc.Node(joboptions["fn_model")
    cli.args.append(new_arg), joboptions["fn_model"].node_type)
            inputNodes.push_back(node)

            # output
            new_arg = rc.Param(" --o " + outputname + " --fn_sel_parts particles.star --fn_sel_classavgs class_averages.star"

            if joboptions["select_nr_parts"].getNumber(error_message) > 0)
                            new_arg = rc.Param(" --select_min_nr_particles ", "select_nr_parts")
    cli.args.append(new_arg)
                        else if joboptions["select_nr_classes"].getNumber(error_message) > 0)
                            new_arg = rc.Param(" --select_min_nr_classes ", "select_nr_classes")
    cli.args.append(new_arg)
            
            FileName fn_parts = outputname+"particles.star"
            rc.Node node2(fn_parts, rh.LABEL_SELECT_PARTS)
            outputNodes.push_back(node2)

            FileName fn_imgs = outputname+"class_averages.star"
            rc.Node node3(fn_imgs, rh.LABEL_SELECT_CLAVS)
            outputNodes.push_back(node3)

            #  Also save optimiser.star, which could be used for next manual selection (but ordered for examples on the new scores)
            new_arg = rc.Param(" --fn_root rank"

            #  Only save the 2D class averages for 2D jobs
            FileName fn_opt = outputname+"rank_optimiser.star"
            node4 = rc.Node(jo(fn_opt, rh.LABEL_SELECT_OPT)
            outputNodes.push_back(node4)

            #  perform the actual prediction and selection
            new_arg = rc.Param(" --do_granularity_features "
            new_arg = rc.Param(" --auto_select "
            new_arg = rc.Param(" --min_score ", "rank_threshold")
    cli.args.append(new_arg)
                else
        
            #  Interactive selection
            label += ".interactive"

            command="`which relion_display`"

            #  I/O
            if joboptions["fn_model")
    cli.args.append(new_arg) != "")
            
                new_arg = rc.Param(" --gui --i ", "fn_model")
    cli.args.append(new_arg)
                node = rc.Node(joboptions["fn_model")
    cli.args.append(new_arg), joboptions["fn_model"].node_type)
                inputNodes.push_back(node)

                FileName fn_parts = outputname+"particles.star"
                new_arg = rc.Param(" --allow_save --fn_parts " + fn_parts
                rc.Node node2(fn_parts, rh.LABEL_SELECT_PARTS)
                outputNodes.push_back(node2)

                #  Only save the 2D class averages for 2D jobs
                FileName fnt = joboptions["fn_model")
    cli.args.append(new_arg)
                if fnt.contains("Class2D/"))
                                    FileName fn_imgs = outputname+"class_averages.star"
                    new_arg = rc.Param(" --fn_imgs " + fn_imgs
                    rc.Node node3(fn_imgs, rh.LABEL_SELECT_CLAVS)
                    outputNodes.push_back(node3)

                    if joboptions["do_recenter"].getBoolean())
                                            new_arg = rc.Param(" --recenter "
                                                            else if joboptions["fn_mic")
    cli.args.append(new_arg) != "")
                            new_arg = rc.Param(" --gui --i ", "fn_mic")
    cli.args.append(new_arg)
                node = rc.Node(joboptions["fn_mic")
    cli.args.append(new_arg), joboptions["fn_mic"].node_type)
                inputNodes.push_back(node)

                FileName fn_mics = outputname+"micrographs.star"
                new_arg = rc.Param(" --allow_save --fn_imgs " + fn_mics
                rc.Node node2(fn_mics, rh.LABEL_SELECT_MICS)
                outputNodes.push_back(node2)
                        else if joboptions["fn_data")
    cli.args.append(new_arg) != "")
                            new_arg = rc.Param(" --gui --i ", "fn_data")
    cli.args.append(new_arg)
                node = rc.Node(joboptions["fn_data")
    cli.args.append(new_arg), joboptions["fn_data"].node_type)
                inputNodes.push_back(node)

                FileName fn_parts = outputname+"particles.star"
                new_arg = rc.Param(" --allow_save --fn_imgs " + fn_parts
                rc.Node node2(fn_parts, rh.LABEL_SELECT_PARTS)
                outputNodes.push_back(node2)
                        
    #  Re-grouping
    if joboptions["do_regroup"].getBoolean())
            if joboptions["fn_model")
    cli.args.append(new_arg) == "")
                    error_message = "Re-grouping only works for model.star/optimiser.star files..."
            return false
                new_arg = rc.Param(" --regroup ", "nr_groups")
    cli.args.append(new_arg)
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return cli

def getCommandsClass2DJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    rc.Prog("`which relion_refine_mpi`","use_mpi",True)
    rc.Prog("`which relion_refine`","use_mpi",False)

    FileName fn_run = "run"
    if is_continue)
            if joboptions["fn_cont")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for continuation STAR file..."
            return false
                int pos_it = joboptions["fn_cont")
    cli.args.append(new_arg).rfind("_it")
        int pos_op = joboptions["fn_cont")
    cli.args.append(new_arg).rfind("_optimiser")
        if pos_it < 0 || pos_op < 0)
                    error_message = "Warning: invalid optimiser.star filename provided for continuation run!"
            return false
                #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
        # int it = (int)textToFloat((joboptions["fn_cont")
    cli.args.append(new_arg).substr(pos_it+3, 6)).c_str())
        # fn_run += "_ct" + floatToString(it)
        new_arg = rc.Param(" --continue ", "fn_cont")
    cli.args.append(new_arg)
    
    new_arg = rc.Param(" --o " + outputname + fn_run

    int my_classes = (int)joboptions["nr_classes"].getNumber(error_message)
    if error_message != "") return false

    #  Optimisation
    int my_iter
    if joboptions["do_em"].getBoolean())
            if joboptions["do_grad"].getBoolean())
                    error_message = "You cannot specify to use both the EM and the VDAM algorithm!"
            return false
        
        new_arg = rc.Param(" --iter ", "nr_iter_em")
    cli.args.append(new_arg)

        my_iter = (int)joboptions["nr_iter_em"].getNumber(error_message)
        if error_message != "") return false
        else if joboptions["do_grad"].getBoolean())
            if joboptions["nr_mpi"].getNumber(error_message) > 1)
                    error_message = "Gradient refinement (running the VDAM algorithm) is not supported together with MPI."
            return false
        
        new_arg = rc.Param(" --grad --class_inactivity_threshold 0.1 --grad_write_iter 10"
        new_arg = rc.Param(" --iter ", "nr_iter_grad")
    cli.args.append(new_arg)

        my_iter = (int)joboptions["nr_iter_grad"].getNumber(error_message)
        if error_message != "") return false
        else
            error_message = "You need to specify to use either the EM or the VDAM algorithm"
        return false
    
    outputNodes = getOutputNodesRefine(outputname + fn_run, "Class2D", my_iter, my_classes, 2, 1, is_tomo)

    if !is_continue)
            if joboptions["fn_img")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for input STAR file..."
            return false
                new_arg = rc.Param(" --i ", "fn_img")
    cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_img")
    cli.args.append(new_arg), joboptions["fn_img"].node_type)
        inputNodes.push_back(node)
    
    #  Always do compute stuff
#   if !joboptions["do_combine_thru_disc"].getBoolean())
    new_arg = rc.Flag(" --dont_combine_weights_via_disc","","do_combine_thru_disc",False)
#   if !joboptions["do_parallel_discio"].getBoolean())
    new_arg = rc.Flag(" --no_parallel_disc_io","","do_parallel_discio",False)
#   if joboptions["do_preread_images"].getBoolean())
    new_arg = rc.Flag(" --preread_images ", "","do_preread_images", True)
#    else if joboptions["scratch_dir"] != "")
    new_arg = rc.Flag(" --scratch_dir ","scratch_dir","scratch_dir",True)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --pool ", "nr_pool")
    cli.args.append(new_arg)
    #  Takanori observed bad 2D classifications with pad1, so use pad2 always. Memory isnt a problem here anyway.
    new_arg = rc.Param(" --pad","2")
    cli.args.append(new_arg)

    #  CTF stuff
    if !is_continue)
            if joboptions["do_ctf_correction"].getBoolean())
                    new_arg = rc.Param(" --ctf "
            if joboptions["ctf_intact_first_peak"].getBoolean())
                new_arg = rc.Param(" --ctf_intact_first_peak "
            
    new_arg = rc.Param(" --tau2_fudge ", "tau_fudge")
    cli.args.append(new_arg)
     new_arg = rc.Param(" --particle_diameter ", "particle_diameter")
    cli.args.append(new_arg)
    if !is_continue)
    
        new_arg = rc.Param(" --K ", "nr_classes")
    cli.args.append(new_arg)
        #  Always flatten the solvent
        new_arg = rc.Param(" --flatten_solvent "
        if joboptions["do_zero_mask"].getBoolean())
            new_arg = rc.Param(" --zero_mask "
        if joboptions["highres_limit"].getNumber(error_message) > 0)
            new_arg = rc.Param(" --strict_highres_exp ", "highres_limit")
    cli.args.append(new_arg)
        if error_message != "") return false

    
    if joboptions["do_center"].getBoolean())
            new_arg = rc.Param(" --center_classes "
        #  Sampling
    int iover = 1
    new_arg = rc.Param(" --oversampling " + floatToString((float)iover)

    if !joboptions["dont_skip_align"].getBoolean())
            new_arg = rc.Param(" --skip_align "
        else
            #  The sampling given in the GUI will be the oversampled one!
        new_arg = rc.Param(" --psi_step " + floatToString(joboptions["psi_sampling"].getNumber(error_message) * pow(2., iover))
        if error_message != "") return false

        #  Offset range
        new_arg = rc.Param(" --offset_range ", "offset_range")
    cli.args.append(new_arg)
        #  The sampling given in the GUI will be the oversampled one!
        new_arg = rc.Param(" --offset_step " + floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover))
        if error_message != "") return false

        if joboptions["allow_coarser"].getBoolean())
                    new_arg = rc.Param(" --allow_coarser_sampling"
        
    
    #  Helix
    if joboptions["do_helix"].getBoolean())
            label += ".helical"

        new_arg = rc.Param(" --helical_outer_diameter ", "helical_tube_outer_diameter")
    cli.args.append(new_arg)

        if joboptions["dont_skip_align"].getBoolean())
                    if joboptions["do_bimodal_psi"].getBoolean())
                new_arg = rc.Param(" --bimodal_psi"

            RFLOAT val = joboptions["range_psi"].getNumber(error_message)
            if error_message != "") return false

            val = (val < 0.) ? (0.) : (val)
            val = (val > 90.) ? (90.) : (val)
            new_arg = rc.Param(" --sigma_psi " + floatToString(val / 3.)

            if joboptions["do_restrict_xoff"].getBoolean())
                            new_arg = rc.Param(" --helix --helical_rise_initial ", "helical_rise")
    cli.args.append(new_arg)
                        
    #  Always do norm and scale correction
    if !is_continue)
        new_arg = rc.Param(" --norm --scale "

    #  Running stuff
    new_arg = rc.Param(" --j ", "nr_threads")
    cli.args.append(new_arg)

    #  GPU-stuff
    if joboptions["use_gpu"].getBoolean())
            new_arg = rc.Param(" --gpu \"", "gpu_ids")
    cli.args.append(new_arg) +"\""
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

        return cli

def getCommandsInimodelJob(outputname,label,job_counter=-1):
    cli = clear(label)

    initialisePipeline(outputname, job_counter)

#   USELESS
#   if joboptions["nr_mpi"].getNumber(error_message) > 1)
#            error_message = "Gradient refinement is not supported together with MPI."
#        return false
#        if (error_message != "") return false

    
    command="`which relion_refine`"

    FileName fn_sym = joboptions["sym_name")
    cli.args.append(new_arg)

    FileName fn_run = "run"
    if is_continue)
            if joboptions["fn_cont")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for continuation STAR file..."
            return false
                int pos_it = joboptions["fn_cont")
    cli.args.append(new_arg).rfind("_it")
        int pos_op = joboptions["fn_cont")
    cli.args.append(new_arg).rfind("_optimiser")
        if pos_it < 0 || pos_op < 0)
            std::cerr << "Warning: invalid optimiser.star filename provided for continuation run: " << joboptions["fn_cont")
    cli.args.append(new_arg) << std::endl
        #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
        # int it = (int)textToFloat((joboptions["fn_cont")
    cli.args.append(new_arg).substr(pos_it+3, 6)).c_str())
        # fn_run += "_ct" + floatToString(it)
        new_arg = rc.Param(" --continue ", "fn_cont")
    cli.args.append(new_arg)

    
    new_arg = rc.Param(" --o " + outputname + fn_run
    new_arg = rc.Param(" --iter ", "nr_iter")
    cli.args.append(new_arg)

    if is_tomo) label += ".tomo"

    int total_nr_iter = joboptions["nr_iter"].getNumber(error_message)
    if error_message != "") return false
    int nr_classes = joboptions["nr_classes"].getNumber(error_message)
    if error_message != "") return false

    if !is_continue)
            new_arg = rc.Param(" --grad --denovo_3dref "

        if is_tomo)
                    error_message = getTomoInputCommmand(true, command, HAS_COMPULSORY, HAS_COMPULSORY, HAS_NOT, HAS_NOT)
            if error_message != "") return false

            rc.Node node1( outputname + fn_run + "_optimisation_set.star", rh.LABEL_INIMOD_OPTSET)
            outputNodes.push_back(node1)

            float sigma = joboptions["sigma_tilt"].getNumber(error_message)
            if error_message != "") return false
            if sigma > 0.)
                            new_arg = rc.Param(" --sigma_tilt ", "sigma_tilt")
    cli.args.append(new_arg)
            
                else
                    if joboptions["fn_img")
    cli.args.append(new_arg) == "")
                            error_message = "ERROR: empty field for input STAR file..."
                return false
                        else
                            new_arg = rc.Param(" --i ", "fn_img")
    cli.args.append(new_arg)
                node = rc.Node(joboptions["fn_img")
    cli.args.append(new_arg), joboptions["fn_img"].node_type)
                inputNodes.push_back(node)
                    
        #  CTF stuff
        if joboptions["do_ctf_correction"].getBoolean())
                    new_arg = rc.Param(" --ctf"
            if joboptions["ctf_intact_first_peak"].getBoolean())
                new_arg = rc.Param(" --ctf_intact_first_peak"
        
        new_arg = rc.Param(" --K ", "nr_classes")
    cli.args.append(new_arg)
        if joboptions["do_run_C1"].getBoolean())
                    new_arg = rc.Param(" --sym C1 "
                else
                    new_arg = rc.Param(" --sym " + fn_sym
        
        if joboptions["do_solvent"].getBoolean())
            new_arg = rc.Param(" --flatten_solvent "
        new_arg = rc.Param(" --zero_mask "
    
    #  Always do compute stuff
#   if !joboptions["do_combine_thru_disc"].getBoolean())
    new_arg = rc.Flag(" --dont_combine_weights_via_disc","","do_combine_thru_disc",False)
#   if !joboptions["do_parallel_discio"].getBoolean())
    new_arg = rc.Flag(" --no_parallel_disc_io","","do_parallel_discio",False)
#   if joboptions["do_preread_images"].getBoolean())
    new_arg = rc.Flag(" --preread_images ", "","do_preread_images", True)
#    else if joboptions["scratch_dir"] != "")
    new_arg = rc.Flag(" --scratch_dir ","scratch_dir","scratch_dir",True)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --pool ", "nr_pool")
    cli.args.append(new_arg)
    #  Pad 1
    new_arg = rc.Param(" --pad","1")
    cli.args.append(new_arg)

    #  Optimisation
    new_arg = rc.Param(" --particle_diameter ", "particle_diameter")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --oversampling 1  --healpix_order 1  --offset_range 6  --offset_step 2 --auto_sampling "
    new_arg = rc.Param(" --tau2_fudge ", "tau_fudge")
    cli.args.append(new_arg)

    #  Running stuff
    new_arg = rc.Param(" --j ", "nr_threads")
    cli.args.append(new_arg)

    #  GPU-stuff
    if joboptions["use_gpu"].getBoolean())
            new_arg = rc.Param(" --gpu \"", "gpu_ids")
    cli.args.append(new_arg) +"\""
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    #  Quickly remove RELION_JOB_EXIT_SUCCESS
    0 = "rm -f " + outputname + RELION_JOB_EXIT_SUCCESS
    commands.push_back(command0)


    FileName fn_model
    fn_model.compose(outputname + fn_run + "_it", total_nr_iter,"",3)
    fn_model+="_model.star"

    #  Align with symmetry axes and apply symmetry
    2 = "`which relion_align_symmetry`"
    command2 += " --i " + fn_model
    command2 += " --o " + outputname + "initial_model.mrc"

    if  joboptions["do_run_C1"].getBoolean() && !(fn_sym == "C1" || fn_sym == "c1") )
            command2 += " --sym ", "sym_name")
    cli.args.append(new_arg)
        else
            command2 += " --sym C1 "
        command2 += " --apply_sym --select_largest_class "
    commands.push_back(command2)

    #  And re-introduce RELION_JOB_EXIT_SUCCESS
    F = "touch " + outputname + RELION_JOB_EXIT_SUCCESS
    commands.push_back(commandF)

    #  Output nodes
    rc.Node node2(outputname + "initial_model.mrc", rh.LABEL_INIMOD_MAP)
    outputNodes.push_back(node2)

    #  If doing more than 1 class, make them all available (one of them will be the same as initial_model.mrc)
    if nr_classes > 1)
            for (int iclass = 0 iclass < nr_classes iclass++)
                    FileName fn_tmp
            fn_tmp.compose(outputname + fn_run + "_it", total_nr_iter, "", 3)
            fn_tmp.compose(fn_tmp + "_class", iclass+1, "mrc", 3)
            rc.Node node3(fn_tmp, rh.LABEL_INIMOD_MAP)
            outputNodes.push_back(node3)
            
    return cli

def getCommandsClass3DJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    rc.Prog("`which relion_refine_mpi`","use_mpi",True)
    rc.Prog("`which relion_refine`","use_mpi",True)

    FileName fn_run = "run"
    if is_continue)
            if joboptions["fn_cont")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for continuation STAR file..."
            return false
                int pos_it = joboptions["fn_cont")
    cli.args.append(new_arg).rfind("_it")
        int pos_op = joboptions["fn_cont")
    cli.args.append(new_arg).rfind("_optimiser")
        if pos_it < 0 || pos_op < 0)
            std::cerr << "Warning: invalid optimiser.star filename provided for continuation run: " << joboptions["fn_cont")
    cli.args.append(new_arg) << std::endl
        #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
        # int it = (int)textToFloat((joboptions["fn_cont")
    cli.args.append(new_arg).substr(pos_it+3, 6)).c_str())
        # fn_run += "_ct" + floatToString(it)
        new_arg = rc.Param(" --continue ", "fn_cont")
    cli.args.append(new_arg)

    
    new_arg = rc.Param(" --o " + outputname + fn_run

    int my_iter = (int)joboptions["nr_iter"].getNumber(error_message)
    if error_message != "") return false

    int my_classes = (int)joboptions["nr_classes"].getNumber(error_message)
    if error_message != "") return false

    outputNodes = getOutputNodesRefine(outputname + fn_run, "Class3D", my_iter, my_classes, 3, 1, is_tomo)

    if !is_continue)
            if is_tomo)
                    error_message = getTomoInputCommmand(true, command, HAS_COMPULSORY, HAS_COMPULSORY, HAS_NOT, HAS_NOT)
            if error_message != "") return false

            rc.Node node1( outputname + fn_run + "_optimisation_set.star", rh.LABEL_CLASS3D_OPTSET)
            outputNodes.push_back(node1)

            float sigma = joboptions["sigma_tilt"].getNumber(error_message)
            if error_message != "") return false
            if sigma > 0.)
                            new_arg = rc.Param(" --sigma_tilt ", "sigma_tilt")
    cli.args.append(new_arg)
            
                else
                    if joboptions["fn_img")
    cli.args.append(new_arg) == "")
                            error_message = "ERROR: empty field for input STAR file..."
                return false
                        else
                            new_arg = rc.Param(" --i ", "fn_img")
    cli.args.append(new_arg)
                node = rc.Node(joboptions["fn_img")
    cli.args.append(new_arg), joboptions["fn_img"].node_type)
                inputNodes.push_back(node)
                    
        if joboptions["fn_ref")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for reference."
            return false
                else
                    new_arg = rc.Param(" --ref ", "fn_ref")
    cli.args.append(new_arg)
            if joboptions["fn_ref")
    cli.args.append(new_arg) != "None")
                            node = rc.Node(joboptions["fn_ref")
    cli.args.append(new_arg), joboptions["fn_ref"].node_type)
                inputNodes.push_back(node)
                        if !joboptions["ref_correct_greyscale"].getBoolean())
                new_arg = rc.Param(" --firstiter_cc"

            if joboptions["trust_ref_size"].getBoolean())
                new_arg = rc.Param(" --trust_ref_size"
        
        if joboptions["ini_high"].getNumber(error_message) > 0.)
            new_arg = rc.Param(" --ini_high ", "ini_high")
    cli.args.append(new_arg)
        if error_message != "") return false

    
    #  Always do compute stuff
#   if !joboptions["do_combine_thru_disc"].getBoolean())
    new_arg = rc.Flag(" --dont_combine_weights_via_disc","","do_combine_thru_disc",False)
#   if !joboptions["do_parallel_discio"].getBoolean())
    new_arg = rc.Flag(" --no_parallel_disc_io","","do_parallel_discio",False)
#   if joboptions["do_preread_images"].getBoolean())
    new_arg = rc.Flag(" --preread_images ", "","do_preread_images", True)
#    else if joboptions["scratch_dir"] != "")
    new_arg = rc.Flag(" --scratch_dir ","scratch_dir","scratch_dir",True)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --pool ", "nr_pool")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --pad","1","do_pad1",True)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --pad","2", "do_pad1", False)
    cli.args.append(new_arg)


    #  CTF stuff
    if !is_continue)
            if joboptions["do_ctf_correction"].getBoolean())
                    new_arg = rc.Param(" --ctf"
            if joboptions["ctf_intact_first_peak"].getBoolean())
                new_arg = rc.Param(" --ctf_intact_first_peak"
            
    #  Optimisation
    new_arg = rc.Param(" --iter ", "nr_iter")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --tau2_fudge ", "tau_fudge")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --particle_diameter ", "particle_diameter")
    cli.args.append(new_arg)
    if !is_continue)
            if joboptions["do_fast_subsets"].getBoolean())
            new_arg = rc.Param(" --fast_subsets "

        new_arg = rc.Param(" --K ", "nr_classes")
    cli.args.append(new_arg)
        #  Always flatten the solvent
        new_arg = rc.Param(" --flatten_solvent"
        if joboptions["do_zero_mask"].getBoolean())
            new_arg = rc.Param(" --zero_mask"
        if joboptions["highres_limit"].getNumber(error_message) > 0)
            new_arg = rc.Param(" --strict_highres_exp ", "highres_limit")
    cli.args.append(new_arg)
        if error_message != "") return false
    
    if joboptions["do_blush"].getBoolean())
        new_arg = rc.Param(" --blush "

    if joboptions["fn_mask")
    cli.args.append(new_arg).length() > 0)
            new_arg = rc.Param(" --solvent_mask ", "fn_mask")
    cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_mask")
    cli.args.append(new_arg), joboptions["fn_mask"].node_type)
        inputNodes.push_back(node)
    
    #  Sampling
    if !joboptions["dont_skip_align"].getBoolean())
            new_arg = rc.Param(" --skip_align "
        else
            int iover = 1
        new_arg = rc.Param(" --oversampling " + floatToString((float)iover)
        int sampling = JobOption::getHealPixOrder(joboptions["sampling")
    cli.args.append(new_arg))
        if sampling <= 0)
                    error_message = "Wrong choice for sampling"
            return false
                #  The sampling given in the GUI will be the oversampled one!
        new_arg = rc.Param(" --healpix_order " + integerToString(sampling - iover)

        #  Manually input local angular searches
        if joboptions["do_local_ang_searches"].getBoolean())
                    new_arg = rc.Param(" --sigma_ang " + floatToString(joboptions["sigma_angles"].getNumber(error_message) / 3.)
            if joboptions["relax_sym")
    cli.args.append(new_arg).length() > 0)
                new_arg = rc.Param(" --relax_sym ", "relax_sym")
    cli.args.append(new_arg)

            if error_message != "") return false
        
        #  Offset range
        new_arg = rc.Param(" --offset_range ", "offset_range")
    cli.args.append(new_arg)
        #  The sampling given in the GUI will be the oversampled one!
        new_arg = rc.Param(" --offset_step " +  floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover))
        if error_message != "") return false

        if joboptions["allow_coarser"].getBoolean())
                    new_arg = rc.Param(" --allow_coarser_sampling"
            
    #  Provide symmetry, and always do norm and scale correction
    if !is_continue)
            new_arg = rc.Param(" --sym ", "sym_name")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --norm --scale "
    
    if  (!is_continue) && (joboptions["do_helix"].getBoolean()) )
            label += ".helical"

        new_arg = rc.Param(" --helix"

        float inner_diam = joboptions["helical_tube_inner_diameter"].getNumber(error_message)
        if error_message != "") return false
        if inner_diam > 0.)
            new_arg = rc.Param(" --helical_inner_diameter ", "helical_tube_inner_diameter")
    cli.args.append(new_arg)

        new_arg = rc.Param(" --helical_outer_diameter ", "helical_tube_outer_diameter")
    cli.args.append(new_arg)
        if joboptions["do_apply_helical_symmetry"].getBoolean())
                    new_arg = rc.Param(" --helical_nr_asu ", "helical_nr_asu")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --helical_twist_initial ", "helical_twist_initial")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --helical_rise_initial ", "helical_rise_initial")
    cli.args.append(new_arg)

            float myz = joboptions["helical_z_percentage"].getNumber(error_message) / 100.
            if error_message != "") return false
            new_arg = rc.Param(" --helical_z_percentage " + floatToString(myz)

            if joboptions["do_local_search_helical_symmetry"].getBoolean())
                            new_arg = rc.Param(" --helical_symmetry_search"
                new_arg = rc.Param(" --helical_twist_min ", "helical_twist_min")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --helical_twist_max ", "helical_twist_max")
    cli.args.append(new_arg)

                float twist_inistep = joboptions["helical_twist_inistep"].getNumber(error_message)
                if error_message != "") return false
                if twist_inistep > 0.)
                    new_arg = rc.Param(" --helical_twist_inistep ", "helical_twist_inistep")
    cli.args.append(new_arg)

                new_arg = rc.Param(" --helical_rise_min ", "helical_rise_min")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --helical_rise_max ", "helical_rise_max")
    cli.args.append(new_arg)

                float rise_inistep = joboptions["helical_rise_inistep"].getNumber(error_message)
                if error_message != "") return false
                if rise_inistep > 0.)
                    new_arg = rc.Param(" --helical_rise_inistep ", "helical_rise_inistep")
    cli.args.append(new_arg)
                            else
            new_arg = rc.Param(" --ignore_helical_symmetry"
        if joboptions["keep_tilt_prior_fixed"].getBoolean())
            new_arg = rc.Param(" --helical_keep_tilt_prior_fixed"
        if  (joboptions["dont_skip_align"].getBoolean()) && (!joboptions["do_local_ang_searches"].getBoolean()) )
                    float val = joboptions["range_tilt"].getNumber(error_message)
            if error_message != "") return false
            val = (val < 0.) ? (0.) : (val)
            val = (val > 90.) ? (90.) : (val)
            new_arg = rc.Param(" --sigma_tilt " + floatToString(val / 3.)

            val = joboptions["range_psi"].getNumber(error_message)
            if error_message != "") return false
            val = (val < 0.) ? (0.) : (val)
            val = (val > 90.) ? (90.) : (val)
            new_arg = rc.Param(" --sigma_psi " + floatToString(val / 3.)

            val = joboptions["range_rot"].getNumber(error_message)
            if error_message != "") return false
            val = (val < 0.) ? (0.) : (val)
            val = (val > 90.) ? (90.) : (val)
            new_arg = rc.Param(" --sigma_rot " + floatToString(val / 3.)

            val = joboptions["helical_range_distance"].getNumber(error_message)
            if error_message != "") return false
            if val > 0.)
                new_arg = rc.Param(" --helical_sigma_distance " + floatToString(val / 3.)
            
    #  Running stuff
    new_arg = rc.Param(" --j ", "nr_threads")
    cli.args.append(new_arg)

    #  GPU-stuff
    if joboptions["use_gpu"].getBoolean())
            if !joboptions["dont_skip_align"].getBoolean())
                    error_message = "ERROR: you cannot use GPUs when skipping image alignments."
            return false
                new_arg = rc.Param(" --gpu \"", "gpu_ids")
    cli.args.append(new_arg) + "\""
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return cli

def getCommandsAutorefineJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    rc.Prog("`which relion_refine_mpi`","use_mpi",True)
    rc.Prog("`which relion_refine`","use_mpi",False)

    FileName fn_run = "run"
    if is_continue)
            if joboptions["fn_cont")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for continuation STAR file..."
            return false
                int pos_it = joboptions["fn_cont")
    cli.args.append(new_arg).rfind("_it")
        int pos_op = joboptions["fn_cont")
    cli.args.append(new_arg).rfind("_optimiser")
        if pos_it < 0 || pos_op < 0)
                    error_message = "Invalid optimiser.star filename provided for auto-refine continuation run: ", "fn_cont")
    cli.args.append(new_arg)
            return false
        
        #  SHWS 10dec2020: switch off using run_ctXX output for continue jobs, as this will affect Schedulers
        # int it = (int)textToFloat((joboptions["fn_cont")
    cli.args.append(new_arg).substr(pos_it+3, 6)).c_str())
        # fn_run += "_ct" + floatToString(it)
        new_arg = rc.Param(" --continue ", "fn_cont")
    cli.args.append(new_arg)

    
    new_arg = rc.Param(" --o " + outputname + fn_run
    #  TODO: add bodies!! (probably in next version)
    outputNodes = getOutputNodesRefine(outputname + fn_run, "Refine3D", -1, 1, 3, 1, is_tomo)

    if is_tomo) label += ".tomo"

    if !is_continue)
            new_arg = rc.Param(" --auto_refine --split_random_halves"


        if is_tomo)
                    error_message = getTomoInputCommmand(true, command, HAS_COMPULSORY, HAS_COMPULSORY, HAS_NOT, HAS_NOT)
            if error_message != "") return false

            rc.Node node1( outputname + fn_run + "_optimisation_set.star", rh.LABEL_REFINE3D_OPTSET)
            outputNodes.push_back(node1)

            float sigma = joboptions["sigma_tilt"].getNumber(error_message)
            if error_message != "") return false
            if sigma > 0.)
                            new_arg = rc.Param(" --sigma_tilt ", "sigma_tilt")
    cli.args.append(new_arg)
            
                else
                    if joboptions["fn_img")
    cli.args.append(new_arg) == "")
                            error_message = "ERROR: empty field for input STAR file..."
                return false
                        else
                            new_arg = rc.Param(" --i ", "fn_img")
    cli.args.append(new_arg)
                node = rc.Node(joboptions["fn_img")
    cli.args.append(new_arg), joboptions["fn_img"].node_type)
                inputNodes.push_back(node)
                    
        if joboptions["fn_ref")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for input reference..."
            return false
                else
                    new_arg = rc.Param(" --ref ", "fn_ref")
    cli.args.append(new_arg)
            if joboptions["fn_ref")
    cli.args.append(new_arg) != "None")
                            node = rc.Node(joboptions["fn_ref")
    cli.args.append(new_arg), joboptions["fn_ref"].node_type)
                inputNodes.push_back(node)
                        if !joboptions["ref_correct_greyscale"].getBoolean())
                new_arg = rc.Param(" --firstiter_cc"

            if joboptions["trust_ref_size"].getBoolean())
                new_arg = rc.Param(" --trust_ref_size"

                if joboptions["ini_high"].getNumber(error_message) > 0.)
                    if error_message != "") return false
            new_arg = rc.Param(" --ini_high ", "ini_high")
    cli.args.append(new_arg)
        
    
    if joboptions["do_blush"].getBoolean())
            new_arg = rc.Param(" --blush "
    
    #  Always do compute stuff
#   if !joboptions["do_combine_thru_disc"].getBoolean())
    new_arg = rc.Flag(" --dont_combine_weights_via_disc","","do_combine_thru_disc",False)
#   if !joboptions["do_parallel_discio"].getBoolean())
    new_arg = rc.Flag(" --no_parallel_disc_io","","do_parallel_discio",False)
#   if joboptions["do_preread_images"].getBoolean())
    new_arg = rc.Flag(" --preread_images ", "","do_preread_images", True)
#    else if joboptions["scratch_dir"] != "")
    new_arg = rc.Flag(" --scratch_dir ","scratch_dir","scratch_dir",True)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --pool ", "nr_pool")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --pad","1","do_pad1",True)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --pad","2", "do_pad1", False)
    cli.args.append(new_arg)
    
    if joboptions["auto_faster"].getBoolean())
            new_arg = rc.Param(" --auto_ignore_angles --auto_resol_angles"
    
    #  CTF stuff
    if !is_continue)
            if joboptions["do_ctf_correction"].getBoolean())
                    new_arg = rc.Param(" --ctf"
            if joboptions["ctf_intact_first_peak"].getBoolean())
                new_arg = rc.Param(" --ctf_intact_first_peak"
            
    #  Optimisation
    new_arg = rc.Param(" --particle_diameter ", "particle_diameter")
    cli.args.append(new_arg)
#    if !is_continue)
    #  Always flatten the solvent
    new_arg = rc.Param(" --flatten_solvent","")
#   if joboptions["do_zero_mask"].getBoolean())
    new_arg = rc.Flag(" --zero_mask","do_zero_mask",True)
#   if joboptions["fn_mask"].length() > 0)
    new_arg = rc.Param(" --solvent_mask ", "fn_mask",assertion="is_field_not_empty")
    cli.args.append(new_arg)

#   if joboptions["do_solvent_fsc"].getBoolean())
    new_arg = rc.Param(" --solvent_correct_fsc ","do_solvent_fsc",True)
   cli.args.append(new_arg)

    node = rc.Node(joboptions["fn_mask").getString(), joboptions["fn_mask"].node_type)
    inputNodes.push_back(node)
    
#    if !is_continue)
    #  Sampling
    int iover = 1
    new_arg = rc.Param(" --oversampling " + floatToString((float)iover)

    int sampling = JobOption::getHealPixOrder(joboptions["sampling"])
    if sampling <= 0)
                error_message = "Wrong choice for sampling"
        return false
            #  The sampling given in the GUI will be the oversampled one!
    new_arg = rc.Param(" --healpix_order " + integerToString(sampling - iover)

    #  Minimum sampling rate to perform local searches (may be changed upon continuation
    int auto_local_sampling = JobOption::getHealPixOrder(joboptions["auto_local_sampling"])
    if auto_local_sampling <= 0)
                error_message = "Wrong choice for auto_local_sampling"
        return false
            #  The sampling given in the GUI will be the oversampled one!
    new_arg = rc.Param(" --auto_local_healpix_order " + integerToString(auto_local_sampling - iover)

    #  Offset range
    new_arg = rc.Param(" --offset_range ", "offset_range")
    cli.args.append(new_arg)
    #  The sampling given in the GUI will be the oversampled one!
    new_arg = rc.Param(" --offset_step ",floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover))
    if error_message != "") return false

    new_arg = rc.Param(" --sym ", "sym_name")
    cli.args.append(new_arg)
    #  Always join low-res data, as some D&I point group refinements may fall into different hands!
    new_arg = rc.Param(" --low_resol_join_halves","40")
    new_arg = rc.Param(" --norm --scale ","")

        #  Helix
        if joboptions["do_helix"].getBoolean())
                    label += ".helical"

            new_arg = rc.Param(" --helix"

            float inner_diam = joboptions["helical_tube_inner_diameter"].getNumber(error_message)
            if error_message != "") return false
            if inner_diam > 0.)
                new_arg = rc.Param(" --helical_inner_diameter ", "helical_tube_inner_diameter")
    cli.args.append(new_arg)

            new_arg = rc.Param(" --helical_outer_diameter ", "helical_tube_outer_diameter")
    cli.args.append(new_arg)
            if joboptions["do_apply_helical_symmetry"].getBoolean())
                            new_arg = rc.Param(" --helical_nr_asu ", "helical_nr_asu")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --helical_twist_initial ", "helical_twist_initial")
    cli.args.append(new_arg)
                new_arg = rc.Param(" --helical_rise_initial ", "helical_rise_initial")
    cli.args.append(new_arg)

                float myz = joboptions["helical_z_percentage"].getNumber(error_message) / 100.
                if error_message != "") return false
                new_arg = rc.Param(" --helical_z_percentage " + floatToString(myz)

                if joboptions["do_local_search_helical_symmetry"].getBoolean())
                                    new_arg = rc.Param(" --helical_symmetry_search"
                    new_arg = rc.Param(" --helical_twist_min ", "helical_twist_min")
    cli.args.append(new_arg)
                    new_arg = rc.Param(" --helical_twist_max ", "helical_twist_max")
    cli.args.append(new_arg)

                    float twist_inistep = joboptions["helical_twist_inistep"].getNumber(error_message)
                    if error_message != "") return false
                    if twist_inistep > 0.)
                        new_arg = rc.Param(" --helical_twist_inistep ", "helical_twist_inistep")
    cli.args.append(new_arg)

                    new_arg = rc.Param(" --helical_rise_min ", "helical_rise_min")
    cli.args.append(new_arg)
                    new_arg = rc.Param(" --helical_rise_max ", "helical_rise_max")
    cli.args.append(new_arg)

                    float rise_inistep = joboptions["helical_rise_inistep"].getNumber(error_message)
                    if error_message != "") return false
                    if rise_inistep > 0.)
                        new_arg = rc.Param(" --helical_rise_inistep ", "helical_rise_inistep")
    cli.args.append(new_arg)
                                        else
                new_arg = rc.Param(" --ignore_helical_symmetry"

            float val
            if sampling != auto_local_sampling)
                            val = joboptions["range_tilt"].getNumber(error_message)
                if error_message != "") return false
                val = (val < 0.) ? (0.) : (val)
                val = (val > 90.) ? (90.) : (val)
                new_arg = rc.Param(" --sigma_tilt " + floatToString(val / 3.)

                val = joboptions["range_psi"].getNumber(error_message)
                if error_message != "") return false
                val = (val < 0.) ? (0.) : (val)
                val = (val > 90.) ? (90.) : (val)
                new_arg = rc.Param(" --sigma_psi " + floatToString(val / 3.)

                val = joboptions["range_rot"].getNumber(error_message)
                if error_message != "") return false
                val = (val < 0.) ? (0.) : (val)
                val = (val > 90.) ? (90.) : (val)
                new_arg = rc.Param(" --sigma_rot " + floatToString(val / 3.)
            
            val = joboptions["helical_range_distance"].getNumber(error_message)
            if error_message != "") return false
            if val > 0.)
                new_arg = rc.Param(" --helical_sigma_distance " + floatToString(val / 3.)

            if joboptions["keep_tilt_prior_fixed"].getBoolean())
                new_arg = rc.Param(" --helical_keep_tilt_prior_fixed"
            
    if joboptions["relax_sym")
    cli.args.append(new_arg).length() > 0)
        new_arg = rc.Param(" --relax_sym ", "relax_sym")
    cli.args.append(new_arg)

    #  Running stuff
    new_arg = rc.Param(" --j ", "nr_threads")
    cli.args.append(new_arg)

    #  GPU-stuff
    if joboptions["use_gpu"].getBoolean())
            new_arg = rc.Param(" --gpu \"", "gpu_ids")
    cli.args.append(new_arg) + "\""
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return cli

def getCommandsMultiBodyJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    if !exists(joboptions["fn_bodies")
    cli.args.append(new_arg)))
            error_message = "ERROR: you have to specify an existing body STAR file."
        return false
    
    if is_continue && joboptions["fn_cont")
    cli.args.append(new_arg) == "" && !joboptions["do_analyse"].getBoolean())
            error_message = "ERROR: either specify a optimiser file to continue multibody refinement from OR run flexibility analysis..."
        return false
    
    FileName fn_run = ""
    if !is_continue || (is_continue && joboptions["fn_cont")
    cli.args.append(new_arg) != ""))
    
        if joboptions["nr_mpi"].getNumber(error_message) > 1)
            command="`which relion_refine_mpi`"
        else
            command="`which relion_refine`"
        if error_message != "") return false

        MetaDataTable MD
        MD.read(joboptions["fn_bodies")
    cli.args.append(new_arg))
        int nr_bodies = MD.numberOfObjects()

        if is_continue)
                    int pos_it = joboptions["fn_cont")
    cli.args.append(new_arg).rfind("_it")
            int pos_op = joboptions["fn_cont")
    cli.args.append(new_arg).rfind("_optimiser")
            if pos_it < 0 || pos_op < 0)
                std::cerr << "Warning: invalid optimiser.star filename provided for continuation run: " << joboptions["fn_cont")
    cli.args.append(new_arg) << std::endl
            int it = (int)textToFloat((joboptions["fn_cont")
    cli.args.append(new_arg).substr(pos_it+3, 6)).c_str())
            fn_run = "run_ct" + floatToString(it)
            new_arg = rc.Param(" --continue ", "fn_cont")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --o " + outputname + fn_run
            outputNodes = getOutputNodesRefine(outputname + fn_run, "MultiBody", -1, 1, 3, nr_bodies, is_tomo)

                else
                    fn_run = "run"
            new_arg = rc.Param(" --continue ", "fn_in")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --o " + outputname + fn_run
            outputNodes = getOutputNodesRefine(outputname + "run", "MultiBody", -1, 1, 3, nr_bodies, is_tomo)
            new_arg = rc.Param(" --solvent_correct_fsc --multibody_masks ", "fn_bodies")
    cli.args.append(new_arg)

            node = rc.Node(joboptions["fn_in")
    cli.args.append(new_arg), rh.LABEL_REFINE3D_OPT)
            inputNodes.push_back(node)

            #  Sampling
            int iover = 1
            new_arg = rc.Param(" --oversampling " + floatToString((float)iover)
            int sampling = JobOption::getHealPixOrder(joboptions["sampling")
    cli.args.append(new_arg))
            if sampling <= 0)
                            error_message = "Wrong choice for sampling"
                return false
                        #  The sampling given in the GUI will be the oversampled one!
            new_arg = rc.Param(" --healpix_order " + integerToString(sampling - iover)
            #  Always perform local searches!
            new_arg = rc.Param(" --auto_local_healpix_order " + integerToString(sampling - iover)

            #  Offset range
            new_arg = rc.Param(" --offset_range ", "offset_range")
    cli.args.append(new_arg)
            #  The sampling given in the GUI will be the oversampled one!
            new_arg = rc.Param(" --offset_step " + floatToString(joboptions["offset_step"].getNumber(error_message) * pow(2., iover))
            if error_message != "") return false
        
        if joboptions["do_blush"].getBoolean())
            new_arg = rc.Param(" --blush "

        if joboptions["do_subtracted_bodies"].getBoolean())
            new_arg = rc.Param(" --reconstruct_subtracted_bodies "

    #  Always do compute stuff
#   if !joboptions["do_combine_thru_disc"].getBoolean())
    new_arg = rc.Flag(" --dont_combine_weights_via_disc","","do_combine_thru_disc",False)
#   if !joboptions["do_parallel_discio"].getBoolean())
    new_arg = rc.Flag(" --no_parallel_disc_io","","do_parallel_discio",False)
#   if joboptions["do_preread_images"].getBoolean())
    new_arg = rc.Flag(" --preread_images ", "","do_preread_images", True)
#    else if joboptions["scratch_dir"] != "")
    new_arg = rc.Flag(" --scratch_dir ","scratch_dir","scratch_dir",True)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --pool ", "nr_pool")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --pad","1","do_pad1",True)
    cli.args.append(new_arg)
    new_arg = rc.Param(" --pad","2", "do_pad1", False)
    cli.args.append(new_arg)
    

        #  Running stuff
        new_arg = rc.Param(" --j ", "nr_threads")
    cli.args.append(new_arg)

        #  GPU-stuff
        if joboptions["use_gpu"].getBoolean())
                    new_arg = rc.Param(" --gpu \"", "gpu_ids")
    cli.args.append(new_arg) + "\""
        
        #  Other arguments
        new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

            } #  end if !is_continue || (is_continue && joboptions["fn_cont")
    cli.args.append(new_arg) != ""))

    if joboptions["do_analyse"].getBoolean())
            cli.add_prog(rc.Prog("`which relion_flex_analyse`")

        #  If we had performed relion_refine command, then fn_run would be set now
        #  Otherwise, we have to search for _model.star files that do NOT have a _it??? specifier
        if fn_run == "")
                    FileName fn_wildcard = outputname + "run*_model.star"
            std::vector<FileName> fns_model
            std::vector<FileName> fns_ok
            fn_wildcard.globFiles(fns_model)
            for (int i = 0 i < fns_model.size() i++)
                            if !fns_model[i].contains("_it"))
                    fns_ok.push_back(fns_model[i])
                        if fns_ok.size() == 0)
                            error_message = "ERROR: cannot find appropriate model.star file in the output directory"
                return false
                        if fns_ok.size() > 1)
                            error_message = "ERROR: there are more than one model.star files (without '_it' specifiers) in the output directory. Move all but one out of the way."
                return false
                        fn_run = fns_ok[0].beforeFirstOf("_model.star")
                else
            fn_run = outputname + fn_run

        #  General I/O
        new_arg = rc.Param(" --PCA_orient "
        new_arg = rc.Param(" --model " + fn_run + "_model.star"
        new_arg = rc.Param(" --data " + fn_run + "_data.star"
        new_arg = rc.Param(" --bodies ", "fn_bodies")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --o " + outputname + "analyse"

        #  Eigenvector movie maps
        if joboptions["nr_movies"].getNumber(error_message) > 0)
                    new_arg = rc.Param(" --do_maps "
            new_arg = rc.Param(" --k ", "nr_movies")
    cli.args.append(new_arg)
                if error_message != "") return false

        #  Selection
        if joboptions["do_select"].getBoolean())
                    float minval = joboptions["eigenval_min"].getNumber(error_message)
            if error_message != "") return false

            float maxval = joboptions["eigenval_max"].getNumber(error_message)
            if error_message != "") return false

            if  minval >= maxval)
                            error_message = "ERROR: the maximum eigenvalue should be larger than the minimum one!"
                return false
            
            new_arg = rc.Param(" --select_eigenvalue ", "select_eigenval")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --select_eigenvalue_min ", "eigenval_min")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --select_eigenvalue_max ", "eigenval_max")
    cli.args.append(new_arg)

            #  Add output node: selected particles star file
            FileName fnt = outputname + "analyse_eval"+integerToString(joboptions["select_eigenval"].getNumber(error_message),3)+"_select"
            if error_message != "") return false

            int min = ROUND(joboptions["eigenval_min"].getNumber(error_message))
            if error_message != "") return false

            int max = ROUND(joboptions["eigenval_max"].getNumber(error_message))
            if error_message != "") return false

            if min > -99998)
                fnt += "_min"+integerToString(min)
            if max < 99998)
                fnt += "_max"+integerToString(max)
            fnt += ".star"
            rc.Node node2(fnt, rh.LABEL_MULTIBODY_SEL_PARTS)
            outputNodes.push_back(node2)

        
        #  PDF with histograms of the eigenvalues
        rc.Node node3(outputname + "analyse_logfile.pdf", rh.LABEL_MULTIBODY_FLEXLOG)
        outputNodes.push_back(node3)

            
    return cli

def getCommandsMaskcreateJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    command="`which relion_mask_create`"

    #  I/O
    if joboptions["fn_in")
    cli.args.append(new_arg) == "")
            error_message = "ERROR: empty field for input STAR file..."
        return false
        new_arg = rc.Param(" --i ", "fn_in")
    cli.args.append(new_arg)
    node = rc.Node(joboptions["fn_in")
    cli.args.append(new_arg), joboptions["fn_in"].node_type)
    inputNodes.push_back(node)

    new_arg = rc.Param(" --o " + outputname + "mask.mrc"
    rc.Node node2(outputname + "mask.mrc", rh.LABEL_MASK3D_MASK)
    outputNodes.push_back(node2)

    if joboptions["lowpass_filter"].getNumber(error_message) > 0)
            new_arg = rc.Param(" --lowpass ", "lowpass_filter")
    cli.args.append(new_arg)
        if error_message != "") return false

    if joboptions["angpix"].getNumber(error_message) > 0)
            new_arg = rc.Param(" --angpix ", "angpix")
    cli.args.append(new_arg)
        if error_message != "") return false

    new_arg = rc.Param(" --ini_threshold ", "inimask_threshold")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --extend_inimask ", "extend_inimask")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --width_soft_edge ", "width_mask_edge")
    cli.args.append(new_arg)

    if joboptions["do_helix"].getBoolean())
            new_arg = rc.Param(" --helix --z_percentage " + floatToString(joboptions["helical_z_percentage"].getNumber(error_message) / 100.)
        if error_message != "") return false
    
    #  Running stuff
    new_arg = rc.Param(" --j ", "nr_threads")
    cli.args.append(new_arg)

    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return cli

def getCommandsJoinstarJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    
    command="`which relion_star_handler`"

    int ii = 0
    if joboptions["do_part"].getBoolean())
            ii++
        label += ".particles"
        if joboptions["do_mic"].getBoolean())
            ii++
        label += ".micrographs"
        if joboptions["do_mov"].getBoolean())
            ii++
        label += ".movies"
    
    if ii == 0)
            error_message = "You've selected no type of files for joining. Select a single type!"
        return false
    
    if ii > 1)
            error_message = "You've selected more than one type of files for joining. Only select a single type!"
        return false
    
    #  I/O
    if joboptions["do_part"].getBoolean())
            if joboptions["fn_part1")
    cli.args.append(new_arg) == "" || joboptions["fn_part2")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for first or second input STAR file..."
            return false
                new_arg = rc.Param(" --combine --i \" ", "fn_part1")
    cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_part1")
    cli.args.append(new_arg), joboptions["fn_part1"].node_type)
        inputNodes.push_back(node)
        new_arg = rc.Param(" ", "fn_part2")
    cli.args.append(new_arg)
        rc.Node node2(joboptions["fn_part2")
    cli.args.append(new_arg), joboptions["fn_part2"].node_type)
        inputNodes.push_back(node2)
        if joboptions["fn_part3")
    cli.args.append(new_arg) != "")
                    new_arg = rc.Param(" ", "fn_part3")
    cli.args.append(new_arg)
            rc.Node node3(joboptions["fn_part3")
    cli.args.append(new_arg), joboptions["fn_part3"].node_type)
            inputNodes.push_back(node3)
                if joboptions["fn_part4")
    cli.args.append(new_arg) != "")
                    new_arg = rc.Param(" ", "fn_part4")
    cli.args.append(new_arg)
            node4 = rc.Node(jo(joboptions["fn_part4")
    cli.args.append(new_arg), joboptions["fn_part4"].node_type)
            inputNodes.push_back(node4)
                new_arg = rc.Param(" \" "

        #  Check for duplicates
        new_arg = rc.Param(" --check_duplicates rlnImageName "
        new_arg = rc.Param(" --o " + outputname + "join_particles.star"
        rc.Node node5(outputname + "join_particles.star", joboptions["fn_part1"].node_type)
        outputNodes.push_back(node5)

        else if joboptions["do_mic"].getBoolean())
            if joboptions["fn_mic1")
    cli.args.append(new_arg) == "" || joboptions["fn_mic2")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for first or second input STAR file..."
            return false
                new_arg = rc.Param(" --combine --i \" ", "fn_mic1")
    cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_mic1")
    cli.args.append(new_arg), joboptions["fn_mic1"].node_type)
        inputNodes.push_back(node)
        new_arg = rc.Param(" ", "fn_mic2")
    cli.args.append(new_arg)
        rc.Node node2(joboptions["fn_mic2")
    cli.args.append(new_arg), joboptions["fn_mic2"].node_type)
        inputNodes.push_back(node2)
        if joboptions["fn_mic3")
    cli.args.append(new_arg) != "")
                    new_arg = rc.Param(" ", "fn_mic3")
    cli.args.append(new_arg)
            rc.Node node3(joboptions["fn_mic3")
    cli.args.append(new_arg), joboptions["fn_mic3"].node_type)
            inputNodes.push_back(node3)
                if joboptions["fn_mic4")
    cli.args.append(new_arg) != "")
                    new_arg = rc.Param(" ", "fn_mic4")
    cli.args.append(new_arg)
            node4 = rc.Node(jo(joboptions["fn_mic4")
    cli.args.append(new_arg), joboptions["fn_mic4"].node_type)
            inputNodes.push_back(node4)
                new_arg = rc.Param(" \" "

        #  Check for duplicates
        new_arg = rc.Param(" --check_duplicates rlnMicrographName "
        new_arg = rc.Param(" --o " + outputname + "join_mics.star"
        rc.Node node5(outputname + "join_mics.star", joboptions["fn_mic1"].node_type)
        outputNodes.push_back(node5)

        else if joboptions["do_mov"].getBoolean())
            if joboptions["fn_mov1")
    cli.args.append(new_arg) == "" || joboptions["fn_mov2")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for first or second input STAR file..."
            return false
                new_arg = rc.Param(" --combine --i \" ", "fn_mov1")
    cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_mov1")
    cli.args.append(new_arg), joboptions["fn_mov1"].node_type)
        inputNodes.push_back(node)
        new_arg = rc.Param(" ", "fn_mov2")
    cli.args.append(new_arg)
        rc.Node node2(joboptions["fn_mov2")
    cli.args.append(new_arg), joboptions["fn_mov2"].node_type)
        inputNodes.push_back(node2)
        if joboptions["fn_mov3")
    cli.args.append(new_arg) != "")
                    new_arg = rc.Param(" ", "fn_mov3")
    cli.args.append(new_arg)
            rc.Node node3(joboptions["fn_mov3")
    cli.args.append(new_arg), joboptions["fn_mov3"].node_type)
            inputNodes.push_back(node3)
                if joboptions["fn_mov4")
    cli.args.append(new_arg) != "")
                    new_arg = rc.Param(" ", "fn_mov4")
    cli.args.append(new_arg)
            node4 = rc.Node(jo(joboptions["fn_mov4")
    cli.args.append(new_arg), joboptions["fn_mov4"].node_type)
            inputNodes.push_back(node4)
                new_arg = rc.Param(" \" "

        #  Check for duplicates
        new_arg = rc.Param(" --check_duplicates rlnMicrographMovieName "
        new_arg = rc.Param(" --o " + outputname + "join_movies.star"
        rc.Node node5(outputname + "join_movies.star", joboptions["fn_mov1"].node_type)
        outputNodes.push_back(node5)
    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return cli

def getCommandsSubtractJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    if joboptions["do_fliplabel"].getBoolean())
            if joboptions["nr_mpi"].getNumber(error_message) > 1)
                    error_message = "You cannot use MPI parallelization to revert particle labels."
            return false
        
        node = rc.Node(joboptions["fn_fliplabel")
    cli.args.append(new_arg), joboptions["fn_fliplabel"].node_type)
        inputNodes.push_back(node)

        rc.Node node2(outputname + "original.star", rh.LABEL_SUBTRACT_REVERTED)
        outputNodes.push_back(node2)

        label += ".revert"

        cli.add_prog(rc.Prog("`which relion_particle_subtract`"))
        new_arg = rc.Param(" --revert ", "fn_fliplabel")
    cli.args.append(new_arg) + " --o " + outputname
        else
            if joboptions["nr_mpi"].getNumber(error_message) > 1)
            command="`which relion_particle_subtract_mpi`"
        else
            command="`which relion_particle_subtract`"
        if error_message != "") return false

        #  I/O
        if joboptions["fn_opt")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: empty field for input optimiser.star..."
            return false
                new_arg = rc.Param(" --i ", "fn_opt")
    cli.args.append(new_arg)
        node = rc.Node(joboptions["fn_opt")
    cli.args.append(new_arg), rh.LABEL_OPTIMISER_CPIPE)
        inputNodes.push_back(node)

        if joboptions["fn_mask")
    cli.args.append(new_arg) != "")
                    new_arg = rc.Param(" --mask ", "fn_mask")
    cli.args.append(new_arg)
            rc.Node node2(joboptions["fn_mask")
    cli.args.append(new_arg), joboptions["fn_mask"].node_type)
            inputNodes.push_back(node2)
                if joboptions["do_data"].getBoolean())
                    if joboptions["fn_data")
    cli.args.append(new_arg) == "")
                            error_message = "ERROR: empty field for the input particle STAR file..."
                return false
                        new_arg = rc.Param(" --data ", "fn_data")
    cli.args.append(new_arg)
            rc.Node node3(joboptions["fn_data")
    cli.args.append(new_arg), joboptions["fn_data"].node_type)
            inputNodes.push_back(node3)
        
        new_arg = rc.Param(" --o " + outputname
        node4 = rc.Node(jo(outputname + "particles_subtracted.star", rh.LABEL_SUBTRACT_SUBTRACTED)
        outputNodes.push_back(node4)

        if joboptions["do_center_mask"].getBoolean())
                    new_arg = rc.Param(" --recenter_on_mask"
                else if joboptions["do_center_xyz"].getBoolean())
                    new_arg = rc.Param(" --center_x ", "center_x")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --center_y ", "center_y")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --center_z ", "center_z")
    cli.args.append(new_arg)
        
        if joboptions["do_float16"].getBoolean())
                    new_arg = rc.Param(" --float16 "
        
        if joboptions["new_box"].getNumber(error_message) > 0)
                    new_arg = rc.Param(" --new_box ", "new_box")
    cli.args.append(new_arg)
                if error_message != "") return false

    
    #  Other arguments
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

    
    return cli

def getCommandsPostprocessJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    command="`which relion_postprocess`"

    #  Input mask
    if joboptions["fn_mask")
    cli.args.append(new_arg) == "")
            error_message = "ERROR: empty field for input mask..."
        return false
        new_arg = rc.Param(" --mask ", "fn_mask")
    cli.args.append(new_arg)
    rc.Node node3(joboptions["fn_mask")
    cli.args.append(new_arg), joboptions["fn_mask"].node_type)
    inputNodes.push_back(node3)

    #  Input half map (one of them)
    FileName fn_half1 = joboptions["fn_in")
    cli.args.append(new_arg)
    FileName fn_half2

    if fn_half1 == "")
            error_message = "ERROR: empty field for input half-map..."
        return false
    
    if fn_half1 != "")
            if !fn_half1.getTheOtherHalf(fn_half2))
                    error_message = "ERROR: cannot find 'half' substring in the input filename..."
            return false
        
        rc.Node node(fn_half1, joboptions["fn_in"].node_type)
        inputNodes.push_back(node)
        new_arg = rc.Param(" --i " + fn_half1
    
    #  The output name contains a directory: use it for output
    new_arg = rc.Param(" --o " + outputname + "postprocess"
    new_arg = rc.Param("  --angpix ", "angpix")
    cli.args.append(new_arg)
    rc.Node node1(outputname+"postprocess.mrc", rh.LABEL_POST_MAP)
    outputNodes.push_back(node1)
    rc.Node node2(outputname+"postprocess_masked.mrc", rh.LABEL_POST_MASKED)
    outputNodes.push_back(node2)

    rc.Node node2b(outputname+"logfile.pdf", rh.LABEL_POST_LOG)
    outputNodes.push_back(node2b)

    rc.Node node2c(outputname+"postprocess.star", rh.LABEL_POST_POST)
    outputNodes.push_back(node2c)

    #  Sharpening
    if joboptions["fn_mtf")
    cli.args.append(new_arg).length() > 0)
            new_arg = rc.Param(" --mtf ", "fn_mtf")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --mtf_angpix ", "mtf_angpix")
    cli.args.append(new_arg)
        if joboptions["do_auto_bfac"].getBoolean())
            new_arg = rc.Param(" --auto_bfac "
        new_arg = rc.Param(" --autob_lowres ", "autob_lowres")
    cli.args.append(new_arg)
        if joboptions["do_adhoc_bfac"].getBoolean())
            new_arg = rc.Param(" --adhoc_bfac ", "adhoc_bfac")
    cli.args.append(new_arg)
    
    #  Filtering
    if joboptions["do_skip_fsc_weighting"].getBoolean())
            new_arg = rc.Param(" --skip_fsc_weighting "
        new_arg = rc.Param(" --low_pass " , "low_pass")
    cli.args.append(new_arg)
    
    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)

        return cli

def getCommandsLocalresJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    if joboptions["do_resmap_locres"].getBoolean() == joboptions["do_relion_locres"].getBoolean())
            error_message = "ERROR: choose either ResMap or Relion for local resolution estimation"
        return false
    
    if joboptions["fn_in")
    cli.args.append(new_arg) == "")
            error_message = "ERROR: empty field for input half-map..."
        return false
        #  Get the two half-reconstruction names from the single one
    FileName fn_half1 = joboptions["fn_in")
    cli.args.append(new_arg)
    FileName fn_half2
    if !fn_half1.getTheOtherHalf(fn_half2))
            error_message = "ERROR: cannot find 'half' substring in the input filename..."
        return false
    
    node = rc.Node(joboptions["fn_in")
    cli.args.append(new_arg), joboptions["fn_in"].node_type)
    inputNodes.push_back(node)

    if joboptions["do_resmap_locres"].getBoolean())
    
        label += ".resmap"

        #  ResMap wrapper
        if joboptions["fn_resmap")
    cli.args.append(new_arg).length() == 0)
                    error_message = "ERROR: please provide an executable for the ResMap program."
            return false
        
        if joboptions["fn_mask")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: Please provide an input mask for ResMap local-resolution estimation."
            return false
        
        if joboptions["do_queue"].getBoolean())
                    error_message = "ERROR: You cannot submit a ResMap job to the queue, as it needs user interaction."
            return false
        
        if joboptions["nr_mpi"].getNumber(error_message) > 1)
                    error_message = "You cannot use more than 1 MPI processor for the ResMap wrapper..."
            return false
                if error_message != "") return false

        #  Make symbolic links to the half-maps in the output directory
        commands.push_back("ln -s ../../" + fn_half1 + " " + outputname + "half1.mrc")
        commands.push_back("ln -s ../../" + fn_half2 + " " + outputname + "half2.mrc")

        rc.Node node2(joboptions["fn_mask")
    cli.args.append(new_arg), joboptions["fn_mask"].node_type)
        inputNodes.push_back(node2)

        rc.Node node3(outputname + "half1_resmap.mrc", rh.LABEL_LOCRES_RESMAP)
        outputNodes.push_back(node3)

        command = joboptions["fn_resmap")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --maskVol=", "fn_mask")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --noguiSplit " + outputname + "half1.mrc " +  outputname + "half2.mrc"
        new_arg = rc.Param(" --vxSize=", "angpix")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --pVal=", "pval")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --minRes=", "minres")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --maxRes=", "maxres")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --stepRes=", "stepres")
    cli.args.append(new_arg)

        else if joboptions["do_relion_locres"].getBoolean())
            #  Relion postprocessing
        label += ".own"

        if joboptions["nr_mpi"].getNumber(error_message) > 1)
            command="`which relion_postprocess_mpi`"
        else
            command="`which relion_postprocess`"
        if error_message != "") return false

        new_arg = rc.Param(" --locres --i ", "fn_in")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --o " + outputname + "relion"
        new_arg = rc.Param(" --angpix ", "angpix")
    cli.args.append(new_arg)
        # new_arg = rc.Param(" --locres_sampling ", "locres_sampling")
    cli.args.append(new_arg)
        # new_arg = rc.Param(" --locres_randomize_at ", "randomize_at")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --adhoc_bfac ", "adhoc_bfac")
    cli.args.append(new_arg)
        if joboptions["fn_mtf")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --mtf ", "fn_mtf")
    cli.args.append(new_arg)

        if joboptions["fn_mask")
    cli.args.append(new_arg) != "")
                    new_arg = rc.Param(" --mask ", "fn_mask")
    cli.args.append(new_arg)
            rc.Node node0(outputname+"histogram.pdf", rh.LABEL_LOCRES_LOG)
            outputNodes.push_back(node0)
        
        rc.Node node1(outputname+"relion_locres_filtered.mrc", rh.LABEL_LOCRES_FILTMAP)
        outputNodes.push_back(node1)
        rc.Node node2(outputname+"relion_locres.mrc", rh.LABEL_LOCRES_RESMAP)
        outputNodes.push_back(node2)
    
    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    return cli

def getCommandsDynaMightJob(std::string &outputname, std::vector<std::string> &commands,
                                       std::string &final_command, bool do_makedir, int job_counter, std::string &error_message):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    command = joboptions["fn_dynamight_exe")
    cli.args.append(new_arg)

    if !is_continue)
            #  New jobs need to add the input nodes

        node = rc.Node(joboptions["fn_star")
    cli.args.append(new_arg), joboptions["fn_star"].node_type)
        inputNodes.push_back(node)
        rc.Node node2(joboptions["fn_map")
    cli.args.append(new_arg), joboptions["fn_map"].node_type)
        inputNodes.push_back(node2)
        /*
        if joboptions["fn_mask")
    cli.args.append(new_arg) != "")
                    rc.Node node3(joboptions["fn_mask")
    cli.args.append(new_arg), joboptions["fn_mask"].node_type)
            inputNodes.push_back(node3)
                */
        else
            int c = 0
        if joboptions["do_visualize"].getBoolean()) c++
        if joboptions["do_inverse"].getBoolean()) c++
        if joboptions["do_reconstruct"].getBoolean()) c++
        if c == 0)
                    error_message = "You need to select at least one task on one of the tabs..."
            return false
                if c > 1)
                    error_message = "You can not perform more than one task simultaneously..."
            return false
            
    if !is_continue || !(joboptions["do_visualize"].getBoolean() || joboptions["do_inverse"].getBoolean() || joboptions["do_reconstruct"].getBoolean()) )
            new_arg = rc.Param(" optimize-deformations "
        new_arg = rc.Param(" --refinement-star-file ", "fn_star")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --output-directory " + outputname
        new_arg = rc.Param(" --initial-model ", "fn_map")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --n-gaussians ", "nr_gaussians")
    cli.args.append(new_arg)
        if joboptions["initial_threshold")
    cli.args.append(new_arg) != "")
        new_arg = rc.Param(" --initial-threshold ", "initial_threshold")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --regularization-factor " , "reg_factor")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --n-threads ", "nr_threads")
    cli.args.append(new_arg)

        if joboptions["do_preload"].getBoolean())
            new_arg = rc.Param(" --preload-images "

        # if joboptions["fn_mask")
    cli.args.append(new_arg) != "")
        #     new_arg = rc.Param(" --mask-file ", "fn_mask")
    cli.args.append(new_arg)

        else if joboptions["do_visualize"].getBoolean())
    
        new_arg = rc.Param(" explore-latent-space " + outputname
        new_arg = rc.Param(" --half-set ", "halfset")
    cli.args.append(new_arg)

        if joboptions["fn_checkpoint")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --checkpoint-file ", "fn_checkpoint")
    cli.args.append(new_arg)

        # if joboptions["fn_mask")
    cli.args.append(new_arg) != "")
        #     new_arg = rc.Param(" --mask-file ", "fn_mask")
    cli.args.append(new_arg)
        else if joboptions["do_inverse"].getBoolean())
            new_arg = rc.Param(" optimize-inverse-deformations " + outputname
        new_arg = rc.Param(" --n-epochs ", "nr_epochs")
    cli.args.append(new_arg)

        if joboptions["fn_checkpoint")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --checkpoint-file ", "fn_checkpoint")
    cli.args.append(new_arg)

        if joboptions["do_store_deform"].getBoolean())
            new_arg = rc.Param(" --save-deformations "

        if joboptions["do_preload"].getBoolean())
            new_arg = rc.Param(" --preload-images"
        else if joboptions["do_reconstruct"].getBoolean())
            new_arg = rc.Param(" deformable-backprojection " + outputname
        new_arg = rc.Param(" --batch-size ", "backproject_batchsize")
    cli.args.append(new_arg)

        if joboptions["fn_checkpoint")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --checkpoint-file ", "fn_checkpoint")
    cli.args.append(new_arg)

        if joboptions["do_preload"].getBoolean())
            new_arg = rc.Param(" --preload-images"

        # if joboptions["fn_mask")
    cli.args.append(new_arg) != "")
        #     new_arg = rc.Param(" --mask-file ", "fn_mask")
    cli.args.append(new_arg)

        rc.Node onode(outputname + "backprojection/map_half1.mrc", rh.LABEL_DYNAMIGHT_HALFMAP)
        outputNodes.push_back(onode)
        rc.Node onode2(outputname + "backprojection/map_half2.mrc", rh.LABEL_DYNAMIGHT_HALFMAP)
        outputNodes.push_back(onode2)

    
    if joboptions["gpu_id")
    cli.args.append(new_arg) != "")
        new_arg = rc.Param(" --gpu-id ", "gpu_id")
    cli.args.append(new_arg)

    #  Other arguments for model_angelo
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    #  Besides

    return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message, true)

def getCommandsModelAngeloJob(std::string &outputname, std::vector<std::string> &commands,
               std::string &final_command, bool do_makedir, int job_counter, std::string &error_message):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)

    FileName outputmodel = outputname
    outputmodel = (outputmodel.afterFirstOf("/")).beforeLastOf("/")
    outputmodel = outputname + outputmodel + ".cif"

    #  Only run model building for new job or if output.cif is not there yet.
    if !is_continue || !exists(outputmodel) )
            #  Run on a map
        node = rc.Node(joboptions["fn_map")
    cli.args.append(new_arg), joboptions["fn_map"].node_type)
        inputNodes.push_back(node)

         = joboptions["fn_modelangelo_exe")
    cli.args.append(new_arg)
        if joboptions["p_seq")
    cli.args.append(new_arg) != "" || joboptions["d_seq")
    cli.args.append(new_arg) != "" || joboptions["r_seq")
    cli.args.append(new_arg) != "" )
                    new_arg = rc.Param(" build "

            if joboptions["p_seq")
    cli.args.append(new_arg) != "" )
                            #  Run with a protein sequence file
                rc.Node node2(joboptions["p_seq")
    cli.args.append(new_arg), joboptions["p_seq"].node_type)
                inputNodes.push_back(node2)

                new_arg = rc.Param(" -pf ", "p_seq")
    cli.args.append(new_arg)
                        if joboptions["d_seq")
    cli.args.append(new_arg) != "" )
                            #  Run with a DNA sequence file
                rc.Node node2(joboptions["d_seq")
    cli.args.append(new_arg), joboptions["d_seq"].node_type)
                inputNodes.push_back(node2)

                new_arg = rc.Param(" -df ", "d_seq")
    cli.args.append(new_arg)
                        if joboptions["r_seq")
    cli.args.append(new_arg) != "" )
                            #  Run with a protein sequence file
                rc.Node node2(joboptions["r_seq")
    cli.args.append(new_arg), joboptions["r_seq"].node_type)
                inputNodes.push_back(node2)

                new_arg = rc.Param(" -rf ", "r_seq")
    cli.args.append(new_arg)
                            else
                    new_arg = rc.Param(" build_no_seq "
        
        new_arg = rc.Param(" -v ", "fn_map")
    cli.args.append(new_arg)
        new_arg = rc.Param(" -o " + outputname
        new_arg = rc.Param(" -d ", "gpu_id")
    cli.args.append(new_arg)

        rc.Node node3(outputmodel, rh.LABEL_ATOMCOORDS_CPIPE)
        outputNodes.push_back(node3)

        #  Other arguments for model_angelo
        new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
            
    #  If no sequence was provided, but a library was provided, then also run an HMM search
    if joboptions["do_hhmer"].getBoolean())
            if joboptions["fn_lib")
    cli.args.append(new_arg) == "")
                    error_message = "ERROR: you need to provide a library to perform the HMM search against."
            return false
        
        2 = joboptions["fn_modelangelo_exe")
    cli.args.append(new_arg)

        command2 += " hmm_search "
        command2 += " -i " + outputname
        command2 += " -f ", "fn_lib")
    cli.args.append(new_arg)
        command2 += " -o " + outputname
        command2 += " -a ", "alphabet")
    cli.args.append(new_arg)

        # HMMSearch parameters
        command2 += " --F1 ", "F1")
    cli.args.append(new_arg)
        command2 += " --F2 ", "F2")
    cli.args.append(new_arg)
        command2 += " --F3 ", "F3")
    cli.args.append(new_arg)
        command2 += " --E ", "E")
    cli.args.append(new_arg)

        #  Other arguments for model_angelo
        command2 += " ", "other_args")
    cli.args.append(new_arg)
        commands.push_back(command2)
    
    return prepareFinalCommand(outputname, commands, final_command, do_makedir, error_message, true)

def getCommandsMotionrefineJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    rc.Prog("`which relion_motion_refine_mpi`","use_mpi",True)
    rc.Prog("`which relion_motion_refine`","use_mpi",False)

    if joboptions["fn_data")
    cli.args.append(new_arg) == "")
            error_message = "ERROR: empty field for input particle STAR file..."
        return false
        if joboptions["fn_mic")
    cli.args.append(new_arg) == "")
            error_message = "ERROR: empty field for input micrograph STAR file..."
        return false
        if joboptions["fn_post")
    cli.args.append(new_arg) == "")
            error_message = "ERROR: empty field for input PostProcess STAR file..."
        return false
    
    if joboptions["do_param_optim"].getBoolean() && joboptions["do_polish"].getBoolean())
            error_message = "ERROR: Choose either parameter training or polishing, not both."
        return false
    
    if !joboptions["do_param_optim"].getBoolean() && !joboptions["do_polish"].getBoolean())
            error_message = "ERROR: nothing to do, choose either parameter training or polishing."
        return false
    
    if (joboptions["eval_frac"].getNumber(error_message) <= 0.1 || joboptions["eval_frac"].getNumber(error_message) > 0.9 )
            && !joboptions["eval_frac"].isSchedulerVariable() )
            error_message = "ERROR: the fraction of Fourier pixels used for evaluation should be between 0.1 and 0.9."
        return false
        if error_message != "") return false

    node = rc.Node(joboptions["fn_data")
    cli.args.append(new_arg), joboptions["fn_data"].node_type)
    inputNodes.push_back(node)

    rc.Node node2(joboptions["fn_post")
    cli.args.append(new_arg), joboptions["fn_post"].node_type)
    inputNodes.push_back(node)

    new_arg = rc.Param(" --i ", "fn_data")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --f ", "fn_post")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --corr_mic ", "fn_mic")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --first_frame ", "first_frame")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --last_frame ", "last_frame")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --o " + outputname

    if joboptions["do_float16"].getBoolean())
            new_arg = rc.Param(" --float16 "
    
    if joboptions["do_param_optim"].getBoolean())
    
        label += ".train"

        #  Estimate meta-parameters
        RFLOAT align_frac = 1.0 - joboptions["eval_frac"].getNumber(error_message)
        if error_message != "") return false
        new_arg = rc.Param(" --min_p ", "optim_min_part")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --eval_frac ", "eval_frac")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --align_frac " + floatToString(align_frac)

        if joboptions["sigma_acc"].getNumber(error_message) < 0)
                    new_arg = rc.Param(" --params2 "
                else
                    new_arg = rc.Param(" --params3 "
                if error_message != "") return false

        rc.Node node5(outputname+"opt_params_all_groups.txt", rh.LABEL_POLISH_PARAMS)
        outputNodes.push_back(node5)
        else if joboptions["do_polish"].getBoolean())
            if joboptions["do_own_params"].getBoolean())
                    #  User-specified Parameters
            new_arg = rc.Param(" --s_vel ", "sigma_vel")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --s_div ", "sigma_div")
    cli.args.append(new_arg)
            new_arg = rc.Param(" --s_acc ", "sigma_acc")
    cli.args.append(new_arg)
                else
                    if joboptions["opt_params")
    cli.args.append(new_arg) == "")
                            error_message = "ERROR: Please specify an optimised parameter file OR choose 'use own paramaeters' and set three sigma values."
                return false
                        new_arg = rc.Param(" --params_file ", "opt_params")
    cli.args.append(new_arg)
        
        new_arg = rc.Param(" --combine_frames"
        new_arg = rc.Param(" --bfac_minfreq ", "minres")
    cli.args.append(new_arg)
        new_arg = rc.Param(" --bfac_maxfreq ", "maxres")
    cli.args.append(new_arg)

        const int window = ROUND(joboptions["extract_size"].getNumber(error_message))
        if error_message != "") return false

        const int scale = ROUND(joboptions["rescale"].getNumber(error_message))
        if error_message != "") return false

        if window * scale <= 0)
                    error_message = "ERROR: Please specify both the extraction box size and the downsampled size, or leave both the default (-1)"
            return false
        
        if window > 0 && scale > 0)
                    if window % 2 != 0)
                            error_message = "ERROR: The extraction box size must be an even number"
                return false
                        new_arg = rc.Param(" --window ", "extract_size")
    cli.args.append(new_arg)

            if scale % 2 != 0)
                            error_message = "ERROR: The downsampled box size must be an even number."
                return false
            
            if scale > window)
                            error_message = "ERROR: The downsampled box size cannot be larger than the extraction size."
                return false
                        new_arg = rc.Param(" --scale ", "rescale")
    cli.args.append(new_arg)
        
        rc.Node node6(outputname+"logfile.pdf", rh.LABEL_POLISH_LOG)
        outputNodes.push_back(node6)

        rc.Node node7(outputname+"shiny.star", rh.LABEL_POLISH_PARTS)
        outputNodes.push_back(node7)
    
    #  If this is a continue job, then only process unfinished micrographs
    if is_continue)
        new_arg = rc.Param(" --only_do_unfinished "

    #  Running stuff
    new_arg = rc.Param(" --j ", "nr_threads")
    cli.args.append(new_arg)

    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    return cli

def getCommandsCtfrefineJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    


    rc.Prog("`which relion_ctf_refine_mpi`","use_mpi",True)
    rc.Prog("`which relion_ctf_refine`","use_mpi",False)

    if joboptions["fn_data")
    cli.args.append(new_arg) == "")
            error_message = "ERROR: empty field for input particle STAR file..."
        return false
        if joboptions["fn_post")
    cli.args.append(new_arg) == "")
            error_message = "ERROR: empty field for input PostProcess STAR file..."
        return false
    
    if !joboptions["do_aniso_mag"].getBoolean() &&
        !joboptions["do_ctf"].getBoolean() &&
        !joboptions["do_tilt"].getBoolean() &&
        !joboptions["do_4thorder"].getBoolean())
            error_message = "ERROR: you haven't selected to fit anything..."
        return false
    
    if !joboptions["do_aniso_mag"].getBoolean() && joboptions["do_ctf"].getBoolean() &&
        joboptions["do_defocus")
    cli.args.append(new_arg) == job_ctffit_options[0] &&
        joboptions["do_astig")
    cli.args.append(new_arg) == job_ctffit_options[0] &&
        joboptions["do_bfactor")
    cli.args.append(new_arg) == job_ctffit_options[0] &&
        joboptions["do_phase")
    cli.args.append(new_arg) == job_ctffit_options[0])
            error_message = "ERROR: you did not select any CTF parameter to fit. Either switch off CTF parameter fitting, or select one to fit."
        return false
    
    node = rc.Node(joboptions["fn_data")
    cli.args.append(new_arg), joboptions["fn_data"].node_type)
    inputNodes.push_back(node)

    rc.Node node2(joboptions["fn_post")
    cli.args.append(new_arg), joboptions["fn_post"].node_type)
    inputNodes.push_back(node)

    rc.Node node6(outputname+"logfile.pdf", rh.LABEL_CTFREFINE_LOG)
    outputNodes.push_back(node6)

    new_arg = rc.Param(" --i ", "fn_data")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --f ", "fn_post")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --o " + outputname

    #  Always either do anisotropic magnification, or CTF,tilt-odd,even
    if joboptions["do_aniso_mag"].getBoolean())
            label += ".anisomag"

        new_arg = rc.Param(" --fit_aniso"
        new_arg = rc.Param(" --kmin_mag ", "minres")
    cli.args.append(new_arg)

        rc.Node node5(outputname+"particles_ctf_refine.star", rh.LABEL_CTFREFINE_ANISOPARTS)
        outputNodes.push_back(node5)

        else
            rc.Node node5(outputname+"particles_ctf_refine.star", rh.LABEL_CTFREFINE_REFINEPARTS)
        outputNodes.push_back(node5)

        if joboptions["do_ctf"].getBoolean())
                    new_arg = rc.Param(" --fit_defocus --kmin_defocus ", "minres")
    cli.args.append(new_arg)
            std::string fit_options = ""

            fit_options += JobOption::getCtfFitString(joboptions["do_phase")
    cli.args.append(new_arg))
            fit_options += JobOption::getCtfFitString(joboptions["do_defocus")
    cli.args.append(new_arg))
            fit_options += JobOption::getCtfFitString(joboptions["do_astig")
    cli.args.append(new_arg))
            fit_options += "f" #  always have Cs refinement switched off
            fit_options += JobOption::getCtfFitString(joboptions["do_bfactor")
    cli.args.append(new_arg))

            if fit_options.size() != 5)
                            error_message = "Wrong CTF fitting options"
                return false
            
            new_arg = rc.Param(" --fit_mode " + fit_options
        
        #  do not allow anisotropic magnification to be done simultaneously with higher-order aberrations
        if joboptions["do_tilt"].getBoolean())
                    new_arg = rc.Param(" --fit_beamtilt"
            new_arg = rc.Param(" --kmin_tilt ", "minres")
    cli.args.append(new_arg)

            if joboptions["do_trefoil"].getBoolean())
                            new_arg = rc.Param(" --odd_aberr_max_n 3"
                    
        if joboptions["do_4thorder"].getBoolean())
                    new_arg = rc.Param(" --fit_aberr"
            
    #  If this is a continue job, then only process unfinished micrographs
    if is_continue)
            new_arg = rc.Param(" --only_do_unfinished "
    
    #  Running stuff
    new_arg = rc.Param(" --j ", "nr_threads")
    cli.args.append(new_arg)

    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    return cli

def getCommandsExternalJob(outputname,label,job_counter=-1):
    cli = clear(label)
    initialisePipeline(outputname, job_counter)
    

    if joboptions["fn_exe")
    cli.args.append(new_arg) == "")
            error_message = "ERROR: empty field for the external executable script..."
        return false
    
    command=joboptions["fn_exe")
    cli.args.append(new_arg)
    new_arg = rc.Param(" --o " + outputname

    #  Optional input nodes
    if joboptions["in_mov")
    cli.args.append(new_arg) != "")
            node = rc.Node(joboptions["in_mov")
    cli.args.append(new_arg), joboptions["in_mov"].node_type)
        inputNodes.push_back(node)
        new_arg = rc.Param(" --in_movies ", "in_mov")
    cli.args.append(new_arg)
        if joboptions["in_mic")
    cli.args.append(new_arg) != "")
            node = rc.Node(joboptions["in_mic")
    cli.args.append(new_arg), joboptions["in_mic"].node_type)
        inputNodes.push_back(node)
        new_arg = rc.Param(" --in_mics ", "in_mic")
    cli.args.append(new_arg)
        if joboptions["in_part")
    cli.args.append(new_arg) != "")
            node = rc.Node(joboptions["in_part")
    cli.args.append(new_arg), joboptions["in_part"].node_type)
        inputNodes.push_back(node)
        new_arg = rc.Param(" --in_parts ", "in_part")
    cli.args.append(new_arg)
        if joboptions["in_coords")
    cli.args.append(new_arg) != "")
            node = rc.Node(joboptions["in_coords")
    cli.args.append(new_arg), joboptions["in_coords"].node_type)
        inputNodes.push_back(node)
        new_arg = rc.Param(" --in_coords ", "in_coords")
    cli.args.append(new_arg)
        if joboptions["in_3dref")
    cli.args.append(new_arg) != "")
            node = rc.Node(joboptions["in_3dref")
    cli.args.append(new_arg), joboptions["in_3dref"].node_type)
        inputNodes.push_back(node)
        new_arg = rc.Param(" --in_3dref ", "in_3dref")
    cli.args.append(new_arg)
        if joboptions["in_mask")
    cli.args.append(new_arg) != "")
            node = rc.Node(joboptions["in_mask")
    cli.args.append(new_arg), joboptions["in_mask"].node_type)
        inputNodes.push_back(node)
        new_arg = rc.Param(" --in_mask ", "in_mask")
    cli.args.append(new_arg)
    
    #  Optional arguments
    if joboptions["param1_label")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --", "param1_label")
    cli.args.append(new_arg) + " ", "param1_value")
    cli.args.append(new_arg)
        if joboptions["param2_label")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --", "param2_label")
    cli.args.append(new_arg) + " ", "param2_value")
    cli.args.append(new_arg)
        if joboptions["param3_label")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --", "param3_label")
    cli.args.append(new_arg) + " ", "param3_value")
    cli.args.append(new_arg)
        if joboptions["param4_label")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --", "param4_label")
    cli.args.append(new_arg) + " ", "param4_value")
    cli.args.append(new_arg)
        if joboptions["param5_label")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --", "param5_label")
    cli.args.append(new_arg) + " ", "param5_value")
    cli.args.append(new_arg)
        if joboptions["param6_label")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --", "param6_label")
    cli.args.append(new_arg) + " ", "param6_value")
    cli.args.append(new_arg)
        if joboptions["param7_label")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --", "param7_label")
    cli.args.append(new_arg) + " ", "param7_value")
    cli.args.append(new_arg)
        if joboptions["param8_label")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --", "param8_label")
    cli.args.append(new_arg) + " ", "param8_value")
    cli.args.append(new_arg)
        if joboptions["param9_label")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --", "param9_label")
    cli.args.append(new_arg) + " ", "param9_value")
    cli.args.append(new_arg)
        if joboptions["param10_label")
    cli.args.append(new_arg) != "")
            new_arg = rc.Param(" --", "param10_label")
    cli.args.append(new_arg) + " ", "param10_value")
    cli.args.append(new_arg)
    
    #  Running stuff
    new_arg = rc.Param(" --j ", "nr_threads")
    cli.args.append(new_arg)

    #  Other arguments for extraction
    new_arg = rc.Param(" ", "other_args")
    cli.args.append(new_arg)
    
    return cli



def getCommands(cmdtype,subtype):

    bool result = false
    commands = None
    final_command = None
    do_makedir = None
    job_counter = None
    error_message = None
    outputname =  rh.proc_type2dirname(rh.PROC_IMPORT) + '/job{counter}/'
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

cmd = getCommands(rh.PROC_IMPORT)
print(cmd)

