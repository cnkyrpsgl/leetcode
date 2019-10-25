class Solution:
    def findOrder(self, numCourses, prerequisites):
        children, parent = collections.defaultdict(set), collections.defaultdict(set)
        for i, j in prerequisites: children[i].add(j); parent[j].add(i)
        stack = [i for i in range(numCourses) if not children[i]]
        for i in stack:
            for j in parent[i]:
                children[j].remove(i)
                if not children[j]: stack += j,
        return stack if len(stack) == numCourses else []