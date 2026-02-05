# Reading file line by line

with open("Example 1.txt", "r") as file:
    for line in file:
        print(line.strip())