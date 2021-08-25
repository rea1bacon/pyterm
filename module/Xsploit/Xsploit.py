#__  __          _       _ _
#\ \/ /___ _ __ | | ___ (_) |_
# \  // __| '_ \| |/ _ \| | __|
# /  \\__ \ |_) | | (_) | | |_
#/_/\_\___/ .__/|_|\___/|_|\__|
#         |_|
#module for pyterm
import re
from termcolor import colored
import colorama
from exploits import *
colorama.init()

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
        c = [i for i in exploits if re.search(a[0].upper().strip(),i.upper()) or re.search(a[0].upper().strip(),exploits[i]['Description'].upper())]
        d = c if len(c) > 0 else []
        print(len(d),"exploit(s) found")
        print("-" * 40)
        for i in d:
                a = list(exploits[i].items())
                print(f"- {a[1][0]} :",colored(f"{a[1][1]}","green"))
                for p in a[2:]:
                    print(f"  {p[0]} : {p[1]}")
                print("-"*40)
    else:
        print("-" * 40)
        for i in exploits:
            a = list(exploits[i].items())
            print(f"- {a[1][0]} :",colored(f"{a[1][1]}","green"))
            for p in a[2:]:
                print(f"  {p[0]} : {p[1]}")
            print("-"*40)


#launch exploit function
def exploit(p,a):
    if type(x.retuv(['r'],["current_exploit"])) == str:
        try :
            exploits[x.retuv(['r'],["current_exploit"])]["function"](x)
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

'''Template :
,"exploit": {
'function': fun,
'name':'exploit',
'author':'auth',
'version':'0.0',
'Description':'desc'
}
'''

exploits = {
"Padding_Oracle_attack":{
"function": init_padding_attack,
"name":"Padding_Oracle_attack",
'author':'realbacon',
'version':'1.1',
'Description':'Padding oracle attack is an attack which uses the padding validation of a cryptographic message to decrypt the ciphertext'
}
,"Freemarker_RCE":{
"function": not_avail,
"name":"Freemarker_RCE",
'author':'realbacon',
'version':'0.0',
'Description':'Bad character escaping and misconfiguration lead to RCE in Freemarker Webapps'
}
,"Subsearcher":{
"function": subsearcher,
"name":"Subsearcher",
'author':'realbacon',
'version':'1.0',
'Description':'Directory buster to find hidden files and directorys'
}
,"spip_RCE": {
'function': spip_RCE,
'name':'spip_RCE',
'author':'realbacon - vuln by Laluka',
'version':'1.0',
'Description':'Vulnerability in oups parameter /ecrire/?exec=article&id_article=1&ajouter=non&tri_liste_aut=statut&deplacer=oui&_oups= leads to php code execution'
}
}
