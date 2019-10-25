class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lampsOn = set()
        rowsOn = collections.defaultdict(int)
        colsOn = collections.defaultdict(int)
        diagOnTopLeftBottomRight = collections.defaultdict(int)
        diagOnBottomLeftTopRight = collections.defaultdict(int)
        for r, c in lamps:
            lampsOn.add((r, c))
            rowsOn[r] += 1
            colsOn[c] += 1
            diagOnTopLeftBottomRight[c-r] += 1
            diagOnBottomLeftTopRight[c+r-N] += 1
        
        result = []
        for r, c in queries:
            if rowsOn[r] > 0 or colsOn[c] > 0 or diagOnTopLeftBottomRight[c-r] > 0 or diagOnBottomLeftTopRight[c+r-N] > 0:
                result.append(1)
            else:
                result.append(0)
            adjacentLamps = [(r, c), (r, c-1), (r, c+1), (r-1, c), (r-1, c-1), (r-1, c+1), (r+1, c), (r+1, c-1), (r+1, c+1)]
            for r, c in adjacentLamps:
                if (r, c) in lampsOn:
                    lampsOn.discard((r, c))
                    rowsOn[r] -= 1
                    colsOn[c] -= 1
                    diagOnTopLeftBottomRight[c-r] -= 1
                    diagOnBottomLeftTopRight[c+r-N] -= 1
        return result