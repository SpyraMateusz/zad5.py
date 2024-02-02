class ValidationDescriptor:
    def __init__(self, name):
        self.name = name

    def __set_name__(self, owner, name):
        self.internal_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.internal_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than zero.")
        setattr(instance, self.internal_name, value)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    width = ValidationDescriptor("Width")
    height = ValidationDescriptor("Height")


rectangle = Rectangle(width=5, height=10)
print("Initial values:", rectangle.width, rectangle.height)

# Próba(spowoduje błąd ValueError)
try:
    rectangle.width = -3
except ValueError as e:
    print(f"Error: {e}")

# Sprawdzeni czy wartości zostały poprawnie ustawione
print("After invalid assignment:", rectangle.width, rectangle.height)