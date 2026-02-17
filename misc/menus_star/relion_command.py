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
    def __init__(self,progname,flag,boolean):
        self.prog = progname
        self.flag = flag
        self.value = boolean
        
        
class Arg:
    def __init__(self):
        self.out_nodes = []

    def assertion(self,type):
        self.assertion = type

    def add_outnode(nod):
        self.out_nodes.append(nod)

class Flag(Arg):
    def __init__(self,type,arg,value, flag,boolean):
        super(self,Flag).__init__()
        # arg if value == boolean
        self.arg = arg
        self.value = value
        self.flag = (flag,boolean)

class Param(Arg):
    def __init__(self,type,arg,value,assertion=None):
        super(self,Param).__init__()
        self.arg = arg
        self.value = str(value)
        self.assertion = assertion

class CLI:
    def __init__(self):
        self.progs: []
        self.args: []
        self.outnodes = []
        self.innodes = []

    def add_prog(self,nod):
        self.progs.append(nod)

    def add_innode(self,nod):
        self.innodes.append(nod)

    def add_outnode(self,nod):
        self.outnodes.append(nod)

class Script:
    def __init__(self):
        self.commands = [CLI()]
        self.index = 0

    def new_command(self,i = 0):
        active = None
        if i == self.index:
            active = self.commands[self.level]
        else:
            active = self.commands.append(CLI())
            self.index = len(self.commands) - 1
        return active

    
