student1 = {
    "name": "Benastone Waithaka",
    "adm_no": "CIM/00089/024",
    "subjects": {
        "Data structures": "B",
        "Algorithms": "A",
        "Databases": "B"
    },
    "next": None
}

student2 = {
    "name": "Alice Wanjiru",
    "adm_no": "CIM/00090/024",
    "subjects": {
        "Data structures": "A",
        "Algorithms": "C",
        "Databases": "A"
    },
    "next": None
}

student3 = {
    "name": "Angela Liam",
    "adm_no": "CIM/00091/024",
    "subjects": {
        "Data structures": "B",
        "Algorithms": "A",
        "Databases": "C"
    },
    "next": None
}

student1["next"] = student2
student2["next"] = student3

head = student1
current = head

while current is not None:
    print("Name:", current["name"])
    print("Admission Number:", current["adm_no"])
    print("Subjects and Grades:")
    for subject, grade in current["subjects"].items():
        print("   ", subject, ":", grade)
    print()  # space between students
    current = current["next"]
