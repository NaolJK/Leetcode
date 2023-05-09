class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int n_row = maze.size();
        int n_col = maze[0].size();
        
        vector <int> xd{1, -1, 0 , 0};
        vector <int> yd{0, 0, 1, -1};
        
        vector <vector <bool >> seen(n_row, vector<bool>(n_col, false));
        queue<tuple <int, int, int>> q;
        q.push(make_tuple(entrance[0], entrance[1], 0));
        seen[entrance[0]][entrance[1]] = true;
        
        while(!q.empty()){
            auto [row, col, level] = q.front();
            q.pop();
           // cout << row << " " <<col << endl;
            if(row == n_row-1 || col == n_col-1){
                if(level > 0) return level;
            }
            if(row == 0 || col == 0){
                if(level > 0) return level;
            }
            
            for(int i=0; i < 4; ++i){
                int n_r = row + xd[i];
                int n_c = col + yd[i];
                if(n_r >=0 && n_r < n_row && n_c >=0 && n_c < n_col && !seen[n_r][n_c] && maze[n_r][n_c] == '.'){
                    q.push(make_tuple(n_r, n_c, level + 1));
                    seen[n_r][n_c] = true;
                }
            }
        }
        
        return -1;
    }
};