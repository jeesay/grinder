// Select

const select_io_none = [
  {
    name: 'fn_none',
    title: 'Select from:',
    widget: 'paragraph',
    content: 'Choose file type above',
    help: `Choose file type above`,
  }
];
const select_io_class = [
  {
    name: 'fn_model',
    title: 'Select classes from job:',
    widget: 'file',
    option: '--i',
    status: 'hidden',
    filetype: 'NODE_OPTIMISER_CPIPE',
    placeholder: 'STAR files (*_optimiser.star)',
    help: `A _optimiser.star (or for backwards compatibility also a _model.star) file from a previous 2D or 3D classification run to select classes from.`,
  }
];

const select_io_ugraph = [
  {
    name: 'fn_mic',
    title: 'Select from micrographs.star:',
    widget: 'file',
    option: '--i',
    status: 'hidden',
    filetype: 'NODE_MICS_CPIPE',
    placeholder: 'STAR files (*.star)',
    help: `A micrographs.star file to select micrographs from.`,
  },
];

const select_io_ptcls = [
  {
    name: 'fn_data',
    title: 'Select from particles.star:',
    widget: 'file',
    option: '--i',
    status: 'hidden',
    filetype: 'NODE_PARTS_CPIPE',
    help: 'STAR files (*.star)',
    help: `A particles.star file to select individual particles from.`,
  },
]

const select_add = (ev) => {
  console.log('change',ev.target);
  const el = ev.target;
  const parent = el.closest('.tab-content');
  const children = [...parent.children];
  // reset
  children.forEach( child => child.style.display = 'none');
  children[0].style.display = 'flex';
  console.log(el.value);
  children[+el.value+1].style.display = 'flex';
//  w_group({children: desc}).forEach( w => parent.appendChild(w) );
}

const select_io_settings = {
  widget: 'navtab',
  children: [
    {
      name: 'select_io_filetype',
      title: 'Select subsets from:',
      widget: 'select', 
      option: '--select_filetype',
      default: 0,
      help: '',
      children: [
        {
          name:'fn_none_io',
          title: 'None',
          widget: 'option',
          select: true,
          value: 0
        },
        {
          name:'fn_model_io',
          title: 'Classes from job',
          widget: 'option',
          value: 1
        },
        {
          name:'fn_mic_io',
          title: 'micrographs.star',
          widget: 'option',
          value: 2
        },
        {
          name:'fn_ptcls_io',
          title: 'particles.star',
          widget: 'option',
          value: 3
        },
      ],
      on_change: select_add
    },
    ...select_io_none,
    ...select_io_class,
    ...select_io_ugraph,
    ...select_io_ptcls
  ]
}

const select_ranker = [
  {
    name: 'do_class_ranker',
    title: 'Automatically select 2D classes?',
    widget: 'bool',
    default:  false, 
    help: `If set to True, the class_ranker program will be used to make an automated class selection, based on the parameters below. This option only works when selecting classes from a relion_refine job (input optimiser.star on the I.O tab)`,
  },
  {
    name: 'rank_threshold',
    title: 'Minimum threshold for auto-selection: ',
    widget: 'range',
    default:  0.5, 
    range_min: 0, 
    range_max: 1, 
    range_step: 0.05,
    help: `Only classes with a predicted threshold above this value will be selected.`,
  },
  {
    name: 'select_nr_parts',
    title: 'Select at least this many particles: ',
    widget: 'range',
    default:  -1, 
    range_min: -1, 
    range_max: 10000, 
    range_step: 500,
    help: `Even if they have scores below the minimum threshold, select at least this many particles with the best scores.`,
  },
  {
    name: 'select_nr_classes',
    title: 'OR: select at least this many classes: ',
    widget: 'range',
    default:  -1, 
    range_min: -1, 
    range_max: 24, 
    range_step: 1,
    help: `Even if they have scores below the minimum threshold, select at least this many classes with the best scores.`,
  },
  {
    name: 'python_exe',
    title: 'Python executable: ',
    widget: 'text',
    default: 'default_location',
    help: `This version of python should include torch and numpy. We have found that the one from topaz (which is also used for auto-picking) works well. At the LMB, it is here: /public/EM/anaconda3/envs/topaz/bin/python`,
  },
  {
    name: 'do_recenter',
    title: 'Re-center the class averages?',
    widget: 'bool',
    default:  true,
    help: `This option is only used when selecting particles from 2D classes. The selected class averages will all re-centered on their center-of-mass. This is useful when you plane to use these class averages as templates for auto-picking.`,
  },
  {
    name: 'do_regroup',
    title: 'Regroup the particles?',
    widget: 'switch',
    default:  false,
    help: `If set to Yes, then the program will regroup the selected particles in 'more-or-less' the number of groups indicated below. For re-grouping from individual particle _data.star files, a _model.star file with the same prefix should exist, i.e. the particle star file should be generated by relion_refine`,
  },
  {
    name: 'nr_groups',
    title: 'Approximate nr of groups: ',
    widget: 'range',
    default:  1, 
    range_min: 50, 
    range_max: 20, 
    range_step: 1,
    help: `It is normal that the actual number of groups may deviate a little from this number. `,
  },
];

