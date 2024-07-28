

1. Data Types in python
Int, Float, Double, Bool, etc.

2.  Swap 1st and Last digit of a given list
	alist = [1,5,8,10]
	alist[0],alist[-1] = alist[-1],alist[0]
	print(alist)
	
	#Output = [10,5,8,1]
 
3. append a value in a list.
	list1 = [1, 2, 3, [200, 200, [5000, 6000], 300], 5, 6]

	# Adding 7000 to the innermost list
	list1[3][2].append(7000)
	print(list1)
 
	#Output = [1, 2, 3, [200, 200, [5000, 6000, 7000], 300], 5, 6]
 
4. str = "English = 23, maths = 30, science = 50" extract marks and find avg in python
    
	import re
	# Given string
	str_data = "English = 23, maths = 30, science = 50"
 
	# Extract numerical values using regular expression
	marks = [int(match.group()) for match in re.finditer(r'\d+', str_data)]
 
	# Calculate the average
	average_marks = sum(marks) / len(marks) if len(marks) > 0 else 0
 
	print("Marks:", marks)
	print("Average Marks:", average_marks)
