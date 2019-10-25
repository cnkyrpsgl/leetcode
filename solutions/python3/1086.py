class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        res = []
        items.sort(key = lambda x: (-x[0], x[1]))
        while items:
            res.append([items[-1][0], sum(b for a, b in items[-5:]) // 5])
            while items and items[-1][0] == res[-1][0]:
                items.pop()
        return res