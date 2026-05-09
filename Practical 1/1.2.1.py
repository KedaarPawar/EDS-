n = int(input())
marks = list(map(int,input().split()))
if all( m>=40 for m in marks):
	agg = sum(marks)/n
	print("Aggregate Percentage:",'%.2f'%agg)
	if(agg>= 75):
		print("Grade: Distinction")
	elif(60<=agg<75):
		print("Grade: First Division")
	elif(50<=agg<60):
		print("Grade: Second Division")
	elif(40<=agg<50):
		print("Grade: Third Division")
else:
	print("Fail")
