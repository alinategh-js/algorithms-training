from binary_search_tree import BinarySearchTree

def branchSums(root: BinarySearchTree):
    sums_list = []
    calculateBranchSums(root, 0, sums_list)
    return sums_list

def calculateBranchSums(node: BinarySearchTree, running_sum, sums_list: list):
    if node is None:
        return

    running_sum = running_sum + node.value
    if node.right is None and node.left is None:
        sums_list.append(running_sum)
        return
    
    calculateBranchSums(node.left, running_sum, sums_list)
    calculateBranchSums(node.right, running_sum, sums_list)

bst = BinarySearchTree(10)
bst.insert(1).insert(12).insert(11).insert(21).insert(13).insert(15)
sums_list = branchSums(bst)
print(sums_list)