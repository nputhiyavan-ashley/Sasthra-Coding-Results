Description:

This Python program reads events with timestamps and counts how many times each event occurs on each date.

The output is displayed in the following format: date,event,count

Input Format:
The first line contains the number of events.
Each following line contains:
timestamp,event_name

Example:
4
2026-08-20T10:30:00,login
2026-08-20T12:00:00,login
2026-08-20T14:00:00,logout
2026-08-21T09:00:00,login

Output
2026-08-20,login,2
2026-08-20,logout,1
2026-08-21,login,1

How It Works : The program extracts the date from each timestamp and combines the date and event name as a unique key.
