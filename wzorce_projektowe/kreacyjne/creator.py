from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        results = f"Creator: The same creator's code has just worked with {product.operation()}"
        return results


class ConcreteCreator1(Creator):

    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self):
        return ConcrteProduct2()


class Product(ABC):

    @abstractmethod
    def operation(self):
        pass


class ConcreteProduct1(Product):

    def operation(self):
        return "{Result of the ConcrteProduct1}"


class ConcrteProduct2(Product):

    def operation(self):
        return "{Result of the ConcrteProduct2}"


def client_code(creator: Creator):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
    f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())