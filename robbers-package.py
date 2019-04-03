#encoding:UTF-8
'''
在一个圆环上，有n个房屋，每个房屋中有数量不等的财报，一个盗贼希望从房屋中盗取财宝，
由于房屋中有报警器，如果同时从相邻的两个房屋中盗取财宝就会触发报警器。问在不触发报
警器的前提下且只能偷取m个房间，最多能获取多少财宝
input m
input[1.2.3.4]
output:4
'''
'''
数据关系 
    n1m1+n2m2+n3m3+...nnmn= Max n=0/1 
    限制方程:mi-1mimi+1 不能相连
            且为m个
状态转移方程：
        对第i个物品  Max( 若选：1 2 3 ...i-2 i的最大值,若不选：1 2 3 .....i-1 的最大值)
                    
                    
'''
m = raw_input("").split()
w = raw_input("").split()
def robL(i,m):
    if i<0: 
        return 0
    if i == len(w)-1:
       return max(rob(1,i-2,m-1)+int(w[i]),rob(0,i-1,m))
def rob(j,i,m):
    if i<j or m<0:
        return 0
    return max(rob(j,i-2,m-1)+int(w[i]),rob(j,i-1,m))
print robL(len(w)-1,int(m[0]))