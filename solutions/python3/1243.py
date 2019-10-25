class Solution:
    def transformArray(self, arr: List[int], change: bool = True) -> List[int]:
        while change:
            new = (
                arr[:1]
                + [
                    b + (a > b < c) - (a < b > c)
                    for a, b, c in zip(arr, arr[1:], arr[2:])
                ]
                + arr[-1:]
            )
            arr, change = new, arr != new
        return arr
