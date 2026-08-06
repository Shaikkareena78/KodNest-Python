number=int(input("enter the number:"))
word=input("enter:")
print("Numbers:")
for i in range(1, number+1):
    print(i)
print("Characters:")
for i in range(len(word)):
    print(word[i])