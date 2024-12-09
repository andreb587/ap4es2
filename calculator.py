class MemoryCalculator:
  
  #Construtor
    def __init__(self, save_last_sum=False):
        self._total = 0

    def add(self, number):
        self._total += number

    def subtract(self, number):
        self._total -= number

    def multiply(self, number):
        self._total *= number

    def total(self):
        return self._total