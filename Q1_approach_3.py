# find the reverse of a number provided by the user 
# by using the recursion

def reverse(num,rev=0):
	if(num==0): # anchor step
		return rev
	return reverse(num//10,rev*10+num%10) # recursive step
# main program 
number=int(input("enter a number:"))
reversed_value=reverse(number)
print("reversed value=",reversed_value)