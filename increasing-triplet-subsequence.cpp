class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {

    vector<int> next_big(nums.size(),-1);
    vector<int> pre_small(nums.size(),-1);
    stack<int> stk;
    stack<int> stk2;
    
    for(int i=0;i<nums.size();i++){
        while(!stk.empty() && nums[stk.top()] < nums[i]){
            next_big[stk.top()]=i;
            stk.pop();
        }
        stk.push(i);
    }
    
    for(int j=nums.size()-1;j>=0;j--){
        while(!stk2.empty() && nums[stk2.top()] > nums[j]){
            pre_small[stk2.top()]=j;
            stk2.pop();
        }
        stk2.push(j);
    }
    
    for(int i=0;i<nums.size();i++){
        if(pre_small[i]!=-1 && next_big[i]!=-1){return true;}
    }
    
    return false;
}
};