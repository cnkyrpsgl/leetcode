class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        res = []
        for i in range(len(phrases)):
            for j in range(i + 1, len(phrases)):
                w1 = phrases[i].split()[-1]
                w2 = phrases[j].split()[0]
                if w1 == w2:
                    r = phrases[i] + ' ' + ' '.join(phrases[j].split()[1:])
                    res.append(r.rstrip())
                w1 = phrases[j].split()[-1]
                w2 = phrases[i].split()[0]
                if w1 == w2:
                    r = phrases[j] + ' ' + ' '.join(phrases[i].split()[1:])
                    res.append(r.rstrip())
        return sorted(set(res))        