class Solution {
public:
    int racecar(int target) {   
        queue <pair<long long, long long>> q;
        set <pair<long long , long long>>  seen;
        q.push({0, 1});
       
        
        
        int level = 0;
        while(!q.empty()){
            int length = q.size();
            
            for(int i=0; i < length; ++i){
                pair<int, int> node = q.front();
                
                q.pop();
                
                long long pos = node.first;
                long long speed = node.second;
                
                if(pos == target) return level;
                
                long long n_pos = pos + speed;
                long long n_speed = speed*2;
                
                if(seen.count(node)) continue;
                
                if(n_pos <= 10000 && n_pos > 0) q.push({n_pos, n_speed});
                
                if(speed > 0){
                    q.push({pos, -1});
                }else{
                    q.push({pos, 1}); 
                }
                
                seen.insert(node);
            }
            ++level;
        }
    
        return -1;
      
    }
           
 
};