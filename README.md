# Binary Search Tree Validator

## Overview

This Python script builds a binary tree from level-order input and checks whether:
- the entire tree,
- the left subtree,
- the right subtree  
are valid Binary Search Trees (BSTs).

## What is a BST?

A Binary Search Tree is a binary tree in which:
- All nodes in the left subtree are less than the parent node.
- All nodes in the right subtree are greater than or equal to the parent node.
- The same rules apply recursively to every subtree.

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. When prompted, input a space-separated list of node values in level-order. Use `"null"` for missing children.

   **Example:**
   ```
   5 3 8 1 4 null 10
   ```

3. Output:
   - The script will print `True` or `False` for each of:
     - the entire tree
     - the left subtree
     - the right subtree

## Example

**Input:**
```
5 3 8 1 4 null 10
```

**Output:**
```
True True True
```

## License

This project is released under the MIT License.