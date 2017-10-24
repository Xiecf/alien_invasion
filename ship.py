import pygame
import settings

from settings import Settings

class Ship:

    def __init__(self, screen):
        """初始化飞船并设置其位置"""
        self.screen = screen

        # 加载飞船图像并获取其外界矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.rect.centerx += settings.Settings.ship_speed_factor
        if self.moving_left:
            self.rect.centerx -= settings.Settings.ship_speed_factor
