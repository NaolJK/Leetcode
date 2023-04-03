class Solution {
public:
    bool hasAlternatingBits(int n) {
        int length = floor(log2(n));
        bitset <32> bin(n);
        bool ans = true;
        for(int i = 1; i <= length; ++i){
            if (bin[i] == bin[i-1]){
                ans = false;
                break;
            }
        }
        
        return ans;
    }
};