const select_meta = [
  {
    name: 'do_select_values',
    title: 'Select based on metadata values?',
    widget: 'bool',
    default:  false,
    help: `If set to Yes, the job will be non-interactive and the selected star file will be based only on the value of the corresponding metadata label. Note that this option is only valid for micrographs or particles STAR files.`,
  },
  {
    name: 'select_label',
    title: 'Metadata label for subset selection:',
    widget: 'text',
    default: 'rlnCtfMaxResolution',
    help: `This column from the input STAR file will be used for the subset selection.`,
  },
  {
    name: 'select_minval',
    title: 'Minimum metadata value:',
    widget: 'float',
    default: -9999.,
    help: `Only lines in the input STAR file with the corresponding metadata value larger than or equal to this value will be included in the subset.`,
  },
  {
    name: 'select_maxval',
    title: 'Maximum metadata value:',
    widget: 'float',
    default: 9999.,
    help: `Only lines in the input STAR file with the corresponding metadata value smaller than or equal to this value will be included in the subset.`,
  },
];

const select_stats = [
  {
    name: 'do_discard',
    title: 'OR: select on image statistics?',
    widget: 'bool',
    default:  false,
    help: `If set to Yes, the job will be non-interactive and all images in the input star file that have average and/or stddev pixel values that are more than the specified sigma-values away from the ensemble mean will be discarded.`,
  },
  {
    name: 'discard_label',
    title: 'Metadata label for images:',
    default: 'rlnImageName',
    help: `Specify which column from the input STAR contains the names of the images to be used to calculate the average and stddev values.`,
  },
  {
    name: 'discard_sigma',
    title: 'Sigma-value for discarding images:',
    widget: 'range',
    default:  4, 
    range_min: 1, 
    range_max: 10, 
    range_step: 0.1,
    help: `Images with average and/or stddev values that are more than this many times the ensemble stddev away from the ensemble mean will be discarded.`,
  },
];

// Select -> Split

const split_size = [
  {
    name: 'do_random',
    title: 'Randomise before making subsets?',
    widget: 'bool',
    option: '--random_order',
    default: false, 
    help: `If set to Yes, the input STAR file order will be randomised. If set to No, the original order in the input STAR file will be maintained.`,
  },
  {
    name: 'split_size',
    title: 'Subset size:',
    widget: 'range',
    option: '--size_split',
    default:  100, 
    range_min: 100, 
    range_max: 10000, 
    range_step: 100, 
    help: `The number of lines in each of the output subsets. When this is -1, items are divided into a number of subsets specified in the next option.`,
  },
  /*
  {
    name: 'nr_split',
    title: 'OR: number of subsets: ',
    widget: 'range',
    default:  -1, 
    range_min: 1, 
    range_max: 50, 
    range_step: 1, 
    help: `Give a positive integer to specify into how many equal-sized subsets the data will be divided. When the subset size is also specified, only this number of subsets, each with the specified size, will be written, possibly missing some items. When this is -1, all items are used, generating as many subsets as necessary.`,
  },
  */
];

