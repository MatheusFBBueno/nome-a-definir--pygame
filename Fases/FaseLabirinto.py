import pygame
from Fases.player import Player
from Fases.wall import Wall

guy = pygame.image.load('images/dood.png')
camac = pygame.image.load('images/bed.png')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
LIME = (26, 242, 152)
#NADA = (255, 255, 255, 0)
marrom_bombom = (188, 100, 28)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
background = pygame.image.load("images/FaseLabirinto.png")

pygame.init()
fonte = pygame.font.Font('pokemon_fire_red.ttf', 24)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption('Test')

# lista de sprites
all_sprite_list = pygame.sprite.Group()

# paredes (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

wall = Wall(0, 0, 0, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(0, 670, 800, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(0, 0, 800, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(870, 0, 0, 670)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)



#---

wall = Wall(10, 8, 2, 584)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(11, 589, 735, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(785, 11, 2, 576)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(9, 3, 780, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(144, 362, 2, 165)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(229, 203, 2, 131)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(187, 395, 2, 99)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(101, 299, 2, 94)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(144, 75, 2, 124)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(59, 203, 2, 93)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(101, 139, 2, 96)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(144, 558, 2, 31)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(102, 461, 2, 27)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(58, 491, 2, 68)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(13, 459, 92, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(13, 331, 219, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(59, 363, 2, 68)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(59, 427, 86, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(63, 266, 167, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(146, 297, 44, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(144, 266, 2, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(60, 556, 46, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(103, 523, 88, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(102, 527, 2, 32)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(187, 526, 2, 33)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(187, 557, 92, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(188, 491, 45, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(229, 493, 2, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(13, 169, 42, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(13, 105, 93, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(60, 138, 129, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(870, 0, 2, 670)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(187, 74, 2, 67)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(59, 75, 85, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(59, 42, 2, 33)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(103, 40, 174, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(272, 42, 2, 61)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(229, 41, 2, 100)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(189, 169, 87, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(187, 173, 2, 65)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(103, 233, 86, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(147, 362, 172, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(231, 298, 216, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(400, 169, 2, 130)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(358, 138, 2, 131)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(315, 9, 2, 222)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(273, 169, 2, 101)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(275, 266, 86, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(233, 139, 81, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(315, 300, 2, 29)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(272, 333, 2, 30)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(193, 395, 82, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(229, 427, 2, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(315, 363, 2, 60)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(319, 395, 43, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(231, 461, 131, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(273, 491, 173, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(401, 462, 2, 59)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(315, 559, 2, 30)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(358, 526, 2, 30)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(230, 524, 132, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(316, 105, 46, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(357, 10, 2, 67)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(401, 10, 2, 28)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(400, 74, 2, 66)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(361, 138, 42, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(443, 106, 2, 94)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(405, 170, 40, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(405, 234, 85, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(487, 138, 2, 98)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(445, 105, 87, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(528, 41, 2, 35)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(443, 40, 88, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(444, 300, 2, 30)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(360, 331, 45, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(401, 332, 2, 31)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(359, 362, 131, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(358, 364, 2, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(402, 398, 2, 32)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(359, 429, 2, 31)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(359, 428, 44, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(400, 559, 2, 31)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(401, 557, 45, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(443, 526, 2, 33)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(445, 523, 45, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(487, 491, 2, 36)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(529, 524, 2, 66)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(487, 557, 42, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(573, 557, 44, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(488, 491, 172, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(572, 495, 2, 63)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(613, 461, 2, 36)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(657, 524, 2, 68)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(743, 525, 43, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(742, 527, 2, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(699, 558, 46, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(613, 523, 91, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(699, 493, 2, 32)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(701, 492, 44, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(742, 462, 2, 33)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(657, 461, 88, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(657, 396, 2, 65)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(661, 395, 42, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(699, 298, 2, 99)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(703, 362, 42, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(744, 396, 42, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(743, 397, 2, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(698, 427, 45, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(445, 459, 131, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(443, 430, 2, 62)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(528, 429, 2, 33)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(572, 429, 2, 32)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(573, 428, 44, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(615, 364, 2, 67)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(574, 361, 85, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(657, 138, 2, 227)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(401, 395, 176, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(487, 397, 2, 29)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(529, 300, 2, 96)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(487, 267, 2, 98)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(443, 266, 90, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(532, 331, 85, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(614, 233, 2, 102)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(745, 331, 39, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(743, 267, 2, 68)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(659, 266, 87, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(573, 203, 174, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(572, 106, 2, 193)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(698, 233, 48, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(742, 205, 2, 28)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(529, 298, 48, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(528, 106, 2, 164)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(701, 169, 84, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(742, 40, 2, 101)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(660, 137, 87, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(615, 105, 2, 62)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(699, 41, 2, 66)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(575, 105, 127, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(657, 9, 2, 62)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(573, 9, 2, 29)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(613, 40, 2, 37)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(359, 73, 258, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

#---

'''
cama = Interagivel(10, 10, 100, 100, ["time", "to", "sleep"])
camac = pygame.transform.scale(camac, (100, 100))
wall_list.add(cama)
all_sprite_list.add(cama)
cama.carregarImagem(camac)
'''
'''
textbox = Wall(10, 500, 780, 90)
textbox.image.fill(BLUE)
wall_list.add(textbox)
all_sprite_list.add(textbox)
'''

# Jogador
guyF = pygame.image.load('images/dood_frontal.png')
guyL = pygame.image.load('images/dood_left.png')
guyR = pygame.image.load('images/dood_right.png')
guyB = pygame.image.load('images/dood_back.png')
guyF = pygame.transform.scale(guyF,(100,100))
guyL = pygame.transform.scale(guyL,(100,100))
guyR = pygame.transform.scale(guyR,(100,100))
guyB = pygame.transform.scale(guyB,(100,100))

player = Player(20, 20,2,2)
guy = pygame.transform.scale(guy, (2, 2))
player.definirImagem(guyF,guyB,guyL,guyR)
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

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-2, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(2, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -2)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 2)
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
                    player.changespeed(2, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-2, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 2)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -2)
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

        keyset = [keyq, keyw, keye, keyr, keyt, keyy, keyu, keyi, keyo, keyp, keya, keyS, keyd, keyf, keyg, keyh, keyj,
                  keyk, keyl, keyz, keyx, keyc, keyv, keyb, keyn, keym, backspace, space]
        all_sprite_list.update()

        #screen.blit(background, (0, 0))
        screen.fill(WHITE)
        all_sprite_list.draw(screen)
        #textbox.image.fill(BLUE)
        pygame.display.flip()

        clock.tick(60)


fase1()

pygame.quit()