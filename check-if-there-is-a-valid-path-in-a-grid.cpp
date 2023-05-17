class Solution {
public:
    bool hasValidPath(vector<vector<int>>& grid) {
        int n  = grid.size();
        int m = grid[0].size();
        map<int, vector<pair<int, int>>> moves{
            {1, {{0,-1}, {0, 1}}},
            {2, {{-1,0}, {1, 0}}},
            {3, {{0,-1}, {1,0}}},
            {4, {{0, 1},{1, 0}}},
            {5, {{0,-1}, {-1,0}}},
            {6, {{0, 1}, {-1, 0}}}
        };

        function <bool(pair<int, int>, vector<pair<int, int>>)> checkPairs;
        checkPairs = [&](pair<int, int> target, vector<pair<int, int>> paths){
            target = {-1*target.first, -1*target.second};
            for(auto& path : paths){
                if(path == target) return true;
            }
            return false;
        };

        vector <vector <pair<int, int>>> connected_nodes;
      
        vector< vector <pair <int, int > > > repr(n, vector<pair<int, int>>(m));
        vector <vector <int>> rank(n, vector<int>(m, 1));
        vector<vector<bool>>seen(n, vector<bool>(m, false));

        for(int i=0; i< n; ++i) for(int j=0; j <m ; ++j) repr[i][j] = {i, j};

        function <pair<int, int>(pair<int, int>)> find;
        find = [&](pair<int, int> pos){
            pair <int, int> c_pos = repr[pos.first][pos.second];
            if(c_pos != pos){
                repr[pos.first][pos.second] = find(c_pos);
            }
            return repr[pos.first][pos.second];
        };

        function <void(pair<int, int>, pair<int, int>)> unite;
        unite = [&](pair<int, int> x, pair<int, int> y){
            if(x == y) return;
            // cout << x.first << " " << x.second  << "   "<< y.first << " "<<y.second << endl;
             x = find(x);
             y = find(y);
            if(rank[x.first][x.second] < rank[y.first][y.second]){
                repr[x.first][x.second] = y;
            }else if(rank[x.first][x.second] > rank[y.first][y.second]){
                repr[y.first][y.second] = x;
            }else{
                repr[x.first][x.second] = y;
                ++rank[y.first][y.second];
            }
        };

        function <bool(pair<int, int>,pair<int,int>)> isConnected;
        isConnected = [&](pair<int, int> x , pair<int, int> y){
            return find(x) == find(y);
        };

          for(int i=0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                int op = grid[i][j];
                auto paths = moves[op];
                seen[i][j] = true;
                for(int k = 0; k < paths.size(); ++k){
                    int i_pos = i + paths[k].first;
                    int j_pos = j + paths[k].second;
                    // cout << i << " " << j << " "<< paths[k].first << " " << paths[k].second << "      "<< op << endl;
                    if(i_pos < n && j_pos < m && i_pos >=0 && j_pos >= 0 && !seen[i_pos][j_pos]){
                        int op2 = grid[i_pos][j_pos];
                        vector<pair<int, int>> t = moves[op2];
                        bool ans = checkPairs(paths[k], t);
                        
                        if(ans){
                        // cout << i << " " << j << " "<< i_pos << " " << j_pos << "      " <<  paths[k].first <<" "<<paths[k].second<< endl;
                        vector <pair<int, int>> c{make_pair(i, j), make_pair(i_pos, j_pos)};
                        // break;
                        // connected_nodes.push_back(c);
                         
                        unite({i, j},{i_pos, j_pos});
                        }
                    }
                }
                
            }
        }

        return  isConnected({0, 0}, {n-1,m-1});
        // return true;
    }

};