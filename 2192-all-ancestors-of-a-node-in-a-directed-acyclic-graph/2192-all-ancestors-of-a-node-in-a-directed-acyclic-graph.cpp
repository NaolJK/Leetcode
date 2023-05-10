class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<set <int>> ans(n);
        vector <int> graph[n]; 
        vector <int> deg(n, 0);
        for(int i=0; i < edges.size(); ++i){
            graph[edges[i][0]].push_back(edges[i][1]);
            ++deg[edges[i][1]];
        }
        
        queue <int> q;
        for(int i=0; i < n; ++i) if(!deg[i]) q.push(i);
        
        while(!q.empty()){
            int node = q.front();
            q.pop();
            
            for(auto vertex : graph[node]){
                --deg[vertex];
                ans[vertex].insert(ans[node].begin(), ans[node].end());
                ans[vertex].insert(node); 
                if(!deg[vertex]) q.push(vertex);
            }
        }
        vector <vector <int> > result;
        for(auto n : ans){
            vector <int> r(n.begin(), n.end());
            result.push_back(r);
        }
        return result;
    }
};