import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        points = [((point[0]**2 + point[1]**2)** (1/2), point) for point in points ]
        heapq.heapify(points) 
        for _ in range(k):
            res.append(heapq.heappop(points)[1]) 
        return res
     