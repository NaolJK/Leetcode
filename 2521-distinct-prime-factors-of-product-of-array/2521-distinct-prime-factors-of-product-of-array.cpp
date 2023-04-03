class Solution {
public:
    int distinctPrimeFactors(vector<int>& nums) {
        unordered_set<int> primes; 
        
        for(auto& num:nums){
            
            int d = 2;
            int n = num;
            
            
            while(d*d <= n){
                
                while(n%d == 0){
                    primes.insert(d); 
                    n = n / d;
                }
                ++d;
            }
            if(n > 1){
                primes.insert(n);
            }
        }
        
        return primes.size();
    }
};