class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x = abs(x)
        reversed_num = int(str(x)[::-1])
        if negative:
            reversed_num = -reversed_num

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0

        return reversed_num


if __name__ == "__main__":
    solution = Solution()
    
    x = 123
    result = solution.reverse(x)
    print("Reversed number:", result)


    x = -123
    result = solution.reverse(x)
    print("Reversed number:", result)


    x = 120
    result = solution.reverse(x)
    print("Reversed number:", result)
