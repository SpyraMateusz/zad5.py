class LazinessDescriptor:
    def __init__(self, threshold=10):
        self.threshold = threshold

    def __get__(self, instance, owner):
        return f"{instance.name} is {'lazy' if instance.study_hours < self.threshold else 'hardworking'}."

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Study hours cannot be negative.")
        instance._study_hours = value

class Student:
    laziness_status = LazinessDescriptor()

    def __init__(self, name, study_hours):
        self.name = name
        self._study_hours = study_hours

    @property
    def study_hours(self):
        return self._study_hours

# Przykłady użycia:
student1 = Student("Alice", 5)
print(student1.laziness_status)  # Output: Alice is lazy.

student2 = Student("Bob", 15)
print(student2.laziness_status)  # Output: Bob is hardworking.

# Próba ustawienia ujemnej liczby godzin (spowoduje błąd ValueError)
try:
    student2.study_hours = -5
except ValueError as e:
    print(f"Error: {e}")