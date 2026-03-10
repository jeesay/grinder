data_
#
loop_
_pprcss.id
_pprcss.label
_pprcss.icon
_pprcss.widget
_pprcss.value
_pprcss.help
io                   "I/O"                      bi-arrow-down-up    tab              ?        ?
settings             "Settings"                bi-tools             tab              ?        ?
log                  "Log"                     bi-binoculars-fill   tab              ?        ?
dataviz              "DataViz"                 bi-eye               tab              ?        ?
#
loop_
_io.id
_io.label
_io.icon
_io.widget
_io.value
_io.display
_io.help
indata               "Input Data"                             bi-box-arrow-in-down fieldset   ?          show       ?
outdata              "Output Data"                            bi-box-arrow-down    fieldset   ?          hidden     ?
nodes                "Nodes"                                  bi-controller        fieldset   ?          hidden     ?
system               "System"                                 bi-incognito         fieldset   ?          hiddden    ?
pprcss_cmd           "Check command"                          bi-chat-right-text   cli        ?          show       ?
#
loop_
_indata.id
_indata.label
_indata.widget
_indata.default
_indata.arg0
_indata.arg1
_indata.arg2
_indata.constraint
_indata.help
fn_in                "One of the 2 unfiltered half-maps:" file       ?               "DensityMap.mrc.halfmap" 1               "MRC map files (*half1*.mrc)" required        
; Provide one of the two unfiltered half-reconstructions that were output upon convergence of a 3D auto-refine run.
;
fn_mask              "Solvent mask:"                     file       ?               "Mask3D.mrc"    1               "Image Files (*.{spi,vol,msk,mrc})" required        
; Provide a soft mask where the protein is white (1) and the solvent is black (0).
Often, the softer the mask the higher resolution estimates you will get.
A soft edge of 5-10 pixels is often a good edge width.
;
#
loop_
_outdata.id
_outdata.label
_outdata.widget
_outdata.default
_outdata.arg0
_outdata.arg1
_outdata.arg2
_outdata.constraint
_outdata.help
#
loop_
_nodes.id
_nodes.label
_nodes.widget
_nodes.default
_nodes.arg0
_nodes.arg1
_nodes.arg2
_nodes.constraint
_nodes.help
#
loop_
_system.id
_system.label
_system.widget
_system.default
_system.arg0
_system.arg1
_system.arg2
_system.constraint
_system.help
#
loop_
_pprcss_cmd.id
_pprcss_cmd.label
_pprcss_cmd.widget
_pprcss_cmd.default
_pprcss_cmd.arg0
_pprcss_cmd.arg1
_pprcss_cmd.arg2
_pprcss_cmd.constraint
_pprcss_cmd.help
#
loop_
_settings.id
_settings.label
_settings.icon
_settings.widget
_settings.value
_settings.display
_settings.help
general              "General"                                bi-chat-right-text   fieldset   ?          show       ?
do_auto_bfac         "Estimate B-factor automatically?"       bi-chat-right-text   switch     ?          show       ?
do_adhoc_bfac        "Use your own B-factor?"                 bi-chat-right-text   switch     ?          show       ?
do_skip_fsc_weighting "Skip FSC-weighting?"                    bi-chat-right-text   switch     ?          show       ?
params_01            "Parameters"                             bi-chat-right-text   fieldset   ?          show       ?
#
loop_
_general.id
_general.label
_general.widget
_general.default
_general.arg0
_general.arg1
_general.arg2
_general.constraint
_general.help
angpix               "Calibrated pixel size (A)"         range      -1              0.3             5               0.1             ?               
; Provide the final, calibrated pixel size in Angstroms.
This value may be different from the pixel-size used thus far, e.g.
when you have recalibrated the pixel size using the fit to a PDB model.
The X-axis of the output FSC plot will use this calibrated value.
;
#
loop_
_do_auto_bfac.id
_do_auto_bfac.label
_do_auto_bfac.widget
_do_auto_bfac.default
_do_auto_bfac.arg0
_do_auto_bfac.arg1
_do_auto_bfac.arg2
_do_auto_bfac.constraint
_do_auto_bfac.help
autob_lowres         "Lowest resolution for auto-B fit (A):" range      10              8               15              0.5             ?               
; This is the lowest frequency (in Angstroms) that will be included in the linear fit of the Guinier plot as described in Rosenthal and Henderson (2003, JMB).
Dont use values much lower or higher than 10 Angstroms.
If your map does not extend beyond 10 Angstroms, then instead of the automatedrh.PROCedure use your own B-factor.
;
#
loop_
_do_adhoc_bfac.id
_do_adhoc_bfac.label
_do_adhoc_bfac.widget
_do_adhoc_bfac.default
_do_adhoc_bfac.arg0
_do_adhoc_bfac.arg1
_do_adhoc_bfac.arg2
_do_adhoc_bfac.constraint
_do_adhoc_bfac.help
adhoc_bfac           "User-provided B-factor:"           range      -1000           -2000           0               -50             ?               
; Use negative values for sharpening.
Be careful: if you over-sharpen your map, you may end up interpreting noise for signal!
;
#
loop_
_do_skip_fsc_weighting.id
_do_skip_fsc_weighting.label
_do_skip_fsc_weighting.widget
_do_skip_fsc_weighting.default
_do_skip_fsc_weighting.arg0
_do_skip_fsc_weighting.arg1
_do_skip_fsc_weighting.arg2
_do_skip_fsc_weighting.constraint
_do_skip_fsc_weighting.help
do_skip_fsc_weighting "Skip FSC-weighting?"               bool       false           "?"             "?"             "?"             ?               
; If set to No (the default), then the output map will be low-pass filtered according to the mask-corrected, gold-standard FSC-curve.
Sometimes, it is also useful to provide an ad-hoc low-pass filter (option below), as due to local resolution variations some parts of the map may be better and other parts may be worse than the overall resolution as measured by the FSC.
In such cases, set this option to Yes and provide an ad-hoc filter as described below.
;
low_pass             "Ad-hoc low-pass filter (A):"       range      5               1               40              1               ?               
; This option allows one to low-pass filter the map at a user-provided frequency (in Angstroms).
When using a resolution that is higher than the gold-standard FSC-reported resolution, take care not to interpret noise in the map for signal...
;
#
loop_
_params_01.id
_params_01.label
_params_01.widget
_params_01.default
_params_01.arg0
_params_01.arg1
_params_01.arg2
_params_01.constraint
_params_01.help
fn_mtf               "MTF of the detector (STAR file)"   file       ?               "STAR Files (*.star)" "."             "?"             ?               
; If you know the MTF of your detector, provide it here.
Curves for some well-known detectors may be downloaded from the RELION Wiki.
Also see there for the exact format 
 If you do not know the MTF of your detector and do not want to measure it, then by leaving this entry empty, you include the MTF of your detector in your overall estimated B-factor upon sharpening the map.Although that is probably slightly less accurate, the overall quality of your map will probably not suffer very much.
;
mtf_angpix           "Original detector pixel size:"     range      1.0             0.3             2.0             0.1             ?               
; This is the original pixel size (in Angstroms) in the raw (non-super-resolution!) micrographs.
;
#
loop_
_log.id
_log.label
_log.icon
_log.widget
_log.value
_log.display
_log.help
#
loop_
_dataviz.id
_dataviz.label
_dataviz.icon
_dataviz.widget
_dataviz.value
_dataviz.display
_dataviz.help
#
