class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {

        /*
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        */

        vector <vector<double>> glasses(101, vector<double>(101, 0));
        glasses[0][0] = poured;
        for(int i=0; i < 100; ++i){
            for(int j=0; j <= i; ++j){
                double p = glasses[i][j] - 1;
                if(p > 0){
                    glasses[i][j] = 1;
                    glasses[i+1][j]+=(p / 2);
                    glasses[i+1][j+1]+=(p/ 2);
                }
            }
        }
        
        // for(const auto& row : glasses){
        //     copy(row.begin(), row.end(), ostream_iterator<double>(cout, " ")); 
        //     cout << endl;
        // }
        return glasses[query_row][query_glass]; 
    }
};