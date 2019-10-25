from collections import Counter as cnt
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(not cnt(w) - cnt(chars) and len(w) for w in words)