
n=int(input("enter:"))
total=0
positive_values=0
negative_values=0
zero_value=0
for i in range(n):
    a=int(input())
    total+=a
    if a>0:
        positive_values+=1
    elif a<0:
        negative_values+=1
    else:
        zero_value+=1
print(f"Positive Count: {positive_values}")
print(f"Negative Count: {negative_values}")
print(f"Zero Count: {zero_value}")
print(f"Total: {total}")