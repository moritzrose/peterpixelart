import pygame

EXPLOSION_HEIGHT = 179
EXPLOSION_WIDTH = 153

PETER_SPRITES = "resources/Bierfechten.png"
SNAIL_SPRITES_SHOCK = "resources/Schnecke_Schreck.png"
SNAIL_SPRITES_EAT = "resources/Schnecke_Essen.png"
EXPLOSION_SPRITES = "resources/Explosions.png"

PETER_POSITION = 0.1
PETER_SCALE = 1
SNAIL_POSITION = 0.1
SNAIL_SCALE = 1


def init_sprite_sheets():
    explosion_sprites = pygame.image.load(EXPLOSION_SPRITES).convert_alpha()
    peter_sprites = pygame.image.load(PETER_SPRITES).convert_alpha()
    snail_eat_sprites = pygame.image.load(SNAIL_SPRITES_EAT).convert_alpha()
    snail_shock_sprites = pygame.image.load(SNAIL_SPRITES_SHOCK).convert_alpha()

    return explosion_sprites, peter_sprites, snail_eat_sprites, snail_shock_sprites


class BierFight:

    def __init__(self, screen):
        self.snail_blink_counter = 0
        self.explosion_y = None
        self.explosion_x = None
        self.screen = screen

        self.center_x = screen.get_width() // 2
        self.center_y = screen.get_height() // 2

        self.explosion_sprites, self.bierfight_sprites, self.snail_eat_sprites, self.snail_shock_sprites = init_sprite_sheets()

        self.sprite_frame = 0

        self.explosion_frame = 0
        self.current_explosion_row = 0
        self.current_explosion_sprite = None

        self.bierfight_frame = 0
        self.current_bierfight_sprite = None

        self.snail_eat_frame = 0
        self.current_snail_eat_sprite = None
        self.snail_shock_frame = 1
        self.current_snail_shock_sprite = None

    def run(self):
        self.sprite_frame = (self.sprite_frame + 1) % 51

        if self.sprite_frame > 20:
            self.show_bierfight()
        if self.sprite_frame < 30:
            self.show_snail_eat()
        else:
            self.show_snail_shock()
        if 18 <= self.sprite_frame < 27:
            self.show_explosion()


    def show_explosion(self):
        self.update_explosion_sprite()

        explosion_x = self.center_x - self.current_explosion_sprite.get_width() / 2 - self.screen.get_width() * PETER_POSITION
        explosion_y = self.center_y - self.current_explosion_sprite.get_height() / 2

        self.screen.blit(self.current_explosion_sprite,
                         (explosion_x,
                          explosion_y))

    def show_snail_eat(self):
        self.snail_shock_frame = 0
        self.update_snail_eat_sprite()
        self.screen.blit(self.current_snail_eat_sprite,
                         (self.center_x + self.screen.get_width() * SNAIL_POSITION,
                          self.center_y - self.current_snail_eat_sprite.get_height() / 2))

    def update_snail_eat_sprite(self):
        rect = pygame.Rect(self.snail_eat_frame * 128, 0, 128, 150)
        snail_eat_sprite = self.snail_eat_sprites.subsurface(rect)
        self.current_snail_eat_sprite = snail_eat_sprite
        self.snail_eat_frame = (self.snail_eat_frame + 1) % 3

    def show_snail_shock(self):
        self.update_snail_shock_sprite()
        self.screen.blit(self.current_snail_shock_sprite,
                         (self.center_x + self.screen.get_width() * SNAIL_POSITION,
                          self.center_y - self.current_snail_shock_sprite.get_height() / 2))

    def show_bierfight(self):
        self.update_bierfight_sprite()
        bierfight_x = self.center_x - self.current_bierfight_sprite.get_width() / 2 - self.screen.get_width() * PETER_POSITION
        bierfight_y = self.center_y - self.current_bierfight_sprite.get_height() / 2

        self.screen.blit(self.current_bierfight_sprite,
                         (bierfight_x, bierfight_y))

    def update_bierfight_sprite(self):
        peter_width = self.bierfight_sprites.get_width() / 6
        peter_height = self.bierfight_sprites.get_height()
        rect = pygame.Rect(self.bierfight_frame * peter_width, 0, peter_width, peter_height)
        bierfight_sprite = self.bierfight_sprites.subsurface(rect)
        self.current_bierfight_sprite = bierfight_sprite
        self.bierfight_frame = (self.bierfight_frame + 1) % 6

    def update_explosion_sprite(self):
        explosion_width = self.explosion_sprites.get_width() / 9
        explosion_height = self.explosion_sprites.get_height()

        rect = pygame.Rect(self.explosion_frame * explosion_width, 0, explosion_width, explosion_height)
        explosion_sprite = self.explosion_sprites.subsurface(rect)

        self.current_explosion_sprite = explosion_sprite

        self.explosion_frame = (self.explosion_frame + 1) % 9

    def update_snail_shock_sprite(self):
        rect = pygame.Rect(self.snail_shock_frame * 128, 0, 128, 150)
        snail_shock_sprites = self.snail_shock_sprites.subsurface(rect)
        self.current_snail_shock_sprite = snail_shock_sprites

        if self.snail_shock_frame == 5:
            self.snail_shock_frame = 3

        self.snail_shock_frame = (self.snail_shock_frame + 1) % 6
