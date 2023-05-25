class Solution {
public:

    vector<int> prevPermOpt1(vector<int>& arr) {
        
        int n = arr.size();

        int i, j = n-1;

        for(i = n - 2; i >= 0; --i){
            if(arr[i+1] < arr[i]){
                // cout << arr[i+1] << " " << arr[i] << endl;
                break;
            };
        } 
        

        if(i < 0) return arr;
        
        
        while((arr[j] >= arr[i] && j > i) || (arr[j-1]==arr[j])){
            cout << arr[j] << " " << arr[i] << endl;
            j--;
        }
            
        swap(arr[i], arr[j]);
  
         return arr;      
    }
};