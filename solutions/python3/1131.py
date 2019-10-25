class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        l1, l2 ,l3, l4 = [], [], [], []
        for i in range(len(arr1)):
            l1 += [arr1[i]+arr2[i]+i]
            l2 += [arr1[i]-arr2[i]+i]
            l3 += [-arr1[i]+arr2[i]+i]
            l4 += [-arr1[i]-arr2[i]+i]
        res = []
        res += [max(l1)-min(l1)]
        res += [max(l2) -min(l2)]
        res += [max(l3)-min(l3)]
        res += [max(l4)-min(l4)]
        return max(res)