def isBalanced(root):
    """ returns true if the tree is balanced, i.e. the depths of the children vary by no more than one """
    heights = set()
    getHeights(root, 0, heights)
    return not heights or (max(heights) - min(heights) <= 1)

def getHeights(node, h, heights):
    """ add the height of this node's children to heights """
    if node is None:
        return
    if len(node.children) == 0:
        heights.add(h)
        return
    for n in node.children:
        getHeights(n, h+1, heights)
    return

def runTest(root, expected):
    """ print whether expected matches whether the given tree is balanced """
    bal = isBalanced(root)
    if bal != expected:
        print('Expected ' + str(expected) + ' found ' + str(bal) + ' for tree ' + str(root))

class Node:
    def __init__(self, children = []):
        self.children = children

    def __repr__(self):
        s = 'x [' + ','.join([str(c) for c in self.children]) + ']'
        return s

if __name__ == '__main__':
    runTest(None, True)
    runTest(Node(), True)
    runTest(Node([Node()]), True)
    runTest(Node([Node([Node()]),
                  Node()]), True)
    runTest(Node([Node([Node([Node()])]),
                  Node()]), False)
    runTest(Node([Node([Node([Node()])]),
                  Node([Node()])]), True)

