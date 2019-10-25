class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                if stack[-2] < abs(stack[-1]): stack[-2] = stack[-1]
                elif stack[-2] == abs(stack[-1]): stack.pop()
                stack.pop()
        return stack            