class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root is None:
            return -1  # Height of an empty tree is -1
        else:
            # Recursively calculate the height of the left and right subtrees
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)
            
            # Return the maximum height between left and right subtrees, plus 1 for the current node
            return max(left_height, right_height) + 1


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
