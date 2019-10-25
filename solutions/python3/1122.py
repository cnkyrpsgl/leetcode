class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key = lambda x: arr2.index(x) if x in arr2 else len(arr2) + x)