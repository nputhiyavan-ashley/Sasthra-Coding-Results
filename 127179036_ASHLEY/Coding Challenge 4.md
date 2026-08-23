Coding Challenge 
Write a program that processes employee performance scores by department and 
generates a summary report showing average score and highest score for each 
department. 
Requirements 
1. Group scores by department 
2. Calculate average score for each department (rounded to 2 decimal places) 
3. Find maximum score for each department 
4. Sort results by: 
• Primary: Average score (descending - highest average first) 
• Secondary: Department name (ascending - alphabetically) 
5. Output format: department:average:max 
6. Handle decimal scores and tied averages correctly 
 
Input Format 
• Line 1: An integer n (number of records) 
• Lines 2 to n+1: Records in format: department,score 
Record Fields 
• department: String, department name (no spaces or commas) 
• score: Number (can be integer or decimal) 
 
Output Format 
• One line per department: department:average:max 
• average: Rounded to exactly 2 decimal places (e.g., 85.00, 75.50) 
• max: Display as given (if integer, no decimals; if decimal, keep original precision) 
• Sorted by: 
1. Average descending (highest first) 
2. Department name ascending (alphabetical) for ties 
 

Examples 
Example 1: Basic Case 
Input: 
5 
AI,80 
CSE,70 
AI,90 
DS,75 
CSE,80 
 
Output: 
AI:85.00:90 
CSE:75.00:80 
DS:75.00:75 
Explanation: 
• AI: scores [80, 90] → average = 85.00, max = 90 
• CSE: scores [70, 80] → average = 75.00, max = 80 
• DS: scores [75] → average = 75.00, max = 75 
• Sorting: 
• AI (85.00) comes first (highest average) 
• CSE and DS tied at 75.00 → alphabetically: CSE before DS 
 
Example 2: Decimal Scores 
Input: 
6 
HR,85.5 
HR,90.3 
IT,88.7 

IT,92.1 
IT,87.5 
Sales,89.0 
 
Output: 
IT:89.43:92.1 
Sales:89.00:89.0 
HR:87.90:90.3 
Explanation: 
• IT: [88.7, 92.1, 87.5] → average = 268.3/3 = 89.43, max = 92.1 
• Sales: [89.0] → average = 89.00, max = 89.0 
• HR: [85.5, 90.3] → average = 175.8/2 = 87.90, max = 90.3 
• Sorted by average descending: 89.43, 89.00, 87.90 
 
Constraints 
• 1 ≤ n ≤ 100,000 
• Department names: alphabetic characters only (A-Z, a-z) 
• Scores: positive numbers (integers or decimals) 
• Score range: 0 ≤ score ≤ 100 