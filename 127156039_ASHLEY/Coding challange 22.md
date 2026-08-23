Coding Challenge: Customer Data Cleaning Pipeline 
Problem Statement 
Write a program that cleans and deduplicates customer records. Given raw data with potenƟal 
quality issues, apply validaƟon rules, remove duplicates by keeping the latest valid entry per ID, and 
output cleaned records along with quality metrics showing input count, valid records, rejected 
records, and duplicates removed. 
Requirements 
 Trim leading/trailing whitespace from all ﬁelds 
 Normalize email addresses to lowercase 
 Validate records (reject if missing ID or invalid email) 
 For duplicate IDs, keep only the latest valid record 
 Output cleaned records followed by quality metrics 
 Email validaƟon: must contain exactly one @ with characters before and aŌer 
Input Format 
 Line 1: An integer n (number of records) 
 Lines 2 to n+1: Records in format: id,name,email 
Record Fields 
 id: String idenƟﬁer (cannot be empty aŌer trimming) 
 name: String name (can be empty) 
 email: Email address (must be valid format) 
Constraints 
 1 ≤ n ≤ 20,000 
 Fields may have leading/trailing spaces 
 No quoted commas in data 
 IDs are case-sensiƟve strings 
 Email validaƟon: must contain exactly one @ with at least one character before and aŌer 
ValidaƟon Rules 
1. Trim: Remove leading/trailing whitespace from all ﬁelds 
2. Email NormalizaƟon: Convert email to lowercase 
3. Reject if: 
 ID is empty (aŌer trimming) 
 Email is invalid (missing @, mulƟple @, or nothing before/aŌer @) 

4. DeduplicaƟon: For duplicate IDs, keep the last valid occurrence 
Output Format 
Part 1: Cleaned Records 
 One line per valid record: id,name,email 
 Records ordered by ﬁrst valid appearance of each ID 
 Latest valid record for each ID only 
Part 2: Quality Metrics 
input:n 
valid:count 
rejected:count 
duplicates_removed:count 
Metrics DeﬁniƟons 
 input: Total records in input (n) 
 valid: Final number of unique cleaned records output 
 rejected: Records that failed validaƟon 
 duplicates_removed: Valid records discarded due to duplicate IDs 
Examples 
Example 1: Basic Cleaning 
Input: 
4 
1, Ana ,ANA@EXAMPLE.COM 
2,Ben,invalid 
1,Ana,ana.new@example.com 
3,Cia,cia@example.com 
Output: 
1,Ana,ana.new@example.com 
3,Cia,cia@example.com 
input:4 
valid:2 
rejected:1 
duplicates_removed:1 

ExplanaƟon: 
 Record 1: 1, Ana ,ANA@EXAMPLE.COM 
 Trim: 1, Ana, ANA@EXAMPLE.COM 
 Normalize email: ana@example.com 
 Valid, ID=1 (ﬁrst occurrence) 
 Record 2: 2,Ben,invalid 
 Trim: 2, Ben, invalid 
 Email has no @ → rejected 
 Record 3: 1,Ana,ana.new@example.com 
 Trim: 1, Ana, ana.new@example.com 
 Valid, ID=1 (duplicate, replaces ﬁrst) 
 First occurrence becomes duplicate removed 
 Record 4: 3,Cia,cia@example.com 
 Valid, ID=3 
 Final: 2 valid records (IDs 1 and 3) 
 Metrics: 
 input: 4 
 valid: 2 (IDs 1 and 3) 
 rejected: 1 (record 2) 
 duplicates_removed: 1 (ﬁrst ID=1 record) 
Example 2: MulƟple Duplicates 
Input: 
6 
100,Alice,alice@test.com 
200,Bob,bob@test.com 
100,Alice Updated,alice2@test.com 
100,Alice Final,alice3@test.com 
,Carol,carol@test.com 
200,Bob New,bob.new@test.com 
Output: 
100,Alice Final,alice3@test.com 

200,Bob New,bob.new@test.com 
input:6 
valid:2 
rejected:1 
duplicates_removed:3 
ExplanaƟon: 
 Record 1: ID=100, valid (ﬁrst) 
 Record 2: ID=200, valid (ﬁrst) 
 Record 3: ID=100, valid (replaces record 1) 
 Record 4: ID=100, valid (replaces record 3) 
 Record 5: Empty ID → rejected 
 Record 6: ID=200, valid (replaces record 2) 
 Final: 2 valid records 
 Duplicates removed: 3 (ﬁrst ID=100, second ID=100, ﬁrst ID=200) 