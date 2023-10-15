import math
def Nth_of_GP(a, r, N):
  return(a * (int)(math.pow(r, N - 1)))
if __name__ == "__main__":
	a = 2 
	r = 3 
	N = 90 
	print("The", N, "th term of the series is :",
		Nth_of_GP(a, r, N))


