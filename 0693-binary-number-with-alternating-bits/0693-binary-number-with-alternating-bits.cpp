class Solution {
public:
    bool hasAlternatingBits(int n) {
        long int xorval = (n ^ (n >> 1));
        bool ans = !(xorval & (xorval + 1));
        return ans;
        }
};