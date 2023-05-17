class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<int>p(n);
        vector<int>rank(n,1);

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


        function <void(int, int)> unite;
        unite = [&](int x, int y){
            // cout << x << y << endl;
            
            int r1 = find(x); 
            int r2 = find(y);
            if(r1 == r2) return;

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
        };
        for(auto& a : edges){
            unite(a[0], a[1]);
        }
        return find(source) == find(destination);
    }
};