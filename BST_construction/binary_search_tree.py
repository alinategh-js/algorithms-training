from enum import Enum
import math

class ChildDirection(Enum):
    LEFT = 1
    RIGHT = 2

class BinarySearchTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        while True:
            if value >= current_node.value:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = BinarySearchTree(value)
                    break
            else:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = BinarySearchTree(value)
                    break
        
        return self
        
    def search(self, value):
        current_node = self
        while True:
            if value == current_node.value:
                return True
            elif value > current_node.value:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    return False
            else: # value < current_node.value
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    return False

    def remove(self, value, parent_node = None, child_direction = None):
        current_node = self
        while current_node is not None:
            if value > current_node.value:
                parent_node = current_node
                child_direction = ChildDirection.RIGHT
                current_node = current_node.right
            elif value < current_node.value:
                parent_node = current_node
                child_direction = ChildDirection.LEFT
                current_node = current_node.left
            else: # value == current_node.value
                if parent_node is None:
                    current_node.value = None
                    break

                # if current node has no other child nodes attached to it
                if current_node.left is None and current_node.right is None:
                    if child_direction == ChildDirection.RIGHT:
                        parent_node.right = None
                    else:
                        parent_node.left = None
                    break

                # else if current node has either both 'left' and 'right' nodes
                # or only a 'right' node attached to it.
                elif (current_node.left is not None and current_node.right is not None
                        or current_node.left is None and current_node.right is not None):
                    current_node.value = current_node.right.getMinValue()
                    current_node.right.remove(current_node.value, current_node, ChildDirection.RIGHT)
                    break
                
                else: # current node only has a 'left' node attached to it.
                    if child_direction == ChildDirection.RIGHT:
                        parent_node.right = current_node.left
                    else:
                        parent_node.left = current_node.left
                    break

        return self


    def getMinValue(self):
        current_node = self
        min_value = current_node.value
        while current_node.left is not None:
            current_node = current_node.left
            min_value = current_node.value
        return min_value

    def findClosestValue(self, target_value):
        current_node = self
        closest_value = math.inf
        while current_node is not None:
            new_diff = abs(target_value - current_node.value)
            last_diff = abs(target_value - closest_value)
            if new_diff < last_diff:
                closest_value = current_node.value

            if target_value > current_node.value:
                current_node = current_node.right
            elif target_value < current_node.value:
                current_node = current_node.left
            else:
                break

        return closest_value

# Test:
if __name__ == "__main__":
    bst = BinarySearchTree(10)
    bst.insert(1).insert(12).insert(11).insert(21).insert(13).insert(15)
    # bst.remove(10)
    # bst.insert(10)
    print(bst.findClosestValue(23))