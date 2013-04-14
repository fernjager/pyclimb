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

def init_game(world): #set up game according to menu options
	if(globals.gameinit == 0):
		# go default on this one
		
		
		#we're done
		globals.gameinit =1
	else: #nothing to do here, moving along
		pass
	