import sys
n1 =  raw_input("")
n = int(n1)
i = 0
q = 0
lines = []
res =""
loop =1
temp = True
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        line = line.split(',')
        tem = [int(e) for e in line]
        lines.append(tem)
        q +=len(tem)
        i = i+1
    for u in range(q/(i*n)+1):
        for x in range(i):
            aline=lines[x]
            for j in range(n):
                if(len(aline)==0):
                    continue
                res +=str(aline[0])+","
                del(aline[0])
    res=res[:-1]
    print res
except:
    pass