import relion_h as rh
import relion_option as rno
import relion_spa_gui as rsg

# import relion_spa_commands as rcom
import os

# Helper to get boolean from joboption
def get_bool(key):
    if key not in joboptions: return False
    val = joboptions[key].value
    return str(val).lower() == "true" or val is True

# Helper to get string
def get_str(key):
    if key not in joboptions: return ""
    return str(joboptions[key].value)

# Initialise
def initialise(_job_type):
    type = _job_type
    opts = None
    rsg.init_joboptions()
    global has_disk, has_gpu ,has_mpi, has_thread
    
    if (type == "PROC_IMPORT_RAW_GRR"):
        has_mpi = has_thread = has_gpu = has_disk = False
        hidden_name = rsg.initialiseImportRawJob()
        opts = rsg.get_joboptions()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]
        _main.append({"id" : id, 
                        "label" : label,
                        "parent" : parent,
                        "help" : help,
                        "proc": proc_id,
                        "dirname" : proc_dirname,
                        "labelnew" : proc_label,
                        "hidden_name" : hidden_name
                        })
        # dirname = rh.proc_type2dirname(rh.PROC_IMPORT)
#        getCommandsImportJobRaw(f'{dirname}/job{counter}/')
#        getCommandsImportJobOther(f'{dirname}/job{counter}/')
    elif (type == "PROC_IMPORT_PARTICLES_GRR") :
        has_mpi = has_thread = has_gpu = has_disk = False
        hidden_name = rsg.initialiseImportParticlesJob()
        opts = rsg.get_joboptions()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]
        _main.append({"id" : id, 
                        "label" : label,
                        "parent" : parent,
                        "help" : help,
                        "proc": proc_id,
                        "dirname" : proc_dirname,
                        "labelnew" : proc_label,
                        "hidden_name" : hidden_name
                        })
    elif (type == "PROC_IMPORT_OTHER_GRR") :
        has_mpi = has_thread = has_gpu = has_disk = False
        hidden_name = rsg.initialiseImportOtherJob()
        opts = rsg.get_joboptions()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]
        _main.append({"id" : id, 
                        "label" : label,
                        "parent" : parent,
                        "help" : help,
                        "proc": proc_id,
                        "dirname" : proc_dirname,
                        "labelnew" : proc_label,
                        "hidden_name" : hidden_name
                        })

    elif (type == "PROC_MOTIONCORR_OWN_GRR") or (type == "PROC_MOTIONCORR_MC2_GRR"):
        has_mpi = has_thread = has_gpu = True
        has_disk = False
        hidden_name = rsg.initialiseMotioncorrJob()
        opts = rsg.get_joboptions()
        # print(opts)
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]
        _main.append({"id" : id, 
                        "label" : label,
                        "parent" : parent,
                        "help" : help,
                        "proc": proc_id,
                        "dirname" : proc_dirname,
                        "labelnew" : proc_label,
                        "hidden_name" : hidden_name
                        })

    elif (type == "PROC_CTFFIND"):
        has_mpi = True
        has_thread = has_gpu = has_disk = False
        hidden_name = initialiseCtffindJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]
        _main.append({"id" : id, 
                        "label" : label,
                        "parent" : parent,
                        "help" : help,
                        "proc": proc_id,
                        "dirname" : proc_dirname,
                        "labelnew" : proc_label,
                        "hidden_name" : hidden_name
                        })

    elif (type == "PROC_MANUALPICK"):
        has_mpi = has_thread = False
        initialiseManualpickJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_AUTOPICK"):
        has_mpi = True
        has_thread = has_gpu = has_disk = False
        initialiseAutopickJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_EXTRACT"):
        has_mpi = True
        has_thread = has_disk = has_gpu = False
        initialiseExtractJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_CLASSSELECT"):
        has_mpi = has_thread = False
        initialiseSelectJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_2DCLASS"):
        has_mpi = has_thread = has_disk = has_gpu = True
        initialiseClass2DJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_INIMODEL"):
        has_mpi = has_thread = has_disk = has_gpu = True
        initialiseInimodelJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_3DCLASS"):
        has_mpi = has_thread = has_disk = has_gpu = True
        initialiseClass3DJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_3DAUTO"):
        has_mpi = has_thread = has_disk = has_gpu = True
        initialiseAutorefineJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_MULTIBODY"):
        has_mpi = has_thread = has_disk = has_gpu = True
        initialiseMultiBodyJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_MASKCREATE"):
        has_mpi = False
        has_thread = True
        initialiseMaskcreateJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_JOINSTAR"):
        has_mpi = has_thread = False
        initialiseJoinstarJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_SUBTRACT"):
        has_mpi = True
        has_thread = False
        initialiseSubtractJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_POST"):
        has_mpi = has_thread = False
        initialisePostprocessJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_RESMAP"):
        has_mpi = True
        has_thread = False
        initialiseLocalresJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_MOTIONREFINE"):
        has_mpi = has_thread = True
        initialiseMotionrefineJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_CTFREFINE"):
        has_mpi = has_thread = True
        initialiseCtfrefineJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_DYNAMIGHT"):
        has_mpi = False
        has_thread = True
        initialiseDynaMightJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == "PROC_MODELANGELO"):
        has_mpi = has_thread = False
        initialiseModelAngeloJob()
        id, label, parent, help, proc_id, proc_dirname, proc_label = rh.proc_grinder_settings[type]

    elif (type == rh.PROC_TOMO_IMPORT):
        has_mpi = has_thread = False
        initialiseTomoImportJob()

    elif (type == rh.PROC_TOMO_EXCLUDE_TILT_IMAGES):
        has_mpi = has_thread = False
        initialiseTomoExcludeTiltImagesJob()

    elif (type == rh.PROC_TOMO_ALIGN_TILTSERIES):
        has_mpi = True
        has_thread = False
        initialiseTomoAlignTiltSeriesJob()

    elif (type == rh.PROC_TOMO_RECONSTRUCT_TOMOGRAM):
        has_mpi = has_thread = True
        initialiseTomoReconstructTomogramsJob()

    elif (type == rh.PROC_TOMO_DENOISE_TOMOGRAM):
        has_mpi = has_thread = False
        initialiseTomoDenoiseTomogramsJob()

    elif (type == rh.PROC_TOMO_PICK_TOMOGRAM):
        has_mpi = has_thread = False
        initialiseTomoPickTomogramsJob()

    elif (type == rh.PROC_TOMO_EXCLUDE_TILT_IMAGES):
        has_mpi = has_thread = False
        initialiseTomoExcludeTiltImagesJob()

    elif (type == rh.PROC_TOMO_SUBTOMO):
        has_mpi = has_thread = True
        initialiseTomoSubtomoJob()

    elif (type == rh.PROC_TOMO_CTFREFINE):
        has_mpi = has_thread = True
        initialiseTomoCtfRefineJob()

    elif (type == rh.PROC_TOMO_ALIGN):
        has_mpi = has_thread = True
        initialiseTomoAlignJob()

    elif (type == rh.PROC_TOMO_RECONSTRUCT):
        has_mpi = has_thread = True
        initialiseTomoReconPartJob()

    elif (type == rh.PROC_EXTERNAL):
        has_mpi = False
        has_thread = True
        initialiseExternalJob()

    else:
        print("ERROR: unrecognised job-type")

    return opts
        
