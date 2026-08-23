Coding Challenge 
Write a program that analyzes timestamped events and produces an aggregated report 
showing the count of each event type per date. The input contains ISO 8601 timestamps 
with event types, and the output must be sorted by date and event type. 
Requirements 
1. Parse ISO 8601 timestamps in format: YYYY-MM-DDTHH:MM:SS 
2. Extract the date portion (YYYY-MM-DD) 
3. Group events by date and event type 
4. Count occurrences of each (date, event) pair 
5. Sort output by: 
• Primary: Date (ascending - earliest first) 
• Secondary: Event type (alphabetically ascending) 
6. Output format: date,event,count 
 
ISO 8601 Timestamp Format 
Format Structure 
YYYY-MM-DDTHH:MM:SS 
 
Where: 
- YYYY = 4-digit year 
- MM = 2-digit month (01-12) 
- DD = 2-digit day (01-31) 
- T = literal separator 
- HH = 2-digit hour (00-23) 
- MM = 2-digit minute (00-59) 
- SS = 2-digit second (00-59) 
Examples 
• 2026-08-20T10:00:00 → Date: 2026-08-20, Time: 10:00:00 
• 2026-12-31T23:59:59 → Date: 2026-12-31, Time: 23:59:59 

• 2024-01-01T00:00:00 → Date: 2024-01-01, Time: 00:00:00 
Date Extraction 
From timestamp 2026-08-20T10:00:00, extract date 2026-08-20 (characters before 'T') 
 
Input Format 
• Line 1: Integer n (number of events) 
• Lines 2 to n+1: Records in format: timestamp,event 
Record Fields 
• timestamp: ISO 8601 format YYYY-MM-DDTHH:MM:SS 
• event: Event type name (alphanumeric string, no spaces) 
 
Output Format 
For each unique (date, event) combination: 
date,event,count 
• date: In format YYYY-MM-DD 
• event: Event type name (as given in input) 
• count: Number of occurrences 
Sorting Rules 
1. Primary: Date ascending (chronological order) 
2. Secondary: Event type alphabetically ascending (for same date) 
 
Examples 
Example 1: Multiple Events Per Day 
Input: 
4 
2026-08-20T10:00:00,login 
2026-08-20T12:00:00,view 
2026-08-20T13:00:00,login 

2026-08-21T09:00:00,login 
 
Output: 
2026-08-20,login,2 
2026-08-20,view,1 
2026-08-21,login,1 
Explanation: 
• 2026-08-20: 
• login events: 2 (at 10:00:00 and 13:00:00) 
• view events: 1 (at 12:00:00) 
• Alphabetically: login before view 
• 2026-08-21: 
• login events: 1 (at 09:00:00) 
 
Example 2: Unsorted Input 
Input: 
5 
2026-08-22T10:00:00,click 
2026-08-20T08:00:00,login 
2026-08-21T15:00:00,view 
2026-08-20T09:00:00,login 
2026-08-21T16:00:00,click 
 
Output: 
2026-08-20,login,2 
2026-08-21,click,1 
2026-08-21,view,1 
2026-08-22,click,1 

Explanation: 
• Input dates are out of order 
• Output sorted by date: 08-20, 08-21, 08-22 
• Within 08-21: click before view (alphabetically) 
 
Constraints 
• 1 ≤ n ≤ 100,000 
• Timestamps are in ISO 8601 local time (no timezone) 
• Event names: alphanumeric characters, underscores, hyphens allowed 
• Dates can span multiple years 