const split_n_groups = [
/*
  {
    name: 'do_split',
    title: 'OR: split into subsets?',
    widget: 'bool',
    default:  false, 
    help: `If set to Yes, the job will be non-interactive and the star file will be split into subsets as defined below.`,
  },
*/
  {
    name: 'do_random',
    title: 'Randomise before making subsets?',
    widget: 'bool',
    option: '--random_order',
    default: false, 
    help: `If set to Yes, the input STAR file order will be randomised. If set to No, the original order in the input STAR file will be maintained.`,
  },
  {
    name: 'nr_split',
    title: 'Number of subsets:',
    widget: 'range',
    option: '--nr_split',
    default:  -1, 
    range_min: 1, 
    range_max: 50, 
    range_step: 1, 
    help: `Give a positive integer to specify into how many equal-sized subsets the data will be divided. When the subset size is also specified, only this number of subsets, each with the specified size, will be written, possibly missing some items. When this is -1, all items are used, generating as many subsets as necessary.`,
  },
  {
    name: 'split_size',
    title: 'Subset size:',
    widget: 'range',
    option: '--size_split',
    default:  -1, 
    range_min: 100, 
    range_max: 10000, 
    range_step: 100, 
    help: `The number of lines in each of the output subsets. When this is -1, items are divided into a number of subsets specified in the previous option.`,
  },
];

const duplicates = [
  {
    name: 'do_remove_duplicates',
    title: 'OR: remove duplicates?',
    widget: 'bool',
    default:  false, 
    help: `If set to Yes, duplicated particles that are within a given distance are removed leaving only one. Duplicated particles are sometimes generated when particles drift into the same position during alignment. They inflate and invalidate gold-standard FSC calculation.`,
  },
  {
    name: 'duplicate_threshold',
    title: 'Minimum inter-particle distance (A)',
    widget: 'range',
    default:  30, 
    range_min: 0, 
    range_max: 1000, 
    range_step: 1, 
    help: `Particles within this distance are removed leaving only one.`,
  },
  {
    name: 'image_angpix',
    title: 'Pixel size before extraction (A)',
    widget: 'range',
    default:  -1, 
    range_min: -1, 
    range_max: 10, 
    range_step: 0.01, 
    help: `The pixel size of particles (relevant to rlnOriginX/Y) is read from the STAR file. When the pixel size of the original micrograph used for auto-picking and extraction (relevant to rlnCoordinateX/Y) is different, specify it here. In other words, this is the pixel size after binning during motion correction, but before down-sampling during extraction.`,
  },
];


const joinstar_particles = {
  widget: 'navtab',
  hidden_name: '.gui_joinstar',
  children: [
  {
    name: 'do_part',
    title: 'Combine particle STAR files?',
    widget: 'bool',
    default:  false,
  },
  {
    name: 'fn_part1',
    title: 'Particle STAR file 1: ',
    widget: 'file',
    filetype: 'NODE_PARTS_CPIPE',
    placeholder: 'particle STAR file (*.star)',
    help: `The first of the particle STAR files to be combined.`,
  },
  {
    name: 'fn_part2',
    title: 'Particle STAR file 2: ',
    widget: 'file',
    filetype: 'NODE_PARTS_CPIPE',
    placeholder: 'particle STAR file (*.star)',
    help: `The second of the particle STAR files to be combined.`,
  },
  {
    name: 'fn_part3',
    title: 'Particle STAR file 3: ',
    widget: 'file',
    filetype: 'NODE_PARTS_CPIPE',
    placeholder: 'particle STAR file (*.star)',
    help: `The third of the particle STAR files to be combined. Leave empty if there are only two files to be combined.`,
  },
  {
    name: 'fn_part4',
    title: 'Particle STAR file 4: ',
    widget: 'file',
    filetype: 'NODE_PARTS_CPIPE',
    placeholder: 'particle STAR file (*.star)',
    help: `The fourth of the particle STAR files to be combined. Leave empty if there are only two or three files to be combined.`,
  },
  ]
};



