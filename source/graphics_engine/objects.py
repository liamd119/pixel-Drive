"""Contains all graphics related objects."""
# pylint: disable = import-error
import pygame
from source.constants import DIMENSIONS


class GameLoop:
    def __init__(self, *funcs):
        def loop():
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type in [pygame.QUIT]:
                        pygame.event.event_name(event.type)
                for func in funcs:
                    func()
        self.screen = pygame.display.set_mode(DIMENSIONS)
        self.loop = loop