def init_table(name):
  return f'#\nloop_\n{name}.id\n{name}.label\n{name}.widget\n{name}.default\n{name}.arg0\n{name}.arg1\n{name}.arg2\n{name}.help\n'

def header():
    _main = f"""
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
"""
    
def tabs():
    return """
loop_
_tabs.id
_tabs.label
_tabs.icon
_tabs.widget
_tabs.default
_tabs.parent
_tabs.help
io       'I/O'                    bi-arrow-down-up       tab ? ? ?
settings 'Settings'               bi-tools               tab ? ? ?
log      'Logs'                   bi-binoculars-fill     tab ? ? ?
result   'DataViz'                bi-eye                 tab ? ? ?
"""

# def tabs():
#     return """
# loop_
# _groups.id
# _groups.label
# _groups.icon
# _groups.widget
# _groups.default
# _groups.parent
# _groups.help
# io       'I/O'                    bi-arrow-down-up       tab ? ? ?
# settings 'Settings'               bi-tools               tab ? ? ?
# display  'Display'                bi-palette             tab ? ? ?
# compute  'Compute'                bi-cpu                 tab ? ? ?
# running  'Running'                bi-send                tab ? ? ?
# result   'DataViz'                bi-eye                 tab ? ? ?
# indata   'Input'                  bi-arrow-bar-down      fieldset ?      io       ?
# cont     'Continue Job'           bi-send-plus           fieldset hidden io       ?
# outdata  'Output and System'      bi-terminal            fieldset ?      io       ?
# general  'General'                bi-chat-right-text     fieldset ?      settings ?
# other    'Other Parameters'       bi-chat-right-dots     fieldset ?      settings ?
# disk     'Disk Access'            bi-database            fieldset ?      compute  ?    
# gpu      'Use GPU Acceleration?'  bi-gpu-card            switch   false  compute  'If set to Yes, the job will try to use GPU acceleration.'
# process  'Processes'              bi-gear-fill           fieldset ?      compute  ?
# do_queue 'Submit to queue?'       bi-box-arrow-in-right  switch   false  running  'If set to Yes, the job will be submitted to a queue, otherwise the job will be executed locally. Note that only MPI jobs may be sent to a queue. The default can be set through the environment variable RELION_QUEUE_USE.'
# command  'Check Command'          bi-terminal-plus       cli      ?      running  'RELION Command as it appears in `note.txt`'
# exec     'Execute Command'        bi-send-plus           toolbar  ?      running  'No help'
# """

