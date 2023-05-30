class Solution {

public:
    int findTargetSumWays(vector<int>& nums, int target) {

        map <pair<int, int>, int> dp;
        int length = nums.size();
        function <int(int, int)> recursive;

        recursive = [&](int i, int tot){


            if(tot == target && i == length){
                return 1;
            }

            if(dp.count(make_pair(i, tot))) return dp[make_pair(i, tot)];
            if(i >= length){
                return 0;
            }

            int pos = recursive(i+1, tot+nums[i]);
            int neg = recursive(i+1, tot - nums[i]);

            dp[make_pair(i, tot)] = pos + neg;
            return pos + neg;
        };

        return recursive(0,0);
    }
};