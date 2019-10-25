class Solution:
    def catMouseGame(self, graph: 'List[List[int]]') -> 'int':
        mouse_visited = [False] * len(graph)
        mouse_win_map = [[None for column in range(len(graph))] for row in range(len(graph))]
        cat_visited = [False] * len(graph)
        cat_win_map = [[None for column in range(len(graph))] for row in range(len(graph))]
        if self.isMouseWin(graph, 1, 2, mouse_visited, mouse_win_map):
            return 1
        elif self.isCatWin(graph, 1, 2, cat_visited, cat_win_map):
            return 2
        else:
            return 0

    def isMouseWin(self, graph, mouse, cat, mouse_visited, mouse_win_map):
        if mouse == 0:
            return True
        if mouse_win_map[mouse][cat] is not None:
            return mouse_win_map[mouse][cat]
        mouse_visited[mouse] = True
        for mouseMove in graph[mouse]:
            if mouseMove == 0 or (mouseMove not in graph[cat] and  mouseMove != cat):
                if not mouse_visited[mouseMove]:
                    mouseWinFlag = True
                    for catMove in graph[cat]:
                        if catMove != 0 and not self.isMouseWin(graph, mouseMove, catMove, mouse_visited, mouse_win_map):
                            mouseWinFlag = False
                            break
                    if mouseWinFlag:
                        mouse_visited[mouse] = False
                        mouse_win_map[mouse][cat] = True
                        return True
        mouse_visited[mouse] = False
        mouse_win_map[mouse][cat] = False
        return False

    def isCatWin(self, graph, mouse, cat, cat_visited, cat_win_map):
        if mouse == 0:
            return False
        if cat_win_map[mouse][cat] is not None:
            return cat_win_map[mouse][cat]
        cat_visited[cat] = True
        for mouseMove in graph[mouse]:
            if mouseMove == 0 or (mouseMove not in graph[cat] and  mouseMove != cat):
                catWinFlag = True
                for catMove in graph[cat]:
                    if catMove != 0 and not cat_visited[catMove] and not self.isCatWin(graph, mouseMove, catMove,
                                                                                       cat_visited, cat_win_map):
                        catWinFlag = False
                        break
                if not catWinFlag:
                    cat_visited[cat] = False
                    cat_win_map[mouse][cat] = False
                    return False
        cat_visited[cat] = False
        cat_win_map[mouse][cat] = True
        return True