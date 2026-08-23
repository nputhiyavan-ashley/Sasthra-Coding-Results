Coding Challenge 
Write a program that validates a password against a set of security rules and provides 
detailed feedback on which rules passed or failed, along with an overall strength score. 
Requirements 
1. Validate password against 6 security rules 
2. Return validation status: VALID or INVALID 
3. If invalid, list all failed rules (comma-separated) 
4. Calculate and return a score (0 to 6) based on rules passed 
5. Handle edge cases: spaces, empty input, multiple failures 
 
Validation Rules 
A strong password must meet ALL of the following criteria: 
Rule Description Keyword 
1. Minimum Length At least 8 characters length 
2. Uppercase Letter At least one uppercase letter (A-Z) uppercase 
3. Lowercase Letter At least one lowercase letter (a-z) lowercase 
4. Digit At least one digit (0-9) digit 
5. Special Character At least one special character (!@#$%^&*()_+-=[]{};:'" ,.<>?/|`~) special 
6. No Spaces Must not contain any spaces space 
 
Scoring System 
• Score = Number of rules passed (0 to 6) 
• Each rule passed adds 1 point to the score 
• A password is VALID only if score = 6 (all rules passed) 
 
Input Format 
• Single line: A password string 
• Password length ≤ 1,000 characters 

• Can contain any printable ASCII characters 
 
Output Format 
If VALID (all 6 rules passed): 
VALID score:6 
If INVALID (one or more rules failed): 
INVALID:rule1,rule2,... score:n 
• List all failed rules in the order they appear in the rules table 
• Rules separated by commas (no spaces after commas) 
• Score = number of rules that passed 
Rule Keywords for Output 
• length - Minimum length requirement failed 
• uppercase - Missing uppercase letter 
• lowercase - Missing lowercase letter 
• digit - Missing digit 
• special - Missing special character 
• space - Contains spaces (not allowed) 
 
Examples 
Example 1: Missing Special Character 
Input: 
Campus25 
 
Output: 
INVALID:special score:5 
Explanation: 
• ✓ Length: 8 characters (passes) 
• ✓ Uppercase: C (passes) 

• ✓ Lowercase: a, m, p, u, s (passes) 
• ✓ Digit: 2, 5 (passes) 
• ✗ Special: none (fails) 
• ✓ No spaces (passes) 
• Score: 5/6 rules passed 
• Failed rules: special 
 
Example 2: Valid Password 
Input: 
SecurePass123! 
 
Output: 
VALID score:6 
Explanation: 
• ✓ Length: 14 characters 
• ✓ Uppercase: S, P 
• ✓ Lowercase: e, c, u, r, e, a, s, s 
• ✓ Digit: 1, 2, 3 
• ✓ Special: ! 
• ✓ No spaces 
• Score: 6/6 - ALL PASSED 
 