# Print something a specified number of times
for i in range(3):
      print("go to sleep")

# Print out all items in a list
items = ['go', 'to', 'sleep']

for i in items:
    print(i)

# Break ends loop
for i in items:
    print(i)
    if i == 'to':
        break

# Skip over items (skip over word 'to')
for i in items:
    if i == 'to':
        continue
    print(i)


# while loops
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
    students_in_poetry.append(all_students.pop())
    print(students_in_poetry)

students_in_poetry = []

i = 0
while i < 3:
    students_in_poetry.append(all_students[i])
    print(students_in_poetry)
    i += 1


# Loop comprehension
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

usernames = [i for i in words if i[0] == '@']
print(usernames)

message = [i + " Please follow!" for i in usernames]
print(message)

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [i*9/5+32 for i in celsius]
print(fahrenheit)




