class LinkedList:
    def __init__(self):
        self.head = None  # La cabeza de la lista está vacía al principio

    # Método para insertar un nodo al final de la lista
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Método para eliminar el primer nodo con un valor específico
    def delete(self, key):
        current = self.head
        # Si el nodo a eliminar es la cabeza
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Buscar el nodo a eliminar
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # Si no se encontró el nodo
        if not current:
            print("El valor no se encontró.")
            return

        # Eliminar el nodo
        prev.next = current.next
        current = None

    # Método para buscar un valor en la lista
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Método para mostrar la lista
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Ejemplo de uso
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)

ll.print_list()  # Imprime: 10 -> 20 -> 30 -> None

print("Buscar 20:", ll.search(20))  # Imprime: True
print("Buscar 40:", ll.search(40))  # Imprime: False

ll.delete(20)  # Elimina el nodo con valor 20
ll.print_list()  # Imprime: 10 -> 30 -> None
