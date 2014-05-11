def isRoute(node, target):
    """ Returns true if there a route between the node and target """
    def isRouteHelper(node, target, visited):
        if node == target:
            return True
        visited.add(node)
        return any([isRouteHelper(n, target, visited)
                    for n in node.neighbors
                    if n not in visited])

    return isRouteHelper(node, target, set())

def runTest(node, target, expected):
    found_route = isRoute(node, target)
    if found_route != expected:
        print('Expected ' + str(expected) + ' found ' + str(found_route) + ' for graph ' + str(node))

class Node:
    def __init__(self, value, neighbors=[]):
        self.value = value
        self.neighbors = neighbors

    def __repr__(self):
        visited = set(self)
        s = self.value + ': [' + ','.join([str(n.value) for n in self.neighbors]) + ']\n'
        s += ''.join([str(n) for n in self.neighbors if n not in visited])
        return s

if __name__ == '__main__':
    runTest(Node(1), Node(2), False)
    n4 = Node(4)
    runTest(Node(1, [Node(3), n4]), Node(2, [n4]), False)
    runTest(Node(1, [Node(3, [Node(2)]), n4]), n4, True)
    n2 = Node(2, [n4])
    n4.neighbors = [n2]
    runTest(Node(1, [Node(3, [n2]), n4]), n4, True)

