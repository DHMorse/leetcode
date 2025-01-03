from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            try:
                if roman_dict[s[i]] < roman_dict[s[i + 1]]:
                    total -= roman_dict[s[i]]
                else:
                    total += roman_dict[s[i]]
            except:
                total += roman_dict[s[i]]
        return total

case1 = Solution().romanToInt('III')

case2 = Solution().romanToInt('LVIII')

case3 = Solution().romanToInt('MCMXCIV')

if case1 == 3 and case2 == 58 and case3 == 1994:
    print('All test cases pass')