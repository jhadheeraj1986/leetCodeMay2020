'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

#Solution 1
    def majorityElement1(self, nums: List[int]) -> int:
        maxCount = 0; 
        index = -1
        for i in range(len(nums)): 
            count = 0
            for j in range(len(nums)): 
                if(nums[i] == nums[j]): 
                    count += 1
            if(count > maxCount): 
                maxCount = count 
                index = i 
        if (maxCount > len(nums)/2): 
            return (nums[index])
            
#Solution 2
    def majorityElement2(self, nums: List[int]) -> int:        
        length = len(nums)
        count = -1
        for i in nums:
            count = nums.count(i)
            if count > (length/2) :
                return i
 
#Solution 3
    def majorityElement3(self, nums: List[int]) -> int:
        #half = 
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] == nums[i+ int(len(nums)/2)]:
                return nums[i]

