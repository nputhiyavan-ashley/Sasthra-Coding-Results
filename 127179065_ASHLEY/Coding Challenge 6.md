Coding Challenge 
Write a program that processes a sequence of numbers using a sliding 
window approach. For each complete window of size k, calculate 
the average and maximum value, then output the results. 
Requirements 
1. Process n numbers with a sliding window of size k 
2. For each window, calculate: 
• Average: Mean of all values in the window (rounded to 2 decimal places) 
• Maximum: Largest value in the window 
3. Output one line per window in format: average,max 
4. Process windows from left to right (sliding one position at a time) 
5. Total windows = n - k + 1 
 
Input Format 
• Line 1: Two integers n and k (space-separated) 
• n = total number of elements 
• k = window size 
• Line 2: n space-separated numbers (integers or decimals) 
 
Output Format 
• One line per window: average,max 
• average: Rounded to exactly 2 decimal places 
• max: Display in original format (integer or decimal as given) 
• No spaces around the comma 
• Total output lines = n - k + 1 
 
Examples 
Example 1: Basic Sliding Window 
Input: 

5 3 
2 4 6 8 10 
 
Output: 
4.00,6 
6.00,8 
8.00,10 
Explanation: 
• Window 1: [2, 4, 6] → avg = 12/3 = 4.00, max = 6 
• Window 2: [4, 6, 8] → avg = 18/3 = 6.00, max = 8 
• Window 3: [6, 8, 10] → avg = 24/3 = 8.00, max = 10 
• Total windows: 5 - 3 + 1 = 3 
 
Example 2: Window Size = 1 
Input: 
4 1 
5 10 3 7 
 
Output: 
5.00,5 
10.00,10 
3.00,3 
7.00,7 
Explanation: 
• Window 1: [5] → avg = 5.00, max = 5 
• Window 2: [10] → avg = 10.00, max = 10 
• Window 3: [3] → avg = 3.00, max = 3 
• Window 4: [7] → avg = 7.00, max = 7 

• Total windows: 4 - 1 + 1 = 4 (one per element) 
 
Constraints 
• 1 ≤ k ≤ n ≤ 100,000 
• Numbers can be positive, negative, or zero 
• Numbers can be integers or decimals 
• Number range: -1,000,000 ≤ value ≤ 1,000,000 
 