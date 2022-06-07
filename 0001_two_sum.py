class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #用len()方法取得nums列表的长度
        n = len(nums)
        #x取值从0一直到n（不包括n）
        for x in range(n):
            #y取值从x+1一直到n（不包括n）
            #用x+1是减少不必要的循环,y的取值肯定是比x大
            for y in range(x+1,n):
                #假如 target-nums[x]的某个值存在于nums中
                if nums[y] == target - nums[x]:
                    #返回x和y
                    return x,y



class Solution2:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            delt = target - nums[i]
            if delt in nums:
                y = nums.index(delt)
                if y != i:
                    return [i, y]


#求差值、把差值存进字典里作为键、索引作为值，第一次循环理解：d[7]=0 即字典d={7:0}，表示为索引0需要数组里值为7的元素配对。
# if 判断是否为前面元素所需要配对的值 ， 是则返回两个索引值。（补充：nums[x] in d  是判断值是否在字典某个key里面）
class Solution3:
    def twoSum(self, nums, target):
        d = {}
        n = len(nums)
        for i in range(n):
            rest = target - nums[i]
            if nums[i] in d:
                return d[nums[i]], i
            else:
                d[rest] = i



S = Solution3()
result = S.twoSum([1,2,3,4], 3)
print(result)




