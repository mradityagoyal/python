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

def levelOrder(root):
    """

    :param root: The root of the three.
    :return: a list of lists.. which are the levels
    """

    def next(currentLevel):
        """
        Returns the next level of the tree.
        :param currentLevel: list of TreeNodes.
        :return: next level
        """
        result = []
        for node in currentLevel:
            if node.left is not None: result.append(node.left)
            if node.right is not None: result.append(node.right)
        return result

    result = []
    level = [root]
    result.append([node.val for node in level])
    done = False
    while not done:
        level = next(level)
        if len(level) > 0 : result.append([node.val for node in level])
        else: done = True


    return result

def columnOrder(root):
    """
    print out the columns in a BST
    :param root:
    :return:
    """
    cols = {} # dict to column id to list of vals.
    cols[0]= [root.val]
    level = [(root,0)]


    def nextLevel(lvl):
        result = []
        for node, colId in lvl:
            if node.left is not None: result.append((node.left, colId -1))
            if node.right is not None: result.append((node.right, colId +1))
        return result

    done = False
    while not done:
        level = nextLevel(level)
        if len(level)>0:
            for node , colId in level: cols[colId]= cols.get(colId, [])+ [node.val]
        else: done = True
    return cols


# startup.
root = TreeNode(5)
print(levelOrder(root))
print(inOrder(root))
root.insert(4)
print(levelOrder(root))
print(inOrder(root))
print(inOrderRecursive(root))
root.insert(17)
print(levelOrder(root))
root.insert(2)
print(levelOrder(root))
root.insert(6)
print(levelOrder(root))
print(inOrderRecursive(root))
print(inOrder(root))
print(levelOrder(root))
print("column Order")
print(columnOrder(root))


