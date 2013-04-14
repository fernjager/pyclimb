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
    
'''Simple data loader module.

Loads data files from the "data" directory shipped with a game.

Enhancing this to handle caching etc. is left as an exercise for the reader.
'''

import os
import pygame
from pygame.locals import *
import globals

block1 = block2 = block3 = 0
poof = rocks = click =0
def load(filename, mode='rb'):
    '''Open a file in the data directory.

    "mode" is passed as the second arg to open().
    '''
    return open(os.path.join(data_dir, filename), mode)


def load_img(name, colorkey=None):
			
				
	fullname  = os.path.join('data', name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'Cannot load image:', fullname
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image#, image.get_rect()


# ripped from "chimp line-by-line tutorial"
def load_image(name, colorkey=None):
	global block1, block2, block3, click
	# preload stuff, once
	if(globals.firstload):
		block1 = load_img("block1.png")
		block2 = load_img("block2.png")		
		block3 = load_img("block3.png")
		globals.firstload =0
	else:
		if(name == "block1.png"):
			return block1
		elif(name == "block2.png"):
			return block2
		elif(name == "block3.png"):
			return block3
			
				
	fullname  = os.path.join('data', name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'Cannot load image:', fullname
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image#, image.get_rect()
def load_snd(name):
	class NoneSound:
		def play(self): pass
	if not pygame.mixer or not pygame.mixer.get_init():
		return NoneSound()
	fullname = os.path.join('data', name)
	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error, message:
		print 'Cannot load sound:', fullname
		raise SystemExit, message
	return sound
	
def load_sound(name):
	global rocks, poof, click
	if(globals.firstloadsnd):
		poof = load_snd("poof.wav")
		rocks = load_snd("poof.wav")
		click = load_snd("click.wav")
		globals.firstloadsnd = 0
	else:
		if(name == "poof.wav"):
			return poof
		if(name == "rocks.wav"):	
			return rocks
		if(name == "click.wav"):
			return click
			
	class NoneSound:
		def play(self): pass
	if not pygame.mixer or not pygame.mixer.get_init():
		return NoneSound()
	fullname = os.path.join('data', name)
	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error, message:
		print 'Cannot load sound:', fullname
		raise SystemExit, message
	return sound
		
