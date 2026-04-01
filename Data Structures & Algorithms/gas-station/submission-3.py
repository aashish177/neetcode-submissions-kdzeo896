class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        n = len(gas)
        for i in range(n):
            tank = 0
            print("i: ", i)
            tank += gas[i]
            tank -= cost[i]

            if tank<0:
                continue
            print("---------")

            for j in range(n):
                k = (i + j + 1) % n
                print("k: ", k)
                tank+=gas[k]
                tank-=cost[k]
                if tank < 0:
                    break
                print("tank: ", tank)
            print("-----")

            if tank>0:
                return i
        return -1 if tank < 0 else 0