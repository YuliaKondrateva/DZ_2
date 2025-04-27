import random

class CustomList:
    def __init__(self, size):
        self.data = [random.randint(-100, 100) for _ in range(size)]
        self.size = size
        self.read_count = 0
        self.write_count = 0

    def print_list(self):
        print("Список:", *self.data)

    def get(self, index):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return None
        self.read_count += 1
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return False
        if value < -100 or value > 100:
            print("Value out of allowed range [-100, 100]")
            return False
        self.data[index] = value
        self.write_count += 1
        print(f"Элемент {index} изменён на {value}")
        return True

    def add_value(self, value):
        if value < -100 or value > 100:
            print("Value out of allowed range [-100, 100], not adding.")
            return False
        self.data.append(value)
        self.size += 1
        self.write_count += 1
        print(f"Добавлено значение {value} в конец списка")
        return True

    def add_list(self, other_list):
        if isinstance(other_list, CustomList):
            other_data = other_list.data
            other_length = other_list.size
        else:
            other_data = other_list
            try:
                other_length = len(other_data)
            except TypeError:
                print("Provided other_list is not a list or CustomList")
                return False

        max_len = max(self.size, other_length)
        for i in range(max_len):
            x = self.data[i] if i < self.size else 0
            y = other_data[i] if i < other_length else 0
            new_val = x + y
            if i < self.size:
                self.data[i] = new_val
            else:
                self.data.append(new_val)
            self.write_count += 1
        self.size = max_len
        print("Выполнено сложение списков")
        return True

    def sub_list(self, other_list):
        if isinstance(other_list, CustomList):
            other_data = other_list.data
            other_length = other_list.size
        else:
            other_data = other_list
            try:
                other_length = len(other_data)
            except TypeError:
                print("Provided other_list is not a list or CustomList")
                return False

        max_len = max(self.size, other_length)
        for i in range(max_len):
            x = self.data[i] if i < self.size else 0
            y = other_data[i] if i < other_length else 0
            new_val = x - y
            if i < self.size:
                self.data[i] = new_val
            else:
                self.data.append(new_val)
            self.write_count += 1
        self.size = max_len
        print("Выполнено вычитание списков")
        return True


list1 = CustomList(5)
list1.print_list()

print("Читаем элемент с индексом 2:", list1.get(2))
list1.set(2, 50)
list1.print_list()
list1.add_value(25)
list1.print_list()
list2 = CustomList(3)
list2.print_list()
list1.add_list(list2)
list1.print_list()
list1.sub_list([10, 20, 30, 40])
list1.print_list()

print(f"Счётчик чтений: {list1.read_count}, Счётчик записей: {list1.write_count}")
