"""
Products of Array Except Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20


Recommended Time & Space Complexity

Hint 1
A brute-force solution would be to iterate through the array with index i and compute the product of the array except for that index element. This would be an O(n^2) solution. Can you think of a better way?


Hint 2
Is there a way to avoid the repeated work? Maybe we can store the results of the repeated work in an array.


Hint 3
We can use the prefix and suffix technique. First, we iterate from left to right and store the prefix products for each index in a prefix array, excluding the current index's number. Then, we iterate from right to left and store the suffix products for each index in a suffix array, also excluding the current index's number. Can you figure out the solution from here?


Hint 4
We can use the stored prefix and suffix products to compute the result array by iterating through the array and simply multiplying the prefix and suffix products at each index.

SOLUTION
1. Brute Force
Intuition
For each position in the array, we can compute the product of all other elements by multiplying every value except the one at the current index.
This directly follows the problem statement and is the most straightforward approach:
for each index, multiply all elements except itself.
Although simple, this method is inefficient because it repeats a full pass through the array for every element.

Algorithm
Let n be the length of the input array and create a result array res of size n.
For each index i from 0 to n - 1:
Initialize a running product prod = 1.
Loop through all indices j from 0 to n - 1:
If j is not equal to i, multiply prod by nums[j].
Store prod in res[i].
After all indices are processed, return res.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]

            res[i] = prod
        return res
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
O(1) extra space.
O
(
n
)
O(n) space for the output array.
2. Division
Intuition
This approach works by using a simple idea:
If we know the product of all non-zero numbers, we can easily compute the answer for each position using division — as long as there are no division-by-zero issues.

So we first check how many zeros the array has:

If there are two or more zeros, then every product will include at least one zero → the entire result is all zeros.
If there is exactly one zero, then only the position containing that zero will get the product of all non-zero numbers. All other positions become zero.
If there are no zeros, we can safely do:
result[i] = total_product // nums[i]
Algorithm
Traverse the array once:
Multiply all non-zero numbers to get the total product.
Count how many zeros appear.
If the zero count is greater than 1:
Return an array of all zeros.
Create a result array of size n.
Loop through the numbers again:
If there is one zero:
The index with zero gets the product of all non-zero numbers.
All other positions get 0.
If there are no zeros:
Set each result value to total_product // nums[i].
Return the result array.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
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
O(1) extra space.
O
(
n
)
O(n) space for the output array.
3. Prefix & Suffix
Intuition
For each index, we need the product of all elements before it and all elements after it.
Instead of recomputing the product repeatedly, we can pre-compute two helpful arrays:

Prefix product: pref[i] = product of all elements to the left of i
Suffix product: suff[i] = product of all elements to the right of i
Then, the final answer for each index is simply:

result[i] = prefix[i] × suffix[i]

This works because:

The prefix handles everything before the index
The suffix handles everything after the index
Both pieces together form the product of all numbers except the one at that position.

Algorithm
Let n be the length of the array.
Create three arrays of size n:
pref for prefix products
suff for suffix products
res for the final result
Set:
pref[0] = 1 (nothing to the left of index 0)
suff[n - 1] = 1 (nothing to the right of last index)
Build the prefix product array:
For each i from 1 to n - 1:
pref[i] = nums[i - 1] × pref[i - 1]
Build the suffix product array:
For each i from n - 2 down to 0:
suff[i] = nums[i + 1] × suff[i + 1]
Build the result:
For each index i, compute:
res[i] = pref[i] × suff[i]
Return the result array.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
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
4. Prefix & Suffix (Optimal)
Intuition
We can compute the product of all elements except the current one without using extra prefix and suffix arrays.
Instead, we reuse the result array and build the answer in two simple passes:

In the first pass, we fill res[i] with the product of all elements to the left of i (prefix product).
In the second pass, we multiply each res[i] with the product of all elements to the right of i (postfix product).
By maintaining two running values — prefix and postfix — we avoid the need for separate prefix and suffix arrays.
This gives us the same logic as the previous method, but with O(1) extra space.

Algorithm
Initialize the result array res with all values set to 1.
Create a variable prefix = 1.
First pass (left to right):
For each index i:
Set res[i] = prefix (product of all elements to the left).
Update prefix *= nums[i].
Create a variable postfix = 1.
Second pass (right to left):
For each index i:
Multiply res[i] by postfix (product of all elements to the right).
Update postfix *= nums[i].
Return the result array res.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

"""
Line-by-line explanation (with a worked example)

