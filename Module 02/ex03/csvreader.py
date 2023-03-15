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
        self.file = open(self.filename)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

    def parse_line(self, line: str):
        return line.split(self.sep)

    def get_data(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        cols = -1
        if self.header:
            cols = len(self.get_header(self.file))
        self.file.seek(self.skip_top)
        data = self.file.readlines()
        print(data)


    def get_header(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if not self.header:
            return False
        self.file.seek(0)
        return self.parse_line(self.file.readline())


if __name__ == "__main__":
    with CsvReader('no_header_hurricanes.csv') as file:
        print(type(file))
        print(file.get_data())
        print(file.get_header())
    print("---------------------------")
    """    with CsvReader('header_hurricanes.csv') as file:
        print(file.get_data())
        print(file.get_header())
    print("---------------------------")
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")
"""