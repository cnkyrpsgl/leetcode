class Solution:
    def canFinish(self, numCourses, prerequisites):
        def cycle(course):
            visited[course] = 0
            for Next in route[course]:
                if visited[Next] == 0 or (visited[Next] == -1 and cycle(Next)): return True
            visited[course] = 1
            return False
        route, visited = {i: [] for i in range(numCourses)}, [-1] * numCourses 
        for req in prerequisites: route[req[1]].append(req[0])
        for course in range(numCourses):
            if visited[course] == -1 and cycle(course): return False
        return True