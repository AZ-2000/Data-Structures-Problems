class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        elif len(gas) == 1:
            return 0
        elif len(gas) == 2:
            if gas[0] - cost[0] >= 0:
                return 0
            elif gas[1] - cost[1] >= 0:
                return 1

        else:
            diff = 0
            for i in range(len(gas)):
                if gas[i] - cost[i] <= 0:
                    continue
                if i == len(gas)-1:
                    if diff <  gas[i]-cost[i] + gas[0] - cost[0]:
                        diff =  gas[i]-cost[i] + gas[0] - cost[0]
                        idx = i
                    continue
                if diff < gas[i]-cost[i] + gas[i+1] - cost[i+1]:
                    diff = gas[i]-cost[i] + gas[i+1] - cost[i+1]
                    idx = i
            return idx 
