#encoding:UTF-8
'''
在一条直线上，有n个房屋，每个房屋中有数量不等的财报，一个盗贼希望从房屋中盗取财宝，
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
        对第i个物品  Max( 若选：1 2 3 ...i-2 i的最大值,若不选：1 2 3 .....i-1 的最大值)
                    
                    
'''
w = raw_input("").split()
def rob(i):
    if i<0:
        return 0
    return max(rob(i-2)+int(w[i]),rob(i-1))
print rob(len(w)-1)