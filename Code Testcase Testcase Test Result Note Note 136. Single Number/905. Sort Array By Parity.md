# 905. Sort Array By Parity

## Problem Statement
Given an integer array `nums`, move all the even integers to the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

### Example 1:
```python
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

### Example 2:
```python
Input: nums = [0]
Output: [0]
```

## Constraints:
- `1 <= nums.length <= 5000`
- `0 <= nums[i] <= 5000`

---

## Solution Approach
### Method 1: Using Two Lists
1. Separate even and odd numbers into two lists.
2. Concatenate even numbers followed by odd numbers.
3. Return the resulting list.

```python
def sortArrayByParity(nums):
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]
    return evens + odds
```

### Method 2: In-Place Two-Pointer Approach
1. Use two pointers to swap even numbers to the front and odd numbers to the back.
2. Iterate through the list and adjust elements in place.

```python
def sortArrayByParity(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 > nums[right] % 2:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] % 2 == 0:
            left += 1
        if nums[right] % 2 == 1:
            right -= 1
    return nums
```

## Complexity Analysis
- **Method 1 (Two Lists)**: O(n) time and O(n) space
- **Method 2 (Two-Pointer In-Place)**: O(n) time and O(1) space

---

## How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/sort-array-by-parity.git
   cd sort-array-by-parity
   ```
2. Run the script:
   ```sh
   python sort_array_by_parity.py
   ```

## License
This project is open-source and available under the [MIT License](LICENSE).
