# helloworld.py
# https://github.com/Deathspawn/xchat-stuff/helloworld
#
#    Example layout for a python script.
#    Copyright (C) 2012  Stryker Blue // E-mail:deathspawn989@gmail.com // Website: http://deathspawn.net/
#########################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses.
########################################################################
#
# ABOUT
#
#  This implements a new idea for making python scripts (And other scripts) inside XChat.
# Configuration files are generated and put into the respective plugin folder.
# The location of the folder can be called with "command" location.
# 
# Hopefully more scripts will follow suit after this.
#
# CHANGELOG
#
# 0.1
# Released to public.
#
# 1.0
# Cleaned up the readme. Made it easier to understand. (I hope.)
# Changed the checking method so the README can be updated and it will also update the user on load if changed.
# Changed hellofolder to configfolder so that it doesn't have to be changed for other scripts and can just be copied into them instead.
# Added conf.example generation and made it work like the README file so you can update that without harming the original config.
# Added version checks for both the README and config so that you can easily change them when you update a config.
# Changing the files will update the users on load, and the config update should alert before an error if the layout is kept the same.

# Import the necessary modules.
import xchat
import os

# Set xchat plugin info.
__module_name__ = "Hello World"
__module_version__ = "0.2"
__module_description__ = "Example layout for a python script."

# Define working directory here.
configfolder = xchat.get_info("xchatdir") + "/helloworld/"
readmefile = configfolder+"README"
configfile = configfolder+"helloworld.conf"

# Check to see if the folder exists.
if not os.path.exists(configfolder):
    # Make the folder...
    os.makedirs(configfolder)
    # Print out welcome message.
    print "=========="
    print "This is an example welcome message. It will only be shown when the configuration folder doesn't exist."
    print "This script has created a folder at "+configfolder
    print "Inside, you will find a README (Please read, it actually is worth it.) and a simple config. The config only has one option, plenty more can be added easily."
    print " "
    print "Please report any issues at the GitHub page. See /helloworld gitinfo for git info."
    # Define this so that we have an ending ======= to make it look nice.
    firstrun = True
else:
    firstrun = False

# Make or update README.
readmeversion = "1"
if os.path.exists(readmefile):
    readmeopen = open(readmefile, "r")
    readmecheck = readmeopen.readline()
    readmeopen.close()
    # Version check.
    if readmecheck != "version = "+readmeversion+"\n":
        updatereadme = True
    else:
        updatereadme = False
else:
    updatereadme = True
readmefilemake = open(readmefile, "w")
# Change the readme version number above if updating or else the user will not see changes.
readmelist = ["version = "+readmeversion+"\n",
"\n"
"This is an example script for XChat. It implements a couple new ideas within it.\n",
"The first idea is generating all necessary files within the script. While this method may seem a bit tedious to the scripter,\n",
"it lets the user be able to easily load the script and get all of the necessary files on first run.\n",
"\n",
"The second idea is making folders within the XChat directory with the respective plugin name. An author can easily change the folder\n",
"above and make their own files generate inside using this method. This prevents clutter in the XChat directory.\n",
"\n",
"This script can be kept loaded, it merely has some test commands for a general layout. You can choose to use all of it or some of it.\n",
"To the end user, this script is actually useless, but to a tester/coder, it is.\n"
"When you reload the script, it will show the help command, or you can look in \""+configfile+"\". The command can be changed on the fly which is why it cannot be listed here.\n"
"The config fille will be read within the script, but in order to change the main command you need to reload the script."
"I would hope that if you didn't use any of it that you would still take the idea into consideration and make your script easier to use."]
for i in readmelist:
    readmefilemake.write(i)
readmefilemake.close()

#check to see if config file exists. If not, create it...
# You can specify a version number and it will only modify the conf.example file.
configversion = "1"
exampleconfig = ["version = "+configversion+"\n",
"# The line above is for internal version checks. Removing it will regenerate the conf.example only. This doesn't apply to the .conf.\""
"\n"
"# This is the command that will be used to call the scripts subcommands.\n",
"# If you change this value, you must reload the script for it to take effect.\n",
"command = helloworld"]
confexamplefile = configfile+".example"
# If config doesn't exist, make it.
if not os.path.exists(configfile):
    configfilemake = open(configfile, "w")
    for i in exampleconfig:
        configfilemake.write(i)
    configfilemake.close()
# Make or update the config.conf.example
if os.path.exists(confexamplefile):
    exampleopen = open(confexamplefile, "r")
    examplecheck = exampleopen.readline()
    exampleopen.close()
    # Version check.
    if examplecheck != "version = "+configversion+"\n":
        updateconfig = True
    else:
        updateconfig = False
else:
    updateconfig = True
# Make the config example file...
examplefilemake = open(confexamplefile, "w")
for i in exampleconfig:
    examplefilemake.write(i)
examplefilemake.close()

# Alert users if the config file is updated before the script kills itself from any possible error.
if updateconfig == True:
    # Redundancy check.
    if firstrun == True:
        pass
    else:
        print "Config example has been updated. You may need to update your config! See "+confexamplefile

# Call for the main command from the config.
config = open(configfile, "r")
configlist = config.readlines()
config.close()
for i in configlist:
    if i.startswith("command") == True:
        rc = i.split(" = ")
        command = rc[1]
    else:
        pass

# The functions behind the script can go here.
# This is an example script so it doesn't have any functions.

# Internal commands can go here.
def commands(word, word_eol, userdata):
    try:
        # Sub commands can be defined this way. Prevents scripts from fighting over triggers.
        try:
            subcommand = word[1].lower()
        except IndexError:
            subcommand = None
        if subcommand == "help":
            print "This is an example help layout."
            print "=============================="
            print "/"+command+" help: Generates this help output."
            print "/"+command+" gitinfo: Outputs the git url. This can be changed to another source url."
            print "/"+command+" test: Outputs a test message."
        elif subcommand == "gitinfo":
            print "This script can be found at https://github.com/Deathspawn/xchat-stuff/helloworld"
        elif subcommand == "test":
            print "This is a test message. Testing 1, 2, 3."
        else:
            print "Error: please see \"/"+command+" help\" for help."
        return xchat.EAT_ALL
    except IndexError:          
        pass
    return xchat.EAT_NONE

# Output an unload message.
def unload(userdata):
    print __module_name__+" "+__module_version__+" unloaded."

# Print load successful messages.
print __module_name__+" "+__module_version__+" loaded."
print "For help, see \"/"+command+" help\". Also read the README!"
if updatereadme == True:
    # Redundancy check.
    if firstrun == True:
        pass
    else:
        print "README has been updated. See "+readmefile
# The firstrun seperation line.
if firstrun == True:
    print "=========="
# All the hooks.
xchat.hook_unload(unload)
xchat.hook_command(command, commands)
