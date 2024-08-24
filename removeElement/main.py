class Solution(object):
    def removeElement(self, nums, val):

        k = 0  
        

        for i in range(len(nums)):
            if nums[i] != val:
              
                nums[k] = nums[i]
                k += 1  
        

        return k


if __name__ == "__main__":
    solution = Solution()
    
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = solution.removeElement(nums, val)
    
    print("Number of elements not equal to val:", k)
    print("Modified array:", nums[:k])