"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        def dfs(id):
            self.val += dic[id].importance
            for sub in dic[id].subordinates:
                dfs(sub)
        dic = {}
        for emp in employees:
            dic[emp.id] = emp
        self.val = 0
        dfs(id)
        return self.val