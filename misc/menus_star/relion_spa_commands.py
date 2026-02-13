import relion_h as rh
# import relion_option as ro
import relion_command as rc

class Node:
    def __init__(self,name,nodetype):
        self.name = name
        self.nodetype = nodetype

class Command:
    def __init__(self):
      args = []
      
    def add(self,cmnd_type,cmnd_content,cmnd_flag='?',cmnd_bool='?'):
        if cmnd_type in ['prog','io','param','flag']:
            args.append({'type':cmnd_type'content':cmnd_content_content,'flag': cmnd_flag,'bool':cmnd_bool})

class Arg:
    def __init__(self):
        pass

    def assertion(self,type):
        self.assertion = type


class Flag(Arg):
    def __init__(self,type,arg,flag,boolean):
        super(self,Flag).__init__()
        # arg if value == boolean
        self.arg = arg
        self.flag = value
        self.value = boolean

class Param(Arg):
    def __init__(self,type,arg,value,assertion=None):
        super(self,Param).__init__()
        self.arg = arg
        self.value = str(value)
        self.assertion = assertion

class CLI:
    def __init__(self):
        self.command: None
        self.args: []
        self.outnodes = []
        self.innodes = []

    def add_outnode(self,nod):
        self.outnodes.append(nod)


      
def initialisePipeline(outputname,job_counter):
    job_counter += 1
    outputname = ""
    

def clear():
  pass
  

def getCommandsImportJobRaw(outputname, job_counter=-1):
    cli = CLI()
    commands = []
    outputNodes = []
    error_message = ""
    
    cli.command = "relion_import"
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
    nod = Node(outputname + fn_out, rh.LABEL_IMPORT_MOVIES)
    cli.set_outnode(nod)
    new_arg = Flag("--do_movies","is_multiframe", True )
    cli.args.append(new_arg)

    fn_out = "micrographs.star"
    nod = Node(outputname + fn_out, rh.LABEL_IMPORT_MICS)
    new_arg = Flag("--do_micrographs","is_multiframe",  False)
    cli.set_outnode(nod)
    cli.args.append(new_arg)

    optics_group = get_str("optics_group_name")
    if not optics_group:
        error_message = "ERROR: please specify an optics group name."
        return "", "", error_message
    
    new_arg = Param("--optics_group_name", "optics_group_name")
    new_arg.assertion(rh.REQUIRED_OPTICS_GROUP)
    cli.args.append(new_arg)
        
    fn_mtf = get_str("fn_mtf")
    # if len(fn_mtf) > 0:
    new_arg = Param("--optics_group_mtf","fn_mtf", "is_field_not_empty")
    cli.args.append(new_arg) 

    new_arg = Param("--angpix","angpix")
    cli.args.append(new_arg) 
    new_arg = Param("--kV","kV")
    cli.args.append(new_arg) 
    new_arg = Param("--Cs", "Cs")
    cli.args.append(new_arg) 
    new_arg = Param("--Q0", "Q0")
    cli.args.append(new_arg) 
    new_arg = Param("--beamtilt_x","beamtilt_x")
    cli.args.append(new_arg) 
    new_arg = Param("--beamtilt_y","beamtilt_y")
    cli.args.append(new_arg) 

    # Generate STAR tables
    outdata_star = "data_outdata\\nloop_\\n_rlnOutputNodeName\\n_rlnOutputNodeLabel\\n"
    for node in outputNodes:
        outdata_star += f"{node.filename} {node.label}\\n"
        
    commands_star = "data_commands\\nloop_\\n_rlnCommand\\n"
    for cmd in commands:
        commands_star += f"{cmd}\\n"
        
    return cli


def getCommandsImportJobOther(outputname, job_counter):
    commands = []
    outputNodes = []
    error_message = ""
    
    # Helper to get boolean from joboption
    def get_bool(key):
        if key not in joboptions: return False
        val = joboptions[key].value
        return str(val).lower() == "true" or val is True

    # Helper to get string
    def get_str(key):
        if key not in joboptions: return ""
        return str(joboptions[key].value)

    command = "relion_import"
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
        outputNodes.append(Node(outputname + fn_out, rh.LABEL_IMPORT_COORDS))
        command += " --do_coordinates "
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
        
        outputNodes.append(Node(outputname + fn_out, mynodetype))
        
        if mynodetype == rh.LABEL_HALFMAP_CPIPE or mynodetype == rh.LABEL_IMPORT_HALFMAP:
            fn_inb = os.path.basename(fn_in)
            if "half1" in fn_inb:
                fn_inb = fn_inb.replace("half1", "half2")
            elif "half2" in fn_inb:
                fn_inb = fn_inb.replace("half2", "half1")
            
            outputNodes.append(Node(outputname + fn_inb, mynodetype))
            command += " --do_halfmaps"
        
        elif mynodetype == rh.LABEL_PARTS_CPIPE or mynodetype == rh.LABEL_IMPORT_PARTS:
                command += " --do_particles"
                optics_group = get_str("optics_group_particles")
                if optics_group:
                    command += ' --optics_group_name "' + optics_group + '"'

    commands.append(command)

    # Generate STAR tables
    outdata_star = "data_outdata\\nloop_\\n_rlnOutputNodeName\\n_rlnOutputNodeLabel\\n"
    for node in outputNodes:
        outdata_star += f"{node.filename} {node.label}\\n"
        
    commands_star = "data_commands\\nloop_\\n_rlnCommand\\n"
    for cmd in commands:
        commands_star += f"{cmd}\\n"
        
    return outdata_star, commands_star, error_message
    
    
