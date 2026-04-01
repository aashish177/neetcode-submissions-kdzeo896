class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(index, path, totalSum):
            if totalSum > target:
                return

            if totalSum == target:
                res.append(path.copy())
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path, totalSum+candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res


            
            
            