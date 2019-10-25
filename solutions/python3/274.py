class Solution:
    def hIndex(self, citations):
        citations.sort()
        for i in range(len(citations)):
            if len(citations) - i <= citations[i]: return len(citations) - i
        return 0