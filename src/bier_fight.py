import pygame

PETER_SPRITES = "../resources/Bierfechten.png"
SNAIL_SPRITES_SHOCK = "../resources/Schnecke_Schreck.png"
SNAIL_SPRITES_EAT = "../resources/Schnecke_Essen.png"
EXPLOSION_SPRITES = "resources/free-effect-bullet-impact-explosion-32x32/Yellow Effect Bullet Impact Explosion 32x32.png"

PETER_POSITION = 0.35
PETER_SCALE = 1
SNAIL_POSITION = 0.35
SNAIL_SCALE = 1
EXPLOSION_SCALE = 1
# 13 17
def init_explosion():
    sprites = pygame.image.load(PETER_SPRITES).convert_alpha()

    rect = pygame.Rect(17 * 32, 13 * 32, 32, 32)
    return sprites.subsurface(rect)

class BierFight:

    def __init__(self, screen):
        self.screen = screen

        self.explosion = init_explosion()
