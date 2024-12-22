# find the reverse of a number provided by the user 
# by using the loops
num=int(input("enter a number:"))
rev=0
while(num>0):
	digit=num%10
	rev=rev*10+digit
	num=num//10
else:
	print("reversed value=",rev)