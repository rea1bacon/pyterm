# Pyterm

## Easily create command line tools with python 

![image](https://user-images.githubusercontent.com/40965674/129588360-42005246-9cc9-49c1-afc3-01f376bf5ab3.png)

### Installation

```bash
    git clone https://github.com/evilcater/pyterm.git
    
    cd pyterm

    pip install -r requirements.txt
```
You also need python 3.7 to run Pyterm

### Usage

To discover the module, you can use the file test.py

```python
import cmdline
```
Pyterm is very easy to use. You just need a few lines to deploy a cli app.

```python
x = cmdline.cmd()
x.initsession()
```
You have now a interactive shell fully functionnal with some pre-built commands ready to go !

You can try them by typing 'help'

![image](https://user-images.githubusercontent.com/40965674/129593236-098540b8-53f2-4dc9-88f5-6e020cbaff06.png)

As you can see, there are 3 lines displayed for each command :

first line : the command name

second line : the function called by this command

third line : a little description

- Personalize the interface

```python
x.initsession() #has many arguments to personalize your cli !
```
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
       
```bash 
help "dump"
```
This command will only print the output for the 'dump' command

You can play around with parameters and options with the 'dumpc' command

```bash
cli$- dumpc -n "hello world" -cap
dumpcmd ['n', 'cap'] ['hello world']
```
For the moment you can only pass 2 type of options to a command (parameters beginning with a - and arguments delimited by "")

- Variables

You can set variable with command 'set'

```bash
cli$- set -var "hello"
"hello" was assigned to $var
cli$- set -var "world" -var2 "nice"
"world" was assigned to $var
"nice" was assigned to $var2
```
And dump the content with dump "var"
        
```bash
cli$- dump "var"
$var : hello
```
You can also dump the content of all variables with 'dump'

Finally you can also add variables before the program starts:

```python
x.setv("var","hello")
```
- Functions

Now we want to add new commands to our cli :

Let's add the command echo who prints a string or the content of a variable :

```python
def echo(p,a):
```
Every time you define a new function, you need to pass the options 'p' which stands for the parameter array and 'a' for arguments array.

```python
if "$" in p: #check if we want to output a variable
            for i in a:
	                x.retuv([''],[i]) #We execute the function retuv() used by the command dump
	                return 0
else:
            for i in a:
			print(i)
```
Then we add the function :

```python
x.addc("echo", echo)
```
First we define the keyword, the command that will call the function.
To the second position, we pass the function called by the command, here, echo.

You can also add a descritpion to the command :

```python
x.addc("echo",echo,desc="Print a string or a var")
```
Now we can test it by launching again the script :

```bash
cli$- echo "Hello world"
Hello world
cli$- echo "var" -$
$var : 123
```

### Import module

You can import modules with pre-built functions :
```python
import cmdline
x = cmdline.cmd()
x.importm("module_name")
x.initsession()
```

### TO-DO

- Throw more errors with description

if we write dumpc "test" 

```bash	
dumpcmd [''] [''] # <-- current output
```
Goal :

```bash
Error : while parsing argument dump "test
			            ^
```
- Ability to personnalize colors


