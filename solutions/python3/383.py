class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = collections.Counter(magazine)
        for c in ransomNote:
            if cnt[c]:
                cnt[c] -= 1
            else:
                return False
        return True