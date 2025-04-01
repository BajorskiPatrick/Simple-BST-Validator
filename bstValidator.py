from typing import List, Optional

class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(node_values: List[str]):
    if (
        not node_values
        or len(node_values) == 0
        or node_values[0].strip() == ""
        or node_values[0] == "null"
    ):
        return None
    root = Node(int(node_values[0]))
    queue = [(root, 0)]
    while queue:
        current_node, idx = queue.pop()
        left_idx = idx * 2 + 1
        right_idx = idx * 2 + 2
        if left_idx < len(node_values):  # left child
            value = node_values[left_idx]
            if value != "null":
                current_node.left = Node(int(value))
                if left_idx <= len(node_values) // 2:  # is not a leaf
                    queue.append((current_node.left, left_idx))

        if right_idx < len(node_values):  # right child
            value = node_values[right_idx]
            if value != "null":
                current_node.right = Node(int(value))
                if right_idx <= len(node_values) // 2:  # is not a leaf
                    queue.append((current_node.right, right_idx))

    return root


def get_left_subtree(root: Optional[Node]):
    if root:
        return root.left
    return None


def get_right_subtree(root: Optional[Node]):
    if root:
        return root.right
    return None


def is_valid_BST(root: Optional[Node]) -> bool:
    parent = root
    left = root.left
    right = root.right
    if parent is None:
        return True

    if left is None and right is None:
        return True
    elif left is None and right is not None:
        result = checkR(parent, right)
        if result:
            is_valid_BST(right)
        else:
            return False
    elif left is not None and right is None:
        result = checkL(parent, left)
        if result:
            is_valid_BST(left)
        else:
            return False
    else:
        result_l = checkL(parent, left)
        result_r = checkR(parent, right)
        if result_l and result_r:
            is_valid_BST(left)
            is_valid_BST(right)
        else:
            return False

    return True


def checkL(parent: Optional[Node], node: Optional[Node]) -> bool:
    if node.left is None and node.right is None:
        if parent.val > node.val:
            return True
        else:
            return False

    if node.right is not None:
        if parent.val > node.right.val >= node.val:
            pass
        else:
            return False
    if node.left is not None:
        if parent.val > node.val > node.left.val:
            pass
        else:
            return False

    return True


def checkR(parent: Optional[Node], node: Optional[Node]) -> bool:
    if node.left is None and node.right is None:
        if parent.val <= node.val:
            return True
        else:
            return False

    if node.right is not None:
        if node.right.val >= node.val >= parent.val:
            pass
        else:
            return False
    if node.left is not None:
        if node.val > node.left.val >= parent.val:
            pass
        else:
            return False

    return True


if __name__ == "__main__":
    node_values = input().strip().split(" ")
    root = create_binary_tree(node_values)
    subRoot1 = get_left_subtree(root)
    subRoot2 = get_right_subtree(root)
    print(is_valid_BST(root), is_valid_BST(subRoot1), is_valid_BST(subRoot2))
