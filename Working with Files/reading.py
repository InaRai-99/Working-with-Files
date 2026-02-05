with open("data.txt", "r") as file:
    content = file.read()
print(content)
print ("-----------------")
print("-----below reading line by line")

with open ("data.txt", "r")as file:
    i=1
    for line in file:
        print(f"{i} : {line}")
        i=i+1
        