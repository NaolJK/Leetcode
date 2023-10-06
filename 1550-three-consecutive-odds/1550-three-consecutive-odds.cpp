class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        
        bool cnt = false;
        int left = 0, right = 1;
        while(left < arr.size()){
           
            while(right < arr.size() && arr[left] % 2 == 1 && arr[right] % 2 == 1){
                ++right;
            }

            if(right - left >= 3){
                cnt = true;
                break;
            } 
            
            left = right;
            ++right;
            
        }
        return cnt;
    }
};