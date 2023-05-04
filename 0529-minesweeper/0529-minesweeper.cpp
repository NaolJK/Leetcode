class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int row = board.size();
        int col = board[0].size();
        
        queue < pair <int, int>> q;
        q.push({click[0], click[1]});
        
        vector <int> rd{1,-1, 0, 0, -1, 1, 1, -1};
        vector <int> cd{0, 0, 1, -1, 1, 1, -1, -1};
        
        while(!q.empty()){
            auto [r, c] = q.front();
            
            q.pop();
            if(board[r][c] == 'M'){
                board[r][c] = 'X';
            }
            else if(board[r][c] == 'E'){
                int mines = 0;
                for(int i=0; i <8; ++i){
                    int n_row = rd[i] + r;
                    int n_col = cd[i] + c;
                    if(n_row >=0 && n_row < row && n_col >=0 && n_col < col && board[n_row][n_col] == 'M'){
                        ++mines;
                    }
                }
                string s_num = to_string(mines);
                if(mines > 0) board[r][c] = s_num[0];
                else board[r][c] = 'B';
                
                if(mines == 0){
                    for(int i=0; i < 8; ++i){
                    int n_row = rd[i] + r;
                    int n_col = cd[i] + c;
                    if(n_row >=0 && n_row < row && n_col >=0 && n_col < col && (board[n_row][n_col] == 'E' || board[n_row][n_col] == 'M')){
                        q.push({n_row, n_col});
                 }
                        
              }
           }
     }
   }
        
        return board;
}
};