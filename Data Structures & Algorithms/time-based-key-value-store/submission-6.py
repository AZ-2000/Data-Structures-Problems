from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap or timestamp < self.hashmap[key][0][1]:
            return ""
        l = 0
        r = len(self.hashmap[key])-1
        while l <= r:
            mid = (l+r)//2
            if timestamp > self.hashmap[key][mid][1]:
                l = mid + 1
            elif timestamp < self.hashmap[key][mid][1]:
                r = mid - 1
            else:
                return self.hashmap[key][mid][0]
            
            if l > r and l == mid + 1:
                print('here', self.hashmap,r,self.hashmap[key][r][0])
                return self.hashmap[key][r][0]
        return self.hashmap[key][r][0]


                



        


        
        
        

            







        
