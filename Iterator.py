import csv

class SimpleIterator:
    def __init__(self, path: str) -> None:
        self.path = path
        self.path_list, self.annotations = self.load_paths()
        self.lim = len(self.path_list)
        self.counter = 0

    def __iter__(self) -> 'SimpleIterator':
        return self

    def __next__(self) -> tuple:
        if self.counter < self.lim:
            next_element = (self.path_list[self.counter], self.annotations[self.counter])
            self.counter += 1
            return next_element
        else:
            raise StopIteration

    def load_paths(self) -> tuple:
        path_list = []
        annotations = []
        with open(self.path, mode='r', encoding='utf-8') as file:
            reader  = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    path_list.append(row[0])
                    annotations.append(row[1])
        return path_list, annotations