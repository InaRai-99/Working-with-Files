#Write a Python script that asks the user for a single line of text. 
# #The script should then append this line, along with a timestamp, to a file named log.txt.
# #The script should not overwrite the file if it already exists.

from datetime import datetime
with open ("log.txt", "a") as file:
    name = input ("Enter your name")
    t =  datetime.now()
    file.write(f"{name} : {t} \n")