class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(openN, closedN, path):
            if openN == closedN == n:
                res.append(path)
                return
            
            if openN < n:
                backtrack(openN+1, closedN, path + "(")
            
            if openN>closedN:
                backtrack(openN, closedN+1, path + ")")

        backtrack(0, 0, "")
        return res