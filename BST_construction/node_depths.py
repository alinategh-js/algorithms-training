from binary_search_tree import BinarySearchTree

def nodeDepths(root: BinarySearchTree):
    depths_list = []
    calculateNodeDepths(root, -1, depths_list)
    return sum(depths_list)

def calculateNodeDepths(node: BinarySearchTree, prev_depth, depths_list: list):
    if node is None:
        return
    
    depth = prev_depth + 1
    depths_list.append(depth)

    calculateNodeDepths(node.left, depth, depths_list)
    calculateNodeDepths(node.right, depth, depths_list)

# using stack
def nodeDepths2(root: BinarySearchTree):
    nodes_stack = []
    nodes_stack.append((root, 0))
    depths_sum = 0
    while len(nodes_stack) != 0:
        current_item = nodes_stack.pop()
        current_node = current_item[0]
        node_depth = current_item[1]
        if current_node == None:
            continue
        depths_sum += node_depth
        nodes_stack.append((current_node.left, node_depth + 1))
        nodes_stack.append((current_node.right, node_depth + 1))
    return depths_sum

bst = BinarySearchTree(10)
bst.insert(1).insert(12).insert(11).insert(21).insert(13).insert(15)
depths_sum = nodeDepths(bst)
print(depths_sum)
depths_sum = nodeDepths2(bst)
print(depths_sum)