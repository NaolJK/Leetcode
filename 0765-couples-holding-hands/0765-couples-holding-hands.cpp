class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        int n = row.size();
        vector <int> pairs(n);
        
        for(int i =0; i < n ; i+=2){
            pairs[i] = i+1;
            pairs[i+1] = i;
        }
        
        int count = 0;
        for(int i=1; i< n; i+=2){
            if(pairs[row[i-1]] != row[i]){
                auto idx = find(row.begin(), row.end(), pairs[row[i-1]]);
                int index = 0;
                if(idx != row.end()){
                    index = idx - row.begin();
                }
                
                int temp = row[index];
                row[index] = row[i];
                row[i] = temp;
                ++count;
            }
        }
        
        return count;
    }
};