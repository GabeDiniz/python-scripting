import pygame # pip install pygame
from pygame.font import Font
from pygame.time import Clock
import random 
import sys

# Object-Oriented programming
class DodgySquare:
  def __init__(self) -> None:
    # Pygame
    pygame.init()
    pygame.mouse.set_visible(False) # Disable mouse visability

    # Screen
    self.screen_width, self.screen_height = 600, 600
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    pygame.display.set_caption("Dodgy Square")

    # Colors
    self.WHITE: tuple = (255, 255, 255)
    self.BLACK: tuple = (0, 0, 0)
    self.RED: tuple = (255, 100, 100)
    self.BLUE: tuple = (65, 120, 240)

    # Font
    self.default_font: str = pygame.font.get_default_font()
    self.font: Font = pygame.font.Font(self.default_font, 26)

    # Player
    self.player_size: int = 30 # square size
    self.player_size: list[int] = [0, 0] # Player starting coordinates

    # Enemies
    self.enemy_size: int = 50 # enemy square size
    self.enemy_position: list[int] = []
    self.enemy_list = []
    self.enemy_speed: int = 3
    self.enemy_frequency: int = 20 # Low = Lots, High = Few

    # Clock
    self.clock: Clock = pygame.time.Clock()

    # Game Data
    self.game_over: bool = False
    self.score: int = 0
    self.frame_count: int = 0