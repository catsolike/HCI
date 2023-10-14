class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating


    def __eq__(self, other):
        if (isinstance(other, (int, ChessPlayer))):
            if(self.rating == other):
                return True
            else:
                return False
        else:
            return "Невозможно выполнить сравнение"


    def __gt__(self, other):
        if (isinstance(other, int)):
            return self.rating > other.rating
        elif(isinstance(other, ChessPlayer)):
            return self.rating > other.rating
        else:
            return "Невозможно выполнить сравнение"


    def __lt__(self, other):
        if (isinstance(other, int)):
            return self.rating < other.rating
        elif(isinstance(other, ChessPlayer)):
            return self.rating < other.rating
        else:
            return "Невозможно выполнить сравнение"
        

magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000) # False
print(ian == 2789) # True
print(magnus == ian) # False
print(magnus == [1, 2]) # печатает "Невозможно выполнить сравнениe"
print(magnus > 2) # True
print(magnus > 5000) # False
print(magnus > ian) # True
print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"
print(magnus < ian) # False
print(magnus < 2) # False
print(magnus < 5000) # True
print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"
print(2 > magnus) # False
print(5000 > magnus) # True