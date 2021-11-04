class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value, current_node=None):
        if self.root is None:
            self.root = BinaryTreeNode(value)
            return

        if current_node is None:
            current_node = self.root

        if value > current_node.value:
            if current_node.right is None:
                current_node.right = BinaryTreeNode(value)
            else:
                self.insert(value, current_node.right)
        else:
            if current_node.left is None:
                current_node.left = BinaryTreeNode(value)
            else:
                self.insert(value, current_node.left)
        return

    def find(self, value, current_node=None):
        if self.root is None:
            raise Exception("Empty tree!")

        if current_node is None:
            current_node = self.root
        
        if value == current_node.value:
            return current_node

        if value > current_node.value and current_node.right is not None:
            return self.find(value, current_node.right)

        elif value <= current_node.value and current_node.left is not None:
            return self.find(value, current_node.left)

        raise Exception("Not found!")

    def delete(self, value, current_node=None):
        if self.root is None:
            raise Exception("Empty tree!")
        
        if current_node is None:
            current_node = self.root

        if current_node.value == value:
            if current_node.left is None and current_node.right is None:
                return None

            elif current_node.left is None:
                return current_node.right

            elif current_node.right is None:
                return current_node.left
            else:
                min_node = self.min(current_node.right)
                current_node.value = min_node.value
                current_node.right = self.delete(min_node.value, current_node.right)

        if current_node.right is not None and value > current_node.value:
            current_node.right = self.delete(value, current_node.right)

        elif current_node.left is not None and value < current_node.value:
            current_node.left = self.delete(value, current_node.left)

        return current_node
        
            

    def min(self, current_node=None):
        if self.root is None:
            raise Exception("Empty tree!")

        if current_node is None:
            current_node = self.root

        if current_node.left is None:
            return current_node
        
        return self.min(current_node.left)

    def get_list_in_level_order(self):
        if self.root is None:
            return []

        current = self.root
        queue = [current]
        level_order_list = []

        while len(queue):
            current = queue.pop(0)
            level_order_list.append(current.value)

            if current.left is not None :
                queue.append(current.left)

            if current.right is not None :
                queue.append(current.right)

        return level_order_list