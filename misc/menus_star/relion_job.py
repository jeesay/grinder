bool RelionJob::containsLabel(std::string _label, std::string &option)
{
    for (std::map<std::string,JobOption>::iterator it=joboptions.begin(); it!=joboptions.end(); ++it)
    {
        if ((it->second).label == _label)
        {
            option = it->first;
            return true;
        }
    }
    return false;
}

def setOption(std::string setOptionLine):
    std::size_t equalsigns = setOptionLine.find("==");
    if (equalsigns == std::string::npos)
        REPORT_ERROR(" ERROR: no '==' entry on JobOptionLine: " + setOptionLine);

    std::string label, value, option;
    label = setOptionLine.substr(0, equalsigns - 1);
    value = setOptionLine.substr(equalsigns + 3, setOptionLine.length() - equalsigns - 3);

    if (joboptions.find(label) != joboptions.end()):
        joboptions[label].setString(value);

    elif (containsLabel(label, option)):
        joboptions[option].setString(value);

    else:
        REPORT_ERROR(" ERROR: Job does not contain label: " + label);



bool RelionJob::read(std::string fn, bool &_is_continue, bool do_initialise):
    # If fn is empty, use the hidden name
    FileName myfilename = (fn=="") ? hidden_name : fn;
    bool have_read = false;

    # For backwards compatibility
    if (!exists(myfilename + "job.star") && exists(myfilename + "run.job")):
        std::ifstream fh;
        fh.open((myfilename+"run.job").c_str(), std::ios_base::in);
        if (fh.fail())
        {
            REPORT_ERROR("ERROR reading file: " + myfilename + "run.job");
    
        else
        {
            std::string line;

            # Get job type from first line
            getline(fh, line, '\n');
            size_t idx = line.find("==");
            idx++;

            type = (int)textToFloat((line.substr(idx+1,line.length()-idx)).c_str());

            # Get is_continue from second line
            getline(fh, line, '\n');
            if (line.rfind("is_continue == true") == 0)
                is_continue = true;
            else
                is_continue = false;
            _is_continue = is_continue;

            if (do_initialise)
                initialise(type);

            # Read in all the stored options
            bool read_all = true;
            for (std::map<std::string,JobOption>::iterator it=joboptions.begin(); it!=joboptions.end(); ++it)
            {
                if (!(it->second).readValue(fh))
                    read_all = false;
        
            have_read = true;
    

        fh.close();


    if (!have_read):
        # Read from STAR
        MetaDataTable MDhead;
        MetaDataTable MDvals;

        FileName fn_star = myfilename;
        if (fn_star.getExtension() != "star" || !exists(fn_star)) # full name was given
        {
            fn_star += "job.star"; # "Refine3D/job123" OR ".gui_auto3d"
            if (!exists(fn_star))
                return false;
    

        MDhead.read(fn_star, "job");
        if (MDhead.containsLabel(EMDL_JOB_TYPE_LABEL))
        {
            MDhead.getValue(EMDL_JOB_TYPE_LABEL, label);
            type = get_proc_type(label);
    
        else
        {
            # backwards compatibility with 3.0
            MDhead.getValue(EMDL_JOB_TYPE, type);
    

        MDhead.getValue(EMDL_JOB_IS_CONTINUE, is_continue);
        _is_continue = is_continue;
        MDhead.getValue(EMDL_JOB_IS_TOMO, is_tomo);
        if (do_initialise)
            initialise(type);

        MDvals.read(fn_star, "joboptions_values");
        std::string label, value;
        FOR_ALL_OBJECTS_IN_METADATA_TABLE(MDvals)
        {
            MDvals.getValue(EMDL_JOBOPTION_VARIABLE, label);
            MDvals.getValue(EMDL_JOBOPTION_VALUE, value);
            if (joboptions.find(label) == joboptions.end())
            {
                std::cerr << "WARNING: cannot find " << label << " in the defined joboptions. Ignoring it ..." <<std::endl;
        
            else
            {
                joboptions[label].value = value;
        
    
        have_read = true;


    if (have_read):
        # Just check that went OK
        if (type != PROC_IMPORT &&
            type != PROC_MOTIONCORR &&
            type != PROC_CTFFIND &&
            type != PROC_MANUALPICK &&
            type != PROC_AUTOPICK &&
            type != PROC_EXTRACT &&
            type != PROC_CLASSSELECT &&
            type != PROC_2DCLASS &&
            type != PROC_3DCLASS &&
            type != PROC_3DAUTO &&
            type != PROC_MULTIBODY &&
            type != PROC_MASKCREATE &&
            type != PROC_JOINSTAR &&
            type != PROC_SUBTRACT &&
            type != PROC_POST &&
            type != PROC_RESMAP &&
            type != PROC_INIMODEL &&
            type != PROC_MOTIONREFINE &&
            type != PROC_CTFREFINE &&
            type != PROC_MODELANGELO &&
            type != PROC_DYNAMIGHT &&
            type != PROC_TOMO_IMPORT &&
            type != PROC_TOMO_SUBTOMO &&
            type != PROC_TOMO_CTFREFINE &&
            type != PROC_TOMO_ALIGN &&
            type != PROC_TOMO_ALIGN_TILTSERIES &&
            type != PROC_TOMO_RECONSTRUCT_TOMOGRAM &&
            type != PROC_TOMO_DENOISE_TOMOGRAM &&
            type != PROC_TOMO_PICK_TOMOGRAM &&
            type != PROC_TOMO_RECONSTRUCT &&
            type != PROC_TOMO_EXCLUDE_TILT_IMAGES &&
            type != PROC_EXTERNAL)
            return false;

        return true;

    else:
        return false;

}

def write(std::string fn):
    # If fn is empty, use the hidden name
    FileName myfilename = (fn=="") ? hidden_name : fn;

    FileName fn_star = myfilename;
    if (fn_star.getExtension() != "star") # full name was given:
        fn_star += "job.star"; # "Refine3D/job123" OR ".gui_auto3d"


    std::ofstream fh;
    fh.open((fn_star).c_str(), std::ios::out);
    if (!fh)
        REPORT_ERROR("ERROR: Cannot write to file: " + fn_star);

    MetaDataTable MDhead;
    MetaDataTable MDvals, MDopts;

    MDhead.setIsList(true);
    MDhead.addObject();
    # as of 3.1-beta do not write integer into the STAR files anymore....
    # MDhead.setValue(EMDL_JOB_TYPE, type);
    MDhead.setValue(EMDL_JOB_TYPE_LABEL, label);
    MDhead.setValue(EMDL_JOB_IS_CONTINUE, is_continue);
    MDhead.setValue(EMDL_JOB_IS_TOMO, is_tomo);
    # TODO: add name for output directories!!! make a std:;map between type and name for all options!
    #MDhead.setValue(EMDL_JOB_TYPE_NAME, type);
    MDhead.setName("job");
    MDhead.write(fh);

    # Now make a table with all the values
    for (std::map<std::string,JobOption>::iterator it=joboptions.begin(); it!=joboptions.end(); ++it):
        (it->second).writeToMetaDataTable(MDvals);

    MDvals.setName("joboptions_values");
    MDvals.write(fh);

    fh.close();
}

bool RelionJob::saveJobSubmissionScript(std::string newfilename, std::string outputname, std::vector<std::string> commands, std::string &error_message):
    # Open the standard job submission file
    FileName fn_qsub = joboptions["qsubscript"].getString();


    std::ofstream fo;
    std::ifstream fh;
    fh.open(fn_qsub.c_str(), std::ios_base::in);
    fo.open(newfilename.c_str(), std::ios::out);
    if (fh.fail()):
        error_message = "Error reading template submission script in: " + fn_qsub;
        return false;

    elif (fo.fail()):
        error_message = "Error writing to job submission script in: " + newfilename;
        return false;

    else:
        int nmpi = (joboptions.find("nr_mpi") != joboptions.end()) ? joboptions["nr_mpi"].getNumber(error_message) : 1;
        if (error_message != "") return false;

        int nthr = (joboptions.find("nr_threads") != joboptions.end()) ? joboptions["nr_threads"].getNumber(error_message) : 1;
        if (error_message != "") return false;

        int ncores = nmpi * nthr;
        int ndedi = joboptions["min_dedicated"].getNumber(error_message);
        if (error_message != "") return false;

        float fnodes = (float)ncores / (float)ndedi;
        int nnodes = CEIL(fnodes);
        /*
        if (fmod(fnodes, 1) > 0)
        {
            std:: cout << std::endl;
            std::cout << " Warning! You're using " << nmpi << " MPI processes with " << nthr << " threads each (i.e. " << ncores << " cores), while asking for " << nnodes << " nodes with " << ndedi << " cores." << std::endl;
            std::cout << " It is more efficient to make the number of cores (i.e. mpi*threads) a multiple of the minimum number of dedicated cores per node " << std::endl;
    
        */

        fh.clear(); # reset eof if happened...
        fh.seekg(0, std::ios::beg);
        std::string line;
        std::map<std::string, std::string> replacing;
        replacing["XXXmpinodesXXX"] = floatToString(nmpi);
        replacing["XXXthreadsXXX"] = floatToString(nthr);
        replacing["XXXcoresXXX"] = floatToString(ncores);
        replacing["XXXdedicatedXXX"] = floatToString(ndedi);
        replacing["XXXnodesXXX"] = floatToString(nnodes);
        replacing["XXXnameXXX"] = outputname;
        replacing["XXXerrfileXXX"] = outputname + "run.err";
        replacing["XXXoutfileXXX"] = outputname + "run.out";
        replacing["XXXqueueXXX"] = joboptions["queuename"].getString();
        char *extra_count_text = getenv("RELION_QSUB_EXTRA_COUNT");
        const char extra_count_val = (extra_count_text ? atoi(extra_count_text) : 2);
        for (int i=1; i<=extra_count_val; i++)
        {
            std::stringstream out;
            out<<i;
            const std::string i_str=out.str();
            if (joboptions.find(std::string("qsub_extra")+i_str) != joboptions.end())
            {
                replacing[std::string("XXXextra")+i_str+"XXX"] = joboptions[std::string("qsub_extra")+i_str].getString();
        
    

        while (getline(fh, line, '\n'))
        {
            # Replace all entries in the replacing map
            for (std::map<std::string,std::string>::iterator it=replacing.begin(); it!=replacing.end(); ++it)
            {
                std::string from = it->first;
                std::string to = it->second;

                # Replace all instances of the string on the line
                size_t start_pos = 0;
                while((start_pos = line.find(from, start_pos)) != std::string::npos)
                {
                    line.replace(start_pos, from.length(), to);
                    start_pos += to.length();
            
        

            if (line.find("XXXcommandXXX") == std::string::npos)
            {
                fo << line << std::endl;;
        
            else
            {
                # Append the commands
                std::string ori_line = line;
                for (int icom = 0; icom < commands.size(); icom++)
                {
                    # For multiple relion mpi commands: add multiple lines from the XXXcommandXXX template
                    if ((commands[icom]).find("relion_") != std::string::npos &&
                            ((commands[icom]).find("_mpi`") != std::string::npos || nmpi==1) ) # if there are no MPI programs, then still use XXXcommandXXX once
                    {
                        std::string from = "XXXcommandXXX";
                        std::string to = commands[icom];
                        line.replace(line.find(from), from.length(), to);
                        fo << line << std::endl;
                        line = ori_line;
                
                    else
                    {
                        # Just add the sequential command
                        fo << commands[icom] << std::endl;
                
            
        
    

        fo << std::endl;

        fo.close();
        fh.close();


    return true;
}

def initialisePipeline(std::string &outputname, int job_counter):
    outputNodes.clear();
    inputNodes.clear();

    FileName dirname = proc_type2dirname.at(type);
    # TODO: insert "relion." prefix to dirname when using the ccpem-pipeliner...

    if (outputname == "") # for continue jobs, use the same outputname:
        if (job_counter < 1000)
            outputname = dirname + "/job" + integerToString(job_counter, 3) + "/";
        else
            outputname = dirname + "/job" + integerToString(job_counter) + "/";


    # This is the default label, deeper levels can be added for specific jobs
    label = get_proc_label(type);
    outputName = outputname;
}

bool RelionJob::prepareFinalCommand(std::string &outputname, std::vector<std::string> &commands,
                                    std::string &final_command, bool do_makedir, std::string &error_message, bool do_dash_for_python):
    int nr_mpi;

    # Create output directory if the outname contains a "/"
    if (do_makedir):
        int last_slash = outputname.rfind("/");
        if (last_slash < outputname.size())
        {
            mktree(outputname.substr(0, last_slash));
    


    # Add the --pipeline_control argument to all relion_ programs
    for (int icom = 0; icom < commands.size(); icom++):
        if ((commands[icom]).find("relion_") != std::string::npos)
        {
            if (do_dash_for_python)
                commands[icom] += " --pipeline-control " + outputname;
            else
                commands[icom] += " --pipeline_control " + outputname;
    


    # Prepare full mpi commands or save jobsubmission script to disc
    if (joboptions["do_queue"].getBoolean() && do_makedir):
        # Make the submission script and write it to disc
        std::string output_script = outputname + "run_submit.script";

        if (!saveJobSubmissionScript(output_script, outputname, commands, error_message))
            return false;
        final_command = joboptions["qsub"].getString() + " " + output_script + " &";

    else:
        # If there are multiple commands, then join them all on a single line (final_command)
        # Also add mpirun in front of those commands that have relion_ and _mpi` in it (if no submission via the queue is done)
        std::string one_command;
        final_command = "";
        for (size_t icom = 0; icom < commands.size(); icom++)
        {
            # Is this a relion mpi program?
            nr_mpi = (joboptions.find("nr_mpi") != joboptions.end()) ? joboptions["nr_mpi"].getNumber(error_message) : 1;
            if (error_message != "") return false;

            if (nr_mpi > 1 &&
                    (commands[icom]).find("_mpi`") != std::string::npos &&
                    (commands[icom]).find("relion_") != std::string::npos)
            {

                const char *default_mpirun = getenv("RELION_MPIRUN");
                if (default_mpirun == NULL)
                {
                    default_mpirun = DEFAULTMPIRUN;
            
                one_command = std::string(default_mpirun) + " -n " + floatToString(nr_mpi) + " " + commands[icom] ;
        
            else
                one_command = commands[icom];

            # Save stdout and stderr to a .out and .err files
            # But only when a re-direct '>' is NOT already present on the command line!
            if (std::string::npos == commands[icom].find(">"))
                one_command += " >> " + outputname + "run.out 2>> " + outputname + "run.err";
            final_command += one_command;
            if (icom == commands.size() - 1)
                final_command += " & "; # end by putting composite job in the background
            else
                final_command += " && "; # execute one command after the other...
    


    char * my_warn = getenv("RELION_ERROR_LOCAL_MPI");
    int my_nr_warn = (my_warn == NULL) ? DEFAULTWARNINGLOCALMPI : textToInteger(my_warn);

    if (nr_mpi > my_nr_warn && !joboptions["do_queue"].getBoolean()):
        error_message = "You're submitting a local job with " + floatToString(nr_mpi) + " parallel MPI processes. That's more than allowed by the RELION_ERROR_LOCAL_MPI environment variable.";
        return false;

    else:
        return true;

}

# Initialise
def initialise(int _job_type):
    type = _job_type;

    bool has_mpi, has_thread;
    if (type == PROC_IMPORT):
        has_mpi = has_thread = false;
        initialiseImportJob();

    elif (type == PROC_MOTIONCORR):
        has_mpi = has_thread = true;
        initialiseMotioncorrJob();

    elif (type == PROC_CTFFIND):
        has_mpi = true;
        has_thread = false;
        initialiseCtffindJob();

    elif (type == PROC_MANUALPICK):
        has_mpi = has_thread = false;
        initialiseManualpickJob();

    elif (type == PROC_AUTOPICK):
        has_mpi = true;
        has_thread = false;
        initialiseAutopickJob();

    elif (type == PROC_EXTRACT):
        has_mpi = true;
        has_thread = false;
        initialiseExtractJob();

    elif (type == PROC_CLASSSELECT):
        has_mpi = has_thread = false;
        initialiseSelectJob();

    elif (type == PROC_2DCLASS):
        has_mpi = has_thread = true;
        initialiseClass2DJob();

    elif (type == PROC_INIMODEL):
        has_mpi = has_thread = true;
        initialiseInimodelJob();

    elif (type == PROC_3DCLASS):
        has_mpi = has_thread = true;
        initialiseClass3DJob();

    elif (type == PROC_3DAUTO):
        has_mpi = has_thread = true;
        initialiseAutorefineJob();

    elif (type == PROC_MULTIBODY):
        has_mpi = has_thread = true;
        initialiseMultiBodyJob();

    elif (type == PROC_MASKCREATE):
        has_mpi = false;
        has_thread = true;
        initialiseMaskcreateJob();

    elif (type == PROC_JOINSTAR):
        has_mpi = has_thread = false;
        initialiseJoinstarJob();

    elif (type == PROC_SUBTRACT):
        has_mpi = true;
        has_thread = false;
        initialiseSubtractJob();

    elif (type == PROC_POST):
        has_mpi = has_thread = false;
        initialisePostprocessJob();

    elif (type == PROC_RESMAP):
        has_mpi = true;
        has_thread = false;
        initialiseLocalresJob();

    elif (type == PROC_MOTIONREFINE):
        has_mpi = has_thread = true;
        initialiseMotionrefineJob();

    elif (type == PROC_CTFREFINE):
        has_mpi = has_thread = true;
        initialiseCtfrefineJob();

    elif (type == PROC_DYNAMIGHT):
        has_mpi = false;
        has_thread = true;
        initialiseDynaMightJob();

    elif (type == PROC_MODELANGELO):
        has_mpi = has_thread = false;
        initialiseModelAngeloJob();

    elif (type == PROC_TOMO_IMPORT):
        has_mpi = has_thread = false;
        initialiseTomoImportJob();

    elif (type == PROC_TOMO_EXCLUDE_TILT_IMAGES):
        has_mpi = has_thread = false;
        initialiseTomoExcludeTiltImagesJob();

    elif (type == PROC_TOMO_ALIGN_TILTSERIES):
        has_mpi = true;
        has_thread = false;
        initialiseTomoAlignTiltSeriesJob();

    elif (type == PROC_TOMO_RECONSTRUCT_TOMOGRAM):
        has_mpi = has_thread = true;
        initialiseTomoReconstructTomogramsJob();

    elif (type == PROC_TOMO_DENOISE_TOMOGRAM):
        has_mpi = has_thread = false;
        initialiseTomoDenoiseTomogramsJob();

    elif (type == PROC_TOMO_PICK_TOMOGRAM):
        has_mpi = has_thread = false;
        initialiseTomoPickTomogramsJob();

    elif (type == PROC_TOMO_EXCLUDE_TILT_IMAGES):
        has_mpi = has_thread = false;
        initialiseTomoExcludeTiltImagesJob();

    elif (type == PROC_TOMO_SUBTOMO):
        has_mpi = has_thread = true;
        initialiseTomoSubtomoJob();

    elif (type == PROC_TOMO_CTFREFINE):
        has_mpi = has_thread = true;
        initialiseTomoCtfRefineJob();

    elif (type == PROC_TOMO_ALIGN):
        has_mpi = has_thread = true;
        initialiseTomoAlignJob();

    elif (type == PROC_TOMO_RECONSTRUCT):
        has_mpi = has_thread = true;
        initialiseTomoReconPartJob();

    elif (type == PROC_EXTERNAL):
        has_mpi = false;
        has_thread = true;
        initialiseExternalJob();

    else
        REPORT_ERROR("ERROR: unrecognised job-type");

    # Check for environment variable RELION_MPI_MAX and RELION_QSUB_NRMPI
    const char *mpi_max_input = getenv("RELION_MPI_MAX");
    int mpi_max = (mpi_max_input == NULL) ? DEFAULTMPIMAX : textToInteger(mpi_max_input);
    char * qsub_nrmpi_text = getenv("RELION_QSUB_NRMPI");
    const char qsub_nrmpi_val = (qsub_nrmpi_text ? atoi(qsub_nrmpi_text) : DEFAULTNRMPI);
    if (has_mpi):
        joboptions["nr_mpi"] = JobOption("Number of MPI procs:", qsub_nrmpi_val , 1, mpi_max, 1, "Number of MPI nodes to use in parallel. When set to 1, MPI will not be used. The maximum can be set through the environment variable RELION_MPI_MAX.");


    const char *thread_max_input = getenv("RELION_THREAD_MAX");
    int thread_max = (thread_max_input == NULL) ? DEFAULTTHREADMAX : textToInteger(thread_max_input);
    char * qsub_nrthr_text = getenv("RELION_QSUB_NRTHREADS");
    const char qsub_nrthreads_val = (qsub_nrthr_text ? atoi(qsub_nrthr_text) : DEFAULTNRTHREADS);
    if (has_thread):
        joboptions["nr_threads"] = JobOption("Number of threads:", qsub_nrthreads_val, 1, thread_max, 1, "Number of shared-memory (POSIX) threads to use in parallel. \
When set to 1, no multi-threading will be used. The maximum can be set through the environment variable RELION_THREAD_MAX.");


    const char * use_queue_input = getenv("RELION_QUEUE_USE");
    bool use_queue = (use_queue_input == NULL) ? DEFAULTQUEUEUSE : textToBool(use_queue_input);
    joboptions["do_queue"] = JobOption("Submit to queue?", use_queue, "If set to Yes, the job will be submit to a queue, otherwise \
the job will be executed locally. Note that only MPI jobs may be sent to a queue. The default can be set through the environment variable RELION_QUEUE_USE.");

    # Check for environment variable RELION_QUEUE_NAME
    const char * default_queue = getenv("RELION_QUEUE_NAME");
    if (default_queue==NULL):
        default_queue = DEFAULTQUEUENAME;


    # Need the std::string(), as otherwise it will be overloaded and passed as a boolean....
    joboptions["queuename"] = JobOption("Queue name: ", std::string(default_queue), "Name of the queue to which to submit the job. The default name can be set through the environment variable RELION_QUEUE_NAME.");

    # Check for environment variable RELION_QSUB_COMMAND
    const char * default_command = getenv("RELION_QSUB_COMMAND");
    if (default_command==NULL):
        default_command = DEFAULTQSUBCOMMAND;


    joboptions["qsub"] = JobOption("Queue submit command:", std::string(default_command), "Name of the command used to submit scripts to the queue, e.g. qsub or bsub.\n\n\
Note that the person who installed RELION should have made a custom script for your cluster/queue setup. Check this is the case \
(or create your own script following the RELION Wiki) if you have trouble submitting jobs. The default command can be set through the environment variable RELION_QSUB_COMMAND.");

    # additional options that may be set through environment variables RELION_QSUB_EXTRAi and RELION_QSUB_EXTRAi (for more flexibility)
    char * extra_count_text = getenv("RELION_QSUB_EXTRA_COUNT");
    const char extra_count_val = (extra_count_text ? atoi(extra_count_text) : 2);
    for (int i=1; i<=extra_count_val; i++):
        std::stringstream out;
        out<<i;
        const std::string i_str=out.str();
        char * extra_text = getenv((std::string("RELION_QSUB_EXTRA")+i_str).c_str());
        if (extra_text != NULL)
        {
            const std::string query_default=std::string("RELION_QSUB_EXTRA")+i_str+"_DEFAULT";
            char *extra_default = getenv(query_default.c_str());
            char emptychar[] = "";
            if (extra_default == NULL)
            {
                extra_default=emptychar;
        
            const std::string query_help=std::string("RELION_QSUB_EXTRA")+i_str+"_HELP";
            char *extra_help = getenv(query_help.c_str());
            std::string txt;
            if (extra_help == NULL)
            {
                txt = std::string("Extra option to pass to the qsub template script. Any occurrences of XXXextra")+i_str+"XXX will be changed by this value.";
        
            else
            {
                txt=std::string(extra_help);
        
            joboptions[std::string("qsub_extra")+i_str] = JobOption(std::string(extra_text), std::string(extra_default), txt.c_str());
    


    # Check for environment variable RELION_QSUB_TEMPLATE
    char * default_location = getenv("RELION_QSUB_TEMPLATE");
    char default_qsub[] = DEFAULTQSUBLOCATION;
    if (default_location == NULL):
        default_location = default_qsub;

    joboptions["qsubscript"] = JobOption("Standard submission script:", std::string(default_location), "Script Files (*.{csh,sh,bash,script})", ".",
"The template for your standard queue job submission script. \
Its default location may be changed by setting the environment variable RELION_QSUB_TEMPLATE. \
In the template script a number of variables will be replaced: \n \
XXXcommandXXX = relion command + arguments; \n \
XXXqueueXXX = The queue name; \n \
XXXmpinodesXXX = The number of MPI nodes; \n \
XXXthreadsXXX = The number of threads; \n \
XXXcoresXXX = XXXmpinodesXXX * XXXthreadsXXX; \n \
XXXdedicatedXXX = The minimum number of dedicated cores on each node; \n \
XXXnodesXXX = The number of requested nodes = CEIL(XXXcoresXXX / XXXdedicatedXXX); \n \
If these options are not enough for your standard jobs, you may define a user-specified number of extra variables: XXXextra1XXX, XXXextra2XXX, etc. \
The number of extra variables is controlled through the environment variable RELION_QSUB_EXTRA_COUNT. \
Their help text is set by the environment variables RELION_QSUB_EXTRA1, RELION_QSUB_EXTRA2, etc \
For example, setenv RELION_QSUB_EXTRA_COUNT 1, together with setenv RELION_QSUB_EXTRA1 \"Max number of hours in queue\" will result in an additional (text) ein the GUI \
Any variables XXXextra1XXX in the template script will be replaced by the corresponding value.\
Likewise, default values for the extra entries can be set through environment variables RELION_QSUB_EXTRA1_DEFAULT, RELION_QSUB_EXTRA2_DEFAULT, etc. \
But note that (unlike all other entries in the GUI) the extra values are not remembered from one run to the other.");

    # Check for environment variable RELION_QSUB_TEMPLATE
    char * my_minimum_dedicated = getenv ("RELION_MINIMUM_DEDICATED");
    int minimum_nr_dedicated = (my_minimum_dedicated == NULL) ? DEFAULTMININIMUMDEDICATED : textToInteger(my_minimum_dedicated);
    joboptions["min_dedicated"] = JobOption("Minimum dedicated cores per node:", minimum_nr_dedicated, 1, 64, 1, "Minimum number of dedicated cores that need to be requested on each node. This is useful to force the queue to fill up entire nodes of a given size. The default can be set through the environment variable RELION_MINIMUM_DEDICATED.");

    # Need the std::string(), as otherwise it will be overloaded and passed as a boolean....
    joboptions["other_args"] = JobOption("Additional arguments:", std::string(""), "In this box command-line arguments may be provided that are not generated by the GUI. \
This may be useful for testing developmental options and/or expert use of the program. \
To print a list of possible options, run the corresponding program from the command line without any arguments.");

    # Set the variable name in all joboptions

    std::map<std::string, JobOption>::iterator it;
    for ( it = joboptions.begin(); it != joboptions.end(); it++ ):
        (it->second).variable = it->first;

}

bool RelionJob::getCommands(std::string &outputname, std::vector<std::string> &commands,
        std::string &final_command, bool do_makedir, int job_counter, std::string &error_message):
    bool result = false;

    if (type == PROC_IMPORT):
        result = getCommandsImportJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_MOTIONCORR):
        result = getCommandsMotioncorrJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_CTFFIND):
        result = getCommandsCtffindJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_MANUALPICK):
        result = getCommandsManualpickJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_AUTOPICK):
        result = getCommandsAutopickJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_EXTRACT):
        result = getCommandsExtractJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_CLASSSELECT):
        result = getCommandsSelectJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_2DCLASS):
        result = getCommandsClass2DJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_INIMODEL):
        result = getCommandsInimodelJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_3DCLASS):
        result = getCommandsClass3DJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_3DAUTO):
        result = getCommandsAutorefineJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_MULTIBODY):
        result = getCommandsMultiBodyJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_MASKCREATE):
        result = getCommandsMaskcreateJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_JOINSTAR):
        result = getCommandsJoinstarJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_SUBTRACT):
        result = getCommandsSubtractJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_POST):
        result = getCommandsPostprocessJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_RESMAP):
        result = getCommandsLocalresJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_MOTIONREFINE):
        result = getCommandsMotionrefineJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_CTFREFINE):
        result = getCommandsCtfrefineJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_DYNAMIGHT):
        result = getCommandsDynaMightJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_MODELANGELO):
        result = getCommandsModelAngeloJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_TOMO_IMPORT):
        result = getCommandsTomoImportJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_TOMO_SUBTOMO):
        result = getCommandsTomoSubtomoJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_TOMO_CTFREFINE):
        result = getCommandsTomoCtfRefineJob(outputname, commands, final_command, do_makedir, job_counter,
                                             error_message);

    elif (type == PROC_TOMO_ALIGN):
        result = getCommandsTomoAlignJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_TOMO_ALIGN_TILTSERIES):
        result = getCommandsTomoAlignTiltSeriesJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_TOMO_EXCLUDE_TILT_IMAGES):
        result = getCommandsTomoExcludeTiltImagesJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_TOMO_RECONSTRUCT_TOMOGRAM):
        result = getCommandsTomoReconstructTomogramsJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_TOMO_DENOISE_TOMOGRAM):
        result = getCommandsTomoDenoiseTomogramsJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_TOMO_PICK_TOMOGRAM):
        result = getCommandsTomoPickTomogramsJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_TOMO_RECONSTRUCT):
        result = getCommandsTomoReconPartJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    elif (type == PROC_EXTERNAL):
        result = getCommandsExternalJob(outputname, commands, final_command, do_makedir, job_counter, error_message);

    else:
        REPORT_ERROR("ERROR: unrecognised job-type: type = " + integerToString(type));


    return result;
}


