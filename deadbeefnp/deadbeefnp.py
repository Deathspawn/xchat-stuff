# deadbeefnp.py
# https://github.com/Deathspawn
#
#    Script to control deadbeef media player with XChat
#    Copyright (C) 2011  Stryker Blue // E-mail:deathspawn989@gmail.com // Website: http://deathspawn.net/
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
# This script was made to work with deadbeef 0.5.1 and XChat 2.8.8, however, other versions may work with it. Use at your own risk, etc.
#
# CHANGELOG
#
# 1.0
# Initial version. Made for personal use.
#
# 1.0p
# Public release. Stripped down personal modding, etc.
# Features the terminal switches.
# (Yeah, most of it is taking the terminal switches and playing with them, but it adds convenience, which is the main goal.)
#
# 1.1
# Added an echo flag for the now playing, and changed version to output in the channel unless the echo flag is applied.
# Moved the version display to the config so you can take it out easier.
# Other minor edits.
#
# 1.1g
# Uploaded to Github. Nothing else special.
#
#TODO: Make a config file instead of editing the config at the top of the script and reloading all the time.
#TODO: Make the script add now playing buttons. Don't expect this though...

# import the necessary modules.
import xchat
import commands
import time

# Set the XChat stuff so your plugin shows up fancy.
__module_name__ = "deadbeefnp"
__module_description__ = "DeaDBeeF control and now playing script."
__module_version__ = "1.1g"

dbver = commands.getoutput('deadbeef --version').split("\n")
longversion = dbver[1]
dbver2 = dbver[1].split(" ")
version = dbver2[1]

#############################################
###   CONFIGURATION   #######################
#############################################

# Here, you can change how your script will output for the nowplaying commands.
# See http://sourceforge.net/apps/mediawiki/deadbeef/index.php?title=Title_Formatting for a list of variables.
#
# If you want to display the version, include it with +version+
# config display = "np whatever"+version+"anything else"
# Version displays in numbers, e.g. 0.5.1

config_display = "12NP: 07[12%a 07- 12%t07] [12%b07] [12%e07/12%l07] [12%@:bitrate@kbps07] DeaDBeeF "+version
config_display_no_color = "NP: [%a - %t] [%b] [%e/%l] [%@:bitrate@kbps] DeaDBeeF "+version
config_display_not_playing = "hit the now playing button when DeaDBeeF wasn't playing anything."
config_display_player_off = "hit the now playing button when DeaDBeeF was off."

# This is the command to use when displaying songs. Either SAY or ACTION.
# You can use something different if you desperately want to. The second
# command is only used if you did the command while deadbeef wasn't playing.
config_command = "SAY"
config_command_nt = "ACTION"

# Below are the two commands you can use to call the script. You can use one or the other
# or both, it is your choice. Do not leave these blank.
longcommand = "deadbeef"
shortcommand = "dbnp"

#############################################
###   END OF CONFIGURATION   ################
#############################################

