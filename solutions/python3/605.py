class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num=n
        if len(flowerbed)<=1:
            if (num==1 and flowerbed==[0]) or (num==0):
                return True
            else:
                return False
        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0]=1
            num-=1
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            flowerbed[-1]=1
            num-=1
        for i in range(1,len(flowerbed)-2):
            if flowerbed[i]!=1 and flowerbed[i+1]!=1 and flowerbed[i-1]!=1:
                flowerbed[i]=1
                num-=1
        if num<=0:
            return True
        return False
            