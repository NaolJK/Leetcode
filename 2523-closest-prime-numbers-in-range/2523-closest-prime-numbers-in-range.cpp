class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        vector <bool> primes (right+1, true);
        int length = ceil(sqrt(right));
        primes[0] = false;
        primes[1] = false;
        int j =0;
        for (int i =2; i <= length; ++i){
            j = i+i;
            while (j <= right){
                primes[j] = false;
                j+=i; 
            }
        }
        vector<int> prime_n;
        for(int i=left; i< primes.size(); ++i){
            if(primes[i] == true){
                prime_n.push_back(i);
            }
        }
        
        
        int min_gap = right;
        vector<int> ans;
        for (int i=1; i < prime_n.size(); ++i){ 
            if(prime_n[i] - prime_n[i-1] < min_gap){
                vector <int> n{prime_n[i-1] , prime_n[i]};
                ans = n;
                min_gap = prime_n[i] - prime_n[i-1];
            }
        }
        if(!ans.size()){
            vector <int> n{-1,-1};
            ans = n;
        }
        return ans;
    }
};