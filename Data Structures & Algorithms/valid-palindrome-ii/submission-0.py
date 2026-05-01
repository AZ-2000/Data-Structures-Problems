class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1        
        flag = True
        while left < right:
            if s[left] != s[right]:
                inp_1 = s[left]
                inp_2 = s[right]
                flag = False
                break
            else:
                left += 1
                right -= 1
        if flag:
            return True
        
        s_1 = s[:left] + s[left+1:]
        s_2 = s[:right] + s[right+1:]
        left = 0
        right = len(s_1)-1

        flag = True

        while left < right:
            if s_1[left] != s_1[right]:
                flag = False
                break
            left += 1
            right -= 1
        if flag:
            return True
        else:
            left = 0
            right = len(s_2)-1
            while left < right:
                if s_2[left] != s_2[right]:
                    return False
                left +=1 
                right -= 1


        return True