This is a clean O(n) solution to the Product of Array Except Self problem (return an array where each position i is the product of all elements of the input except nums[i]) without using division.

I'll explain each line and then walk through a concrete example (nums = [1,2,3,4]).

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))


res is a list initialized to length len(nums) where every entry is 1.

We will fill res[i] with the product of all numbers except nums[i] by first storing the prefix products then multiplying by postfix products.

Starting with 1 is necessary because 1 is the multiplicative identity (so multiplying accumulators into res does nothing until we overwrite).

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]


prefix holds the product of all elements to the left of the current index i.

Loop goes left → right:

res[i] = prefix puts the product of all elements before i into res[i].

prefix *= nums[i] then updates prefix to include nums[i] so that on the next iteration it represents the product of all elements left of i+1.

After this loop finishes, res[i] = product of elements before i for every i.

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]


postfix holds the product of all elements to the right of the current index i.

Loop goes right → left (from last index down to 0):

res[i] *= postfix multiplies the previously stored left-product by the right-product, producing product of everything except nums[i].

postfix *= nums[i] updates postfix to include nums[i] for the next iteration (one step left).

By the end of this loop, res[i] is the desired result for every i.

        return res


Return the res list containing products except self.

Worked example: nums = [1,2,3,4]

Initial:

res = [1,1,1,1]

prefix = 1

First loop (build prefixes):

i = 0: res[0] = prefix = 1; then prefix *= nums[0] = 1 → prefix = 1. res = [1,1,1,1]

i = 1: res[1] = prefix = 1; then prefix *= nums[1] = 2 → prefix = 2. res = [1,1,1,1]

i = 2: res[2] = prefix = 2; then prefix *= nums[2] = 3 → prefix = 6. res = [1,1,2,1]

i = 3: res[3] = prefix = 6; then prefix *= nums[3] = 4 → prefix = 24. res = [1,1,2,6]

Now res holds left-products:

res = [1, 1, 2, 6] (products of elements left of index 0..3 respectively)

Second loop (multiply by postfixes):

postfix = 1

i = 3: res[3] *= postfix = 6 * 1 = 6; then postfix *= nums[3] = 4 → postfix = 4. res = [1,1,2,6]

i = 2: res[2] *= postfix = 2 * 4 = 8; then postfix *= nums[2] = 3 → postfix = 12. res = [1,1,8,6]

i = 1: res[1] *= postfix = 1 * 12 = 12; then postfix *= nums[1] = 2 → postfix = 24. res = [1,12,8,6]

i = 0: res[0] *= postfix = 1 * 24 = 24; then postfix *= nums[0] = 1 → postfix = 24. res = [24,12,8,6]

Final answer: [24,12,8,6] — each entry is product of all other elements.

Why this is efficient

Time complexity: O(n) — two single-pass loops over the input.

Space complexity: O(1) extra space (ignoring output). res is the required output; only prefix and postfix are extra scalars. This meets the problem constraint of no extra arrays for prefix/postfix.

Edge cases & behavior

Empty list [] → returns [].

Single element [x] → returns [1] (product of "all other elements" — empty product — is 1).

Contains zeros:

If exactly one zero in nums, the result will have zeros everywhere except at the index of that zero, which will be the product of all non-zero elements (this algorithm handles that correctly).

If two or more zeros, all results will be zero (also handled correctly).

Works with negative numbers, large numbers (beware of overflow in languages without big integers — Python handles big integers).

Alternative / note

A more explicit (but memory heavier) version builds two arrays left[i] and right[i] then multiplies them. This version does the same idea in-place (in res) and uses O(1) extra memory.

If you want, I can:

show the two-array variant for comparison, or

provide a version with comments inline, or

explain how the algorithm behaves step-by-step for a case with zeros.
"""
