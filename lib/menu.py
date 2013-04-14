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
import time

import globals
from input import *
from cleanup import *
counter = 0
stage = 0
selection = 0
playonce = 0
def menu(screen, buffer, clock):
	backgroundfire = load_snd("backgroundAK-47.wav")
	backgroundfire.set_volume(0.5)
		
	tut = load_image("tut.jpg")
	wind = load_snd("wind.wav")
	wind.set_volume(0.5)
	
	main = pygame.Surface ( (924, 668))
	main.fill ((0,0,0))
	main.set_alpha(128)
	
	
	
	global counter, stage, selection
	intro1 = load_image("intro1.jpg")
	intro2 = load_image("intro2.jpg")
	intro3 = load_image("intro3.jpg")
	intro4 = load_image("intro4.jpg")
	#rock 
	while globals.menu:
		clock.tick(60) #max out at 60 fps
		buffer.fill((200, 200, 250)) # fill the buffer
		handle_input(None,None,screen) # handles mouse and keys
		
			
		textbuffer = ""
		if pygame.font:
			font = pygame.font.Font(None, 45)
			for i in globals.keypresses:
				if(i == "BACKSPACE"):# it's a backspace :D
					textbuffer = textbuffer[:len(textbuffer)-1]
				else:
					textbuffer +=str(i)
						
		text = font.render(textbuffer, 1, (0, 10, 10))
		textpos = text.get_rect(centerx=buffer.get_width()/2)
		
		buffer.blit(text, (globals.SCREEN_W/2-100,0))
		
		if(stage == 0):
			intro4.set_alpha(counter)
			buffer.blit(intro4, (0,0))
			if(counter >= 800):
				stage = 1
				counter = 0
		if(stage == 1):
			intro2.set_alpha(counter)
			buffer.blit(intro2, (0,0))
			if(counter >= 800):
				stage = 2
				counter = 0
		if(stage == 2):
			intro3.set_alpha(counter)
			buffer.blit(intro3, (0,0))
			if(counter >= 800):
				stage = 3	
				counter = 0	
		if(stage == 3):
			intro1.set_alpha(counter)
			buffer.blit(intro1, (0,0))
			if(counter >= 800):
				stage = 0
				counter = 0
		
		if(globals.snow and random.randrange(0, 3)==0 ):
			globals.snowflakes.append(Snowflake())
		
		
		for i in globals.snowflakes:
			i.update()
		for i in globals.snowflakes: # SNOW! With relativistic  effects :D
			buffer.blit(i.snowflake, (i.x_pos, i.y_pos))		
			
		buffer.blit(main, (50, 50)) ### *** ###
		pygame.draw.rect(buffer, (0,255, 0), (50, 50, globals.SCREEN_W-100, globals.SCREEN_H-100), 1)
		
		if(globals.onmenu):
			font = pygame.font.Font(None, 75)
			text = font.render("PyClimb - \"The Only Way is Up\"", 1, (255,255, 0))
			buffer.blit(text, (125,100))
			if(globals.selected==1):
				font = pygame.font.Font(None, 50)
				text = font.render("- Play PyClimb", 1, (255,0, 0))
				buffer.blit(text, (globals.SCREEN_W/2-125,250))
			else:
				font = pygame.font.Font(None, 50)
				text = font.render("- Play PyClimb", 1, (255,255, 255))
				buffer.blit(text, (globals.SCREEN_W/2-125,250))
			if(globals.selected==2):	
				font = pygame.font.Font(None, 50)
				text = font.render("- Instructions", 1, (255, 0, 0))
				buffer.blit(text, (globals.SCREEN_W/2-125,350))
			else:
				font = pygame.font.Font(None, 50)
				text = font.render("- Instructions", 1, (255, 255, 255))
				buffer.blit(text, (globals.SCREEN_W/2-125,350))
			if(globals.selected==3):	
				font = pygame.font.Font(None, 50)
				text = font.render("- Quit", 1, (255, 0, 0))
				buffer.blit(text, (globals.SCREEN_W/2-125,450))
			else:
				font = pygame.font.Font(None, 50)
				text = font.render("- Quit", 1, (255,255, 255))
				buffer.blit(text, (globals.SCREEN_W/2-125,450))
			
		if(globals.ontut and globals.onmenu):
			buffer.blit(tut ,(0,0))
			font = pygame.font.Font(None, 30)
			text = font.render("See readme for more information...", 1, (255,0, 0))
			buffer.blit(text, (globals.SCREEN_W/2-400,450))

			font = pygame.font.Font(None, 30)
			text = font.render("Press ESC to return to menu.", 1, (255,0, 0))
			buffer.blit(text, (globals.SCREEN_W/2-400,480))

			
		if(globals.debug):
			font = pygame.font.Font(None, 50)
			text = font.render("X: "+str(pygame.mouse.get_pos()[0]+18)+" Y: "+str(pygame.mouse.get_pos()[1]+18), 1, (255, 255, 255))
			buffer.blit(text, (globals.SCREEN_W/2-175,600))
			
		#if(selection == 1):
			
		#if(selection == 2):
		#if(selection == 3):
		
		buffer.blit(globals.cursor, pygame.mouse.get_pos())
		
		#ambient sounds
		if(random.randrange(0, 250)==50): # 1/250 chance
			backgroundfire.play()
		if(random.randrange(0, 300) ==50): #1/300 chance 
			wind.play()
						
		screen.blit(buffer, (0, 0))	
		pygame.display.update()
		if(textbuffer == "done"):
			globals.menu = 0
		
		
		counter+=5	
		
