#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit

windowsize = (700,700)

def main():
    pygame.init()
    mouse0 = 'images/mouse0.png'
    mouse1 = 'images/mouse1.png'
    mouse2 = 'images/mouse2.png'
    mouse3 = 'images/mouse3.png'
    screen = pygame.display.set_mode(windowsize, DOUBLEBUF, 32)
    pygame.display.set_caption("Mouse")

    textfont = pygame.font.SysFont("Ubuntu", 20)
    thetexts = (textfont.render(u"Αριστερό πλήκτρο", True, (255,0,0), (255,255,0)),
                    textfont.render(u"Μεσαίο πλήκτρο", True, (255,0,0), (255,255,0)),
                    textfont.render(u"Δεξί πλήκτρο", True, (255, 0, 0), (255, 255, 0)))
    systemMessages = (textfont.render(u"Μπράβο", True, (255,0,0), (255,255,0)),
                      textfont.render(u"Δοκίμασε πάλι", True, (255, 0, 0), (255, 255, 0)))

    mouse_0 = pygame.image.load(mouse0)
    mouse_1 = pygame.image.load(mouse1)
    mouse_2 = pygame.image.load(mouse2)
    mouse_3 = pygame.image.load(mouse3)

    sequence1 = (1, 1, 1, 2, 3, 2, 1, 3, 2, 1, 2, 2, 3)
    sequence1_index = 0
    item_cur = sequence1[sequence1_index]
    sequence1_length = len(sequence1)

    next_item = False

    screen.blit(mouse_0, (0, 0))
    screen.blit(thetexts[item_cur-1], (100,100))

    while 1:
        pygame.display.update()

        if next_item:
            sequence1_index = sequence1_index + 1
            if (sequence1_index==sequence1_length-1):
                pygame.quit()
                exit()
            else:
                item_cur = sequence1[sequence1_index]
                next_item = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    screen.blit(mouse_1, (0,0))
                elif event.button == 3:
                    screen.blit(mouse_2, (0,0))
                elif event.button == 2:
                    screen.blit(mouse_3, (0,0))
                if (item_cur == event.button):
                    screen.blit(systemMessages[0], (100, 400))
                    pygame.display.update()
                    pygame.time.wait(2000)
                    next_item = True
                else:
                    screen.blit(systemMessages[1], (100, 400))
                    pygame.display.update()
                    pygame.time.wait(2000)


            if event.type == MOUSEBUTTONUP:
                screen.blit(mouse_0, (0, 0))
                screen.blit(thetexts[item_cur - 1], (100, 100))

if __name__ == "__main__":
    main()