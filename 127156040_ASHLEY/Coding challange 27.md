Coding Challenge: Binary Tree Level Sum Calculator 
Problem Statement 
Write a program that calculates the sum of node values at each level of a binary tree. Given a binary 
tree represented in level-order traversal with null markers for missing nodes, compute and output 
the sum of all values at each non-empty level of the tree. 
Requirements 
 Parse level-order representaƟon of binary tree 
 Handle null markers for missing nodes 
 Calculate sum of values at each level 
 Output one sum per level 
 Handle negaƟve values correctly 
 Skip levels that contain only null nodes 
Input Format 
 Single line: Space-separated values represenƟng level-order traversal 
 Numeric values: tree node values (can be negaƟve, zero, or posiƟve) 
 null: marker for missing/empty nodes 
Record Fields 
 Node values: Integers (posiƟve, negaƟve, or zero) 
 null: Represents absence of a node 
Constraints 
 0 ≤ total_nodes ≤ 50,000 
 -1,000,000 ≤ node_value ≤ 1,000,000 
 Input uses null (lowercase) for empty nodes 
 Root can be null (empty tree) 
Binary Tree Structure 
 Level-order (breadth-ﬁrst) representaƟon 
 For node at index i: 
 LeŌ child at index 2*i + 1 
 Right child at index 2*i + 2 
 null indicates missing child nodes 
Output Format 
 One line per level containing the sum of all node values at that level 

 Only output levels that contain at least one non-null node 
 Levels output in order from root to leaves 
Examples 
Example 1: Complete Tree with Nulls 
Input: 
1 2 3 null 4 5 6 
Output: 
1 
5 
15 
ExplanaƟon: 
 Tree structure: 
       1          Level 0: sum = 1 
      / \ 
     2   3        Level 1: sum = 2 + 3 = 5 
      \ / \ 
      4 5 6       Level 2: sum = 4 + 5 + 6 = 15 
 Level 0: [1] → sum = 1 
 Level 1: [2, 3] → sum = 5 
 Level 2: [null, 4, 5, 6] → sum = 4 + 5 + 6 = 15 (ignore null) 
Example 2: Single Node 
Input: 
42 
Output: 
42 
ExplanaƟon: 
 Tree has only root node with value 42 
 Level 0: [42] → sum = 42 