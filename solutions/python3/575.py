class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return len(set(candies)) if len(set(candies))<=len(candies)//2 else len(candies)//2