class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        gasConsumed = 0
        start = 0
        totalGasConsumed = 0
        
        for i in range(len(gas)):
            gas_amt = gas[i]
            gas_needed = cost[i]

            gasConsumed = gas_amt - gas_needed

            totalGasConsumed += gasConsumed

            if totalGasConsumed < 0:
                totalGasConsumed = 0
                start = i+1
        
        return start