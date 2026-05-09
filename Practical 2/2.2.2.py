l=list(map(int,input().split()))
max=l[0]
for i in l:
	if i > max:
		max = i
print(max)
