class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        first_fruit = -2
        second_fruit = -2
        
        first_fruit_count = 0
        # second_fruit_count = 0
        
        current_max = 0
        maximum = 0
        
        for fruit in fruits:
            if fruit == first_fruit or fruit == second_fruit:
                current_max +=1
            else:
                current_max = first_fruit_count + 1
            
            if fruit == first_fruit:
                first_fruit_count +=1
            else:
                first_fruit_count = 1
                second_fruit = first_fruit
                first_fruit = fruit
            
            maximum = max(current_max , maximum)
        
        return maximum
                
        