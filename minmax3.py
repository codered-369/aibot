import math
def minmax(tree,depth):
    max_turn = bool(depth%2)
    for i in range(int(depth)):
        zipped = zip(tree[::2],tree[1::2])
        print(tree[::2],tree[1::2])
        if max_turn:
            tree = [max(a,b) for a,b in zipped]
        else:
            tree = [max(a,b) for a,b in zipped]
        max_turn = not max_turn
    return tree[0]
A = [3,5,2,9,12,5,23,23]
depth = math.ceil(math.log(len(A)))
print(A)
print(minmax(A,depth))
