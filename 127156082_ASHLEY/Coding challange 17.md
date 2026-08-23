Coding Challenge: Shortest Path in Undirected Graph 
Problem Statement 
Write a program that ﬁnds the shortest path between two nodes in an undirected graph. Given a 
graph represented by its edges, determine the minimum number of edges needed to travel from a 
source node to a desƟnaƟon node. If the desƟnaƟon is unreachable from the source, return -1. 
Requirements 
 Build an undirected graph from edge list 
 Find shortest path from source to desƟnaƟon 
 Count minimum number of edges in the path 
 Return -1 if no path exists 
 Handle duplicate edges correctly 
Input Format 
 Line 1: Two space-separated integers n and m 
 n = number of nodes (numbered 1 to n) 
 m = number of edges 
 Lines 2 to m+1: Each line contains two space-separated integers u and v 
 Represents an undirected edge between node u and node v 
 Line m+2: Two space-separated integers source and desƟnaƟon 
 source = starƟng node 
 desƟnaƟon = target node 
Record Fields 
 n: Total nodes in graph (1 to n) 
 m: Total edges in graph 
 u, v: Node idenƟﬁers for edge endpoints 
 source, desƟnaƟon: Start and end nodes for path query 
Constraints 
 1 ≤ n ≤ 50,000 
 0 ≤ m ≤ 50,000 
 1 ≤ u, v, source, desƟnaƟon ≤ n 
 Graph is undirected (edge u-v implies edge v-u) 
 MulƟple edges between same nodes possible 
 Self-loops possible 

Output Format 
 Single integer represenƟng: 
 Minimum number of edges from source to desƟnaƟon 
 -1 if desƟnaƟon unreachable from source 
Examples 
Example 1: Connected Path 
Input: 
5 4 
1 2 
2 3 
1 4 
4 5 
1 5 
Output: 
2 
ExplanaƟon: 
 Graph structure: 
 1 --- 2 --- 3 
 | 
 4 --- 5 
 Paths from node 1 to node 5: 
 Path 1: 1 → 4 → 5 (2 edges) 
 This is the shortest path 
 Minimum edges: 2 
Example 2: Disconnected Graph 
Input: 
6 3 
1 2 
2 3 
4 5 
1 4 

Output: 
-1 
ExplanaƟon: 
 Graph structure: 
 1 --- 2 --- 3 
  
 4 --- 5         6 (isolated) 
 Node 1 and node 4 are in diﬀerent connected components 
 No path exists from node 1 to node 4 
 Return: -1 
 