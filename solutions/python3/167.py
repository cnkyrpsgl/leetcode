class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=numbers[0]
        right=numbers[-1]
        i,j=0,0
        while True:
            sum=left+right
            if sum>target:
                j+=1
                right=numbers[-1-j]
            if sum<target:
                i+=1
                left=numbers[0+i]
            if sum==target:
                return [i+1,len(numbers)-j]
            
                
        