class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        l1 = l2 = l3 = -1
        left = [[float('inf') for _ in range(3)] for __ in range(len(colors))]
        res = []
        for i, c in enumerate(colors):
            if c == 1:
                l1 = i
            elif c == 2:
                l2 = i
            else:
                l3 = i
            if l1 != -1:
                left[i][0] = i - l1
            if l2 != -1:
                left[i][1] = i - l2
            if l3 != -1:
                left[i][2] = i - l3
                
        l1 = l2 = l3 = -1
        right = [[float('inf') for _ in range(3)] for __ in range(len(colors))]
        for i in range(len(colors) - 1, -1, -1):
            c = colors[i]
            if c == 1:
                l1 = i
            elif c == 2:
                l2 = i
            else:
                l3 = i
            if l1 != -1:
                right[i][0] = l1  - i
            if l2 != -1:
                right[i][1] = l2 - i
            if l3 != -1:
                right[i][2] = l3 - i
        for i, c in queries:
            res.append(min(left[i][c - 1], right[i][c - 1]))
        return [c if c != float('inf') else -1 for c in res]
            
            
        
            
        