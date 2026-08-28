import heapq

def euclidean_distance(arr1, arr2):
    x = (arr1[0]-arr2[0])**2
    y = (arr1[1] -arr2[1]) **2
    distance = (x+y) ** 0.5
    return distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        for i in range(len(points)):
            distance = euclidean_distance(points[i], [0,0])
            distances.append((distance, points[i]))
        
        heapq.heapify_max(distances)
        while len(distances) > k:
            heapq.heappop_max(distances)

        for i in range(k):
            res.append(distances[i][1])
        
        return res


        



        