const joinstar_micrographs = {
  widget: 'navtab',
  hidden_name: '.gui_joinstar',
  children: [
    {
      name: 'fn_mic1',
      title: 'Micrograph STAR file 1: ',
      widget: 'file',
      filetype: 'NODE_MICS_CPIPE',
      placeholder: 'micrograph STAR file (*.star)',
      help: `The first of the micrograph STAR files to be combined.`,
    },
    {
      name: 'fn_mic2',
      title: 'Micrograph STAR file 2: ',
      widget: 'file',
      filetype: 'NODE_MICS_CPIPE',
      placeholder: 'micrograph STAR file (*.star)',
      help: `The second of the micrograph STAR files to be combined.`,
    },
    {
      name: 'fn_mic3',
      title: 'Micrograph STAR file 3: ',
      widget: 'file',
      filetype: 'NODE_MICS_CPIPE',
      placeholder: 'micrograph STAR file (*.star)',
      help: `The third of the micrograph STAR files to be combined. Leave empty if there are only two files to be combined.`,
    },
    {
      name: 'fn_mic4',
      title: 'Micrograph STAR file 4: ',
      widget: 'file',
      filetype: 'NODE_MICS_CPIPE',
      placeholder: 'micrograph STAR file (*.star)',
      help: `The fourth of the micrograph STAR files to be combined. Leave empty if there are only two or three files to be combined.`,
    },
  ]
};

