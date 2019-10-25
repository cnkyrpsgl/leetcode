class Solution:
    def findDuplicate(self, paths):
        dic = collections.defaultdict(list)
        for path in paths:
            root, *f = path.split(" ")
            for file in f:
                txt, content = file.split("(")
                dic[content] += root + "/" + txt,
        return [dic[key] for key in dic if len(dic[key]) > 1]