# Using context manager to write to a file

with open("Example 1.txt", "w") as file:
    file.write("Hello, This is a simple file write example. This doesn't contain anything else.")
    