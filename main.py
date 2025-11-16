import sys
import pygame
from VeKhung import VeKhung
from AnMoi import AnMoi
from HelperFunctions import DrawButton
from Snake import Snake 

# ==========================
# MAIN GAME
# ==========================   
def main():
    pygame.init()

    width, height = 600, 1000
    size = 20  # kích thước 1 ô

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game (Windows Version)")

    clock = pygame.time.Clock()

    # Rắn ban đầu
    snake = Snake()
    direction = "RIGHT"

    # Mồi
    food_pos = AnMoi(snake.snake_body, width, height, size)

    score = 0
    running = True
    game_over = False

    while running:
        screen.fill((0, 0, 0))
        VeKhung(screen, width, height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Điều khiển
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # Di chuyển đầu rắn
        snake.ChangeDirection(direction)        

        # Kiểm tra ăn mồi
        if snake.CheckEat(food_pos):
            score += 1
            food_pos = AnMoi(snake.snake_body, width, height, size)

        # Kiểm tra thua (đụng tường)
        if snake.CheckCollideWall(width, height):
            running = False
            game_over = True

        # Kiểm tra đụng thân
        if snake.CheckCollideItself():
            running = False
            game_over = True

        # Vẽ rắn
        for block in snake.snake_body:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(block[0], block[1], size, size))

        # Vẽ mồi
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], size, size))

        # Điểm
        font = pygame.font.SysFont(None, 24)
        txt = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(txt, (10, 10))

        pygame.display.update()
        clock.tick(10)  # tốc độ FPS

    # GAME OVER
    while game_over:
        screen.fill((30, 30, 30))

        label = font.render("GAME OVER!", True, (255, 255, 255))
        screen.blit(label, (width//2 - 80, height//2 - 80))

        restart_rect = pygame.Rect(width//2 - 100, height//2, 200, 40)
        quit_rect = pygame.Rect(width//2 - 100, height//2 + 60, 200, 40)

        DrawButton(screen, restart_rect, "Restart", font, (70, 160, 70), (255, 255, 255))
        DrawButton(screen, quit_rect, "Quit", font, (160, 70, 70), (255, 255, 255))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                if restart_rect.collidepoint(mx, my):
                    main()
                if quit_rect.collidepoint(mx, my):
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()