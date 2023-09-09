"""Interfaces with PyGame."""
# pygame: disable = import-error
import pygame
import threading
from decorators import debug


@debug
def init(dimensions=None):
    """Initialises PyGame"""
    pygame.init()
    if dimensions is None:
        dimensions = [800, 600]
    screen = pygame.display.set_mode(dimensions)
    # event_thread = threading.Thread(target=event_monitor, daemon=False)
    event_thread.start()
    return screen


# USE DECORATORS AROUND GAME LOOP FUNCTIONS
