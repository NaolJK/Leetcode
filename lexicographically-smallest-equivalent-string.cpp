class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        map <char, char> repr;
        for(int i=0; i < s1.size(); ++i){
            repr[s1[i]] = s1[i];
            repr[s2[i]] = s2[i];
        }

        function <char(char)> represent;
        represent = [&](char c){
            return repr[c];
        };

        function <void(char, char)> unite;
        unite = [&](char x, char y){

            char r1 = represent(x);
            char r2 = represent(y);
            // cout << r1 << " "<< r2 << "   " << x << " " << y << endl;
            if(r1 >= r2){
                for(auto& [k, v] : repr){
                    if(v == r1) v = r2;
                }
            }else{
                for(auto& [k, v] : repr){
                    if(v == r2) v = r1;
                }
            }
            // cout << represent(x) <<" "<< represent(y) << endl;

        };
        for(int i=0; i < s1.size(); ++i){
            unite(s1[i], s2[i]);
        }

        string ans = "";
        for(int i=0; i < baseStr.size(); ++i){
            if(!repr[baseStr[i]]){
                ans+=baseStr[i];
                continue;
            }
            ans+=repr[baseStr[i]];
        }

        return ans;

    }
};