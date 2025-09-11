#!/bin/bash


# > spa/01-Import
cat > label.txt <<EOL
#
_main.label    'Raw movies'
_main.widget    radio
_main.toolbox   movies
_main.help     'Set this to Yes if you plan to import raw movies'
EOL
echo data_movies | cat - label.txt menu_template.star > spa/01_import/01_import_movies.star
cat > label.txt <<EOL
#
_main.label    'Raw micrographs'
_main.widget    radio
_main.toolbox   movies
_main.help     'Set this to Yes if you plan to import raw micrographs'
EOL
echo data_micrographs | cat - label.txt menu_template.star > spa/01_import/02_import_micrographs.star
cat > label.txt <<EOL
#
_main.label    'Micrographs STAR File (.star)'
_main.widget    radio
_main.toolbox   movies
_main.help     ''
EOL
echo data_micrographs_star | cat - label.txt menu_template.star > spa/01_import/03_import_micrographs_starfile.star
cat > label.txt <<EOL
#
_main.label    '???'
_main.widget    radio
_main.toolbox   particles
_main.help     ''
EOL
echo data_ptcls_coords | cat - label.txt menu_template.star > spa/01_import/04_import_particle_coords.star
cat > label.txt <<EOL
#
_main.label    '???'
_main.widget    radio
_main.toolbox   particles
_main.help     ''
EOL
echo data_ptcls_star | cat - label.txt menu_template.star > spa/01_import/05_import_particle_starfile.star
cat > label.txt <<EOL
#
_main.label    '???'
_main.widget    radio
_main.toolbox   refs
_main.help     ''
EOL
echo data_import_ref | cat - label.txt menu_template.star > spa/01_import/06_import_ref.star
cat > label.txt <<EOL
#
_main.label    '???'
_main.widget    radio
_main.toolbox   refs
_main.help     ''
EOL
echo data_import_ref3d | cat - label.txt menu_template.star > spa/01_import/07_import_ref3d.star
cat > label.txt <<EOL
#
_main.label    '???'
_main.widget    radio
_main.toolbox   masks
_main.help     ''
EOL
echo data_import_mask3d | cat - label.txt menu_template.star > spa/01_import/08_import_mask3d.star
cat > label.txt <<EOL
#
_main.label    '???'
_main.widget    radio
_main.toolbox   masks
_main.help     ''
EOL
echo data_import_mask_half | cat - label.txt menu_template.star > spa/01_import/09_import_mask_half.star
cat > label.txt <<EOL
#
_main.label    '???'
_main.widget    radio
_main.toolbox   others
_main.help     ''
EOL
echo data_import_other | cat - label.txt menu_template.star > spa/01_import/10_import_other.star

exit

#  > spa/02_preprocess
echo data_motion_relion | cat - menu_template.star > spa/02_preprocess/01_motion_relion.star
echo data_motion_ucsf   | cat - menu_template.star > spa/02_preprocess/02_motion_ucsf.star
echo data_ctffind4      | cat - menu_template.star > spa/02_preprocess/03_ctffind4.star
echo data_gctf          | cat - menu_template.star > spa/02_preprocess/04_gctf.star
# > spa/03_particles
echo data_test | cat - menu_template.star > spa/03_particles/01_manual.star
echo data_test | cat - menu_template.star > spa/03_particles/02_auto_LoG.star
echo data_test | cat - menu_template.star > spa/03_particles/03_auto_template.star
echo data_test | cat - menu_template.star > spa/03_particles/04_auto_topaz_train_coords.star
echo data_test | cat - menu_template.star > spa/03_particles/05_auto_topaz_train_ptcls.star
echo data_test | cat - menu_template.star > spa/03_particles/06_auto_topaz_pick.star
echo data_test | cat - menu_template.star > spa/03_particles/07_extract.star
echo data_test | cat - menu_template.star > spa/03_particles/08_re_extract.star
echo data_test | cat - menu_template.star > spa/03_particles/09_re_extract_center.star
echo data_test | cat - menu_template.star > spa/03_particles/10_class2d_em.star
echo data_test | cat - menu_template.star > spa/03_particles/11_class2d_vdam.star
# > spa/04_3d
echo data_test | cat - menu_template.star > spa/04_3d/01_abinitio.star
echo data_test | cat - menu_template.star > spa/04_3d/02_class3d.star
echo data_test | cat - menu_template.star > spa/04_3d/03_class3d_noalign.star
echo data_test | cat - menu_template.star > spa/04_3d/04_refine.star
echo data_test | cat - menu_template.star > spa/04_3d/05_autorefine.star
echo data_test | cat - menu_template.star > spa/04_3d/06_multibody.star
# > spa/05_postprocess
echo data_test | cat - menu_template.star > spa/05_postprocess/01_mask.star
echo data_test | cat - menu_template.star > spa/05_postprocess/02_postprocess.star
echo data_test | cat - menu_template.star > spa/05_postprocess/03_sharpen_auto.star
echo data_test | cat - menu_template.star > spa/05_postprocess/04_sharpen_user.star
echo data_test | cat - menu_template.star > spa/05_postprocess/05_ctfrefine.star
echo data_test | cat - menu_template.star > spa/05_postprocess/06_aberrations.star
echo data_test | cat - menu_template.star > spa/05_postprocess/07_anisomag.star
echo data_test | cat - menu_template.star > spa/05_postprocess/08_defocus.star
echo data_test | cat - menu_template.star > spa/05_postprocess/09_advctfrefine.star
echo data_test | cat - menu_template.star > spa/05_postprocess/10_polish.star
echo data_test | cat - menu_template.star > spa/05_postprocess/11_polish_train.star
echo data_test | cat - menu_template.star > spa/05_postprocess/12_polish_perform.star
echo data_test | cat - menu_template.star > spa/05_postprocess/13_polish_perform_manual.star
# > spa/06_metrics
echo data_test | cat - menu_template.star > spa/06_metrics/locres.star
echo data_test | cat - menu_template.star > spa/06_metrics/locres_relion.star
# > spa/07_tools
echo data_test | cat - menu_template.star > spa/07_tools/01_subset_selection.star
echo data_test | cat - menu_template.star > spa/07_tools/01_subset_selection_stats.star
# Automatic class selection
#echo data_test | cat - menu_template.star > spa/07_tools/01_select_particles_from_classes.star
#echo data_test | cat - menu_template.star > spa/07_tools/01_select_classes.star
echo data_test | cat - menu_template.star > spa/07_tools/01_split_in_elements.star
echo data_test | cat - menu_template.star > spa/07_tools/01_split_in_subsets.star
echo data_test | cat - menu_template.star > spa/07_tools/01_join_star.star
echo data_test | cat - menu_template.star > spa/07_tools/01_combine_particle.star
echo data_test | cat - menu_template.star > spa/07_tools/01_combine_micrograph.star
echo data_test | cat - menu_template.star > spa/07_tools/01_combine_movie.star
echo data_test | cat - menu_template.star > spa/07_tools/01_ptcls_subtract.star
echo data_test | cat - menu_template.star > spa/07_tools/01_crop_pad.star
echo data_test | cat - menu_template.star > spa/07_tools/01_resize_map.star
echo data_test | cat - menu_template.star > spa/07_tools/01_external.star



