# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

def main():
    root = [5,3,8,1,4,7,9,null,2]
    p = 3
    q = 8
    res = Solution()
    print(res.lowestCommonAncestor(root, p, q))

if __name__ == "__main__":
    main()