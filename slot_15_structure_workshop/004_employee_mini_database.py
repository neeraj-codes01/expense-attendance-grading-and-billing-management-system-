employees=[
    {"name":"asha","id":101,"department":"sales","salary":45000},
    {"name":"neeraj","id":102,"department":"it","salary":60000},
    {"name":"paras","id":103,"department":"sales","salary":470000},
]
departments=set()
for emp in employees:
    print(emp["name"],"-",emp["department"],"-rs",emp["salary"])
    departments.add(emp["department"])
print("unique departments:",departments)
