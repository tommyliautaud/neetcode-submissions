class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1

        while front < back:
            if not (s[front].isalpha() or
            s[front].isnumeric()):
                front += 1
                continue
            if not (s[back].isalpha() or
            s[back].isnumeric()):
                back -= 1
                continue

            if ((s[front].isalpha() and
               not s[back].isalpha()) or
               (not s[front].isalpha() and
               s[back].isalpha())):
               return False       
            
            if ((s[front] == s[back]) or
               (ord(s[front]) - ord(s[back]) == 32) or
               (ord(s[back]) - ord(s[front]) == 32)):
               front += 1
               back -= 1

            else:
                return False
        return True
        