#encoding:UTF-8
'''
在一个环上，有n个房屋，每个房屋中有数量不等的财报，一个盗贼希望从房屋中盗取财宝，
由于房屋中有报警器，如果同时从相邻的两个房屋中盗取财宝就会触发报警器。问在不触发报
警器的前提下，最多获取多少财宝
input[1.2.3.4]
output:4
'''
'''
数据关系 
    n1m1+n2m2+n3m3+...nnmn= Max n=0/1 
    限制方程:mi-1mimi+1 不能相连
状态转移方程：
        环的解决方法：解决一个，将环拆成顺序链 即i==n  max(rob(1,i-2)+w[i],rob(0,i-1))
        对第i个物品  Max( 若选：1 2 3 ...i-2 i的最大值,若不选：1 2 3 .....i-1 的最大值)
                    
                    
'''
'''
w = raw_input("").split()
def robL(i):
    if i<0: 
        return 0
    if i == len(w)-1:
       return max(rob(1,i-2)+int(w[i]),rob(0,i-1))
def rob(j,i):
    if i<j:
        return 0
    return max(rob(j,i-2)+int(w[i]),rob(j,i-1))
print robL(len(w)-1)
'''
'''
class Solution:
def rob(self, nums: List[int]) -> int:
    if len(nums) == 0: return 0
    if len(nums) < 4: return max(nums)
    
    opts1 = [0]*len(nums)
    opts2 = [0]*len(nums)
    
    not_first_robbed = nums[1:]
    not_last_robbed = nums[:-1]
    
    opts1[1] = not_first_robbed[0]
    opts2[1] = not_last_robbed[0]
    
    for i in range(2, len(nums)):
        opts1[i] = max(opts1[i-1], opts1[i-2] + not_first_robbed[i-1])
        opts2[i] = max(opts2[i-1], opts2[i-2] + not_last_robbed[i-1])
    return max(opts1[-1], opts2[-1])
'''