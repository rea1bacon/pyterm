#!/usr/bin/python3
#!/usr/bin/py3
import re
import datetime
import pyfiglet
import colorama
from termcolor import colored, cprint



class cmd:
	def __init__(self,title="CLI",desc="cli tool (module by @realbacon)",inp="$- ",name="cli"):
		self.cmd_dic = {}
		self.locv = {}
		self.input = str(inp)
		self.desc = str(desc) 
		self.title = str(title)
		self.name = str(name)

	def addv(self,var,con):
		self.locv[str(var)] = str(con)


	def retuv(self,p,a):
		if len(a[0]) > 0:
			var = a[0]
			if var in self.locv:
				print(f'${var} : {self.locv[var]}')
			else:
				print(f"Error : variable ${var} not found. Add it ")
		else:
			for i in self.locv:
				print(f'${i} : {self.locv[i]}')


	#Init shell
	def initsession(self):
		colorama.init()
		date = datetime.datetime.now()
		ascii_b = pyfiglet.figlet_format(self.title)
		print(ascii_b+'\n'+self.desc)
		print("Start at "+date.strftime('%Y-%m-%d %H:%M'))
		print("Type 'help' to see a list of commands")
		self.addc("help",self.printc,"List all available commands")
		self.addc("exit",self.quit,"Exit the shell")
		self.addc("dump",self.retuv,"Return the value of all/one variable")
		self.addc("dumpc",self.dumpcmd,"Return parameters and arguments")
		while True:
			cprint(self.name,'cyan',end="")
			cprint(self.input,'magenta',end="")
			c = input()
			self.executec(c)


	# function to add a command
	def addc(self,pattern : str, func, desc=False):
		if not desc:
			des = f"Execute command : {func.__name__}"
		else:
			des = desc
		self.cmd_dic[str(pattern)]= func,str(des)


	#parsing the command
	def parse(self, cmd_c):
		if len(cmd_c) == 0:
			return '','',''
		self.a = ' '.join(cmd_c.split()[1:])
		cm = [cmd_c.split()[0]]
		params = []
		args = []
		parp = re.compile(r'-[\S]+')
		argp = re.compile(r'"(?:[^"\\]|\\.)*"')
		art = re.findall(argp,self.a)
		pat = re.findall(parp,self.a)
		if pat:
			params = list(map(self.mapp,pat))
		if art:
			args = list(map(self.mapp,art))
		if len(args) == 0:
			args = [""]
		if len(params) == 0:
			params = [""]
		return cm,params,args


	#map quotes and hyphen
	def mapp(self,i):
		if i[0] == "-":
			return i[1:]
		elif i[0] == '"':
			return i[1:-1]


	#Execute the command
	def executec(self, p):
		cm,para,arg = self.parse(p)
		if cm == '':
			print('\r')
		elif cm[0]in self.cmd_dic:
			self.cmd_dic[cm[0]][0](para,arg)
		else:
			print(f"Error : Command not found '{cm[0]}'. Type help to see a list of all the commands")


	#function for help command
	def printc(self,p,a):
		if len(a[0]) > 0:
			na = a[0]
			if na  in self.cmd_dic:
				print(f"- Command : ",end="")
				cprint(na,'green')    
				print(f"   Function : {self.cmd_dic[na][0].__name__}()\n    Description : {self.cmd_dic[na][1]}")					
			else:
				print(f"Error help: Command not found '{na}'.")	
		else:
			for i in self.cmd_dic:
				print(f"- Command : ",end="")
				cprint(i,'green')
				print(f"Function : {self.cmd_dic[i][0].__name__}()\n    Description : {self.cmd_dic[i][1]}")
	
	def quit(self,p,a):
		print('Exiting shell')
		exit()


	def dumpcmd(self,p,a):
		print("dumpcmd",p,a)