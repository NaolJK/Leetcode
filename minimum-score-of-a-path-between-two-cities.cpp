class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        vector<int> rank(n+1, INT_MAX);
        vector<int> repr(n+1);
        for(int i=0; i<n; ++i) repr[i] = i;
        int length = roads.size();

        function <int(int)> find;
        find = [&](int node){
            if(node == repr[node]){
                return repr[node];
            }
            repr[node] = find(repr[node]);
            return repr[node];
        };

        function <void(int, int, int)> unite;
        unite = [&](int x, int y, int dis){
            int r1 = find(x); 
            int r2 = find(y);

            if(rank[r1] <= rank[r2]){
                repr[r2] = r1;
                rank[r1] = min(dis, rank[r1]);
            }else{
                repr[r1] = r2;
                rank[r2] = min(dis, rank[r2]);
            }
        };

        for(auto& r : roads){
            unite(r[0], r[1], r[2]);
        }

        return rank[find(n)];
    }
};