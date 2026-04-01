class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        print(adjList)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            print(visited)
            print(node)
            for nd in adjList[node]:
                if nd not in visited:
                    dfs(nd)
            return 0

        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        
        return count
