"""
Task 7: Trees
Contributor: Member D

Binary Search Tree with at least 7 nodes.
Implements insertion, Breadth-First (level order) traversal,
and Depth-First (in-order) traversal.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Time Complexity: O(h) where h = tree height (O(log n) if balanced)
        if self.root is None:
            self.root = TreeNode(value)
            return
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def bfs(self):
        """Breadth-First (level order) traversal using a manually built queue."""
        # Time Complexity: O(n) - every node visited exactly once
        result = []
        if self.root is None:
            return result

        queue = [self.root]  # list used purely as FIFO storage here
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs_inorder(self):
        """Depth-First in-order traversal (left, root, right)."""
        # Time Complexity: O(n) - every node visited exactly once
        result = []

        def _walk(node):
            if node is None:
                return
            _walk(node.left)
            result.append(node.value)
            _walk(node.right)

        _walk(self.root)
        return result


if __name__ == "__main__":
    tree = BinaryTree()
    values = [50, 30, 70, 20, 40, 60, 80]  # 7 nodes

    print("Inserting values:", values)
    for v in values:
        tree.insert(v)

    print("\nBreadth-First (level order) traversal:", tree.bfs())
    print("Depth-First (in-order) traversal:", tree.dfs_inorder())