# Generate the correct commands
def getCommandsImportMovieJob(joboptions, do_makedir, job_counter):

    commands.clear()
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
    command.output( "movies.star","LABEL_IMPORT_MOVIES")
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
def getCommandsImportMicroGraphJob(joboptions, do_makedir, job_counter):

    commands.clear()
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
    command.output("fn_out", "LABEL_IMPORT_MICS")
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
def getCommandsImportOtherJob(joboptions, do_makedir, job_counter):

    commands.clear()
    initialisePipeline(outputname, job_counter)

    command = rc.JobCommand( "relion_import.other")

    fn_in = joboptions["fn_in_other"]
    node_type = joboptions["node_type"]
    if node_type == "Particle coordinates (*.box, *_pick.star)":
        # Make a suffix file, which contains the actual suffix as a suffix
        # Get the coordinate-file suffix
        fn_out = "coords_suffix" + fn_in.afterLastOf("*")
        Node node(outputname + fn_out, LABEL_IMPORT_COORDS)
        outputNodes.push_back(node)
        command.add("param", "--do_coordinates")
    else:
        fn_out = "/" + fn_in
        fn_out = fn_out.afterLastOf("/")

        std::string mynodetype
        if node_type == "Particles STAR file (.star)":
            mynodetype = LABEL_IMPORT_PARTS
        elif node_type == "Multiple (2D or 3D) references (.star or .mrcs)":
            mynodetype = LABEL_IMPORT_2DIMG
        elif node_type == "3D reference (.mrc)":
            mynodetype = LABEL_IMPORT_MAP
        elif node_type == "3D mask (.mrc)":
            mynodetype = LABEL_IMPORT_MASK
        elif node_type == "Micrographs STAR file (.star)":
            mynodetype = LABEL_IMPORT_MICS
        elif node_type == "Unfiltered half-map (unfil.mrc)":
            mynodetype = LABEL_IMPORT_HALFMAP
        else:
            error_message = "Unrecognized menu option for node_type = " + node_type
            return False


        Node node(outputname + fn_out, mynodetype)
        outputNodes.push_back(node)

        # Also get the other half-map
        if mynodetype == LABEL_HALFMAP_CPIPE::
            FileName fn_inb = "/" + fn_in
            size_t pos = fn_inb.find("half1")
            if pos != std::string::npos:
                fn_inb.replace(pos, 5, "half2")
            else:
                pos = fn_inb.find("half2")
                if pos != std::string::npos:
                    fn_inb.replace(pos, 5, "half1")
                
            fn_inb = fn_inb.afterLastOf("/")
            Node node2(outputname + fn_inb, mynodetype)
            outputNodes.push_back(node2)
            command.add("param", "--do_halfmaps")
        
        elif mynodetype == LABEL_PARTS_CPIPE:
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
    


def getCommands():

    bool result = false
    commands = None
    final_command = None
    do_makedir = None
    job_counter = None
    error_message = None
    if (type == PROC_IMPORT):
        dirname = rh.proc_type2dirname(rh.PROC_IMPORT)
        getCommandsImportJobRaw(f'{dirname}/job{counter}/')
        getCommandsImportJobOther(f'{dirname}/job{counter}/')
        result = getCommandsImportJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_MOTIONCORR):
        result = getCommandsMotioncorrJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_CTFFIND):
        result = getCommandsCtffindJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_MANUALPICK):
        result = getCommandsManualpickJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_AUTOPICK):
        result = getCommandsAutopickJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_EXTRACT):
        result = getCommandsExtractJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_CLASSSELECT):
        result = getCommandsSelectJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_2DCLASS):
        result = getCommandsClass2DJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_INIMODEL):
        result = getCommandsInimodelJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_3DCLASS):
        result = getCommandsClass3DJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_3DAUTO):
        result = getCommandsAutorefineJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_MULTIBODY):
        result = getCommandsMultiBodyJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_MASKCREATE):
        result = getCommandsMaskcreateJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_JOINSTAR):
        result = getCommandsJoinstarJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_SUBTRACT):
        result = getCommandsSubtractJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_POST):
        result = getCommandsPostprocessJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_RESMAP):
        result = getCommandsLocalresJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_MOTIONREFINE):
        result = getCommandsMotionrefineJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_CTFREFINE):
        result = getCommandsCtfrefineJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_DYNAMIGHT):
        result = getCommandsDynaMightJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    elif (type == PROC_MODELANGELO):
        result = getCommandsModelAngeloJob(outputname, commands, final_command, do_makedir, job_counter, error_message)
    }



    return result
}
