# Info util https://ellibrodepython.com/context-managers-python
# Source of csv example: https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html

class CsvReader():
    def __init__(self, filename=None, sep=', ', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.file = open(self.filename)
        except FileNotFoundError:
            self.file = None
            return None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self is not None and self.file:
            self.file.close()

    def parse_line(self, line: str):
        return line.split(self.sep)
    
    def parse_data(self, data: list):
        new_data = []
        for line in data:
            if line[-1] == '\n':
                line = line[:-1]
            new_data.append(self.parse_line(line))
        return new_data

    def get_data(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        if not self.file:
            return None
        cols = -1
        if self.header:
            cols = len(self.get_header())
            self.skip_top += 1
        self.file.seek(0)
        data = self.file.readlines()
        for i in range(0, self.skip_top):
            data.remove(data[0])
        for i in reversed(range(0, self.skip_bottom)):
            data.remove(data[len(data) - 1])
        data = self.parse_data(data)
        return data


    def get_header(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """ 
        if not self.file:
            return None
        if not self.header:
            return False
        self.file.seek(0)
        return self.parse_line(self.file.readline())


if __name__ == "__main__":
    with CsvReader('no_header_hurricanes.csv') as file:
        print(type(file))
        print("HEADER\n", file.get_header())
        print("DATA\n", file.get_data())
    print("---------------------------")
    with CsvReader('header_hurricanes.csv', header = True, skip_top=1, skip_bottom=2) as file:
        print("HEADER\n", file.get_header())
        print("DATA\n", file.get_data())
    print("---------------------------")
    with CsvReader('bad.csv') as file:
        print(file)
        if file == None:
            print("File is corrupted")