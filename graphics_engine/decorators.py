"""Contains all graphics related decorator functions."""
# pylint: disable = import-error
import functools
import pygame


def on_event(event):
    """Only executes when the event occurs"""
    def filler(func):
        if event in pygame.event.get():
            @functools.wraps(func)
            def wrapper_on_event(*args, **kwargs):
                print("before")
                output = func(*args, **kwargs)
                print("after")
                return output
            return wrapper_on_event
        return None
    return filler
