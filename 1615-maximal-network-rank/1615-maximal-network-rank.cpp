class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        vector <int> graph[n+1];
        vector <int> degree(n,0);
        for(auto &n : roads){
            graph[n[0]].push_back(n[1]); 
            graph[n[1]].push_back(n[0]);
            degree[n[1]]+=1; 
            degree[n[0]]+=1;
        }
        
        function <bool(int, int)> check;
        check = [&](int source, int dest){
            for(auto n: graph[source]){
                if(n == dest){
                    return true;
                }
            }
            return false;
        };
        
        int maximum = 0;
        int total =0;
        for(int i=0; i<n; ++i){
            for(int j =i+1; j < n ; ++j){
                bool ans = check(i,j);
                total = degree[i] + degree[j];
                if(ans) total-=1;
                maximum = max(maximum, total);
            }
        }
        
        return maximum;
    }
};