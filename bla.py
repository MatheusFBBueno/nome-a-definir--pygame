import pygame
from player import Player
from wall import Wall
from interagivel import Interagivel
from texto import inserttext


#Constantes globais
guy = pygame.image.load('images/dood.png')
camac = pygame.image.load('images/bed.png')

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
LIME = (26, 242, 152)
marrom_bombom = (188,100,28)

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

cama = Interagivel(10,10,100,100,["time","to","sleep"])
camac = pygame.transform.scale(camac, (100, 100))
wall_list.add(cama)
all_sprite_list.add(cama)
cama.carregarImagem(camac)

textbox = Wall(10,500,780,90)
textbox.image.fill(BLUE) 
wall_list.add(textbox)
all_sprite_list.add(textbox)

# Jogador
player = Player(100, 10)
guy = pygame.transform.scale(guy,(100,100))
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
    
    bg = pygame.image.load("images/bricks.png")
    bg = pygame.transform.scale(bg,(800,600))
    img_escova = pygame.image.load("images/toothbrush.png")
    img_escova= pygame.transform.scale(img_escova,(30,30))
    escova = Interagivel(750,350,30,30,["Uma escova de dentes","escovar os dentes?","S/N"])
    escova.carregarImagem(img_escova)
    wall_list.add(escova)
    all_sprite_list.add(escova)

    img_dinheiro = pygame.image.load("images/moni.png")
    img_dinheiro = pygame.transform.scale(img_dinheiro,(30,30))
    dinheiro= Interagivel(100,100,30,30,["Surpreendentemente, ha dinheiro no chao.","pagar suas contas?","S/N"])
    dinheiro.carregarImagem(img_dinheiro)
    wall_list.add(dinheiro)
    all_sprite_list.add(dinheiro)
    
    img_faca = pygame.image.load("images/knife.png")
    img_faca = pygame.transform.scale(img_faca,(30,30))
    faca = Interagivel(400,300,30,30,["Uma faca."])
    faca.carregarImagem(img_faca)
    wall_list.add(faca)
    all_sprite_list.add(faca)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
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
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
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
        cama.sayhi(player,textbox,fonte)
        faca.sayhi(player,textbox,fonte)

        if escova.sayhi(player,textbox,fonte) and keyset[11]==True:
            chave1 = True
        if dinheiro.sayhi(player,textbox,fonte) and keyset[11] == True:
            chave2 = True
            
        screen.fill((188,100,28))
        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        if chave1 and chave2:
            wall_list.remove(escova)
            wall_list.remove(dinheiro)
            all_sprite_list.remove(escova)
            all_sprite_list.remove(dinheiro)
            screen.fill(BLACK)
            screen.blit(fonte.render("Parabéns, voce tem higiene bucal e nao esta no SPC",True,WHITE),(250,250))
        pygame.display.flip()
    
        clock.tick(60)

fase1() 


pygame.quit()