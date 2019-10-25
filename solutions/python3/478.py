class Solution:

    def __init__(self, radius, x_center, y_center):
        self.x, self.y, self.r = x_center, y_center, radius

    def randPoint(self):
        r, angle, scale = random.uniform(0, self.r), random.uniform(0, 2 * math.pi), math.sqrt(random.uniform(0, 1))
        return [self.x + self.r * scale * math.cos(angle), self.y + self.r * scale * math.sin(angle)]