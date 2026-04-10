class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        s2 = ''
        print(s)
        for c in s:
            if c.isalnum():
                s2 += c.lower()
        right = len(s2) - 1
        while left <= right:
            print(s2[left],s2[right])
            if left == right and s2[left] == s2[right]:
                return True
            if s2[left] != s2[right]:
                return False
            else:
                left += 1
                right -= 1
        return True