def io():
    return """
#
loop_
_io.id
_io.label
_io.icon
_io.widget
_io.default
_io.help
indata   'Input'       bi-arrow-bar-down      fieldset ?      'No Help' """

def settings():
    return """
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.default
_settings.help
general  'General'      bi-chat-right-text     fieldset ?      'No Help' 
"""

def additional_args():
    return """
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
"""

def disk_access():
    return """
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
"""

def compute_gpu():
    return """
loop_
_use_gpu.id
_use_gpu.label
_use_gpu.widget
_use_gpu.default
_use_gpu.arg0
_use_gpu.arg1
_use_gpu.arg2
_use_gpu.help
gpu_ids 'Which GPUs to use:' string '' ? ? ?
;This argument is not necessary. If left empty, the job itself will try to allocate available GPU resources. You can override the default allocation by providing a list of which GPUs (0,1,2,3, etc) to use. MPI-processes are separated by ':', threads by ','. For example: '0,0:1,1:0,0:1,1'
;
#
"""

def compute_queue():
    return """
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
"""

def compute_mpi_thread():
    return """
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
"""

def compute_mpi():
    return """
loop_
_mpi.id
_mpi.label
_mpi.widget
_mpi.default
_mpi.arg0
_mpi.arg1
_mpi.arg2
_mpi.help
nr_mpi "Number of MPI procs:" range '{QSUB_NRMPI_VAL}' 1 '{RELION_MPI_MAX}' 1 "Number of MPI nodes to use in parallel. When set to 1, MPI will not be used. The maximum can be set through the environment variable RELION_MPI_MAX."
#
"""


def cont_process():
    return """
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
"""

def run_buttons():
    return """
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
"""

########################## M A I N ##########################
#


