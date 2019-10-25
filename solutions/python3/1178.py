from itertools import combinations as cb
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        cnt = collections.Counter(''.join(sorted(set(w))) for w in words)
        return [sum(cnt[''.join(sorted(s + (p[0], )))] for l in range(len(p)) for s in cb(p[1:], l)) for p in puzzles]