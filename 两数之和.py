class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for index, value in enumerate(nums):
            if target - value not in num:
                num[value] = index
            else:
                return [index, num[target - value]]
        return []