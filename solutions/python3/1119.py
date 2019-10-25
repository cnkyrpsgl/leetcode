class Solution:
    def removeVowels(self, S: str) -> str:
        return ''.join(filter(lambda x: x not in 'aeiou', S))
        return ''.join(c for c in S if c not in 'aeiou')
        