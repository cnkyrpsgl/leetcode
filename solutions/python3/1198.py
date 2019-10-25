from itertools import chain as chn
from collections import Counter as cnt
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        return min([k for k, v in cnt(chn(*mat)).items() if v == len(mat)] or [-1])