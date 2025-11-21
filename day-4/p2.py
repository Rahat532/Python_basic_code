# create a dictonary to record the student score and  avrage the scores
student_results= [
    {
        "name":"john",
        "Grade":85,
    },
    {
        "name":"Alice",
        "Grade":90,
    },
    {
        "name":"Bob",
        "Grade":78,
    },
]
total_score=0
mumber_of_students=0
for student in student_results:
    mumber_of_students +=1
for student in student_results:
    total_score += student["Grade"]
average_score= total_score / mumber_of_students
print(f"the avrage score of the students is : {average_score}")