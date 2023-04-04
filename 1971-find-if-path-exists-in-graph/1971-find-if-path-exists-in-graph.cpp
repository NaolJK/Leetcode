class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<int> graph[n + 1];
        
        for (auto e: edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        
        queue<int> Q;
        vector<bool> visited(n + 1);
        // unordered_set<int> visited;
        Q.push(source);
        visited[source] = true;
        // visited.insert(source);
        while (!Q.empty()) {
            int node = Q.front();
            Q.pop();
            if (node == destination)
                return true;
            for (auto u: graph[node]) {
                if (visited[u])
                    continue;
                // if (visited.count(u))
                    // continue;
                Q.push(u);
                visited[u] = true;
                // visited.insert(u);
            }
        }
        return false;
    }
};


// class Solution:
//     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
//         graph = defaultdict(list)
        
//         for a, b in edges:
//             graph[a].append(b)
//             graph[b].append(a)
            
//         stack = []
//         stack.append(source)
//         seen = set([source])
        
//         while stack:
//             cur = stack.pop()
            
//             if cur == destination:
//                 return True
            
//             for next_node in graph[cur]:
//                 if next_node not in seen:
//                     seen.add(next_node)
//                     stack.append(next_node)
                    
//         return False