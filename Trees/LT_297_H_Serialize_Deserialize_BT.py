# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        res = data.split(",")
        self.i = 0

        def dfs():
            if res[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(res[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            return node        
        return dfs()        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

def main():
    root = [1,2,3,None,None,4,5]
    res = Codec()
    print(Codec.serialize(root))

if __name__ == "__main__":
    main()