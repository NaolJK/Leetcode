class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ## 4 9 9 7 4 5

        prefix = list(accumulate(nums))

        cnt = defaultdict(int)

        ans = 0
        cnt[0] = 1

        for n in prefix:

            diff = n % k

            ans+=cnt[diff]

            cnt[diff] += 1

         

        return ans










        
        