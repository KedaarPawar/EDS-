n = int(input(""))
ans = 0

while(n>0):
	sum=n%10
	ans=ans*10+sum
	n=n//10
print(ans)
