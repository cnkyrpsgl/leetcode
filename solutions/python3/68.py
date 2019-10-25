class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, used, s = [], 0, []
        for i, w in enumerate(words):
            if not s or len(w) + used + len(s) <= maxWidth:
                used += len(w)
                s += [w]
            else:
                if len(s) == 1:
                    res.append(s[0] + (maxWidth - used) * ' ')
                else:
                    br = (maxWidth - used) // (len(s) - 1)
                    res.append(''.join((br + (i <= (maxWidth - used) % (len(s) - 1))) * ' ' + c for i, c in enumerate(s)).lstrip())
                used, s = len(w), [w]
        return res + [' '.join(c for c in s) + (maxWidth - used - len(s) + 1) * ' ']