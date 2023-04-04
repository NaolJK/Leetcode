class Solution {
int ans = 0;
int seen ;
public:
    int countArrangement(int n) {
        vector <int> path;
        backtrack(1,n);
        return ans;
    }
public:
    void backtrack(int index, int n){
        if(index > n){
            // cout << index << endl;
            ++ans;
            return;
        }
        
        for (int i=1; i <= n; i++){
            int v = seen & (1<<i);
            if(v){
                continue;
            }
    
            if((index % i == 0) || (i % (index) == 0)){
                seen|=(1<<i);
                backtrack(index+1 , n);
                seen &= ~(1<<i);
            }
            
        }
    }
};