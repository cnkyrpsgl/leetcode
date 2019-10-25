class Solution(object):
    def numberOfBoomerangs(self, points):
        res = 0
        for p in points:
            dic = collections.defaultdict(int)
            for q in points:
                d = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                dic[d] += 1
            for k in dic: res += dic[k] * (dic[k] - 1)
        return res