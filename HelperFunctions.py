import pygame

# ---------------------------
# Hàm vẽ nút
# ---------------------------
def DrawButton(screen, rect, text, font, color, text_color):
    pygame.draw.rect(screen, color, rect, border_radius=8)
    label = font.render(text, True, text_color)
    screen.blit(label, (rect.x + 20, rect.y + 10))