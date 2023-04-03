class Solution {
public:
    int findGCD(vector<int>& nums) {

        int minimum = *min_element(nums.begin(), nums.end());
        int maximum = *max_element(nums.begin(), nums.end());
        // cout << minimum << " " << maximum<< " ";
        return gcd(maximum, minimum);
      
    }
public:
    int gcd(int a, int b){
        if(b == 0){
            return a;
        }
        return gcd(b, a%b);
    }
};