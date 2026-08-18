n = int(input("enter the number:"))
scores = []
highest_score=0
total=0
for i in range(n):
   items=int(input())
   scores.append(items)
   total+=items
print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))
print("Total Score:", total)
search_score=int(input())
if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")