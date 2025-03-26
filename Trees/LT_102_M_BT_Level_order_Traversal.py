from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        q = deque()
        res = []
        q.append(root)

        while q:
            qLen = len(q)
            lvl = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if lvl: res.append(lvl)        
        return res

def main():
    root = [1,2,3,4,5,6,7]
    res = Solution()
    print(res.levelOrder(root))

if __name__ == "__main__":
    main()