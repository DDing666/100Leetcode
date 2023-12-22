#https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked
'''
这里的是将value作为index来减少复杂度
即创建num的这样的一个哈希表
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for index, value in enumerate(nums):
            if target - value not in num:
                num[value] = index
            else:
                return [index, num[target - value]]
        return []   
'''
题解
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
'''