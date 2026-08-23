Coding Challenge 
Write a program that reads a line of text and returns the top 3 most frequent 
alphabetic words along with their occurrence counts. 
Requirements 
1. Count each alphabetic word in the input (case-insensitive) 
2. Return the top 3 most frequent words with their counts 
3. When multiple words have the same frequency, sort them alphabetically 
4. Ignore all digits, punctuation, and special characters 
5. Only alphabetic characters form valid words 
 
Input Format 
• A single line of text 
• May contain letters, digits, punctuation, and special characters 
• Maximum length: 100,000 characters 
Output Format 
• Up to three lines in the format: word:count 
• Words must be in lowercase 
• Sorted by: 
• Primary: Frequency (descending - highest count first) 
• Secondary: Alphabetical order (for words with same frequency) 
• If fewer than 3 unique words exist, output only those words 
 
Examples 
Example 1: Basic Case 
Input: 
Data science uses data; science finds insight. 
 
Output: 

data:2 
science:2 
finds:1 
Explanation: 
• "data" and "science" both appear twice (tied at highest frequency) 
• Alphabetically, "data" comes before "science" 
• "finds" appears once (third most frequent) 
 
Example 2: Punctuation and Capitalization 
Input: 
Ashley furniture! Ashley designs, Ashley delivers quality furniture. 
 
Output: 
ashley:3 
furniture:2 
delivers:1 
Explanation: 
• "Ashley" appears 3 times (case-insensitive) 
• "furniture" appears 2 times 
• "delivers" appears once 
 
Constraints 
• Input text length ≤ 100,000 characters 
• Only alphabetic characters (a-z, A-Z) form valid words 
• Words are separated by any non-alphabetic characters (spaces, punctuation, 
digits, special characters) 
• Your solution must handle the maximum input size efficiently 