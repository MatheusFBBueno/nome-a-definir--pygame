import pygame

class Player(pygame.sprite.Sprite):

    # Constructor function
    def __init__(self, x, y):
        super().__init__()
 
        # altura, largura
        self.image = pygame.Surface([100, 100],pygame.SRCALPHA,32)
        self.image.convert_alpha()

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # vetor de velocidade
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def definirImagem(self,imagem):
        self.image.blit(imagem,(0,0))

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    def update(self):
        # mover
        self.rect.x += self.change_x
 
        # conferir se há uma parede
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
 
        # mesma coisa p/ vertical
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom