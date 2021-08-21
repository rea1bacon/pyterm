import cmdline, sys



def echo(p, a):
	if "$" in p: #check if we want to output a variable
		for i in a:
			x.retuv([''],[i])
			return 0
	else:
		for i in a:
			print(i)



x = cmdline.cmd()
Xsploit = x.importm("Xsploit")
Xsploit.set_object(x)
x.addc("echo",echo,desc="Print a string")
x.initsession()