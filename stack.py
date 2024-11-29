class Stack:
    """
    Класс для реализации стека с использованием списка.
    Стек работает по принципу LIFO (последний вошёл — первый вышел).
    """

    def __init__(self):
        # Инициализируем пустой стек
        self.items = []

    def is_empty(self):
        # Проверяем, пуст ли стек
        return len(self.items) == 0

    def push(self, item):
        # Добавляем элемент в конец списка (на вершину стека)
        self.items.append(item)

    def pop(self):
        # Удаляем элемент с конца списка (с вершины стека)
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Попытка удалить элемент из пустого стека")

    def peek(self):
        # Получаем верхний элемент стека без его удаления
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Попытка получить верхний элемент из пустого стека")

    def size(self):
        # Возвращаем количество элементов в стеке
        return len(self.items)

# Пример использования стека
print("Работа со стеком:")
stack = Stack()
print("Стек пуст?", stack.is_empty())

stack.push(10)
stack.push(20)
stack.push(30)
print("Добавили элементы: 10, 20, 30")
print("Текущий размер стека:", stack.size())
print("Верхний элемент стека (без удаления):", stack.peek())

print("Удаляем верхний элемент:", stack.pop())
print("Верхний элемент после удаления:", stack.peek())
print("Текущий размер стека:", stack.size())
print("Стек пуст?", stack.is_empty())
print()

