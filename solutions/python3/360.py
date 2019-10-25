class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        arr, l, r, ind = [0] * len(nums), 0, len(nums) - 1, a >= 0 and len(nums) - 1 or 0
        while l <= r:
            n1, n2 = a * nums[l] * nums[l] + b * nums[l] + c, a * nums[r] * nums[r] + b * nums[r] + c
            if a >= 0:
                if n1 >= n2: l += 1
                else: r -= 1
                arr[ind] = n1 >= n2 and n1 or n2
                ind -= 1
            else:
                if n1 < n2: l += 1
                else: r -= 1
                arr[ind] = n1 < n2 and n1 or n2
                ind += 1
        return arr