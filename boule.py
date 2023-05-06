import pygame
from window import *
import math

class Boule:
    def __init__(self, velocity, angle, surface:Window, radius):
        self.radius = radius
        self.surface = surface
        self.x = self.radius
        self.angle = angle
        self.y = self.surface.window_size[1]-self.radius
        self.velocity = velocity
        self.vel_x = self.velocity * math.cos(math.radians(self.angle))
        self.vel_y = -self.velocity * math.sin(math.radians(self.angle))
        
        
        self.variation_speed_y = 0.001
        self.variation_speed_x = 0
        self.clock = pygame.time.Clock()
        self.g = 9.81

    def afficher(self):
        self.calculate_new_coordinate()
        pygame.draw.circle(self.surface.screen, (255,255,255), (self.x, self.y), self.radius)
    
    def calculate_new_coordinate(self):
        delta_time = self.clock.tick_busy_loop(60) / 1000.0
        self.vel_y += self.variation_speed_y
        self.x += self.vel_x
        self.y += self.vel_y
        
        
        

