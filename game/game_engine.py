import random

import pygame

from game.rope import Rope
from game.player import Puller


class GameEngine:
    NORMAL_PULL_INTERVAL_MS = 180
    PANIC_PULL_INTERVAL_MS = 60
    PANIC_DISTANCE_RATIO = 0.35

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rope = Rope(width, height)
        self.player = Puller(90, height // 2, (50, 120, 220), "PLAYER (A/D)")
        self.computer = Puller(width - 90, height // 2, (220, 80, 50), "COMPUTER")

        self.last_key = None
        self.held_keys = set()
        self.winner = None
        self.game_state = "PLAYING"
        self.panic_mode = False

        self.computer_pull_cooldown = self.NORMAL_PULL_INTERVAL_MS
        self.last_computer_pull = pygame.time.get_ticks()

        self.font_big = pygame.font.SysFont(None, 48)
        self.font_small = pygame.font.SysFont(None, 26)

    def handle_event(self, event):
        if event.type == pygame.KEYUP:
            self.held_keys.discard(event.key)
            return

        if event.type != pygame.KEYDOWN:
            return

        if self.game_state != "PLAYING":
            if event.key == pygame.K_r:
                self.reset()
            return

        if event.key not in (pygame.K_a, pygame.K_d) or event.key in self.held_keys:
            return

        self.held_keys.add(event.key)
        if event.key != self.last_key:
            self.rope.pull_left(1.0)
            self.last_key = event.key

    def update(self):
        if self.game_state != "PLAYING":
            return

        now = pygame.time.get_ticks()
        center_x = self.width // 2
        player_range = max(1, center_x - self.rope.left_win_x)
        distance_to_player_goal = self.rope.marker_x - self.rope.left_win_x
        self.panic_mode = (
            distance_to_player_goal <= player_range * self.PANIC_DISTANCE_RATIO
        )
        self.computer_pull_cooldown = (
            self.PANIC_PULL_INTERVAL_MS if self.panic_mode else self.NORMAL_PULL_INTERVAL_MS
        )

        if now - self.last_computer_pull >= self.computer_pull_cooldown:
            if self.panic_mode:
                computer_strength = random.uniform(1.8, 2.4)
            else:
                computer_strength = random.uniform(0.7, 1.2)
            self.rope.pull_right(computer_strength)
            self.last_computer_pull = now

        result = self.rope.check_winner()
        if result:
            self.winner = result
            self.game_state = "GAME_OVER"

    def reset(self):
        self.rope.reset()
        self.last_key = None
        self.held_keys.clear()
        self.winner = None
        self.game_state = "PLAYING"
        self.last_computer_pull = pygame.time.get_ticks()

    def render(self, screen):
        screen.fill((30, 32, 36))

        mud_rect = pygame.Rect(self.width // 2 - 120, self.height // 2 - 80, 240, 160)
        pygame.draw.rect(screen, (45, 38, 30), mud_rect, border_radius=12)

        self.rope.render(screen)
        self.player.render(screen)
        self.computer.render(screen)

        inst_surf = self.font_small.render(
            "Alternate [A] and [D] keys rapidly to pull!", True, (210, 210, 210)
        )
        screen.blit(inst_surf, (self.width // 2 - inst_surf.get_width() // 2, 40))

        if self.panic_mode and self.game_state == "PLAYING":
            panic_surface = self.font_small.render(
                "COMPUTER PANIC SURGE!", True, (255, 115, 80)
            )
            screen.blit(
                panic_surface,
                (self.width // 2 - panic_surface.get_width() // 2, 72),
            )

        if self.game_state == "GAME_OVER":
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))

            win_text = f"{self.winner} WINS!"
            color = (80, 220, 80) if self.winner == "PLAYER" else (240, 80, 80)
            text_surf = self.font_big.render(win_text, True, color)
            screen.blit(
                text_surf,
                (self.width // 2 - text_surf.get_width() // 2, self.height // 2 - 50),
            )

            restart_surf = self.font_small.render(
                "Press [R] to Play Again", True, (240, 240, 240)
            )
            screen.blit(
                restart_surf,
                (self.width // 2 - restart_surf.get_width() // 2, self.height // 2 + 10),
            )
