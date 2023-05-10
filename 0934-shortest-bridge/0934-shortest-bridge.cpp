class Solution {
public:
    int shortestBridge(vector<vector<int>>& grid) {
        int n = grid.size();
        queue <pair <int, int> > island_one; 
        queue <pair<int, int>> q;
        vector <int> xd{1, -1, 0, 0 };
        vector<int> yd{0, 0, 1, -1};
        vector <vector <bool>> seen(n , vector<bool>(n,false));
        
        for(int i=0; i < n; ++i){
            for(int j=0; j <n ; ++j){
                if(grid[i][j]){
                    island_one.push({i, j});
                    q.push({i, j});
                    seen[i][j] = true;
                    break;
                }
            }
            if(q.size()) break;
        }
    
    
    
    while(!q.empty()){
        auto [row, col] = q.front();
        q.pop();
        for(int i=0; i < 4; ++i){
            int n_r = row + xd[i];
            int n_c = col + yd[i];
            if(n_r >= 0 && n_c >= 0 && n_r < n && n_c < n && !seen[n_r][n_c] && grid[n_r][n_c]){
                q.push({n_r, n_c}); 
                island_one.push({n_r, n_c}); 
                seen[n_r][n_c] = true;
            }
        }
    }
    
    
    int level = 0;
    while(!island_one.empty()){
        int length = island_one.size();
        for(int _=0; _< length; ++_){
            auto [row, col] = island_one.front(); 
            island_one.pop();

            for(int i=0; i < 4; ++i){
            int n_r = row + xd[i];
            int n_c = col + yd[i];
            if(n_r >= 0 && n_c >= 0 && n_r < n && n_c < n && !seen[n_r][n_c]){ 
                if(grid[n_r][n_c]) return level;
                
                
                island_one.push({n_r, n_c}); 
                seen[n_r][n_c] = true;
             }
            }
        }
        ++level;
        
    }
    return -1;
}
    
};