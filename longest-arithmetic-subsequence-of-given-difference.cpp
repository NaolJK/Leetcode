class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        unordered_map<int, int> memo;

        for(int i = 0; i < arr.size(); ++i){
            if(!memo.count(arr[i] - difference)){
                memo[arr[i]] = 1;
            }else{
                if (!memo.count(arr[i])){
                    memo[arr[i]] += memo[ arr[i] - difference] + 1;
                }else{
                memo[arr[i]] = max(memo[arr[i]-difference]+1,memo[arr[i]]);
                }
            }
        }

        auto pr = max_element(memo.begin(), memo.end(), [](const auto &x, const auto &y){
        return x.second < y.second;
        }
        );

        return pr->second;
    }
};