from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        
        res = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)   # append cả null
                queue.append(node.right)  # để serialize đúng shape
        
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return None
        
        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        queue = deque([root])
        i = 1
        
        while queue:
            node = queue.popleft()
            
            if tokens[i] != "N":
                node.left = TreeNode(int(tokens[i]))
                queue.append(node.left)
            i += 1
            
            if tokens[i] != "N":
                node.right = TreeNode(int(tokens[i]))
                queue.append(node.right)
            i += 1
        
        return root