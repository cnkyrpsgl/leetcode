class Solution:
    def minIncrementForUnique(self, A):
        st, used, move = set(A), set(), 0
        heapq.heapify(A)
        empty = [i for i in range(80000) if i not in st][::-1] if A else [] 
        while A:
            num = heapq.heappop(A)
            if num not in used:
                used.add(num)
            else:
                while empty[-1] < num:
                    empty.pop()
                move += empty[-1] - num
                heapq.heappush(A, empty.pop())
        return move