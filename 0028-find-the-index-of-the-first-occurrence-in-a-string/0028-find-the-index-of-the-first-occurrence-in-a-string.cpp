class Solution {
public:
    int strStr(string haystack, string needle) {
        
        const int pow = 31; 
        
        const int mod = 1e9 + 9;
        
        int S = needle.size(), T = haystack.size();

        vector<long long> p_pow(max(S, T)); 
        
        p_pow[0] = 1; 
        
        for (int i = 1; i < (int)p_pow.size(); i++) 
            p_pow[i] = (p_pow[i-1] * pow) % mod;

        vector<long long> h(T + 1, 0); 
        
        
        for (int i = 0; i < T; i++)
            
            h[i+1] = (h[i] + (haystack[i] - 'a' + 1) * p_pow[i]) % mod; 
        
        long long h_n = 0; 
        for (int i = 0; i < S; i++) 
            h_n = (h_n + (needle[i] - 'a' + 1) * p_pow[i]) % mod; 

 
        
        int ans = -1;
        
        for (int i = 0; i + S - 1 < T; i++) {
            
            long long cur_h = (h[i+S] + mod - h[i]) % mod;
            
            if (cur_h == h_n * p_pow[i] % mod){
                ans = i;
                break;
            }
        }
        return ans;
    }
};