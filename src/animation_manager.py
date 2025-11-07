from bier_fight import BierFight
from budda import Budda
from time_manager import TimeManager

NACHTS = "NACHTS"

ABENDS = "ABENDS"

MITTAGS = "MITTAGS"

MORGENS = "MORGENS"
BG = (8, 6, 14)

class AnimationManager:
    def __init__(self, screen):
        self.screen = screen
        self.time_manager = TimeManager()
        self.frame_timer = 0
        self.frame_speed = None
        self.animations = {MORGENS: BierFight(screen), MITTAGS: BierFight(screen) , ABENDS: Budda(screen), NACHTS: Budda(screen)}
        self.current_animation = None
        self.next_animation = None
        # self.meditation = Meditation()
        # self.beerfight = Beerfight()
        # self.sleep = Sleep()
        # self.dessert = Dessert()
        # self.current_animation = None

    def update(self):
        current_period = self.time_manager.determine_period()

        if current_period == MORGENS or current_period == MITTAGS:
            self.frame_speed = 10
        if current_period == ABENDS or current_period == NACHTS:
            self.frame_speed = 2

        self.frame_timer = (self.frame_timer + 1) % self.frame_speed
        if self.frame_timer == 0:
            self.screen.fill(BG)
            current_animation = self.animations.get(current_period)
            current_animation.run()
