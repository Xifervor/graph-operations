class Graph:
    def __init__(self):
        self.matrix = []

    #Чтение из файла
    def load_from_file(self, filename):
        self.matrix = [] 
        
        with open(filename, 'r') as file:
            for line in file:
                pieces = line.split() 
                row = [] 
                for piece in pieces:
                    number = int(piece)   
                    row.append(number)    
                self.matrix.append(row)
                
        print("Прочитан файл:", filename)

    #Сохранение в файл
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.matrix:
                text_pieces = [] 
                for number in row:
                    text_piece = str(number)     
                    text_pieces.append(text_piece) 
                
                line_to_write = ' '.join(text_pieces)
                file.write(line_to_write + '\n')
        print("Результат сохранен в файл:", filename)

    #Выравнивание
    def pad_to_size(self, target_size):
        current_size = len(self.matrix)
        if current_size >= target_size:
            return 

        for row in self.matrix:
            missing_zeros = target_size - len(row)
            for i in range(missing_zeros):
                row.append(0)
                
        missing_rows = target_size - current_size
        for i in range(missing_rows):
            new_row = [] 
            for j in range(target_size):
                new_row.append(0)
            self.matrix.append(new_row)

    #Объединение графов
    def get_union(self, other_graph):
        result_graph = Graph()
        size = len(self.matrix)
        
        for i in range(size):
            new_row = []
            for j in range(size):
                val1 = self.matrix[i][j]
                val2 = other_graph.matrix[i][j]
                
                #хотя бы в одном графе есть связь
                if val1 == 1 or val2 == 1:
                    new_row.append(1)
                else:
                    new_row.append(0)
                    
            result_graph.matrix.append(new_row)
        return result_graph

    #Пересечение графов
    def get_intersection(self, other_graph):
        result_graph = Graph()
        size = len(self.matrix)
        
        for i in range(size):
            new_row = []
            for j in range(size):
                val1 = self.matrix[i][j]
                val2 = other_graph.matrix[i][j]
                
                #связь должна быть строго в обоих графах
                if val1 == 1 and val2 == 1:
                    new_row.append(1)
                else:
                    new_row.append(0)
                    
            result_graph.matrix.append(new_row)
        return result_graph

    #Умножение графов
    def get_product(self, other_graph):
        result_graph = Graph()
        size = len(self.matrix)
        
        for i in range(size):
            new_row = []
            for j in range(size):
                # Считаем сумму умножений строки на столбец
                cell_sum = 0
                for k in range(size):
                    # Берем элемент из строки первого графа и из столбца второго
                    val1 = self.matrix[i][k]
                    val2 = other_graph.matrix[k][j]
                    cell_sum = cell_sum + (val1 * val2)
                
                # Если сумма больше нуля, значит связь
                if cell_sum > 0:
                    new_row.append(1)
                else:
                    new_row.append(0)
                    
            result_graph.matrix.append(new_row)
        return result_graph


#Создаем
graph1 = Graph()
graph2 = Graph()

#Загружаем 
graph1.load_from_file('input1.txt')
graph2.load_from_file('input2.txt')

#Выравниваем
size1 = len(graph1.matrix)
size2 = len(graph2.matrix)
max_size = max(size1, size2)

graph1.pad_to_size(max_size)
graph2.pad_to_size(max_size)


#Объединение
print("\nОбъединение выполнено")
graph_union = graph1.get_union(graph2)
graph_union.save_to_file('output_union.txt')

#Пересечение 
print("Пересечение выполнено")
graph_intersection = graph1.get_intersection(graph2)
graph_intersection.save_to_file('output_intersection.txt')

#Умножение
print("Умножение выполнено")
graph_product = graph1.get_product(graph2)
graph_product.save_to_file('output_product.txt')

print("\nЗавершено.")
