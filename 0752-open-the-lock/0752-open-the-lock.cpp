class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        
        
        
        unordered_set<string> deadends_keys(begin(deadends), end(deadends));
        
        
        string lock, lock_;
        
        if(deadends_keys.count("0000")) return -1;
        if(target == "0000") return 0;
        
        int ans=0;
        
        queue<string> q;
        
        q.push("0000");
        
        while(!q.empty()){
            ans++;
            int length = q.size();    
            
            for(int k=0;k<length;k++){
                
                
                lock_= q.front();
                q.pop();
                
                for(int i=0;i<4;i++){
                    lock = lock_;
                    
                    lock[i]= (lock[i]=='9') ? '0' : ++lock[i];
                    
                    if(lock == target) return ans;
                    
                    if(!deadends_keys.count(lock)){
                        q.push(lock);
                        deadends_keys.insert(lock);
                    }
                    
                    lock = lock_;
                    lock[i]= lock[i]=='0' ? '9' : --lock[i];
                    if(lock == target) return ans;
                    
                    if(deadends_keys.count(lock)) continue;
                        q.push(lock);
                        deadends_keys.insert(lock);
                    
                }
            }
        }
        
        return -1;
    }
};