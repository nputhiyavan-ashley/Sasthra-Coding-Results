Coding Challenge 
Write a program that analyzes a CSV-like table and generates a data quality report 
showing the count of missing values and the percentage of valid (non-missing) values 
for each column. 
Requirements 
1. Read a CSV table with header row and data rows 
2. For each column, calculate: 
• Missing count: Number of missing values 
• Valid percentage: Percentage of non-missing values (rounded to 2 
decimals) 
3. Identify missing values: 
• Empty string: "" 
• The literal text: "NULL" (case-sensitive) 
• Missing trailing fields in short rows 
4. Output format: column:missing:valid_percentage for each column 
5. Handle edge cases: blank fields, short rows, fully missing columns 
 
Missing Value Rules 
What Counts as Missing? 
Value Type Example Is Missing? 
Empty string ,, or , at end ✓ Yes 
Literal "NULL" NULL (exact text) ✓ Yes 
Short row Row has fewer fields than header ✓ Yes (trailing fields) 
Whitespace only   or   ✗ No (valid value) 
Zero 0 ✗ No (valid value) 
Text "null" null (lowercase) ✗ No (valid value) 
Number 123 or -45 ✗ No (valid value) 
 

Important Notes 
• Case-sensitive: Only NULL (uppercase) is missing 
• Trailing fields: If a row has fewer commas, trailing fields are missing 
• Empty vs NULL: Both count as missing 
 
Input Format 
• Line 1: Header row (comma-separated column names) 
• Lines 2+: Data rows (comma-separated values) 
• No quoted commas (simple CSV parsing) 
• Maximum: 100 columns, 100,000 rows 
 
Output Format 
For each column (in header order): 
column_name:missing_count:valid_percentage 
• column_name: From header row 
• missing_count: Integer count of missing values 
• valid_percentage: Percentage of valid values, rounded to exactly 2 decimal 
places 
 
Valid Percentage Calculation 
valid_percentage = (valid_count / total_rows) × 100 
 
Where: 
- valid_count = total_rows - missing_count 
- total_rows = number of data rows (excluding header) 
 
Examples 
Example 1: Basic Missing Values 

Input: 
id,name,score 
1,Ana,80 
2,,90 
3,Cia,NULL 
 
Output: 
id:0:100.00 
name:1:66.67 
score:1:66.67 
Explanation: 
• Total data rows: 3 
• id column: 
• Row 1: 1 ✓ valid 
• Row 2: 2 ✓ valid 
• Row 3: 3 ✓ valid 
• Missing: 0, Valid: 3/3 = 100.00% 
• name column: 
• Row 1: Ana ✓ valid 
• Row 2: `` ✗ empty (missing) 
• Row 3: Cia ✓ valid 
• Missing: 1, Valid: 2/3 = 66.67% 
• score column: 
• Row 1: 80 ✓ valid 
• Row 2: 90 ✓ valid 
• Row 3: NULL ✗ missing 
• Missing: 1, Valid: 2/3 = 66.67% 
 

Example 2: Short Row (Missing Trailing Fields) 
Input: 
a,b,c 
1,2,3 
4,5 
6,7,8 
 
Output: 
a:0:100.00 
b:0:100.00 
c:1:66.67 
Explanation: 
• Total data rows: 3 
• Header has 3 columns: a, b, c 
• Row 2 is short: 4,5 (missing column c) 
• Column a: All present: [1, 4, 6] → Missing: 0 
• Column b: All present: [2, 5, 7] → Missing: 0 
• Column c: [3, missing, 8] → Missing: 1, Valid: 2/3 = 66.67% 
 