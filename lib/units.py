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
from data import *
import random
import math # huh...? whassat?
waitcounter = 0

class Player: # me!
	
	def __init__(self):
			self.x_pos = int(globals.SCREEN_W/2)
			self.y_pos = int(globals.SCREEN_H/2)+50#screen scrolls with player
			
			self.movestate = 0
			self.sidestate = 0
			
			self.battlemode = 0
			self.reloadinghg = 0
			self.reloadingak = 0
			self.needreloadhg = 0
			self.needreloadak = 0
			
			self.moving = 0
			#CONFIG
			self.akpouch = [30,30, 30, 30]
			self.handgunpouch = [15,15,15, 15]
			
			self.handgunclips = len(self.handgunpouch)-1 # counting from zero
			self.akpouchclips = len(self.akpouch)-1
		
			self.handgunnoammo = 0
			self.aknoammo = 0
			self.alreadyplayedreload = 1
			
			self.image0 = load_image("player.png")
			self.image1 = load_image("player1.png")
			self.image2 = load_image("player2.png")
			self.image3 = load_image("player3.png")
			self.image4 = load_image("player4.png")
			self.image = self.image0 #default
			
			self.rockhit = load_sound("hitbyrock.wav")
			self.rockhit.set_volume(0.5)
			#healthbar
			self.width = 300
			self.height = 10
			self.percentage = 100
			
			self.guntype = 0 #none, handgun, ak
			
			self.bar = pygame.Surface((self.width, self.height)).convert()
			self.bar.fill((255, 50, 25))
			#player related images
			self.akammo = load_image("7.62mm.png")
			self.handgunammo = load_image("9mm.png")
			
			self.akclip = load_image("akclip.png")
			self.m9clip = load_image("m9clip.png")
			#player sounds
			self.move = load_sound("crunch.wav")
			self.move.set_volume(0.1)
			
			self.load_gun = load_sound("reload.wav")
			self.load_gun.set_volume(0.3)
			
			self.putaway = load_sound("putaway.wav")
			self.putaway.set_volume(0.3)
			
			self.akreload = load_sound("akreload.wav")
			self.ak47 = load_sound("AK47.WAV")
			self.shells = load_sound("gunshell.wav")
			self.handgun = load_sound("handgun.wav")
			self.handgun.set_volume(0.3)
			self.click = load_sound("click.wav")
			
	def update(self, world):
			global waitcounter
			if(self.percentage <= 0):
				globals.gamelost = 1
				if(globals.debug):
					print "you lost"
			if (self.needreloadhg and self.battlemode ): # no reloading at the same time
				if(self.guntype == 1 and self.reloadinghg ==0 ):
					if(globals.debug):
						print "reload needed:"
						print self.handgunpouch
					self.reloadinghg = 1
				if(self.guntype == 1 and self.reloadinghg == 1 and waitcounter > 150):
					self.load_gun.play()
					self.handgunclips-=1
					self.handgunpouch.pop()
					self.needreloadhg = 0
					self.reloadinghg = 0
					waitcounter = 0
			if(self.battlemode and self.needreloadak):
				if(self.guntype == 2 and self.reloadingak ==0):
					self.reloadingak = 1
					
				if(self.guntype == 2 and self.reloadingak == 1 and waitcounter > 150 ):
					self.akreload.play()
					self.akpouchclips-=1
					self.akpouch.pop()
					self.needreloadak = 0
					self.reloadingak = 0
					waitcounter = 0
			
			if(self.movestate == 0):
				self.image = self.image0
				
			if(self.movestate == 1):
				self.image = self.image1
				
			if(self.movestate == 2):
				self.image = self.image2
				
			if(self.movestate > 2):
				self.movestate =0
				
			
				
			if(self.sidestate == 1):
				self.image = self.image3
			if(self.sidestate == 2):
				self.image = self.image4
				
			waitcounter+=1
	def getBar(self):
			self.bar.fill((255, 50, 25))
		
			position = int(float(self.percentage)/float(100)*self.width)
		
			progress = pygame.Surface((position, self.height)).convert() # draw the partial bar
			progress.fill((0, 255, 0))
		
			self.bar.blit(progress, (0, 0))
			return self.bar
	def doDamage(self, percentage):
			self.percentage -= percentage
			
	def fire(self, location):
			pass
			#if(self.guntype == 2 and not self.aknoammo):
			#	self.ak47.play() special case
			#	self.shells.play()
			#	self.handpouch[self.handgunclips]-=1
			#globals.bullets 
class Enemy:
	def __init__(self, difficulty):
		
			self.image0 = load_image("enemy.png")
			self.image1 = load_image("enemy1.png")
			self.image2 = load_image("enemy2.png")
			self.image3 = load_image("enemy3.png")
			self.image4 = load_image("enemy4.png")
			self.image = self.image0 #default
			
			self.dead = 0
			
			self.movestate = 0
			self.sidestate = 0
			
			self.battlemode = 0
			self.reloading = 0
			self.needreload = 0
			
			self.moving = 0
			#CONFIG NUMBER OF BULLETS
			if(difficulty == 2):
				self.akpouch = [25,25,25]
				self.handgunpouch = [7]
			if(difficulty == 1):
				self.handgunpouch = [7,7,7,7,7]
				self.akpouch = []
			self.handgunclips = len(self.handgunpouch)-1 # counting from zero
			self.akpouchclips = len(self.akpouch)-1
		
			self.handgunnoammo = 0
			self.aknoammo = 0
			self.alreadyplayedreload = 1
			#healthbar
			self.width = 300
			self.height = 10
			self.percentage = 100
			
			self.guntype = 0 #none, handgun, ak
			
			self.bar = pygame.Surface((self.width, self.height)).convert()
			self.bar.fill((255, 50, 25))
			#player related images
			self.akammo = load_image("7.62mm.png")
			self.handgunammo = load_image("9mm.png")
			
			self.akclip = load_image("akclip.png")
			self.m9clip = load_image("m9clip.png")
			#player sounds
			self.move = load_sound("crunch.wav")
			self.move.set_volume(0.1)
			
			self.load_gun = load_sound("reload.wav")
			self.load_gun.set_volume(0.3)
			
			self.putaway = load_sound("putaway.wav")
			self.putaway.set_volume(0.3)
			
			self.akreload = load_sound("akreload.wav")
			self.ak47 = load_sound("AK47.WAV")
			self.shells = load_sound("gunshell.wav")
			self.handgun = load_sound("handgun.wav")
			self.handgun.set_volume(0.3)
			self.click = load_sound("click.wav")
					
