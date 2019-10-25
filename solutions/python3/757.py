class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key = lambda k: k[1])
        solution = []
        for start, end in intervals:
            if not len(solution) or solution[-1] < start:
                solution.append(end - 1)
                solution.append(end)
            elif solution[-2] < start:
                solution.append(end)
        return len(solution)