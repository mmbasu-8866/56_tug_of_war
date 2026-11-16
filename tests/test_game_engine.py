import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame
import pytest

import game.game_engine as game_engine
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


def test_panic_surge_uses_faster_cadence_and_stronger_pull(monkeypatch):
    engine = make_engine(monkeypatch, now=1_000)
    engine.rope.marker_x = 250
    engine.last_computer_pull = 0
    monkeypatch.setattr(game_engine.random, "uniform", lambda _low, _high: 2.0)

    engine.update()

    assert engine.panic_mode
    assert engine.computer_pull_cooldown == engine.PANIC_PULL_INTERVAL_MS
    assert engine.rope.marker_x == 274
