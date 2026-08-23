Coding Challenge 
Write a program that finds two distinct indices in an array such that the values at those 
indices sum to a given target. When multiple valid pairs exist, return the pair with the 
smallest second index, and if there's still a tie, the smallest first index. 
Requirements 
1. Find two distinct indices i and j where i < j 
2. The values at these indices must sum to target: array[i] + array[j] = target 
3. If multiple valid pairs exist, choose the pair with: 
• Primary: Smallest second index j 
• Secondary: Smallest first index i (when j is tied) 
4. Return indices as i j (zero-based, space-separated) 
5. Return NONE if no valid pair exists 
 
Index Selection Rules 
Priority Rules (When Multiple Pairs Exist) 
1. First Priority: Choose the pair with the smallest second index (j) 
2. Second Priority: If multiple pairs have the same j, choose the one with 
the smallest first index (i) 
Why These Rules? 
These rules ensure a deterministic result when multiple valid pairs exist. 
Example 
Array: [1, 2, 3, 4, 5], Target: 6 
Indices: 0  1  2  3  4 
 
Valid pairs: 
- (0, 4): 1 + 5 = 6 → indices 0, 4 
- (1, 3): 2 + 4 = 6 → indices 1, 3 
 
Comparison: 

- Pair (1, 3): second index = 3 
- Pair (0, 4): second index = 4 
 
3 < 4, so choose (1, 3) 
Answer: 1 3 
 
Input Format 
• Line 1: Two integers n and target (space-separated) 
• n = number of elements 
• target = target sum 
• Line 2: n space-separated integers (the array) 
 
Output Format 
If a valid pair exists: 
i j 
• i and j are zero-based indices where i < j 
• Space-separated 
If no valid pair exists: 
NONE 
 
Examples 
Example 1: Basic Case 
Input: 
5 9 
2 7 4 5 1 
 
Output: 
0 1 

Explanation: 
• Array: [2, 7, 4, 5, 1] 
• Target: 9 
• Valid pairs: 
• (0, 1): 2 + 7 = 9 ✓ 
• (2, 3): 4 + 5 = 9 ✓ 
• Compare second indices: 1 < 3 
• Answer: 0 1 
 
Example 2: No Valid Pair 
Input: 
4 10 
1 2 3 4 
 
Output: 
NONE 
Explanation: 
• Array: [1, 2, 3, 4] 
• Target: 10 
• Maximum possible sum: 3 + 4 = 7 
• No pair sums to 10 
 
Constraints 
• 2 ≤ n ≤ 100,000 
• Values can be positive, negative, or zero 
• Value range: -1,000,000 ≤ value ≤ 1,000,000 
• Target range: -2,000,000 ≤ target ≤ 2,000,000 