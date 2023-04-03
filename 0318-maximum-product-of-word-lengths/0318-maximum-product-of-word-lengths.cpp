class Solution {
public:
    int maxProduct(vector<string>& words) {
        vector <int> bits;
        for(int i =0; i < words.size(); ++i){
            int bin = 0;
            string s = words[i];
            for(auto& st : s){
                bin |= 1 << (st - 'a');
            }
            
            bits.push_back(bin);
        }
        int maximum = 0;
        
        for (int i=0; i < bits.size(); ++i){
            for(int j =i+1; j < bits.size(); ++j){
                if ((bits[i] & bits[j]) == 0){
                    maximum = max(maximum , (int)words[i].length() * (int)words[j].length());
                }
            }
        }
        return maximum;
    }
};