class Solution:
    def isPossible(self, nums):
        heap, last = [], collections.defaultdict(int)
        for num in nums:
            last[num] += 1
            if heap and heap[0][0] <= num - 1:
                if heap[0][0] < num - 1:
                    return False
                else:
                    last[num - 1] -= 1
                    n, l = heapq.heappop(heap)
                    if l == -1:
                        heapq.heappush(heap, (num, -2))
            elif num - 1 not in last or not last[num - 1]:
                heapq.heappush(heap, (num, -1))
            else:
                last[num - 1] -= 1
        return not heap