class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        all_distances = {}
        distance_list = []
        for coordinates in points:
            distance = math.sqrt((coordinates[0] **2) + (coordinates[1] **2))
            if distance not in all_distances:
                all_distances[distance] = [coordinates]
            else:
                all_distances[distance].append(coordinates)
            distance_list.append(distance)
            
        distance_list.sort()
        final_distance_list = distance_list[:k]
        final_coordinates_list = []
        
        for key,value in enumerate(final_distance_list):
            if key < (len (final_distance_list) - 1):
                if value == final_distance_list[key+1]:
                    continue
            if any(isinstance(el,list) for el in all_distances[value]):
                final_coordinates_list.extend(all_distances[value])
            else:
                final_coordinates_list.append(all_distances[value])
        return final_coordinates_list