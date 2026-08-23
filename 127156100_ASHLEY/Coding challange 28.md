Coding Challenge: Longest Substring Without RepeaƟng Characters 
Problem Statement 
Write a program that ﬁnds the longest substring without repeaƟng characters in a given string. 
Return both the length of the longest substring and its starƟng index (0-based). If mulƟple substrings 
have the same maximum length, return the one with the smallest starƟng index. 
Requirements 
 Find longest substring with all unique characters 
 No character can repeat within the substring 
 Return both length and starƟng index 
 Use 0-based indexing for starƟng posiƟon 
 For Ɵes (mulƟple substrings with same max length), choose the one starƟng earliest 
 Handle empty strings and single characters 
 Case-sensiƟve comparison (e.g., 'A' and 'a' are diﬀerent) 
Input Format 
 Single line: A string (may contain any characters including spaces) 
Record Fields 
 Input string: Can contain leƩers, digits, spaces, special characters 
 Empty string is valid input 
Constraints 
 0 ≤ string_length ≤ 100,000 
 String can contain any printable ASCII characters 
 Characters are case-sensiƟve 
Output Format 
 Single line: Two space-separated integers length start_index 
 length: Length of longest substring without repeaƟng characters 
 start_index: 0-based starƟng posiƟon of that substring 
Examples 
Example 1: Basic Case 
Input: 
abcabcbb 
Output: 
3 0 

ExplanaƟon: 
 Input: "abcabcbb" 
 Substrings without repeaƟng characters: 
 StarƟng at 0: "abc" → length 3 
 StarƟng at 1: "bca" → length 3 
 StarƟng at 2: "cab" → length 3 
 StarƟng at 3: "abc" → length 3 
 StarƟng at 4: "bc" → length 2 
 StarƟng at 5: "cb" → length 2 
 StarƟng at 6: "b" → length 1 
 StarƟng at 7: "b" → length 1 
 Maximum length: 3 
 MulƟple substrings with length 3, choose earliest start (index 0) 
 Output: 3 0 
Example 2: All Unique Characters 
Input: 
abcdef 
Output: 
6 0 
ExplanaƟon: 
 All characters are unique 
 EnƟre string "abcdef" is the longest substring 
 Length: 6, Start: 0 