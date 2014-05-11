# Why is the input list sorted?  It doesn't matter that it's sorted unless
# we're making a BST.  I'll do it both ways just in case.

def makeMinTree(lst):
    """ returns a minimum-height binary tree populated from the list, root is lst[0] """
    if len(lst) == 0:
        return None
    root = Node(lst[0])
    needs_children = [root]
    for i in xrange(1, len(lst), 2):
        n = needs_children[0]
        needs_children = needs_children[1:]
        n.left = Node(lst[i])
        if i+1 == len(lst):
            break
        n.right = Node(lst[i+1])
        needs_children.append(n.left)
        needs_children.append(n.right)
    return root

def makeMinBST(lst):
    """ Returns a minimum height BST, root is the median of lst ie lst[len(lst)]/2 """
    if len(lst) == 0:
        return None
    root = Node(lst[len(lst)/2])
    smaller_lst = lst[0:len(lst)/2]
    larger_lst  = lst[len(lst)/2+1:]
    root.left = makeMinBST(smaller_lst)
    root.right = makeMinBST(larger_lst)
    return root

def bstAdd(root, val):
    """ Adds val to the right place in BST root """
    which = 'right' if val > root.val else 'left'
    if getattr(root, which) is None:
        setattr(root, which, Node(val))
    else:
        bstAdd(getattr(root, which), val)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        s = 'Node(' + str(self.val) + ', left:' + str(self.left) + ', right:' + str(self.right) + ')'
        return s

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right
    
    def __ne__(self, other):
        return not self.__eq__(other)

def compare(lst, root, expected):
    try:
        if root != expected:
            print('Expected ' + str(expected) + ' got ' + str(root) + ' for ' + str(lst))
    except:
        print('Expected ' + str(expected) + ' got ' + str(root) + ' for ' + str(lst))

if __name__ == '__main__':
    compare([], makeMinTree([]), None)
    compare([0], makeMinTree([0]), Node(0))
    compare([1, 2, 3, 4], makeMinTree([1, 2, 3, 4]), Node(1, left=Node(2, left=Node(4)), right=Node(3)))
    compare([1, 2, 3, 4, 5], makeMinTree([1, 2, 3, 4, 5]), Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3)))
    compare([], makeMinBST([]), None)
    compare([0], makeMinBST([0]), Node(0))
    compare([1, 2, 3, 4], makeMinBST([1, 2, 3, 4]),
            Node(3, left=Node(2, left=Node(1)),
                   right=Node(4)))
    compare([1, 2, 3, 4, 5], makeMinBST([1, 2, 3, 4, 5]),
            Node(3, left=Node(2, left=Node(1)),
                   right=Node(5, left=Node(4))))
    compare([1, 2, 3, 4, 5, 6, 7], makeMinBST([1, 2, 3, 4, 5, 6, 7]),
            Node(4, left=Node(2, left=Node(1), right=Node(3)),
                   right=Node(6, left=Node(5), right=Node(7))))

