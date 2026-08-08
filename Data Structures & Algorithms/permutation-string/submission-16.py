class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        else:
            freq1 = {}
            freq2 = {}

            for i in range(len(s1)):
                freq1[s1[i]] = freq1.get(s1[i], 0) + 1
                freq2[s2[i]] = freq2.get(s2[i],0) + 1
            
            if freq1 == freq2:
                return True
                
            l, r =0,len(s1)

            while r < len(s2):
                if freq1 == freq2:
                    return True
                else:
                    freq2[s2[l]] -= 1
                    if freq2[s2[l]] == 0:
                        del freq2[s2[l]]
                    l += 1
                    freq2[s2[r]] = freq2.get(s2[r],0) + 1
                    r += 1
            return freq1==freq2
                

        
        

