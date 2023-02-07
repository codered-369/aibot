class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def iddfs(root, target, depth=0):
    if root is None:
        return False
    if root.value == target:
        return True
    if depth == 0:
        return False
    for child in root.children:
        if iddfs(child, target, depth - 1):
            return True
    return False

# Example usage
root = Node("A", [Node("B", [Node("D"), Node("E")]), Node("C", [Node("F"), Node("G")])])
target = "E"

for i in range(5):
    if iddfs(root, target, i):
        print(f"Target found at depth {i}")
        break
else:
    print("Target not found")
