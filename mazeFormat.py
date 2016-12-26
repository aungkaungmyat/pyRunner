import numpy

A = numpy.matrix( [ [2 , 2 , 2 , 2 , 2 , 2 , 2 , 2] ,
				    [5 , 0 , 1 , 0 , 1 , 0 , 1 , 2] ,
					[2 , 0 , 1 , 0 , 1 , 0 , 1 , 2] ,
					[2 , 0 , 0 , 0 , 0 , 0 , 1 , 2] ,
					[2 , 1 , 0 , 1 , 1 , 0 , 0 , 2] ,
					[2 , 1 , 0 , 1 , 0 , 0 , 1 , 2] ,
					[2 , 1 , 0 , 1 , 0 , 0 , 0 , 5] ,
					[2 , 2 , 2 , 2 , 2 , 2 , 2 , 2]])


def mazeMap():
	
	
	start_point = A[1 , 0];
	end_point = A[6 , 7];

	print A
	print start_point
	print end_point
	# for x in A:
		
		# for y in A[x]:
			

		
mazeMap()		 	