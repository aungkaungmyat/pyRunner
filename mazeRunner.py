import numpy

A = numpy.matrix( [ [2 , 2 , 2 , 2 , 2 , 2 , 2 , 2] ,
				    [0 , 0 , 1 , 0 , 1 , 0 , 1 , 2] ,
					[2 , 0 , 1 , 0 , 1 , 0 , 1 , 2] ,
					[2 , 0 , 0 , 0 , 0 , 0 , 1 , 2] ,
					[2 , 1 , 0 , 1 , 1 , 0 , 0 , 2] ,
					[2 , 1 , 0 , 1 , 0 , 0 , 1 , 2] ,
					[2 , 1 , 0 , 1 , 0 , 0 , 0 , 5] ,
					[2 , 2 , 2 , 2 , 2 , 2 , 2 , 2]])


end_point = A[6 , 7]

def mazeSolver(x , y):
	
	

	if(x < 0 or y < 0 or x > len(A) or y > len(A) or A[x , y] != 0):
		return False

	
	
	A[x , y] = 3

	print(A)



	if(A[x+1 , y] == 5 or A[x-1 , y] == 5 or A[x , y-1] == 5 or A[x , y+1] ==5):
		return True


		

	if(mazeSolver(x+1 , y) or mazeSolver(x-1 , y) or mazeSolver(x , y+1) or mazeSolver(x , y-1)):
		return True

	A[x , y] = 0
	return False


print(mazeSolver(1 , 0))
print(A)
# A[1 , 0] = 3

