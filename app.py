import sys
2	
3	def perform_operation(num1, num2, operation):
4	    if operation == "add":
5	        return num1 + num2
6	    elif operation == "sub":
7	        return num1 - num2
8	    elif operation == "mul":
9	        return num1 * num2
10	    elif operation == "div":
11	        return num1 / num2
12	    else:
13	        return "Invalid operation"
14	
15	# Get input values from command line arguments
16	num1 = float(sys.argv[1])
17	num2 = float(sys.argv[2])
18	operation = sys.argv[3]
19	
20	result = perform_operation(num1, num2, operation)
21	
22	print("Result:", result)
