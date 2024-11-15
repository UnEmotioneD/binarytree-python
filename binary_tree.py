""""
Usage
_____
Binary tree with search and delete function
Randomly order 0 to 9
After search or delete shows the list with inorder function
Delete function is separated into delete leaf, 1child, 2child methods
"""

import random

# pylint: disable=missing-function-docstring, too-few-public-methods


class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def inorder(tree_node):
    if tree_node is None:
        return
    inorder(tree_node.left)
    print(tree_node.data, end=" -> ")
    inorder(tree_node.right)


def delete_leaf(left_node, parent_node):
    if parent_node.left == left_node:
        parent_node.left = None
    else:
        parent_node.right = None
    del left_node


def delete_node_1_left(single_left_node, parent_node):
    if parent_node:
        if parent_node.left == single_left_node:
            parent_node.left = single_left_node.left
        else:
            parent_node.right = single_left_node.left
    del single_left_node


def delete_node_1_right(single_right_node, parent_node):
    if parent_node:
        if parent_node.left == single_right_node:
            parent_node.left = single_right_node.right
        else:
            parent_node.right = single_right_node.right
    del single_right_node


def delete_node_2child(two_child_node):
    successor_parent = two_child_node
    successor = two_child_node.right
    while successor.left is not None:
        successor_parent = successor
        successor = successor.left
    two_child_node.data = successor.data
    if successor_parent.left == successor:
        successor_parent.left = successor.right
    else:
        successor_parent.right = successor.right
    del successor


memory = []
ROOT = None

# Create a list of numbers from 0 to 9
# Shuffle the list
numbers = list(range(10))
random.shuffle(numbers)
numAry = numbers

if __name__ == "__main__":

    node = TreeNode()
    node.data = numAry[0]
    ROOT = node
    memory.append(node)

    for number in numAry[1:]:
        node = TreeNode()
        node.data = number

        current = ROOT
        while True:
            if number < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            elif number > current.data:
                if current.right is None:
                    current.right = node
                    break
                current = current.right

        memory.append(node)

    print(numAry)

    # Search
    findNumber = int(input("Type a number you want to search -> "))
    current = ROOT
    while True:
        print(current.data)
        if findNumber == current.data:
            print(findNumber, "Found")
            break
        elif findNumber < current.data:
            if current.left is None:
                print(findNumber, "Not here")
                break
            current = current.left
        else:
            if current.right is None:
                print(findNumber, "Not here")
                break
            current = current.right

    print("Inorder: ", end=" ")
    inorder(ROOT)
    print("End")

    while True:
        # Delete
        deleteNumber = int(input("Type in a number you want to delete -> "))
        print("-" * 60)
        current = ROOT
        parent = None
        while True:
            print(current.data)
            if deleteNumber == current.data:
                if current.left is None and current.right is None:
                    delete_leaf(current, parent)

                elif current.left is not None and current.right is None:
                    if parent is None:
                        ROOT = current.left
                    else:
                        delete_node_1_right(current, parent)

                elif current.left is None and current.right is not None:
                    if parent is None:
                        ROOT = current.right
                    else:
                        delete_node_1_left(current, parent)

                elif current.left is not None and current.right is not None:
                    delete_node_2child(current)

                print(deleteNumber, "Deleted")
                break

            elif deleteNumber < current.data:
                if current.left is None:
                    print(deleteNumber, "Not here")
                    break
                parent = current
                current = current.left
            else:
                if current.right is None:
                    print(deleteNumber, "Not here")
                    break
                parent = current
                current = current.right

        print("Inorder: ", end=" ")
        inorder(ROOT)
        print("End")

        print("Do you want to repeat? (y/n)")
        user_input = input()
        if user_input.lower() == "n":
            print("Terminated")
            break