if __name__ == "__main__":
    is_tomo = False
    has_mpi = False 
    has_thread =  False
    has_gpu = False
    has_disk = False
    header()

    # tools = rno.JobOptionTool(rh.proc_grinder_settings["PROC_IMPORT_RAW_GRR"])
    # print(tools.to_star())

    # print(rh.proc_grinder_settings["PROC_IMPORT_RAW_GRR"][0])

    dirs = {"00_home" : [], 
            "01_import" : ["PROC_IMPORT_RAW_GRR", "PROC_IMPORT_PARTICLES_GRR", "PROC_IMPORT_OTHER_GRR"],
            "02_preprocess" :  ["PROC_MOTIONCORR_OWN_GRR", "PROC_MOTIONCORR_MC2_GRR","PROC_CTFFIND"], 
            "03_particles" : ["PROC_MANUALPICK", "PROC_AUTOPICK", "PROC_EXTRACT", "PROC_2DCLASS", "PROC_CLASSSELECT"],
            "04_3d" : ["PROC_3DCLASS", "PROC_3DAUTO", "PROC_INIMODEL"],
            "05_postprocess" : ["PROC_MASKCREATE", "PROC_POST", "PROC_MOTIONREFINE", "PROC_CTFREFINE"],
            "06_enhance" : ["PROC_RESMAP"],
            "07_model" : ["PROC_DYNAMIGHT", "PROC_MODELANGELO"],
            "08_tools" : ["PROC_JOINSTAR", "PROC_SUBTRACT", "PROC_MULTIBODY"]
            }
    
    indexes = [0 for i in range (9)]

    jobs_list = ["PROC_IMPORT_RAW_GRR", "PROC_IMPORT_PARTICLES_GRR", "PROC_IMPORT_OTHER_GRR", "PROC_MOTIONCORR_OWN_GRR", "PROC_MOTIONCORR_MC2_GRR"] #, "PROC_CTFFIND", "PROC_MANUALPICK", 
                #  "PROC_AUTOPICK", "PROC_EXTRACT", "PROC_CLASSSELECT", "PROC_2DCLASS", "PROC_3DCLASS", "PROC_3DAUTO", 
                #  "PROC_MASKCREATE", "PROC_JOINSTAR", "PROC_SUBTRACT", "PROC_POST", "PROC_RESMAP", "PROC_INIMODEL", 
                #  "PROC_MULTIBODY", "PROC_MOTIONREFINE", "PROC_CTFREFINE", "PROC_DYNAMIGHT", "PROC_MODELANGELO" ]

    for job in jobs_list :
        print(job)
        # tables = {'indata': init_table('_indata'), 'odata': init_table('_odata'), 'general': init_table('_general')}
        tables = {'indata': init_table('_indata'), 'general': init_table('_general')}

        joboptions = {}
        _main = []

        for r in dirs.keys() :
            if job in dirs[r] :
                # append in 00_tools file
                tool_file = open(f"../../public/spa/{r}/00_tools_test.star", "a")
                tool = rno.JobOptionTool(rh.proc_grinder_settings[f"{job}"])
                tool_file.write(tool.to_star())
                tool = None
                tool_file.close()

                # writing in 0_.star
                indexes[list(dirs).index(r)]+=1
                fic = open(f"../../public/spa/{r}/0{indexes[list(dirs).index(r)]}.star", "w")

                joboptions = initialise(job)
                # print(joboptions)
                # add header from `_main`
                # for hd in range(len(_main)) :
                #     fic.write(f"""data_\n#\n_id {_main[hd]["id"]:<50}\n_label       {_main[hd]["label"]}\n_widget      radio\n_parent      {_main[hd]["parent"]}\n_help        {_main[hd]["help"]}\n_proc_id     {_main[hd]["proc"]}\n_labelnew    {_main[hd]["labelnew"]}\n_dirname     {_main[hd]["dirname"]}\n_hidden_name {_main[hd]["hidden_name"]}\n#""")
                #Tabs
                fic.write(tabs())
                #I/O
                fic.write(io())
                #Settings
                fic.write(settings())
                for e in joboptions.keys():
                    if joboptions[e].widget == 'node':
                        joboptions[e].widget = 'file'
                        joboptions[e].arg2 = 'inode'
                        tables['indata'] += joboptions[e].to_star(e) + '\n'
                    elif joboptions[e].fieldset == 'indata' :
                        tables['indata'] += joboptions[e].to_star(e) + '\n'
                    elif joboptions[e].widget == 'select':
                        # print('select + option')
                        tables['general'] += joboptions[e].to_star(e) + '\n'
                        # Children
                        parent = e
                        if parent not in tables:
                            tables[parent] = init_table(f'_{parent}')
                        for opt in joboptions[e].radio_options:
                            # TODO
                            tables[parent] += opt.to_star(parent) + '\n'
                    else:
                        tables['general'] += joboptions[e].to_star(e) + '\n'

                for t in tables:
                    fic.write(tables[t])
                
                print(f"MPI : {has_mpi} / Thread : {has_thread} / GPU : {has_gpu} / DISK : {has_disk}")
                
                # Optional Argument
                if has_gpu :
                    fic.write(compute_gpu())
                if has_thread and has_mpi : 
                    fic.write(compute_mpi_thread())
                if has_mpi and not has_thread :
                    fic.write(compute_mpi())
                if has_disk :
                    fic.write(disk_access())
                fic.close()

