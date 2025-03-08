# 1. Creating a Dictionary with at least 5 key-value pairs (Student ID and Name)
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eva"
}
#1.1 Adding values in dictionary
students[106] = "Frank"
students[107] = "Grace"
print("-----ADDING VALUES-----")
print("Dictionary after adding values:", students)

# 1.2 Updating values in dictionary
students[103] = "Chloe"
print("-----UPDATING VALUES-----")
print("Dictionary after updating value of key 103:", students)

# 1.3 Accessing a value in dictionary
print("-----ACCESSING VALUES-----")
print("Student with ID 102:", students[102])

# 1.4 Creating a nested dictionary
nested_students = {
    "Class A": {201: "John", 202: "Emma"},
    "Class B": {203: "Olivia", 204: "Liam"},
}
print("-----NESTED LOOP-----")
print("Nested Dictionary:", nested_students)

# 1.5 Accessing values of nested dictionary
print("Students in Class A:", nested_students["Class A"])
print("Student with ID 201 in Class A:", nested_students["Class A"][201])

# 1.6 Printing keys present in dictionary
print("-----KEYS-----")
print("Keys in students dictionary:", students.keys())
print("Keys in nested_students dictionary:", nested_students.keys())

# 1.7 Deleting a value from a dictionary
del students[104]
print("-----VALUES-----")
print("Dictionary after deleting key 104:", students)
