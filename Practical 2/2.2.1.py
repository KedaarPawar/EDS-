l=list(map(int,input().split()))
key=int(input())
flag=0
pos=0
for i in range(len(l)):
	if(key==l[i]):
		flag=1
		pos=i
		break
if(flag==1):
	print(pos)
else:
	print("Not found")
