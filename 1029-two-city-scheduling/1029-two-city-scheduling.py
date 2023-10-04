class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        ans = [0, 0]
        cc1, cc2 = 0, 0
        costs.sort(key= lambda x: abs(x[0] - x[1]), reverse=True)
        # print(costs)
        for c1, c2 in costs:
            if c1 < c2 and cc1 < len(costs)//2:
                
                ans[0]+=c1
                # print("c1", c1, ans)
                cc1+=1
            elif c2 < c1 and cc2 < len(costs)//2:
                ans[1]+=c2
                # print("c2", c2 , ans)
                cc2+=1
            elif cc1 < len(costs)//2:
                
                ans[0]+=c1
                cc1+=1
                # print("not c1", c1, ans)
            else:
                ans[1]+=c2
                cc2+=1
                # print("not c2", c2 , ans)
            
            
        return sum(ans)
        