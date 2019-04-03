from optparse import OptionParser 

def opthandler():
    usage = "usage: %prog <options>"
    parser = OptionParser(usage)
    parser.add_option("-x", "--ip", dest="mip",
                    action="store_true",
                    help="mip is a output standard", default=False)
    (options, args) = parser.parse_args()
    return options,args
a = 0
options,args = opthandler()
if(len(args) == 1):
    print args
    tem = args[0]
    print type(tem)
#print type(options)
#if(options['mip'] == True):
#   print args
with open('alert','r') as fr:
    for line in fr.readlines():
        line.strip()
        t=line.split()
        tem2 = t[len(t)-1].split(":",1)
        tem2 = tem2[0]
        if (tem2 == tem):
            with open(tem2,'a') as fw:
                fw.write(line)
            a = a+1
            print a 
        #for i in range(len(tem)) :
         #   if(tem[i]=)

        #print(line.split())
        
        