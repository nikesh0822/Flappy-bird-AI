import pygame
import neat
import time
import os
import random

WIN_WIDTH = 500
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
        # TODO:
        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        # TODO: hyper-parameter?
        if d >= 16:
            d = 16
        if d < 0:
            d-=2

        self.y = self.y + d
        # titlting the bird
        if d < 0 or self.y < self.height + 50:
            if self.title < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROTATION_VEL

    def draw(self, win):
        self.img_count += 1
        # TODO:
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0
        # if the bird is tilting and falling down
        # choose the img which has wings levelled
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2
    
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topLeft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

def draw_window(win, bird):
    win.blit(BG_IMAGE, (0,0))
    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird(200,200)
    win = pygame.display.set_mode(WIN_WIDTH, WIN_HEIGHT)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(win, bird)
    pygame.quit()
    quit()
