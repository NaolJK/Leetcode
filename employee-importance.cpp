class Solution {
public:
    // int solve(map<int,Employee*> mp, int id){
    //     int ap = mp[id]->importance;
    //     for(auto i:mp[id]->subordinates){
    //         ap+=solve(mp,i);
    //     }
    //     return ap;
    // }
    int getImportance(vector<Employee*> employees, int id) {

        
        map<int,Employee*> mp;
        for(auto i:employees) mp[i->id]=i;
        
        function <int(int)> dfs;

        dfs = [&](int s){
            int ans = mp[s]->importance;
            for(auto& v : mp[s]->subordinates){
                ans+=dfs(v);
            }
            return ans;
        };
        return dfs(id);
    }
};