class Solution {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = bombs.size();
        vector <int> graph[n+1];
        
        for(int i=0; i < n; ++i){
            int x1 = bombs[i][0]; 
            int y1 = bombs[i][1];
            int r1 = bombs[i][2];
            
            for(int j=i+1; j<n; ++j){
                int x2 = bombs[j][0]; 
                int y2 = bombs[j][1];
                int r2 = bombs[j][2];
                
                long long distance = ceil(sqrt(pow((x2-x1), 2) + pow((y2-y1), 2)));
                
                if(distance <= r1){
                    graph[i].push_back(j);
                }
                
                if(distance <= r2){
                    graph[j].push_back(i);
                }
            }
        }
        
        
        int k=0;
     
        
        function <int(int, int)> bfs;
        bfs = [&] (int source, int len){
            queue <int> q;
            vector <bool> seen(len, false);
            q.push(source);
            seen[source] = true;
            int count = 1;
            
            while(!q.empty()){
                int node = q.front();
                q.pop();
                
                for(auto vertex : graph[node]){
                    if (seen[vertex]) continue;
                    ++count;
                    q.push(vertex);
                    seen[vertex] = true;
                }
                
            }
            return count;
        };
        
        int max_count = 0;
        for(int i=0; i <n; ++i){
            int c = bfs(i,n);
            max_count = max(c, max_count);
        }
        return max_count;
        
    }
};