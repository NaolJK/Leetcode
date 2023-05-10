class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        make_heap(stones.begin(), stones.end());
        
        while(stones.size() > 1){
            pop_heap(stones.begin(), stones.end());
            int f = stones[stones.size()-1];
            stones.pop_back();
            pop_heap(stones.begin(), stones.end());
            int s = stones[stones.size()-1];
            stones.pop_back();
            int r = abs(f - s); 
            if(r > 0){
                stones.push_back(r);
                push_heap(stones.begin(), stones.end());
            }
        }
        if(stones.size()) return stones[0];
        else return 0;
    }
};