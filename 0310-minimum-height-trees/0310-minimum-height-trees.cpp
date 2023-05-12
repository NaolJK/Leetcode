class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        
        if(n < 2) return vector<int> { 0 };
        
        unordered_map <int, unordered_set<int>> graph(n);
        vector <int> indeg(n);
        for(int i=0; i < edges.size(); ++i){
            graph[edges[i][0]].insert(edges[i][1]);
            graph[edges[i][1]].insert(edges[i][0]);
            ++indeg[edges[i][0]];
            ++indeg[edges[i][1]];
        }
        
        queue <int> q;
        for(int i=0; i < n; ++i){
            if(indeg[i] == 1) q.push(i);
        }
        
        // while(!q.empty()){
        //     cout << q.front() << " ";
        //     q.pop();
        // }
        
        int count = n;
        
       
        while(count > 2){
            
            count-=q.size();
            queue <int> nq;
            
            while(!q.empty()){
                
                int node = q.front();
                q.pop();
                auto neigh = *graph[node].begin();
                     
                graph[neigh].erase(node);
                // cout << neigh << " " << indeg[neigh] << endl;
                if(--indeg[neigh] == 1) nq.push(neigh);
            }
            
            while(!nq.empty()){
                q.push(nq.front()); 
                nq.pop();
            }
        }
        
        
        vector <int> ans;
        while(!q.empty()){
            ans.push_back(q.front()); 
            q.pop();
        }
        
        return ans;
    }
};