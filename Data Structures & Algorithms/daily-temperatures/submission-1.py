class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Iterate the temperature
        # see if there is higher temp on the right ( j=i+1, len(temp))
        # if not, res[i] = 0
        # if yes, res[i] = j-i

        n = len(temperatures)
        res = [0]*(n)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temperatures[i] < temperatures[j]:
        #             res[i] = j-i
        #             break
        # return res

        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                val = stack.pop()
                res[val] = i - val
            stack.append(i)

        return res
                