# 127156096_ASHLEY

Write a program that normalizes a numeric matrix by scaling each column independently to the
range [0, 1]. For columns where all values are the same (constant columns), output 0 for all entries.
All output values should be rounded to exactly 4 decimal places.
Requirements
 Scale each column independently using min-max normalizaƟon
 Formula: scaled_value = (value - min) / (max - min)
 Constant columns (where max = min) should output 0.0000
 Round all output values to exactly 4 decimal places
 Preserve matrix dimensions in output


Input:
3 2
10 5
20 5
30 5
Output:
0.0000 0.0000
0.5000 0.0000
1.0000 0.0000
Explanation:
 Column 1: values [10, 20, 30]
 min = 10, max = 30, range = 20
 Row 1: (10-10)/20 = 0.0000
 Row 2: (20-10)/20 = 0.5000
 Row 3: (30-10)/20 = 1.0000
 Column 2: values [5, 5, 5]  
NEGATIVE VALUES to be handled as follows : 
Example 2: NegaƟve Values
Input:
4 3
-10 0 100
0 50 200
10 100 300
20 150 400
Output:
0.0000 0.0000 0.0000
0.3333 0.3333 0.3333
0.6667 0.6667 0.6667
1.0000 1.0000 1.0000
Explanation : 
Column 1: [-10, 0, 10, 20]
 min = -10, max = 20, range = 30
 (-10-(-10))/30 = 0.0000
 (0-(-10))/30 = 0.3333
 (10-(-10))/30 = 0.6667
 (20-(-10))/30 = 1.0000
 Column 2: [0, 50, 100, 150]
 min = 0, max = 150, range = 150
 0/150 = 0.0000
 50/150 = 0.3333
 100/150 = 0.6667
 150/150 = 1.0000
 Column 3: [100, 200, 300, 400]
 min = 100, max = 400, range = 300
 0/300 = 0.0000
 100/300 = 0.3333
 200/300 = 0.6667
 300/300 = 1.0000


 All values identical (constant column)
 Output 0.0000 for all rows
