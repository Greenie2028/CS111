from functools import reduce
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self,value):
        self.children.append(value)
    

root = TreeNode(0)
c1 = TreeNode(100)
c2 = TreeNode(200)
c3 = TreeNode(300)
c4 = TreeNode(5000)
c5 = TreeNode(15)
c6 = TreeNode(160)

root.add_child(c1)
root.add_child(c2)
root.add_child(c3)
c3.add_child(c4)
c1.add_child(c5)
c1.add_child(c6)

def count(node, cond):
    c = 0
    if cond(node): c += 1
    for child in node.children: c += count(child,cond)
    return c

def gt_one_fifty(node):
    count = 0
    if node.value > 150: count += 1
    if node.children != []:
        for child in node.children: count += gt_one_fifty(child)
    return count

def gt_150(node): return reduce(lambda current, child: current+gt_150(child), node.children, 0) + (1 if node.value>150 else 0)

def eq_200(node): return reduce(lambda current, child: current+eq_200(child), node.children,0) + (1 if node.value==200 else 0)

print(count(root, lambda node: node.value == 200)) # Counts how many nodes have a value of exactly 200

print(f"Number of nodes that have at least one child: {str(count(root, lambda node: node.children != []))}")

print(f"Number of nodes: {count(root, lambda *_: True)}")