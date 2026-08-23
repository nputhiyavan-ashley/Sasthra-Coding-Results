Coding Challenge 
Write a program that finds the second highest distinct integer from a list of integers 
and returns both the value and its first zero-based index in the original list. 
Requirements 
1. Identify the second highest distinct integer (duplicates count as one value) 
2. Return the value and its first occurrence index (zero-based) 
3. DO NOT sort the full list - use an efficient approach 
4. Return NA if fewer than two distinct values exist 
5. Handle negative numbers, duplicates, and edge cases 
 
Input Format 
• Line 1: An integer n (the number of elements) 
• Line 2: n space-separated integers 
 
Output Format 
• If second highest exists: value index (space-separated) 
• value = the second highest distinct integer 
• index = zero-based index of its first occurrence 
• If fewer than two distinct values: NA 
 
Examples 
Example 1: Basic Case 
Input: 
6 
4 8 2 8 6 4 
 
Output: 
6 4 

Explanation: 
• Distinct values: 2, 4, 6, 8 
• Highest: 8 
• Second highest: 6 
• First occurrence of 6 is at index 4 (zero-based) 
 
Example 2: Duplicates of Second Highest 
Input: 
7 
10 5 10 20 5 20 15 
 
Output: 
15 6 
Explanation: 
• Distinct values: 5, 10, 15, 20 
• Highest: 20 
• Second highest: 15 
• First occurrence of 15 is at index 6 
 
Constraints 
• 1 ≤ n ≤ 100,000 
• Integer values can be positive, negative, or zero 
• Integers can range from -1,000,000 to 1,000,000 
 