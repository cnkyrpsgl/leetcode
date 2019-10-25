class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        for num in list(arr):
            if i >= len(arr): break
            arr[i] = num
            if not num:
                i += 1
                if i < len(arr):
                    arr[i] = num
            i += 1