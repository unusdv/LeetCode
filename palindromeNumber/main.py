class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False
        
        s = str(x)
        
        return s == s[::-1]

if __name__ == "__main__":
    solution = Solution()
    
    print("Is 121 a palindrome?", solution.isPalindrome(121))
    print("Is -121 a palindrome?", solution.isPalindrome(-121))
    print("Is 10 a palindrome?", solution.isPalindrome(10))  
