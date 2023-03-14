from typing import List

class Vector():
    values: List[List[float]]
    shape: tuple
    
    def __init__(self, values):
        self.values = values
        self.shape = None

    def dot(self, v: "Vector"):
        for index in range(shape)