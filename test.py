# numbers = {'x': 1,'y': 2,'z':3}
# print({**numbers})

# s = "This is a common interview question"

# mx = '', 0
# for i in s:
#     if ch.get(i, 0) == 0 and i != ' ':
#         ch[i] = 1
#     elif ch.get(i, 0) != 0 and i != ' ':
#         ch[i] += 1

# for k, v in ch.items():
#     if v > mx[1]:
#         mx = k, v

# print(mx)


# class Point:
#     color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point ({self.x} , {self.y})")

#     def __str__(self):
#         return f"Point ({self.x} , {self.y})"

#     def __eq__(self, value):
#         return self.x == value.x and self.y == value.y

#     def __add__(self , other):
#         return Point(self.x+other.x , self.x , other.y)


# Point.color = "yellow"
# point = Point(1, 2)
# other = Point(1, 2)
# point.draw()
# print(point + other)


# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self, price):
#         if price < 0:
#             raise ValueError("Value cannot negative")
#         self.__price = price


# pro = Product(10)
# print(pro.price)
# pro.price = 5
# print(pro.price)

# mov = [
#     {"id": 1, "title": "I love you Fatoomty"},
#     {"id": 2, "title": "I love you Zozy"}
# ]

# data = json.dumps(mov)
# print(data)
# Path("mov.json").write_text(data)
# print(Path("mov.json").read_text())
# print(data[0]["title"])

# from pathlib import Path
# import json
# import sqlite3
# data = json.loads(Path("mov.json").read_text())

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "insert into Mov values(? , ?)"
#     for mov in data:
#         conn.execute(command , tuple(mov.values()))
#     conn.commit()


# from datetime import datetime
# import time
# dt = datetime(2003, 3, 25)
# dt1 = datetime.now()
# dt2 = datetime.strptime("2003/03/25", "%Y/%m/%d")
# dt3 = datetime.fromtimestamp(time.time())
# print(dt1)
# print(f"{dt2.year}/{dt2.month}/{dt2.day}")
# print(dt3.strftime("%Y/%m"))

# import random
# import string
# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1, 2, 3, 4]))
# print(random.choices([1, 2, 3, 4], k=2))
# print("".join(random.choices(string.ascii_letters +
#       string.digits + string.hexdigits, k=8)))

# number = [1, 2, 3, 4]
# random.shuffle(number)
# print(number)

# import webbrowser
# webbrowser.open("codeforces.com")


import requests
res = requests.get("https://google.com")
print(res)
