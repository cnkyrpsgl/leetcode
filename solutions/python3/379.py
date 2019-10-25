class PhoneDirectory:

    def __init__(self, maxNumbers):
        self.nums = set(range(maxNumbers))

    def get(self):
        return self.nums.pop() if self.nums else -1

    def check(self, number):
        return number in self.nums

    def release(self, number):
        self.nums.add(number)