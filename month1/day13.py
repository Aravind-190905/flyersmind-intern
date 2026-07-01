
import json

with open("file.json", "r") as f:
    student = json.load(f)

print(student)