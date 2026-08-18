student_count=int(input("enter no.of students:"))
total_marks=0
passed_count=0
failed_count=0
batch=True
for i in range(student_count):
    mark=int(input("enter the marks:"))
    total_marks+=mark
    if mark>=40:
        passed_count+=1
    else:
        failed_count+=1
print("Total Marks:", total_marks)
print("Passed Students:", passed_count)
print("Failed Students:", failed_count)
if failed_count==0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Need improvement")
