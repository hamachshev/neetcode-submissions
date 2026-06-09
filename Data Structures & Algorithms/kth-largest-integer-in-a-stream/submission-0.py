import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        self.k = k


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        temp =[]
        for _ in range(self.k):
            temp.append(heapq.heappop(self.heap))
        for el in temp:
            heapq.heappush(self.heap, el)
        return -1 * temp[-1]


