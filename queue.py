class Queue:
    """
    Класс для реализации очереди с использованием списка.
    Очередь работает по принципу FIFO (первый вошёл — первый вышел).
    """

    def __init__(self):
        # Инициализируем пустую очередь
        self.items = []

    def is_empty(self):
        # Проверяем, пуста ли очередь
        return len(self.items) == 0

    def enqueue(self, item):
        # Добавляем элемент в конец списка (в конец очереди)
        self.items.append(item)

    def dequeue(self):
        # Удаляем элемент с начала списка (из начала очереди)
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Попытка удалить элемент из пустой очереди")

    def size(self):
        # Возвращаем количество элементов в очереди
        return len(self.items)


# Пример использования очереди
print("Работа с очередью:")
queue = Queue()
print("Очередь пуста?", queue.is_empty())

queue.enqueue("Первая задача")
queue.enqueue("Вторая задача")
queue.enqueue("Третья задача")
print("Добавили задачи в очередь: 'Первая задача', 'Вторая задача', 'Третья задача'")
print("Текущий размер очереди:", queue.size())

print("Удаляем первый элемент:", queue.dequeue())
print("Текущий размер очереди после удаления:", queue.size())
print("Очередь пуста?", queue.is_empty())