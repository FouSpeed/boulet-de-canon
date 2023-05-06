from window import *

class Circle:
    def __init__(self, surface:Window):
        
        self.surface = surface
        self.x = self.surface.window_size[0]//2
        self.y = self.surface.window_size[1]//2
        self.position = (self.x, self.y)
        self.radius = min(self.surface.window_size[0]//2,self.surface.window_size[1]//2)-30

    def afficher(self):
        pygame.draw.circle(self.surface.screen, (255,255,255), self.position, self.radius, 2)