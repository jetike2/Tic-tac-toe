import pygame


class Marks(pygame.sprite.Sprite):
    
    def __init__(self,p):
        
        self.p = p

        super().__init__()

        if self.p == 'X':
            self.image = pygame.image.load('cross.png')

        if self.p == 'O':
            self.image = pygame.image.load('circle.png')


        self.rect = self.image.get_rect()
        
