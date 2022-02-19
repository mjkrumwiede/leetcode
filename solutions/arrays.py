from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [d[diff], index]
        d[num] = index

def removeDuplicates(nums: List[int]) -> int:
    slow = 0
    last_num = 101
    for fast in range(len(nums)):
        if nums[fast] != last_num:
            last_num = nums[fast]
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return slow

def searchInsert(nums: List[int], target: int) -> int:
    length = len(nums)
    if length == 1:
        return 1 if target > nums[0] else 0
    middle_index = length//2
    if nums[middle_index] == target:
        return middle_index
    elif nums[middle_index] > target:
        return self.searchInsert(nums[:middle_index], target)
    else:
        return middle_index + self.searchInsert(nums[middle_index:], target)

def plusOne(digits: List[int]) -> List[int]:
    ind = len(digits) - 1
    digits[ind] += 1
    while(digits[ind] > 9):
        if ind == 0:
            digits[ind] = 0
            digits.insert(0,1)
            break
        else:
            digits[ind] = 0
            ind -= 1
            digits[ind] += 1
    return digits

def maxProfit(prices: List[int]) -> int:
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

def singleNumber(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[0]^=nums[i]
    return nums[0]

def majorityElement(nums: List[int]) -> int:
    table = {}
    for num in nums:
        if num in table:
            table[num] = table[num] + 1
        else:
            table[num] = 1
    return max(table, key=table.get)

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    index = 0
    while(index<length):
        if nums[index] == 0:
            del nums[index]
            nums.append(0)
            length -= 1
        else:
            index += 1

def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)
    n_set = set()
    for num in nums:
        n_set.add(num)
    missing = []
    for num in range(1,n+1):
        if num not in n_set:
            missing.append(num)
    return missing