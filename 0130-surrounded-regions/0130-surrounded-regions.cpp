class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int r = board.size(), c = board[0].size();
        
        vector < vector <bool> > seen(r, vector<bool>(c, false));
        queue <pair <int, int>> q;
        
        
        for(int i=0; i < r; ++i){
            for(int j=0;  j < c ; ++j){
                if(i == 0 || i == r-1 || j == 0 || j == c-1){
                    if(board[i][j] == 'O'){
                        q.push({i, j});
                        seen[i][j] = true;
                    }
                }
            }
        }
        
        
        vector <int> rd{1, -1, 0, 0};
        vector <int> cd{0, 0, 1, -1};
        
        while(!q.empty()){
            auto [row, col] = q.front(); 
            q.pop();
            
            for(int i = 0; i < 4; ++i){
                int n_r = row + rd[i];
                int n_c = col + cd[i];
                
                if(n_r >= 0 && n_r < r && n_c >= 0 && n_c < c && !seen[n_r][n_c] && board[n_r][n_c] == 'O'){
                    q.push({n_r, n_c});
                    seen[n_r][n_c] = true;
                }
            }
        }
        
        
        for(int i = 0; i < r; ++i){
            for(int j=0; j < c; ++j){
                if(!seen[i][j] && board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
            }
        }
        
        // return board;
    }
};