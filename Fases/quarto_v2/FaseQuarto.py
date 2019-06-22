import pygame
from player import Player
from wall import Wall
from interagivel import Interagivel
from texto import inserttext


#Constantes globais
guy = pygame.image.load('dood.png')

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

img_background = pygame.image.load("quarto.png")
img_background = pygame.transform.scale(img_background,(800, 500))
background = Interagivel(0,0,800,600,[""])
background.carregarImagem(img_background)
all_sprite_list.add(background)

# Colisões

wall = Wall(0, 437, 177, 63)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(557, 291, 146, 4)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(683, 308, 20, 151)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(566, 390, 138, 69)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(269, 437, 476, 62)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(177, 481, 92, 19)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(703, 285, 97, 215)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(768, 218, 22, 67)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 0, 800, 145)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(319, 138, 128, 83)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(63, 122, 124, 64)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 124, 63, 385)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(177, 481, 92, 19)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(703, 285, 97, 215)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(768, 218, 22, 67)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 0, 800, 145)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(319, 138, 128, 83)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(63, 122, 124, 64)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(703, 138, 97, 62)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(63, 412, 60, 24)
wall_list.add(wall)
all_sprite_list.add(wall)

# Paredes das Bordas

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

# Caixa de Texto

textbox = Wall(10,500,780,90)
textbox.image.fill(BLUE) 
wall_list.add(textbox)
all_sprite_list.add(textbox)

# Jogador
player = Player(188, 378)
guy = pygame.transform.scale(guy,(75,75))
player.definirImagem(guy)
player.walls = wall_list
all_sprite_list.add(player)

clock = pygame.time.Clock()
 

def fase1():
    done = False
    keyq = False
    keyw = False
    keye = False
    keyr = False
    keyt = False
    keyy = False
    keyu = False
    keyi = False
    keyo = False
    keyp = False
    keya = False
    keyS = False
    keyd = False
    keyf = False
    keyg = False
    keyh = False
    keyj = False
    keyk = False
    keyl = False
    keyz = False
    keyx = False
    keyc = False
    keyv = False
    keyb = False
    keyn = False
    keym = False
    backspace = False   
    space = False
    chave1 = False
    chave2 = False

    # local para inserir objetos, se houver

    img_galho = pygame.image.load("galho_quarto.png")
    img_galho = pygame.transform.scale(img_galho,(60, 46))
    galho = Interagivel(63,373,60,46,[""])
    galho.carregarImagem(img_galho)
    all_sprite_list.add(galho)

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
                if event.key == pygame.K_q:
                    keyq = True
                if event.key == pygame.K_w:
                    keyw = True
                if event.key == pygame.K_e:
                    keye = True
                if event.key == pygame.K_r:
                    keyr = True
                if event.key == pygame.K_t:
                    keyt = True
                if event.key == pygame.K_y:
                    keyy = True
                if event.key == pygame.K_u:
                    keyu = True
                if event.key == pygame.K_i:
                    keyi = True
                if event.key == pygame.K_o:
                    keyo = True
                if event.key == pygame.K_p:
                    keyp = True
                if event.key == pygame.K_a:
                    keya = True
                if event.key == pygame.K_s:
                    keyS = True
                if event.key == pygame.K_d:
                    keyd = True
                if event.key == pygame.K_f:
                    keyf = True
                if event.key == pygame.K_g:
                    keyg = True
                if event.key == pygame.K_h:
                    keyh = True
                if event.key == pygame.K_j:
                    keyj = True
                if event.key == pygame.K_k:
                    keyk = True
                if event.key == pygame.K_l:
                    keyl = True
                if event.key == pygame.K_z:
                    keyz = True
                if event.key == pygame.K_x:
                    keyx = True
                if event.key == pygame.K_c:
                    keyc = True
                if event.key == pygame.K_v:
                    keyv = True
                if event.key == pygame.K_b:
                    keyb = True
                if event.key == pygame.K_n:
                    keyn = True
                if event.key == pygame.K_m:
                    keym = True
                if event.key == pygame.K_BACKSPACE:
                    backspace = True
                if event.key == pygame.K_SPACE:
                    space = True
        
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)
                if event.key == pygame.K_q:
                    keyq = False
                if event.key == pygame.K_w:
                    keyw = False
                if event.key == pygame.K_e:
                    keye = False
                if event.key == pygame.K_r:
                    keyr = False
                if event.key == pygame.K_t:
                    keyt = False
                if event.key == pygame.K_y:
                    keyy = False
                if event.key == pygame.K_u:
                    keyu = False
                if event.key == pygame.K_i:
                    keyi = False
                if event.key == pygame.K_o:
                    keyo = False
                if event.key == pygame.K_p:
                    keyp = False
                if event.key == pygame.K_a:
                    keya = False
                if event.key == pygame.K_s:
                    keyS = False
                if event.key == pygame.K_d:
                    keyd = False
                if event.key == pygame.K_f:
                    keyf = False
                if event.key == pygame.K_g:
                    keyg = False
                if event.key == pygame.K_h:
                    keyh = False
                if event.key == pygame.K_j:
                    keyj = False
                if event.key == pygame.K_k:
                    keyk = False
                if event.key == pygame.K_l:
                    keyl = False
                if event.key == pygame.K_z:
                    keyz = False
                if event.key == pygame.K_x:
                    keyx = False
                if event.key == pygame.K_c:
                    keyc = False
                if event.key == pygame.K_v:
                    keyv = False
                if event.key == pygame.K_b:
                    keyb = False
                if event.key == pygame.K_n:
                    keyn = False
                if event.key == pygame.K_m:
                    keym = False
                if event.key == pygame.K_BACKSPACE:
                    backspace = False   
                if event.key == pygame.K_SPACE:
                    space = False
        
        keyset =[keyq,keyw,keye,keyr,keyt,keyy,keyu,keyi,keyo,keyp,keya,keyS,keyd,keyf,keyg,keyh,keyj,keyk,keyl,keyz,keyx,keyc,keyv,keyb,keyn,keym,backspace,space]
        all_sprite_list.update()

        # local para inserir interações (sayhi), se houver

        screen.fill(WHITE)

        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        
        # local para inserir comandos lógicos, se houver
        
        pygame.display.flip()
    
        clock.tick(60)

fase1() 


pygame.quit()
