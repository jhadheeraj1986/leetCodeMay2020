'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
'''

mapTemp = dict()
class Solution:
    
    def findElement(self, root: TreeNode, z: int, level:int):
        if root is None:
            return
        else:
            if (z == root.val) or(root.left and z == root.left.val) or (root.right and z == root.right.val):
                mapTemp[z] = [level, root.val]
                return
            self.findElement(root.left, z, level+1)
            self.findElement(root.right, z,level+1)


    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
            self.findElement(root,x, 1)
            self.findElement(root, y, 1)
            print(mapTemp[x]," ", mapTemp[y])
            if (mapTemp[x][0] == mapTemp[y][0]) and (mapTemp[x][1] != mapTemp[y][1]):
                return True
            else:
                return False


