class Snake:
    def __init__(self):
        self.snake_head = [100, 60]       # đầu rắn
        self.snake_body = [[100, 60], [80, 60], [60, 60]]
        
        Snake.sizeOfOneBlock = 20
    
    def ChangeDirection(self, direction):
        if direction == "UP":
            self.snake_head[1] -= Snake.sizeOfOneBlock
        elif direction == "DOWN":
            self.snake_head[1] += Snake.sizeOfOneBlock
        elif direction == "LEFT":
            self.snake_head[0] -= Snake.sizeOfOneBlock
        elif direction == "RIGHT":
            self.snake_head[0] += Snake.sizeOfOneBlock

        self.AddNewHead(self.snake_head)

    def AddNewHead(self, snake_head):
        self.snake_body.insert(0, list(snake_head))

    def CheckEat(self, food_pos):
        if self.snake_head == food_pos:
            return True
        else:
            self.snake_body.pop()
            return False
        
    def CheckCollideWall(self, width, height, wall=10):
        if (self.snake_head[0] < wall or self.snake_head[0] + Snake.sizeOfOneBlock > width - wall or
            self.snake_head[1] < wall or self.snake_head[1] + Snake.sizeOfOneBlock > height - wall):
            return True
        return False
        
    def CheckCollideItself(self):
        if self.snake_head in self.snake_body[1:]:
            return True
        return False