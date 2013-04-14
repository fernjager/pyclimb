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
    
import globals

def cleanup(newgame):
	globals.keypresses = []
	if(newgame):	
		globals.SCREEN_W = 1024
		globals.SCREEN_H = 768

		globals.done = 0 # not game over yet!
		globals.menu = 1 #we're in the menu
		globals.gameinit =0 #we need to set up game

		globals.gamewon =0 #nope, not yet
		globals.gamelost = 0
		globals.fullscreen = 1
		globals.smooth = 1#smooth climbing?
		globals.keypresses = [] # cleared every loop
	#gameoptions = ["Singleplayer", 0, 1, 1,] #game options, default, #gametype, timelimit, difficulty( #of enemies) spawned, weapons
		globals.snow = 1 #snow?
		globals.points = 0 # yay!
	
		globals.cursorvisible = 0
		globals.cursor = None
	
		globals.snowflakes = []
		globals.bullets = []
		globals.rocks = []
		globals.powerups = []
		globals.initing = 1
		globals.moving = 0
		globals.machinegunning = 0 # for inaccuracy purposes
	
		globals.donemenu = 0
	
		globals.snowdeathmode = 0 # :-)
		globals.firstload = 1
		globals.firstloadsnd = 1
	
		globals.debug = 0
		globals.loop = 1
		globals.gave_powerup=0
		globals.onmenu = 1
		globals.ontut = 0
		globals.onsettings = 0
		globals.selected = 0
		
			