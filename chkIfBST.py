class TreeNode:
    def __init__(self, key, left=None,right=None,parent = None):
        self.left = left
        self.right = right
        self.key = key

    def insert(self,data):
        if self.key:
            if data < self.key:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = TreeNode(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = TreeNode(data)
        else:
            self.key = TreeNode(data)
    def display_tree(self):
        if self.key:
            print self.key
            if self.left:
                self.left.display_tree()
            if self.right:
                self.right.display_tree()
        else:
            return None
def chkIfBST(tree): #Wrong Since it does not check max and min property of BST
    if tree.key:
        if tree.left:
            if tree.key < tree.left.key:
                return -1
            else:
                return chkIfBST(tree.left)
        if tree.right:
            if tree.key > tree.right.key:
                return -1
            else:
                return chkIfBST(tree.right)
        return 0
    return True

def chkBST(tree, min, max):
    if tree == None:
        return True
    if ((min!=None and tree.key <= min) or (max!=None and tree.key >= max)):
        return False
    if ((chkBST(tree.left,min,tree.key) == False) or (chkBST(tree.right, tree.key, max))== False):
        return False
    return True


nodes = TreeNode(10)
nodes.insert(12)
nodes.insert(8)
nodes.insert(6)
nodes.insert(14)
nodes.insert(9)
root = TreeNode(10)
root.right = TreeNode(20)
root.left = TreeNode(5)
root.left.left = TreeNode(7)
root.display_tree()
print chkBST(nodes,None, None)
print chkBST(root,None,None)
