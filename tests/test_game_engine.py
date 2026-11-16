import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame
import pytest

from game.game_engine import GameEngine


@pytest.fixture(scope="module", autouse=True)
def pygame_setup():
    pygame.init()
    yield
    pygame.quit()


def key_event(event_type, key):
    return pygame.event.Event(event_type, key=key)


def make_engine(monkeypatch, now=0):
    monkeypatch.setattr(pygame.time, "get_ticks", lambda: now)
    return GameEngine(800, 450)


def test_overlapping_alternating_presses_do_not_deadlock(monkeypatch):
    engine = make_engine(monkeypatch)
    start = engine.rope.marker_x

    engine.handle_event(key_event(pygame.KEYDOWN, pygame.K_a))
    engine.handle_event(key_event(pygame.KEYDOWN, pygame.K_d))
    engine.handle_event(key_event(pygame.KEYUP, pygame.K_a))
    engine.handle_event(key_event(pygame.KEYUP, pygame.K_d))
    engine.handle_event(key_event(pygame.KEYDOWN, pygame.K_a))

    assert engine.rope.marker_x == start - 3 * engine.rope.pull_step


def test_held_key_repeat_does_not_create_duplicate_pulls(monkeypatch):
    engine = make_engine(monkeypatch)
    start = engine.rope.marker_x

    engine.handle_event(key_event(pygame.KEYDOWN, pygame.K_a))
    engine.handle_event(key_event(pygame.KEYDOWN, pygame.K_a))
    engine.handle_event(key_event(pygame.KEYDOWN, pygame.K_a))

    assert engine.rope.marker_x == start - engine.rope.pull_step
