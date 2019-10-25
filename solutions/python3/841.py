class Solution:
    def canVisitAllRooms(self, rooms):
        pool, stack = set(range(len(rooms))), [0]
        while stack: 
            pool.discard(stack[-1])
            for nex in rooms[stack.pop()]:
                if nex in pool: 
                    stack.append(nex)
        return not pool