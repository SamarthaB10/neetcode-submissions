import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1: 
            f = -heapq.heappop(maxHeap)
            s = -heapq.heappop(maxHeap)


            if f > s: 
                heapq.heappush(maxHeap,-(f-s))

        
        return 0 if not maxHeap else -(maxHeap[0])