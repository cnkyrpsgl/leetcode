class Solution:
    def minAvailableDuration(self, s1: List[List[int]], s2: List[List[int]], d: int) -> List[int]:
        s2.sort()
        j = 0
        for s, e in sorted(s1):
            while j < len(s2) - 1 and s2[j][1] < s:
                j += 1
            if s2[j][0] <= e:
                l, r = max(s, s2[j][0]), min(e,s2[j][1])
                if r - l >= d:
                    return [l, l + d]