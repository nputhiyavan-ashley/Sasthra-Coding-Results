Coding Challenge 
Write a program that takes a nested JSON object and flattens it into a single-level object 
with dot-separated keys. Arrays should be preserved as values (not flattened), and the 
output keys must be sorted lexicographically. 
Requirements 
1. Flatten nested JSON objects using dot notation for keys 
2. Preserve arrays as values (do not flatten array contents) 
3. Sort output keys lexicographically (alphabetically) 
4. Handle null values, empty objects, and nested structures 
5. Maximum nesting depth: 20 levels 
6. Input keys are guaranteed to not contain dots 
 
Flattening Rules 
Nested Objects 
Input:  {"user": {"name": "Ana"}} 
Output: {"user.name": "Ana"} 
Multiple Levels 
Input:  {"a": {"b": {"c": "value"}}} 
Output: {"a.b.c": "value"} 
Arrays (Preserve as Values) 
Input:  {"items": [1, 2, 3]} 
Output: {"items": [1, 2, 3]} 
Mixed Types 
Input:  {"name": "Ana" , "age": 25, "active": true, "data": null} 
Output: {"active": true, "age": 25, "data": null, "name": "Ana"} 
Empty Objects 
Input:  {"user": {}} 
Output: {} (empty object removed) 
 

Input Format 
• Single line: Valid JSON object 
• JSON can contain: 
• Objects (nested) 
• Arrays (preserved as values) 
• Strings 
• Numbers 
• Booleans (true/false) 
• null 
 
Output Format 
• Single line: Flattened JSON object 
• Keys sorted lexicographically (alphabetical order) 
• Compact format (no extra whitespace) 
• Arrays preserved as values 
 
Examples 
Example 1: Basic Nesting 
Input: 
{"user":{"name":"Ana"}, "active":true} 
 
Output: 
{"active":true, "user.name":"Ana"} 
Explanation: 
• user.name flattened from nested object 
• active remains at root level 
• Sorted alphabetically: "active" before "user.name" 
 

Example 2: Multiple Levels 
Input: 
{"a":{"b":{"c":"value"}}} 
 
Output: 
{"a.b.c":"value"} 
Explanation: 
• Three levels deep: a → b → c 
• Flattened to single key with dots 
 
Constraints 
• Maximum nesting depth: 20 levels 
• Keys do not contain dots (guaranteed) 
• Valid JSON format (properly formatted) 
 