#     # version with print()

#     for job in jobs_list :
#         joboptions = {}
#         _main = []
#         tables = {'indata': init_table('_indata'), 'odata': init_table('_odata'), '_main': init_table('__main')}

#         for r in dirs.keys():
        
#             if job in dirs[r] :
#                 indexes[list(dirs).index(r)]+=1
#                 print(f"open file : ../../public/spa/{r}/0{indexes[list(dirs).index(r)]}.star, w")

#                 initialise(job)
#                 # add header from `_main`
#                 for hd in range(len(_main)) :
#                     print(f"""
# data_
# _id      {_main[hd]["id"]}
# _parent  {_main[hd]["parent"]}
# _widget  {_main[hd]["widget"]}
# _label   {_main[hd]["label"]}
# #
# """)
#                 for e in joboptions.keys():
#                     if joboptions[e].widget == 'node':
#                         joboptions[e].widget = 'file'
#                         joboptions[e].arg2 = 'inode'
#                         tables['indata'] += joboptions[e].to_star(e) + '\n'
#                     elif joboptions[e].widget == 'select':
#                         tables['_main'] += joboptions[e].to_star(e) + '\n'
#                         # Children
#                         parent = e
#                         if parent not in tables:
#                             tables[parent] = init_table(f'_{parent}')
#                         for opt in joboptions[e].radio_options:
#                             # TODO
#                             tables[parent] += opt.to_star(parent) + '\n'
#                     else:
#                         tables['_main'] += joboptions[e].to_star(e) + '\n'

#                 for t in tables:
#                     print(tables[t])

"""

# class rno.Tool
tool = {
    'header': {id:'import_mov'},
    'tabs': {
        'io': rno.Tab('????')
    } # [Tab]
}

tool.tabs['io'].append('indata',rno.Table('indata'))
tool.tabs['io'].append({'outdata', rno.Table('outdata')),
tool.tabs['io'].append({'cli', rno.Table('cli')}
tool.tabs['settings'].append({'general': rno.Table('general'))

for jo in joboptions:
    if isinstance(jo,rno.JobOptionIO):
        tool.tabs['io].tables['indata'].append(jo)
    elif isinstance(jo,rno.JobOption):
        tool.tables['general'].append(jo)

if has_gpu:
    tool.tables['gpu'] = gpu_table
if has_thread:
    tool.tables['process'] = gpu_table    

fc.write(str(tool))

"""