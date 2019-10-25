class Solution:
    def reconstructMatrix(
        self, upper: int, lower: int, colsum: List[int]
    ) -> List[List[int]]:
        res = [[0] * len(colsum) for _ in range(2)]
        for j, sm in enumerate(colsum):
            if sm == 2:
                if upper == 0 or lower == 0:
                    return []
                upper -= 1
                lower -= 1
                res[0][j] = res[1][j] = 1
            elif sm:
                if upper == lower == 0:
                    return []
                if upper >= lower:
                    upper -= 1
                    res[0][j] = 1
                else:
                    lower -= 1
                    res[1][j] = 1
        return res if upper == lower == 0 else []
