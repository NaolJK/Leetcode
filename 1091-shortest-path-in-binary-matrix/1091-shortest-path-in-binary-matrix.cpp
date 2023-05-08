class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        
        vector <int> x_u{1, -1, 0, 0, 1, 1, -1, -1};
        vector <int> y_u{0, 0, 1, -1, 1, -1, 1, -1};
        int n_row = grid.size();
        int n_col = grid[0].size();
        
        vector <vector <bool> > seen(grid.size(), vector<bool> (grid[0].size(),false)); 
        queue <tuple <int, int, int> > q;
        if(grid[0][0] == 1) return -1;
        q.push(make_tuple(0, 0, 1));
        seen[0][0] = true;
        int ans = -1; 
        while(!q.empty()){
            auto [row, col, level] = q.front();
            q.pop();
            if(row == n_row -1 && col == n_col -1){
                cout << row << " " << col << " ";
                ans = level;
                break;
            }
            
            for(int i=0; i < 8; ++i){
                int n_r = row + x_u[i]; 
                int n_c = col + y_u[i];
                if(n_r >= 0 && n_r < n_row && n_c >=0 && n_c < n_col && !seen[n_r][n_c] && grid[n_r][n_c] == 0){
                    q.push(make_tuple(n_r, n_c, level+ 1));
                    seen[n_r][n_c] = true;
                }
            }
        }
        return ans;
        }
};