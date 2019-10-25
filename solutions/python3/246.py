class Solution:
    def isStrobogrammatic(self, num):
        return not any(num[i] + num[-1-i] not in ("88", "69", "96", "11", "00") for i in range((len(num) + 1) // 2))