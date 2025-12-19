students = {
    1:  {"first_name": "Rahul",  "surname": "Sharma"},
    2:  {"first_name": "Amit",   "surname": "Verma"},
    3:  {"first_name": "Neha",   "surname": "Gupta"},
    4:  {"first_name": "Rahul",  "surname": "Singh"},
    5:  {"first_name": "Priya",  "surname": "Mehta"},
    6:  {"first_name": "Amit",   "surname": "Kumar"},
    7:  {"first_name": "Sonal",  "surname": "Patel"},
    8:  {"first_name": "Vikas",  "surname": "Yadav"},
    9:  {"first_name": "Neha",   "surname": "Malhotra"},
    10: {"first_name": "Rohit",  "surname": "Agarwal"},
    11: {"first_name": "Ankit",  "surname": "Jain"},
    12: {"first_name": "Pooja",  "surname": "Bansal"},
    13: {"first_name": "Rohit",  "surname": "Khanna"},
    14: {"first_name": "Suresh", "surname": "Iyer"},
    15: {"first_name": "Kiran",  "surname": "Reddy"},
    16: {"first_name": "Amit",   "surname": "Chopra"},
    17: {"first_name": "Priya",  "surname": "Kapoor"},
    18: {"first_name": "Vikas",  "surname": "Mishra"},
    19: {"first_name": "Neha",   "surname": "Arora"},
    20: {"first_name": "Rahul",  "surname": "Meena"}
}

unique_students = {}

for student_id, info in students.items():
    first = info["first_name"]
    last = info["surname"]

    if first not in unique_students:
        unique_students[first] = info
    else:
        # Duplicate first name with different surname found
        if unique_students[first]["surname"] != last:
            print(f"Duplicate found: {first} {last}")

print("\nStudents after removing duplicates:\n")
for name, details in unique_students.items():
    print(f"{name} {details['surname']}")

