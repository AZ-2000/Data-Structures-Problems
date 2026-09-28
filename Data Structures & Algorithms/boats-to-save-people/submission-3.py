class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        r = len(people) - 1
        while r > 0  and people[0] + people[r] > limit:
            r -= 1
        print(len(people[0:r+1])//2)
        print((len(people[0:r+1])//2) % 2)
        if len(people[0:r+1]) % 2 and len(people[0:r+1]) > 2:        
            couples = len(people[0:r+1])//2 + 1  
        else:
            couples = len(people[0:r+1])//2 
            print(couples)
        if r:
            singles = len(people) - (r+1)
        else:
            singles = len(people)
        
        return singles + couples


        