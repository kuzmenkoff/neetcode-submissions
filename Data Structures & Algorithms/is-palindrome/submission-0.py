class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        for i in range (0, len(cleaned)//2):
            if (cleaned[i] != cleaned[len(cleaned) - i - 1]):
                return False
        return True 
        