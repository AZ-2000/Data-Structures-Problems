import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        stones_heap = stones
        while len(stones_heap) != 1:
            if not stones_heap:
                return 0
            if len(stones_heap) > 2:
                max_child = max(stones_heap[1], stones_heap[2])
            else:
                max_child = stones_heap[1]
            root_val = heapq.heappop_max(stones_heap)
            remainder= abs(root_val - max_child)
            if not remainder:
                heapq.heappop_max(stones_heap)
            else:
                stones_heap[0] = remainder
                heapq.heapify_max(stones_heap)

        if stones_heap:
            return stones_heap[0]
        else:
            return 0