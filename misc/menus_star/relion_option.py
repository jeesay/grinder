import relion_h as rh
from typing import List, Dict, Union, override

def clear():
  pass

def format_star_string(value):
        """Gère les quotes et les blocs de texte multi-lignes (;)"""
        s = str(value)
        if '\n' in s: # Texte multi-lignes
            return f"\n;\n{s}\n;"
        if ' ' in s or s == '': # Texte avec espaces
            return f"'{s}'" if '"' in s else f'"{s}"'
        return s
  
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


    def to_star(self):
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

        # self.id = id
        if self.widget == 'option':
          self.id = f"{self.id}_opt_{self.value:02d}"
          
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
        parts = [
            f"{self.id:<15}",
            f"{self.label:<20}",
            f"{self.widget:<10}",
            f"{self.proc_id:<5}",
            f"{self.labelnew:<30}",
            f"{self.help:<30}",
            f"{self.filename:<30}",
            '\n'
        ]
        return "   ".join(parts)
    
        # def simple_widget():
        #     _i = self.id
        #     _l = self.label
        #     _w = self.widget
        #     _p = f"{self.proc_id}"
        #     _ln = f"{self.labelnew}"
        #     _h = f"{self.help}"
        #     _f = f"{self.filename}"
        #     return f'{_i}   "{_l}"    {_w}    {_p}    {_ln}    {_h}    {_f}\n'

        # s = simple_widget()
        # return s

class Row:
    def __init__(self,*args, **kwargs):
        print(args,kwargs)
        self.content = kwargs

    def from_joboption(self,jo):
        self.content = jo.__dict__

    @property
    def columns(self):
        return self.content.keys()
    
    @property
    def values(self):
        return self.content.values()
    
    def get(self,k):
        return self.content[k]
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        def quoted(s):
            if type(s) == str and ' ' in s:
                return f'"{s}"'
            return s
        
        return  ''.join([f'{quoted(v):<20} '  for v in self.values])
    
# class Table:
#     def __init__(self, id,columns):
#         self.id = id
#         self.columns = columns
#         self.rows: List[Row] = []

#     def append(self, option: Row):
#         row = {}
#         for k in self.columns:
#             if k in option.columns:
#                 row[k] = option.get(k)
#             else:
#                 row[k] = '?'

#         self.rows.append(Row(**row))

#     def to_definition_line(self, parent_name: str) -> str:
#         """Génère la ligne qui définit cette table dans l'en-tête de l'onglet"""
#         # Format: id label icon widget default help
#         return f"{self.id:<15} {format_star_string(self.label):<25} {self.icon:<20} {self.widget:<15} ?      {format_star_string(self.help_text)}"

#     def __repr__(self) -> str:
#         """Génère le bloc loop_ complet avec les données"""
#         if not self.rows: 
#             return ""
        
#         prefix = f"_{self.id}"
#         header = f"#\nloop_\n"
#         for col in self.columns:
#             header += f'{prefix}.{col:<20}\n'
        
#         rows = [str(opt) for opt in self.rows]
#         return header + "\n".join(rows) + "\n"
    
class Table:
    def __init__(self, id: str, label: str = "", icon: str = "", widget: str = "fieldset", help_text: str = "?"):
        self.id = id  # ex: indata
        self.label = label
        self.icon = icon
        self.widget = widget # fieldset, range, etc.
        self.help_text = help_text
        self.options: Dict[str,JobOption] = {}

    def append(self, key: str, option: JobOption):
        option.id = key
        self.options[key] = option
        # self.options.append(option)

    def to_definition_line(self, parent_name: str) -> str:
        """Génère la ligne qui définit cette table dans l'en-tête de l'onglet"""
        # Format: id label icon widget default help
        return f"{self.id:<15} {format_star_string(self.label):<25} {self.icon:<20} {self.widget:<15} ?      {format_star_string(self.help_text)}"

    def to_content_block(self) -> str:
        """Génère le bloc loop_ complet avec les données"""
        if not self.options: return ""
        
        prefix = f"_{self.id}"
        header = f"#\nloop_\n{prefix}.id\n{prefix}.label\n{prefix}.widget\n{prefix}.default\n{prefix}.arg0\n{prefix}.arg1\n{prefix}.arg2\n{prefix}.help"
        
        lines = [opt.to_star() for opt in self.options.values()]
        
        return header + "\n" + "\n".join(lines)
    

class Tab:
    def __init__(self, name: str, label: str, icon: str):
        self.name = name # ex: io
        self.label = label
        self.icon = icon
        self.tables: Dict[str, Table] = {} # Dictionnaire de tables

    def add_table(self, table: Table):
        self.tables[table.id] = table

    def to_definition_line(self) -> str:
        """Génère la ligne pour le loop principal du Tool"""
        # Format: id label icon widget default parent help
        return f"{self.name:<10} {format_star_string(self.label):<25} {self.icon:<25} tab ? ? ?"

    def get_structure_block(self) -> str:
        """Génère le bloc loop_ qui liste les tables contenues dans cet onglet"""
        if not self.tables: return ""
        
        prefix = f"_{self.name}"
        header = f"#\nloop_\n{prefix}.id\n{prefix}.label\n{prefix}.icon\n{prefix}.widget\n{prefix}.default\n{prefix}.help"
        
        lines = [t.to_definition_line(self.name) for t in self.tables.values()]
        return header + "\n" + "".join(lines)
    
class Tool:
    def __init__(self):
        self.prefix = "tabs"
        self.tabs: Dict[str, Tab] = {}

    def add_tab(self, tab: Tab):
        self.tabs[tab.name] = tab

    def __str__(self):
        output = ["data_"]
        
        # 1. HEADER GLOBAL (Liste des onglets)
        output.append("#")
        output.append("loop_")
        for tag in ["id", "label", "icon", "widget", "default", "parent", "help"]:
            output.append(f"_{self.prefix}.{tag}")
        
        for tab in self.tabs.values():
            output.append(tab.to_definition_line())
        
        output.append("") # Ligne vide

        # 2. DEFINITION DES ONGLETS (Liste des tables par onglet)
        for tab in self.tabs.values():
            output.append(tab.get_structure_block())

        # 3. CONTENU DES TABLES (Les JobOptions)
        for tab in self.tabs.values():
            for table in tab.tables.values():
                output.append(table.to_content_block())

        return "\n".join(output)

    # Méthodes helpers pour faciliter l'ajout comme dans votre pseudo-code
    def get_or_create_tab(self, name, label="?", icon="?"):
        if name not in self.tabs:
            self.add_tab(Tab(name, label, icon))
        return self.tabs[name]

    def get_or_create_table(self, tab_name, table_name, label="?", icon="?"):
        tab = self.tabs[tab_name] # Doit exister
        if table_name not in tab.tables:
            tab.add_table(Table(table_name, label, icon))
        return tab.tables[table_name]
    

if __name__ == '__main__' :
    table = Table('test',['a','b','c'])
    row0 = Row(a=1,b='range',c=100)
    row1 = Row(a=10,b='Movie or Image (*.{mrc,mrcs,tif,tiff,eer,mrc.bz2,mrcs.bz2,mrc.zst,mrcs.zst,mrc.xz,mrcs.xz})',c=100)
    row2 = Row(a=1,b='range',c=100)
    print(row0)
    print(str(row0))
    table.append(row0)
    table.append(row1)
    table.append(row2)
    print(table)