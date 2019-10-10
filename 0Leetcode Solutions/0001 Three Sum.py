class Solution:
    def threeSum(self,nums,t):
        seen={}
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                while nums[j] in seen.keys():
                    print(seen)
                    return seen.get(nums[j])+[j]
                else:
                    seen[t-nums[i]-nums[j]]=[i,j]
        return[]
print(Solution().threeSum([2,3,4,5,6,7], 12))