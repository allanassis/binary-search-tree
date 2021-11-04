from unittest import TestCase
import unittest

from binary_search_tree import BinarySearchTree, BinaryTreeNode

class TestBinarySearchTree(TestCase):
    def setUp(self):
        self.root_value = "Marvin Robot"
        self.some_value = "Babel Fish"

    def test_instance(self):
        # arrange/act
        tree = BinarySearchTree()
        # assert
        self.assertIsInstance(tree, BinarySearchTree)

    def test_insert_root(self):
        # arrange
        tree = BinarySearchTree()
        # act
        tree.insert(self.root_value)
        # assert
        self.assertIsInstance(tree.root, BinaryTreeNode)
        self.assertEqual(tree.root.value, self.root_value)

    def test_insert_root_child(self):
        # arrange
        tree = BinarySearchTree()
        tree.insert(self.root_value)
        # act
        tree.insert(self.some_value)
        # assert
        self.assertIsInstance(tree.root.left, BinaryTreeNode)
        self.assertEqual(tree.root.left.value, self.some_value)

    def test_get_in_level_order_list(self):
        # arrange
        tree = BinarySearchTree()
        tree.insert(1)
        tree.insert(3)
        tree.insert(2)
        tree.insert(10)
        tree.insert(5)
        tree.insert(6)
        expected = [1,3,2,10,5,6]
        # act
        ordered_list = tree.get_list_in_level_order()
        # assert
        self.assertListEqual(expected, ordered_list)

    def test_insert_in_binary_search_order(self):
        # arrange
        tree = BinarySearchTree()
        # act
        tree.insert(1)
        tree.insert(3)
        tree.insert(2)
        tree.insert(4)
        tree.insert(5)
        # assert
        self.assertLess(tree.root.value, tree.root.right.value)
        self.assertGreater(tree.root.right.right.value, tree.root.right.left.value)

    def test_find_node(self):
        # arrange
        tree = BinarySearchTree()
        tree.insert(1)
        tree.insert(3)
        tree.insert(2)
        tree.insert(4)
        tree.insert(5)
        # act
        node = tree.find(3)
        # assert
        self.assertEqual(node.value, 3)
        self.assertEqual(node.left.value, 2)
        self.assertEqual(node.right.value, 4)

    def test_min_value(self):
        # arrange
        tree = BinarySearchTree()
        tree.insert(4)
        tree.insert(1)
        tree.insert(2)
        tree.insert(5)
        tree.insert(7)
        # act
        node = tree.min()
        # assert
        self.assertEqual(node.value, 1)

    def test_delete_leaf_node(self):
        # arrange
        tree = BinarySearchTree()
        tree.insert(3)
        tree.insert(2)
        tree.insert(1) # leaf
        tree.insert(5)
        tree.insert(4)
        tree.insert(10)
        tree.insert(11)
        
        expected = [3,2,5,4,10,11]
        # act
        tree.delete(1)
        # assert
        self.assertListEqual(expected, tree.get_list_in_level_order())

    def test_delete_node_with_one_child(self):
        # arrange
        tree = BinarySearchTree()
        tree.insert(3)
        tree.insert(2) # one child
        tree.insert(1) # leaf
        tree.insert(5)
        tree.insert(4)
        tree.insert(10)
        tree.insert(11)

        expected = [3,1,5,4,10,11]
        # act
        tree.delete(2)
        # assert
        self.assertListEqual(expected, tree.get_list_in_level_order())

    def test_delete_node_with_two_child(self):
        # arrange
        tree = BinarySearchTree()
        tree.insert(3)
        tree.insert(2) # one child
        tree.insert(1) # leaf
        tree.insert(5) # has two childs
        tree.insert(4)
        tree.insert(10)
        tree.insert(11)

        expected = [3,2,10,1,4,11]
        # act
        tree.delete(5)
        # assert
        self.assertListEqual(expected, tree.get_list_in_level_order())
        
if __name__ == "__main__":
    unittest.main()