class Solution {
public:
    int hammingDistance(int x, int y) {
      bitset <32> bit1(x); 
      bitset <32> bit2(y);
      bit1 = bit1 ^ bit2; 
      
      return bit1.count();  
    }
};