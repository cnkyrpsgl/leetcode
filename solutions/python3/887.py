class Solution:
    def superEggDrop(self, K, N):
        drops = 0                           # the number of eggs dropped
        floors = [0 for _ in range(K + 1)]  # floors[i] is the number of floors that can be checked with i eggs

        while floors[K] < N:                # until we can reach N floors with K eggs 

            for eggs in range(K, 0, -1):
                floors[eggs] += 1 + floors[eggs - 1]
            drops += 1

        return drops