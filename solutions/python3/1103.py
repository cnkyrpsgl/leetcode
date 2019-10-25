class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i = 0
        while candies > 0:
            res[i % num_people] += min(candies, i + 1)
            i += 1
            candies -= i
        return res