def deadbeefcafe(word, word_eol, userdata):
    try:
        try:
            secondcommand = word[1].lower()
        except IndexError:
            secondcommand = None
        if secondcommand == None:
            stuff = commands.getoutput('deadbeef --nowplaying \"'+config_display+'\"').lstrip("starting deadbeef").split("\n")
            songinfo = stuff[1]
            if songinfo == "server_start":
                xchat.command(config_command_nt+" "+config_display_player_off)
            elif songinfo == "nothing":
                xchat.command(config_command_nt+" "+config_display_not_playing)
            else:
                xchat.command(config_command + " " + songinfo + "")
        elif secondcommand == "echo":
            stuff = commands.getoutput('deadbeef --nowplaying \"'+config_display+'\"').lstrip("starting deadbeef").split("\n")
            stuff2 = commands.getoutput('deadbeef --nowplaying \"'+config_display_no_color+'\"').lstrip("starting deadbeef").split("\n")
            songinfo = stuff[1]
            songinfo2 = stuff2[1]
            print "Not playing: /"+config_command_nt+" "+config_display_not_playing
            print "Player off: /"+config_command_nt+" "+config_display_player_off
            print "Color: /"+config_command + " " + songinfo + ""
            print "No Color: /"+config_command + " " + songinfo2
        elif secondcommand == "nc":
            stuff = commands.getoutput('deadbeef --nowplaying \"'+config_display_no_color+'\"').lstrip("starting deadbeef").split("\n")
            songinfo = stuff[1]
            if songinfo == "server_start":
                xchat.command(config_command_nt+" "+config_display_player_off)
            elif songinfo == "nothing":
                xchat.command(config_command_nt+" "+config_display_not_playing)
            else:
                xchat.command(config_command + " " + songinfo)
        elif secondcommand == "next":
            commands.getoutput('deadbeef --next')
            time.sleep(0.5) #For some damn reason, if I do the nowplaying immediately, it shows the previous track... >.>
            stuff = commands.getoutput('deadbeef --nowplaying \"%a - %t\"').lstrip("starting deadbeef").split("\n")
            songinfo = stuff[1]
            print "Now playing: "+songinfo
        elif secondcommand == "prev":
            commands.getoutput('deadbeef --prev')
            time.sleep(0.5)
            stuff = commands.getoutput('deadbeef --nowplaying \"%a - %t\"').lstrip("starting deadbeef").split("\n")
            songinfo = stuff[1]
            print "Now playing: "+songinfo
        elif secondcommand == "random":
            commands.getoutput('deadbeef --random')
            time.sleep(0.5)
            stuff = commands.getoutput('deadbeef --nowplaying \"%a - %t\"').lstrip("starting deadbeef").split("\n")
            songinfo = stuff[1]
            print "Now playing: "+songinfo
        elif secondcommand == "play":
            commands.getoutput('deadbeef --play')
            time.sleep(0.5)
            stuff = commands.getoutput('deadbeef --nowplaying \"%a - %t\"').lstrip("starting deadbeef").split("\n")
            songinfo = stuff[1]
            print "Now playing: "+songinfo
        elif secondcommand == "pause":
            commands.getoutput('deadbeef --pause')
        elif secondcommand == "stop":
            commands.getoutput('deadbeef --stop')
        elif secondcommand == "version":
            try:
                thirdcommand = word[2].lower()
            except IndexError:
                thirdcommand = None
            if thirdcommand == None:
                print longversion
            elif thirdcommand == "output":
                xchat.command("SAY "+longversion)
            else:
                print "Error: please see \"/"+longcommand+" help\" for help."
        elif secondcommand == "quit":
            commands.getoutput('deadbeef --quit')
        elif secondcommand == "help":
            print "DeaDBeeF Control & Now playing script v"+__module_version__
            print "============================================"
            print "Any of these commands may be used with /"+longcommand+" or /"+shortcommand
            print "/"+longcommand+" will be used in this help output."
            print " "
            print "/"+longcommand+" - shows the now playing info in color as specified in configuration."
            print "/"+longcommand+" echo - prints the now playing info to the client showing both color and no color."
            print "/"+longcommand+" nc - shows the now playing info without color."
            print "/"+longcommand+" play - plays the song if the player is stopped and shows the name."
            print "/"+longcommand+" pause - pauses the track."
            print "/"+longcommand+" stop - stops the track from playing."
            print "/"+longcommand+" next - switches to the next song and prints the name."
            print "/"+longcommand+" prev - switches to the previous song and prints the name."
            print "/"+longcommand+" random - switches to a random song in the playlist and prints the name."
            print "/"+longcommand+" version [output] - prints out the version of the player. (output sends this to chat.)"
            print "/"+longcommand+" quit - exits DeaDBeeF"
        else:
            print "Error: please see \"/"+longcommand+" help\" for help."
        return xchat.EAT_ALL
    except IndexError:          
        pass
    return xchat.EAT_NONE

def unload(userdata):
     print "deadbeefnp "+__module_version__+" unloaded."

print "deadbeefnp "+__module_version__+" loaded. See \"/"+longcommand+" help\" for commands."
xchat.hook_unload(unload)
xchat.hook_command(longcommand, deadbeefcafe)
xchat.hook_command(shortcommand, deadbeefcafe)
