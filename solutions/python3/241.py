class Solution:
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i + 1:])
                for j in l:
                    for k in r:
                        res.append(self.calc(j, input[i], k))
        return res
    def calc(self, l, op, r):
        return l + r if op == "+" else l - r if op == "-" else l * r