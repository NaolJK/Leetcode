class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<int> graph[n + 1];
        
        for (auto e: edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        
        vector<bool> seen(n);
        
        function<bool(int)> dfs;
        dfs = [&](int node) {
            if (node == destination)
                return true;
            if (seen[node])
                return false;
            
            seen[node] = true;
            for (auto next_node: graph[node]) {
                if (dfs(next_node))
                    return true;
            }
            return false;
        };
        
        return dfs(source);
    }
};
