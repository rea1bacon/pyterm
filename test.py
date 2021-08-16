import cmdline

def echo(pa, ar):
		r = ""
		print(ar[0])
		#if ar[0][0] == '$':
			

def setv(pa, ar):
	if len(pa) == len(ar):
		if '' in pa :
			print("Error : You can't fill a blank name")
		else:
			for i,a in enumerate(pa):
				x.addv(a, ar[i]) 
				print(f"\"{ar[i]}\" was assigned to ${a}")
	else:
		print("Error : You must provide as many names as values")


x = cmdline.cmd(desc="This is a test v2.0", title="Terminal",name="root")
x.addc("echo",echo,desc="Print a string")
x.addc("set",setv,desc="Assign a value to a variable")
x.initsession()