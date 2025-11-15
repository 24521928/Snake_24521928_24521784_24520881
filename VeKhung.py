import pygame

# ==========================
# Hàm vẽ khung
# ==========================
def VeKhung(screen, width, height):
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, width, height), 10)
