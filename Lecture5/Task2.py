names = []
while True:
    name = input("Enter name:- ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.append(name)

unique_names = set(names)

print("The list of unique names are:-")
for i in unique_names:
    print(i)