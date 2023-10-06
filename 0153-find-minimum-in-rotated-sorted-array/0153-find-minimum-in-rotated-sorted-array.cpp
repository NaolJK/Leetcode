class Solution {
public:
    int findMin(vector<int>& nums) {
        
        int left = 0 , right = nums.size() - 1;
        
        while(nums[left] > nums[right] && left <= right){
            
            int mid = left + (right - left) / 2;
            
            if(nums[mid] > nums[right]){
                left  = mid + 1;
                
            }else{
                right  = mid;
            }
            cout << mid << " " << right << endl;
        }
        
        return nums[left];
    }
};