from __future__ import print_function


n = input("> ")
n = 2000+n
r=[0]*(n+1)
c=0

for i in range(0,n):
	r[i] = 2000
	
for k in range(n,0,-14):
	d=0
	i=k
	while True:
		d+=r[i] * 10000
		b= 2*i-1	
		r[i] = d%b
		d/=b
		i-=1
		if i ==0:
			break
		
		d*=i
	print("%.4d"%(c+d/10000),end=" ")
	
	
	c=d%10000
