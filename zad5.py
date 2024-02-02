class PositiveIntegerDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance, f"_{self.name}", None)

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{self.name} must be a positive integer.")
        setattr(instance, f"_{self.name}", value)

class MyClass:
    my_attribute = PositiveIntegerDescriptor()

# Przykład użycia:
obj = MyClass()
obj.my_attribute = 42  # dobra wartość
print(obj.my_attribute)  # Output: 42

# Próba przypisania wartości nie będącej liczbą całkowitą lub mniejszą bądź równą zero powinno (spowoduje błąd ValueError)
try:
    obj.my_attribute = "invalid"
except ValueError as e:
    print(f"Error: {e}")

try:
    obj.my_attribute = 0
except ValueError as e:
    print(f"Error: {e}")