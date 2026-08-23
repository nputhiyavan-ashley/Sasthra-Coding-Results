Coding Challenge: LRU Cache ImplementaƟon 
Problem Statement 
Write a program that implements a Least Recently Used (LRU) cache with ﬁxed capacity. The cache 
supports two operaƟons: GET (retrieve value by key) and PUT (insert or update key-value pair). When 
the cache reaches capacity, the least recently used item is evicted to make room for new entries. 
Both GET and PUT operaƟons update the recency of accessed keys. 
Requirements 
 Implement LRU cache with ﬁxed capacity 
 Support GET operaƟon: return value if key exists, otherwise -1 
 Support PUT operaƟon: insert or update key-value pair 
 Evict least recently used item when at capacity 
 Both GET and PUT mark key as most recently used 
 Handle capacity of 1 correctly 
 Handle updaƟng exisƟng keys without evicƟon 
Input Format 
 Line 1: Two space-separated integers capacity and q 
 capacity = maximum number of key-value pairs in cache 
 q = number of operaƟons to perform 
 Lines 2 to q+1: Commands in one of two formats: 
 GET key - retrieve value for key 
 PUT key value - insert or update key with value 
Record Fields 
 capacity: Maximum cache size 
 q: Total number of operaƟons 
 key: Integer key idenƟﬁer 
 value: Integer value associated with key 
Constraints 
 1 ≤ capacity ≤ 1,000 
 1 ≤ q ≤ 10,000 
 1 ≤ key ≤ 1,000,000 
 1 ≤ value ≤ 1,000,000 
 Keys and values are posiƟve integers 

LRU Cache Behavior 
1. GET key: 
 If key exists: return value and mark key as most recently used 
 If key doesn't exist: return -1 
2. PUT key value: 
 If key exists: update value and mark as most recently used 
 If key doesn't exist and cache not full: insert and mark as most recently used 
 If key doesn't exist and cache at capacity: evict least recently used, then insert new 
key 
Output Format 
 One line per GET operaƟon containing the returned value 
 PUT operaƟons produce no output 
 Output -1 for GET on non-existent key 
Examples 
Example 1: Basic LRU OperaƟons 
Input: 
2 6 
PUT 1 10 
PUT 2 20 
GET 1 
PUT 3 30 
GET 2 
GET 3 
Output: 
10 
-1 
30 
ExplanaƟon: 
 Cache capacity: 2 
 OperaƟon 1: PUT 1 10 → Cache: {1:10} 
 OperaƟon 2: PUT 2 20 → Cache: {1:10, 2:20} 

 OperaƟon 3: GET 1 → Returns 10, Cache: {2:20, 1:10} (1 now most recent) 
 OperaƟon 4: PUT 3 30 → Capacity reached, evict LRU (key 2), Cache: {1:10, 3:30} 
 OperaƟon 5: GET 2 → Key 2 was evicted, return -1 
 OperaƟon 6: GET 3 → Returns 30 
Example 2: Update ExisƟng Key 
Input: 
2 5 
PUT 1 100 
PUT 2 200 
PUT 1 150 
GET 1 
GET 2 
Output: 
150 
200 
ExplanaƟon: 
 OperaƟon 1: PUT 1 100 → Cache: {1:100} 
 OperaƟon 2: PUT 2 200 → Cache: {1:100, 2:200} 
 OperaƟon 3: PUT 1 150 → Update exisƟng key, no evicƟon, Cache: {2:200, 1:150} (1 now 
most recent) 
 OperaƟon 4: GET 1 → Returns 150 
 OperaƟon 5: GET 2 → Returns 200 