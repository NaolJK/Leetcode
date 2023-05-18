class Solution {
public:
    bool equationsPossible(vector<string>&equations){
        int n = 26;

        vector<int> graph[26];
        vector<int> repr(26 , 0);

        function<int(int)> find;
        find = [&](int node){
            int pr = repr[node];
            if(pr == node) return pr;
            return find(pr);
        };

        for(int i=0 ; i<26 ; i++){
            repr[i] = i;
        }
        int len = equations.size();

        for(int i=0 ; i<len ; i++){

            string equa = equations[i];

            int s = equations[i][0]-97;

            int d = equations[i][3]-97;

            char op1 = equations[i][1];

            if(op1 == '='){
                int p1 = find(s);
                int p2 = find(d);

                if(p1!=p2){
                    repr[p1] = p2;
                }
            }
        }

        for(int i=0 ; i<len ; i++){

            string equa = equations[i];

            int s = equations[i][0]-97;

            int d = equations[i][3]-97;

            char op1 = equations[i][1];

            if(op1=='!'){

            int p1 = find(s);

            int p2 = find(d);

            if(p1 == p2){
                return false;
            }

    }
        }

        return true;
    }
};