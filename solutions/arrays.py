from typing import List

class ArraySolutions():

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], index]
            d[num] = index
    
    @staticmethod
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        last_num = 101
        for fast in range(len(nums)):
            if nums[fast] != last_num:
                last_num = nums[fast]
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return slow
    
    @staticmethod
    def searchInsert(self, nums: List[int], target: int) -> int:
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