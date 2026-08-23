Coding Challenge: Minimum MeeƟng Rooms 
Problem Statement 
Write a program that determines the minimum number of meeƟng rooms required to schedule all 
meeƟngs without conﬂicts. Given a list of meeƟng intervals with start and end Ɵmes, calculate the 
minimum number of rooms needed such that no two meeƟngs in the same room overlap. Note that 
a meeƟng ending at Ɵme t does not conﬂict with a meeƟng starƟng at Ɵme t (they can use the same 
room). 
Requirements 
 Calculate minimum rooms needed for all meeƟngs 
 MeeƟngs ending at Ɵme t do not overlap meeƟngs starƟng at Ɵme t 
 Handle meeƟngs that touch at boundaries (end Ɵme = start Ɵme) 
 OpƟmize for minimum room count 
 All meeƟngs must be scheduled 
Input Format 
 Line 1: An integer n (number of meeƟngs) 
 Lines 2 to n+1: Each line contains two space-separated integers start end 
 start: MeeƟng start Ɵme 
 end: MeeƟng end Ɵme 
Record Fields 
 n: Total number of meeƟngs 
 start: MeeƟng start Ɵme (inclusive) 
 end: MeeƟng end Ɵme (exclusive - room becomes available at this Ɵme) 
Constraints 
 1 ≤ n ≤ 100,000 
 0 ≤ start < end ≤ 1,000,000 
 Time values are integers 
 MeeƟng ending at Ɵme t does NOT overlap with meeƟng starƟng at Ɵme t 
Output Format 
 Single integer represenƟng the minimum number of rooms required 
Examples 
Example 1: Basic Case with Touching MeeƟngs 
Input: 

4 
0 30 
5 10 
15 20 
20 25 
Output: 
2 
ExplanaƟon: 
 MeeƟngs: 
 MeeƟng 1: [0, 30) 
 MeeƟng 2: [5, 10) 
 MeeƟng 3: [15, 20) 
 MeeƟng 4: [20, 25) 
 Timeline analysis: 
 Time 0-5: MeeƟng 1 only (1 room) 
 Time 5-10: MeeƟngs 1 and 2 overlap (2 rooms) 
 Time 10-15: MeeƟng 1 only (1 room) 
 Time 15-20: MeeƟngs 1 and 3 overlap (2 rooms) 
 Time 20-25: MeeƟngs 1 and 4 overlap (2 rooms) 
 Time 25-30: MeeƟng 1 only (1 room) 
 Note: MeeƟng 3 ends at 20, MeeƟng 4 starts at 20 → no overlap 
 Maximum simultaneous meeƟngs: 2 
 Minimum rooms: 2 
Example 2: All MeeƟngs Overlap 
Input: 
3 
0 10 
5 15 
10 20 
Output: 
2 

ExplanaƟon: 
 MeeƟngs: 
 MeeƟng 1: [0, 10) 
 MeeƟng 2: [5, 15) 
 MeeƟng 3: [10, 20) 
 Timeline: 
 Time 0-5: MeeƟng 1 (1 room) 
 Time 5-10: MeeƟngs 1 and 2 overlap (2 rooms) 
 Time 10-15: MeeƟng 2 only (1 room) - MeeƟng 1 ends at 10, MeeƟng 3 starts at 10 
 Time 15-20: MeeƟng 3 only (1 room) 
 Maximum simultaneous: 2 (during Ɵme 5-10) 
 Minimum rooms: 2 
 