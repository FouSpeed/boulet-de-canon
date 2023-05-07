import pygame
from window import *
import math
from circle import *

class Boule:
    center_balls = []

    def __init__(self, velocity, angle, surface:Window, radius, circle:Circle, x_decal = 0, y_decal = 0):
        self.radius = radius
        self.surface = surface
        self.x = surface.window_size[0]//2 + x_decal
        self.x_before = self.x
        self.angle = angle
        self.y = surface.window_size[1]//2 + y_decal
        self.y_before = self.y
        self.position = (self.x, self.y)
        self.velocity = velocity
        self.vel_x = self.velocity * math.cos(math.radians(self.angle))
        self.vel_y = -self.velocity * math.sin(math.radians(self.angle))
        self.sens = "right"
        self.circle = circle
        self.center_ball = []
        self.i_center_balls = 0
        
        
        self.variation_speed_y = 0
        self.variation_speed_x = 0
        self.clock = pygame.time.Clock()
        self.g = 9.81

    def afficher(self):
        self.calculate_new_coordinate()
        self.position = (self.x, self.y)    
        pygame.draw.circle(self.surface.screen, (255,255,255), (self.x, self.y), self.radius)
        self.x_before = self.x
        self.y_before = self.y

    
    def calculate_new_coordinate(self):

        delta_time = self.clock.tick_busy_loop(60) / 1000.0
        self.variation_speed_y = self.g * delta_time
        self.vel_y += self.variation_speed_y
        self.collision_circulaire()
        self.x += self.vel_x
        self.y += self.vel_y
        
    
    def collision_circulaire(self):
        distance_center_cercle = math.sqrt((self.circle.x-self.x)**2 + (self.circle.y - self.y)**2)

        if distance_center_cercle + self.radius >= self.circle.radius:
            if self.y - self.y_before != 0:
                alpha = (self.x_before-self.x)/(self.y_before-self.y)
                print(alpha)
            elif (self.x_before>self.x and self.y_before>self.y) or (self.x_before<self.x and self.y_before<self.y):
                alpha = 1e-7
            else:
                alpha = 1e-7

            petit_beta = math.atan2(self.y, self.x) - 1e-9
            x_near = self.circle.x + self.circle.radius * math.cos(petit_beta)
            y_near = self.circle.y + self.circle.radius * math.sin(petit_beta)

            beta = -math.atan2(self.y - y_near, self.x - x_near)

            phi = alpha - beta
            theta = alpha -  2 * phi
            self.vel_x = math.cos(theta) * 10
            self.vel_y = -math.sin(theta) *10
    
    def is_collision_ball(self):
        for i, position in enumerate(Boule.center_balls):
            distance_center_ball = math.sqrt((Boule.center_balls[i][0]-self.x)**2 + (Boule.center_balls[i][1] - self.y)**2)

            if distance_center_ball + self.radius >= self.radius and i != self.i_center_balls:
                return i
        return -1

    def collision_ball(self, all_balls:list):
        i_collision = self.is_collision_ball

        if i_collision>=0:
            alpha = (self.x_before-self.x)/(self.y_before-self.y)

            petit_beta = math.atan2(self.y, self.x) - 1e-0
            x_near = Boule.center_balls[i_collision][0] + self.radius * math.cos(petit_beta)
            y_near = Boule.center_balls[i_collision][1] + self.radius * math.sin(petit_beta)

            beta = -math.atan2(self.y - y_near, self.x - x_near)

            phi = alpha - beta
            theta = alpha -  2 * phi
            self.vel_x = math.cos(theta) * 10
            self.vel_y = -math.sin(theta) *10
