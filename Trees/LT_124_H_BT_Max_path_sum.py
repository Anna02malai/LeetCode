# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):

            if not node:
                return 0
            
            leftmax = dfs(node.left)
            rightmax = dfs(node.right)
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)

            # Result with split
            res[0] = max(res[0], res[0] + leftmax + rightmax)
            # Result without split
            return node.val + max(leftmax, rightmax)
        
        dfs(root)
        return res[0]

def main():
    root = [-15,10,20,None,None,15,5,-5]
    res = Solution()
    print(res.maxPathSum(root))

if __name__ == "__main__":
    main()