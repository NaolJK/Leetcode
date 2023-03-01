class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        left_ans = [0,0]
        right_ans = [0,0]
        l, r = 0, len(nums)-1
        
        def predict(l, r, turn):
            if r == l:
                if turn:
                    return [nums[l],0]
                else:
                    return [0, nums[l]]
            
            if turn:
                left = predict(l+1,r,False)
                right = predict(l, r-1, False)
                left[0]+=nums[l]
                right[0]+=nums[r]
                if left[0] > right[0]:
                    return left
                return right

            else:
                left = predict(l+1,r,True)
                right = predict(l, r-1, True)
                left[1]+=nums[l]
                right[1]+=nums[r]
                if left[1] > right[1]:
                    return left
                return right

            
        ans = predict(l,r,True)
        print(ans)
        if ans[0] >= ans[1]:
            return True
        return False

                

                
                
                
            
        
       