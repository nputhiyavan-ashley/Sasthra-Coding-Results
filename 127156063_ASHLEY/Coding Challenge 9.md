Coding Challenge 
Write a program that finds the value whose second occurrence appears earliest in the 
sequence, and calculates the distance (number of positions) between its first and 
second occurrence. 
Requirements 
1. Find the value that repeats first (earliest second occurrence) 
2. Calculate the distance between its first and second occurrence 
3. Distance = index of second occurrence - index of first occurrence 
4. Return value distance if a repeat exists 
5. Return NONE if no value appears more than once 
6. Use zero-based indexing for distance calculation 
 
Distance Calculation 
Formula 
distance = index_of_second_occurrence - index_of_first_occurrence 
Example 
Array: [5, 1, 3, 4, 3, 5, 6] 
Index:  0  1  2  3  4  5  6 
 
Value 3: 
- First occurrence: index 2 
- Second occurrence: index 4 
- Distance: 4 - 2 = 2 
 
Value 5: 
- First occurrence: index 0 
- Second occurrence: index 5 
- Distance: 5 - 0 = 5 
 

Winner: 3 (second occurrence at index 4 comes before 5's at index 5) 
 
Input Format 
• Line 1: Integer n (number of elements) 
• Line 2: n space-separated integers 
 
Output Format 
If a repeat exists: 
value distance 
• value = the value with earliest second occurrence 
• distance = number of positions between first and second occurrence 
If no repeat exists: 
NONE 
 
Examples 
Example 1: Basic Case 
Input: 
7 
5 1 3 4 3 5 6 
 
Output: 
3 2 
Explanation: 
• Value 5: First at index 0, second at index 5 → distance = 5 
• Value 3: First at index 2, second at index 4 → distance = 2 
• Value 1: No repeat 
• Value 4: No repeat 
• Value 6: No repeat 

• Winner: Value 3 (second occurrence at index 4 is earliest) 
• Distance: 4 - 2 = 2 
 
Example 2: No Repeats 
Input: 
5 
1 2 3 4 5 
 
Output: 
NONE 
Explanation: 
• Every value appears exactly once 
• No repeats found 
 
Constraints 
• 1 ≤ n ≤ 100,000 
• Values can be positive, negative, or zero 
• Value range: -1,000,000 ≤ value ≤ 1,000,000 