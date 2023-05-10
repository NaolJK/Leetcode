class Solution {
    
     struct stringComp{
        bool operator()(pair<int,string>& a,pair<int,string>& b){
            if(a.first==b.first)
                return a.second > b.second;  
            return a.first<b.first; 
        }
    };
    
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        map <string, int> count;
        for(auto s : words){
            count[s]+=1;
        }
        vector<string> ans;
        
        priority_queue<pair<int, string> , vector<pair<int, string>>, stringComp> pq;
        for(auto [k, v] : count){
            pq.push({v, k});
        }
       
        while (k--) {
        ans.push_back(pq.top().second);   
        pq.pop();
    }
        return ans;
    }
};