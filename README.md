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



