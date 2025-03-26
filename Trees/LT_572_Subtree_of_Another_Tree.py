# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s, t = root, subRoot
        if not t: return True
        if not s: return False

        if self.isSametree(s, t):
            return True
        
        else:
            return(self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
    
    def isSametree(self, s, t):
        if not s and not t:
            return True
        elif s and t and s.val == t.val:
            return (self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right))
        else:
            return False

def main():
    root = [1,2,3,4,5]
    subRoot = [2,4,5]
    res = Solution()
    print(res.isSubtree(root, subRoot))

if __name__ == "__main__":
    main()