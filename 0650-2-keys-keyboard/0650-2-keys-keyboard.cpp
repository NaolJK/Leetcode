class Solution {
public:
    int minSteps(int n) {
       vector <int> primes;
        int d = 2;
        
        while(d*d <= n){
            while(n % d == 0){
                primes.push_back(d);
                n = n / d;
            }
            ++d;
        }
        if(n > 1){
            primes.push_back(n);
        }
        int ans = 0;
        for(auto &n:primes){
            if(n ==1){
                continue;
            }
            ans+=n;
        }
        return ans;
        
    }
};