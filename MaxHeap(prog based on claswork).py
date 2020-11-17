from collections import defaultdict


class MaxHeap:
    def __init__(self):
        self.list = [0]
        self.size = 0

    def move_up(self, i):
        while i // 2 > 0:
            if self.list[i] > self.list[i // 2]:
                self.list[i], self.list[i // 2] = self.list[i // 2], self.list[i]
            i = i // 2

    def insert(self, k):
        self.list.append(k)
        self.size += 1
        self.move_up(self.size)

    def move_down(self, i):
        while i * 2 <= self.size:
            mc = self.max_leaf(i)
            if self.list[i] < self.list[mc]:
                self.list[i], self.list[mc] = self.list[mc], self.list[i]
            i = mc

    def max_leaf(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            return (i * 2, i * 2 + 1)[self.list[i * 2] < self.list[i * 2 + 1]]

    def get_max(self):
        return_value = self.list[1]
        self.list[1] = self.list[self.size]
        self.size -= 1
        self.list.pop()
        self.move_down(1)
        return return_value
    
    
input_list = [[1,2,1], [1,7,9], [2,3,2],[3,4,1], [4,7,2], [4,5,2], [5,6,3], [6,7,1], [7,9,6], [7,9,1], [7,8,2], [8,9,2]]
number_of_elements = 9
source = 1
target = 9

# Инициализируем граф
graph = defaultdict(list)
# Заполняем граф: вершина -> (стоимость, вершина куда можем прийти)
for a, b, cost in input_list:
    graph[a] += [(cost, b)]
# Инициализируем список вершин для посещения
nodes_to_visit = MaxHeap()
# Добавляем нашу исходную с расстоянием равным нулю
nodes_to_visit.insert((0, source))
# Инициализируем список уникальных значений для хранения вершин которые уже посетили
visited = set()
# Заполняем расстояния до всех остальных вершие
min_dist = {i: float('inf') for i in range(1, number_of_elements + 1)}
# Заполняем расстояние до текущей вершины
min_dist[source] = 0
# Проходимся по всем вершинам которые нужно посетить
# Проходимся до тех пор, пока такие вершины есть
while nodes_to_visit.size:
    # Берем самую близкую вершину к нам
    # cost - стоимость попадания, node - название вершины
    cost, node = nodes_to_visit.get_max()
    # Проверяем что мы в нее еще не заходили (если вдруг мы сначала добавили (9,7), а потом (6,7)
    if node in visited:
        continue
    # Добавляем в список посещенных
    visited.add(node)
    # Проходимся по всем соединенным вершинам
    # n_cost - стоимость попадания из текущей вершины, n_node - прикрепленная вершина, в которую хотим попасть
    for n_cost, n_node in graph[node]:
        # Проверяем нашли ли мы оптимальный путь
        if cost + n_cost < min_dist[n_node] and n_node not in visited:
            # Если нашли то обновляем значение расстояния
            min_dist[n_node] = cost + n_cost
            # И добавляем эту вершину в список вершин для посещения
            nodes_to_visit.insert((cost + n_cost, n_node))

# Выводим ответ
print(min_dist[target]) #10