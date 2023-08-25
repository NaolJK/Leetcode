class Solution {
public:
    int countGoodSubstrings(string s) {
        
        int left = 0;
        int cnt = 0;
        unordered_map<char, int> count;
        
       
        for(int right=0; right < s.size(); ++right){
            
            count[s[right]] += 1;
            
            while(left <= right && (count[s[right]] > 1 || right - left + 1 > 3)){
                count[s[left]]-=1;
                ++left;
            }
        
        if(right - left + 1 == 3){
            ++cnt;
        }
    }
        
        return cnt;
        
    }
};