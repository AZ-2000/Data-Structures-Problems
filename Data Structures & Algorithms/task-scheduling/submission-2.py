import heapq
from collections import deque as queue
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = {}
        store = queue()
        cnter = 0
        for t in tasks:
            freq[t] = 1 + freq.get(t, 0)
        
        pq_list = [(-value,key) for key, value in freq.items()]
        heapq.heapify(pq_list)
        while pq_list or store:
            while store and store[0][1] == cnter:
                task, available_time = store.popleft()
                heapq.heappush(pq_list, task)
            # if not pq_list:
            #     while i < len(store):
            #         store[i] = list(store[i])
            #         store[i][1] -= 1
            #         store[i] = tuple(store[i])
            #         if store[i][1] == 0:
            #             mut_val = store.popleft()
            #             heapq.heappush(pq_list, mut_val[0])
            #         else:
            #             i += 1
            #     cnter += 1
            #     continue
            if pq_list:
                val = heapq.heappop(pq_list)
                val = list(val)
                val[0] += 1
                val = tuple(val)
                # while i < len(store):
                #     store[i] = list(store[i])
                #     store[i][1] -= 1
                #     store[i] = tuple(store[i])
                #     if store[i][1] == 0:
                #         mut_val = store.popleft()
                #         heapq.heappush(pq_list, mut_val[0])
                #     else:
                #         i += 1
                if val[0] != 0:
                    store.append((val, cnter + n + 1))
                
                        
            cnter += 1

        return cnter
                




        
