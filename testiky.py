student = {"jméno": "Jan", "příjmení": "Novák", "věk": 20}

student["obor"] = "Informatika"
student["kontakt"] = {"email": "jan.novak@gmail.com", "mobil": "+420777666555"}

print(student.get("pohlaví"))
print(student.get("kontakt").get("mobil"))
print(student.keys())

print(len(student.keys()), len(student.values()))
