list = [1,2,3,4,5,23,35,12,67,84,23,78,65,23,85,68]

y=list[0]
for x in list:
    if x > y:
        y=x

print(f"The Largest number in list is: {y}")
