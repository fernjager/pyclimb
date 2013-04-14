#PyClimb - "The Only Way is Up"
#Copyright (C) 2007  wegstar

#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along
#with this program; if not, write to the Free Software Foundation, Inc.,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
    

debug = 0 #debug mode?
fullscreen = 1
smooth = 1#smooth climbing?
snow = 1 #snow?


SCREEN_W = 1024
SCREEN_H = 768

done = 0 # not game over yet!
menu = 1 #we're in the menu
gameinit =0 #we need to set up game


gamewon =0 #nope, not yet
gamelost = 0
keypresses = [] # cleared every loop
#gameoptions = ["Singleplayer", 0, 1, 1,] #game options, default, #gametype, timelimit, difficulty( #of enemies) spawned, weapons

points = 0 # yay!

cursorvisible = 0
cursor = None

snowflakes = []
bullets = []
rocks = []
powerups = []
initing = 1
moving = 0
machinegunning = 0 # for inaccuracy purposes

donemenu = 0

snowdeathmode = 0 # :-)
firstload = 1
firstloadsnd = 1


loop = 1
gave_powerup=0
onmenu = 1
ontut = 0
onsettings = 0
selected = 0