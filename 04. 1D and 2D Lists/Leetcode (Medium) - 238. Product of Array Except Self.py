"""
Leetcode Problem #: 238
Leetcode Problem: Product of Array Except Self
Difficulty: Medium

At a particular index in the array, the product at that
array is the product of all items to the left of the 
current index with the product of all of the items to 
the right of that index. If there's nothing to the left
or right, then we can return 1.
"""

class Solution:
    def productExceptSelf(self, nums):
        product = 1
        zeroFrequency = 0
        n = len(nums)

        for num in nums:
            if num == 0:
                zeroFrequency += 1
                if zeroFrequency > 1:
                    return [0] * n
            product *= num

        res = []
        if zeroFrequency == 1:
            for i in range (n):
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(product)
        else:
            for i in range (n):
                res.append(product//nums[i])
            
        return res
            

# We can shorten our solution by using prefix and postfix

class Solution:
    def productExceptSelf(self, nums):
        pre = 1
        post = 1
        n = len(nums)

        res = [1] * n
        for i in range(n):
            res[i] = pre
            pre *= nums[i]

        for j in range(reversed(n)):
            res[j] *= post
            post *= nums[j]

        return res