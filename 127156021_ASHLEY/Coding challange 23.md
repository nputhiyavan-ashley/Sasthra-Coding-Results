Coding Challenge: Longest ConsecuƟve Sequence 
Problem Statement 
Write a program that ﬁnds the length of the longest sequence of consecuƟve integers in an unsorted 
list. Given a list of integers, determine the maximum length of a sequence where each number is 
exactly one more than the previous number, without requiring the numbers to be adjacent in the 
original list. 
Requirements 
 Find longest consecuƟve integer sequence 
 Numbers don't need to be adjacent in input 
 Sequence must be consecuƟve (e.g., 1,2,3,4 not 1,2,4) 
 Handle duplicates (ignore repeated values) 
 Handle negaƟve numbers 
 Return sequence length only (not the actual sequence) 
Input Format 
 Line 1: An integer n (number of values) 
 Line 2: n space-separated integers 
Record Fields 
 n: Total number of integers in the list 
 Integer values: Can be posiƟve, negaƟve, or zero 
Constraints 
 1 ≤ n ≤ 50,000 
 -1,000,000 ≤ integer_value ≤ 1,000,000 
 Duplicates may exist 
 Values are not sorted 
Output Format 
 Single integer represenƟng the length of the longest consecuƟve sequence 
Examples 
Example 1: Basic Case 
Input: 
6 
100 4 200 1 3 2 
Output: 

4 
ExplanaƟon: 
 Input list: [100, 4, 200, 1, 3, 2] 
 Possible consecuƟve sequences: 
 [1, 2, 3, 4] → length 4 ← longest 
 [100] → length 1 
 [200] → length 1 
 Longest consecuƟve sequence: 1,2,3,4 
 Length: 4 
Example 2: With Duplicates 
Input: 
8 
10 5 12 10 11 5 13 14 
Output: 
4 
ExplanaƟon: 
 Input list: [10, 5, 12, 10, 11, 5, 13, 14] 
 Unique values: [10, 5, 12, 11, 13, 14] 
 Possible consecuƟve sequences: 
 [5] → length 1 
 [10, 11, 12, 13, 14] → length 5 ← longest 
 Duplicates (10, 5) are ignored 
 Length: 5 