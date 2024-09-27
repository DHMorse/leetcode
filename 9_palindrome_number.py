from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_x = list(str(x))
        for i in range(len(list_x)):
            list_x.insert(i, list_x.pop())
        return list_x == list(str(x))
    
case1 = Solution().isPalindrome(121)

case2 = Solution().isPalindrome(-121)

case3 = Solution().isPalindrome(10)

if case1 == True and case2 == False and case3 == False:
    print('All test cases pass')