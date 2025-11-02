import pygame

EXPLOSION_HEIGHT = 179
EXPLOSION_WIDTH = 153

PETER_SPRITES = "resources/Bierfechten.png"
SNAIL_SPRITES_SHOCK = "resources/Schnecke_Schreck.png"
SNAIL_SPRITES_EAT = "resources/Schnecke_Essen.png"
EXPLOSION_SPRITES = "resources/Explosions.png"

PETER_POSITION = 0.4
PETER_SCALE = 1
SNAIL_POSITION = 0.2
SNAIL_SCALE = 1


def init_sprite_sheets():
    explosion_sprites = pygame.image.load(EXPLOSION_SPRITES).convert_alpha()
    peter_sprites = pygame.image.load(PETER_SPRITES).convert_alpha()
    snail_eat_sprites = pygame.image.load(SNAIL_SPRITES_EAT).convert_alpha()
    snail_shock_sprites = pygame.image.load(SNAIL_SPRITES_SHOCK).convert_alpha()

    return explosion_sprites, peter_sprites, snail_eat_sprites, snail_shock_sprites


class BierFight:

    def __init__(self, screen):
        self.screen = screen

        self.center_x = screen.get_width() // 2
        self.center_y = screen.get_height() // 2

        self.explosion_sprites, self.peter_sprites, self.snail_eat_sprites, self.snail_shock_sprites = init_sprite_sheets()

        self.frame_timer = 0
        self.sprite_frame = 0

        self.explosion_frame = 0
        self.current_explosion_row = 0
        self.current_explosion_sprite = None

        self.peter_frame = 0
        self.snail_eat_frame = 0
        self.current_snail_eat_sprite = None
        self.snail_shock_frame = 0
        self.current_snail_shock_sprite = None

    def run(self):
        if self.frame_timer == 0:
            self.update_snail_eat_sprite()
            self.update_explosion_sprite()
        self.frame_timer = (self.frame_timer + 1) % 13

        self.screen.blit(self.current_snail_eat_sprite,
                         (self.center_x + self.screen.get_width() * SNAIL_POSITION,
                          self.center_y - self.current_snail_eat_sprite.get_height() / 2))
        self.screen.blit(self.current_explosion_sprite,
                         (self.center_x - self.screen.get_width() * PETER_POSITION,
                          self.center_y - self.current_explosion_sprite.get_height() / 2))

    def update_snail_eat_sprite(self):
        rect = pygame.Rect(self.snail_eat_frame * 128, 0, 128, 150)
        snail_eat_sprite = self.snail_eat_sprites.subsurface(rect)
        self.current_snail_eat_sprite = snail_eat_sprite
        self.snail_eat_frame = (self.snail_eat_frame + 1) % 3

    def show_snail_shock(self):
        pass

    def show_peter(self):
        pass

    def update_explosion_sprite(self):
        explosion_width = self.explosion_sprites.get_width() / 9
        explosion_height = self.explosion_sprites.get_height()

        rect = pygame.Rect(self.explosion_frame * explosion_width, 0, explosion_width, explosion_height)
        explosion_sprite = self.explosion_sprites.subsurface(rect)

        self.current_explosion_sprite = explosion_sprite

        self.explosion_frame = (self.explosion_frame + 1) % 9
