import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


    def levelOrder(self,root):
            #Write your code here
        queue = [root] if root else []
        
        while queue:
            node = queue.pop()
            print(node.data, end=" ")

            if node.left: queue.insert(0,node.left)
            if node.right: queue.insert(0,node.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
  data=int(input())
  root=myTree.insert(root,data)
myTree.levelOrder(root)


#+++++++++++++++++++Compare with this++++++++++++++++

class Solution:
    def insert(self, root, data):
        if not root:
            return Node(data)
        else:
            if data <= root.data:
                current = self.insert(root.left, data)
                root.left = current
            else:
                current = self.insert(root.right, data)
                root.right = current
        return root

    def level_order_traverse(self, root):
        #Write your code here
        if root:
            queue = [root]
            while queue:
                node = queue.pop()
                print(node.data)
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
