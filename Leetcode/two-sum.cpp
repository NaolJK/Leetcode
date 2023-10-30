class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for(int i=0; i < nums.size(); ++i){
            int x = target - nums[i];
            if(seen.count(x)){
                return {i, seen[x]};
            }
            seen[nums[i]] = i;
        }

        return {-1, -1};
    }
};