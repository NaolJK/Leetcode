class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        vector<int> graph[n+1];
        vector <int> color(n+1, -1);
        for(auto& ed : dislikes){
            graph[ed[0]].push_back(ed[1]);
            graph[ed[1]].push_back(ed[0]);
        }




        function <bool(int)> bfs;
        bfs = [&](int s){
            queue<int> q;
            q.push(s);
            color[s] = 0;

            while(!q.empty()){
                int node = q.front();
                q.pop();

                for(auto& v : graph[node]){
                    if(color[v] == color[node]) return false;
                    if(color[v] == -1){
                        color[v] = 1 - color[node];
                        q.push(v);
                    }
                }
            }
            return true;
        };

        for(int i=1; i < n+1; i++){
            if(color[i] == -1){
                bool r = bfs(i);
                if(!r) return false;
            }
        }

        return true;
        
    }
};