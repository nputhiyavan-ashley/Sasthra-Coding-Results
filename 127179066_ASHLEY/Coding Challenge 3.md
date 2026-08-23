Coding Challenge 
Write a program that processes a stream of employee records and applies 
deduplication logic to retain only the most recent valid record for each unique ID. 
Requirements 
1. Process records with format: id,name,score,updated_at 
2. Keep only the latest record (highest updated_at) for each unique id 
3. Validate scores: Only retain records with scores between 0 and 100 (inclusive) 
4. Discard records with invalid scores (below 0 or above 100) 
5. Output retained records sorted by updated_at in ascending order 
6. Maintain original CSV format in output 
 
Input Format 
• Line 1: An integer n (number of records) 
• Lines 2 to n+1: CSV records in format: id,name,score,updated_at 
Record Fields 
• id: Integer, unique identifier for a person 
• name: String, person's name (no spaces, no commas) 
• score: Integer, performance score 
• updated_at: Integer, timestamp (higher = more recent) 
 
Output Format 
• Retained records in CSV format: id,name,score,updated_at 
• Sorted by updated_at in ascending order 
• One record per line 
• If no valid records exist, output nothing 
 
Validation Rules 
Valid Record Requirements 

• Score must be: 0 ≤ score ≤ 100 
• Records with scores outside this range are invalid and must be discarded 
Deduplication Logic 
• For each unique id, keep only the record with the highest updated_at value 
• If multiple records for the same id exist: 
• Compare all valid records for that id 
• Keep the one with the maximum updated_at 
• Discard all others 
 
Examples 
Example 1: Basic Deduplication 
Input: 
5 
1,Ana,80,10 
2,Ben,120,11 
1,Ana,90,12 
3,Cia,75,13 
2,Ben,88,14 
 
Output: 
1,Ana,90,12 
3,Cia,75,13 
2,Ben,88,14 
Explanation: 
• ID 1 (Ana): 
• Record 1: score=80, updated_at=10 ✓ valid 
• Record 3: score=90, updated_at=12 ✓ valid (newer) 
• Keep: 1,Ana,90,12 

• ID 2 (Ben): 
• Record 2: score=120, updated_at=11 ✗ invalid (score > 100) 
• Record 5: score=88, updated_at=14 ✓ valid 
• Keep: 2,Ben,88,14 
• ID 3 (Cia): 
• Record 4: score=75, updated_at=13 ✓ valid 
• Keep: 3,Cia,75,13 
• Output sorted by updated_at: 12, 13, 14 
 
Example 2: All Invalid Scores for One ID 
Input: 
4 
1,John,110,5 
1,John,120,10 
2,Sara,85,8 
2,Sara,90,12 
 
Output: 
2,Sara,90,12 
Explanation: 
• ID 1 (John): Both records have invalid scores (>100), discard all 
• ID 2 (Sara): Keep latest valid: 2,Sara,90,12 
 
Constraints 
• 1 ≤ n ≤ 100,000 
• id: positive integer 
• name: alphabetic characters only (no spaces or special characters) 
• score: integer (can be negative or > 100, must validate) 

• updated_at: positive integer (timestamp) 
• No quoted commas in the input (simple CSV parsing) 
 