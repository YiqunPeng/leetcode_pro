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
        """BFS.
        
        Running time: O(n) where n is the number of employees.
        """
        d = {e.id: e for e in employees}
        
        r = 0
        q = collections.deque([d[id]])
        while q:
            e = q.popleft()
            r += e.importance
            
            for sub in e.subordinates:
                q.append(d[sub])
        
        return r