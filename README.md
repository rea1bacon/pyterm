# Pyterm

## Easily create command line tools with python 

![image](https://user-images.githubusercontent.com/40965674/129588360-42005246-9cc9-49c1-afc3-01f376bf5ab3.png)

### Installation

    git clone https://github.com/evilcater/pyterm.git

    pip install -r requirements.txt

You also need python 3.10 to run Pyterm

### Usage

    import cmdline

Pyterm is very easy to use. You just need a few lines to deploy a cli app.

    cmd = cmdline.cmd()
    x.initsession()

You have now a interactive shell fully functionnal with some pre-built commands ready to go !

You can try them by typing 'help'

![image](https://user-images.githubusercontent.com/40965674/129593236-098540b8-53f2-4dc9-88f5-6e020cbaff06.png)

As you can see, there are 3 lines displayed for each command :

first line : the command name

second line : the function called by this command

third line : a little description

- Personalize the interface

        x.initsession() 
        has many arguments to personalize your cli !

##### title

The ascii art string 

##### desc

The description displayed when you start the cli 

##### inp

The sign after the hostname

##### name

The hostname

##### To-do

Edit the colors

Feel free to play around with those options

- How it works ?

After you write the command, you can pass parameter (-parameter) and arguments ("argument") 

Try to type 
        
        help "dump"

This command will only print the output for the 'dump' command

You can play around with parameters and options with the 'dumpc' command

        cli$- dumpc -n "hello world" -cap
        dumpcmd ['n', 'cap'] ['hello world']
        
For the moment you can only pass 2 type of options to a command (parameters beginning with a - and arguments delimited by "")

- Variables

You can set variable with command 'set'

        cli$- set -var "hello"
        "hello" was assigned to $var
        cli$- set -var "world" -var2 "nice"
        "world" was assigned to $var
        "nice" was assigned to $var2
        
And dump the content with dump "var"
        
        cli$- dump "var"
        $var : hello
        
You can also dump the content of all variables with 'dump'

Finally you can also add variables before the program starts:

        x.setv("var","hello")

- Functions

Now we want to add new commands to our cli :

Let's add the command echo who prints a string or the content of a variable :

        def echo(p,a):
      
Every time you define a new function, you need to pass the options p which stand for the parameter array and a for arguments array.

       if "$" in p: #check if we want to output a variable
		for i in a:
			x.retuv([''],[i]) #We execute the function retuv() used by the command dump
			return 0
	    else:
		    for i in a:
			    print(i)
       


