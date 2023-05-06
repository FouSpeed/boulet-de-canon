import pygame

class Window:
    def __init__(self, window_size = (1024, 780)):

        self.window_size = window_size
        self.screen = pygame.display.set_mode(window_size)
        self.window_size = self.screen.get_size()
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("boulet de canon")

    def renitialiser(self):
        pygame.display.update()
        self.screen.fill((0, 0, 0)) 
        # ou pygame.display.flip()


    def afficher_objet(self, objet_surface, position):
        self.screen.blit(objet_surface, position)
    
    def afficher_text(self, texte: str, position, font_size = 75 , color = (0,0,0)):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(str(texte), True, color)
        self.screen.blit(text_surface, position)
