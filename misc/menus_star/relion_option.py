import relion_h as rh
from typing import override


def clear():
  pass
  
class JobOption:

# Any constructor
    def __init__(self,*args):
    
        self.id     = '?'
        self.label  = '?'
        self.widget = '?'
        self.value  = '?'
        self.arg0   = '?'
        self.arg1   = '?'
        self.arg2   = '?'
        self.help   = '?'
        self.tab = 'settings'
        self.fieldset = 'general'
        if len(args) == 3 and type(args[1]) == bool:
            self.init_bool(*args)
        elif len(args) == 3:
            self.init_any(*args)
        elif len(args) == 4:
            self.init_radio(*args)
        elif len(args) == 5: 
            self.init_fn(*args)
        elif len(args) == 6 and (type(args[2]) == int or type(args[2]) == float) and (type(args[3]) == int or type(args[3]) == float): 
            self.init_slider(*args)
        elif len(args) == 6: 
            self.init_innode(*args)
        elif len(args) == 8: 
            self.init_widget(*args)
        else:
          print('Unknown widget',args[0])
    
    def initialise(self,_label,_defaultvalue,_help):
        self.label = _label
        self.value = _defaultvalue
        self.help = _help
  

    def init_any(self, _label, _default_value, _helptext):
        # signature: std::string std::string std::string
        clear()
        self.widget = 'string'
        self.initialise(_label, _default_value, _helptext)
        joboption_type = rh.JOBOPTION_ANY

    def init_widget(self, _id, _label, _wdg, _default_value, _a0, _a1, _a2, _helptext):
        # all the params filled
        clear()
        self.id = _id
        self.label = _label
        self.widget = _wdg
        self.value = _default_value
        self.arg0 = _a0
        self.arg1 = _a1
        self.arg2 = _a2
        self.help = _helptext


# FileName constructor
    def init_fn(self, _label, _default_value, _pattern, _directory, _helptext):
        # signature: std::string std::string std::string std::string std::string
        clear()
        self.widget = 'file'
        if _default_value == '':
            self.initialise(_label, '?', _helptext)
        else:
            self.initialise(_label, _default_value, _helptext)
        joboption_type = rh.JOBOPTION_FILENAME
        self.arg0 = _pattern
        self.arg1 = _directory
        pattern = _pattern
        directory = _directory


# InputNode constructor
    def init_innode(self, _label, _nodetype, _node_type_depth, _default_value, _pattern, _helptext):
        # signature  (std::string std::string int  std::string std::string std::string
        clear()
        self.initialise(_label, _default_value, _helptext)
        self.widget = 'node'
        self.value = _nodetype
        self.arg0 = _pattern
        self.arg1 = _node_type_depth
        
        joboption_type = rh.JOBOPTION_INPUTNODE
        pattern = _pattern
        node_type_depth = _node_type_depth
        node_type = _nodetype


# Radio constructor
    def init_radio(self, _label, _radio_options, ioption, _helptext):
        # signature  (std::string, List, int,  std::string)
        clear()
        defaultval = ''
        options = []
        for i,opt in enumerate(_radio_options):
            options.append(
                JobOption('None', opt, 'option', i, '?', '?', '?', '?')
            )
        self.radio_options = options
        defaultval = ioption
        self.arg0 = _radio_options[ioption]
        self.widget = 'select'
        self.initialise(_label, defaultval, _helptext)
        joboption_type = rh.JOBOPTION_RADIO


# Boolean constructor
    def init_bool(self, _label, _boolvalue, _helptext):
        # signature  (std::string, bool, std::string)
        clear()
        _default_value = "true" if (_boolvalue) else "false"
        self.widget = 'bool'
        self.initialise(_label, _default_value, _helptext)
        joboption_type = rh.JOBOPTION_BOOLEAN


# Slider constructor
    def init_slider(self, _label, _default_value, _min_value, _max_value, _step_value, _helptext):
        # signature  (std::string, float, float, float, float, std::string)
        clear()
        self.initialise(_label, _default_value, _helptext)
        joboption_type = rh.JOBOPTION_SLIDER
        self.widget = 'range'
        self.arg0 = _min_value
        self.arg1  = _max_value
        self.arg2  = _step_value


    def to_star(self,id):
        def simple_widget():
            _i = self.id
            _l = self.label
            _v = f'"{self.value}"' if (' ' in str(self.value) or len(str(self.value)) == 0) else self.value
            _w = self.widget
            _a = f'"{self.arg0}"' if ' ' in str(self.arg0) else self.arg0
            _b = f'"{self.arg1}"' if ' ' in str(self.arg1) else self.arg1
            _c = f'"{self.arg2}"' if ' ' in str(self.arg2) else self.arg2
            _h = f'    "{self.help}"'
            if len(self.help) > 80:
                _h = f'\n;\n{self.help}\n;'
            return f'{_i}   "{_l}"    {_w}    {_v}    {_a}    {_b}    {_c}' + _h

        self.id = id
        if self.widget == 'option':
          self.id = f"{id}_opt_{self.value:02d}"
          
        _i = self.id

        s = simple_widget()
        
        # Create a new table with parent's name
#        if self.widget == 'radio':
#            for k,opt in enumerate(self.radio_options):
#              s += f'\n{_i}_opt_{k:02d}  "{opt}"    option    {k}    {_i}    ?    ?   ?'

        return s

    def getBoolean(self):
        return self.valuevalue

class JobOptionIO(JobOption):
    def __init__(self, *args):
        super().__init__(*args)
        self.tab='io'
        self.fieldset='indata'

class JobOptionTool(JobOption):
    def __init__(self, tuple): # tuple : (_id, _label, _widget, _proc_id, _labelnew, _help, _filename)
        self.id       = tuple[0]
        self.label    = tuple[1]
        self.widget   = tuple[2]
        self.proc_id  = tuple[3]
        self.labelnew = tuple[4]
        self.help     = tuple[5]
        self.filename = tuple[6]

    @override
    def to_star(self):
        def simple_widget():
            _i = self.id
            _l = self.label
            _w = self.widget
            _p = f"{self.proc_id}"
            _ln = f"{self.labelnew}"
            _h = f"{self.help}"
            _f = f"{self.filename}"
            return f'{_i}   "{_l}"    {_w}    {_p}    {_ln}    {_h}    {_f}\n'

        s = simple_widget()
        return s