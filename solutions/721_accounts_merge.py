class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """DFS.
        """
        email_to_name = defaultdict(str)
        graph = defaultdict(set)
        for k in range(len(accounts)):
            name, emails = accounts[k][0], accounts[k][1:]
            for i in range(len(emails)):
                graph[emails[i]].add(emails[i])
                if i:
                    graph[emails[i]].add(emails[i-1])
                    graph[emails[i-1]].add(emails[i])
                email_to_name[emails[i]] = name
        visited = set()
        res = []
        for k in graph:
            if k not in visited:
                visited.add(k)
                email_list = self._dfs(k, graph, visited)
                res.append([email_to_name[k]] + sorted(email_list))
        return res
    
    def _dfs(self, k, graph, v):
        c = [k]
        for nei in graph[k]:
            if nei not in v:
                v.add(nei)
                c += self._dfs(nei, graph, v)
        return c
