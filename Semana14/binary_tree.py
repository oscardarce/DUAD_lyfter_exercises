class BinaryNode:

    # Creamos el contructor del Nodo
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#
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

        # Tomamos la cabecera y la guardamos en una variable en este caso el root
        current = self.root

        # Agregamos nodos derechos e izquierdos de manera consecutiva y lo mostramos en pantalla
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BinaryNode(value)
                    return
                else:
                    current = current.left
                    print(f"Soy el número {current.value} un nodo izquierdo")
            elif value > current.value:
                if current.right is None:
                    current.right = BinaryNode(value)
                    return
                else:
                    current = current.right
                    print(f"Soy el número {current.value} un nodo derecho")

            else:
                print("No puedes agregar un número igual (duplicado).")
                return


tree = BinaryTree()
tree.add_numbers_to_binary_tree(20)
tree.add_numbers_to_binary_tree(25)
tree.add_numbers_to_binary_tree(5)
tree.add_numbers_to_binary_tree(2)
tree.add_numbers_to_binary_tree(20)
tree.add_numbers_to_binary_tree(28)
tree.add_numbers_to_binary_tree(36)
