a =  raw_input("")
inp=a.split()
n=int(inp[0])
s=int(inp[1])
m=int(inp[2])
print n,s,m
ret = range(1,n+1)
for loop_i in range(n-1):
    s=(s+m)%n-1
    print ret[s]
    del ret[s]
    if s == -1:
        s=0
print ret[0]


