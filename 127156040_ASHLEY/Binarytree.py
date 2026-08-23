import sys
from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def build(tokens):
    if not tokens or tokens[0]=="null":
        return None
    root=TreeNode(int(tokens[0]))
    queue=deque([root])
    i=1
    while queue and i < len(tokens):
        curr=queue.popleft()
        if i<len(tokens):
            if tokens[i]!="null":
                curr.left=TreeNode(int(tokens[i]))
                queue.append(curr.left)
            i+=1

        if i<len(tokens):
            if tokens[i]!="null":
                curr.right=TreeNode(int(tokens[i]))
                queue.append(curr.right)
            i+=1
    return root
def level_sums(root):
    if not root:
        return
    queue=deque([root])
    while queue:
        level_size=len(queue)
        level_sum=0
        for _ in range(level_size):
            node=queue.popleft()
            level_sum+=node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(level_sum)

def main():
    input=sys.stdin.read().split()
    if input:
        root=build(input)
        level_sums(root)
if __name__=="__main__": 
    main()
    