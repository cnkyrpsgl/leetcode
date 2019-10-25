class TwoSum:

    def __init__(self):
        self.nums = {}

    def add(self, number):
        self.nums[number] = self.nums.get(number, 0) + 1

    def find(self, value):
        for num in self.nums:
            if value - num in self.nums and (num != value - num or self.nums[num] > 1):
                return True
        return False