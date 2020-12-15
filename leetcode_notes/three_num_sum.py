# codeing=utf-8

# 方法一：
def threeSum1(self, nums):
    if len(nums) < 3:
        return []
    nums.sort()  # 排序后方便判重
    res = set()
    for i, v in enumerate(nums[:-2]):
        if i >= 1 and v == nums[i-1]:
            continue
        d = dict()
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x] = 1
            else:
                res.add((v, -v-x, x))
    return map(list, res)



# 方法二：
def threeSum2(self, nums):
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i + 1, len(nums) -1 # l:左边界，r:有边界
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0: l += 1
            elif s > 0: r -= 1
            else:
                res.append((nums[i],nums[l], nums[r]))
                while l < r and nums[l] ==nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -=1


                


