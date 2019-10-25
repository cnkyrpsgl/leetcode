class Solution:
    def findItinerary(self, tickets):
        graph, stack, reached = collections.defaultdict(list), ["JFK"], []
        for a, b in tickets: heapq.heappush(graph[a], b)  
        while stack:
            if graph[stack[-1]]: stack.append(heapq.heappop(graph[stack[-1]]))
            else: reached.append(stack.pop())
        return reached[::-1]