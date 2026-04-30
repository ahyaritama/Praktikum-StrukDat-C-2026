class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root: BinaryTreeNode = None
    
    def insert_root(self, data):
        self.root = BinaryTreeNode(data)
    
    def insert_left(self, parent: BinaryTreeNode, data):
        if parent.left is None:
            parent.left = BinaryTreeNode(data)
        else:
            new_node = BinaryTreeNode(data)
            new_node.left = parent.left
            parent.left = new_node
    
    def insert_right(self, parent: BinaryTreeNode, data):
        if parent.right is None:
            parent.right = BinaryTreeNode(data)
        else:
            new_node = BinaryTreeNode(data)
            new_node.right = parent.right
            parent.right = new_node
    
    def traverse_preorder(self, node, res):
        if node is not None:
            res.append(node.data)
            self.traverse_preorder(node.left, res)
            self.traverse_preorder(node.right, res)
        return res

    def traverse_inorder(self, node, res):
        if node is not None:
            self.traverse_inorder(node.left, res)
            res.append(node.data)
            self.traverse_inorder(node.right, res)
        return res

    def traverse_postorder(self, node, res):
        if node is not None:
            self.traverse_postorder(node.left, res)
            self.traverse_postorder(node.right, res)
            res.append(node.data)
        return res
    
    def get_leaf_nodes(self, node, leaf_list):
        if node:
            if node.left is None and node.right is None:
                leaf_list.append(node.data)
            self.get_leaf_nodes(node.left, leaf_list)
            self.get_leaf_nodes(node.right, leaf_list)
        return leaf_list


def main():
    tree = BinaryTree()
    tree.insert_root("A")
    tree.insert_left(tree.root, "B")
    tree.insert_right(tree.root, "C")
    tree.insert_left(tree.root.left, "D")
    tree.insert_right(tree.root.left, "E")
    tree.insert_right(tree.root.right, "F")

    pre_res = []
    in_res = []
    post_res = []
    last = []

    tree.traverse_preorder(tree.root, pre_res)
    tree.traverse_inorder(tree.root, in_res)
    tree.traverse_postorder(tree.root, post_res)
    tree.get_leaf_nodes(tree.root, last)

    print("Preorder:", " - ".join(pre_res))
    print("Inorder:", " - ".join(in_res))
    print("Postorder:", " - ".join(post_res))

    print("Gudang Ujung (Leaf Nodes):", ", ".join(last))



if __name__ == "__main__":
    main()