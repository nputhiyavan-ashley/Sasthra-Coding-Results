Coding Challenge 
Write a program that detects outliers in a dataset using the IQR (Interquartile Range) 
method. The program calculates Q1 (first quartile) and Q3 (third quartile) using the 
median-of-halves approach, then identifies values that fall outside the acceptable 
range defined by the IQR boundaries. 
Requirements 
1. Calculate Q1 and Q3 using the median-of-halves method 
2. For odd-length arrays, exclude the overall median when splitting into halves 
3. Calculate IQR = Q3 - Q1 
4. Find outliers: values < Q1 - 1.5×IQR OR values > Q3 + 1.5×IQR 
5. Return outliers in original order (as they appeared in input) 
6. Return NONE if no outliers exist 
 
Statistical Definitions 
Quartiles (Q1 and Q3) 
Q1 (First Quartile): The median of the lower half of the data 
Q3 (Third Quartile): The median of the upper half of the data 
Median-of-Halves Method 
1. Sort the data 
2. Find the overall median 
3. Split into halves: 
• If array length is even: divide exactly in half 
• If array length is odd: exclude the median, then split 
4. Q1 = median of lower half 
5. Q3 = median of upper half 
IQR (Interquartile Range) 
IQR = Q3 - Q1 
Outlier Boundaries 
Lower Boundary: 

Lower = Q1 - 1.5 × IQR 
Upper Boundary: 
Upper = Q3 + 1.5 × IQR 
Outliers: 
• Any value < Lower 
• Any value > Upper 
 
Median Calculation 
For Even-Length Array 
Median = average of two middle values 
Example: [1, 2, 3, 4] → median = (2 + 3) / 2 = 2.5 
For Odd-Length Array 
Median = middle value 
Example: [1, 2, 3, 4, 5] → median = 3 
 
Input Format 
• Line 1: Integer n (number of values) 
• Line 2: n space-separated numbers (integers or decimals) 
 
Output Format 
If outliers exist: 
value1 value2 value3 ... 
• Space-separated outlier values 
• In original order (as they appeared in input) 
• If value appears multiple times, include all occurrences 
If no outliers exist: 
NONE 
 

Examples 
Example 1: Single Outlier 
Input: 
8 
10 12 11 13 12 14 100 9 
 
Output: 
100 
Explanation: 
• Sorted: [9, 10, 11, 12, 12, 13, 14, 100] 
• Length: 8 (even) 
• Median: (12 + 12) / 2 = 12 
• Lower half: [9, 10, 11, 12] → Q1 = (10 + 11) / 2 = 10.5 
• Upper half: [12, 13, 14, 100] → Q3 = (13 + 14) / 2 = 13.5 
• IQR: 13.5 - 10.5 = 3 
• Lower bound: 10.5 - 1.5×3 = 10.5 - 4.5 = 6 
• Upper bound: 13.5 + 1.5×3 = 13.5 + 4.5 = 18 
• Outliers: Values < 6 OR > 18 → 100 (only value > 18) 
• Original order: 100 appears at position 6 in input 
 
Example 2: No Outliers 
Input: 
6 
5 6 7 8 9 10 
 
Output: 
NONE 
Explanation: 

• Sorted: [5, 6, 7, 8, 9, 10] 
• Length: 6 (even) 
• Median: (7 + 8) / 2 = 7.5 
• Lower half: [5, 6, 7] → Q1 = 6 
• Upper half: [8, 9, 10] → Q3 = 9 
• IQR: 9 - 6 = 3 
• Lower bound: 6 - 1.5×3 = 6 - 4.5 = 1.5 
• Upper bound: 9 + 1.5×3 = 9 + 4.5 = 13.5 
• Outliers: All values are between 1.5 and 13.5 → NONE 
 
Constraints 
• 4 ≤ n ≤ 10,000 
• Values can be positive, negative, or zero 
• Values can be integers or decimals 
• Value range: -1,000,000 ≤ value ≤ 1,000,000 