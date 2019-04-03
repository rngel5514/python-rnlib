from optparse import OptionParser 
def mmmalogM(x1,x2,x3,y1,y2,y3):

    if(y2==0 and x1==0):
        current1 = 0
    else:
        current1 = x1*(x1*y2)/(x1+y2) 
    if(y3==0 and x1==0):
        current2 = 0
    else:
        current2 = x1*(x1*y3)/(x1+y3) 
    if(y1==0 and x2==0):
        current3 = 0
    else:
        current3 = y1*(x2*y1)/(x2+y1) 
    if(y1==0 and x3==0):
        current4 = 0
    else:
        current4 = y1*(x3*y1)/(x3+y1)
    m1=round(x1*y1+ current1+current2+current3+current4,2)
        
    if(y1==0 and x2==0):
        cur1 = 0
    else:
        cur1 = x2*(x2*y1)/(x2+y1) 
    if(y3==0 and x2==0):
        cur2 = 0
    else:
        cur2 = x2*(x2*y3)/(x2+y3) 
    if(y2==0 and x1==0):
        cur3 = 0
    else:
        cur3 = y2*(x1*y2)/(x1+y2) 
    if(y2==0 and x3==0):
        cur4 = 0
    else:
        cur4 = y2*(x3*y2)/(x3+y2)
    m2=round(x2*y2+ cur1+cur2+cur3+cur4,2)

    m3=1-m1-m2
    
    rn = "{M1:"+str(m1)+" "+"M2:"+str(m2)+" "+"M3:"+str(m3)+"}"+" "
    return m1,m2,m3,rn

def mmmalogN(m1,m2,m3,z1,z2,z3):

    if(z2==0 and m1==0):
        res1 = 0
    else:
        res1 = m1*(m1*z2)/(m1+z2) 
    if(z3==0 and m1==0):
        res2 = 0
    else:
        res2 = m1*(m1*z3)/(m1+z3) 
    if(z1==0 and m2==0):
        res3 = 0
    else:
        res3 = z1*(m2*z1)/(m2+z1) 
    if(z1==0 and m3==0):
        res4 = 0
    else:
        res4 = z1*(m3*z1)/(m3+z1)
    N1=round(m1*z1+ res1+res2+res3+res4,2)
     
    
    if(z1==0 and m2==0):
        asd1 = 0
    else:
        asd1 = m2*(m2*z1)/(m2+z1) 
    if(z3==0 and m2==0):
        asd2 = 0
    else:
        asd2 = m2*(m2*z3)/(m2+z3) 
    if(z2==0 and m1==0):
        asd3 = 0
    else:
        asd3 = z2*(m1*z2)/(m1+z2) 
    if(z2==0 and m3==0):
        asd4 = 0
    else:
        asd4 = z2*(m3*z2)/(m3+z2)
    N2=round(m2*z2+ asd1+asd2+asd3+asd4,2)

    N3=1-N1-N2

    rn = "{N1:"+str(N1)+" "+"N2:"+str(N2)+" "+"N3:"+str(N3)+"}"+"\n"
    return N1,N2,N3,rn
def mmmalogK(x1,x2,x3,y1,y2,y3):
    k=x1*y2+x1*y3+x2*y1+x2*y3+x3*y2
    rn="{K:"+str(k)+"}"+" "
    return k,rn
def mmmalogR(x):
    y1=x
    y2=1.0-x
    y3=0.0
    rn = "{Rate:"+str(y1)+':'+str(y2)+':'+str(y3)+"}"+" "
    return y1,y2,y3,rn
def mmmalogD(x):
    t1=t2=t3=0
    if(x.has_key(1)):
        t1=x[1]
    if(x.has_key(2)):
        t2=x[2]
    if(x.has_key(3)):
        t3=x[3]
    num=t1*1.0+t2*0.4+t3*0.2
    if(num<3):
        y1=0
        y2=num/3.0
        y3=(3.0-num)/3.0
    elif(num>=3 and num<=6):
        y1=(num-3.0)/3.0
        y2=(6.0-num)/3.0
        y3=0.0
    else:
        y1=1.0
        y2=0.0
        y3=0.0
    y1=round(y1,2)
    y2=round(y2,2)
    y3=round(y3,2)
    rn = "{DifRate:"+str(y1)+':'+str(y2)+':'+str(y3)+"}"+" "
    return y1,y2,y3,rn


def mmmalogC(x):
    if(x<1):
        y1=0.0
        y2=x
        y3=1.0-x
    elif(x>=1 and x<=3):
        y1=(x-1)/2.0
        y2=(3-x)/2.0
        y3=0.0
    else:
        y1=1.0
        y2=0.0
        y3=0.0
    rn = "{ClassRate:"+str(y1)+':'+str(y2)+':'+str(y3)+"}"+" "
    return y1,y2,y3,rn
def opthandler():
    usage = "usage: %prog <options>"
    parser = OptionParser(usage)
    parser.add_option("-x", "--ip", dest="mip",
                    action="store_true",
                    help="mip is a output standard", default=False)
    (options, args) = parser.parse_args()
    return options,args
options,args = opthandler()
if(len(args) == 1):
    print args
    tem = args[0]
cl = 0
amm = 0
re = 1
amh = 0
readd = dict()
readd[1]=3
readd[2]=8
ret = 0
with open(tem,'r') as fr:
    for line in fr.readlines():
        rtm=line.split()[0]
        tm=line.split("[Priority: ",1)[1]
        tm=tm.split("]",1)[0]
        line.strip()
        tim =  line.split()
        tim = tim[0]
        timh = tim.split(":",1)[0]
        tmt=line.split("[Priority: ",1)[0]
        tmt=tmt.split("[**]",1)[1]
        tmt=tmt.split()
        # tim-h = tim-h[0]
        timm = tim.split(":",2)[1]
        t=line.split("[**]",2)
        t=t[2].split("[Prio",1)[0]
        # tim-m =  tim-m[0]
        if ('icmp' in tmt or 'PROTOCOL-ICMP' in tmt) or ('RPC' in tmt or 'rpc' in tmt) or ('sadmind' in tmt):
            ret = 0.8
        else:
            ret = 0.1
        if ( not (amh == timh and int(timm) < amm )):
            cl = 1
        if(cl == 1 ): 
            x1,x2,x3,rnc=mmmalogC(re+0.0) 
            y1,y2,y3,rnd=mmmalogD(readd)
            z1,z2,z3,rnr=mmmalogR(ret+0.0)
            k,rnk=mmmalogK(x1,x2,x3,y1,y2,y3)
            m1,m2,m3,rnm=mmmalogM(x1,x2,x3,y1,y2,y3)
            n1,n2,n3,rnn=mmmalogN(m1,m2,m3,z1,z2,z3)
            reout = rtm+" "+"Clas:"+str(re)+" "+"dif:"+str(readd)+" "+"Ret:"+str(ret)+" "+rnc+rnd+rnr+rnk+rnm+rnn
            with open(tem+'.bak','a') as fw:
                fw.write(reout)
            print reout
            readd=dict()
            readd[int(tm)] = 1
            amm = int(timm)+5
            amh = timh
            dif = list()
            dif.append(t)
            re = 1
            cl = 0
            ret = 0
            continue
        else:
            if readd.has_key(int(tm)) == 0:
                readd[int(tm)] = 1
            else:
                readd[int(tm)] +=1
            if t not in dif:
                dif.append(t)
                re = re + 1
    reout = "Clas:"+str(re)+" "+"dif:"+str(readd)+" "+"Ret:"+str(ret)+" "
    with open(tem+'.bak','a') as fw:
        fw.write(reout)