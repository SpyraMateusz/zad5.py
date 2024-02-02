def logged(cls):
    class LoggedClass(cls):
        def __setattr__(self, name, value):
            descriptor = getattr(self.__class__, name, None)
            if isinstance(descriptor, (UpperCaseDescriptor, LazinessDescriptor)):
                print(f"Attempted to set value of {name} to {value}")
            super().__setattr__(name, value)

    return LoggedClass

class UpperCaseDescriptor:
    def __set__(self, instance, value):
        if not value.isupper():
            raise ValueError("Name must be fully uppercase.")
        instance._name = value

    def __get__(self, instance, owner):
        return instance._name

class LazinessDescriptor:
    def __init__(self, threshold=10):
        self.threshold = threshold

    def __get__(self, instance, owner):
        return f"{instance.name} is {'lazy' if instance.study_hours < self.threshold else 'hardworking'}."

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Study hours cannot be negative.")
        instance._study_hours = value

@logged
class Person:
    def __init__(self, name, study_hours):
        self.name = name
        self._study_hours = study_hours

    name = UpperCaseDescriptor()
    study_hours = LazinessDescriptor()

# Przykład użycia:
person = Person("John", 8)
person.name = "Bob"  # Output: Attempted to set value of name to Bob
person.study_hours = 5  # Output: Attempted to set value of study_hours to 5