def done(screen, buffer, clock):		
	global playonce
	
		
	backgroundfire = load_snd("backgroundAK-47.wav")
	backgroundfire.set_volume(0.5)
		
	tut = load_image("tut.jpg")
	wind = load_snd("wind.wav")
	wind.set_volume(0.5)
	
	scream = load_sound("fall.wav")
	win = load_sound("win.wav")
	
	main = pygame.Surface ( (924, 668))
	main.fill ((0,0,0))
	main.set_alpha(128)
	
	x = open("pyclimb_scores.txt", 'a')
	if(globals.gamewon):
		x.write(time.asctime()+" --- Win! --- "+str(globals.points)+ "\n")
	else:
		x.write(time.asctime()+" --- Lose! --- "+str(globals.points)+ "\n")
	x.close()
	
	global counter, stage, selection
	intro1 = load_image("intro1.jpg")
	intro2 = load_image("intro2.jpg")
	intro3 = load_image("intro3.jpg")
	intro4 = load_image("intro4.jpg")
	#rock 
	while globals.donemenu:
		clock.tick(60) #max out at 60 fps
		buffer.fill((200, 200, 250)) # fill the buffer
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_ESCAPE: # quit	
				pygame.quit()
			elif event.type == KEYDOWN and event.key == K_RETURN:
				
				cleanup(1)
				return 1
	
		#handle_input(None,None,screen) # handles mouse and keys
		
			
		textbuffer = ""
		if pygame.font:
			font = pygame.font.Font(None, 45)
			for i in globals.keypresses:
				if(i == "BACKSPACE"):# it's a backspace :D
					textbuffer = textbuffer[:len(textbuffer)-1]
				else:
					textbuffer +=str(i)
						
		text = font.render(textbuffer, 1, (0, 10, 10))
		textpos = text.get_rect(centerx=buffer.get_width()/2)
		
		buffer.blit(text, (globals.SCREEN_W/2-100,0))
		
		if(stage == 0):
			intro1.set_alpha(counter)
			buffer.blit(intro1, (0,0))
			if(counter >= 800):
				stage = 1
				counter = 0
		if(stage == 1):
			intro2.set_alpha(counter)
			buffer.blit(intro2, (0,0))
			if(counter >= 800):
				stage = 2
				counter = 0
		if(stage == 2):
			intro3.set_alpha(counter)
			buffer.blit(intro3, (0,0))
			if(counter >= 800):
				stage = 3	
				counter = 0	
		if(stage == 3):
			intro4.set_alpha(counter)
			buffer.blit(intro4, (0,0))
			if(counter >= 800):
				stage = 0
				counter = 0
		
		if(globals.snow and random.randrange(0, 3)==0 ):
			globals.snowflakes.append(Snowflake())
		
		
		for i in globals.snowflakes:
			i.update()
		for i in globals.snowflakes: # SNOW! With relativistic  effects :D
			buffer.blit(i.snowflake, (i.x_pos, i.y_pos))		
			
		buffer.blit(main, (50, 50)) ### *** ###
		pygame.draw.rect(buffer, (0,255, 0), (50, 50, globals.SCREEN_W-100, globals.SCREEN_H-100), 1)
		
		if(globals.gamewon):
			font = pygame.font.Font(None, 40)
			text = font.render("You've reached the top! You Win!", 1, (0,255,0))
			buffer.blit(text, (globals.SCREEN_W/2-200,100))
			if not playonce:
				win.play()
				playonce = 1
		else:
			font = pygame.font.Font(None, 40)
			text = font.render("You've Lost! Try again :-))", 1, (255,0,0))
			buffer.blit(text, (globals.SCREEN_W/2-200,100))
			if not playonce:
				scream.play()
				playonce = 1
				
		font = pygame.font.Font(None, 50)
		text = font.render("----- Final Score -----", 1, (255,255, 255))
		buffer.blit(text, (globals.SCREEN_W/2-125,130))
		if(globals.points < 0):
			font = pygame.font.Font(None, 200)
			text = font.render(str(globals.points), 1, (255,0, 0))
			buffer.blit(text, (globals.SCREEN_W/2-125,300))
		else:
			font = pygame.font.Font(None, 200)
			text = font.render(str(globals.points), 1, (0,255, 0))
			buffer.blit(text, (globals.SCREEN_W/2-125,300))	
		
		
		font = pygame.font.Font(None, 40)
		text = font.render("Press ESC to quit or Enter to go to menu...", 1, (0,255, 0))
		buffer.blit(text, (125,600))	
		
		buffer.blit(globals.cursor, pygame.mouse.get_pos())
		
		#ambient sounds
		if(random.randrange(0, 250)==50): # 1/250 chance
			backgroundfire.play()
		if(random.randrange(0, 300) ==50): #1/300 chance 
			wind.play()
						
		screen.blit(buffer, (0, 0))	
		pygame.display.update()
		
			
		counter+=5	
		
