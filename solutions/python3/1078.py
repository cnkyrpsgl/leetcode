class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        return [text[i] for i in range(2, len(text)) if text[i-1] == second and text[i-2] == first]                         