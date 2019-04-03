#encoding:UTF-8
"""
下面是一个可以试用贪心算法解的题目，贪心解不是最优解。
    [背包问题]有一个背包，背包容量是M=150。有7个物品，物品可以分割成任意大小。
    要求尽可能让装入背包中的物品总价值最大，但不能超过总容量。
    物品 A B C D E F G
    重量 35 30 60 50 40 10 25
    价值 10 40 30 50 35 40 30
"""
"""
贪心算法无法解决 存在因为大物品导致稍微小一点的物品和再稍微小的物品无法装下 只能装最差的物品 并且最差的物品和最大的物品和小于稍微小一些的物品和
"""
"""
动态规划
状态转移方程 最基础的问题 选还是不选
                        相当于用f[i][v]表示前i个背包装入容量为v的背包中所可以获得的最大值
                        对于一个物品有两钟情况
                            情况1：第i件物品不放进去 这时所得价值为f[i-1][v]
                            情况2：第i件物品放进去 这时所得价值为f[i-1][v-w[i]]+c[i]
"""
# c is cost  w is weiht 
v = int(raw_input(""))
c = raw_input("").split()
w = raw_input("").split()
def recurse(i,v):
    if(i < 0 or v <= 0):
        return 0
    if(v < int(w[i])):
        return recurse(i-1,v)
    return max(recurse(i-1,v-int(w[i]))+int(c[i]),recurse(i-1,v))
print recurse(len(w)-1,v)
"""
pr = list()
for i,j in zip(r_input_co,r_input_we):  #zip把列表对应的组合起来 按长度小的组合 unzip(*zz)可以把组合的重新拆分
    if(j!=0):
        pr.append(i/(j*1.0))
    else:
        pr.append(0)
while(max(pr)<=remain and remain 
    pr.
print "hello"
"""