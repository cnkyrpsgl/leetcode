class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        table = collections.defaultdict(list)
        for w in strings:
            pattern = ""
            for i in range(1, len(w)):
                if ord(w[i]) - ord(w[i - 1]) >= 0:
                    pattern += str(ord(w[i]) - ord(w[i - 1]))
                else:
                    pattern += str(ord(w[i]) - ord(w[i - 1]) + 26)
            table[pattern].append(w)
        return [table[pattern] for pattern in table]