class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        j = len(s)-1
        print(j)
        if not s:
            return True
        while i < j:
            if s[i] != s[j]:
                print(s[i],s[j])
                return False
            i += 1
            j -= 1
        return True