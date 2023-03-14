
class GotCharacter():
    first_name: str
    is_alive: bool
    
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Bolton(GotCharacter):
    """Bolton is the most evil house"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Bolton"
        self.house_words = "Our Blades Are Sharp"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
