import math

def main(y):
	n = int(y)
	r = 16
	npr = math.factorial(n)/math.factorial(n-r);
	ncr = npr/math.factorial(r);
	print("Steps =",ncr);
	#print("nPr =",npr);

if __name__ == "__main__":
	print("Enter 'x' for exit.")
	x = input("Input a number  ")
	
	if x == 'x':
		raise SystemExit
		
	elif x.isdigit():
		y = int(x)
	else:
		print("ERROR 612: Only INT Values Accepted")
		raise SystemExit
		
	main(y)