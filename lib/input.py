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
    
import pygame
from pygame.locals import *

import globals
from units import *
#some counter variables
i = 0
j =0
k =0
waitcounter =0
machinegunning = 0 # this is different
playclick = 0
playmenuclick = 0
offclick = 0
def handle_input(world, player, screen):
	global i, j, k, waitcounter, machinegunning, playmenuclick, offclick
	
	globals.moving = 0
	if(globals.menu and globals.onmenu and not globals.ontut and not globals.onsettings):
		if(pygame.mouse.get_pos()[1]+18 > 253 and pygame.mouse.get_pos()[1]+18 < 277):
			if(pygame.mouse.get_pos()[0]+18 > 410 and pygame.mouse.get_pos()[0]+18 < 620):
				globals.selected = 1
				if(not playmenuclick):
					load_sound("click.wav").play()
					playmenuclick = 1
			else:
				globals.selected = 0
				
		elif(pygame.mouse.get_pos()[1]+18 > 353 and pygame.mouse.get_pos()[1]+18 < 378):
			if(pygame.mouse.get_pos()[0]+18 > 410 and pygame.mouse.get_pos()[0]+18 < 602):
				globals.selected = 2
				
				if(not playmenuclick):
					load_sound("click.wav").play()
					playmenuclick = 1
			
		elif(pygame.mouse.get_pos()[1]+18 > 451 and pygame.mouse.get_pos()[1]+18 < 489):
			if(pygame.mouse.get_pos()[0]+18 > 410 and pygame.mouse.get_pos()[0]+18 < 478):
				globals.selected = 3
				
				if(not playmenuclick):
					load_sound("click.wav").play()
					playmenuclick = 1
			
		else:
			globals.selected = 0
			playmenuclick = 0
			
	if(not globals.menu and not globals.donemenu and waitcounter > 2 and machinegunning and player.akpouch[player.akpouchclips] > 0): ##
		if(globals.debug):
			print "go go go"
		
		if(player.akpouch[player.akpouchclips]-1 >= 0):
			player.akpouch[player.akpouchclips] -=1
			globals.bullets.append(Bullet((player.x_pos+45, player.y_pos+90), ((pygame.mouse.get_pos()[0]+18), pygame.mouse.get_pos()[1]+18)))
			waitcounter =0
			playclick = 0
			globals.machinegunning += 1
		if(player.akpouch[player.akpouchclips]<= 0):
			machinegunning = 0
			globals.machinegunning = 0
			player.ak47.stop()
			player.click.play()
			waitcounter =0
			playclick = 1
		if(player.reloadingak and not playclick):
			player.click.play()
			playclick = 1
	# loop stuff	
	waitcounter +=1
	i+=1
	j+=1
	
	#handling mouse stuff, scrolling the screen, if the center of the cross cursor is moved within 10 pixels of the screen edge
	
	#if(pygame.mouse.get_pos()[0]+18 < 30):
		#globals.movingleft = 1
		#world.view_x = world.view_x-10
	#if(pygame.mouse.get_pos()[0]+18 > SCREEN_W - 30):
		#world.view_x= world.view_x +10
	#if(pygame.mouse.get_pos()[1]+18 < 30):
		#world.view_y = world.view_y-10
	#if(pygame.mouse.get_pos()[1]+18 > SCREEN_H - 30):
		#world.view_y= world.view_y +10	
		
	# get those keyboard keys which are  meant to be "pressed and held", i.e. held, i.e. scroll the map
	keys = pygame.key.get_pressed()
	
		
	if(not globals.menu and not globals.donemenu and not player.battlemode): # if player does not want to fight
		if keys[K_LEFT] or keys[K_a]:
			player.x_pos -= 5
			if(k>15):
				player.sidestate=2
				k=0
			if(j>20): # play some crunching sounds to signify movement
				player.move.play()
				j=0
		if keys[K_RIGHT] or keys[K_d]:
			player.x_pos+=5
			if(k>15):
				player.sidestate=1
				k=0
			if(j>20): # play some crunching sounds to signify movement
				player.move.play()
				j=0
		if keys[K_UP] or keys[K_w]:
			if(not globals.smooth and i>3):
				world.view_y = world.view_y-3# + player.akpouchclips
				globals.moving = 1
			else:
				world.view_y = world.view_y-3 # +player.akpouchclips
				globals.moving = 1
			if(i>15):
				player.movestate+=1
				i=0
			if(j>20): # play some crunching sounds to signify movement
				player.move.play()
				j=0
		
		
		#some sound
			
	#if keys[K_DOWN]: YOU CAN'T GO DOWN: "THE ONLY WAY IS UP" :D
		
	# get the keypresses "pressed and released", i.e. typing text
	for event in pygame.event.get():
		# important events first...
		if event.type == QUIT: #user wants out! 
			pygame.quit()
		elif event.type == KEYDOWN and event.key == K_ESCAPE: # quit
			if(globals.onmenu and globals.ontut):
				globals.onmenu = 1
				globals.ontut = globals.onsettings = 0
			else:
				pygame.quit()
		elif event.type == KEYDOWN and event.key == K_BACKSPACE: #special case 1
			globals.keypresses.append("BACKSPACE")
		#elif event.type == KEYDOWN and globals.menu:
		#	globals.keypresses.append(event.unicode)
		elif event.type == KEYDOWN and event.key == K_1:
			player.guntype = 1
		elif event.type == KEYDOWN and event.key == K_2:	
			player.guntype = 2
		elif event.type == KEYDOWN and event.key == K_p:#pause
			globals.menu = not globals.menu
		elif event.type == KEYDOWN and event.key == K_o:
			globals.snow = not globals.snow
		elif event.type == KEYDOWN and event.key == K_f:
			globals.fullscreen = not globals.fullscreen
			if(globals.fullscreen):
				screen = pygame.display.set_mode((globals.SCREEN_W, globals.SCREEN_H), FULLSCREEN)
			else:
				screen = pygame.display.set_mode((globals.SCREEN_W, globals.SCREEN_H))	
				
		elif event.type == KEYDOWN and event.key == K_k:	
			globals.done = 1
			globals.gamelost = 1
		
			
		
		elif event.type == MOUSEBUTTONDOWN and globals.menu and globals.onmenu:
			if(globals.selected == 1):
				globals.menu = 0
				load_sound("click.wav").play()
				globals.initing = 1
			if(globals.selected == 2):
				load_sound("click.wav").play()
				globals.ontut = 1
			if(globals.selected == 3):	
				load_sound("click.wav").play()
				pygame.quit()
		elif not globals.menu and not globals.donemenu and event.type == MOUSEBUTTONDOWN and event.button == 1 and player.battlemode: #left click to switch modes
			
			if(player.guntype == 1):
				if(not player.reloadinghg):
					if(len(player.handgunpouch) > 0): # if there's ammo left
						if(player.handgunpouch[player.handgunclips]-1 == 0  ): # last shot, 
							if(globals.debug):						
								print "last shot" 
								print player.handgunpouch
							player.handgun.play()
							player.shells.play()
							player.handgunpouch[player.handgunclips]-=1
							if(not len(player.handgunpouch)==1):#make sure it's not the last clip, before we make the reload sound
								if(globals.debug):
									print "lastshot... we need reload"
									print player.handgunpouch
								player.needreloadhg =1# to be dealt with in player.update()
								globals.bullets.append(Bullet((player.x_pos+45, player.y_pos+90), ((pygame.mouse.get_pos()[0]+18), pygame.mouse.get_pos()[1]+18)))
						elif(player.handgunpouch[player.handgunclips]-1 > 0 ): # nope
							if(globals.debug):
								print "normal"
								print player.handgunpouch
							player.handgun.play()
							player.shells.play()
							player.handgunpouch[player.handgunclips]-=1
							globals.bullets.append(Bullet((player.x_pos+45, player.y_pos+90), ((pygame.mouse.get_pos()[0]+18), pygame.mouse.get_pos()[1]+18)))
							if(globals.debug):
								print "normal end"
								print player.handgunpouch
						elif(player.handgunpouch[player.handgunclips]-1 < 0): # for those rare cases, apparently happens after all clips are exhausted
							if (globals.debug):
								print "rare case"
								print player.handgunpouch
							#player.handgunclips-=1
							#player.handgunpouch.pop()
							player.click.play()
							player.handgunpouch =[0]
							#if(player.handgunclips-1 < 0): #it's the last one, keep the zero
								
							#player.handgun.play()
							#player.shells.play()
							#player.handgunpouch[player.handgunclips]-=1
							#player.
					else:
						player.click.play()
				else:
					player.click.play()
			elif not globals.menu and not globals.donemenu and event.type == MOUSEBUTTONDOWN and event.button == 1 and player.battlemode and player.guntype ==2: #left click to switch modes
				if(not player.reloadingak):
					if(len(player.akpouch) > 0): # if there's ammo left
						if(player.akpouch[player.akpouchclips] >0  ): 
							player.ak47.play(-1) # play until player lets go
							machinegunning = 1
							
						else:
							player.click.play()
							if(not len(player.akpouch)==1): # don't reload for the last one
								player.needreloadak = 1
					else:
							player.click.play()			
		elif not globals.menu and not globals.donemenu and not globals.initing and event.type == MOUSEBUTTONUP and event.button == 1 and player.battlemode and player.guntype == 2: #left click to switch modes
			globals.machinegunning = 0
			if(globals.debug):
				print "player let go of the rocker"
				print player.akpouch
			player.ak47.stop() #stop
			waitcounter = 0
			machinegunning = 0
			if(len(player.akpouch) > 1 and player.akpouch[player.akpouchclips]<1):
				player.needreloadak = 1
			if(not player.reloadingak and len(player.akpouch)>1 and player.akpouch[player.akpouchclips]>1):
					player.shells.play() # yeah, shells drop only when you;ve fired something
							
		
		elif not globals.menu and not globals.donemenu and event.type == MOUSEBUTTONDOWN and event.button == 3: #right click to switch modes
			player.battlemode = not player.battlemode#player wants to fight, prevent him from moving
			globals.cursorvisible = not globals.cursorvisible
			if(player.battlemode):
				player.putaway.play() # player takes out gun
			else:
				player.putaway.play()
			#check if keyclicks are inside minimap
			
			
			
			#selection box
			#globals.startx, globals.starty = pygame.mouse.get_pos()
			#globals.startx +=18
			#globals.starty +=18
			
			#globals.selecting = 1
			
			

		#elif event.type == MOUSEBUTTONUP:
			
			#globals.selecting = 0
			#handle selected objects
			#pass
	
