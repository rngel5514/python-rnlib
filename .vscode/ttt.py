a =  raw_input("")
lst =  raw_input("")
lst = lst.split()
inp=a.split()
n=int(inp[0])
s=int(inp[1])
m=int(inp[2])
print n,s,m
ret = range(1,n)
rlst = lst.sort(reverse=True)
q=0
def xvl(n,x,m):
    for i in range(n):
        j = i+1
        eh
        if(abs(ret.index(rlst[j])-ret.index(rlst[i]))>1):
            if(j-i>1):
                s += rlst[j-1]
                if(rlst[i]+rlst[j]>=s):
                    i = j
                    q +=1
                    c = 1
                
        if()
        ret.index(rlst)
        ret.index(rlst[i])
        
def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0], nums[1])
    N = len(nums)
    return max(self.rob_range(nums[0 : N - 1]), self.rob_range(nums[1 : N]))

def rob_range(self, nums):
    if not nums: return 0
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0], nums[1])
    N = len(nums)
    dp = [0] * N
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, N):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]
 
