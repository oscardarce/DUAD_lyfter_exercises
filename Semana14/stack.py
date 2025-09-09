class OrderNode:

    def __init__(self, book_number, next_node=None):
        self.book_number = book_number
        self.next = next_node


class BooksShelf:

    # Cabeza por default vacia
    def __init__(self):
        self.head = None

    # Metodo para colocar un nuevo libro en la pila
    def push_new_book(self):

        # Si la cabeza esta vacia, será nuestro head y primer nodo
        head = self.head

       # Si la cabeza esta vacia, será nuestro head y primer nodo
        if head is None:
            self.head = OrderNode(1)
            return

        # Si hay un libro en la pila de libros será el 2 y así consecutivamente
        next_number = head.book_number + 1

        # Añadimos nuestro proximo libro a la pila y se lo ligamos al stack
        self.head = OrderNode(next_number, next_node=self.head)

    # Metodo para quitar libros de la pila
    def pop_a_book(self):

        # Validamos que la cabecera exista, en el momento que ya no exista es porque no hay más libros
        head = self.head
        if head is None:
            print("No puedes quitar más libros porque ya no hay")
            return

        #Quitamos un libro de la pila
        self.head = head.next
        print(f"Quitaste el libro #{head.book_number}")

    def print_linked_list(self):

        # Tomamos la cabecera
        current_node = self.head

        # Recorremos de la cabeza hasta que el el ultimo nodo sea None
        while current_node is not None:
            print(
                f"Estas colocando el libro # {current_node.book_number} en la pila de libros")
            current_node = current_node.next


books_stack = BooksShelf()

books_stack.push_new_book()
books_stack.push_new_book()
books_stack.push_new_book()
books_stack.print_linked_list()

books_stack.pop_a_book()
books_stack.pop_a_book()
books_stack.pop_a_book()
books_stack.pop_a_book()
books_stack.print_linked_list()
