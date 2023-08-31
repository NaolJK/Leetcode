class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int row = grid.size();
        int col = grid[0].size();
        
        
        for(int i=0; i < row; ++i){
            for(int j=0; j < col ; ++j){
                if(i == 0 && j ==0){
                    continue;
                }
                
                if(i > 0  && j <= 0){
                    grid[i][j] = grid[i-1][j] + grid[i][j];
                    continue;
                }
                
                if(i <= 0 && j > 0){
                    grid[i][j] = grid[i][j-1] + grid[i][j];
                    continue;
                }
                
                grid[i][j] = min(grid[i-1][j] , grid[i][j - 1]) + grid[i][j];
            }
        }
        
        return grid[row-1][col-1];
    }
};