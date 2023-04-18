class Solution {
public:
    int findComplement(int num) {
        if (num == 1){
            return 0;
        }
        unsigned int size = floor(log2(num) - 1); 
        bitset <32> bin(num); 
        int numberOfBits = floor(log2(num)) + 1;
        bin = (~bin) << (32-numberOfBits);
        bin = bin >> (32-numberOfBits);
        int mybit_int;
        mybit_int = (int)(bin.to_ulong());
        
        
        return mybit_int;
    }
};