# Check if a specific word exists in the file

with open("Example 1.txt", "r") as file:
    content = file.read()
    if "appended" in content:
        print("The word 'appended' was found.")
