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
import globals
import random # very important
from data import *
from units import *


class World:# the snow and glacier
	def __init__(self):
		self.view_x = 0
		self.view_y =globals.SCREEN_H*19# start one screen from the bottom?
		
		self.height = globals.SCREEN_H*20 # say, ten
		
		self.part1 = load_image("glacier.png")
		
		self.buffer = pygame.Surface((globals.SCREEN_W, globals.SCREEN_H))
		self.buffer.fill((200,200,250))
		
		self.worldmap = pygame.Surface((globals.SCREEN_W, self.height))
	

		
		for i in range(20):
			self.worldmap.blit(self.part1, (0, globals.SCREEN_H*i))
		
		#for i in range(100): #config of powerups
		#	i = random.randrange(0, 15)
		#	if(i ==0):
		#		globals.powerups.append(Clip(random.randrange(1,3)))
		#pygame.draw.rect(self.worldmap, (0,0,255), (0,0,globals.SCREEN_W, globals.SCREEN_H/2), 0)
		self.worldmap.blit(load_image("sky.png"), (0, 0))
		self.worldmap.blit(load_image("ground.png"),(0, globals.SCREEN_H*19+587))
		#sounds
		self.backgroundfire = load_sound("backgroundAK-47.wav")
		self.backgroundfire.set_volume(0.5)
		
		self.wind = load_sound("wind.wav")
		self.wind.set_volume(0.5)
	def update(self, player):
		#very important, update screen first
		self.buffer = self.worldmap.subsurface((0,self.view_y,globals.SCREEN_W, globals.SCREEN_H))
		#make sure player does not go over the edge
		if(player.x_pos < 0):
			player.x_pos = 0
		elif(player.x_pos+100>globals.SCREEN_W): # 90 is the width of player sprite
			player.x_pos = globals.SCREEN_W - 100
		
		#
		if(self.view_y < 10):
			globals.gamewon = 1 # player wins the game YAY!
			globals.done = 1
		if(self.view_y < globals.SCREEN_H*10 and not globals.gave_powerup):
			globals.gave_powerup = 1
			player.load_gun.play()
			
			for i in range(3):
				player.akpouch.append(30)
				player.akpouchclips+=1
				player.handgunpouch.append(15)
				player.handgunclips +=1
		#update bullets	
		for i in globals.bullets:
			i.update()	
		#update rocks	
		for i in globals.rocks:
			i.update()
		#generate rocks?
		if(random.randrange(0, 25) == 0 and not self.view_y < 500): # 
			globals.rocks.append(Rock())
		#config	
		#SNOW!
		for i in globals.snowflakes:
			i.update()
		#generate snowflakes?	
		if(globals.snow and random.randrange(0, 3)==0 ):
			globals.snowflakes.append(Snowflake())
		
		#random sounds
		if(random.randrange(0, 250)==50): # 1/250 chance
			self.backgroundfire.play()
		if(random.randrange(0, 300) ==50): #1/300 chance 
			self.wind.play()
			
		# do the damage:
		if(globals.loop): #don't use that much resources
			for i in globals.rocks:
				if(i.y_pos+100 > player.y_pos + 39 and i.y_pos < player.y_pos+152):
					if(i.x_pos+100 > player.x_pos and i.x_pos < player.x_pos + 88):
						player.percentage -= 10
						player.rockhit.play()
						i.die()
						globals.points -= 30
		#block bullets
		if(globals.loop): #don't use that much resources
			for j in globals.rocks:
				for i in globals.bullets:
					if(i.fy+i.y > j.y_pos and i.fy+i.y < (j.y_pos+100)):
						if(i.fx+ i.x > j.x_pos and i.fx +i.x< (j.x_pos +100)):
							i.die()
							j.hits+=1
							
							
		#player gets powerups!
		
	#	for i in globals.powerups:
		
		#	if(i.x_pos > player.x_pos and i.x_pos+30 < player.x_pos):
			#	if(i.type == 1 and i.y_pos > player.y_pos and i.y_pos+ 73): #different sizes
				#	for x in i.clips:
				#		player.akpouch.append(x)
				#		i.die()
					
				#elif(i.type == 2 and i.y_pos > player.y_pos and i.y_pos +54):
				#	for x in i.clips:
				#		player.handgunpouch.append(x)
				#		i.die()
						
		if(globals.snowdeathmode):
			for i in globals.snowflakes:
				if(i.y_pos > player.y_pos+39  and i.y_pos < player.y_pos+152 ): # 39 is the head 152 is body length 88 is body width
					if(i.x_pos > player.x_pos and i.x_pos < player.x_pos + 88):
						player.percentage -=1
						i.die()
						
			for j in globals.snowflakes:
				for i in globals.bullets:
					if(not i.dead):
						if(i.fy+i.y > j.y_pos and i.fy < (j.y_pos + j.length)):
							if(i.fx+ i.x > j.x_pos and i.fx < (j.x_pos + j.length)):
								if(globals.debug):
									print "collision"
								i.die()
								j.die()
								break
		
