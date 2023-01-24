from typing import List


class Solution:
    #排序 + 双指针
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        #枚举a
        for first in range(n):
            #a不重复
            if first > 0 and nums[first] == nums[first-1]:
                continue

            third = n - 1
            target = -nums[first]

            #枚举b
            for second in range(first+1, n):
                # b不重复
                if second > first+1 and nums[second] == nums[second-1]:
                    continue

                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans



S = Solution()
result = S.threeSum([-1,0,1,2,-1,-4])
print(result)


