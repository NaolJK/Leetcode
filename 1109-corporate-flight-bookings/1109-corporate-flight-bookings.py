class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0]*n
        
        for first,last,seat in bookings:
            result[first-1] += seat
            
            if last < n:
                result[last] -=seat
            
        return accumulate(result)
                
                    
        