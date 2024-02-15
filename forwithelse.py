numbers = [1, 2, 6, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Found 6!")
        break
    print(num)
else:
    print("Loop completed without finding 6.")
