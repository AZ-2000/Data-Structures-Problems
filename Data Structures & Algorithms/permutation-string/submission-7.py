class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            count1 = {}
            for c in s1:
                count1[c] = count1.get(c,0) + 1

            window = {}

            left = 0   

            for right in range(len(s2)):
                c = s2[right]
                window[c] = window.get(c, 0) + 1
                if right - left + 1 > len(s1):
                    left_char = s2[left]
                    window[left_char] -= 1
                    if window[left_char] == 0:
                        del window[left_char]
                    left += 1
                
                if window == count1:
                    return True
                
            return False