import pygame

def VeKhung(screen, width, height):
    """Vẽ một đường viền đơn giản quanh khu vực chơi."""
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, width, height), 2)
