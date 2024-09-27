from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_prefix = ''
        for i in range(len(strs[0])):
            try:
                if strs[0][i] == strs[1][i] and strs[0][i] == strs[2][i] and strs[1][i] == strs[2][i]:
                    new_prefix += strs[0][i]
                else:
                    break
            except:
                break
        return new_prefix

case1 = Solution().longestCommonPrefix(["flower","flow","flight"])

case2 = Solution().longestCommonPrefix(["dog","racecar","car"])

if case1 == 'fl' and case2 == '':
    print('All test cases pass')