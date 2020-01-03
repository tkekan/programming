def canPartitionKSubsets(nums, k):
    s=sum(nums)
    if s%k!=0:
        return False
    target=s//k
    buckets=[0]*k
    nums.sort(reverse=True)
    def dfs(idx):
        if idx==len(nums):
            return True
        failed=set()
        for i in range(k):
            if buckets[i] in failed or buckets[i]+nums[idx]>target:
                continue
            buckets[i]+=nums[idx]
            if dfs(idx+1):
                return True
            buckets[i]-=nums[idx]
            failed.add(buckets[i])
        return False
    return dfs(0)

nums = [3,1,4,4,3,2,3,5,2,1]
k = 4
print canPartitionKSubsets(nums,k)
