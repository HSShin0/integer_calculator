from abc import ABC, abstractmethod

class Calculator(ABC):

    @abstractmethod
    def operate(self, x:int, y:int) -> int:
        pass  


class Adder(Calculator):

    def operate(self, x:int, y:int) -> int:
        pass


class Subtractor(Calculator):

    def operate(self, x:int, y:int) -> int:
        pass


class Multiplier(Calculator):

    def operate(self, x:int, y:int) -> int:
        pass


class Divider(Calculator):

    def operate(self, x:int, y:int) -> int:
        pass
