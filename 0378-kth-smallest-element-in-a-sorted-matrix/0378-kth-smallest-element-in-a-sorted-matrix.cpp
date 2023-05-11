class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        
        priority_queue<int> pq;
        for(int i=0; i < n; ++i){
            for(int j=0; j < n ; ++j){
                pq.push(-1*matrix[i][j]);
                // if(pq.size() > k) pq.pop();
            }
        }
        --k;
        while(k > 0){
            // cout << pq.top() << " ";
            pq.pop();
            --k;
        }
        return -1*pq.top();
    }
};