class Rock: #rocks
	def __init__(self):
		block1 = load_image("block1.png")
		block2 = load_image("block2.png")
		block3 = load_image("block3.png")
		self.image = pygame.Surface((101,101))

		self.hits = 0 # CONFIG HITS TO KILL ROCK
		self.image = pygame.transform.rotate(random.choice((block1, block2, block3)), random.choice(( -3, -2,-1,1,2, 3))*90)
		
		self.x_pos = random.randrange(0, globals.SCREEN_W)
		self.y_pos = 0
		
		self.sound = load_sound("rocks.wav")
		self.sound.set_volume(0.3)
		self.sound.play()
		self.poof = load_sound("poof.wav")
		self.poof.set_volume(0.7)
	def update(self):
		if(self.hits > 3): #config	
			self.poof.play()
			self.die()
			globals.points +=15 # five points for getting a rock YAY!
		elif(self.y_pos < globals.SCREEN_H): 
			if(globals.moving):
				self.y_pos = 8+ 3 + self.y_pos#CONFIG SPEED player's and the rock's
			else:
				self.y_pos +=8
		else:
			self.die()
	def die(self):
		globals.rocks.remove(self)
		globals.points+=10
		del self
		
class Bullet: #oh yeah, 
	def __init__(self, source, destination):
		#config
		
		self.bulletspeed = 100
		self.bulletlast = 100# it'll die out by itself
		self.bulletlength = 20
		#you can't be _that_ accurate :P, imagine shooting while hanging on a cliff
		randomnization1 = random.randrange(0,10) 
		randomnization2 = random.randrange(0,10)
		
		if(globals.machinegunning ): #the longer you fire, the more innacurate you get- hey, you're firing an AK one-handed anyway
			randomnization1 = random.randrange(0,6*globals.machinegunning) 
			randomnization2 = random.randrange(0,6*globals.machinegunning)
			if(globals.debug):
				print "inaccurate"
		sign = random.randrange(-1, 2)# inaccurate left and right
		self.finaldestination = (destination[0]+randomnization1*sign, destination[1] + randomnization2*sign)
		self.dead = 0
		
		# THE MATH -> Step 1: find the distance between the source and destination in both x and y to derive an angle
		distance_x = source[0] - self.finaldestination[0]
		distance_y = source[1] - self.finaldestination[1]
		# Step 2: derive angle :D
		self.theta = math.atan2(float(distance_y),float(distance_x))+math.pi # wrong way, rotate it around
		#step 3: determine length in x and length in y
		length_x = self.bulletlength*math.cos(self.theta)
		length_y = self.bulletlength*math.sin(self.theta)
		
		self.fx = length_x + source[0] # front x
		self.fy = length_y + source[1] # front y
		self.bx = source[0] # back x (original)
		self.by = source[1]	# back y (original)
		self.distance = 0
		
		self.x = 0
		self.y = 0
	def update(self):
		
			
		if(self.distance > self.bulletlast):
			self.die()
		else:
			self.x += math.cos(self.theta)*self.bulletspeed
			self.y += math.sin(self.theta)*self.bulletspeed
			
			self.distance+=1		
	def die(self): # self destruct, bye bye
			self.dead = 1
			globals.bullets.remove(self)
			del self
			

class Clip: # items floating around
	def __init__(self, type):
		self.type = type #ak or hg?
		self.clips = []
		#self.surface
		if(self.type == 1):
			self.image = load_image("akclip.png")
			self.clips = [25]
			#30,73
		if(self.type == 2):
			self.image = load_image("m9clip.png")	
			self.clips = [7]
			#28,54
		self.y_pos = random.randrange(0, globals.SCREEN_H*19)
		self.x_pos = random.randrange(0, globals.SCREEN_W)
	def update(self):	
		pass
	def die(self):
		globals.powerups.remove(self)
		del self
class Snowflake: #You betcha
	def __init__(self):
		self.length = random.randrange(2, 7) # config size
		self.snowflake = pygame.Surface((self.length, self.length))
		self.snowflake = pygame.transform.rotate(self.snowflake, random.randrange(0, 360))	
		self.snowflake.fill((255,255,255))
		self.x_pos = random.randrange(0, globals.SCREEN_W)
		self.y_pos = 0
		
	def update(self):
		if(self.y_pos < globals.SCREEN_H and not globals.moving):
			self.y_pos += 4
		elif(self.y_pos < globals.SCREEN_H and globals.moving):
			self.y_pos = 4 + 3 + self.y_pos # CONFIG PLAYER SPPED (3)
		else:
			globals.snowflakes.remove(self)
			del self
	def die(self):
			globals.snowflakes.remove(self)
			del self
