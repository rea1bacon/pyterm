#__  __          _       _ _
#\ \/ /___ _ __ | | ___ (_) |_
# \  // __| '_ \| |/ _ \| | __|
# /  \\__ \ |_) | | (_) | | |_
#/_/\_\___/ .__/|_|\___/|_|\__|
#         |_|

import re
from termcolor import colored
import colorama
from exploits import *


def set_object(ob):
    global x 
    x = ob
    global init_inp
    init_inp = x.input
    for i in functions:
        ob.addc(i,functions[i][0],functions[i][1])

def use(p,a):
    if len(a[0]) > 0 :
        if a[0] in exploits:
            x.addv("current_exploit",a[0])
            z = colored(f"use:({a[0]})- ","red")
            x.input = f"{init_inp}{z}"
        else:
            print("This exploit doesn't exist : "+a[0])
    else:
        print("Please specify a module : usex \"exploit_name\"")


#function to list all the exploits
def show(p,a):
    if len(a[0]) > 0:
        c = [i for i in exploits if re.search(a[0],i)]
        d = c if len(c) > 0 else []
        print(len(d),"exploit(s) found")
        print("-" * 40)
        for i in d:
            print("-",i)
        print("-" * 40)
    else:
        print("-" * 40)
        for i in exploits:
            print("-",i)
        print("-" * 40)


#launch exploit function
def exploit(p,a):
    if type(x.retuv(['r'],["current_exploit"])) == str:
        try :
            exploits[x.retuv(['r'],["current_exploit"])]()
        except:
            print("Error while launching exploit")
            raise
    else:
        print("You need to select an exploit before running it !")


functions = {
"usex":[use,"Select the exploit to use"],
"showx":[show,"Show a list of exploits"],
"exploitx":[exploit,"Run the exploit selected"]
}

exploits = {
"sql_basic_injection":sql_simple_injection,
"freemarker_RCE":sql_simple_injection,
"subsearcher":subsearcher
}



