#!/bin/bash


# > spa/01-Import
cat > label.txt <<EOL
#
_id        import_movies
_label     'Raw movies'
_widget    radio
_parent    movies
_help      'Set this to Yes if you plan to import raw multi-frame movies. Don\'t import files outside the project directory.\nPlease make a symbolic link by an absolute path before importing.'
_comment   'import_movies'
EOL
echo data_ | cat - label.txt menu_template.star > spa/01_import/01.star
cat > label.txt <<EOL
#
_id        import_micrographs
_label    'Raw micrographs'
_widget   radio
_parent   movies
_help     'Set this to Yes if you plan to import raw single-frame micrographs'
_comment  'import_micrographs'
EOL
echo data_ | cat - label.txt menu_template.star > spa/01_import/02.star
cat > label.txt <<EOL
#
_id        import_micrographs_starfile
_label    'Micrographs STAR File (.star)'
_widget   radio
_parent   movies
_help     ''
_comment  'import_micrographs_starfile'
EOL
echo data_ | cat - label.txt menu_template.star > spa/01_import/03.star
cat > label.txt <<EOL
#
_id       import_particle_coords
_label    'Particles coordinates (.box, *_pick.star)'
_widget    radio
_parent   particles
_help     ''
_comment  'import_particle_coords'
EOL
echo data_ | cat - label.txt menu_template.star > spa/01_import/04.star
cat > label.txt <<EOL
#
_id       particles_starfile
_label    'Particles STAR file (.star)'
_widget    radio
_parent   particles
_help     ''
_comment  'import_particle_starfile'
EOL
echo data_ | cat - label.txt menu_template.star > spa/01_import/05.star
cat > label.txt <<EOL
#
_id       import_ref
_label    'Multiple (2D or 3D) references (.star or .mrcs)'
_widget   radio
_parent   refs
_help     'import_ref'
_comment  'import_movies'
EOL
echo data_ | cat - label.txt menu_template.star > spa/01_import/06.star
cat > label.txt <<EOL
#
_id       import_ref3d
_label    '3D reference (.star)'
_widget    radio
_parent   refs
_help     ''
_comment  'import_ref3d'
EOL
echo data_ | cat - label.txt menu_template.star > spa/01_import/07.star
cat > label.txt <<EOL
#
_id       import_mask3d
_label    '3D mask (.mrc)'
_widget    radio
_parent   masks
_help     ''
_comment  'import_mask3d'
EOL
echo data_ | cat - label.txt menu_template.star > spa/01_import/08.star
cat > label.txt <<EOL
#
_id       import_mask_half
_label    'Unfiltered half-mask (unfil.mrc)'
_widget    radio
_parent   masks
_help     ''
_comment  'import_mask_half'
EOL
echo data_ | cat - label.txt menu_template.star > spa/01_import/09.star
cat > label.txt <<EOL
#
_id       import_other
_label    'MTF, Gain ref., Defect, etc.'
_widget    radio
_parent   others
_help     ''
_comment  'import_other'
EOL
echo data_ | cat - label.txt menu_template.star > spa/01_import/10.star

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



