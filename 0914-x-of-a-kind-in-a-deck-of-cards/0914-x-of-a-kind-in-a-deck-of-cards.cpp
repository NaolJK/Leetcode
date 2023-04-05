class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        map<int, int> count;
        if (deck.size() <=1 ){
            return false;
        }
        
        for(auto &n : deck){
            if(count.count(n)){
                count[n]+=1;
            }else{
                count[n] = 1;
            }
        }
        vector <int> counts;
        
        for(auto it= count.begin(); it != count.end(); ++it){
            int n = it->second;
            counts.push_back(n);
        }
        
        for(int i=1; i<counts.size(); ++i){
            int n1 = counts[i]; 
            int n2 = counts[i-1];
            int gcd = __gcd(max(n1,n2), min(n1, n2)); 
            if(gcd == 1){
                return false;
            }
        }
        
        return true;
    }
    
};