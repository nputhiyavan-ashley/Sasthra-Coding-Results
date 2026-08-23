Coding Challenge 
Write a program that calculates the sum of all border cells in a rectangular matrix. 
Border cells are those in the first row, last row, first column, or last column. Each cell 
should be counted exactly once, even if it belongs to multiple borders (corners). 
Requirements 
1. Read a rectangular matrix of integers 
2. Identify all border cells (perimeter cells) 
3. Sum the values of border cells 
4. Count each cell exactly once (even corner cells) 
5. Return the total sum as an integer 
 
Border Cell Definition 
Border Cells Include: 
• First row: All cells in row 0 
• Last row: All cells in row r-1 
• First column: All cells in column 0 
• Last column: All cells in column c-1 
Corner Cells: 
Corner cells belong to two borders but should be counted only once. 
Visual Example: 
3x4 matrix: 
B  B  B  B    (B = Border cell) 
B  .  .  B    (. = Interior cell) 
B  B  B  B 
 
Border cells: 
- Row 0: all 4 cells 
- Row 2: all 4 cells   
- Column 0: middle cell (row 1) 

- Column 3: middle cell (row 1) 
 
Total border cells: 4 + 4 + 1 + 1 = 10 cells 
 
Input Format 
• Line 1: Two integers r and c (space-separated) 
• r = number of rows 
• c = number of columns 
• Next r lines: Each line contains c space-separated integers (matrix values) 
 
Output Format 
• Single integer: the sum of all border cell values 
 
Examples 
Example 1: Standard 3x4 Matrix 
Input: 
3 4 
1 2 3 4 
5 6 7 8 
9 10 11 12 
 
Output: 
65 
Explanation: 
Matrix visualization: 
1  2  3  4    (Row 0: border) 
5  6  7  8    (Row 1: only columns 0 and 3 are border) 
9 10 11 12    (Row 2: border) 

 
Border cells: 
- Row 0: 1 + 2 + 3 + 4 = 10 
- Row 2: 9 + 10 + 11 + 12 = 42 
- Column 0 (middle): 5 
- Column 3 (middle): 8 
 
Total: 10 + 42 + 5 + 8 = 65 
 
Example 2: Single Cell (1x1) 
Input: 
1 1 
42 
 
Output: 
42 
Explanation: 
• Only one cell in the matrix 
• It is a border cell 
• Sum: 42 
 
Constraints 
• 1 ≤ r, c ≤ 1,000 
• Matrix values: -1,000,000 ≤ value ≤ 1,000,000 