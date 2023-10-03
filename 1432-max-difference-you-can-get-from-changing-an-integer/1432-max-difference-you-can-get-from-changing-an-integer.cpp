class Solution {
public:
    int maxDiff(int num) {
        int i = 1;
        string mnm = to_string(num);
    
        if(mnm[0] == '1'){
            // cout << int(mnm[i] - int('0')) << endl;
            while(i < mnm.size() && int(mnm[i] - int('0')) <= 1){
                ++i;
            }
            
            if(i < mnm.size()){
                char fx = mnm[i];
                while(i < mnm.size()){
                    if(mnm[i] == fx){
                        mnm[i] = '0';
                    }
                    ++i;
                }
            }
        }else{
            char fx = mnm[0];
            for(int i=0; i < mnm.size(); ++i){
                if(mnm[i] == fx) mnm[i] = '1';
            }
        }
        
        
        
        string mxm = to_string(num);
        i = 0;
        if(mxm[0] == '9'){
            while(i < mxm.size() && mxm[i] == '9'){
                ++i;
            }
             if(i < mxm.size()){
                char fx = mxm[i];
                while(i < mxm.size()){
                    if(mxm[i] == fx){
                        mxm[i] = '9';
                    }
                    ++i;
                }
            }
        }else{
             char fx = mxm[0];
            for(int i=0; i < mxm.size(); ++i){
                if(mxm[i] == fx) mxm[i] = '9';
            }
        }
        
        int mini = stoi(mnm);
        int maxm = stoi(mxm);
        // cout << mini << endl;
        return maxm - mini;
    }
};