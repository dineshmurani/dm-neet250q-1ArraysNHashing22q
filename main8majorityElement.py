"""
Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [5,5,1,1,1,5,5]

Output: 5
Example 2:

Input: nums = [2,2,2]

Output: 2
Constraints:

1 <= nums.length <= 50,000
-1,000,000,000 <= nums[i] <= 1,000,000,000
Follow-up: Could you solve the problem in linear time and in O(1) space?

1. Brute Force
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > n // 2:
                return num
Time & Space Complexity
Time complexity:
O
(
n
2
)
O(n
2
 )
Space complexity:
O
(
1
)
O(1)
2. Hash Map
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res
Time & Space Complexity
Time complexity:
O
(
n
)
O(n)
Space complexity:
O
(
n
)
O(n)
3. Sorting
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
Time & Space Complexity
Time complexity:
O
(
n
log
⁡
n
)
O(nlogn)
Space complexity:
O
(
1
)
O(1) or
O
(
n
)
O(n) depending on the sorting algorithm.
4. Bit Manipulation
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        bit = [0] * 32
        for num in nums:
            for i in range(32):
                bit[i] += ((num >> i) & 1)

        res = 0
        for i in range(32):
            if bit[i] > (n // 2):
                if i == 31:
                    res -= (1 << i)
                else:
                    res |= (1 << i)
        return res
Time & Space Complexity
Time complexity:
O
(
n
∗
32
)
O(n∗32)
Space complexity:
O
(
32
)
O(32)
32
32 represents the number of bits as the given numbers are integers.
5. Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res
Time & Space Complexity
Time complexity:
O
(
n
)
O(n)
Space complexity:
O
(
1
)
O(1)
6. Randomization
class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        while True:
            candidate = random.choice(nums)
            if nums.count(candidate) > n // 2:
                return candidate
"""
import random

class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        while True:
            candidate = random.choice(nums)
            if nums.count(candidate) > n // 2:
                return candidate
