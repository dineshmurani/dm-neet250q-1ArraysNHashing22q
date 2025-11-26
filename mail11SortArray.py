"""
Sort an Array
You are given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [10,9,1,1,1,2,3,1]

Output: [1,1,1,1,2,3,9,10]
Example 2:

Input: nums = [5,10,2,1,3]

Output: [1,2,3,5,10]
Constraints:

1 <= nums.length <= 50,000.
-50,000 <= nums[i] <= 50,000

1. Quick Sort
class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        mid = (left + right) >> 1
        nums[mid], nums[left + 1] = nums[left + 1], nums[mid]

        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left + 1] > nums[right]:
            nums[left + 1], nums[right] = nums[right], nums[left + 1]
        if nums[left] > nums[left + 1]:
            nums[left], nums[left + 1] = nums[left + 1], nums[left]

        pivot = nums[left + 1]
        i = left + 1
        j = right

        while True:
            while True:
                i += 1
                if not nums[i] < pivot:
                    break
            while True:
                j -= 1
                if not nums[j] > pivot:
                    break
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[left + 1], nums[j] = nums[j], nums[left + 1]
        return j

    def quickSort(self, nums: List[int], left: int, right: int) -> None:
        if right <= left + 1:
            if right == left + 1 and nums[right] < nums[left]:
                nums[left], nums[right] = nums[right], nums[left]
            return

        j = self.partition(nums, left, right)
        self.quickSort(nums, left, j - 1)
        self.quickSort(nums, j + 1, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
Time & Space Complexity
Time complexity:
O
(
n
log
⁡
n
)
O(nlogn) in average case,
O
(
n
2
)
O(n
2
 ) in worst case.
Space complexity:
O
(
log
⁡
n
)
O(logn) for recursive stack.
2. Merge Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums
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
n
)
O(n)
3. Heap Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapSort(nums)
        return nums

    def heapify(self, arr, n, i):
        l = (i << 1) + 1
        r = (i << 1) + 2
        largestNode = i

        if l < n and arr[l] > arr[largestNode]:
            largestNode = l

        if r < n and arr[r] > arr[largestNode]:
            largestNode = r

        if largestNode != i:
            arr[i], arr[largestNode] = arr[largestNode], arr[i]
            self.heapify(arr, n, largestNode)

    def heapSort(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
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
log
⁡
n
)
O(logn) for recursive stack.
4. Counting Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            count = defaultdict(int)
            minVal, maxVal = min(nums), max(nums)
            for val in nums:
                count[val] += 1

            index = 0
            for val in range(minVal, maxVal + 1):
                while count[val] > 0:
                    nums[index] = val
                    index += 1
                    count[val] -= 1

        counting_sort()
        return nums
Time & Space Complexity
Time complexity:
O
(
n
+
k
)
O(n+k)
Space complexity:
O
(
n
)
O(n)
Where
n
n is the size of the array
n
u
m
s
nums and
k
k is the range between the minimum and maximum values in the array.
5. Radix Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def countSort(arr, n, d):
            count = [0] * 10
            for num in arr:
                count[(num // d) % 10] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]

            res = [0] * n
            for i in range(n - 1, -1, -1):
                idx = (arr[i] // d) % 10
                res[count[idx] - 1] = arr[i]
                count[idx] -= 1

            for i in range(n):
                arr[i] = res[i]

        def radixSort(arr):
            n = len(arr)
            max_element = max(arr)
            d = 1
            while max_element // d > 0:
                countSort(arr, n, d)
                d *= 10

        negatives = [-num for num in nums if num < 0]
        positives = [num for num in nums if num >= 0]

        if negatives:
            radixSort(negatives)
            negatives = [-num for num in reversed(negatives)]

        if positives:
            radixSort(positives)

        return negatives + positives
Time & Space Complexity
Time complexity:
O
(
d
∗
n
)
O(d∗n)
Space complexity:
O
(
n
)
O(n)
Where
n
n is the size of the array
n
u
m
s
nums and
d
d is the number of digits in the maximum element of the array.
6. Shell Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def shell_sort(nums, n):
            gap = n // 2
            while gap >= 1:
                for i in range(gap, n):
                    tmp = nums[i]
                    j = i - gap
                    while j >= 0 and nums[j] > tmp:
                        nums[j + gap] = nums[j]
                        j -= gap
                    nums[j + gap] = tmp
                gap //= 2

        n = len(nums)
        if n == 1:
            return nums
        shell_sort(nums, n)
        return nums
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums
