def recurse(i,v):
    if(i<0 or v <= 0):
        return 0
    if(v<w[i]):
        return recurse(i-1,v)
    return max(recurse(i-1,v-w[i])+c[i],recurse(i-1,v))
q = int(raw_input(""))
w = raw_input("").split()
c = raw_input("").split()
print recurse(len(w)-1,18