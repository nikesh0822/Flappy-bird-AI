import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
               pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
               pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMAGES = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

class Bird:
    IMGS = BIRD_IMAGES
    # How much the bird is gonna tilt
    MAX_ROTATION = 25
    # How much we're gonna rotate on each frame every time we move the bird
    ROTATION_VEL = 20
    # How long we're gonna show each bird animation
    # larger -> flaps wings faster
    ANIMATION_TIME = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        # keeps track of when we last jumped
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        # upward -ve; right +ve
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    
    def move(self):
        self.tick_count +=1
        # how many pixels we're moving up or down this frame
        # kinda like s = ut + 0.5*a*t**2
        #TODO:
        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        #TODO: hyper-parameter?
        if d >= 16:
            d = 16
        if d < 0:
            d-=2
        
        self.y = self.y + d
        
        
    
