#!/usr/bin/env python
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
    
    
#Import Modules
import pygame
from pygame.locals import *


import globals
from input import *
from menu import *
from init_game import *
from data import *
from cleanup import *
from world import *
from units import *


if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
    #Initialize stuff
	pygame.init()
	screen = pygame.display.set_mode((globals.SCREEN_W, globals.SCREEN_H),)# FULLSCREEN)
	pygame.display.set_caption('PyClimb')
	pygame.mouse.set_visible(0) #hide the mouse
	clock = pygame.time.Clock() #initialize clock
		
	buffer = pygame.Surface(screen.get_size()) # create our buffer
	buffer = buffer.convert()
	buffer.fill((250, 250, 250))
	

	# set up stuff
	world = ""
	player = ""
	
	textbuffer = ""
	globals.cursor = load_image("pointer.png")
	while not globals.done:
		clock.tick(60) #max out at 60 fps
	
		if(globals.menu):
			menu(screen, buffer, clock) #do the menu drawing
			
			
		
		
			
		else: 
		#	globals.loop = not globals.loop
			#init_game(world) # set up game according to gameoptions, this will only be run once
			if not globals.gameinit:
				
				intro4 = load_image("intro4.jpg")
				buffer.blit(intro4, (0,0))
				if pygame.font:
					font = pygame.font.Font(None, 70)
					text = font.render(str("Loading............."), 1, (0, 10, 10))
					buffer.blit(text, (globals.SCREEN_W/2-500,globals.SCREEN_H-75))
				
				screen.blit(buffer, (0, 0))	
				pygame.display.update()
				
				world = World()
				player = Player()
				
				globals.gameinit = 1
				globals.onmenu =0
				globals.initing = 0
			#handle input, do logic calculations, draw, and cleanup
			handle_input(world, player, screen) # handles mouse and keys	
			
			
			player.update(world)
			world.update(player)
			#fill the buffer
			buffer.fill((200, 200, 250)) # fill the buffer
			#
			#draw the world first
			buffer.blit(world.buffer, (0,0))
			
	
				
			#draw player stuff
			buffer.blit(player.image, (player.x_pos, player.y_pos))
			
			
				
			
			
	
			for i in globals.rocks:
					buffer.blit(i.image, (i.x_pos, i.y_pos))	
					
			#draw them
			
		#for i in globals.powerups:
			
			#if(i.type == 1 and i.y_pos > world.view_y):
			#	buffer.blit(i.image, (i.x_pos, i.y_pos - world.view_y))
			#	pygame.draw.circle(buffer, (0,255,255), (i.x_pos+14, i.y_pos+29), 30, 2)
			#if(i.type == 2 and i.y_pos > world.view_y):
			#	buffer.blit(i.image, (i.x_pos, i.y_pos - world.view_y ))
			#	pygame.draw.circle(buffer, (0,255,255), (i.x_pos+ 14, i.y_pos +29), 30, 2)
			
			
			for i in globals.snowflakes: # SNOW! With relativistic  effects :D
				buffer.blit(i.snowflake, (i.x_pos, i.y_pos))		
			#draw player stuff
			if(player.percentage > 0):
				buffer.blit(player.getBar(), (10, 10)) 
				pygame.draw.rect(buffer, (255,255,255), (10, 10, 300, 10), 2)
			else:
				globals.gamelost = 1
				break
			
			pygame.draw.line(buffer, (0,255,0), (globals.SCREEN_W - 20, 85), ( globals.SCREEN_W - 20, globals.SCREEN_H - 80), 8)
			length = globals.SCREEN_H-130
			x = float(world.view_y)/float(world.height)
			
			
			pygame.draw.rect(buffer,(255, 0, 0), (globals.SCREEN_W-23, int(x*length)+80, 8, 5))
						
				
			for i in globals.bullets:
				pygame.draw.line(buffer, (255, 255, 0), (i.fx+i.x, i.fy+i.y), (i.bx+i.x, i.by+i.y))
		
			#buffer.blit(load_image("enemy.png"), (100, 100))
			
			
			
			# ak ammo and gun
			if(player.guntype == 2 and not player.akpouch==[]): #he's got an AK, corrected comparison prob
				
				for i in range(player.akpouch[player.akpouchclips]):
					buffer.blit(player.akammo, (20+15*i, globals.SCREEN_H -125))
				
				buffer.blit(player.akclip, (20, globals.SCREEN_H -200))
				if pygame.font:
					font = pygame.font.Font(None, 50)
					text = font.render(" X "+str(player.akpouchclips), 1, (0, 10,10))
					
					buffer.blit(text, (45, globals.SCREEN_H -180))
			#####		
			
			# handgun ammo and gun
			if(player.guntype == 1 and not player.handgunpouch==[]): #a lowly handgun
				for i in range(player.handgunpouch[player.handgunclips]):
					buffer.blit(player.handgunammo, (20+15*i, globals.SCREEN_H -100))
				
				buffer.blit(player.m9clip, (20, globals.SCREEN_H - 160))
				if pygame.font:
					font = pygame.font.Font(None, 50)
					text = font.render(" X "+str(player.handgunclips), 1, (0, 10, 10))
					buffer.blit(text, (45, globals.SCREEN_H -150))
			#####
			
			if pygame.font:
					font = pygame.font.Font(None, 50)
					text = font.render(str(globals.points), 1, (255, 255, 255))
					buffer.blit(text, (globals.SCREEN_W-100,25))
					
			#fps
			if pygame.font:
				font = pygame.font.Font(None, 20)
				text = font.render(str(clock.get_fps()), 1, (255, 255, 255))
				textpos = text.get_rect(centerx=buffer.get_width()/2)
				buffer.blit(text, (globals.SCREEN_W/2-100,0))
			#mouse?
			if(globals.cursorvisible):
				buffer.blit(globals.cursor, pygame.mouse.get_pos())
			
		screen.blit(buffer, (0, 0))	
		pygame.display.update()
		cleanup(0) # cleanup stuff like keypresses queue
	globals.donemenu = 1	
	if(done(screen, buffer, clock)): #done
		main()
if __name__ == '__main__': main()
