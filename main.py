import pygame
from variable import *
from window import *
from boule import *

pygame.init()

window = Window()
boule = Boule(4, 15, window, 10)

while True:
    boule.afficher()




    window.renitialiser()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()