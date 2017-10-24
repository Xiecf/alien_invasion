import sys
import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 关闭窗口
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 检测按键事件---按下
            if event.key == pygame.K_RIGHT:  # 按键为右方向键
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:  # 按键为左方向键
                ship.moving_left = True
        elif event.type == pygame.KEYUP:  # 检测按键事件---松开
            if event.key == pygame.K_RIGHT:  # 按键为右方向键
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:  # 按键为左方向键
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)  # 重绘背景颜色
    ship.blitme()  # 重绘飞船

    pygame.display.flip()  # 刷新屏幕
