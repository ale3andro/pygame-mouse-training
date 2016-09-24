#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit
from gameclass import GameClass

windowsize = (700,700)

def printScore(screen, cur_score, max_score):
    textfont = pygame.font.SysFont("Ubuntu", 30)
    thetext = textfont.render(u"Σκορ: " + str(cur_score) + "/" + str(max_score), True, (255, 0, 0), (255, 255, 255))
    screen.blit(thetext, (500, 40))

def gameOver(screen):
    screen.blit(pygame.image.load('images/gameover.png'), (350,350))

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

    cur_score = 0
    max_score = mygame.get_items_count()
    printScore(screen, cur_score, max_score)

    while 1:
        pygame.display.update()
        printScore(screen, cur_score, max_score)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if (mygame.get_item() == event.button):
                    cur_score += 1
                    screen.blit(system_images[0], (200,200))
                else:
                    screen.blit(system_images[1], (200, 200))

            if event.type == MOUSEBUTTONUP:
                pygame.time.wait(2000)
                if (mygame.get_next_item()==None):
                    gameOver(screen)
                    mygame.reset()
                    cur_score = 0
                    pygame.display.update()
                    pygame.time.wait(2000)
                    pygame.event.clear()
                    #pygame.quit()
                    #exit()
                screen.blit(mouse_images[mygame.get_item()], (0, 0))
                pygame.event.clear()

if __name__ == "__main__":
    main()