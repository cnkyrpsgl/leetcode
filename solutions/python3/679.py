class Solution:
    def judgePoint24(self, nums):
        q = [[None, nums[i]] + nums[:i] + nums[i + 1:] for i in range(len(nums))]
        while q:
            new = []
            for group1, group2, *rest in q:
                if not rest and group1:
                    for res in (group1 + group2, group1 - group2, group1 * group2, group2 and group1 / group2): 
                        if 23.999 <= res <= 24.0001: return True
                if not rest and not group1 and 23.999 <= group2 <= 24.0001: return True
                for i in range(len(rest)):
                    for newGroup2 in (group2 + rest[i], group2 - rest[i], rest[i] - group2, group2 * rest[i], group2 / rest[i]):
                        new.append([group1, newGroup2] + rest[:i] + rest[i + 1:])
                    if group2:
                        new.append([group1, rest[i] / group2] + rest[:i] + rest[i + 1:])
                    if group1 != None:
                        for newGroup1 in (group1 + group2, group1 - group2, group1 * group2):
                            new.append([newGroup1, rest[i]] + rest[:i] + rest[i + 1:])
                        if group2:
                            new.append([group1 / group2, rest[i]] + rest[:i] + rest[i + 1:])
                    else:
                        new.append([group2, rest[i]] + rest[:i] + rest[i + 1:])
            q = new
        return False