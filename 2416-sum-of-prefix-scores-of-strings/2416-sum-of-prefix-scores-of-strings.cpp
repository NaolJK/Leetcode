struct TrieNode{
    unordered_map<char, TrieNode*> children;
    int cnt = 0;
    bool isEnd = false;
    
};

class Trie{
    public:
        TrieNode* root = new TrieNode();
    
    public:
        void insert(string s){
            TrieNode* curr = root;
            
            for(auto c : s){
                if(!curr->children.count(c)){
                    curr->children[c] = new TrieNode();
                
                }
                curr = curr->children[c];
                curr->cnt += 1;
            }
            curr->isEnd = true;
        }
    public:
        int returnCount(string s){
            int ans = 0;
            TrieNode* curr = root;
            for(auto c : s){
                if(curr->children.count(c)){
                    curr = curr->children[c];
                }
                ans += curr->cnt;
            }
            return ans;
        }
        
};

class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        Trie* trie = new Trie();
        for(auto str : words){
            trie->insert(str);
        }
        
        vector<int> ans;
        for(auto str : words){
            int res = trie->returnCount(str);
            ans.push_back(res);
        }
        return ans;
    }
};