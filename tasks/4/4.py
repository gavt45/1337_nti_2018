# put your python code here

def dir(t1,t2):
    if abs(t1 - t2) == 0:
        k = 0
    elif abs(t1 - t2) == 2:
        k = 2
    else:
        k = 1
    return k
n,m = map(int,input().split())
a = [['#'] *(m + 1) for i in range(n + 1)]
f = [[-1] *(m + 1) for i in range(n + 1)]
for i in range(1,n+1):
    l = input()
    if l.find('s') != -1:
        iis = i
        jjs = l.find('s') + 1
    if l.find('f') != -1:
        iif = i
        jjf = l.find('f') + 1
    for j in range(1,m+1):
        a[i][j] = l[j-1]
t1,t2 = 1,1
for i in range(iis+1, n+1):
    if a[i][jjs] != '#':
        f[i][ jjs] = i - 1
    else:
        f[i][ jjs] = -1
for j in range(jjs+1,m+1):
    if a[iis][j] != '#':
        f[iis][j] = j
    else:
        f[iis][j] = -1
ks = 0
for i in range(iis+1,iif+1):
    if ks == jjf - jjs +1:
        
        break
    for j in range(jjs+1,jjf+1):
        if a[i][j] == '#':
            f[i][j] = -1
            ks += 1
        else:
            if f[i][j-1] != -1 and f[i-1][j] != -1:
                f[i][j]  = min(f[i][j-1] + dir(t1,2),f[i-1][j] + dir(t1,1)) + 1
                if f[i][j] == f[i][j-1] + dir(t1,2) + 1: t1 = 2
            
                if f[i][j] == f[i-1][j] + dir(t1,1) + 1: t1 = 1
            
            elif f[i][j-1] == -1 and f[i-1][j] != -1:
                f[i][j] = f[i-1][j] + dir(t1,1) + 1
                t1 = 1
            elif f[i-1][j] == -1 and f[i][j-1] != -1:
                f[i][j] = f[i][j-1] + dir(t1,2) + 1
                t1 = 2
            else:
                f[i][j] = -1
            
    t1 = 1
        
if ks == 0:        
    print(f[iif][jjf])
else:
    print(-1)




