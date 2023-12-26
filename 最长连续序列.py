#https://leetcode.cn/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-100-liked

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mmax = 1
        temp = 1
        if nums == []:
            return 0
        nums_sort = sorted(list(set(nums)))
        for index, value in enumerate(nums_sort):
            if index < len(nums_sort) - 1 and nums_sort[index + 1] - value == 1:
                mmax += 1
                temp = max(temp, mmax)#这里纠结了temp的值，按理说要temp之间的比较
            else: mmax = 1
        
        return max(temp, mmax)