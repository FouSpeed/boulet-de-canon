import pygame
from variable import *
from window import *
from boule import *
from circle import *

pygame.init()
boules = []
center_ball = []
window = Window()
circle = Circle(window)
for i in range(1):
    boules.append(Boule(20, 200, window, 10,circle, x_decal=i))
    Boule.center_balls.append(boules[i].position)
    boules[i].i_center_balls = i
while True:
    for j,boule in enumerate(boules):
        boule.afficher()
        Boule.center_balls[j] = boule.position
    circle.afficher()



    window.renitialiser()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()