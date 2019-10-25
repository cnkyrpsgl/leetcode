class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        st, cap, vow = set(wordlist), {}, {}
        for w in wordlist:
            newC = w.lower()
            newW = "".join(c if c not in "aeiou" else "*" for c in newC)
            if newC not in cap:
                cap[newC] = w
            if newW not in vow:
                vow[newW] = w
        for i, w in enumerate(queries):
            if w in st:
                pass
            elif w.lower() in cap:
                queries[i] = cap[w.lower()]
            else:
                new = "".join(c if c not in "aeiou" else "*" for c in w.lower())
                if new in vow:
                    queries[i] = vow[new]
                else:
                    queries[i] = ""
        return queries