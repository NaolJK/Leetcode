class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        
        vector<vector<int>> g(n);
        
        vector<int> indegree(n,0), ans;
        
        for(int i = 0; i < n; ++i){
            
            for(auto &x : graph[i]){
                
                g[x].push_back(i);
            }
        }
        for(int i = 0; i < n; ++i){
            
            for(auto &x: g[i]){
                
                indegree[x]++;
            }
        }
        queue<int> q;
       
        for(int i = 0; i < n; i++) if(!indegree[i]) q.push(i);
        
        while(!q.empty()){
            int node = q.front();
            q.pop();
            ans.push_back(node);
            
            for(auto vertex : g[node]){
                --indegree[vertex];
                if(!indegree[vertex]) q.push(vertex);
            }
    
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};