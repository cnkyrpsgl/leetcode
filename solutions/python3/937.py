class Solution:
    def reorderLogFiles(self, logs):
        return sorted(filter(lambda l: l[l.find(" ") + 1].isalpha(), logs), key = lambda x: (x[x.find(" "):], x[:x.find(" ")])) + list(filter(lambda l: l[l.find(" ") + 1].isdigit(), logs))