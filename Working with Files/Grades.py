Total_score = 0
Student_count=0
with open("Grades.txt","r") as file:
    for line in file:
        name, score = line.split(",")
        Total_score = Total_score + float(score)
        Student_count +=1
Average_score=Total_score/Student_count
print(Average_score, Student_count)
with open("Average_grade.txt", "w") as output:
    output.write(f"Average marks of {Student_count} Students is {Average_score}")
print ("Result Written to File.")