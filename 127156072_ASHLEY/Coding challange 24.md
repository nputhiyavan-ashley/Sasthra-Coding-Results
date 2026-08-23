Coding Challenge: Graph Connected Components Analysis 
Problem Statement 
Write a program that analyzes the connected components of an undirected graph. Given a graph 
represented by its nodes and edges, determine how many separate connected components exist and 
the size of each component. Output the total count of components followed by the size of each 
component in descending order. 
Requirements 
 Build an undirected graph from edge list 
 IdenƟfy all connected components 
 Count total number of components 
 Calculate size (node count) of each component 
 Sort component sizes in descending order (largest ﬁrst) 
 Handle isolated nodes (nodes with no edges) 
 Handle self-loops correctly 
Input Format 
 Line 1: Two space-separated integers n and m 
 n = number of nodes (numbered 1 to n) 
 m = number of edges 
 Lines 2 to m+1: Each line contains two space-separated integers u and v 
 Represents an undirected edge between node u and node v 
Record Fields 
 n: Total nodes in graph (1 to n) 
 m: Total edges in graph 
 u, v: Node idenƟﬁers for edge endpoints 
Constraints 
 1 ≤ n ≤ 50,000 
 0 ≤ m ≤ 50,000 
 1 ≤ u, v ≤ n 
 Graph is undirected (edge u-v implies edge v-u) 
 MulƟple edges between same nodes possible 
 Self-loops possible (u = v) 
Output Format 

 Line 1: Single integer represenƟng total number of connected components 
 Line 2: Space-separated integers represenƟng size of each component, sorted in descending 
order 
Examples 
Example 1: MulƟple Components 
Input: 
6 3 
1 2 
2 3 
4 5 
Output: 
3 
3 2 1 
ExplanaƟon: 
 Graph structure: 
 1 --- 2 --- 3 
  
 4 --- 5 
  
 6 (isolated) 
 Connected components: 
 Component 1: {1, 2, 3} → size 3 
 Component 2: {4, 5} → size 2 
 Component 3: {6} → size 1 
 Total components: 3 
 Sizes descending: 3, 2, 1 
Example 2: Single Large Component 
Input: 
5 4 
1 2 
2 3 

3 4 
4 5 
Output: 
1 
5 
ExplanaƟon: 
 Graph structure: 
 1 --- 2 --- 3 --- 4 --- 5 
 Connected components: 
 Component 1: {1, 2, 3, 4, 5} → size 5 
 Total components: 1 
 Sizes: 5 