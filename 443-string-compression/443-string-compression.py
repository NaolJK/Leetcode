class Solution:
    def compress(self, chars: List[str]) -> int:
        fast = 0
        slow = 0
        length = len(chars)
        while fast < length:
		
            chars[slow] = chars[fast]
            count = 1
			
            while fast + 1 < length and chars[fast] == chars[fast+1]:
                fast += 1
                count += 1
			
            if count > 1:
                for i in str(count):
                    chars[slow+1] = i
                    slow += 1
            fast += 1
            slow += 1
        
        return slow