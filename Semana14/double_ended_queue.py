class SongNode:

    def __init__(self, song, next_node=None):
        self.song = song
        self.next = next_node


class Playlist:
    # Constructor de la clase Playlist
    def __init__(self):
        self.head = None

    # Agregamos al inicio de la lista
    def push_left(self, song):
        self.head = SongNode(song, next_node=self.head)

    # Agregamos al final de la lista
    def push_right(self, song):
        new_node = SongNode(song)

        # Si no tenemos canciones en nuestra lista y esta vacía creamos el nuevo nodo con normalidad
        if self.head is None:
            self.head = new_node
            return

        # Primer nodo o head
        current = self.head

        # Iterador de canciones para encontrar la ultima canciòn
        while current.next is not None:
            current = current.next

        # Enlaza al final
        current.next = new_node

    # Quitamos al inicio de la lista
    def pop_left(self):

        # Si la lista esta vacia no hacemos nada
        if self.head is None:
            print("Lista vacia no puedes remover canciones")
            return

        # Movemos el head hacia la derecha por lo que se elimina el primer elemento
        self.head = self.head.next
        print("Removiste la primera canción")

    # Quitamos al final de la lista
    def pop_right(self):

        # Creamos un head temporal
        current = self.head

        # Si la lista esta vacia no hacemos nada
        if self.head is None:
            print("Lista vacia no puedes remover canciones")
            return

        if self.head.next is None:
            self.head = None
            print("Removiste la única canción en la lista")
            return

        # Mientras hayan más elementos a la derecha movemos el head temporal hacia el final y nos detenemos en el penultimo
        while current.next.next is not None and current.next is not None:
            current = current.next

        # Colocamos el ultimo nodo como None por lo que el Garbage Collector lo borra
        current.next = None
        print("Removiste la ultima canción")

    # Impresión de la lista

    def print_double_ended_queue(self):
        # Tomamos la cabecera
        current_node = self.head

        # Contador
        counter = 1

        # Mientras tengamos canciones se van a imprimir
        while current_node is not None:
            print(f"Canción #{counter}: {current_node.song}")
            current_node = current_node.next
            counter += 1


song = Playlist()

song.push_left("Julio Jaramillo - Mienteme")
song.push_right("Alejandro Fernandez - Me dedique a perderte")
song.push_left("Korn - Freak on the leash")

song.push_left("My Name Is - Eminem")
song.push_right("Arch Enemy - Leader of the Rats")
song.push_left("S.O.A.D - ATWA")

song.pop_left()
song.pop_right()

song.print_double_ended_queue()
