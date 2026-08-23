Coding Challenge: JSON Record Filter with Compound CondiƟons 
Problem Statement 
Write a program that ﬁlters JSON records based on compound boolean condiƟons. Given a collecƟon 
of ﬂat JSON objects and a ﬁlter expression with exactly two condiƟons joined by AND, return only the 
records that saƟsfy both condiƟons. Support comparison operators for both numeric and string 
values. 
Requirements 
 Parse ﬂat JSON objects (one level, no nesƟng) 
 Evaluate ﬁlter expression with exactly two condiƟons 
 Support operators: =, !=, >, >=, <, <= 
 Both condiƟons must be true (AND logic) 
 Handle numeric comparisons (integers/decimals) 
 Handle string comparisons (case-sensiƟve equality/inequality only) 
 Output matching records in original order 
 Preserve original JSON formaƫng 
Input Format 
 Line 1: An integer n (number of JSON records) 
 Lines 2 to n+1: Each line contains a ﬂat JSON object 
 Line n+2: Filter expression in format: ﬁeld1 operator1 value1 AND ﬁeld2 operator2 value2 
Record Fields 
 n: Total number of JSON records 
 JSON objects: Flat structure with string keys and string/numeric values 
 Filter expression: Two condiƟons connected by AND (space-AND-space) 
Constraints 
 1 ≤ n ≤ 5,000 
 JSON objects are ﬂat (no nested objects or arrays) 
 All ﬁelds referenced in ﬁlter exist in all records 
 String values in JSON: enclosed in double quotes 
 Numeric values in JSON: integers or decimals without quotes 
 Filter expression always has exactly two condiƟons joined by AND 
Comparison Operators 
Numeric Operators (for numeric ﬁelds) 

 =: Equal to 
 !=: Not equal to 
 >: Greater than 
 >=: Greater than or equal to 
 <: Less than 
 <=: Less than or equal to 
String Operators (for string ﬁelds) 
 =: Equal to (case-sensiƟve) 
 !=: Not equal to (case-sensiƟve) 
 Note: >, >=, <, <= are only for numeric comparisons 
Output Format 
 One JSON object per line for each matching record 
 Preserve original JSON formaƫng 
 Output in order of appearance in input 
 No output if no records match 
Examples 
Example 1: Numeric and String CondiƟons 
Input: 
3 
{"name":"Ana","score":80} 
{"name":"Ben","score":60} 
{"name":"Cia","score":90} 
score >= 80 AND name != Ana 
Output: 
{"name":"Cia","score":90} 
ExplanaƟon: 
 Filter: score >= 80 AND name != Ana 
 Record 1: {"name":"Ana","score":80} 
 score >= 80? 80 >= 80 → true 
 name != Ana? "Ana" != "Ana" → false 
 Result: false (both must be true) 

 Record 2: {"name":"Ben","score":60} 
 score >= 80? 60 >= 80 → false 
 Result: false 
 Record 3: {"name":"Cia","score":90} 
 score >= 80? 90 >= 80 → true 
 name != Ana? "Cia" != "Ana" → true 
 Result: true ✓ 
Example 2: Both Numeric CondiƟons 
Input: 
4 
{"id":1,"age":25,"salary":50000} 
{"id":2,"age":30,"salary":60000} 
{"id":3,"age":35,"salary":55000} 
{"id":4,"age":28,"salary":65000} 
age > 25 AND salary >= 60000 
Output: 
{"id":2,"age":30,"salary":60000} 
{"id":4,"age":28,"salary":65000} 
ExplanaƟon: 
 Filter: age > 25 AND salary >= 60000 
 Record 1: age 25 > 25? false → doesn't match 
 Record 2: age 30 > 25? true, salary 60000 >= 60000? true → match ✓ 
 Record 3: age 35 > 25? true, salary 55000 >= 60000? false → doesn't match 
 Record 4: age 28 > 25? true, salary 65000 >= 60000? true → match ✓ 
 