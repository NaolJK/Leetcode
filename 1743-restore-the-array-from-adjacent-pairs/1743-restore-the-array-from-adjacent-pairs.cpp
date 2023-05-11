class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        int n = adjacentPairs.size() + 1;
        unordered_map <int, vector<int> > graph;
        unordered_map <int, int> cnt;
        for(int i=0; i < n-1; ++i){
            graph[adjacentPairs[i][0]].push_back(adjacentPairs[i][1]); 
            graph[adjacentPairs[i][1]].push_back(adjacentPairs[i][0]);
            cnt[adjacentPairs[i][0]]+=1;
            cnt[adjacentPairs[i][1]]+=1;
        }
        
        
        stack <int> st;
        unordered_set <int> seen;
        for(auto [v,c] : cnt){
            // cout << v << " "<< c<< endl;
            if(c == 1){
                st.push(v);
                seen.insert(v);
                break;
            }
        }
        
        vector <int> ans;
        
        while(!st.empty()){
            int node = st.top();
            ans.push_back(node);
            st.pop();
            for(auto vertex : graph[node]){
                if(seen.count(vertex)) continue;
                st.push(vertex); 
                seen.insert(vertex);
            }
        }
        
        return ans;
    }
};