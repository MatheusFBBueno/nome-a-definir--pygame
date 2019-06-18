import pygame
from player import Player
from wall import Wall
from interagivel import Interagivel

# -- Constantes globais
guy = pygame.image.load('dood.png')
camac = pygame.image.load('bed.png')
camac = pygame.transform.scale(camac, (50, 50))

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
LIME = (26, 242, 152)
 
# tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


pygame.init()
fonte= pygame.font.Font('pokemon_fire_red.ttf',24)
 
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
pygame.display.set_caption('Test')

# lista de sprites
all_sprite_list = pygame.sprite.Group()
 
# paredes (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)


wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)
 
wall = Wall(790, 10, 10, 590)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(10, 590, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

cama = Interagivel(250,250,50,50,["time","to","sleep"])
wall_list.add(cama)
all_sprite_list.add(cama)
cama.carregarImagem(camac)

textbox = Wall(10,500,780,90)
textbox.image.fill(BLUE) 
wall_list.add(textbox)
all_sprite_list.add(textbox)

# Jogador
player = Player(50, 50)
player.definirImagem(guy)
player.walls = wall_list
all_sprite_list.add(player)

clock = pygame.time.Clock()
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
 
    all_sprite_list.update()
    cama.sayhi(player,textbox,fonte,True)
    screen.fill(LIME)
 
    all_sprite_list.draw(screen)
    textbox.image.fill(BLUE)
    pygame.display.flip()
 
    clock.tick(60)

 
pygame.quit()

