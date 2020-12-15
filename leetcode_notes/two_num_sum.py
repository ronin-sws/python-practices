# coding=utf-8

"""
leetcode:第1题， 题目：两数之和
    给定nums = [2, 7, 11, 15], target =9,并返回目标值的下标
思路：
    方法一：暴力法，写两层循环
    方法二: 利用set的特性，少一层循环
"""

def twoSum(self, nums, target):
    tmpdict = dict()
    for i, x in enumerate(nums):
        if target - x in tmpdict:
            return [i, tmpdict[target - x]]
        tmpdict[x] = i
