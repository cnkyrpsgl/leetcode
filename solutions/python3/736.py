class Solution:
    def evaluate(self, expression):
        scopes, items = [{}], [["root"]]
        for item in expression.replace(")", " )").split():
            if item[0] == "(":
                items.append([item[1:]])
                if item[1:] == "let":
                    scopes.append(dict(scopes[-1]))
                continue
            elif item == ")": 
                if items[-1][0] == "add":
                    item = str(int(items[-1][1]) + int(items[-1][-1]))
                elif items[-1][0] == "mult":
                    item = str(int(items[-1][1]) * int(items[-1][-1]))
                else:
                    item = items[-1][-1]
                    if item in scopes[-1]:
                        item = scopes[-1][item]
                    scopes.pop()
                items.pop()
            if item in scopes[-1] and (items[-1][0] != "let" or len(items[-1]) % 2 == 0):
                item = scopes[-1][item]
            if items[-1][0] == "let" and item.lstrip("-").isdigit():
                scopes[-1][items[-1][-1]] = item
            items[-1].append(item)
        return int(items[-1][-1])