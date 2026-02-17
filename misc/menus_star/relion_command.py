import relion_h as rh

class Node:
    def __init__(self,name,nodetype):
        self.name = name
        self.nodetype = nodetype

# class Command:
#     def __init__(self):
#       args = []
      
#     def add(self,cmnd_type,cmnd_content,cmnd_flag='?',cmnd_bool='?'):
#         if cmnd_type in ['prog','io','param','flag']:
#             args.append({'type':cmnd_type'content':cmnd_content_content,'flag': cmnd_flag,'bool':cmnd_bool})

class Prog:
    def __init__(self,progname,flag=None,boolean=None):
        self.prog = progname
        self.flag = flag
        self.value = boolean
        
    def __str__(self):
        return f'prog    {self.prog}  {self.flag} {self.value}'
    
class Arg:
    def __init__(self):
        self.out_nodes = []

    def assertion(self,type):
        self.assertion = type

    def add_outnode(self,nod):
        self.out_nodes.append(nod)

class Flag(Arg):
    def __init__(self,arg,value, flag,boolean):
        super(Flag,self).__init__()
        # arg if value == boolean
        self.type = "flag"
        self.arg = arg
        self.value = value
        self.flag = (flag,boolean)

    def __str__(self):
        argval = f'{self.arg} {{{self.value}}}' if self.value !="" else self.arg
        return f'{self.type:<7} {argval:<50} {self.flag[0]:<20} {str(self.flag[1]):<5}'

class Param(Arg):
    def __init__(self,arg,value,assertion=None):
        super(Param,self).__init__()
        self.type = "param"
        self.arg = arg
        self.value = str(value)
        self.assertion = '?' if not assertion else assertion

    def __str__(self):
        argval = f'{self.arg} {{{self.value}}}' if self.value !="" else self.arg
        return f'{self.type:<7} {argval:<50} {'?':<20} {'?':<20} {self.assertion:<30}'

class CLI:
    def __init__(self):
        self.progs = []
        self.args = []
        self.outnodes = []
        self.innodes = []

    def add_prog(self,nod):
        self.progs.append(nod)

    def add_innode(self,nod):
        self.innodes.append(nod)

    def add_outnode(self,nod):
        self.outnodes.append(nod)

    def __str__(self):
        p = '\n'.join(p.__str__() for p in self.progs)
        a = '\n'.join(a.__str__() for a in self.args)
        return p + '\n' + a

class Script:
    def __init__(self):
        self.commands = [CLI()]
        self.index = 0

    def new_command(self,i = 0):
        active = None
        if i == self.index:
            active = self.commands[self.index]
        else:
            active = self.commands.append(CLI())
            self.index = len(self.commands) - 1
        return active
    
    def __str__(self):
        table = 'loop_\n_command.index\n_command.type\n_command.arg\n_command.flag\n_command.boolean\n_command.assertion\n'
        for i,cmd in enumerate(self.commands):
            row = str(cmd).split('\n')
            row = map(lambda x: f'{i+1:<3}{x}',row)
            table += '\n'.join(row)
        return table

    
