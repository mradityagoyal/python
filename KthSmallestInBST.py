class KthSmallestBST(object):

    def kthSmallest(self, root, k):

        current = root
        stack = []
        sorted = []
        done = 0
        while(not done):
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if(len(stack)>0):
                    current = stack.pop()
                    if k == 1 : return current.val
                    k-=1
                    current=current.right
                else: done = 1





class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None