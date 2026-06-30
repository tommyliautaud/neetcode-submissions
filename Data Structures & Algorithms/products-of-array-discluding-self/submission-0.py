class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        
        postfix[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        res = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                res[i] = postfix[i + 1]
            elif i == len(res) - 1:
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * postfix[i + 1]
        return res


        
        
