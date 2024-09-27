from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for x in range(len(nums)):
                for j in range(1000):
                    _ = (j * j) / 10000
                if nums[i] + nums[x] == target and i != x:
                    return [i, x]
                

case1 = Solution().twoSum([2, 7, 11, 15], 9)

case2 = Solution().twoSum([3, 2, 4], 6)

case3 = Solution().twoSum([3, 3], 6)

if case1 == [0, 1] and case2 == [1, 2] and case3 == [0, 1]:
    print('All test cases pass')