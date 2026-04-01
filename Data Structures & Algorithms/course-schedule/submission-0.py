class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for p, q in prerequisites:
            if p not in courseMap:
                courseMap[p] = []
            courseMap[p].append(q)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if courseMap[course] == []:
                return True
            
            visited.add(course)
            for c in courseMap[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            courseMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
