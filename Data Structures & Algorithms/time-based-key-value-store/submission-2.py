class TimeMap:

    def __init__(self):
        self.hashmap ={}
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        else:
            l, r = 0, len(self.hashmap[key]) - 1

            while l <= r:
                mid = (l+r)//2
                if self.hashmap[key][mid][0] < timestamp:
                    l = mid + 1
                elif self.hashmap[key][mid][0] > timestamp:
                    r = mid - 1
                else:
                    return self.hashmap[key][mid][1]
            
            if r < 0:
                return ""
            else:
                return self.hashmap[key][r][1] 


            







        
