import math

import pygame

GLOW_SPEED = 0.08
GLOW_RADIUS = 22

BUDDA_ANGLE_SPEED = 0.02
BUDDA_RADIUS = 15
BUDDA_SCALE = 0.13

MOON_ANGLE_SPEED = 0.01
MOON_RADIUS = 180
MOON_SCALE = 0.06

MOONS_PATH = [
    "resources/Fleckenentfernerblau.png",
    "resources/Fleckenentfernerbraun.png",
    "resources/Fleckenentfernergelb.png",
    "resources/Fleckenentfernergruen.png",
    "resources/Fleckenentfernerlila.png",
    "resources/Fleckenentfernerorange.png",
    "resources/Fleckenentfernerrot.png"
]

BUDDA_PATH = "resources/peterbudda.png"


def init_sprites():
    budda = pygame.image.load(BUDDA_PATH).convert_alpha()
    budda = pygame.transform.smoothscale(budda, (int (budda.get_width() * BUDDA_SCALE), (int (budda.get_height() * BUDDA_SCALE))))

    moons = []
    scale_factor = MOON_SCALE
    num_moons = len(MOONS_PATH)

    for i, file in enumerate(MOONS_PATH):
        img = pygame.image.load(file).convert_alpha()
        w, h = img.get_size()
        img = pygame.transform.smoothscale(img, (int(w * scale_factor), int(h * scale_factor)))
        start_angle = (2 * math.pi / num_moons) * i
        moons.append({"img": img, "current_angle": start_angle, "glow_phase": i * 0.7})

    return budda, moons

class Budda:

    def __init__(self, screen):
        self.screen = screen

        self.center_x = screen.get_width() // 2
        self.center_y = screen.get_height() // 2

        self.budda, self.moons = init_sprites()
        self.budda_angle = 0
        self.moon_angle = 0

    def run(self):
        self.blit_budda()
        self.blit_moons()

    def blit_budda(self):
        budda_x = self.center_x + BUDDA_RADIUS * math.cos(self.budda_angle)
        budda_y = self.center_y + BUDDA_RADIUS * math.sin(self.budda_angle)

        self.budda_angle += BUDDA_ANGLE_SPEED

        budda_rect = self.budda.get_rect(center=(budda_x, budda_y))
        self.screen.blit(self.budda, budda_rect)

    def blit_moons(self):
        for moon in self.moons:
            current_angle = moon.get("current_angle")
            moon_x = self.center_x + MOON_RADIUS * math.cos(current_angle)
            moon_y = self.center_y + MOON_RADIUS * math.sin(current_angle)

            new_angle = current_angle + MOON_ANGLE_SPEED
            moon["current_angle"] = new_angle

            moon_rect = moon["img"].get_rect(center=(moon_x, moon_y))
            self.blit_glow((moon_x, moon_y), GLOW_RADIUS, pulse_phase=moon["glow_phase"])
            moon["glow_phase"] += GLOW_SPEED
            self.screen.blit(moon["img"], moon_rect)

    def blit_glow(self, pos, glow_radius, pulse_phase):
        x, y = pos
        pulse = math.sin(pulse_phase) * 5
        radius = glow_radius + pulse

        glow_surface = pygame.Surface((radius * 4, radius * 4), pygame.SRCALPHA)
        gx, gy = glow_surface.get_width() // 2, glow_surface.get_height() // 2

        for r in range(int(radius * 1.5), 0, -1):
            fade = r / (radius * 1.5)
            alpha = int(255 * (fade ** 3))
            color = (
                int(255 * fade),
                int(220 * fade),
                int(120 * fade),
                alpha // 2
            )
            pygame.draw.circle(glow_surface, color, (gx, gy), r)

        rect = glow_surface.get_rect(center=(x, y))
        self.screen.blit(glow_surface, rect, special_flags=pygame.BLEND_ADD)
