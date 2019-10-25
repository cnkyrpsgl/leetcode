class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        arr, i = [], 0
        for num in pushed:
            arr.append(num)
            while arr and arr[-1] == popped[i]:
                i += 1
                arr.pop()
        return arr == popped[i:][::-1]