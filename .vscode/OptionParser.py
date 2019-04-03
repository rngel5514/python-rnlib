# -*- coding: utf-8 -*-
#from scapy.all import *
from optparse import OptionParser # 参数处理模块
# 2. 方法实现
def opthandler():
    #优先打印在程序的选项信息之前
    usage = "usage: %prog <options>"
    parser = OptionParser(usage)
    # 注册一个叫做`debug`的`-d`选项
    parser.add_option("-t", "--time", dest="time",
                    action="store_true",
                    help="time between start and end", default=False)
    parser.add_option("-s", "--size", dest="size",
                    action="store_true",
                    help="the pice packet size", default=False)
    parser.add_option("-n", "--num", dest="num",
                    action="store_true",
                    help="the pice packet size", default=False)
    parser.add_option("-i", "--interface", dest="ife",
                    action="store_true",
                    help="the pice packet size", default=False)
    (options, args) = parser.parse_args()
    return options,args
options,args = opthandler()
print type(options)
# options,args
#{'size': True, 'time': True} ['123', '99']
if __name__ == '__main__':
    (options,args) = opthandler()
    if options.size and options.num and options.ife:
        dpkt = sniff(args[2],count=100)
        wrpcap("demo.pcap", dpkt)
        #args[0]
    else:
        print 'need args'
