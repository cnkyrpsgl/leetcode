class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in range(left,right+1) if len([char for char in str(num) if int(char)!=0 and num%int(char)==0])==len(str(num)) ]