import numpy as np
n=int(input("Berapa baris dan kolom :"))
m=n+1
z = np.zeros(n)
val = [0] * n
for x in range (n):
    val[x] =[0.0] * m

for i in range(n):
    for j in range(n+1):
        print(("[{}][{}]").format(i,j),end=' ')
        y=float(input("Masukkan nilai :"))
        val[i][j]=y


#eliminasi maju
for i in range(n):
    for j in range(i+1, n):
        ratio = val[j][i]/val[i][i]
        for k in range(n+1):
            val[j][k] = val[j][k] - ratio * val[i][k]

#eliminasi mundur
z[n-1] = val[n-1][n]/val[n-1][n-1]
for i in range(n-2,-1,-1):
    z[i] = val[i][n]
    for j in range(i+1,n):
        z[i] = z[i] - val[i][j]*z[j]
    z[i] = z[i]/val[i][i]

print('Solusi :')
for i in range(n):
    print('X%d = %0.2f' %(i,z[i]), end = '\t')


