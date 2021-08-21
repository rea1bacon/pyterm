
    __  __          _       _ _
    \ \/ /___ _ __ | | ___ (_) |_
     \  // __| '_ \| |/ _ \| | __|
     /  \\__ \ |_) | | (_) | | |_
    /_/\_\___/ .__/|_|\___/|_|\__|
             |_|
!!!This module is under developpement!!!

# Xsploit 
Xsploit is the first released module for pyterm. It gives you a large number of functions to use pre-built exploits for pentesting ! ( Use it at your own risk )

## Doc

### Import Xsploit :

```python
import cmdline
x = cmdline.cmd()
Xsploit = x.importm("Xsploit")
Xsploit.set_object(x)
x.initsession()
```

### Commands :

#### showx

	- showx (optionnal "arg")

Display a list all/a specific exploit

#### usex

	- usex "arg"

Use the selected exploit

#### exploitx

	 - exploitx

Launch the selected exploit

#### TIP

You can keyboard interrupt while a exploit is running without quitting the cli !


