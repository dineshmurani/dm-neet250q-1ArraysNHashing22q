"""
Sort Colors
You are given an array nums consisting of n elements where each element is an integer representing a color:

0 represents red
1 represents white
2 represents blue
Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

You must not use any built-in sorting functions to solve this problem.

Example 1:

Input: nums = [1,0,1,2]

Output: [0,1,1,2]
Example 2:

Input: nums = [2,1,0]

Output: [0,1,2]
Constraints:

1 <= nums.length <= 300.
0 <= nums[i] <= 2.
Follow up: Could you come up with a one-pass algorithm using only constant extra space?

1. Brute Force

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
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
2. Counting Sort

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1

        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1
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
3. Three Pointers - I

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
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
4. Three Pointers - II

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = two = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[two] = 2
                nums[one] = 1
                nums[zero] = 0
                two += 1
                one += 1
                zero += 1
            elif nums[i] == 1:
                nums[two] = 2
                nums[one] = 1
                two += 1
                one += 1
            else:
                nums[two] = 2
                two += 1
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
5. Three Pointers - III

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = 0
        for two in range(len(nums)):
            tmp = nums[two]
            nums[two] = 2
            if tmp < 2:
                nums[one] = 1
                one += 1
            if tmp < 1:
                nums[zero] = 0
                zero += 1

"""

