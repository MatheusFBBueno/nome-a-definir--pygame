import pygame
from Seila.player import Player
from Seila.wall import Wall

guy = pygame.image.load('images/dood.png')
camac = pygame.image.load('images/bed.png')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
LIME = (26, 242, 152)
NADA = (255,255,255,0)
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

wall = Wall(10, 8, 0, 584)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(11, 589, 735, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(785, 11, 0, 576)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(9, 3, 780, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(144, 362, 0, 165)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(229, 203, 0, 131)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(187, 395, 0, 99)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(101, 299, 0, 94)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(144, 75, 0, 124)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(59, 203, 0, 93)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(101, 139, 0, 96)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(144, 558, 0, 31)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(102, 461, 0, 27)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(58, 491, 0, 68)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(13, 459, 92, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(13, 331, 219, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(59, 363, 0, 68)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(59, 427, 86, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(63, 266, 167, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(146, 297, 44, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(144, 266, 0, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(60, 556, 46, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(103, 523, 88, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(102, 527, 0, 32)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(187, 526, 0, 33)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(187, 557, 92, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(188, 491, 45, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(229, 493, 0, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(13, 169, 42, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(13, 105, 93, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(60, 138, 129, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(870, 0, 0, 670)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(187, 74, 0, 67)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(59, 75, 85, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(59, 42, 0, 33)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(103, 40, 174, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(272, 42, 0, 61)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(229, 41, 0, 100)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(189, 169, 87, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(187, 173, 0, 65)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(103, 233, 86, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(147, 362, 172, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(231, 298, 216, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(400, 169, 0, 130)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(358, 138, 0, 131)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(315, 9, 0, 222)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(273, 169, 0, 101)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(275, 266, 86, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(233, 139, 81, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(315, 300, 0, 29)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(272, 333, 0, 30)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(193, 395, 82, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(229, 427, 0, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(315, 363, 0, 60)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(319, 395, 43, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(231, 461, 131, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(273, 491, 173, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(401, 462, 0, 59)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(315, 559, 0, 30)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(358, 526, 0, 30)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(230, 524, 132, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(316, 105, 46, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(357, 10, 0, 67)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(401, 10, 0, 28)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(400, 74, 0, 66)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(361, 138, 42, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(443, 106, 0, 94)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(405, 170, 40, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(405, 234, 85, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(487, 138, 0, 98)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(445, 105, 87, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(528, 41, 0, 35)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(443, 40, 88, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(444, 300, 0, 30)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(360, 331, 45, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(401, 332, 0, 31)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(359, 362, 131, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(358, 364, 0, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(402, 398, 0, 32)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(359, 429, 0, 31)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(359, 428, 44, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(400, 559, 0, 31)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(401, 557, 45, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(443, 526, 0, 33)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(445, 523, 45, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(487, 491, 0, 36)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(529, 524, 0, 66)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(487, 557, 42, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(573, 557, 44, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(488, 491, 172, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(572, 495, 0, 63)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(613, 461, 0, 36)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(657, 524, 0, 68)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(743, 525, 43, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(742, 527, 0, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(699, 558, 46, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(613, 523, 91, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(699, 493, 0, 32)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(701, 492, 44, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(742, 462, 0, 33)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(657, 461, 88, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(657, 396, 0, 65)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(661, 395, 42, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(699, 298, 0, 99)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(703, 362, 42, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(744, 396, 42, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(743, 397, 0, 34)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(698, 427, 45, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(445, 459, 131, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(443, 430, 0, 62)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(528, 429, 0, 33)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(572, 429, 0, 32)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(573, 428, 44, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(615, 364, 0, 67)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(574, 361, 85, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(657, 138, 0, 227)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(401, 395, 176, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(487, 397, 0, 29)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(529, 300, 0, 96)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(487, 267, 0, 98)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(443, 266, 90, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(532, 331, 85, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(614, 233, 0, 102)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(745, 331, 39, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(743, 267, 0, 68)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(659, 266, 87, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(573, 203, 174, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(572, 106, 0, 193)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(698, 233, 48, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(742, 205, 0, 28)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(529, 298, 48, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(528, 106, 0, 164)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(701, 169, 84, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(742, 40, 0, 101)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(660, 137, 87, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(615, 105, 0, 62)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(699, 41, 0, 66)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(575, 105, 127, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(657, 9, 0, 62)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(573, 9, 0, 29)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(613, 40, 0, 37)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

wall = Wall(359, 73, 258, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(NADA)

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
player = Player(10, 10,5,5)
guy = pygame.transform.scale(guy, (30, 30))
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

        screen.blit(background, (0, 0))

        all_sprite_list.draw(screen)
        #textbox.image.fill(BLUE)
        pygame.display.flip()

        clock.tick(60)


fase1()

pygame.quit()