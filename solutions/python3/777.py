class Solution:
    def canTransform(self, start, end):
        s, e = collections.defaultdict(list), collections.defaultdict(list)
        newS, newE = [c for c in start if c != "X"], [c for c in end if c != "X"]
        for i in range(len(start)):
            if start[i] != "X":
                s[start[i]].append(i)
            if end[i] != "X":
                e[end[i]].append(i)
        if newS == newE and len(s["L"]) == len(e["L"]) and len(s["R"]) == len(e["R"]):
            if all(s["R"][i] <= e["R"][i] for i in range(len(s["R"]))) and all(s["L"][i] >= e["L"][i] for i in range(len(s["L"]))):
                return True
        return False