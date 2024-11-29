class Node:
    """
    Класс для представления узла дерева.
    """

    def __init__(self, value):
        # Значение, хранящееся в узле
        self.value = value
        # Левый дочерний узел
        self.left = None
        # Правый дочерний узел
        self.right = None

    def __str__(self):
        # Удобный вывод узла
        return f"Node({self.value})"

class BinarySearchTree:
    """
    Класс для реализации бинарного дерева поиска.
    """

    def __init__(self):
        # Изначально дерево пусто
        self.root = None

    def insert(self, value):
        """
        Вставка нового значения в дерево.
        """
        new_node = Node(value)
        if self.root is None:
            # Если дерево пустое, новый узел становится корнем
            self.root = new_node
        else:
            # Вставка узла в подходящее место
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        """
        Рекурсивная вставка узла.
        """
        if new_node.value < current.value:
            # Если значение меньше текущего, идем в левое поддерево
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        elif new_node.value > current.value:
            # Если значение больше текущего, идем в правое поддерево
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def search(self, value):
        """
        Поиск значения в дереве.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        """
        Рекурсивный поиск значения.
        """
        if current is None:
            # Если узел не найден
            return False
        if current.value == value:
            # Значение найдено
            return True
        elif value < current.value:
            # Идем в левое поддерево
            return self._search_recursive(current.left, value)
        else:
            # Идем в правое поддерево
            return self._search_recursive(current.right, value)

    def inorder_traversal(self):
        """
        Симметричный обход дерева (in-order traversal).
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current, result):
        """
        Рекурсивный симметричный обход дерева.
        """
        if current is not None:
            # Сначала обходим левое поддерево
            self._inorder_recursive(current.left, result)
            # Затем добавляем значение текущего узла
            result.append(current.value)
            # Потом обходим правое поддерево
            self._inorder_recursive(current.right, result)


# Создаем бинарное дерево поиска
bst = BinarySearchTree()

# Добавляем элементы
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Поиск значений
print("Поиск 40:", bst.search(40))  # True
print("Поиск 25:", bst.search(25))  # False

# Симметричный обход дерева
print("Симметричный обход дерева:", bst.inorder_traversal())
