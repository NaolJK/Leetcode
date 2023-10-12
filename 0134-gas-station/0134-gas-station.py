class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        arr = []
        
        n = len(gas)
        
        for i in range(len(gas)):
            
            diff = gas[i] - cost[i]
            
            arr.append(diff)
            
        prefix = list(accumulate(arr))
        
        mnm = min(prefix)
        
        start = 0
        
        for i in range(len(gas)):
            
            if prefix[i] == mnm:
                start = i
        
        # print(start + 1)
        
        possible = -1
        
        gas = gas*2
        
        arr = cost*2
        
        # print(arr)
        
        total = 0
        
        for i in range(start+1, len(arr)):
            
            total+=(gas[i] - arr[i])
            
            # print(total, gas[i] - arr[i], gas[i])
            
            if i % n == start and total >= 0:
                possible = (start + 1) % n
                return possible
            
            if total < 0:
                return -1
                
            
                
        return possible
        