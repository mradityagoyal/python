class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, x):
        if(x < self.val):
            if(self.left == None): self.left = TreeNode(x)
            else: self.left.insert(x)
        else:
            if(self.right == None): self.right = TreeNode(x)
            else: self.right.insert(x)


def inOrder(root):
    """

    :param root: a TreeNode.
    :return: a list of ints inorder traversal
    """
    current = root
    done = 0
    stack = []
    sorted = []
    while not done :
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            if(len(stack)>0):
                current = stack.pop()
                sorted.append(current.val)
                current=current.right
            else:
                done = 1
    return sorted

def inOrdRecursive(root, acc):
    if root:
        inOrdRecursive(root.left, acc)
        acc.append(root.val)
        inOrdRecursive(root.right, acc)
    return acc

def inOrderRecursive(root):
    return inOrdRecursive(root, [])

# startup.
root = TreeNode(5)
print(inOrder(root))
root.insert(4)
print(inOrder(root))
print(inOrderRecursive(root))
