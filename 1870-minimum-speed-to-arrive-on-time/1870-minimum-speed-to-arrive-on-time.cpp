class Solution {
   public: int minSpeedOnTime(vector<int>& dist, double hour) {
        
        int left = 1;
        int right = 1e7;
        int minSpeed = -1;
        
        function <double(int)> check = [&](int speed){
            
            double t = 0;
            for(int i=0; i < dist.size(); ++i){
                double ti = (double) dist[i]/ (double) speed;
                if(i + 1 == dist.size()){
                    t+=ti;
                }else{
                    t+=ceil(ti);
                }
            }
            
            return t;
        };
        
        
        
        while (left <= right) {
            
            int mid = (left + right) / 2;
            

            if (check(mid) <= hour) {
                minSpeed = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return minSpeed;
    }
};
