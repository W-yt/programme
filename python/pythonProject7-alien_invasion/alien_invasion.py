import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化pyganme、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏信息的实例 并创建记分牌
    stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, stats, screen)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, stats, scoreboard, screen, ship, aliens, bullets, play_button)

        if stats.game_active:
            gf.update_ship(ship)
            gf.update_bullets(ai_settings, stats, scoreboard, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, scoreboard, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, stats, scoreboard, screen, ship, aliens, bullets, play_button)


run_game()