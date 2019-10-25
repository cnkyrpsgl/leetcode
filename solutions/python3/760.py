class Solution:
    def anagramMappings(self, A, B):
        ind = {num: j for j, num in enumerate(B)}
        return [ind[num] for num in A] 