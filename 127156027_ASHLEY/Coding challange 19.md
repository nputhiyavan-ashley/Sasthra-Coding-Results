Coding Challenge: Employee Records MulƟ-Key Sort 
Problem Statement 
Write a program that sorts employee records containing name, department, and performance score. 
Records must be sorted using three criteria in order of priority: department (alphabeƟcally 
ascending), score (numerically descending), and name (alphabeƟcally ascending). 
Requirements 
 Parse employee records with comma-separated ﬁelds 
 Sort records by mulƟple keys with speciﬁc ordering 
 Primary sort: Department (ascending - alphabeƟcally A to Z) 
 Secondary sort: Score (descending - highest score ﬁrst) 
 TerƟary sort: Name (ascending - alphabeƟcally A to Z) 
 Handle decimal scores correctly 
 Preserve original record format in output 
Input Format 
 Line 1: An integer n (number of records) 
 Lines 2 to n+1: Records in format: name,department,score 
Record Fields 
 name: String, employee name (no spaces or commas) 
 department: String, department name (no spaces or commas) 
 score: Number (can be integer or decimal) 
Constraints 
 1 ≤ n ≤ 100,000 
 Names and departments: alphanumeric characters only 
 Scores: posiƟve numbers (integers or decimals) 
 Score range: 0 ≤ score ≤ 100 
Output Format 
 n lines, each containing one record in format: name,department,score 
 Sorted by: 
 Department ascending (alphabeƟcal) 
 Score descending (within same department) 
 Name ascending (for Ɵes in department and score) 
 Preserve original score format (integer or decimal as given) 

Examples 
Example 1: MulƟ-Department SorƟng 
Input: 
4 
Ana,AI,80 
Ben,CSE,90 
Cia,AI,90 
Dan,AI,90 
Output: 
Cia,AI,90 
Dan,AI,90 
Ana,AI,80 
Ben,CSE,90 
ExplanaƟon: 
 SorƟng steps: 
1. Group by department (ascending): 
 AI: [Ana,AI,80], [Cia,AI,90], [Dan,AI,90] 
 CSE: [Ben,CSE,90] 
2. Within AI, sort by score (descending): 
 Score 90: [Cia,AI,90], [Dan,AI,90] 
 Score 80: [Ana,AI,80] 
3. Within AI score 90, sort by name (ascending): 
 Cia comes before Dan alphabeƟcally 
 Final order: Cia (AI,90), Dan (AI,90), Ana (AI,80), Ben (CSE,90) 
Example 2: Decimal Scores 
Input: 
6 
Alice,HR,85.5 
Bob,HR,85.5 
Carol,IT,92.3 
Dave,IT,88.7 

Eve,HR,90.0 
Frank,IT,92.3 
Output: 
Eve,HR,90.0 
Alice,HR,85.5 
Bob,HR,85.5 
Carol,IT,92.3 
Frank,IT,92.3 
Dave,IT,88.7 
ExplanaƟon: 
 Department HR (ascending comes before IT): 
 Eve,HR,90.0 (highest score in HR) 
 Alice,HR,85.5 and Bob,HR,85.5 (Ɵed score, alphabeƟcally Alice < Bob) 
 Department IT: 
 Carol,IT,92.3 and Frank,IT,92.3 (Ɵed score, alphabeƟcally Carol < Frank) 
 Dave,IT,88.7 (lowest score in IT) 
 