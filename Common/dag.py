import copy

class DAG:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def delete_node(self, node):
        for i in range(len(self.nodes)):
            if self.nodes[i].val == node.val and self.nodes[i].parent == node.parent:
                self.nodes.pop(i)

    def __traverse_to_value(self, node, val):
        if node.val == val:
            return node
        for child in node.children:
            self.__traverse_node(child, val)

    def print(self):
        for node in self.nodes:
            print(f'{node.val}\t{node.parent}')

    def contains_node(self, candidate_node):
        for node in self.nodes:
            if node.val == candidate_node.val:
                return True
        return False

    def contains_value(self, value):
        for node in self.nodes:
            if node.val == value:
                return True
        return False

    def __traverse_node(self, node, print_prefix):
        print(f'{print_prefix}{node.val}')
        for child in node.children:
            print_prefix += '-'
            self.__traverse_node(child, print_prefix)


    def print_dag_tree(self):
        root_nodes = []
        for i in range(len(self.nodes)):
            if self.nodes[i].parent is None:
                root_nodes.append(self.nodes[i])
        for node in root_nodes:
            self.__traverse_node(node, '')

    class Node:
        def __init__(self, val, parent=None, children=None):
            self.val = val
            self.parent = parent
            if children is None:
                self.children = []
            else:
                self.children = children

        def set_val(self, val):
            self.val = val

        def set_parent(self, parent_node):
            self.parent = parent_node
        def add_child(self, node):
            self.children.append(node)
        def add_children(self, nodes):
            for node in nodes:
                self.children.append(node)

        def traverse_up(self):
            nodes = []
            tmp_node = copy.deepcopy(self)
            while tmp_node.parent is not None:
                nodes.append(tmp_node)
                tmp_node = copy.deepcopy(self.parent)
            nodes.append(tmp_node)

            return nodes

        def get_depth(self):
            depth = 0

            tmp_node = copy.deepcopy(self)
            while tmp_node.parent is not None:
                depth += 1
                tmp_node = copy.deepcopy(self.parent)

            return depth