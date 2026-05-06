data_
# Menu
loop_
_transfer.id
_transfer.label
_transfer.icon
_transfer.widget
rln_project  'RELION'       bi-r-circle-fill      submenu
cs_project   'CryoSparc'    bi-c-circle-fill      submenu
# Submenu
loop_
_rln_project.id
_rln_project.label        
_rln_project.widget    
_rln_project.proc_id 
_rln_project.proc_label
_rln_project.filename
_rln_project.state 
_rln_project.help  
rln_proj_new     'New...'             tool   0  grinder.rln.new           01.star   connected 'Create a new RELION Project'
rln_proj_load    'Load...'            tool   0  grinder.rln.load          02.star   connected 'Load RELION Project'    
rln_raw_prep     'Raw Data Install'   tool   0  grinder.rln.symlink       03.star   connected 'Create Symbolic Links to Raw Data Collection before importing Movies/micrographs into RELION'                              
# Submenu
loop_
_cs_project.id
_cs_project.label        
_cs_project.widget    
_cs_project.proc_id 
_cs_project.proc_label
_cs_project.filename
_cs_project.help   
cs_raw_prep     'Install Workspace'   tool   0  grinder.cs.workspace       04.star   'Get a Workspace, download the `job.json` and create a RELION-compatible `default_pipeline.star`'                              
#

