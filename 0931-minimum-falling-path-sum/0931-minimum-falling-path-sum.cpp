class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int length = matrix.size();
        
        for(int i = length-2 ; i > -1; --i){
            for(int j = 0; j < length; ++j){
                int left_diagonal = 99999;
                if(j > 0){
                    left_diagonal = matrix[i+1][j-1] + matrix[i][j];
                }
                
                int right_diagonal = 99999;
                if(j < length-1){
                   right_diagonal = matrix[i+1][j+1] + matrix[i][j];
                }
                int bottom = matrix[i][j] + matrix[i+1][j];
                
                matrix[i][j] = min({left_diagonal, right_diagonal, bottom});
            }
            
        }
        
        int mini = *min_element(matrix[0].begin(), matrix[0].end());
        
        return mini;
    }
};