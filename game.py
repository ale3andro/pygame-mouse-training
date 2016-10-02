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

def main():
    pygame.init()
    mouse0 = 'images/mouse0.png'
    mouse1 = 'images/mouse1.png'
    mouse2 = 'images/mouse2.png'
    mouse3 = 'images/mouse3.png'
    screen = pygame.display.set_mode(windowsize, DOUBLEBUF, 32)
    pygame.display.set_caption("ale3andro's mouse training - version 0.2")

    mouse_images = ( pygame.image.load(mouse0), pygame.image.load(mouse1), pygame.image.load(mouse2), pygame.image.load(mouse3))
    system_images = ( pygame.image.load('images/right.png'), pygame.image.load('images/wrong.png'))

    rect_endGame = Rect(0,0,0,0)
    rect_playAgain = Rect(0,0,0,0)

    mygame = GameClass()
    screen.blit(mouse_images[mygame.get_item()], (0,0))

    cur_score = 0
    max_score = mygame.get_items_count()
    printScore(screen, cur_score, max_score)

    endscreenshown = False

    while 1:
        pygame.display.update()
        printScore(screen, cur_score, max_score)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if (not endscreenshown):
                    if (mygame.get_item() == event.button):
                        cur_score += 1
                        screen.blit(system_images[0], (200,200))
                    else:
                        screen.blit(system_images[1], (200, 200))

            if event.type == pygame.KEYDOWN and event.key==pygame.K_r:
                mygame.reset()
                cur_score = 0
                pygame.event.clear()
                screen.blit(mouse_images[mygame.get_item()], (0, 0))
                pygame.display.update()

            if event.type == MOUSEBUTTONUP:
                if (not endscreenshown):
                    pygame.time.wait(2000)
                    if (mygame.get_next_item()==None):
                        screen.blit(pygame.image.load('images/gameover.png'), (150, 350))
                        rect_playAgain = screen.blit(pygame.image.load('images/repeat.png'), (150, 500))
                        rect_endGame = screen.blit(pygame.image.load('images/quit.png'), (350, 500))
                        pygame.display.update()
                        endscreenshown = True
                    else:
                        screen.blit(mouse_images[mygame.get_item()], (0, 0))
                        pygame.event.clear()
                else:
                    if rect_endGame.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                    if rect_playAgain.collidepoint(event.pos):
                        endscreenshown = False
                        mygame.reset()
                        cur_score = 0
                        pygame.event.clear()
                        screen.blit(mouse_images[mygame.get_item()], (0, 0))
                        pygame.display.update()

if __name__ == "__main__":
    main()