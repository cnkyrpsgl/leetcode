class Solution(object):
    def search(self, reader, target):
        l, r = 0, 20000
        while l <= r:
            index = (l + r) // 2
            response = reader.get(index)
            if response > target:
                r = index - 1
            elif response < target:
                l = index + 1
            else:
                return index
        return -1