class BinaryNode:

    # Creamos el contructor del Nodo
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    # Creamos el constructor del root
    def __init__(self):
        self.root = None

    # Creamos la funcion para agregar números
    def add_numbers_to_binary_tree(self, value):

        # Si no tenemos un root creamos suno nuevo de 0
        if self.root is None:
            self.root = BinaryNode(value)
            return

        current = self.root

        # Tomamos la cabecera y la guardamos en una variable en este caso el root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BinaryNode(value)
                    return False
                else:
                    current = current.left

            elif value > current.value:
                if current.right is None:
                    current.right = BinaryNode(value)
                    return False
                else:
                    current = current.right

            else:
                print("No puedes agregar un número igual (duplicado).")
                return

    def print_binary_tree_inorder(self):
        def inorder(node):
            if node is not None:
                inorder(node.left)
                print(node.value, end=" ⭢ ")
                inorder(node.right)

        if self.root is None:
            print("Árbol vacío")
        else:
            inorder(self.root)
            print("Arbol izquierda → raíz → derecha")

    def print_binary_tree_preorder(self):
        def preorder(node):
            if node is not None:
                print(node.value, end=" ⭢ ")
                preorder(node.left)
                preorder(node.right)

        if self.root is None:
            print("Árbol vacío")
        else:
            preorder(self.root)
            print("Arbol raíz → izquierda → derecha")

    def print_binary_tree_postorder(self):
        def postorder(node):
            if node is not None:
                postorder(node.left)
                postorder(node.right)
                print(node.value, end=" ⭢ ")

        if self.root is None:
            print("Árbol vacío")
        else:
            postorder(self.root)
            print("Arbol izquierda → derecha → raíz")


tree = BinaryTree()

tree.add_numbers_to_binary_tree(20)
tree.add_numbers_to_binary_tree(25)
tree.add_numbers_to_binary_tree(5)
tree.add_numbers_to_binary_tree(2)
# tree.add_numbers_to_binary_tree(20)
tree.add_numbers_to_binary_tree(28)
tree.add_numbers_to_binary_tree(36)

tree.print_binary_tree_inorder()
tree.print_binary_tree_preorder()
tree.print_binary_tree_postorder()
