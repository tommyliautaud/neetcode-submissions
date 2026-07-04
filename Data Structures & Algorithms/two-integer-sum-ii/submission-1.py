class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        res = [0] * 2


        while (l < r):
            if (numbers[l] + numbers[r] < target):
                l += 1
            elif (numbers[l] + numbers[r] > target):
                r -= 1
            else:
                res[0] = l + 1
                res[1] = r + 1
                return res

