class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nd in adjList[node]:
                if nd not in visited:
                    dfs(nd)

        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        
        return count
