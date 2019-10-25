class Solution:
    def countOfAtoms(self, formula):
        dic, coeff, stack, elem, cnt, i = collections.defaultdict(int), 1, [], "", 0, 0  
        for c in formula[::-1]:
            if c.isdigit():
                cnt += int(c) * (10 ** i)
                i += 1
            elif c == ")":
                stack.append(cnt)
                coeff *= cnt
                i = cnt = 0
            elif c == "(":
                coeff //= stack.pop()
                i = cnt = 0
            elif c.isupper():
                elem += c
                dic[elem[::-1]] += (cnt or 1) * coeff
                elem = ""
                i = cnt = 0
            elif c.islower():
                elem += c
        return "".join(k + str(v > 1 and v or "") for k, v in sorted(dic.items()))