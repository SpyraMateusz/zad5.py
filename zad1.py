class UpperCaseDescriptor:
    def __set__(self, instance, value):
        if not value.isupper():
            raise ValueError("Name must be fully uppercase.")
        instance._name = value

    def __get__(self, instance, owner):
        return instance._name

class Person:
    def __init__(self, name):
        self._name = name

    name = UpperCaseDescriptor()

# Przykłady użycia:
person1 = Person("JOHN")
print(person1.name)  # Output: JOHN

# Próba przypisania wartości z małą literą (spowoduje błąd ValueError)
try:
    person1.name = "John"
except ValueError as e:
    print(f"Error: {e}")

# Próba przypisania wartości z dużymi literami (poprawne)
person1.name = "DOE"
print(person1.name)  # Output: DOE