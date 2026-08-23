Coding Challenge 
Write a program that validates the balance and proper nesting of three types of 
brackets: parentheses (), square brackets [], and curly braces {}. The validator should 
detect the exact position of the first bracket error or confirm that all brackets are 
balanced. 
Requirements 
1. Check balance and nesting of: (), [], {} 
2. Ignore all other characters (letters, digits, symbols, spaces, etc.) 
3. Return BALANCED if all brackets are properly matched and nested 
4. Return ERROR:index if there's a bracket error (index is zero-based) 
5. For multiple errors, return the first error encountered (leftmost) 
 
Bracket Rules 
Valid Brackets 
• Parentheses: ( and ) 
• Square Brackets: [ and ] 
• Curly Braces: { and } 
Balance Requirements 
1. Every opening bracket must have a matching closing bracket 
2. Every closing bracket must match the most recent unmatched opening 
bracket 
3. Brackets must be properly nested (no cross-matching) 
Error Types 
Error Type Description Example Error Index 
Unmatched 
Closing 
Closing bracket without corresponding 
opening 
] or ) at 
start Index of closing bracket 
Wrong Type Closing bracket doesn't match opening (] Index of wrong closing 
bracket 

Error Type Description Example Error Index 
Leftover Opening Opening bracket never closed (a Index of leftover opening 
bracket 
 
Input Format 
• Single line: Text string 
• Can contain any printable ASCII characters 
• Maximum length: 100,000 characters 
 
Output Format 
If Balanced: 
BALANCED 
If Error Found: 
ERROR:index 
• index is the zero-based position of the first error 
• For leftover opening brackets, use the index of the first unclosed opening bracket 
 
Examples 
Example 1: Balanced Brackets 
Input: 
a[(b+c)] 
 
Output: 
BALANCED 
Explanation: 
• Position 1: [ opens 
• Position 2: ( opens 
• Position 6: ) closes the ( 

• Position 7: ] closes the [ 
• All brackets properly matched and nested 
 
Example 2: Unmatched Closing Bracket 
Input: 
]abc 
 
Output: 
ERROR:0 
Explanation: 
• Position 0: ] closing bracket with no opening bracket 
• Error at index 0 
 