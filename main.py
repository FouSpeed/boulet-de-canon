import pygame
from variable import *
from window import *
from boule import *
from circle import *

pygame.init()
boules = []
window = Window()
circle = Circle(window)
for i in range(10):
    boules.append(Boule(10, 5, window, 10,circle, x_decal=i))
while True:
    for boule in boules:
        boule.afficher()
    circle.afficher()



    window.renitialiser()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()