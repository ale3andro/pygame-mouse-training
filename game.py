#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit
from gameclass import GameClass

windowsize = (700,700)

def main():
    pygame.init()
    mouse0 = 'images/mouse0.png'
    mouse1 = 'images/mouse1.png'
    mouse2 = 'images/mouse2.png'
    mouse3 = 'images/mouse3.png'
    screen = pygame.display.set_mode(windowsize, DOUBLEBUF, 32)
    pygame.display.set_caption("Mouse")

    mouse_images = ( pygame.image.load(mouse0), pygame.image.load(mouse1), pygame.image.load(mouse2), pygame.image.load(mouse3))
    system_images = ( pygame.image.load('images/right.png'), pygame.image.load('images/wrong.png'))

    mygame = GameClass()
    screen.blit(mouse_images[mygame.get_item()], (0,0))

    nextItem = False

    while 1:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if (mygame.get_item() == event.button):
                    screen.blit(system_images[0], (200,200))
                    nextItem = True
                else:
                    screen.blit(system_images[1], (200, 200))

            if event.type == MOUSEBUTTONUP:
                pygame.time.wait(2000)
                if (nextItem):
                    if (mygame.get_next_item()==None):
                        pygame.quit()
                    nextItem=False
                screen.blit(mouse_images[mygame.get_item()], (0, 0))




if __name__ == "__main__":
    main()