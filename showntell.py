


# Create a Person class with properties for name and age.Implement a function in the Person class to print out the person's details.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example usage
person1 = Person("John Doe", 30)
person1.print_details()
