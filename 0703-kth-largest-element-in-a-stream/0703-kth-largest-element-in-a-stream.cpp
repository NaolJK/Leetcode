class KthLargest {
priority_queue <int> h;
int length = 0;
public:
    KthLargest(int k, vector<int>& nums) {
        length = k;
        for(auto i : nums){
            int n = -1*i;
            h.push(n); 
            if(h.size() > length) h.pop();
        }
    }
    
    int add(int val) {
        int n = -1*val;
        h.push(n);
        if(h.size() > length) h.pop();
        
        return -1*h.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */