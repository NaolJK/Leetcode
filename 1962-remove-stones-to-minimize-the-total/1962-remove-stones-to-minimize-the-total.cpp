class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue <int> pq;
        int ans = 0;
        for(auto n:piles){
            pq.push(n);
        }
        
        while(k--){
            double n = pq.top();
            pq.pop();
            int res = ceil(n / 2);
            pq.push(res);
        }
        
        while(!pq.empty()){
            ans+=(pq.top());
            // cout << pq.top() << " ";
            pq.pop();
        }
        return ans;
    }
};