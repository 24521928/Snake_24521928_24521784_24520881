import random

# ==========================
# Hàm sinh mồi mới
# ==========================
def AnMoi(snake_body, width, height, size):
    while True:
        x = random.randrange(1, (width // size) - 1) * size
        y = random.randrange(1, (height // size) - 1) * size
        if [x, y] not in snake_body:
            return [x, y]   