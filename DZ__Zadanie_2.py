
class ListManager:
    def init(self, size):
        self.list = [0] * size
        self.size = size
        self.write_count = 0
        self.read_count = 0

    def print_list(self):
        print(self.list)

    def get_write_count(self):
        return self.write_count

    def get_read_count(self):
        return self.read_count

    def set_value(self, index, value):
        if -100 <= value <= 100 and 0 <= index < self.size:
            self.list[index] = value
            self.write_count += 1
        else:
            print("Значение должно быть в диапазоне [-100, 100] и индекс должен быть в диапазоне [0, size-1]")

    def get_value(self, index):
        if 0 <= index < self.size:
            self.read_count += 1
            return self.list[index]
        else:
            print("Индекс должен быть в диапазоне [0, size-1]")
            return None

    def append(self, value):
        if -100 <= value <= 100:
            self.list.append(value)
            self.size += 1
            self.write_count += 1
        else:
            print("Значение должно быть в диапазоне [-100, 100]")

    def add_arrays(self, arr1, arr2):
        if len(arr1) == len(arr2):
            result = [a + b for a, b in zip(arr1, arr2)]
        else:
            result = [a + b for a, b in zip(arr1 + [0] * (len(arr2) - len(arr1)), arr2 + [0] * (len(arr1) - len(arr2)))]
        return result

    def sub_arrays(self, arr1, arr2):
        if len(arr1) == len(arr2):
            result = [a - b for a, b in zip(arr1, arr2)]
        else:
            result = [a - b for a, b in zip(arr1 + [0] * (len(arr2) - len(arr1)), arr2 + [0] * (len(arr1) - len(arr2)))]
        return result