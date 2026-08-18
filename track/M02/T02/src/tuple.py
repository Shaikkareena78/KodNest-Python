name = input()
course = input()
score = int(input())

# Create the tuple
student_record = (name, course, score)

# Unpack the tuple
name = student_record[0]
course = student_record[1]
score = student_record[2]

# Display the unpacked values
print(f"Name: {name}")      
print(f"Course: {course}")
print(f"Score: {score}")    