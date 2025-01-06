student_heights = input("Input a list of student heights: ").split()
print(type(student_heights))
for n in range(0, len(student_heights)): 
    student_heights[n] = int(student_heights[n]) #converting each inputs to int from str

print(student_heights)
s = 0
count = 0
for h in student_heights:
    count += 1
print("\nTotal number of students: ", count)  # number of items in the list

for h in student_heights:
    s += h
print(f"\nSum of all students heights: {s}\n")  # the sum value of heights

avg_height = round(s / count)
print("The average height of student is: ", avg_height)
