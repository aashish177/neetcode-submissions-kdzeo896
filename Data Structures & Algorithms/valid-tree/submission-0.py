class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        for p, q in edges:
            adjList[p].append(q)
            adjList[q].append(p)
        print(adjList)
        visited = set()

        def dfs(num, prev):
            if num in visited:
                return False
            
            visited.add(num)
            for node in adjList[num]:
                if node == prev:
                    continue
                if not dfs(node, num):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n