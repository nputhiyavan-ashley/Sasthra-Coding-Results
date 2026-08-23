Coding Challenge: Minimum Coin Change 
Problem Statement 
Write a program that calculates the minimum number of coins needed to make a target amount. 
Given a set of coin denominaƟons that can be reused unlimited Ɵmes, determine the fewest coins 
required to reach the exact target value. If it's impossible to make the exact amount, return -1. 
Requirements 
 Calculate minimum coins needed for exact target amount 
 Coins can be reused unlimited Ɵmes 
 Return -1 if target cannot be achieved 
 Handle duplicate denominaƟons correctly 
 OpƟmize for minimum coin count 
Input Format 
 Line 1: Two space-separated integers n and target 
 n = number of coin denominaƟons 
 target = target amount to achieve 
 Line 2: n space-separated integers represenƟng coin denominaƟons 
Record Fields 
 n: Total number of coin denominaƟons 
 target: Target amount to make 
 Coin denominaƟons: PosiƟve integers represenƟng coin values 
Constraints 
 1 ≤ n ≤ 100 
 0 ≤ target ≤ 10,000 
 1 ≤ coin_value ≤ 10,000 
 Coins can be reused unlimited Ɵmes 
 Duplicate denominaƟons may exist 
Output Format 
 Single integer represenƟng: 
 Minimum number of coins needed to make target 
 -1 if target amount cannot be achieved exactly 
Examples 
Example 1: Basic Case 

Input: 
3 11 
1 5 6 
Output: 
2 
ExplanaƟon: 
 Target: 11 
 Available coins: [1, 5, 6] 
 Possible combinaƟons: 
 11 × 1 = 11 coins 
 1 × 5 + 6 × 1 = 7 coins 
 2 × 5 + 1 × 1 = 3 coins 
 1 × 6 + 1 × 5 = 2 coins ← minimum 
 Minimum coins: 2 (one 6-coin + one 5-coin) 
Example 2: Impossible Target 
Input: 
2 7 
3 5 
Output: 
-1 
ExplanaƟon: 
 Target: 7 
 Available coins: [3, 5] 
 Possible combinaƟons: 
 Cannot make 7 with coins of 3 and 5 
 3+3 = 6 (too small) 
 5 = 5 (too small) 
 3+5 = 8 (too large) 
 5+5 = 10 (too large) 
 No exact combinaƟon exists 
 Return: -1 