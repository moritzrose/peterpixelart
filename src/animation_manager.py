from budda import Budda
from time_manager import TimeManager


class AnimationManager:
    def __init__(self, screen):
        self.screen = screen
        self.time_manager = TimeManager()
        self.animations = {"MORGENS": "Schneckenkampf", "MITTAGS": BierFight(), "ABENDS": Budda(screen), "NACHTS": "Schlafen"}
        self.current_animation = None
        self.next_animation = None
        # self.meditation = Meditation()
        # self.beerfight = Beerfight()
        # self.sleep = Sleep()
        # self.dessert = Dessert()
        # self.current_animation = None

    def update(self):
        current_period = self.time_manager.determine_period()
        current_animation = self.animations.get(current_period)
        current_animation.run()
