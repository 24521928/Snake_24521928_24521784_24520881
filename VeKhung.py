import pygame

def VeKhung(screen, width, height):
    border_color = (255, 255, 255)
    border_thickness = 2 
    pygame.draw.rect(screen, border_color, (0, 0, width, height), border_thickness)
