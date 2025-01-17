from typing import Dict

class Solution:
    def romanToInt(self, s: str) -> int:
        romanStrToIntDict: Dict[str, int] = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        total = 0
        for index, char in enumerate(s):
            if index + 1 < len(s):
                if romanStrToIntDict[char] < romanStrToIntDict[s[index + 1]]:
                    total -= romanStrToIntDict[char]
                else:
                    total += romanStrToIntDict[char]
        total += romanStrToIntDict[char]
        return total

case1 = Solution().romanToInt('III')

case2 = Solution().romanToInt('LVIII')

case3 = Solution().romanToInt('MCMXCIV')

if case1 == 3 and case2 == 58 and case3 == 1994:
    print('All test cases pass')