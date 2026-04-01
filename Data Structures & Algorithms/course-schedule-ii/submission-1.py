class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            courseMap[crs].append(pre)

        res = []
        visited = set()
        good = set()

        def dfs(course):
            if course in visited:
                return False
            if course in good:
                return True

            visited.add(course)
            for cr in courseMap[course]:
                if not dfs(cr):
                    return False
            good.add(course)
            visited.remove(course)
            res.append(course)
            return True

        for c in range(numCourses):
            print(c)
            if not dfs(c):
                return []
        
        return res