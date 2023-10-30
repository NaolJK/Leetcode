class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        vector<int> linesweep(2050+1, 0);
        for(int i=0; i < logs.size(); ++i){
            int start = logs[i][0];
            int end = logs[i][1];
            ++linesweep[start]; 
            --linesweep[end];
        }
        int running = 0;
        int ans = -1;
        int res = -1;
        for(int i=0; i <= 2050; ++i){
            running += linesweep[i];
            if(ans < running){
                ans = running;
                res = i;
            }
        }

        return res;
    }
};