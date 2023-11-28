class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {

        int row = grid.size();
        int col = grid[0].size();
        vector<vector<bool>> seen(row, vector<bool>(col, false));

        vector<int> xpos{1, -1, 0, 0};
        vector<int> ypos{0, 0 , 1, -1};

        function <bool(int, int)> check = [&](int i, int j){
            return (i >=0 && i < row && j >= 0 && j < col);
        };

        function <void(int, int)> bfs = [&](int r, int c){
            queue<pair<int, int>> q;
            q.push({r, c});
            seen[r][c] = true;
            while(!q.empty()){
                int ro = q.front().first;
                int co = q.front().second;
                q.pop();

                for(int i=0; i < 4; ++i){
                    int nr = ro + xpos[i];
                    int nc = co + ypos[i];

                    if(check(nr, nc) && grid[nr][nc] == '1' && !seen[nr][nc]){
                        seen[nr][nc] = true;
                        // cout << nr << " " << nc << " " << grid[nr][nc] << endl;
                        q.push({nr, nc});
                    }
                }

            }
        };

        int ans = 0;
        for(int i=0; i < row; ++i){
            for(int j=0;  j < col; ++j){
                if(!seen[i][j] && grid[i][j] == '1'){
                    cout << i << " " << j << endl;
                    bfs(i, j);
                    ++ans;
                }
            }
        }

        return ans;
        
    }
};