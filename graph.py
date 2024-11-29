class Graph:
    """
    Класс для представления графа с использованием списка смежности.
    """

    def __init__(self):
        # Список смежности
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Добавление вершины в граф.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, directed=False):
        """
        Добавление ребра между двумя вершинами.
        Если directed=True, добавляется направленное ребро.
        """
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)

        # Добавляем ребро
        self.adjacency_list[vertex1].append(vertex2)

        # Если граф неориентированный, добавляем обратное ребро
        if not directed:
            self.adjacency_list[vertex2].append(vertex1)

    def display(self):
        """
        Отображение графа.
        """
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {', '.join(map(str, edges))}")

    def bfs(self, start_vertex):
        """
        Поиск в ширину (Breadth-First Search).
        """
        visited = set()
        queue = [start_vertex]
        result = []

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                result.append(current)
                # Добавляем соседей в очередь
                queue.extend([neighbor for neighbor in self.adjacency_list[current] if neighbor not in visited])

        return result

    def dfs(self, start_vertex, visited=None):
        """
        Поиск в глубину (Depth-First Search).
        """
        if visited is None:
            visited = set()

        visited.add(start_vertex)
        result = [start_vertex]

        for neighbor in self.adjacency_list[start_vertex]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))

        return result


# Создаём граф
graph = Graph()

# Добавляем вершины и рёбра
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "E")
graph.add_edge("E", "F")

# Отображение графа
print("Список смежности:")
graph.display()

# Поиск в ширину
print("\nПоиск в ширину (BFS) от вершины A:")
print(graph.bfs("A"))

# Поиск в глубину
print("\nПоиск в глубину (DFS) от вершины A:")
print(graph.dfs("A"))
