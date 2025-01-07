student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

l = student_scores
m = 0
for i in l:
    if i > m:
        m = i
    else:
        m = m

print(f"The highest score in the class is: {m}")
