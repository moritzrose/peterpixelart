import pygame
import math
import numpy as np


# --- Bewegung A: Budda mit goldenen, weichen Glow-Monden ---
def meditation(screen, frame_time):
    """Zeichnet eine Frame der 'heiligen' Orbit-Animation auf den Screen."""
    # --- Statische Ressourcen (einmalig laden, nicht jedes Frame!) ---
    if not hasattr(meditation, "initialized"):
        # Bilder & Setup nur beim ersten Aufruf laden
        planet = pygame.image.load("../resources/peterbudda.png").convert_alpha()
        planet = pygame.transform.scale(planet, (100, 100))

        moon_files = [
            "../resources/Fleckenentfernerblau.png",
            "../resources/Fleckenentfernerbraun.png",
            "../resources/Fleckenentfernergelb.png",
            "../resources/Fleckenentfernergruen.png",
            "../resources/Fleckenentfernerlila.png",
            "../resources/Fleckenentfernerorange.png",
            "../resources/Fleckenentfernerrot.png"
        ]
        moons = []
        scale_factor = 0.1
        num_moons = len(moon_files)
        orbit_radius = 180

        for i, file in enumerate(moon_files):
            img = pygame.image.load(file).convert_alpha()
            w, h = img.get_size()
            img = pygame.transform.smoothscale(img, (int(w * scale_factor), int(h * scale_factor)))
            start_angle = (2 * math.pi / num_moons) * i
            moons.append({"img": img, "start_angle": start_angle, "glow_phase": i * 0.7})

        # weicher, goldener Glow
        def make_radial_glow(radius, color=(255, 220, 120)):
            size = radius * 2
            surf = pygame.Surface((size, size), pygame.SRCALPHA)
            y, x = np.ogrid[-radius:radius, -radius:radius]
            dist = np.sqrt(x ** 2 + y ** 2)
            mask = np.clip(1 - (dist / radius), 0, 1)
            mask = np.exp(-4 * (1 - mask))  # echter Fade-Out
            r, g, b = color
            rgb = np.zeros((size, size, 3), dtype=np.uint8)
            rgb[..., 0], rgb[..., 1], rgb[..., 2] = r, g, b
            alpha = (mask * 255).astype(np.uint8)
            pixels_rgb = pygame.surfarray.pixels3d(surf)
            pixels_alpha = pygame.surfarray.pixels_alpha(surf)
            pixels_rgb[:] = rgb
            pixels_alpha[:] = alpha
            del pixels_rgb, pixels_alpha
            return surf

        meditation.base_glow = make_radial_glow(150, (255, 230, 150))
        meditation.planet = planet
        meditation.moons = moons
        meditation.center_x = screen.get_width() // 2
        meditation.center_y = screen.get_height() // 2
        meditation.global_angle = 0
        meditation.hover_angle = 0
