class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        
        vector<int>p(n+1);
        vector<int>rank(n+1,1);

        for(int i = 0; i < n ; ++i){
            p[i] = i;
        }       

        
    function<int(int)> find = [&](int x) {
        int root = p[x];
        if(root != x){
            p[x] = find(root);
        }
        return p[x];
    };


    function <bool(int, int)> unite;
        unite = [&](int x, int y){
            int r1 = find(x); 
            int r2 = find(y);

            if(r1 == r2) return false;

            if(rank[r1] < rank[r2]){
                p[r1] = r2;
            }
            else if(rank[r1] > rank[r2]){
                p[r2] = r1;
            }
            else{
                p[r1] = r2;
                rank[r2]+=1;
            }
            return true;
        };

        for(auto& a : edges){
            
            bool r = unite(a[0], a[1]);
            if(!r) return a;
        }
        return vector<int> {};
        
    }
};