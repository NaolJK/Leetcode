class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        total_players = len(players)
        total_trainers = len(trainers)
        
        p1 = 0
        p2 = 0
        count = 0
        
        while p1 < total_players and p2 < total_trainers:
            if players[p1] <= trainers[p2]:
                p1+=1 
                p2+=1
                count+=1
            else:
                p2+=1
        
        return (count)
                
            
        