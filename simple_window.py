#Displays a blank window of width 800 and height 600
#
#Requires pygame 1.9.1, www.pygame.org
#Built on python 2.7.6
#Cameron Duff

import pygame

#Intialises window.
pygame.init()
pygame.display.set_mode((800,600))
running = True


#Updates display and checks for QUIT call
while running:
    
    #Updates display
    pygame.display.flip()


    #If QUIT event called, deintialises pygame, then quits.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
