class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        solution = set()
        for a, b in enumerate(nums):
            solution.add(b)
        
        
        if len(nums) == len(solution):
            return False
        else:
            return True