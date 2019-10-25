class Solution:
    def numBusesToDestination(self, routes, starterBus, targetBus):
        path, travel, travelTaken, used = collections.defaultdict(set), [starterBus], 0, set()
        for i, route in enumerate(routes):
            for bus in route:
                path[bus].add(i)
        while travel:
            new = []
            for bus in travel:
                if bus == targetBus:
                    return travelTaken
                for route in path[bus]:
                    if route not in used:
                        used.add(route)
                        for nextBus in routes[route]:
                            if nextBus != bus:
                                new.append(nextBus)
            travelTaken += 1
            travel = new
        return -1