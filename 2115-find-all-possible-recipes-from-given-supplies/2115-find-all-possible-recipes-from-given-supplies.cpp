class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        
        map <string, vector<string>> g;
        map <string, int> deg;
        
        
        for(int i=0; i < recipes.size(); ++i){
            for(int j=0; j < ingredients[i].size(); ++j){
                g[ingredients[i][j]].push_back(recipes[i]);
                deg[recipes[i]]+=1;
            }
        }
        
        queue<string> q;
        unordered_set <string> recipe;
        unordered_set <string> seen;
        vector <string> ans;
        for(auto r : recipes){
            recipe.insert(r);
        }
        for (auto r : supplies){
            q.push(r);
        }
        
        while(!q.empty()){
            string gr = q.front();
            q.pop();
            if(recipe.count(gr)){
                ans.push_back(gr);
            }
            for(auto v : g[gr]){
                deg[v]-=1;
                if(!seen.count(v) && deg[v] <= 0){
                    q.push(v);
                    seen.insert(v);
                }
            }
        }
        
        return ans;
        
    }
};