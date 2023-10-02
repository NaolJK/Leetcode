class Solution {
public:
    bool winnerOfGame(string colors) {
        
        vector<int> cnt(2, 0);
        
        for(int left = 0, right = 0; left < colors.size(); left = right){
            
            while(right < colors.size() && colors[right] == colors[left]){
                ++right;
            }
            
            if(right - left > 2){
                cnt[int(colors[left]) - int('A')] += (right - left - 2);
            }
        }
        
        
        return cnt[0] - cnt[1] > 0;
    }
};