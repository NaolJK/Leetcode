class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        
        // vector<vector<pair<int, int>>> graph(n + 1);
        unordered_map<int,vector<pair<int, int>>> graph;
        
        vector<int> distance(n+1, INT_MAX);
        
        vector<bool> visited(n+1, false);
        
        distance[0] = 0;
        
        for(int i=0; i < times.size(); ++i){
            int u = times[i][0];
            
            int v = times[i][1];
            
            int w = times[i][2];
            
            graph[u].push_back({v, w});
        }
        
        
        priority_queue<pair<int, int>,vector<pair<int, int>>,greater<pair<int, int>>> pq; 
    
        pq.push({0, k});
        
        distance[k] = 0;
      
        
        while(!pq.empty()){
            
            auto [dist , node] = pq.top();
            
            pq.pop();
            
            if(visited[node]) continue;
            
            visited[node] = true;
            
            for(auto [vertex, weight] : graph[node]){
                
                int n_dis = dist + weight;
                
                if(n_dis < distance[vertex]){
                    distance[vertex] = n_dis;
                    pq.push({n_dis, vertex});
                } 
                
            }
        }
        
        for(auto el : distance){
            cout << el << " ";
        }
        if(find(distance.begin(), distance.end(), INT_MAX) != distance.end()) return -1;
        
        return *max_element(distance.begin(), distance.end());
    }
};