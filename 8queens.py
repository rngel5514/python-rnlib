'''
八皇后问题，是一个古老而著名的问题，是回溯算法的典型案例。该问题是国际西洋棋棋手马克
斯·贝瑟尔于1848年提出：在8X8格的国际象棋上摆放八个皇后，使其不能互相攻击，即任意两个
皇后都不能处于同一行、同一列或同一斜线上，问有多少种摆法。 高斯认为有76种方案。1854
年在柏林的象棋杂志上不同的作者发表了40种不同的解，后来有人用图论的方法解出92种结果。
计算机发明后，有多种方法可以解决此问题。
'''
results = []
disk_tmp = []
result = 0
for i in range(8):
        disk_tmp.append([0,0,0,0,0,0,0,0])
disk_test = [[0,0,0],[0,0,0],[0,0,0]]
def confilict(disk,line,i):
        for j in range(line):
                if((j+i-line >= 0 and j+i-line < 8 and disk[j][j+i-line] == 1 ) or (i+line -j >=0 and i+line -j <8 and disk[j][i+line-j] == 1 ) or disk[j][i] == 1):
                        return True
        return False
def queen(disk,line):
        global result
        if(line > 7 ):
                result = result +1
                print(disk)
                return 
        for i in range(8):
                if(not confilict(disk,line,i)):
                        #print(disk)
                        disk[line][i] = 1
                        queen(disk.copy(),line+1)  
                        disk[line][i] = 0
                
if __name__ == '__main__':
        queen(disk_tmp.copy(),0)
        print(result)
