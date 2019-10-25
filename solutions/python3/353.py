class SnakeGame:

    def __init__(self, width, height, food):
        self.foods = collections.deque(food)
        self.i = self.j = 0
        self.w, self.h = width, height
        self.score = 0
        self.snake = collections.OrderedDict()
        self.snake[(0, 0)] = 1
        

    def move(self, direction):
        x, y = self.snake.popitem(last = False)
        if direction == "U":
            self.i -= 1
        elif direction == "D":
            self.i += 1
        elif direction == "R":
            self.j += 1
        else:
            self.j -= 1
        if 0 <= self.i < self.h and 0 <= self.j < self.w and (self.i, self.j) not in self.snake:
            self.snake[(self.i, self.j)] = 1
            if self.foods and self.i == self.foods[0][0] and self.j == self.foods[0][1]:
                self.score += 1
                self.foods.popleft()
                self.snake[(x, y)] = 1
                self.snake.move_to_end((x, y), last = False)
            return self.score
        else:
            return -1