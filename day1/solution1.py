class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return None
    leftValues = serialize(root.left)
    rightValues = serialize(root.right)
    return f'{root.val},{leftValues},{rightValues}'     

def deserialize(s):
    nodes = s.split(',') # creates a list from node values

    def build_tree():
        val = nodes.pop(0)
        if val == 'None':
            return None
        node = Node(val)
        node.left = build_tree()
        node.right = build_tree()
        return node
    
    return build_tree()
        
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left', 'Test case failed!!!'
