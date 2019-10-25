class Solution:

    def __init__(self, nums):
        self.indexes = collections.defaultdict(set)
        for i, num in enumerate(nums):
            self.indexes[num].add(i)

    def pick(self, target):
        return random.sample(self.indexes[target], 1)[0]