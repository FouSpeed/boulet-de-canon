import pygame
from window import *
import math
from circle import *

class Boule:
    def __init__(self, velocity, angle, surface:Window, radius, circle:Circle, x_decal = 0, y_decal = 0):
        self.radius = radius
        self.surface = surface
        self.x = surface.window_size[0]//2 + x_decal
        self.x_before = self.x
        self.angle = angle
        self.y = surface.window_size[1]//2 + y_decal
        self.y_before = self.y
        self.velocity = velocity
        self.vel_x = self.velocity * math.cos(math.radians(self.angle))
        self.vel_y = -self.velocity * math.sin(math.radians(self.angle))
        self.sens = "right"
        self.circle = circle
        
        
        self.variation_speed_y = 0
        self.variation_speed_x = 0
        self.clock = pygame.time.Clock()
        self.g = 9.81

    def afficher(self):
        self.calculate_new_coordinate()
        
        pygame.draw.circle(self.surface.screen, (255,255,255), (self.x, self.y), self.radius)
        self.x_before = self.x
        self.y_before = self.y
    
    def calculate_new_coordinate(self):

        delta_time = self.clock.tick_busy_loop(60) / 1000.0
        self.variation_speed_y = self.g * delta_time
        self.vel_y += self.variation_speed_y
        self.x += self.vel_x
        self.y += self.vel_y
        self.collision_circulaire()
    
    def collision_circulaire(self):
        distance_center_cercle = math.sqrt((self.circle.x-self.x)**2 + (self.circle.y - self.y)**2)

        if distance_center_cercle + self.radius >= self.circle.radius:
            alpha = (self.x_before-self.x)/(self.y_before-self.y)

            petit_beta = math.atan2(self.y, self.x) - 0.001
            x_near = self.circle.x + self.circle.radius * math.cos(petit_beta)
            y_near = self.circle.y + self.circle.radius * math.sin(petit_beta)

            beta = -math.atan2(self.y - y_near, self.x - x_near)

            phi = alpha - beta
            theta = alpha -  2 * phi
            self.vel_x = math.cos(theta) * 10
            self.vel_y = -math.sin(theta) *10
        
