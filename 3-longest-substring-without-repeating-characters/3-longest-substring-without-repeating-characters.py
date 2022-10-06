class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        all_str = []
        
        left_pointer = 0
        right_pointer = 0
        maximum_number = 0
        
        while right_pointer < len(s):
            if s[right_pointer] not in all_str:
                all_str.append(s[right_pointer])
                right_pointer +=1
                maximum_number = max(maximum_number, len(all_str))
            else:
                all_str.remove(s[left_pointer])
                left_pointer+=1
                # print(left_pointer)
                
    
            
        return maximum_number
        