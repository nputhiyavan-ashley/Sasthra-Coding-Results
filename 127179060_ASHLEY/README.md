Write a program that finds the value whose second occurrence appears earliest in the
sequence, and calculates the distance (number of positions) between its first and
second occurrence.
1. Find the value that repeats first (earliest second occurrence)
2. Calculate the distance between its first and second occurrence
3. Distance = index of second occurrence - index of first occurrence
4. Return value distance if a repeat exists
5. Return NONE if no value appears more than once
6. Use zero-based indexing for distance calculation

Constraints
• 1 ≤ n ≤ 100,000
• Values can be positive, negative, or zero
• Value range: -1,000,000 ≤ value ≤ 1,000,000

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
