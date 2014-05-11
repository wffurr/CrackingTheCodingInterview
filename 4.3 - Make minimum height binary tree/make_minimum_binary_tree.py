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

def runUnsortedTest(lst, expected):
    root = makeMinTree(lst)
    try:
        if root != expected:
            print('Expected ' + str(expected) + ' got ' + str(root) + ' for ' + str(lst))
    except:
        print('Expected ' + str(expected) + ' got ' + str(root) + ' for ' + str(lst))

if __name__ == '__main__':
    runUnsortedTest([], None)
    runUnsortedTest([0], Node(0))
    runUnsortedTest([1, 2, 3, 4], Node(1, left=Node(2, left=Node(4)), right=Node(3)))
    runUnsortedTest([1, 2, 3, 4, 5], Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3)))

