class Solution:
    def pourWater(self, heights, V, K):
        for drop in range(V):
            l = r = K
            for i in range(K - 1, -1, -1):
                if heights[i] > heights[l]:
                    break
                elif heights[i] < heights[l]:
                    l = i
            if l < K:
                heights[l] += 1
            else:
                for j in range(K + 1, len(heights)):
                    if heights[j] > heights[r]:
                        break
                    elif heights[j] < heights[r]:
                        r = j
            if l == r == K:
                heights[K] += 1
            elif r > K:
                heights[r] += 1
        return heights