const joinstar_movies = {
  widget: 'navtab',
  hidden_name: '.gui_joinstar',
  children: [
    {
      name: 'fn_mov1',
      title: 'Movie STAR file 1: ',
      widget: 'file',
      filetype: 'NODE_MOVIES_CPIPE',
      placeholder: 'movie STAR file (*.star)',
      help: `The first of the micrograph movie STAR files to be combined.`,
    },
    {
      name: 'fn_mov2',
      title: 'Movie STAR file 2: ',
      widget: 'file',
      filetype: 'NODE_MOVIES_CPIPE',
      placeholder: 'movie STAR file (*.star)',
      help: `The second of the micrograph movie STAR files to be combined.`,
    },
    {
      name: 'fn_mov3',
      title: 'Movie STAR file 3: ',
      widget: 'file',
      filetype: 'NODE_MOVIES_CPIPE',
      placeholder: 'movie STAR file (*.star)',
      help: `The third of the micrograph movie STAR files to be combined. Leave empty if there are only two files to be combined.`,
    },
    {
      name: 'fn_mov4',
      title: 'Movie STAR file 4: ',
      widget: 'file',
      filetype: 'NODE_MOVIES_CPIPE',
      placeholder: 'movie STAR file (*.star)',
      help: `The fourth of the micrograph movie STAR files to be combined. Leave empty if there are only two or three files to be combined.`,
    },
  ]
}
const external = {
  children: [
    // I/O
    {
      name: 'fn_exe',
      title: 'External executable:',
      widget: 'file',
      help: `Location of the script that will launch the external program. This script should write all its output in the directory specified with --o. Also, it should write in that same directory a file called RELION_JOB_EXIT_SUCCESS upon successful exit, and RELION_JOB_EXIT_FAILURE upon failure.`,
    },
    // Optional input nodes
    {
      name: 'in_mov',
      title: 'Input movies: ',
      widget: 'file',
      filetype: 'NODE_MOVIES_CPIPE',
      placeholder: 'movie STAR file (*.star)',
      help: `Input movies. This will be passed with a --in_movies argument to the executable.`,
    },
    {
      name: 'in_mic',
      title: 'Input micrographs: ',
      filetype: 'NODE_MICS_CPIPE',
      default: '',
      placeholder: 'micrographs STAR file (*.star)',
      help: `Input micrographs. This will be passed with a --in_mics argument to the executable.`,
    },
    {
      name: 'in_part',
      title: 'Input particles: ',
      filetype: 'NODE_PARTS_CPIPE',
      default : '',
      placeholder: 'particles STAR file (*.star)',
      help: `Input particles. This will be passed with a --in_parts argument to the executable.`,
    },
    {
      name: 'in_coords',
      title: 'Input coordinates: ',
      filetype: 'NODE_COORDS_CPIPE',
      default: '',
      placeholder: 'STAR files (coords_suffix*.star)',
      help: `Input coordinates. This will be passed with a --in_coords argument to the executable.`,
    },
    {
      name: 'in_3dref',
      title: 'Input 3D reference: ',
      filetype: 'NODE_MAP_CPIPE',
      default: '',
      placeholder: 'MRC files (*.mrc)',
      help: `Input 3D reference map. This will be passed with a --in_3dref argument to the executable.`,
    },
    {
      name: 'in_mask',
      title: 'Input 3D mask: ',
      filetype: 'NODE_MASK_CPIPE',
      default: '',
      placeholder: 'MRC files (*.mrc)',
      help: `Input 3D mask. This will be passed with a --in_mask argument to the executable.`,
    },

    // Optional parameters
    {
      name: 'param1_label',
      title: 'Param1 - label:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param1_value',
      title: 'Param1 - value:' , 
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param2_label',
      title: 'Param2 - label:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param2_value',
      title: 'Param2 - value:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param3_label',
      title: 'Param3 - label:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param3_value',
      title: 'Param3 - value:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param4_label',
      title: 'Param4 - label:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param4_value',
      title: 'Param4 - value:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param5_label',
      title: 'Param5 - label:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param5_value',
      title: 'Param5 - value:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param6_label',
      title: 'Param6 - label:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param6_value',
      title: 'Param6 - value:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param7_label',
      title: 'Param7 - label:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param7_value',
      title: 'Param7 - value:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param8_label',
      title: 'Param8 - label:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param8_value',
      title: 'Param8 - value:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param9_label',
      title: 'Param9 - label:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param9_value',
      title: 'Param9 - value:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param10_label',
      title: 'Param10 - label:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
    {
      name: 'param10_value',
      title: 'Param10 - value:',
      widget: 'text',
      default: '', 
      help: `Define label and value for optional parameters to the script. These will be passed as an argument --label value`,
    },
  ]
};

// Tabs

const rank_io_settings = {
  widget: 'navtab',
  children: select_io_class
}

const rank_settings = {
  widget: 'navtab',
  children: select_ranker
}

const select_meta_settings = {
  widget: 'navtab',
  children: select_meta
}

const split_n_ptcls_tab = {
  widget: 'navtab',
  children: split_n_groups
}

const split_size_ptcls_tab = {
  widget: 'navtab',
  children: split_size
}


const tools_tabs = [
  {
    name: 'tools',
    title: 'Tools',
    icon: 'bi-wrench-adjustable',
    widget: 'navtab',
    default:  true, 
    children: [
      {
        name: 'select_auto',
        title: 'Subset selection',
        icon: 'bi-list-check',
        widget: 'fieldset',
        children: [
          {
            name: 'fn_metadata',
            title: 'Subset selection based on metadata',
            widget: 'radio',
            option: '--fn_model',
            group: 'toolkit',
            help: `A _optimiser.star (or for backwards compatibility also a _model.star) file from a previous 2D or 3D classification run to select classes from.`,
            on_click: (ev) => w_navtab_update({io: select_io_settings,settings: select_meta_settings})
          },
          {
            name: 'fn_stats',
            title: 'Subset selection based on statistics',
            widget: 'radio',
            option: '--fn_mic',
            group: 'toolkit',
            help: `A micrographs.star file to select micrographs from.`,
            on_click: (ev) => w_navtab_update({settings: joinstar_particles})
          }
        ]
      },
      {
        name: 'select_auto',
        title: 'Automatic class selection',
        icon: 'bi-robot',
        widget: 'fieldset',
        children: [
          {
            name: 'do_class_ranker',
            title: 'Select automatically P particles from 2D classes',
            widget: 'radio',
            option: '--do_class_ranker',
            group: 'toolkit',
            help: `If set to True, the class_ranker program will be used to make an automated class selection, based on the parameters below. This option only works when selecting classes from a relion_refine job (input optimiser.star on the I.O tab)`,
            on_click: (ev) => w_navtab_update({io: rank_io_settings,settings: rank_settings})
          },
          {
            name: 'do_class_ranker',
            title: 'Select automatically N classes',
            widget: 'radio',
            option: '--do_class_ranker',
            group: 'toolkit',
            help: `If set to True, the class_ranker program will be used to make an automated class selection, based on the parameters below. This option only works when selecting classes from a relion_refine job (input optimiser.star on the I.O tab)`,
            on_click: (ev) => w_navtab_update({io: rank_io_settings,settings: rank_settings})
          },
        ]
      },
      {
        name: 'do_split',
        title: 'Split data',
        icon: 'bi-arrows-angle-expand',
        widget: 'fieldset',
        children: [
          {
            name: 'split_e',
            title: 'Split in subsets of E elements',
            widget: 'radio',
            option: '--split',
            group: 'toolkit',
            help: `A particles.star file to select individual particles from.`,
            on_click: (ev) => w_navtab_update({io: select_io_settings, settings: split_size_ptcls_tab})
          },
          {
            name: 'split_n',
            title: 'Split in N subsets',
            widget: 'radio',
            option: '--fn_data',
            group: 'toolkit',
            help: `If set to Yes, the job will be non-interactive and the star file will be split into subsets as defined below.`,
            on_click: (ev) => w_navtab_update({io: select_io_settings, settings: split_n_ptcls_tab})
          },
        ]
      },
      {
        name: 'join_star',
        title: 'Join STAR files',
        icon: 'bi-arrows-angle-contract',
        widget: 'fieldset',
        children: [
          {
            name: 'do_part',
            title: 'Combine particle STAR files',
            widget: 'radio',
            option: '--do_part',
            group: 'toolkit',
            help: 'Set this to Yes if you plan to join particle STAR files',
            on_click: (ev) => w_navtab_update({settings: joinstar_particles})
          },
          {
            name: 'do_mic',
            title: 'Combine micrograph STAR files?',
             widget: 'radio',
            option: '--do_mic',
            group: 'toolkit',
            help: 'Set this to Yes if you plan to join micrograph STAR files',
            on_click: (ev) => w_navtab_update({settings: joinstar_micrographs})
          },
          {
            name: 'do_mov',
            title: 'Combine movie STAR files',
            widget: 'radio',
            option: '--do_mov',
            group: 'toolkit',
            help: 'Set this to Yes if you plan to join movie STAR files',
            on_click: (ev) => w_navtab_update({settings: joinstar_movies})
          },
        ]
      },
      {
        name: 'extras',
        title: 'Extras',
        icon: 'bi-bag-plus',
        widget: 'fieldset',
        children : [
          {
            name: 'class2d_particles',
            title: 'Particle subtraction',
            widget: 'radio',
            option: '--fn_model',
            group: 'toolkit',
            help: ``,
            on_click: (ev) => w_navtab_update({settings: class2d_particles_tabs})
          },
          {
            name: 'crop',
            title: 'Crop/Pad 3D map',
            widget: 'radio',
            group: 'toolkit',
            help: 'Set this to Yes if you plan to import raw micrographs',
          },
          {
            name: 'resize',
            title: 'Resize 3D map',
            widget: 'radio',
            group: 'toolkit',
            help: 'Set this to Yes if you plan to import raw micrographs',
          },
          {
            name: 'do_micrographs',
            title: 'External',
            option: '--do_micrographs',
            widget: 'radio',
            group: 'toolkit',
            help: 'Set this to Yes if you plan to import raw micrographs',
            on_click: (ev) => w_navtab_update({settings: raw_settings})
          },
        ]
      }
    ]
  },
  {
    name: 'io',
    icon: 'bi-arrow-down-up',
    title: 'I/O',
    widget: 'navtab',
    children: []
  },
  {
    name: 'settings',
    icon: 'bi-tools',
    title: 'Settings',
    widget: 'navtab',
    children: []
  },
  {
    name: 'running',
    icon: 'bi-send',
    title: 'Running',
    widget: 'navtab',
    children: [
      queue_settings,
      ...submit_settings
    ]
  }
];


