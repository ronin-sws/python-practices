"""
leetcode:第290题 
题目：给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
"""

class Solution1(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        tmps = s.split()
        if len(pattern) != len(tmps):
            return False
        tmpdict = dict()
        for i in range(len(pattern)):
            if pattern[i] not in tmpdict:
                if tmps[i] in tmpdict.values():
                    return False
                tmpdict[pattern[i]] = tmps[i]
            else:
                if tmpdict[pattern[i]] != tmps[i]:
                    return False
        return True

class Solution2:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if len(str.split(" ")) != len(list(pattern)):
            return False
        for l in zip(*set(zip(list(pattern), str.split(" ")))):
            if len(l) != len(set(l)):
                return False
        return True


class Solution3:
    def wordPattern(self, pattern: str, str: str) -> bool:
    res=str.split()
    return list(map(pattern.index, pattern))==list(map(res.index,res))

