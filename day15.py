import json

class Student:
    def __init__(self, name, roll, age):
        self.name = name
        self.roll = roll
        self.age = age

    def display(self):
        print(f"{self.roll} | {self.name} | {self.age}")

    def to_dict(self):
        return self.__dict__


class System:
    def __init__(self):
        self.students = []
        self.load()

    def load(self):
        try:
            with open("students.json", "r") as f:
                data = json.load(f)
                self.students = [Student(**i) for i in data]
        except:
            self.students = []

    def save(self):
        with open("students.json", "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add(self):
        name = input("Name: ")
        roll = int(input("Roll: "))
        age = int(input("Age: "))
        self.students.append(Student(name, roll, age))
        self.save()

    def view(self):
        if not self.students:
            print("No students")
        for s in self.students:
            s.display()

    def update(self):
        roll = int(input("Roll to update: "))
        for s in self.students:
            if s.roll == roll:
                s.name = input("New Name: ")
                s.age = int(input("New Age: "))
                self.save()
                return
        print("Student not found")

    def delete(self):
        roll = int(input("Roll to delete: "))
        for s in self.students:
            if s.roll == roll:
                self.students.remove(s)
                self.save()
                return
        print("Student not found")


system = System()

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        system.add()
    elif ch == "2":
        system.view()
    elif ch == "3":
        system.update()
    elif ch == "4":
        system.delete()
    elif ch == "5":
        break
    else:
        print("Invalid choice")