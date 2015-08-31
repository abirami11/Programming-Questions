
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

def bfsofbst(node):
    n = [node]
    next_list = [[node.key]]
    while n:
        next = []
        for e in n:
            if e.left and e.right:
                next.extend([e.left,e.right])
                next_list.append([e.left.key,e.right.key])
            elif e.left:
                next.append(e.left)
                next_list.append([e.left.key])
            elif e.right:
                next.append(e.right)
                next_list.append([e.right.key])
        n= next

    for e in next_list:
            print e
        #print "\n"
nodes = TreeNode(10)
nodes.insert(12)
nodes.insert(8)
nodes.insert(6)
nodes.insert(14)
nodes.insert(9)
bfsofbst(nodes)
#nodes.display_tree()
