
# if 

if True :
    print("yes value is true")

if 3 > 2 :
    print("if block")
    if 4 > 3 and 5 > 3:
        print("nested if ")

if 2 > 3:
    print("printing is statement")
else :
    print("printing else statement")


if 3 > 4:
    print("1")
elif 3 > 5 :
    print("2")
elif 2 > 1:
    print("3")
else :
    print("none of these satisfied")


i = 0 

while(i < 10 ):
    print(i , end=" ")
    i = i + 1

print("end")

a = [2, 4, 6, 8, 10]

for item   in a:
    print(item )

for i in range(5):
    print(i)
else:
    print("Loop finished")


for item   in a:
    if item == 4:
        continue
    print(item )

for item   in a:
    if item == 4:
        break
    print(item )


student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}

for key in student:
    print(key , student[key])

for value in student.values():
    print(value)

for key, value in student.items():
    if key == "age":
        print("Age found:", value)